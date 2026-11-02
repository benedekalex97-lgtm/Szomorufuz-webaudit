"""1. lépés – képhivatkozások gyűjtése a publikus oldalakról (csak olvasás, késleltetéssel).

Források: <img src/srcset/data-src>, inline style és <style> url(), a href képfájlra,
og:image / ikonok, valamint a hivatkozott CSS-fájlokban lévő url()-ek.
Bemenet: data/crawl.json (a 2026-11-02-i audit oldallistája)
Kimenet: data/images/refs.json
"""
import json, re, sys, time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

ROOT_HOST = ('www.budapest-temetkezes.hu', 'budapest-temetkezes.hu')
DELAY = 1.2
IMG_EXT = re.compile(r'\.(jpe?g|png|gif|webp|svg|bmp|ico|avif)(\?|$)', re.I)
UA_DESKTOP = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36 (site-audit; read-only)'
UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 (site-audit; read-only)'

s = requests.Session()


def get(url, ua, tries=3):
    for i in range(tries):
        try:
            r = s.get(url, timeout=30, headers={'User-Agent': ua})
            return r
        except requests.RequestException:
            time.sleep(4 * (i + 1))
    return None


def norm(u):
    u = u.strip().strip('\'"')
    if not u or u.startswith('data:') or u.startswith('javascript'):
        return None
    return u


refs = {}   # abs_url -> {"pages": set, "contexts": set, "alts": set, "titles": set}


def add(url, page, ctx, alt=None, title=None):
    if not url:
        return
    r = refs.setdefault(url, {'pages': set(), 'contexts': set(), 'alts': set(), 'titles': set()})
    r['pages'].add(page); r['contexts'].add(ctx)
    if alt: r['alts'].add(alt.strip())
    if title: r['titles'].add(title.strip())


CSS_URL = re.compile(r'url\(\s*([^)]+?)\s*\)', re.I)


def scan_html(page_url, html, ua_tag):
    soup = BeautifulSoup(html, 'lxml')
    base = soup.find('base')
    base_url = base.get('href') if base and base.get('href') else page_url
    pg = page_url
    for img in soup.find_all('img'):
        for attr in ('src', 'data-src', 'data-original'):
            v = norm(img.get(attr) or '')
            if v: add(urljoin(base_url, v), pg, f'img{"-mobile" if ua_tag == "m" else ""}', img.get('alt'), img.get('title'))
        for attr in ('srcset', 'data-srcset'):
            for part in (img.get(attr) or '').split(','):
                v = norm(part.strip().split(' ')[0])
                if v: add(urljoin(base_url, v), pg, 'srcset', img.get('alt'))
    for el in soup.find_all(style=True):
        for m in CSS_URL.finditer(el['style']):
            v = norm(m.group(1))
            if v: add(urljoin(base_url, v), pg, 'inline-bg', None, el.get('title'))
    for st in soup.find_all('style'):
        for m in CSS_URL.finditer(st.get_text()):
            v = norm(m.group(1))
            if v and IMG_EXT.search(v): add(urljoin(base_url, v), pg, 'style-bg')
    for a in soup.find_all('a', href=True):
        if IMG_EXT.search(a['href']):
            add(urljoin(base_url, a['href']), pg, 'link-to-image', None, a.get('title'))
    for m in soup.find_all('meta', attrs={'property': re.compile('og:image')}):
        add(urljoin(base_url, m.get('content', '')), pg, 'og:image')
    for l in soup.find_all('link', rel=True):
        rel = ' '.join(l.get('rel'))
        if 'icon' in rel:
            add(urljoin(base_url, l.get('href', '')), pg, 'icon')
    css = [urljoin(base_url, l['href']) for l in soup.find_all('link', href=True)
           if 'stylesheet' in ' '.join(l.get('rel', [])) or l['href'].split('?')[0].endswith('.css')]
    galleries = re.findall(r"xajax_popupGallery\('([^']+)',\s*'(\d+)',\s*'(\d+)'", html)
    return css, galleries


def main():
    crawl = json.load(open('data/crawl.json'))
    pages = [u for u, p in crawl['pages'].items()
             if p.get('status') == 200 and '?' not in u and '+3630' not in u and not u.endswith('.xml')]
    pages.sort()
    css_files, gallery_pages = {}, {}
    for i, u in enumerate(pages):
        time.sleep(DELAY)
        r = get(u, UA_DESKTOP)
        if r is None or r.status_code != 200:
            print('SKIP', u, r and r.status_code, flush=True); continue
        css, gal = scan_html(u, r.text, 'd')
        for c in css: css_files.setdefault(c, set()).add(u)
        if gal: gallery_pages[u] = len(gal)
        print(i, len(refs), u, flush=True)
    # mobil sablon: főoldal + egy aloldal
    for u in pages[:1] + ['https://www.budapest-temetkezes.hu/koporsos-temetes/']:
        time.sleep(DELAY)
        r = get(u, UA_MOBILE)
        if r is not None and r.status_code == 200:
            css, gal = scan_html(u, r.text, 'm')
            for c in css: css_files.setdefault(c, set()).add(u + ' [mobil]')
    # CSS-fájlok url()-jei
    for c, srcpages in css_files.items():
        if urlparse(c).netloc not in ROOT_HOST:
            continue
        time.sleep(DELAY)
        r = get(c, UA_DESKTOP)
        if r is None or r.status_code != 200:
            continue
        for m in CSS_URL.finditer(r.text):
            v = norm(m.group(1))
            if v and IMG_EXT.search(v):
                add(urljoin(c, v), 'CSS: ' + c.split('?')[0].replace('https://www.budapest-temetkezes.hu/', ''), 'css-bg')
    out = {u: {k: sorted(v) for k, v in d.items()} for u, d in refs.items()}
    json.dump({'pages_scanned': len(pages), 'css_files': sorted(css_files), 'gallery_pages': gallery_pages, 'refs': out},
              open('data/images/refs.json', 'w'), ensure_ascii=False, indent=1)
    print('DONE refs', len(out), 'css', len(css_files), 'galleries', gallery_pages)


main()
