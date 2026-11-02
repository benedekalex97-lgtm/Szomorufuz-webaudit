# Hároméves teljes birtoklási költség (TCO)

> Nettó forint. TCO = egyszeri költség (kockázati tartalékkal, ld. [cost-estimation.md](cost-estimation.md)) + 3 × éves üzemeltetés.
> A forrásokkal alátámasztott és a feltételezett tételek jelölése: **[F]** = saját feltételezés, **[S]** = forrással alátámasztott piaci adat.

## 1. Éves üzemeltetési költség

### A – Jelenlegi platform

| Tétel | Minimum | Reális | Magas |
|---|---|---|---|
| Platform-előfizetés (honlap.hu / Oleander; az ár nem nyilvános) **[F]** | 60 000 | 150 000 | 300 000 |
| Karbantartás, tartalomfrissítés (1 / 2 / 4 óra/hó) **[F]** | 144 000 | 384 000 | 1 056 000 |
| Harmadik fél: consent-eszköz, uptime-monitor, hívásmérés **[F]** | 0 | 60 000 | 250 000 |
| **Összesen / év** | **204 000** | **594 000** | **1 606 000** |

### B – Platform újabb generációja

| Tétel | Minimum | Reális | Magas |
|---|---|---|---|
| Platform-előfizetés, magasabb csomag **[F]** | 100 000 | 200 000 | 400 000 |
| Karbantartás, tartalomfrissítés (1 / 2 / 4 óra/hó) **[F]** | 144 000 | 384 000 | 1 056 000 |
| Harmadik fél **[F]** | 0 | 60 000 | 250 000 |
| **Összesen / év** | **244 000** | **644 000** | **1 706 000** |

### C – Új rendszer (WordPress-referencia)

| Tétel | Minimum | Reális | Magas |
|---|---|---|---|
| Hosting + domain (menedzselt WP-tárhely; hazai csomagok ≈ 35–120 GBP/év **[S]**, a magas szint staginggel, prémium supporttal) | 30 000 | 90 000 | 240 000 |
| Licencek (prémium bővítmények / CMS) **[F]** | 50 000 | 100 000 | 200 000 |
| Karbantartás: frissítések, mentés, biztonsági monitorozás, kis módosítások (2 / 3 / 5 óra/hó) **[F]** | 288 000 | 576 000 | 1 320 000 |
| Harmadik fél **[F]** | 0 | 60 000 | 250 000 |
| **Összesen / év** | **368 000** | **826 000** | **2 010 000** |

*Astro-változat:* a karbantartás 30–50%-kal alacsonyabb (nincs bővítményfrissítés), a hosting akár ingyenes. *Next.js-változat:* Vercel Pro 20 USD/fő/hó **[S]** + esetleges headless CMS (Sanity Growth 15 USD/hely/hó **[S]**) → ≈ 100–250 ezer Ft/év többlet.

## 2. Hároméves TCO

| | **Minimum** | **Reális** | **Magas** |
|---|---|---|---|
| **A** – egyszeri | 1,45 M | 3,27 M | 7,59 M |
| A – 3 év üzemeltetés | 0,61 M | 1,78 M | 4,82 M |
| **A – TCO nettó** | **2,06 M** | **5,05 M** | **12,41 M** |
| A – TCO bruttó | 2,61 M | 6,41 M | 15,76 M |
| **B** – egyszeri | 2,29 M | 5,07 M | 11,23 M |
| B – 3 év üzemeltetés | 0,73 M | 1,93 M | 5,12 M |
| **B – TCO nettó** | **3,02 M** | **7,00 M** | **16,35 M** |
| B – TCO bruttó | 3,84 M | 8,89 M | 20,76 M |
| **C** – egyszeri | 3,56 M | 7,63 M | 17,05 M |
| C – 3 év üzemeltetés | 1,10 M | 2,48 M | 6,03 M |
| **C – TCO nettó** | **4,66 M** | **10,11 M** | **23,08 M** |
| C – TCO bruttó | 5,92 M | 12,84 M | 29,31 M |

### Kombinált útvonal: „A-gyorsjavítás most → C a 6. hónapban”

| | Minimum | Reális | Magas |
|---|---|---|---|
| A-gyorsjavítás (30 / 40 / 60 óra, +10% tartalék) | 0,40 M | 0,70 M | 1,45 M |
| C egyszeri (a K-csomaggal együtt) | 3,56 M | 7,63 M | 17,05 M |
| Üzemeltetés: 0,5 év A + 2,5 év C | 1,02 M | 2,36 M | 5,83 M |
| **3 éves TCO nettó** | **4,98 M** | **10,70 M** | **24,33 M** |
| 3 éves TCO bruttó | 6,32 M | 13,59 M | 30,89 M |

> A „gyorsjavítás → C” út mindössze **≈ 0,6 M Ft-tal (6%)** drágább a tiszta C-nél, de a 4 kritikus hiba **5–6 hónappal korábban** javul. Ez a kiesett hívások miatti bevételvesztést szinte biztosan meghaladja (ld. roi-model, fedezeti pont: ≈ 8–9 megrendelés 3 év alatt).

## 3. Amit a TCO-számok nem mutatnak

| Szempont | A | B | C |
|---|---|---|---|
| **Halasztott költség 3 év után** | Magas: a platformgeneráció tovább öregszik, egy későbbi C elkerülhetetlenné válhat (+C költség a 4–5. évben) | Közepes: a szolgáltató ütemezésétől függ | Alacsony: a rendszer 5–7 évig fenntartható, karbantartással |
| **Maradványérték (hordozható tulajdon)** | Nincs: a design a szolgáltatóé, export nincs | Nincs | Van: kód, design, tartalom az ügyfélé |
| **Kilépési költség** | Magas (a C teljes költsége) | Magas | Alacsony: másik fejlesztőhöz vagy tárhelyre átvihető |
| **Árkockázat** | A szolgáltató az árat a határozott idő lejártakor módosíthatja (ÁSZF 8.7) | ugyanaz | Versenyző piac (hosting, karbantartás) |

## 4. Ötéves kitekintés (reális szint, tájékoztató)

| | 5 éves költség | Feltételezés |
|---|---|---|
| A, majd C a 4. évben | ≈ 3,27 + 3 × 0,59 + 7,63 + 2 × 0,83 ≈ **14,3 M** | Az A után 3 évvel mégis szükséges az újraépítés |
| C most | ≈ 7,63 + 5 × 0,83 ≈ **11,8 M** | Karbantartási szerződéssel |
| A-gyors → C | ≈ 0,70 + 7,63 + 0,5 × 0,59 + 4,5 × 0,83 ≈ **12,4 M** | |

**Következtetés:** 3 éves távon az A a legolcsóbb, de **5 éves távon a C (vagy az A-gyors → C) az olcsóbb**, ha az A után a platformváltás amúgy is bekövetkezik – ezt a technológiai értékelés szerint valószínűnek tartjuk (🔶).
