// 2. lépés – galériák nagy felbontású képeinek feltérképezése.
// A galéria-bélyegképek kattintásra (xajax_popupGallery) töltik be a nagy képet.
// A szkript minden bélyegképre kattint, és rögzíti a böngésző által ténylegesen
// letöltött képeket. Csak olvasó: nem küld űrlapot, nem fogad el sütit.
// Bemenet: data/images/refs.json · Kimenet: data/images/gallery.json
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const refs = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/images/refs.json'), 'utf8'));
  const pages = Object.keys(refs.gallery_pages);
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'hu-HU' });
  const out = { pages: {}, large: {} };
  for (const url of pages) {
    const page = await ctx.newPage();
    const seen = new Set();
    page.on('response', (r) => {
      const ct = r.headers()['content-type'] || '';
      if (ct.startsWith('image/') && r.status() === 200) seen.add(r.url());
    });
    await page.goto(url, { waitUntil: 'load', timeout: 60000 });
    await sleep(1500);
    // süti-sáv elrejtése kattintás nélkül (nem ad hozzájárulást)
    await page.evaluate(() => { const c = document.querySelector('#cookie_policy'); if (c) c.style.display = 'none'; });
    const thumbs = await page.$$('a.piccont[onclick*="popupGallery"]');
    const items = [];
    for (let i = 0; i < thumbs.length; i++) {
      const before = new Set(seen);
      const meta = await thumbs[i].evaluate((a) => ({ onclick: a.getAttribute('onclick'), title: a.getAttribute('title'), thumb: (a.querySelector('img') || {}).src }));
      try {
        await thumbs[i].scrollIntoViewIfNeeded();
        await thumbs[i].click({ timeout: 5000 });
      } catch (e) { items.push({ ...meta, error: String(e).slice(0, 120) }); continue; }
      await sleep(1800);
      const shown = await page.evaluate(() => {
        const imgs = [...document.querySelectorAll('#lightview1 img, #lightview2 img, .lightview img, [id^=lightview] img, .popup img')];
        return imgs.filter((im) => im.naturalWidth > 150).map((im) => ({ src: im.src, w: im.naturalWidth, h: im.naturalHeight }));
      });
      const newly = [...seen].filter((u) => !before.has(u));
      items.push({ ...meta, shown, newly });
      for (const s of shown) out.large[s.src] = { w: s.w, h: s.h, page: url, title: meta.title, thumb: meta.thumb };
      await page.keyboard.press('Escape');
      await page.evaluate(() => { ['lightview1', 'lightview2', 'lw_bg1', 'lw_bg2'].forEach((id) => { const e = document.getElementById(id); if (e) e.style.display = 'none'; }); });
      await sleep(600);
    }
    out.pages[url] = items;
    console.log(url, thumbs.length, 'large so far', Object.keys(out.large).length);
    await page.close();
    await sleep(1500);
  }
  fs.writeFileSync(path.join(ROOT, 'data/images/gallery.json'), JSON.stringify(out, null, 1));
  await browser.close();
})();
