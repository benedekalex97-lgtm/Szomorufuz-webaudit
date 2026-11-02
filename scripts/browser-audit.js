// Playwright alapú böngészős audit: képernyőképek 3 viewporton, konzolhibák,
// hibás erőforrások, vízszintes túlcsordulás, kis érintési célpontok, axe-core.
// Csak olvasó: űrlapot nem küld el.
// Futtatás: node scripts/browser-audit.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const AXE = fs.readFileSync(path.join(ROOT, 'tools/node_modules/axe-core/axe.min.js'), 'utf8');
const BASE = 'https://www.budapest-temetkezes.hu/';
const PAGES = {
  home: '',
  hamvasztas: 'hamvasztas-urnakiadas/',
  hamvasztasos: 'hamvasztasos-temetes/',
  koporsos: 'koporsos-temetes/',
  arajanlat: 'arajanlat-keres-itt/',
  arajanlatkeres: 'arajanlatkeres/',
  arlista: 'arlista/',
  elerhetoseg: 'elerhetoseg/',
  teendok: 'teendok-halaleset-utan/',
  iratok: 'szukseges-iratok/',
  tajekoztatas: 'tajekoztatas-keres/',
  gyik: 'gyakori-kerdesek/',
};
const VIEWPORTS = {
  mobile: { width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
  tablet: { width: 768, height: 1024, isMobile: true, hasTouch: true, deviceScaleFactor: 1 },
  desktop: { width: 1440, height: 900, isMobile: false, hasTouch: false, deviceScaleFactor: 1 },
};
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const browser = await chromium.launch();
  const out = {};
  fs.mkdirSync(path.join(ROOT, 'screenshots'), { recursive: true });
  for (const [vpName, vp] of Object.entries(VIEWPORTS)) {
    const ctx = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: vp.deviceScaleFactor,
      isMobile: vp.isMobile,
      hasTouch: vp.hasTouch,
      locale: 'hu-HU',
      userAgent: vp.isMobile
        ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
        : undefined,
    });
    for (const [name, rel] of Object.entries(PAGES)) {
      const page = await ctx.newPage();
      const rec = { console: [], pageErrors: [], failed: [], badStatus: [], dialogs: [] };
      page.on('console', (m) => { if (['error', 'warning'].includes(m.type())) rec.console.push(`${m.type()}: ${m.text()}`.slice(0, 400)); });
      page.on('pageerror', (e) => rec.pageErrors.push(String(e).slice(0, 400)));
      page.on('requestfailed', (r) => rec.failed.push(`${r.url()} — ${r.failure() && r.failure().errorText}`));
      page.on('response', (r) => { if (r.status() >= 400) rec.badStatus.push(`${r.status()} ${r.url()}`); });
      page.on('dialog', async (d) => { rec.dialogs.push(d.message()); await d.dismiss(); });
      const t0 = Date.now();
      try {
        await page.goto(BASE + rel, { waitUntil: 'load', timeout: 60000 });
      } catch (e) {
        rec.navError = String(e).slice(0, 300);
      }
      rec.loadMs = Date.now() - t0;
      await sleep(2500);
      const metrics = await page.evaluate(() => {
        const de = document.documentElement;
        const vw = window.innerWidth;
        const overflowEls = [];
        document.querySelectorAll('body *').forEach((el) => {
          const r = el.getBoundingClientRect();
          if (r.right > vw + 2 && r.width > 0 && getComputedStyle(el).position !== 'fixed') {
            overflowEls.push(`${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}${el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : ''} (${Math.round(r.right)}px)`);
          }
        });
        const small = [];
        document.querySelectorAll('a[href], button, input, select, textarea').forEach((el) => {
          const r = el.getBoundingClientRect();
          const st = getComputedStyle(el);
          if (r.width === 0 || r.height === 0 || st.visibility === 'hidden' || st.display === 'none') return;
          if (r.height < 24 || r.width < 24) small.push(`${el.tagName.toLowerCase()} "${(el.innerText || el.value || el.getAttribute('title') || '').trim().slice(0, 30)}" ${Math.round(r.width)}x${Math.round(r.height)}`);
        });
        const p = document.querySelector('#center p') || document.querySelector('p');
        const fs = p ? getComputedStyle(p).fontSize : null;
        const ff = p ? getComputedStyle(p).fontFamily : null;
        const lh = p ? getComputedStyle(p).lineHeight : null;
        const telVisible = [...document.querySelectorAll('a[href^="tel:"]')].map((a) => {
          const r = a.getBoundingClientRect();
          return { text: a.innerText.trim(), top: Math.round(r.top + window.scrollY), visibleAboveFold: r.top < window.innerHeight && r.bottom > 0 && r.width > 0 };
        });
        return {
          scrollWidth: de.scrollWidth, clientWidth: de.clientWidth, docHeight: de.scrollHeight,
          horizontalOverflow: de.scrollWidth > de.clientWidth + 1,
          overflowEls: overflowEls.slice(0, 15), overflowCount: overflowEls.length,
          smallTargets: small.slice(0, 25), smallTargetCount: small.length,
          bodyFontSize: fs, fontFamily: ff, lineHeight: lh,
          telLinks: telVisible,
          viewportMeta: (document.querySelector('meta[name=viewport]') || {}).content || null,
          menuVisible: !!document.querySelector('#menutop') && getComputedStyle(document.querySelector('#menutop')).display !== 'none',
          hamburger: !!document.querySelector('.menu-toggle, .hamburger, .navbar-toggle, #mobile-menu, .mobile-menu, [aria-label*="menü" i]'),
          cookieBanner: !!document.querySelector('[id*="cookie" i], [class*="cookie" i]'),
        };
      });
      rec.metrics = metrics;
      // Navigation timing / web vitals (labor jellegű)
      rec.timing = await page.evaluate(() => {
        const n = performance.getEntriesByType('navigation')[0];
        const lcp = performance.getEntriesByType('largest-contentful-paint');
        const res = performance.getEntriesByType('resource');
        return n ? {
          ttfb: Math.round(n.responseStart), dcl: Math.round(n.domContentLoadedEventEnd), load: Math.round(n.loadEventEnd),
          transferKB: Math.round((res.reduce((a, r) => a + (r.transferSize || 0), 0) + n.transferSize) / 1024),
          requests: res.length + 1,
        } : null;
      });
      // above-the-fold és teljes oldalas képernyőkép
      await page.screenshot({ path: path.join(ROOT, `screenshots/${vpName}-${name}-fold.png`) });
      if (['home', 'hamvasztas', 'koporsos', 'arajanlat', 'elerhetoseg', 'teendok', 'arlista', 'iratok'].includes(name)) {
        await page.screenshot({ path: path.join(ROOT, `screenshots/${vpName}-${name}-full.jpg`), fullPage: true, type: 'jpeg', quality: 60 });
      }
      if (vpName === 'desktop' || name === 'home' || vpName === 'mobile') {
        await page.addScriptTag({ content: AXE });
        rec.axe = await page.evaluate(async () => {
          const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'best-practice'] } });
          return r.violations.map((v) => ({ id: v.id, impact: v.impact, help: v.help, count: v.nodes.length, sample: v.nodes.slice(0, 3).map((n) => n.target.join(' ') + ' :: ' + (n.failureSummary || '').split('\n').slice(1, 2).join('')) }));
        });
      }
      out[`${vpName}:${name}`] = rec;
      console.log(vpName, name, rec.loadMs, 'ms', 'overflow=', metrics.horizontalOverflow, 'errors=', rec.console.length + rec.pageErrors.length, 'bad=', rec.badStatus.length);
      await page.close();
      await sleep(1500);
    }
    await ctx.close();
  }
  fs.writeFileSync(path.join(ROOT, 'data/browser-audit.json'), JSON.stringify(out, null, 1));
  await browser.close();
})();
