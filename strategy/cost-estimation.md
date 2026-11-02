# Költségbecslés – egyszeri fejlesztési költségek

> **Minden összeg nettó forint (ÁFA nélkül), ha másként nincs jelölve.** Bruttó = nettó × 1,27. Az üzemeltető Kft. ÁFA-körös, ezért az ÁFA várhatóan visszaigényelhető (könyvelővel ellenőrizendő), így döntéshez a **nettó** érték a releváns.
> A számítás reprodukálható: `python3 scripts/strategy_model.py` → `data/strategy-model.json`.

## 1. Forrásokkal alátámasztott piaci adatok

| Adat | Érték | Forrás | Megjegyzés |
|---|---|---|---|
| Többoldalas céges weboldal, magyar nyilvános árlisták 2026 | ~250–800 ezer Ft | [1b.hu, 2026. 08. 25.](https://1b.hu/blog/weboldal-keszites-arak-2026-mennyibe-kerul-egy-ceges-weboldal) | Sablonalapú, kisebb oldalakra vonatkozik; nettó/bruttó nincs jelölve; egyedi fejlesztés „akár milliós” |
| Webfejlesztő szabadúszó óradíja Magyarországon | ~6 000–15 000 Ft/óra | [financera.hu](https://financera.hu/szemelyes-penzugyek/szabaduszo-munkak/) | Portálbecslés, nem hivatalos statisztika |
| Vercel Pro (Next.js hostinghoz) | 20 USD / fejlesztői hely / hó + forgalom | [Vercel Pro plan docs](https://vercel.com/docs/plans/pro-plan), [makerkit.dev](https://makerkit.dev/blog/tutorials/vercel-cost) | A Hobby csomag kereskedelmi célra nem használható |
| Sanity (headless CMS) Growth | 15 USD / hely / hó; Free: max. 20 hely | [sanity.io/pricing](https://sanity.io/pricing) | Csak headless (Astro/Next.js) változatnál |
| Rackhost WordPress-tárhely | ≈ 35–120 GBP/év csomagtól függően | [whtop.com (Rackhost WP csomagok)](https://www.whtop.com/plans/rackhost.hu/147848) | Aggregátoradat, a hivatalos árlistán ellenőrizendő |
| A jelenlegi platform (honlap.hu) díja | **nem nyilvános** | [honlap.hu/arak](https://www.honlap.hu/arak/) | ❔ Ismeretlen – a számlákból kell kiolvasni |
| Platform-ÁSZF | 12 hónap határozott idő, 99% rendelkezésre állás, havonta max. 360 perc karbantartás, 24 óra támogatás / előfizetési időszak | [honlap.hu ÁSZF (2020. 02. 10-től)](https://www.honlap.hu/aszf/) | Az ügyfél egyedi szerződése eltérhet ❔ |
| EUR/HUF | ≈ 361–368 (2026. szept.–okt.) | [valutafx.com](https://www.valutafx.com/history/eur-huf-2026), harmadik feles konverter | Nem hivatalos MNB-adat; a modell 1 EUR ≈ 370 Ft, 1 USD ≈ 320 Ft értékkel számol |

**A piaci adatok korlátja:** nyilvános, forintos magyar ügynökségi óradíj- és SEO-retainer-statisztika nem található; a nemzetközi adatok nem vihetők át közvetlenül. Ezért a lenti óradíjak **saját becslések**, a fenti támpontok közé illesztve.

## 2. Saját becslések – alkalmazott feltételezések

| Paraméter | Minimum | Reális | Magas | Indoklás |
|---|---|---|---|---|
| Fejlesztői / ügynökségi átlagóradíj (nettó) | 12 000 Ft | 16 000 Ft | 22 000 Ft | Minimum: tapasztalt szabadúszó; reális: kis hazai ügynökség; magas: prémium ügynökség PM-mel, QA-val |
| Szövegírói óradíj (nettó) | 8 000 Ft | 12 000 Ft | 18 000 Ft | Szakmai, érzékeny témájú szövegírás |
| Projektvezetési ráta | A: a csomagban · B: 10% · C: 15% | | | A projekt komplexitásával nő |
| Kockázati tartalék | A: 10% · B: 25% · C: 20% | | | B: a legtöbb ismeretlen a szolgáltatónál; C: migrációs komplexitás |

## 3. Közös tartalmi csomag (K) – mindhárom forgatókönyvben

| Tétel | Minimum | Reális | Magas |
|---|---|---|---|
| Szövegírás: 15–20 kulcsoldal, ároldal, GYIK, 5 iroda, hangnem-átírás (40 / 60 / 90 óra) | 320 000 | 720 000 | 1 620 000 |
| Fotózás (irodák, munkatársak, ravatalozó) | 150 000 | 300 000 | 600 000 |
| Jogi szövegek felülvizsgálata (ÁSZF, adatkezelés, süti-tájékoztató) | 100 000 | 200 000 | 400 000 |
| **K összesen** | **570 000** | **1 220 000** | **2 620 000** |

> A K-csomag **nem vész el** platformváltáskor: a szövegek, fotók és jogi dokumentumok egy későbbi C-be változatlanul átvihetők.

## 4. Munkacsomagok forgatókönyvenként (óra)

### A – Felújítás a jelenlegi rendszeren

| Munkacsomag | Min | Reális | Magas |
|---|---|---|---|
| Kritikus hibák (tel:, 404, URL-csapda, NAP) | 4 | 6 | 10 |
| Tartalom beépítése adminban (ároldal, GYIK, űrlapok, menü, title/description 107 oldalon, alt) | 24 | 36 | 60 |
| Egyedi CSS (sticky hívássáv, kontraszt, fókusz, tipográfia, slider ki) | 8 | 16 | 30 |
| Mérés, consent, strukturált adat (ha a platform enged egyedi kódot) | 8 | 14 | 24 |
| Képoptimalizálás és újrafeltöltés | 8 | 12 | 20 |
| Egyeztetés a szolgáltatóval, QA, projektvezetés | 10 | 16 | 28 |
| **Összesen** | **62** | **100** | **172** |

### B – Részleges modernizáció (B1: átállás a platform újabb generációjára)

| Munkacsomag | Min | Reális | Magas |
|---|---|---|---|
| Felmérés, információs architektúra | 8 | 12 | 20 |
| Sablon testreszabása / arculat az új generációban | 16 | 30 | 50 |
| Oldalak újraépítése az oldalépítőben (~60 indexelendő oldal + űrlapok) | 40 | 60 | 90 |
| SEO-migráció (ha az URL-ek változnak), átirányítások | 8 | 16 | 30 |
| Akadálymentesség, teljesítmény, QA | 8 | 14 | 24 |
| Mérés, consent, strukturált adat | 8 | 12 | 20 |
| Projektvezetés (+10%) | 9 | 14 | 23 |
| **Összesen** | **97** | **158** | **257** |

### C – Teljes újraépítés (WordPress-referenciaváltozat)

| Munkacsomag | Min | Reális | Magas |
|---|---|---|---|
| Felmérés, IA, URL-térkép, tartalomstratégia | 16 | 24 | 40 |
| UX/UI tervezés (drótváz, design system, 8–10 sablon) | 30 | 50 | 80 |
| Fejlesztés (téma/komponensek, űrlapok, sticky CTA, irodaoldalak, árak, GYIK, séma) | 60 | 100 | 160 |
| Tartalommigráció (107 URL, képek, archív hírek) | 24 | 40 | 70 |
| SEO-migráció (301-térkép, canonical, sitemap, élesítési teszt, 8 hetes monitorozás) | 16 | 24 | 40 |
| Akadálymentesség, teljesítmény, cross-device QA | 16 | 24 | 40 |
| Mérés, consent (GTM, GA4, hívásmérés) | 8 | 12 | 20 |
| Projektvezetés (+15%) | 25 | 41 | 68 |
| **Összesen** | **195** | **315** | **518** |

**C technológiai változatai (reális szint, a fejlesztési órákra vetítve):**
- **Astro + git-alapú CMS:** +10–20% fejlesztés (űrlapok, CMS-integráció) → ≈ +0,5–1,0 M Ft; az éves karbantartás 30–50%-kal alacsonyabb.
- **Next.js + headless CMS:** +25–40% fejlesztés → ≈ +1,3–2,0 M Ft; hosting ≈ 20 USD/fő/hó + CMS-helyek. Csak alkalmazásszerű funkciók esetén indokolt.

## 5. Egyszeri költség összesítve

| | | **A** | **B** | **C** |
|---|---|---|---|---|
| **Minimum** | Technikai munka | 744 000 | 1 162 000 | 2 346 000 |
| | Szolgáltatói díjak / licencek | 0 | 100 000 | 50 000 |
| | Tartalmi csomag (K) | 570 000 | 570 000 | 570 000 |
| | Kockázati tartalék | 131 000 | 458 000 | 593 000 |
| | **Összesen nettó** | **1,45 M** | **2,29 M** | **3,56 M** |
| | Összesen bruttó | 1,84 M | 2,91 M | 4,52 M |
| **Reális** | Technikai munka | 1 600 000 | 2 534 000 | 5 042 000 |
| | Szolgáltatói díjak / licencek | 150 000 | 300 000 | 100 000 |
| | Tartalmi csomag (K) | 1 220 000 | 1 220 000 | 1 220 000 |
| | Kockázati tartalék | 297 000 | 1 014 000 | 1 272 000 |
| | **Összesen nettó** | **3,27 M** | **5,07 M** | **7,63 M** |
| | Összesen bruttó | 4,15 M | 6,44 M | 9,70 M |
| **Magas** | Technikai munka | 3 784 000 | 5 663 000 | 11 385 000 |
| | Szolgáltatói díjak / licencek | 500 000 | 700 000 | 200 000 |
| | Tartalmi csomag (K) | 2 620 000 | 2 620 000 | 2 620 000 |
| | Kockázati tartalék | 690 000 | 2 246 000 | 2 841 000 |
| | **Összesen nettó** | **7,59 M** | **11,23 M** | **17,05 M** |
| | Összesen bruttó | 9,64 M | 14,26 M | 21,65 M |

## 6. Fejlesztési idő

| | Minimum | Reális | Magas | Kritikus út |
|---|---|---|---|---|
| A | 2 hét | 4 hét | 6 hét | szolgáltatói válaszidő a sablonszintű kérésekre |
| B | 8 hét | 12 hét | 16 hét | a szolgáltató migrációs ütemezése, oldalak kézi újraépítése |
| C | 12 hét | 16 hét | 24 hét | tartalom-jóváhagyás (szövegek, árak), domain-átvitel ❔ |

## 7. Váratlan költségek – kockázatlista

| Kockázat | Érintett | Valószínűség | Lehetséges hatás (nettó) |
|---|---|---|---|
| A szolgáltató nem vállalja / drágán vállalja a sablonszintű javításokat | A, B | közepes | +0,2–0,8 M Ft, vagy a javítás elmarad |
| A domain jogosultja a szolgáltató; átviteli díj / adminisztráció | C | ❔ | +0–0,1 M Ft, 1–4 hét késés |
| A domainhez tartozó e-mail fiókok költöztetése | C | ❔ | +0,05–0,2 M Ft |
| Tartalom-jóváhagyás elhúzódik (árak, jogi szövegek) | mind | magas | +2–6 hét, PM-órák |
| Átmeneti organikus forgalomvesztés az élesítés után | B, C | közepes | rövid távú bevételkiesés (ld. roi-model) |
| Új igények menet közben (árkalkulátor, gyászjelentés-oldal) | C | közepes | +0,5–2 M Ft – külön fázisba kell tenni |
| Határozott idejű platformszerződés átfedése (kettős díj) | C | magas | +1 éves platformdíj arányos része |
