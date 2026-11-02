# Technikai audit

**Vizsgált oldal:** https://www.budapest-temetkezes.hu · **Dátum:** 2026. 11. 02.
A hibakódok a [hibajegyzékre](issue-register.md) hivatkoznak.

## 1. Eszközök és korlátok

| Eszköz | Állapot | Megjegyzés |
|---|---|---|
| Playwright + Chromium | ✅ elérhető, használva | `scripts/browser-audit.js`, `scripts/functional-test.js`, `scripts/consent-check.js` |
| Lighthouse | ✅ telepítve (12.8.2), 11/12 futás sikeres | a Teendők oldal desktop futása `NO_FCP` hibával leállt (headless környezet), a mobil futás sikeres |
| axe-core | ✅ 4.10.2, böngészőbe injektálva | WCAG 2.0/2.1 A+AA + best-practice szabályok |
| HTTP/HTML ellenőrzés | ✅ curl + Python (requests, BeautifulSoup) | `scripts/crawl.py` |
| Terepi Core Web Vitals (CrUX / PageSpeed Insights API) | ❌ nem sikerült | az API napi kvótája kimerült (HTTP 429) – **terepi adat nincs**, csak laboradat |
| TLS-tanúsítvány, HTTP/2 | ❌ nem vizsgálható | a kimenő forgalom TLS-bontó proxyn megy át, ezért a tanúsítvány és a protokoll a proxyé, nem a szerveré |
| W3C HTML-validátor | ⚠️ nem futtatva | külső szolgáltatás; a markup-hibákat az axe és a forráskód-elemzés fedi le |

**Kíméletes működés:** a crawler kérésenként 1,2 s szünetet tartott, a `?mobile=no` duplikátumokat nem töltötte le, a `/admin/` útvonalat (robots.txt) kihagyta. Űrlapot nem küldtünk be, süti-hozzájárulást nem adtunk meg. Párhuzamos kéréseknél a szerver többször bontotta a kapcsolatot (lásd FUN-07), ezért a mérések egymás után futottak.

## 2. Infrastruktúra és HTTP

| Ellenőrzés | Eredmény | Értékelés |
|---|---|---|
| Szerver | Apache, PHP (PHPSESSID), egyedi CMS (xajax 0.5 rc1, `design/13` sablon), Oleander Informatikai Kft. tárhely | régi platform |
| HTTPS | működik, `http://` → 301 | ✅ |
| Átirányítási lánc | `http://budapest-temetkezes.hu/` → `https://budapest-temetkezes.hu/` → `https://www.…/` | 🟢 TEC-09 |
| Perjel-kezelés | `/koporsos-temetes` → 301 → `/koporsos-temetes/` ✅, de `/argarancia` → **200** | 🟡 TEC-08 |
| `/index.php/` | **200**, a főoldal tartalmával | 🟡 TEC-08 |
| 404 oldal | valódi 404 státusz, a sablonban „Az oldal nem található – Hiba 404” | ✅ (de nincs benne segítő link / telefonszám) |
| Cache | HTML-en `cache-control: max-age=31536000` + `expires: 1981` + `pragma: no-cache` | 🟠 TEC-03 |
| `Vary` | csak `Accept-Encoding`, holott a HTML UA-függő | 🟡 TEC-04 |
| Biztonsági fejlécek | HSTS, CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy nem látható | 🟡 TEC-05 (F) |
| Stabilitás | 7 db 502 a böngészős tesztben, kapcsolatbontások, `20.css` `text/plain` MIME-vel | 🟠 FUN-07 |
| Átlagos szerverválasz (TTFB) | crawler: 204 ms átlag, 330 ms max · Lighthouse: 180 ms | ✅ |

### User-Agent szerinti kiszolgálás
A szerver eltérő HTML-t ad desktop és mobil User-Agentnek:

| UA | Méret | viewport meta | robots |
|---|---|---|---|
| Desktop Chrome | 36 042 B | **nincs** | – |
| iPhone Safari | 36 867 B | `width=device-width, initial-scale=1, maximum-scale=1` | – |
| Googlebot Smartphone | 36 867 B | mint az iPhone | – |
| `?mobile=1` / `?mobile=no` | – | – | `noindex, follow` ✅ |

A Googlebot mobilon ugyanazt a mobil HTML-t kapja (indexelhető) – ez rendben van. A kockázat a `Vary` hiánya és a `maximum-scale=1` (A11Y-01).

## 3. Oldaltérkép és crawl-eredmények

A teljes URL-leltár: **[site-map.md](site-map.md)**.

| Mutató | Érték |
|---|---|
| Lekért egyedi URL | 113 |
| 200-as oldal | 107 (ebből 8 a FUN-04 csapda-URL) |
| 404-es belső cél | 6 (`/arlista/`, `/koporsok/`, `/hamvak-szorasa-templom/`, `/kegyeleti-webaruhaz/urna-13172/13172/`, `/temetkezesi-hirek/…/23495/`, csapda 5. szint) |
| Sitemap URL-ek | 95 – mind 200-as ✅ |
| Sitemapben nem szereplő élő oldal | `/argarancia` (perjel nélkül), RSS-fájl, csapda-URL-ek |
| `?mobile=no` belső linkek | 106 db (noindex-es duplikátumok) |
| Átlagos HTML-méret | ~36 KB |

### Fő felhasználói útvonalak

```
Főoldal
├── Felső menü: Hamvasztásos temetés · Koporsós temetés · Árajánlat kérés – itt! · Elérhetőség
├── Bal menü (20): Teendők haláleset után → Hamvasztás urnakiadás → Hamvak hazavitele → Hamvasztás menete
│                  → Ravatalozó terem → Hamvak szórása (temető / Duna) → Hamvak temetése → Árajánlatkérés
│                  → Fiumei úti temető → Tájékoztatás kérés → Polgári búcsúztatás → Szükséges iratok
│                  → Ravatalozó galéria → Urnák → Visszajelzés küldése → Jogszabályok → Sírjelző → Textíliák
├── Főoldali csempék (6): Hamvasztás · Hajós temetés · Szórás · Koporsós temetés · Árajánlatkérés · Árjegyzék (link nélkül)
├── Szövegközi linkek: „Árlista” → 404 · „Árgarancia”
├── Oldalsáv: 5 iroda címe (Google Térkép), 13 telefonszám, e-mail, nyitvatartás
└── Lábléc: Céginformációk · Jogi nyilatkozat · Mobil (?mobile=1)

Csak a sitemapből / belső mély linkekből elérhető: GYIK (üres), ÁSZF (üres), Hírek (2014), Üzenőfal (üres),
Egyedi kedvezmény, Online kedvezmény, Hírlevél, Munkalehetőség, Termékadatlapok, Jogszabályok, Figyelem!
```

**Navigációs problémák:** a GYIK, az Árgarancia, a Céginformációk és a jogi oldalak nincsenek a fő navigációban; a „Kezdőoldal” a bal menü első eleme, de mobilon a lenyíló lista 5. helyére kerül; két külön URL ugyanarra az árajánlat-űrlapra (UX-03).

## 4. HTML-szemantika és kódminőség

| Terület | Megállapítás | Hivatkozás |
|---|---|---|
| Doctype | `XHTML 1.0 Transitional`, hibás `xmlns="https://www.w3.org/1999/xhtml"` | TEC-10 |
| `lang` | `hu` ✅ | |
| Címsorok | aloldalakon nincs H1, a logó a H1 a főoldalon; címsor-sorrend hibák | SEO-01, A11Y-05 |
| Landmarkok | nincs `header/nav/main/footer` | A11Y-05 |
| Layout | 72 tartalmi `<table>`, oldalanként átlag 24,6 inline `style` | TEC-10, UX-04 |
| Linkek | 1 299 `target="_blank"` `rel` nélkül (modern böngészők `noopener`-t feltételeznek – alacsony kockázat), `tel:` linkeken is `target="_blank"` | |
| Hibás linkek | `href="+36305767206"` (FUN-04), rossz `tel:` célok (FUN-01, FUN-02) | |
| JavaScript | 17 szinkron script a `<head>`-ben, `xajax_core.js` kétszer | TEC-07 |
| Könyvtárak | jQuery 1.12.4, jQuery UI 1.8.24, jquery.tools, galleria, qtip, flexslider, elevatezoom, uploadifive | TEC-02 |

## 5. Metaadatok, canonical, robots

| Elem | Állapot |
|---|---|
| `<title>` | minden oldalon van; 51 db 65 karakter felett; elírások (SEO-05) |
| meta description | 106/107 oldalon van, de 71 db 70 karakter alatt (SEO-06) |
| canonical | 50/107 oldalon (csak hírek, jogszabályok, termékek – azok is `http://`); a fő oldalakon nincs (SEO-02) |
| meta robots | csak a `?mobile=` változatokon `noindex, follow` ✅ |
| robots.txt | `Disallow: /admin/`, `Sitemap:` http-s, nem szabványos útvonalon (SEO-08) |
| sitemap.xml | `/pages/avszomfuzbud/sitemap.xml`, 95 URL, `lastmod` nélkül; `/sitemap.xml` 404 |
| Open Graph | csak 50 oldalon (SEO-13) |
| Strukturált adat | **nincs** (SEO-03) |
| Hreflang | nem releváns (egynyelvű) |

## 6. Erőforrások és konzol

Összesítve 36 oldalbetöltés (12 oldal × 3 viewport) alapján (`data/browser-audit.json`):

| Hiba | Előfordulás | Hivatkozás |
|---|---|---|
| Mixed content: `http://www.googleadservices.com/pagead/conversion.js` blokkolva | 24 betöltés | TEC-01 |
| `connect.facebook.net/…/xfbml.customerchat.js` – `ERR_BLOCKED_BY_ORB` (megszűnt szolgáltatás) | 24 | FUN-08 |
| 404 kép: `/pages/szomorufuz-temetkezes/contents/static/19/…_200x.jpg` (2 db) | 3–3 | FUN-06 |
| 502 Bad Gateway képekre / gif-re | 7 | FUN-07 |
| `design/mobile/colors/20.css` – `text/plain` MIME, nem alkalmazva | 1 | FUN-07 |
| `postMessage` origin-figyelmeztetés (YouTube, Google Térkép iframe) | 4 | harmadik fél, alacsony |
| Permissions-Policy figyelmeztetések | minden betöltés | harmadik feles iframe-ek, alacsony |

JavaScript-kivétel (`pageerror`) nem keletkezett. `alert()` dialógus nem jelent meg a tesztek alatt (FUN-13 csak hibaágon fut).

## 7. Követőkódok és hozzájárulás

| Elem | Megállapítás |
|---|---|
| Google Tag Manager | `GTM-NBJCMVB` – a hozzájárulás előtt **nem** töltődik be ✅ |
| Google Consent Mode | `consent default` → minden `denied` ✅ |
| Régi Google Ads konverziókód | `google_conversion_id = 959416490`, `http://` script – blokkolva, valószínűleg nem mér (TEC-01) |
| Facebook SDK | `static.xx.fbcdn.net` erőforrások hozzájárulás előtt (LEG-02); a Chat Plugin megszűnt (FUN-08) |
| Süti-sáv | előre bepipált marketing, nincs elutasítás (LEG-01) |
| Egyéb | `xajax_siteStat` saját statisztika |

## 8. Teljesítmény (Lighthouse, laboradat)

> **Fontos:** laboradat, kimenő proxyn keresztül, szimulált lassú 4G-vel (mobil). A Google rangsorolásban a terepi (CrUX) adatok számítanak, ezek nem voltak lekérhetők. Az értékek nagyságrendje és a feltárt okok megbízhatók, a pontos számok futásonként ±10–15%-kal szórhatnak.

| Oldal | Eszköz | Perf. | Akad. | Best Pr. | SEO | FCP | LCP | TBT | CLS | Speed Index | Méret (KiB) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Főoldal | mobil | **49** | 80 | 75 | 92 | 4,4 s | **5,7 s** | 0 ms | **0,234** | 26,3 s | **1 758** |
| Főoldal | desktop | 66 | 77 | 67 | 92 | 2,5 s | 3,2 s | 0 ms | 0,054 | 2,8 s | 812 |
| Hamvasztás urnakiadás | mobil | 74 | 70 | 71 | 92 | 4,1 s | 4,1 s | 10 ms | 0 | 5,6 s | 1 456 |
| Hamvasztás urnakiadás | desktop | 64 | 73 | 67 | 92 | 2,9 s | 3,7 s | 0 ms | 0,046 | 2,9 s | 1 646 |
| Koporsós temetés | mobil | 64 | 74 | 71 | 92 | 3,5 s | 3,5 s | 0 ms | **0,353** | 4,9 s | 504 |
| Koporsós temetés | desktop | 63 | 73 | 67 | 92 | 2,6 s | 3,0 s | 0 ms | 0,091 | 11,5 s | 693 |
| Árajánlat kérés | mobil | 57 | 74 | 71 | 92 | 4,3 s | 4,3 s | 0 ms | **0,315** | 5,2 s | 372 |
| Árajánlat kérés | desktop | 84 | 73 | 67 | 92 | 1,5 s | 1,7 s | 0 ms | 0,05 | 2,2 s | 561 |
| Elérhetőség | mobil | 58 | **65** | 75 | 92 | 4,3 s | 5,0 s | 10 ms | 0,234 | 5,1 s | 919 |
| Elérhetőség | desktop | 68 | 75 | 67 | 92 | 2,3 s | 3,3 s | 0 ms | 0,015 | 2,5 s | 1 109 |
| Teendők haláleset után | mobil | 59 | 74 | 96 | 92 | 4,1 s | 4,4 s | 20 ms | 0,292 | 4,9 s | 367 |
| Teendők haláleset után | desktop | – | – | – | – | `NO_FCP` futási hiba | | | | | |

Teljes riportok: `data/lighthouse/*.report.html`.

**Core Web Vitals (labor) értékelése** – „jó” küszöb: LCP ≤ 2,5 s, CLS ≤ 0,1, INP ≤ 200 ms (TBT itt jó):
- LCP mobilon minden mért oldalon 3,5–5,7 s → **„javítandó”/„gyenge”**.
- CLS mobilon 5/6 oldalon 0,23–0,35 → **„gyenge”** (a slider és a méret nélküli képek okozzák).
- TBT 0–20 ms → a JavaScript futása nem szűk keresztmetszet; a probléma a hálózat és a képek.

**Fő okok (Lighthouse javaslatai, főoldal mobil):**
1. Képek: modern formátum ~1 085 KiB, hatékony tömörítés ~804 KiB megtakarítás (a slider képei 756 px-es helyre jóval nagyobbak).
2. Render-blokkoló erőforrások: ~2,4–2,7 s.
3. 53 kérés nem HTTP/2-n (proxy miatt nem megbízható, ld. korlátok).
4. `width`/`height` nélküli képek → elrendezés-ugrás.
5. Harmadik feles facade (YouTube-beágyazás) lehetősége.
6. A Speed Index 26,3 s a mobil főoldalon az automatikusan váltó sliderből ered (a vizuális változás sokáig nem áll le).

## 9. Ajánlott technikai intézkedések (összefoglaló)

| Prioritás | Teendő | Hibakód |
|---|---|---|
| Azonnal | hibás `tel:` linkek, üres `<a href="+3630…">`, `/arlista/` átirányítás | FUN-01, FUN-02, FUN-03, FUN-04 |
| Azonnal | HTML cache-fejléc javítása | TEC-03 |
| 1–2 hét | régi Ads-snippet és Facebook SDK eltávolítása, konverziómérés GTM-be | TEC-01, FUN-08, LEG-02 |
| 1–2 hét | canonical, perjel- és `index.php` szabályok, sitemap a gyökérben | SEO-02, TEC-08, SEO-08 |
| 1 hónap | képoptimalizálás, slider eltávolítása, scriptek `defer`-rel | TEC-06, TEC-07 |
| 1 hónap | jQuery / jQuery UI frissítése, biztonsági fejlécek | TEC-02, TEC-05 |
| 3–6 hónap | új, reszponzív sablon HTML5-tel (egy HTML minden eszközre) | TEC-04, TEC-10, UX-04 |
