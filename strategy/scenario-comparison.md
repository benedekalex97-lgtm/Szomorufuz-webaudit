# Forgatókönyvek összehasonlítása

Mindhárom forgatókönyv tartalmazza a **közös tartalmi csomagot (K)**: szövegírás és hangnem-átírás a kulcsoldalakon, ároldal, GYIK, 5 irodaleírás, fotózás, jogi szövegek. Ezek a teendők technológiától függetlenek, és az audit szerint az üzleti hatás jelentős része belőlük származik. Részletek: [cost-estimation.md](cost-estimation.md).

## Áttekintés

| | **A – Felújítás a jelenlegi rendszeren** | **B – Részleges modernizáció** | **C – Teljes újraépítés** |
|---|---|---|---|
| Lényeg | Marad a jelenlegi platform és sablon; tartalmi és konfigurációs javítások, egyedi CSS | Marad a szolgáltató, de átállás a platform újabb generációjára (új sablon, jQuery 3, hajax), újraépített kulcsoldalak | Saját, hordozható rendszer (WordPress vagy Astro), új UX, tudatos SEO-migráció |
| Az audit 62 hibájából kezelhető | ~29 teljesen + ~13 részben (**≈ 55–68%**) | becslés: ~45–50 (**≈ 75–80%**) – a platform új generációjának tényleges tudásától függ ❔ | **62 (100%)** |
| Mind a 4 kritikus hiba javul? | Igen (UX-01 egyedi CSS-sel, 🔶) | Igen | Igen |
| Egyszeri költség (reális, nettó, tartalékkal) | **3,3 M Ft** | **5,1 M Ft** | **7,6 M Ft** |
| Átfutás | 2–6 hét | 8–16 hét | 12–24 hét |
| 3 éves TCO (reális, nettó) | **5,1 M Ft** | **7,0 M Ft** | **10,1 M Ft** |
| Szolgáltatói függés | Változatlanul magas | Magas | Alacsony (hordozható kód és tartalom) |
| SEO-kockázat | Alacsony | Közepes (URL-ek változhatnak ❔) | Közepes, jól kezelhető (URL-megőrzés + 301-térkép) |
| Technikai adósság 3 év múlva | Nő (a platformgeneráció tovább öregszik) | Mérséklődik, de a platform ütemezésétől függ | Alacsony, ha van karbantartási szerződés |

## A – Felújítás a jelenlegi rendszeren

**Tartalom**
- 0. fázis: kritikus hibák (telefonlinkek, URL-csapda, 404-ek, NAP).
- Ároldal, GYIK, ÁSZF, rövidebb űrlapok (amennyire az űrlapmotor engedi), menüszerkezet.
- Egyedi CSS: rögzített hívássáv mobilon, kontraszt, fókuszjelzés, tipográfia, a slider kikapcsolása.
- Title/description mind a 107 oldalon, képek optimalizálása, strukturált adat és mérés, ha egyedi kód beilleszthető.
- Kérés a szolgáltató felé a sablonszintű hibákra (viewport, H1, canonical, cache, süti-sáv).

**Előnyök:** gyors, olcsó, alacsony SEO-kockázat; a legnagyobb üzleti hatású hibák javulnak.
**Hátrányok:** a hibák kb. harmada a szolgáltatón múlik; a technológiai elavulás, az akadálymentesség és a biztonság alapproblémái maradnak; a design korlátai miatt a „méltóságteljes, bizalomépítő” megjelenés csak részben érhető el.
**Kockázat:** a befektetés egy része (CSS-trükkök, adminbeli átszervezés) egy későbbi platformváltáskor elvész. A tartalmi munka (K) viszont átvihető.

## B – Részleges modernizáció

**Két alváltozatot vizsgáltunk:**

| | **B1 – Átállás a platform újabb generációjára** | **B2 – Hibrid: új frontend a kulcsoldalakra, a régi rendszer a maradékra** |
|---|---|---|
| Hogyan | Az Oleander jelenlegi motorjával (honlap.hu) új sablon, a kulcsoldalak újraépítése az oldalépítőben | Elé kerülő proxy (pl. Cloudflare Worker) útvonalanként osztja szét a forgalmat: az új kulcsoldalak saját rendszeren, a többi a régi platformon |
| Megvalósíthatóság | ❔ a szolgáltatótól függ (van-e átállási út, mennyit tud a motor: H1, canonical, viewport, űrlapmezők) | Technikailag lehetséges, de a DNS-t és a domaint ki kell venni a platform kezeléséből; két rendszer párhuzamos üzemeltetése; ÁSZF-kompatibilitás ❔ |
| Értékelés | **Ez a reális B.** Akkor jó választás, ha a szolgáltató írásban igazolja, hogy az új generáció kezeli a sablonszintű hibákat | **Nem javasolt**: a C költségeinek 60–70%-a, kettős üzemeltetés, törékeny SEO-jelek (két sablon, két sitemap). Egy jó C olcsóbb hosszú távon |

A költség- és döntési számítások a **B1-re** vonatkoznak.

**Előnyök (B1):** ismerős szerkesztőfelület marad, a szolgáltató üzemeltet, modernebb motor, várhatóan reszponzív sablon.
**Hátrányok:** a szolgáltatói függés és a design nem hordozható; az oldalépítős újraépítés kézi munka; a platform SEO- és akadálymentességi tudása publikusan nem ellenőrizhető; költségben közel van a C-hez.

## C – Teljes újraépítés

### Technológiai opciók – semleges összehasonlítás

| Szempont | **WordPress** (könnyű blokk-téma, minimális bővítmény) | **Astro** (statikus generálás + git-alapú vagy headless CMS) | **Next.js** (React, SSR/SSG, headless CMS) |
|---|---|---|---|
| Szerkesztői élmény nem technikai munkatársaknak | ★★★★★ ismerős, blokkszerkesztő | ★★★☆☆ (Keystatic/Decap egyszerű; Sanity/Storyblok jobb, de fizetős) | ★★★☆☆ (headless CMS-től függ) |
| Fejlesztési költség (ennél a terjedelemnél) | alap | +10–20% | +25–40% |
| Hazai fejlesztői elérhetőség | nagyon jó | közepes | jó, de drágább |
| Teljesítmény (Core Web Vitals) | jó, ha fegyelmezett (cache, kevés bővítmény) | kiváló (alapból statikus HTML) | kiváló / jó |
| Biztonság, karbantartási teher | rendszeres frissítést igényel (mag, bővítmények) | nagyon alacsony támadási felület | alacsony–közepes (függőségfrissítés) |
| Hosting | hazai menedzselt WP-tárhely (néhány tízezer Ft/év-től) | statikus hosting (ingyenes – néhány ezer Ft/hó) | Vercel Pro ≈ 20 USD/fő/hó + forgalom, vagy saját szerver |
| Űrlapok, hívásmérés | bővítménnyel egyszerű | külső űrlapszolgáltatás vagy serverless függvény | API-útvonal / külső szolgáltatás |
| Bővíthetőség (árkalkulátor, gyászjelentés-oldal, időpontfoglalás) | jó (bővítmények, egyedi blokkok) | jó (szigetek, API) | **kiváló** (alkalmazásszerű funkciók) |
| Szolgáltatói függés | alacsony | alacsony | alacsony (Vercel-specifikus funkciók kerülendők) |
| Mikor ez a legjobb? | Ha a munkatársak maguk szerkesztik az árakat és híreket, és fontos a széles fejlesztői kör | Ha a biztonság és a sebesség a fő szempont, a tartalom ritkán változik, és van tartós fejlesztői partner | Ha 12–24 hónapon belül interaktív funkciók (online árkalkulátor, foglalás, ügyfélportál) várhatók |

**Szakmai álláspont:** ennél a profilnál (≈ 60 indexelendő oldal, évente többször változó árak, nem technikai szerkesztők, 5 iroda) **a WordPress a kiinduló javaslat**, fegyelmezett architektúrával: blokk-téma, kevés bővítmény, menedzselt hosting, karbantartási szerződés. **Az Astro egyenértékű alternatíva**, ha a karbantartási teher minimalizálása fontosabb a szerkesztői kényelemnél. **A Next.js** jelenleg nem indokolt, mert drágább, és alkalmazásszintű funkcióra nincs igazolt igény. A költségmodell a WordPress-változattal számol; az Astro +10–20%-kal drágább fejlesztést, de 30–50%-kal alacsonyabb éves karbantartást jelent.

**Előnyök:** mind a 62 hiba kezelhető; hordozható tulajdon (kód, design, tartalom); reszponzív, akadálymentes alap; a mérés és a strukturált adat teljes kontroll alatt; a hosszú távú bővíthetőség (pl. árkalkulátor) olcsóbb.
**Hátrányok:** a legmagasabb egyszeri költség és a leghosszabb átfutás; szükséges karbantartási szerződés; az átállás SEO-kockázatát tudatosan kezelni kell; a domain és az e-mail kiköltöztetése a szolgáltatótól (❔ jogosultság).

## Mit javít melyik forgatókönyv? – a kritikus és magas súlyú tételek

| Hiba | A | B1 | C |
|---|---|---|---|
| FUN-01/02 telefonlinkek | ✅ | ✅ | ✅ |
| CNV-01 ároldal | ✅ | ✅ | ✅ |
| UX-01 mobil hívássáv | 🔶 egyedi CSS-sel | ✅ | ✅ |
| LEG-01 süti-sáv | ❔ szolgáltató | 🔶 | ✅ |
| CNV-02 rövid űrlap | 🔶 az űrlapmotor korlátaival | 🔶 | ✅ |
| SEO-01 H1, SEO-02 canonical | ❔ szolgáltató | 🔶 | ✅ |
| SEO-03 strukturált adat | 🔶 ha egyedi kód beilleszthető | 🔶 | ✅ |
| TEC-02 elavult könyvtárak | ❌ | 🔶 (jQuery 3.4.1 is régi) | ✅ |
| TEC-03 cache, TEC-05 fejlécek | ❔ szolgáltató | ❔ | ✅ |
| TEC-06 mobil teljesítmény | 🔶 képek igen, scriptek nem | 🔶 | ✅ |
| A11Y-01–04 akadálymentesség | 🔶 / ❔ | 🔶 | ✅ |
| UX-04 elavult megjelenés | ❌ | ✅ | ✅ |
| FUN-07 szerverstabilitás | ❔ szolgáltató | ❔ szolgáltató | ✅ (saját hosting-SLA) |

✅ megoldja · 🔶 részben / feltételesen · ❔ a szolgáltatótól függ · ❌ nem oldja meg
