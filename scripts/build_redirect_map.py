"""SEO-migrációs URL-térkép (javaslat) a crawl-adatokból: strategy/redirect-map.csv"""
import csv, json
d = json.load(open('data/crawl.json'))
B = 'https://www.budapest-temetkezes.hu'
RULES = {  # régi útvonal -> (művelet, cél, indoklás)
    '/arlista/': ('301', '/arak/', 'Hiányzó árlista (404); új ároldal'),
    '/koporsok/': ('301', '/koporsos-temetes/', '404, 16 belső hivatkozással'),
    '/hamvak-szorasa-templom/': ('301', '/hamvak-temetese/', '404; templomi elhelyezés a hamvak temetése oldalon kifejtve'),
    '/kegyeleti-webaruhaz/urna-13172/13172/': ('301', '/urnak/', '404, régi webáruház-URL'),
    '/temetkezesi-hirek/a-szocialis-temetesi-torveny-szovege/23495/': ('301', '/hirek-aktualitasok/a-szocialis-temetesi-torveny-szovege/23495/', '404, régi hírútvonal'),
    '/arajanlatkeres/': ('301', '/arajanlat-keres-itt/', 'Duplikált ajánlatkérő oldal (azonos űrlap)'),
    '/argarancia': ('301', '/argarancia/', 'Perjel nélküli duplikátum'),
    '/?mobile=no': ('301', '/', 'Paraméteres duplikátum (szabály: minden ?mobile=* → paraméter nélkül)'),
    '/?mobile=1': ('301', '/', 'Paraméteres duplikátum'),
    '/temetkezesi-szolgaltata/': ('301', '/', 'Csonka slug, 22 szavas tartalom'),
    '/uzenofal/': ('301', '/visszajelzes-kuldese/', 'Üres vendégkönyv megszüntetése'),
    '/rss/': ('301', '/feed/', 'RSS az új CMS feedjére (ha van hírfolyam), egyébként 410'),
}
KEEP_FIX = {
    '/gyakori-kerdesek/': 'Megtart – tartalommal feltölteni (FAQ-séma)',
    '/a-sz-f/': 'Megtart – ÁSZF feltöltése',
    '/egyedi-kedvezmeny/': 'Megtart – noindex (remarketing-landoló), szöveg átírása',
    '/online-kedvezmeny/': 'Megtart – noindex mérlegelendő',
    '/figyelem-/': 'Megtart – átírás („Mire figyeljen szolgáltatóválasztáskor?”)',
    '/textiliak/': 'Megtart és bővít, vagy 301 → kegyeleti kellékek gyűjtőoldal',
    '/sirjelzo/': 'Megtart és bővít, vagy 301 → kegyeleti kellékek gyűjtőoldal',
    '/temetkezesi-galeria/': 'Megtart és bővít, vagy 301 → /ravatalozo-galeria/',
    '/hamvasztas-urnakiadas/': 'Megtart – keresési szándék elkülönítése a /hamvasztasos-temetes/ oldaltól (összevonás csak Search Console-adat alapján)',
    '/hamvak-temetese/': 'Megtart – title javítása (jelenleg „Hamvasztásos temetés”)',
}
rows = []
for url, p in sorted(d['pages'].items()):
    path = url.replace(B, '') or '/'
    st = p.get('status')
    if '+36305767206' in path:
        rows.append([path, st, '301', '/elerhetoseg/', 'URL-csapda (FUN-04); a hibás link törlése után 301 vagy 410']); continue
    if path.startswith('/pages/') and path.endswith('.xml'):
        rows.append([path, st, '301', '/feed/', 'Régi RSS-fájl']); continue
    if path == '/index.php/':
        rows.append([path, st, '301', '/', 'Duplikált főoldal']); continue
    if path in RULES:
        a, t, why = RULES[path]; rows.append([path, st, a, t, why]); continue
    if path in KEEP_FIX:
        rows.append([path, st, 'megtart', path, KEEP_FIX[path]]); continue
    if path.startswith('/hirek-aktualitasok/') and path != '/hirek-aktualitasok/':
        rows.append([path, st, 'megtart', path, 'Archív hír – URL marad; noindex csak backlink-ellenőrzés után']); continue
    if st == 200:
        rows.append([path, st, 'megtart', path, 'Indexelendő oldal – azonos URL az új rendszerben, önhivatkozó https canonical']); continue
    rows.append([path, st, 'ellenőrizni', '', 'Nem besorolt'])
# Új, létrehozandó oldalak (nem a crawlból)
for new, why in [('/arak/', 'Új ároldal (CNV-01)'), ('/irodak/', 'Irodák gyűjtőoldal (SEO-10)'),
                 ('/irodak/belvaros-izabella-utca/', 'Irodaoldal'), ('/irodak/buda-nagyenyed-utca/', 'Irodaoldal'),
                 ('/irodak/zuglo-thokoly-ut/', 'Irodaoldal'), ('/irodak/rakoskeresztur-pesti-ut/', 'Irodaoldal'),
                 ('/irodak/pesterzsebet-szivacs-utca/', 'Irodaoldal'), ('/rolunk/', 'Bizalomépítő oldal (UX-06)')]:
    rows.append([new, '', 'új', new, why])
with open('strategy/redirect-map.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['regi_url', 'jelenlegi_statusz', 'muvelet', 'cel_url', 'indoklas']); w.writerows(rows)
from collections import Counter
print(len(rows), Counter(r[2] for r in rows))
