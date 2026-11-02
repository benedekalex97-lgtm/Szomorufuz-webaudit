"""5. lépés – besorolás, minőségértékelés, jogi státusz, kimenetek:
  assets/image-inventory.csv  (minden fájl, egy sor / URL)
  assets/image-catalog.html   (egyedi képek vizuális katalógusa – a bélyegképek az EREDETI URL-ről töltődnek,
                               képmásolat nem kerül a repóba)
  data/images/catalog.json    (összesítő a jelentéshez)
A tartalmi képek tárgyleírása és jogi becslése kézi szemrevételezésen alapul (2026-11-02).
"""
import csv, html, json, re
from collections import Counter, defaultdict

B = 'https://www.budapest-temetkezes.hu/'
A = json.load(open('data/images/analysis.json'))
D = json.load(open('data/images/dedup.json'))

CAT = {'arculat': 'Arculat', 'szolg': 'Szolgáltatások', 'rav': 'Ravatalozók', 'iroda': 'Irodák',
       'termek': 'Termékek', 'dekor': 'Dekorációk / sablongrafika', 'hir': 'Hír-illusztráció (archív)'}

R_STOCK = 'Nem igazolt – valószínű stockfotó; licenc (vásárlási bizonylat) szükséges'
R_SUPPLIER = 'Nem igazolt – valószínű beszállítói katalógusfotó; beszállítói engedély szükséges'
R_OWN = 'Nem igazolt – valószínű saját/megrendelt fotó; szerző és felhasználási szerződés igazolandó'
R_UNKNOWN = 'Nem igazolt – eredet ismeretlen'
R_PLATFORM = 'Platformszolgáltató (Oleander) tulajdona – ÁSZF 8.2 alapján a rendszeren kívül nem használható'
R_PRESS = 'Harmadik fél (sajtó-/hírfotó, híresség, rajzfilm, más oldal képe) – NEM használható fel újra'
R_EXIF = 'Harmadik fél: EXIF Copyright „www.judit-fotovideo.ro” – írásos engedély nélkül nem használható'
R_BRAND = 'Nem igazolt – márkajelzés (temetkezes.hu); a márkatulajdonos és a grafikus jogai tisztázandók'

# Kézi besorolás: id -> (kategória, tárgy, jog, javasolt teendő, megjegyzés)
M = {
 221: ('szolg', 'Urna átadása – fém urna kézben (főoldali kártya)', R_STOCK, 'Cserélendő', 'stock-jellegű, kicsi'),
 222: ('szolg', 'Szórókút, szóróparcella (főoldali kártya)', R_UNKNOWN, 'Cserélendő', 'kicsi'),
 223: ('szolg', 'Virágos koporsó, kéz (főoldali kártya)', R_STOCK, 'Cserélendő', 'kicsi'),
 224: ('szolg', 'Számológép (Árjegyzék kártya)', R_STOCK, 'Törlendő', 'klisé, nem illik a hangnemhez'),
 225: ('szolg', 'Számológép kézzel (Árajánlat kártya)', R_STOCK, 'Törlendő', 'klisé'),
 226: ('szolg', 'Urna fehér virágdíszben, gyertyák (Hajós temetés kártya)', R_EXIF, 'Jog tisztázása vagy csere', 'a legnagyobb kép (1052 px), szép motívum'),
 379: ('dekor', 'Mécsesek vízen (főoldal szöveg mellett)', R_STOCK, 'Cserélendő', 'kicsi, dekoratív stock'),
 380: ('arculat', '„100% Árgarancia – rejtett költségek nélkül” jelvény (piros)', R_UNKNOWN, 'Törlendő', 'elavult marketinggrafika'),
 381: ('termek', 'Türkiz üvegurna (Hamvasztásos temetés)', R_SUPPLIER, 'Cserélendő', 'kicsi'),
 382: ('szolg', 'Számológép (Árajánlat kérés)', R_STOCK, 'Törlendő', 'klisé'),
 383: ('szolg', 'Ezüst koporsó fehér virággal', R_STOCK, 'Cserélendő', 'amerikai típusú koporsó – nem a hazai kínálat'),
 384: ('szolg', 'Ravatal koporsóval, gyászolók', R_STOCK, 'Cserélendő', 'kicsi'),
 385: ('szolg', 'Halottszállító autó (fekete Mercedes)', R_UNKNOWN, 'Ellenőrizendő: saját jármű?', 'ha saját, újrafotózandó'),
 386: ('iroda', 'Koporsó-bemutatóterem', R_OWN, 'Megtartható átmenetileg', 'valós helyszín, 600 px'),
 387: ('szolg', 'Szórókút (Hamvak szórása)', R_UNKNOWN, 'Cserélendő', 'kicsi'),
 388: ('szolg', 'Kopjafák a szóróparcellánál', R_OWN, 'Megtartható átmenetileg', 'valós helyszín, 600 px'),
 389: ('szolg', 'Fém urna kézben, öltöny (Hamvasztás urnakiadás)', R_STOCK, 'Cserélendő', 'kicsi'),
 390: ('szolg', 'Virágos sír (Hamvak temetése)', R_STOCK, 'Cserélendő', 'kicsi'),
 391: ('szolg', 'Urnafal / kolumbárium belső tere', R_UNKNOWN, 'Cserélendő', 'kicsi'),
 392: ('dekor', '„Thank you” kézírás', R_STOCK, 'Törlendő', 'angol felirat, nem illik'),
 393: ('szolg', 'Hajós temetés – képkollázs', R_UNKNOWN, 'Cserélendő', 'kollázs, alacsony felbontás'),
 394: ('szolg', 'Rendezvényhajó belső tere', R_UNKNOWN, 'Ellenőrizendő: hajós partner képe?', '600 px'),
 395: ('szolg', 'Hidegtál-torony (hajós vendéglátás)', R_UNKNOWN, 'Törlendő', 'nem illik a kegyeleti kontextushoz'),
 396: ('dekor', 'Stég, hegyi tó (Polgári búcsúztatás)', R_STOCK, 'Cserélendő', 'általános hangulatkép'),
 397: ('iroda', 'Iroda kirakata / bejárat', R_OWN, 'Megtartható átmenetileg – újrafotózandó', 'az egyetlen irodafotó'),
 398: ('szolg', 'Régi iratok (Szükséges iratok)', R_STOCK, 'Cserélendő', 'kicsi'),
 399: ('arculat', '„Segítünk eligazodni? Visszahívjuk!” telefonikon-grafika', R_UNKNOWN, 'Törlendő', 'elavult grafika'),
 400: ('arculat', '„100% Árgarancia” jelvény (kék, kicsi)', R_UNKNOWN, 'Törlendő', 'elavult marketinggrafika'),
 401: ('rav', 'Urnás ravatal gyertyákkal', R_OWN, 'Cserélendő (kicsi)', 'valós ravatalozó, 200 px'),
 402: ('rav', 'Ravatalozó terem színpaddal', R_OWN, 'Cserélendő (kicsi)', 'valós ravatalozó, 200 px'),
 403: ('arculat', '„100% Árgarancia” jelvény (kék, nagy)', R_UNKNOWN, 'Törlendő', 'elavult marketinggrafika'),
 404: ('szolg', 'Búcsúterem koporsóval (Hamvasztás menete)', R_UNKNOWN, 'Ellenőrizendő: krematórium saját képe?', '600 px'),
 405: ('termek', 'Fejfa temetőben (szociális temetés)', R_OWN, 'Megtartható átmenetileg', 'valós helyszín'),
 406: ('termek', 'Fakeresztek temetőben (szociális temetés)', R_OWN, 'Megtartható átmenetileg', 'valós helyszín'),
 407: ('termek', 'Sírjelzők sora temetőben', R_OWN, 'Megtartható átmenetileg', 'valós helyszín'),
 408: ('termek', 'Fekete fakereszt friss síron', R_OWN, 'Megtartható átmenetileg', 'valós helyszín'),
 409: ('termek', 'Régi fejfa közelről', R_OWN, 'Cserélendő (kicsi)', '200 px'),
 410: ('termek', 'Fejfa-sírjelző temetőben', R_OWN, 'Megtartható átmenetileg', 'valós helyszín'),
 411: ('szolg', 'Beszélgető nő (Teendők haláleset után)', R_STOCK, 'Cserélendő', 'üzleti stock'),
 412: ('szolg', 'Gondolkodó nő kék ingben (Figyelem!)', R_STOCK, 'Törlendő', 'üzleti stock, nem illik'),
 413: ('szolg', 'Szökőkút (Fiumei úti temető)', R_UNKNOWN, 'Cserélendő', 'kicsi'),
 414: ('szolg', 'Szabadtéri búcsúztatás szónokkal (Fiumei úti temető)', R_UNKNOWN, 'Ellenőrizendő: azonosítható személyek!', 'személyiségi jog'),
 415: ('szolg', 'Ügyfélfogadás asztalnál (Munkalehetőség)', R_STOCK, 'Cserélendő', 'stock'),
 416: ('szolg', 'Öltönyös férfi halottaskocsival (Munkalehetőség)', R_STOCK, 'Cserélendő', 'stock'),
 417: ('dekor', 'Egyedi CSS-háttérelem (ps.png)', R_PLATFORM, 'Nem migrálandó', 'sablonelem'),
 418: ('arculat', 'Fejléc-logó: „temetkezes.hu” + szomorúfűz-grafika (header.jpg)', R_BRAND, 'Cserélendő – új logó / vektoros változat', 'raszteres, 522 px, elmosódott'),
 419: ('szolg', 'Slider: Hamvasztás (urna átadása)', R_STOCK, 'Cserélendő', '522×201'),
 420: ('szolg', 'Slider: Hamvasztás + temetői szórás (szökőkút)', R_UNKNOWN, 'Cserélendő', '522×201'),
 421: ('arculat', 'Slider: „temetkezes.hu” logó', R_BRAND, 'Törlendő a sliderből', 'márkazavar'),
 422: ('szolg', 'Slider: Koporsós temetés (öltönyös férfi, koporsó)', R_STOCK, 'Cserélendő', '522×201'),
 423: ('szolg', 'Slider: Hajós temetés (urna virágokkal)', 'Nem igazolt – valószínűleg ugyanaz a fotó, mint IMG-226 (© judit-fotovideo.ro)', 'Jog tisztázása vagy csere', '522×201'),
}
for i in range(227, 234):
    M[i] = ('termek', 'Sephia kézzel festett fémurna – termékadatlap', R_SUPPLIER, 'Megtartható termékkártyára', '375×500, egységes')


def fam(u):
    if any(k in u for k in ('/design/', '/common/', '/admin/', '/desing/')): return 'ui'
    if '/contents/article/' in u: return 'article'
    if '/contents/gallery/' in u: return 'gallery'
    return 'content'


def tier(r):
    w, h = r.get('width') or 0, r.get('height') or 0
    L = max(w, h)
    if L >= 1600: return 'A – hero-képnek is alkalmas'
    if L >= 1000: return 'B – kártyához / tartalomba alkalmas'
    if L >= 600: return 'C – csak kis méretben (≤ 600 px)'
    if L >= 300: return 'D – csak bélyegképként'
    return 'E – 300 px alatti (túl kicsi)'


masters = {m: info for m, info in D['masters'].items()}
rows, cat_rows = [], []
for m, info in sorted(masters.items(), key=lambda x: x[1]['id']):
    iid = info['id']; n = int(iid[4:]); r = A[m]; f = fam(m)
    pages = sorted({p for u in info['members'] for p in A[u].get('pages', [])})
    alts = sorted({a for u in info['members'] for a in A[u].get('alts', []) + A[u].get('titles', []) if a})
    ctx = sorted({c for u in info['members'] for c in A[u].get('contexts', [])})
    if n in M:
        cat, subj, rights, action, note = M[n]
    elif f == 'ui':
        cat, subj, rights, action, note = ('dekor', 'Sablongrafika / UI-elem: ' + m.rsplit('/', 1)[1].split('?')[0], R_PLATFORM, 'Nem migrálandó', 'platformsablon része')
    elif f == 'article':
        cat, subj, rights, action, note = ('hir', 'Hír-illusztráció: ' + (alts[0] if alts else m.split('/article/45/')[1].split('/')[0]), R_PRESS, 'Nem migrálandó', 'archív (2013–2014) hírek képe')
    else:
        gp = ' '.join(pages)
        if '/ravatalozo-galeria/' in gp or '/gallery/40/' in m:
            cat, subj, rights, action, note = ('rav', 'Ravatalozó terem (IX. ker., Ernő u.) – galéria', R_OWN, 'Megtartható átmenetileg – újrafotózandó', 'valós helyszín; dátumozott enteriőr')
        elif '/sirjelzo/' in gp:
            cat, subj, rights, action, note = ('termek', 'Sírjelző (fakereszt / fejfa) – termékfotó', R_SUPPLIER, 'Megtartható termékkártyára', 'fehér háttér')
        elif '/textiliak/' in gp:
            cat, subj, rights, action, note = ('termek', 'Urnaterítő / urnatartó háló – termékfotó', R_OWN, 'Újrafotózandó', 'fekete, elmosott vignetta – elavult')
        else:
            cat, subj, rights, action, note = ('termek', 'Urna / koporsó – termékfotó (Urnák galéria)', R_SUPPLIER, 'Megtartható termékkártyára', 'fehér háttér, egységes')
    t = tier(r) if r.get('width') else 'n/a'
    rec = dict(id=iid, cat=CAT[cat], subject=subj, url=m, fmt=r.get('format'), w=r.get('width'), h=r.get('height'),
               kb=round((r.get('bytes') or 0) / 1024, 1), tier=t, rights=rights, action=action, note=note,
               pages=pages, alts=alts, ctx=ctx, members=info['members'], exif=r.get('exif') or {},
               q=r.get('jpeg_q_avg'), frames=r.get('frames'), lastmod=r.get('last_modified'))
    cat_rows.append(rec)

# --- CSV: minden fájl (URL) egy sor ---
with open('assets/image-inventory.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['kep_id', 'mester', 'duplikatum_oka', 'eredeti_url', 'http_statusz', 'formatum', 'szelesseg_px', 'magassag_px',
                'meret_kb', 'jpeg_kvant_atlag', 'utolso_modositas', 'kategoria', 'targy', 'minosegi_szint', 'javasolt_teendo',
                'megjegyzes', 'felhasznalasi_jog_statusz', 'jog_ellenorzes_allapota', 'exif_szerzoi_adat', 'elofordulas_oldalak',
                'kontextus', 'alt_title'])
    by_id = {c['id']: c for c in cat_rows}
    for u, r in sorted(A.items(), key=lambda x: (D['members'].get(x[0], {}).get('id', 'ZZZ'), x[0])):
        mem = D['members'].get(u)
        if mem:
            c = by_id[mem['id']]
            w.writerow([mem['id'], 'igen' if mem['is_master'] else 'nem', mem['dup_reason'] or '', u, r.get('http', ''), r.get('format', ''),
                        r.get('width', ''), r.get('height', ''), round((r.get('bytes') or 0) / 1024, 1), r.get('jpeg_q_avg', ''),
                        r.get('last_modified', ''), c['cat'], c['subject'], c['tier'] if mem['is_master'] else '(ld. mester)',
                        c['action'], c['note'], c['rights'], 'NEM ELLENŐRZÖTT',
                        '; '.join(f'{k}: {v}' for k, v in (r.get('exif') or {}).items()),
                        ' '.join(p.replace(B, '/') for p in r.get('pages', [])), ','.join(r.get('contexts', [])),
                        ' | '.join((r.get('alts') or []) + (r.get('titles') or []))[:200]])
        else:
            w.writerow(['—', '', '', u, r.get('http', ''), '', '', '', '', '', '', '', 'Nem elérhető / nem elemzett: ' + str(r.get('status')),
                        '', 'Hivatkozás javítása vagy törlése', '', R_UNKNOWN, 'NEM ELLENŐRZÖTT', '',
                        ' '.join(p.replace(B, '/') for p in r.get('pages', [])), ','.join(r.get('contexts', [])), ''])

# --- összesítő ---
summary = {
    'files_referenced': len(A), 'files_ok': sum(1 for r in A.values() if r.get('status') == 'ok'),
    'files_missing': [u for u, r in A.items() if r.get('status') != 'ok'],
    'unique_images': len(cat_rows), 'duplicates': sum(1 for v in D['members'].values() if not v['is_master']),
    'dup_reasons': Counter(v['dup_reason'] for v in D['members'].values() if v['dup_reason']),
    'by_category': Counter(c['cat'] for c in cat_rows), 'by_tier': Counter(c['tier'] for c in cat_rows),
    'by_rights': Counter(c['rights'] for c in cat_rows), 'by_action': Counter(c['action'] for c in cat_rows),
    'by_format': Counter(c['fmt'] for c in cat_rows),
    'total_mb_all_files': round(sum((r.get('bytes') or 0) for r in A.values()) / 1e6, 1),
    'max_dimension': max(((c['w'] or 0, c['h'] or 0, c['id']) for c in cat_rows), key=lambda x: x[0] * x[1]),
    'tier_by_category': {k: Counter(c['tier'] for c in cat_rows if c['cat'] == k) for k in CAT.values()},
}
json.dump(summary, open('data/images/catalog.json', 'w'), ensure_ascii=False, indent=1, default=list)

# --- HTML-katalógus ---
def thumb_src(c):
    # a legkisebb méretváltozat szolgál bélyegképként (kisebb terhelés az eredeti szerveren)
    ok = [u for u in c['members'] if A[u].get('width')]
    return min(ok, key=lambda u: (A[u]['width'] or 0) * (A[u]['height'] or 0)) if ok else c['url']


ACT_CLASS = lambda a: 'del' if a.startswith(('Törlendő', 'Nem migrálandó')) else ('rep' if a.startswith(('Cserélendő', 'Újrafotózandó', 'Jog')) else ('chk' if a.startswith('Ellenőrizendő') else 'keep'))
cards = []
for c in cat_rows:
    t = thumb_src(c)
    small = c['tier'][0] in 'DE'
    cards.append(f'''<article class="card" data-cat="{html.escape(c['cat'])}" data-act="{ACT_CLASS(c['action'])}" data-small="{int(small)}">
<a class="th" href="{html.escape(c['url'])}" target="_blank" rel="noopener noreferrer"><img loading="lazy" src="{html.escape(t)}" alt="{html.escape(c['subject'])}" referrerpolicy="no-referrer"></a>
<div class="meta"><div class="row1"><b>{c['id']}</b><span class="pill">{html.escape(c['cat'])}</span></div>
<div class="subj">{html.escape(c['subject'])}</div>
<div class="dim">{c['w'] or '?'}×{c['h'] or '?'} px · {c['fmt']} · {c['kb']} KB{f" · {len(c['members'])-1} dupl." if len(c['members'])>1 else ''}</div>
<div class="tier t{c['tier'][0]}">{html.escape(c['tier'])}</div>
<div class="act a-{ACT_CLASS(c['action'])}">{html.escape(c['action'])}</div>
<details><summary>Jog és előfordulás</summary><p class="rights">{html.escape(c['rights'])}</p>
{('<p class="exif">EXIF: ' + html.escape('; '.join(f'{k}: {v}' for k, v in c['exif'].items())) + '</p>') if c['exif'] else ''}
<p class="pages">{html.escape(', '.join(p.replace(B, '/') for p in c['pages'][:6]) + (f' (+{len(c["pages"])-6})' if len(c['pages']) > 6 else ''))}</p></details>
</div></article>''')

cnt = summary['by_category']
filters = ''.join(f'<button data-f="{html.escape(k)}">{html.escape(k)} <span>{cnt.get(k, 0)}</span></button>' for k in CAT.values())
page = f'''<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Képkatalógus – budapest-temetkezes.hu</title>
<style>
:root{{--bg:#f7f5f1;--fg:#222;--mut:#6b6b6b;--card:#fff;--line:#e3dfd8;--acc:#1f3a4d;--ok:#2e7d32;--warn:#b26a00;--bad:#b3261e;--chk:#5b4bb7}}
@media (prefers-color-scheme:dark){{:root{{--bg:#16181a;--fg:#e8e6e3;--mut:#a3a3a3;--card:#202326;--line:#33373b;--acc:#9cc3dc}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
header{{padding:20px 16px 8px;max-width:1400px;margin:auto}}h1{{font-size:22px;margin:0 0 6px}}p.lead{{color:var(--mut);margin:0 0 10px;max-width:900px}}
.note{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--warn);padding:10px 12px;border-radius:6px;margin:10px 0;max-width:900px}}
.stats{{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}}.stats div{{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:8px 12px}}.stats b{{display:block;font-size:20px}}
nav{{position:sticky;top:0;background:var(--bg);padding:8px 16px;border-bottom:1px solid var(--line);z-index:2}}nav .in{{max-width:1400px;margin:auto;display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
button{{font:inherit;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:16px;padding:4px 10px;cursor:pointer;min-height:32px}}button.on{{background:var(--acc);color:var(--bg);border-color:var(--acc)}}button span{{opacity:.7}}
label{{margin-left:8px;color:var(--mut)}}
main{{max-width:1400px;margin:auto;padding:12px 16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden;display:flex;flex-direction:column}}
.th{{display:flex;align-items:center;justify-content:center;height:170px;background:repeating-conic-gradient(#0000000d 0 25%,#0000 0 50%) 0/16px 16px}}
.th img{{max-width:100%;max-height:170px;object-fit:contain}}
.meta{{padding:8px 10px 10px;font-size:13px}}.row1{{display:flex;justify-content:space-between;gap:6px}}.pill{{font-size:11px;color:var(--mut)}}
.subj{{margin:4px 0;min-height:36px}}.dim{{color:var(--mut)}}.tier{{margin-top:4px;font-weight:600}}
.tA,.tB{{color:var(--ok)}}.tC{{color:var(--warn)}}.tD,.tE{{color:var(--bad)}}
.act{{margin-top:2px}}.a-del{{color:var(--bad)}}.a-rep{{color:var(--warn)}}.a-chk{{color:var(--chk)}}.a-keep{{color:var(--ok)}}
details{{margin-top:6px}}summary{{cursor:pointer;color:var(--acc)}}.rights{{margin:4px 0}}.exif{{color:var(--bad);margin:4px 0}}.pages{{color:var(--mut);word-break:break-all;margin:4px 0}}
.hide{{display:none}}footer{{max-width:1400px;margin:auto;padding:16px;color:var(--mut);font-size:13px}}
</style></head><body>
<header><h1>Képkatalógus – budapest-temetkezes.hu</h1>
<p class="lead">{summary['unique_images']} egyedi kép ({summary['files_ok']} elemzett fájlból, {summary['duplicates']} duplikátum / méretváltozat kiszűrve). Felmérés: 2026. 11. 02., kizárólag nyilvánosan elérhető fájlok.</p>
<div class="note"><b>Felhasználási jog:</b> egyetlen kép felhasználási joga sincs igazolva. A „Megtartható” jelölés csak minőségi/tartalmi alkalmasságot jelent – jogi tisztázás nélkül egyik kép sem használható az új weboldalon.<br>
<b>Bélyegképek:</b> a katalógus nem tartalmaz képmásolatot; a képek az eredeti weboldalról töltődnek be (internetkapcsolat szükséges). Kattintásra a legnagyobb nyilvános változat nyílik meg.</div>
<div class="stats"><div><b>{summary['unique_images']}</b>egyedi kép</div><div><b>{summary['max_dimension'][0]}×{summary['max_dimension'][1]}</b>legnagyobb kép ({summary['max_dimension'][2]})</div>
<div><b>{sum(v for k, v in summary['by_tier'].items() if k[0] in 'AB')}</b>legalább 1000 px</div><div><b>{len(summary['files_missing'])}</b>hivatkozott, de nem elérhető / külső</div>
<div><b>0</b>igazolt felhasználási jog</div></div></header>
<nav><div class="in"><button data-f="*" class="on">Mind <span>{summary['unique_images']}</span></button>{filters}
<label><input type="checkbox" id="hideui"> sablongrafika és hírképek elrejtése</label>
<label><input type="checkbox" id="onlyrep"> csak cserélendő / törlendő</label></div></nav>
<main id="g">{''.join(cards)}</main>
<footer>Forrás: scripts/image_harvest.py, image_gallery_probe.js, image_analyze.py, image_dedup.py, image_catalog_build.py · Részletes nyilvántartás: image-inventory.csv · Ajánlások: image-recommendations.md</footer>
<script>
const g=document.getElementById('g');let f='*';
function apply(){{const hu=document.getElementById('hideui').checked,orp=document.getElementById('onlyrep').checked;
for(const c of g.children){{const cat=c.dataset.cat,act=c.dataset.act;let show=(f==='*'||cat===f);
if(hu&&(cat.startsWith('Dekor')||cat.startsWith('Hír')))show=false;if(orp&&!(act==='rep'||act==='del'))show=false;c.classList.toggle('hide',!show)}}}}
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('nav button').forEach(x=>x.classList.remove('on'));b.classList.add('on');f=b.dataset.f;apply()}});
document.getElementById('hideui').onchange=apply;document.getElementById('onlyrep').onchange=apply;
</script></body></html>'''
open('assets/image-catalog.html', 'w', encoding='utf-8').write(page)
print(json.dumps(summary, ensure_ascii=False, indent=1, default=list)[:3500])
