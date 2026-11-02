# Fejlesztési ütemterv és TOP 20 prioritás

A hibakódok a [hibajegyzékre](issue-register.md) hivatkoznak. A ráfordítás-becslések egy tapasztalt fejlesztő/szerkesztő idejére vonatkoznak, a meglévő CMS-ben (a forráskódot és az adminfelületet nem láttuk, ezért ±50% eltérés lehetséges).

## TOP 20 fejlesztési prioritás

Rendezési elv: **üzleti hatás** (elvesztett hívás / ajánlatkérés, bizalom, jogi kockázat) × **sürgősség** (milyen gyorsan okoz kárt) – a gyorsan javítható, nagy hatású tételek előre kerültek.

| # | Teendő | Hibakód(ok) | Üzleti hatás | Sürgősség | Ráfordítás |
|---|---|---|---|---|---|
| 1 | A két hibás telefonlink javítása („Információ” → 847-1915; árajánlat-oldali „Ügyelet” → `+36308471915`) és minden `tel:` link automatikus ellenőrzése | FUN-01, FUN-02 | Nagyon magas – elveszett sürgős hívások | Azonnal | XS |
| 2 | Rögzített „Hívás” sáv mobilon, egyetlen kiemelt (lehetőleg 0–24) számmal | UX-01, CNV-03 | Nagyon magas – a látogatók többsége mobilon, sürgős helyzetben érkezik | 1 hét | S |
| 3 | Egyértelmű éjszakai / hétvégi elérhetőség („0–24 halottszállítási ügyelet: …”) minden oldalon | UX-09 | Nagyon magas | 1 hét | XS–S |
| 4 | Ároldal létrehozása (hamvasztás, szórás, hajós, koporsós „-tól” árak, tartalom), `/arlista/` 301-gyel erre, „Árjegyzék” csempe linkelése | CNV-01, FUN-03, FUN-09 | Nagyon magas – az árérzékeny látogatók megtartása | 2 hét | M |
| 5 | Rövid, 2 lépéses ajánlatkérő + „Visszahívást kérek” űrlap (mezőtípusok, `required`, `autocomplete`, címkék) | CNV-02, FUN-12, A11Y-03, CNV-04 | Magas – több ajánlatkérés | 2–3 hét | M |
| 6 | Süti-sáv: elutasítás gomb, üres alapállapot, nem átlátszó, mobilon kisebb; Facebook SDK és régi Ads-kód eltávolítása | LEG-01, LEG-02, TEC-01, FUN-08 | Magas – jogi kockázat + mobil használhatóság + mérés | 2 hét | S–M |
| 7 | NAP-adatok egységesítése (telefonszám, 1146/1147, Izabella 65/68, márkanév, céginformációk) a weboldalon és a Cégprofilokban | SEO-04, FUN-10 | Magas – helyi keresés, bizalom | 2 hét | S |
| 8 | Végtelen URL-csapda és belső 404-ek megszüntetése (301 átirányítások) | FUN-04, FUN-05, FUN-06 | Közepes-magas – SEO, zsákutcák | 1 hét | S |
| 9 | Az értékesítési hangnemű szövegek átírása (Egyedi kedvezmény, Figyelem!, Teendők nyitánya, Árgarancia), korrektúra | UX-05, UX-07, UX-08 | Magas – bizalom és méltóság | 3–4 hét | M |
| 10 | HTML cache-fejléc javítása (`no-cache`), `Vary: User-Agent` | TEC-03, TEC-04 | Magas – különben a javítások hónapokig nem látszanak a visszatérő látogatóknál | Azonnal | XS |
| 11 | Akadálymentességi gyorsjavítások: nagyítás engedése, fókuszjelzés, skip link, kontraszt, mobilmenü `button` | A11Y-01, A11Y-02, A11Y-04, FUN-11 | Közepes-magas – idős látogatók | 2 hét | S |
| 12 | `FuneralHome` / LocalBusiness strukturált adat irodánként | SEO-03 | Magas – helyi láthatóság | 3 hét | S–M |
| 13 | H1 bevezetése, title/description újraírása a kulcsoldalakon, kannibalizáló hamvasztás-oldalak rendezése | SEO-01, SEO-05, SEO-06 | Magas – organikus forgalom | 3–4 hét | S–M |
| 14 | Canonical minden oldalon (https), perjel- és `index.php` szabályok, sitemap a gyökérben `lastmod`-dal | SEO-02, TEC-08, SEO-08, TEC-09 | Közepes-magas | 2 hét | S |
| 15 | Üres oldalak: GYIK megírása (15–20 kérdés, FAQ-séma), ÁSZF feltöltése vagy törlése, Üzenőfal megszüntetése, remarketing-oldal `noindex` | SEO-07, LEG-03, SEO-11 | Közepes-magas – bizalom, minőségjelzés | 4 hét | M |
| 16 | Mobil teljesítmény: slider megszüntetése, képek WebP/méretezés, `width/height`, scriptek `defer` | TEC-06, TEC-07, UX-02, A11Y-06, UX-10 | Közepes-magas – LCP/CLS, visszafordulás | 4 hét | M |
| 17 | Bizalomépítő tartalom: Rólunk oldal arcokkal, valós fotók, Google-vélemények, engedélyszám | UX-06 | Magas – hosszú távú konverzió | 6 hét | M |
| 18 | Szerverstabilitás: 502-k, kapcsolatbontások, CSS MIME; uptime-monitor | FUN-07, FUN-13 | Közepes – időszakos szétesett oldal | 2–4 hét | M |
| 19 | Elavult JS-könyvtárak frissítése, biztonsági fejlécek | TEC-02, TEC-05 | Közepes – biztonsági kockázat | 6 hét | M–L |
| 20 | Irodánkénti helyi landoló oldalak és örökzöld útmutatók (temetési költségek, temetési támogatás, budapesti temetők); a 2014-es hírek archiválása | SEO-10, SEO-09 | Közepes – hosszú távú organikus növekedés | 3 hónap | L |

## Ütemezés

### 0. fázis – Azonnali javítások (1–3 nap, ~1 nap munka)
- FUN-01, FUN-02 (telefonlinkek), FUN-04 (üres link), FUN-03 (`/arlista/` ideiglenes 301 az ajánlatkérésre), TEC-03 (cache), A11Y-01 (`maximum-scale`), FUN-10 (térképlink), FUN-09.
- **Eredmény:** egyetlen sürgős hívás se menjen rossz számra.

### 1. fázis – Gyors nyereségek (2–4 hét, ~6–8 nap munka)
- Sticky hívássáv, 0–24 üzenet (UX-01, UX-09, CNV-03).
- Süti-sáv és követőkódok rendbetétele (LEG-01, LEG-02, TEC-01, FUN-08).
- NAP-egységesítés, strukturált adat (SEO-04, SEO-03).
- Canonical, sitemap, 404-ek, duplikátumok (SEO-02, SEO-08, TEC-08, FUN-05, FUN-06).
- Akadálymentességi gyorsjavítások (A11Y-02, A11Y-03, A11Y-04, A11Y-08, FUN-11).
- Rövid űrlap + visszahívás (CNV-02, FUN-12, CNV-04).

### 2. fázis – Tartalom és bizalom (1–2 hónap)
- Ároldal (CNV-01), GYIK, ÁSZF (SEO-07, LEG-03).
- Hangnem-átírás és korrektúra (UX-05, UX-07, UX-08).
- Title/description/H1 (SEO-01, SEO-05, SEO-06), hamvasztás-oldalak összevonása.
- Rólunk oldal, vélemények, fotók (UX-06).
- Teljesítmény: képek, slider, scriptek (TEC-06, TEC-07, UX-02, UX-10).

### 3. fázis – Megújítás (3–6 hónap)
- Új, reszponzív, akadálymentes sablon vagy modern CMS (pl. WordPress / headless), egy HTML minden eszközre (UX-04, TEC-02, TEC-04, TEC-05, TEC-10, A11Y-05).
- Új IA (UX-03), irodánkénti oldalak (SEO-10), örökzöld útmutatók (SEO-09).
- Mérés: GA4-események, hívásmérés irodánként, havi riport.

## Mérőszámok (KPI-javaslat)

| KPI | Kiinduló érték (audit) | Cél 6 hónap múlva |
|---|---|---|
| Hibás `tel:` linkek száma | 2 (minden oldalon érintett) | 0 |
| Első kattintható telefonszám pozíciója mobilon | 4 793 px | 0 px (sticky) |
| Mobil LCP (labor, főoldal) | 5,7 s | ≤ 2,5 s |
| Mobil CLS (labor, főoldal) | 0,234 | ≤ 0,1 |
| Lighthouse Accessibility | 65–80 | ≥ 95 |
| axe kritikus/súlyos hibák | 7 szabály, 231 elem (25 futás összesen) | 0 |
| Belső 404-ek | 6 | 0 |
| Oldalak strukturált adattal | 0 | minden fő oldal + 5 iroda |
| Ajánlatkérés-űrlap mezőszáma (1. lépés) | 37 | ≤ 4 |
| Telefonos és űrlapos konverziók | nem mérhető megbízhatóan | heti szinten mérve, irodánként |

## Költségkeret-becslés (tájékoztató)

| Fázis | Becsült munkaidő |
|---|---|
| 0. fázis | 0,5–1 nap |
| 1. fázis | 6–8 nap |
| 2. fázis | 10–15 nap (+ szövegírás) |
| 3. fázis | 25–40 nap (redesign + migráció) |
