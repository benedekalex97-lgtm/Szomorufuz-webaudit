# Döntési mátrix

**Skála:** 1–10, ahol a **10 mindig a kedvezőbb** (a költség, az idő és a SEO-kockázat esetén is: 10 = olcsó / gyors / alacsony kockázat).
A számítás: `scripts/strategy_model.py` → `CRITERIA`, `SCORES`.

## 1. Súlyok

Két nézetet mutatunk be, mert a rövid és a hosszú távú döntés eltérő prioritásokat kíván.

| Szempont | Súly – **3 éves nézet** | Súly – **rövid távú nézet** (0–6 hónap) | A súly indoklása (3 éves nézet) |
|---|---|---|---|
| Fejlesztési költség | 15% | 25% | KKV-beruházás: fontos, de nem kizárólagos szempont |
| Fejlesztési idő | 10% | 25% | A kritikus hibák gyorsjavítása a forgatókönyvtől függetlenül megoldható, ezért az idő súlya mérsékelt |
| Technikai fenntarthatóság | 15% | 5% | A jelenlegi problémák fő oka az elavult platform |
| SEO-kockázat | 15% | 15% | Az organikus és a helyi keresés a fő ügyfélforrás (🔶 feltételezés) |
| Mobilos felhasználói élmény | 15% | 15% | A sürgős érdeklődés jellemzően mobilról érkezik; az audit legsúlyosabb hibái mobilosak |
| Biztonság | 10% | 5% | Elavult könyvtárak, hiányzó fejlécek; érzékeny (gyász-) adatok az űrlapokon |
| Üzemeltethetőség | 10% | 5% | Nem technikai munkatársak szerkesztenek; szolgáltatói függés |
| Jövőbeni bővíthetőség | 10% | 5% | Árkalkulátor, irodaoldalak, időpontfoglalás lehetősége |
| **Összesen** | **100%** | **100%** | |

## 2. Pontszámok és indoklás

| Szempont | A | B | C | Indoklás |
|---|---|---|---|---|
| Fejlesztési költség | **9** | 6 | 4 | Reális egyszeri költség: 3,3 / 5,1 / 7,6 M Ft nettó |
| Fejlesztési idő | **9** | 6 | 4 | 2–6 / 8–16 / 12–24 hét |
| Technikai fenntarthatóság | 3 | 5 | **9** | A: elavult generáció, nem frissíthető ügyféloldalon. B: újabb motor, de zárt, a szolgáltató ütemezése szerint. C: hordozható, frissíthető, bármely fejlesztő átveheti |
| SEO-kockázat (10 = alacsony) | **9** | 6 | 5 | A: nincs URL-változás. B: az URL-ek sorsa ismeretlen. C: kontrollált migráció 301-térképpel, de átmeneti ingadozás lehetséges |
| Mobilos UX | 4 | 7 | **9** | A: CSS-sel javítható a hívássáv és a kontraszt, a kettős sablon és a nagyítás tiltása marad. B: várhatóan reszponzív sablon. C: mobile-first tervezés, LCP ≤ 2,5 s cél |
| Biztonság | 3 | 5 | **8** | A: jQuery 1.12.4, jQuery UI 1.8.24, nincsenek fejlécek. B: jQuery 3.4.1 (szintén nem friss). C: aktuális függőségek + karbantartási szerződés (WordPressnél rendszeres frissítéssel; Astro esetén 9–10) |
| Üzemeltethetőség | 7 | 7 | 7 | A/B: a szolgáltató üzemeltet, de korlátozott a kontroll és az SLA (99%). C: teljes kontroll, viszont karbantartási szerződés kell. Kiegyenlített |
| Jövőbeni bővíthetőség | 2 | 4 | **9** | A/B: a platform moduljaira korlátozott. C: bármilyen funkció (árkalkulátor, foglalás, irodaoldalak) |

## 3. Súlyozott eredmény

| | **A** | **B** | **C** |
|---|---|---|---|
| **3 éves nézet** | 5,85 | 5,80 | **6,85** |
| **Rövid távú nézet (0–6 hónap)** | **7,20** | 6,00 | 5,75 |
| Egyenlő súlyokkal (ellenőrzés) | 5,75 | 5,75 | **6,88** |

### Értelmezés
- **Rövid távon az A nyer** – gyors, olcsó és alacsony kockázatú, ezért a kritikus hibákra ez a helyes válasz.
- **Hároméves távon a C nyer**, egyértelmű, ~1 pontos előnnyel; az eredmény az egyenlő súlyozással is stabil.
- **A B egyik nézetben sem első.** Költségben és időben közel van a C-hez, fenntarthatóságban és bővíthetőségben viszont az A-hoz. A B akkor válhat versenyképessé, ha a szolgáltató írásban igazolja, hogy az új generáció a sablonszintű hibákat megoldja, és migrációs segítséget ad kedvező áron (ld. érzékenység).

## 4. Érzékenységvizsgálat – mikor változna a sorrend?

| Feltétel | Hatás a 3 éves nézetre |
|---|---|
| A költség súlya 15% → 30%, a bővíthetőségé 10% → 0% | A 7,00 · B 6,30 · C 6,55 → **az A kerül előre** |
| A szolgáltató vállalja a sablonszintű javításokat (A: fenntarthatóság 3 → 5, mobil UX 4 → 6, biztonság 3 → 5) | A 6,65 · C 6,85 → a C marad elöl, de az A megközelíti |
| A B-nél a szolgáltató migrációt + megtartott URL-eket garantál (B: SEO 6 → 8, mobil UX 7 → 8, költség 6 → 7) | B 6,40 · C 6,85 → a C marad elöl |
| A C reális költsége a magas szintre nő (C: költség 4 → 2, idő 4 → 3) | C 6,45 – a C még ekkor is első |
| A C-t rossz SEO-migrációval hajtják végre (SEO 5 → 2) | C 6,40 – még első, de a valós kockázat nagy → a migrációs terv betartása kritikus |

*A számítás a fenti módosításokkal ugyanazzal a képlettel készült (Σ súly × pont / 100).*

## 5. C-n belüli technológiai mátrix (kiegészítő)

Súlyok: szerkesztői élmény 20%, fejlesztési költség 20%, karbantartási teher 15%, teljesítmény 15%, biztonság 10%, hazai fejlesztői elérhetőség 10%, bővíthetőség 10%.

| Szempont | WordPress | Astro + CMS | Next.js + headless CMS |
|---|---|---|---|
| Szerkesztői élmény (20%) | 9 | 6 | 6 |
| Fejlesztési költség (20%) | 8 | 7 | 5 |
| Karbantartási teher (15%, 10 = alacsony) | 5 | 9 | 7 |
| Teljesítmény (15%) | 7 | 10 | 9 |
| Biztonság (10%) | 6 | 10 | 8 |
| Hazai fejlesztői elérhetőség (10%) | 10 | 6 | 7 |
| Bővíthetőség (10%) | 8 | 8 | 10 |
| **Súlyozott** | **7,60** | **7,85** | **7,10** |

**Értelmezés:** az **Astro + CMS** (7,85) és a **WordPress** (7,60) közel azonos pontszámot kap – a különbség a becslések bizonytalanságán belül van. Az Astro a karbantartási tehernél, a biztonságnál és a teljesítménynél, a WordPress a szerkesztői élménynél és a fejlesztői elérhetőségnél jobb. **A döntő kérdés az, hogy ki és milyen gyakran szerkeszti majd az oldalt.**
- Ha az irodák munkatársai maguk frissítik az árakat, híreket, irodai információkat → **WordPress**.
- Ha a tartalom ritkán változik, és a módosításokat egy fejlesztői partner végzi karbantartási szerződésben → **Astro**.
- A **Next.js** csak akkor indokolt, ha 12–24 hónapon belül alkalmazásszerű funkció (pl. online árkalkulátor ügyfélfiókkal, foglalás) várható.

> A költségmodell a WordPress-változattal számol. Astro esetén a fejlesztés +10–20%, az éves karbantartás −30–50%; 3 éves TCO-ban a kettő gyakorlatilag azonos (±0,5 M Ft).
