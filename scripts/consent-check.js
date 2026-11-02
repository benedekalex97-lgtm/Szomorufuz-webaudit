// Ellenőrzi, mely harmadik féltől származó követő kérések indulnak el
// MIELŐTT a látogató bármit kattintana a süti-sávon. Nem kattint, nem küld űrlapot.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'hu-HU' });
  const page = await ctx.newPage();
  const reqs = [];
  let total = 0;
  page.on('request', (r) => {
    total++;
    const u = r.url();
    if (!u.includes('budapest-temetkezes.hu')) reqs.push(u.split('?')[0] + (u.includes('?') ? '?…' : ''));
  });
  await page.goto('https://www.budapest-temetkezes.hu/', { waitUntil: 'load', timeout: 60000 });
  await new Promise((r) => setTimeout(r, 6000));
  const cookies = (await ctx.cookies()).map((c) => `${c.domain} ${c.name}`);
  const consentState = await page.evaluate(() => (window.dataLayer || []).filter((e) => e && (e[0] === 'consent' || (e.length && String(e[0]).includes('consent')))).map((e) => JSON.stringify(Array.from(e))));
  const title = await page.title();
  const bannerVisible = await page.evaluate(() => !!document.querySelector('#cookie_policy'));
  const out = { title, totalRequests: total, bannerVisible, thirdPartyRequestsBeforeConsent: [...new Set(reqs)], cookiesBeforeConsent: cookies, consentCommands: consentState };
  fs.writeFileSync(path.join(ROOT, 'data/consent-check.json'), JSON.stringify(out, null, 1));
  console.log(JSON.stringify(out, null, 1));
  await browser.close();
})();
