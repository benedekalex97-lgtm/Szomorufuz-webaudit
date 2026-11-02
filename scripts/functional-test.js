// Funkcionális ellenőrzések (csak olvasó, űrlapot NEM küld el):
// mobilmenü nyitása, árajánlatkérő űrlap felépítése mobilon, süti-sáv, billentyűzetes fókusz.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const BASE = 'https://www.budapest-temetkezes.hu/';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const browser = await chromium.launch();
  const res = {};
  const mob = await browser.newContext({
    viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'hu-HU',
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
  });
  let page = await mob.newPage();
  await page.goto(BASE, { waitUntil: 'load', timeout: 60000 });
  await sleep(2000);
  // 1) Mobilmenü
  const toggle = page.locator('text=Menü').first();
  res.menuToggleFound = await toggle.count();
  if (res.menuToggleFound) {
    const tag = await toggle.evaluate((el) => ({ tag: el.tagName, role: el.getAttribute('role'), aria: el.getAttribute('aria-expanded'), href: el.getAttribute('href'), html: el.outerHTML.slice(0, 300) }));
    res.menuToggle = tag;
    await toggle.click();
    await sleep(1200);
    await page.screenshot({ path: path.join(ROOT, 'screenshots/mobile-menu-open.png') });
    res.menuItemsVisible = await page.evaluate(() => [...document.querySelectorAll('a')].filter((a) => { const r = a.getBoundingClientRect(); return r.top >= 0 && r.top < 844 && r.width > 0 && getComputedStyle(a).visibility !== 'hidden'; }).map((a) => a.innerText.trim()).filter(Boolean).slice(0, 40));
  }
  // 2) Süti-sáv lefedettsége mobilon
  await page.goto(BASE, { waitUntil: 'load' });
  await sleep(1500);
  res.cookieBanner = await page.evaluate(() => {
    const c = document.querySelector('#cookie_policy');
    if (!c) return null;
    const r = c.getBoundingClientRect();
    const mk = document.querySelector('#marketing_statistics');
    return { heightPx: Math.round(r.height), viewportShare: Math.round((r.height / window.innerHeight) * 100) + '%', marketingPrechecked: mk ? mk.checked : null, hasRejectButton: /elutasít|nem fogad/i.test(c.innerText) };
  });
  // 3) Árajánlat űrlap felépítése mobilon
  await page.goto(BASE + 'arajanlat-keres-itt/', { waitUntil: 'load' });
  await sleep(2000);
  // süti-sáv elrejtése csak a képernyőképhez (kattintás nélkül, nem tárol hozzájárulást)
  await page.evaluate(() => { const c = document.querySelector('#cookie_policy'); if (c) c.style.display = 'none'; });
  res.quoteForm = await page.evaluate(() => {
    const f = document.querySelector('form[id^=form_]');
    if (!f) return null;
    const r = f.getBoundingClientRect();
    const labels = [...f.querySelectorAll('label, .form_label, td, th, .label')].map((l) => l.innerText.trim()).filter((t) => t && t.length < 120);
    const inputs = [...f.querySelectorAll('input:not([type=hidden]), textarea, select')].map((i) => ({ type: i.type, name: i.name, required: i.required || i.getAttribute('aria-required') === 'true', autocomplete: i.autocomplete || null, inputmode: i.inputMode || null }));
    const submit = f.querySelector('button, input[type=submit], a.button, .send');
    return {
      topPx: Math.round(r.top + window.scrollY), heightPx: Math.round(r.height), inputCount: inputs.length,
      requiredAttr: inputs.filter((i) => i.required).length, emailTypeFields: inputs.filter((i) => i.type === 'email').length, telTypeFields: inputs.filter((i) => i.type === 'tel').length,
      autocompleteSet: inputs.filter((i) => i.autocomplete && i.autocomplete !== 'on').length, starMarkers: (f.innerText.match(/\*/g) || []).length,
      submitText: submit ? (submit.innerText || submit.value || '').trim() : null,
      labelSample: [...new Set(labels)].slice(0, 45),
    };
  });
  await page.evaluate(() => { const f = document.querySelector('form[id^=form_]'); if (f) f.scrollIntoView(); });
  await sleep(500);
  await page.screenshot({ path: path.join(ROOT, 'screenshots/mobile-arajanlat-form.png') });
  // 4) Billentyűzetes fókusz látható-e (desktop)
  const desk = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'hu-HU' });
  page = await desk.newPage();
  await page.goto(BASE, { waitUntil: 'load' });
  await sleep(1500);
  const foci = [];
  for (let i = 0; i < 8; i++) {
    await page.keyboard.press('Tab');
    foci.push(await page.evaluate(() => {
      const el = document.activeElement; const st = getComputedStyle(el);
      return { tag: el.tagName, text: (el.innerText || '').trim().slice(0, 30), outline: st.outlineStyle + ' ' + st.outlineWidth, boxShadow: st.boxShadow };
    }));
  }
  res.keyboardFocus = foci;
  res.skipLink = await page.evaluate(() => !![...document.querySelectorAll('a')].find((a) => /tartalomra|ugrás|skip/i.test(a.innerText)));
  await page.keyboard.press('Tab');
  await page.screenshot({ path: path.join(ROOT, 'screenshots/desktop-keyboard-focus.png'), clip: { x: 0, y: 0, width: 1440, height: 450 } });
  fs.writeFileSync(path.join(ROOT, 'data/functional-test.json'), JSON.stringify(res, null, 1));
  console.log(JSON.stringify(res, null, 1));
  await browser.close();
})();
