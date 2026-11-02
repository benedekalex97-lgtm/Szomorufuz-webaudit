# Üzleti megtérülés – hipotetikus modell

> ⚠️ **Fontos:** a weboldal valós látogatottsági, hívás- és konverziós adatai **nem állnak rendelkezésre** (nincs hozzáférés Search Console-hoz, GA4-hez, Ads-fiókhoz, hívásnaplóhoz). Az alábbi számítások **egyértelműen jelölt hipotetikus alapértékekre** épülnek. Céljuk a döntési logika és az érzékenység bemutatása, **nem előrejelzés**. A valós adatok beszerzése után a modell (`scripts/strategy_model.py`) percek alatt újrafuttatható.

## 1. Piaci kontextus (forrásokkal)

| Adat | Érték | Forrás |
|---|---|---|
| Elhunytak száma Budapesten (lakóhely szerint) | 2023: 20 476 · **2024: 20 367** · 2025: 19 913 | [KSH STADAT 22.2.2.4](https://www.ksh.hu/stadat_files/nep/hu/nep0069.html) |
| Hamvasztásos temetés átlagára (országos, 2025. szept.) | **355 880 Ft** (+~11% / év) | KSH-árstatisztika, [Economx, 2025. 10. 09.](https://www.economx.hu/magyar-gazdasag/2025/10/09/halal-dragulas-arak-temetkezes-sirhely-koporso-hamvasztas-817458/) |
| Koporsós temetés átlagára (országos, 2025. szept.) | **501 800 Ft** (+~12% / év) | ugyanott |
| A Szomorúfűz saját közölt ára | „Koporsós temetési díj: 232.288 Ft-tól” | /koporsos-temetes/ |

**Következtetés:** a budapesti piac évi ≈ 20 000 temetés. Egy temetés átlagos értéke 0,35–0,5 M Ft, de ebben jelentős az áthárított tétel (krematórium, temetői díjak), ezért a cég **fedezete** megrendelésenként ennél jóval kisebb (❔ ismeretlen).

## 2. Hipotetikus alapértékek

| Paraméter | Érték | Jelölés |
|---|---|---|
| Weboldalról érkező érdeklődés (hívás + űrlap) | **40 / hó** | 🟨 HIPOTETIKUS |
| Érdeklődésből megrendelés | **35%** | 🟨 HIPOTETIKUS |
| → Weboldalhoz köthető megrendelés | **168 / év** (a budapesti temetések ≈ 0,8%-a) | származtatott |
| Fedezet megrendelésenként | konzervatív 60 000 · alap 80 000 · optimista 100 000 Ft | 🟨 HIPOTETIKUS |
| Google Ads-költés | 300 000 Ft / hó, az érdeklődések 40%-a fizetett forrásból | 🟨 HIPOTETIKUS |
| Felfutás (1. év részaránya) | A: 80% · B: 50% · C: 35% (bevezetési idő + SEO-átmenet) | feltételezés |

## 3. Várható hatások forgatókönyvenként (12 hónap után)

Az irányok az audit bizonyított hibáiból következnek; a nagyságrendek **szakmai becslések** (🟨).

| Mutató | Mi hajtja | A (kons. / alap / opt.) | B | C |
|---|---|---|---|---|
| **Telefonos érdeklődés** | hibás `tel:` linkek javítása (FUN-01/02), sticky hívássáv (UX-01), 0–24 üzenet (UX-09), egy központi szám | +5 / +12 / +20% | +8 / +18 / +30% | +10 / +25 / +40% |
| **Ajánlatkérés (űrlap)** | 37 → 3–4 mezős első lépés (CNV-02), ároldal (CNV-01), visszahívás-kérés | +5 / +15 / +30% | +10 / +25 / +45% | +15 / +35 / +60% |
| **Mobilos konverzió** | első képernyős CTA, LCP 5,7 s → ≤ 2,5 s, CLS, süti-sáv | +5 / +10 / +20% | +10 / +20 / +35% | +15 / +30 / +50% |
| **Organikus forgalom** | H1, canonical, séma, NAP, ároldal, irodaoldalak, GYIK; migrációs kockázat | 0 / +5 / +10% | −5 / +10 / +20% | 1–3. hónap: −15…0%; 12. hónap: +10 / +25 / +40% |
| **Ügyfélszerzési költség (CPL)** | magasabb konverzió azonos hirdetési költés mellett | −5 / −11 / −17% | −7 / −15 / −23% | −9 / −20 / −29% |

A modell egyetlen összevont mutatóval számol: **érdeklődés-növekedés** – A: 5 / 12 / 20%, B: 8 / 18 / 30%, C: 10 / 25 / 40%.

> A javított telefonlinkek hatása önmagában nem becsülhető, mert nem ismert, hány hívás ment eddig rossz számra. Mivel a hibás „Információ” link **minden oldal oldalsávjában** szerepel, a hatás akár a konzervatív becslésnél is nagyobb lehet.

## 4. Eredmények (hipotetikus, reális költségszinten)

**Többletköltség** = a 3 éves TCO mínusz a „nem csinálunk semmit” alternatíva (3 év platformdíj, reális: 0,45 M Ft).

| | **A** | **B** | **C** |
|---|---|---|---|
| 3 éves többletköltség (nettó) | 4,60 M | 6,55 M | 9,66 M |
| **Konzervatív:** többlet megrendelés/év · 3 éves többletfedezet · ROI | 8,4 · 1,41 M · **−69%** | 13,4 · 2,02 M · **−69%** | 16,8 · 2,37 M · **−75%** |
| **Alap:** többlet megrendelés/év · 3 éves többletfedezet · ROI | 20,2 · 4,52 M · **−2%** | 30,2 · 6,05 M · **−8%** | 42,0 · 7,90 M · **−18%** |
| **Optimista:** többlet megrendelés/év · 3 éves többletfedezet · ROI | 33,6 · 9,41 M · **+105%** | 50,4 · 12,60 M · **+92%** | 67,2 · 15,79 M · **+63%** |
| CPL (alap): 18 750 Ft → | 16 741 Ft | 15 890 Ft | 15 000 Ft |
| Vagy: Ads-megtakarítás/év azonos érdeklődésszám mellett (alap) | 0,39 M | 0,55 M | 0,72 M |

### Fedezeti pont – a legrobusztusabb mutató

A valós forgalmi adatok ismerete nélkül ez a legmegbízhatóbb döntési szempont: **hány többlet megrendelés kell havonta ahhoz, hogy a 3 éves többletköltség megtérüljön** (80 000 Ft fedezettel):

| | A | B | C | A-gyorsjavítás önmagában |
|---|---|---|---|---|
| Többlet megrendelés / hó, 3 éven át | **1,6** | **2,3** | **3,4** | **≈ 0,25** (≈ 9 megrendelés 3 év alatt) |

> **Értelmezés:** a C akkor térül meg 3 év alatt, ha a weboldal havonta **3–4 temetéssel többet** hoz. A kritikus hibák gyorsjavítása (≈ 0,7 M Ft) már **kb. 9 többletmegrendelésből** megtérül 3 év alatt – ez gyakorlatilag kockázatmentes befektetés.

### Érzékenység – ROI az alapesetben a havi érdeklődésszám függvényében

| Weboldalas érdeklődés / hó (🟨) | A | B | C |
|---|---|---|---|
| 20 | −51% | −54% | −59% |
| 40 | −2% | −8% | −18% |
| 80 | +96% | +85% | +63% |

**Következtetés:** a beruházás megtérülése elsősorban a **jelenlegi érdeklődési volumentől** függ. Az alapesetben a fedezeti pont havi ≈ 41 (A), 43 (B), illetve 49 (C) weboldalas érdeklődés; havi ~50 felett mindhárom forgatókönyv 3 éven belül megtérül, 80 felett pedig bőven. **Ez a legfontosabb beszerzendő adat** (hívásnapló, űrlapbeérkezések, GA4).

## 5. A modell korlátai és torzításai

1. **A 3 éves horizont a C-t hátrányosan kezeli:** a C egyszeri költsége 5–7 év hasznos élettartamot finanszíroz, az A után viszont valószínű egy későbbi újraépítés (ld. three-year-tco, 5 éves kitekintés).
2. A modell csak az **érdeklődésszám** növekedésével számol. Nem számszerűsíti:
   - a magasabb átlagos rendelési értéket (jobb ároldal → több kiegészítő szolgáltatás: hajós temetés, ravatalozó),
   - a márka- és bizalomhatást,
   - a jogi kockázatok (süti, ÁSZF) csökkenését,
   - a szolgáltatói függés megszűnését.
3. A C első évében az organikus forgalom átmeneti csökkenése lehetséges; a 35%-os felfutás ezt tartalmazza.
4. A „hívás” és az „űrlap” konverziós aránya eltérő lehet (a hívás valószínűleg jobban konvertál) – valós adattal pontosítandó.

## 6. Mit kell mérni a döntés előtt (2–4 hét)

| Adat | Forrás | Mire kell |
|---|---|---|
| Havi hívásszám irodánként, és hogy honnan tudott a cégről a hívó | hívásnapló, kérdezés | alapérték, csatornaarány |
| Űrlapbeérkezések / hó | e-mail fiók | alapérték |
| Organikus kattintások, top lekérdezések, top oldalak | Google Search Console | SEO-alap, migrációs kockázat |
| Ads-költés, kattintás, konverzió | Google Ads | CPL |
| Megrendelésenkénti fedezet (átlag) | könyvelés | ROI |
| Mobil / desktop arány | GA4 | a mobil fejlesztés súlya |
