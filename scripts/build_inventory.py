"""Oldaltérkép (URL-leltár) és Lighthouse-összesítő generálása a nyers adatokból."""
import json, glob, os, collections
d = json.load(open('data/crawl.json'))
P = d['pages']; SM = set(d['sitemap_urls'])
B = 'https://www.budapest-temetkezes.hu'
groups = collections.OrderedDict([
    ('Főoldal és változatai', lambda u: u in ('/', '/?mobile=no', '/?mobile=1')),
    ('Szolgáltatások', lambda u: u.strip('/') in 'hamvasztasos-temetes koporsos-temetes hamvasztas-urnakiadas hamvak-hazavitele hamvasztas-menete hamvak-szorasa-temeto hamvak-szorasa-dunaba hamvak-temetese ravatalozo-terem polgari-bucsuztatas szocialis-temetes urnak sirjelzo textiliak temetkezesi-szolgaltata fiumei-uti-temeto hajos-emlekezes-napja'.split()),
    ('Ajánlatkérés, kedvezmények, kapcsolat', lambda u: u.strip('/') in 'arajanlat-keres-itt arajanlatkeres argarancia argarancia egyedi-kedvezmeny online-kedvezmeny tajekoztatas-keres visszajelzes-kuldese elerhetoseg hirlevel-feliratkozas uzenofal munkalehetoseg figyelem-'.split()),
    ('Információ, ügyintézés', lambda u: u.strip('/') in 'teendok-halaleset-utan szukseges-iratok gyakori-kerdesek hasznos-linkek torvenyek-rendeletek jogszabalyok'.split() or u.startswith('/jogszabalyok/')),
    ('Galériák, termékek', lambda u: 'galeria' in u or u.startswith('/termek-adatlapok')),
    ('Hírek', lambda u: u.startswith('/hirek-aktualitasok') or u.startswith('/rss') or 'rss' in u),
    ('Jogi és céginformáció', lambda u: u.strip('/') in 'ceginformaciok jogi-nyilatkozat adatkezeles a-sz-f'.split()),
    ('Hibás / csapda URL-ek', lambda u: True),
])
rows = collections.defaultdict(list)
for url, p in P.items():
    u = url.replace(B, '') or '/'
    st = p.get('status', 'ERR')
    g = next(k for k, f in groups.items() if (st == 200 and '+3630' not in u and f(u)) or k == 'Hibás / csapda URL-ek')
    rows[g].append((u, st, 'igen' if url in SM else 'nem', p.get('word_count_center', ''), (p.get('title') or '').replace(' - Szomorúfűz Temetkezés  Budapest', '').replace('|', '/')[:60], 'van' if p.get('canonical') else '–', (p.get('meta_robots') or '')))
out = ['# Oldaltérkép (URL-leltár)', '', f'Forrás: `data/crawl.json` – {len(P)} lekért URL, ebből {sum(1 for p in P.values() if p.get("status")==200)} db 200-as, {sum(1 for p in P.values() if p.get("status")==404)} db 404-es. A sitemap {len(SM)} URL-t tartalmaz. További {len(d["query_variants_not_fetched"])} `?mobile=no` paraméteres belső link duplikátumként rögzítve, nem lett letöltve.', '',
       'Oszlopok: státusz · benne van-e a sitemapben · szavak száma a tartalmi részben · title (márkautótag nélkül) · canonical · meta robots', '']
for g, r in rows.items():
    if not r: continue
    out += [f'## {g} ({len(r)})', '', '| URL | Státusz | Sitemap | Szó | Title | Canonical | Robots |', '|---|---|---|---|---|---|---|']
    for x in sorted(r):
        out.append('| `' + x[0] + '` | ' + ' | '.join(str(v) for v in x[1:]) + ' |')
    out.append('')
open('reports/site-map.md', 'w').write('\n'.join(out))

lh = ['| Oldal | Eszköz | Perf. | Akad. | Best Pr. | SEO | FCP | LCP | TBT | CLS | Speed Index | Méret (KiB) |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
for f in sorted(glob.glob('data/lighthouse/*.report.json')):
    r = json.load(open(f)); n = os.path.basename(f).replace('.report.json', '')
    page, dev = n.rsplit('-', 1)
    if r.get('runtimeError'):
        lh.append(f'| {page} | {dev} | – | – | – | – | hiba: `{r["runtimeError"]["code"]}` | | | | | |'); continue
    a = r['audits']; c = r['categories']; g = lambda k: a[k].get('displayValue', '').replace('\xa0', ' ')
    sc = [round((c[k]['score'] or 0) * 100) for k in ['performance', 'accessibility', 'best-practices', 'seo']]
    lh.append(f'| {page} | {dev} | ' + ' | '.join(map(str, sc)) + f" | {g('first-contentful-paint')} | {g('largest-contentful-paint')} | {g('total-blocking-time')} | {g('cumulative-layout-shift')} | {g('speed-index')} | {round(a['total-byte-weight']['numericValue']/1024)} |")
open('data/lighthouse-summary.md', 'w').write('\n'.join(lh) + '\n')
print('\n'.join(lh))
