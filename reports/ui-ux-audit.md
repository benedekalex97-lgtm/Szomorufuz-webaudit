# UI/UX és vizuális audit

**Viewportok:** 390 × 844 (mobil), 768 × 1024 (tablet), 1440 × 900 (desktop).
**Bizonyíték:** `screenshots/` – minden kulcsoldalról első képernyő (`*-fold.png`) és 8 oldalról teljes oldal (`*-full.jpg`).
A hibakódok a [hibajegyzékre](issue-register.md) hivatkoznak.

## 1. Összbenyomás

Az oldal **tartalmilag gazdag** (részletes leírás a hamvasztás menetéről, iratokról, megközelítésről, öt iroda), és a fontos kapcsolatfelvételi adatok desktopon az oldalsávban azonnal láthatók. A megjelenés azonban egy kb. 2012-es dobozos sablonra épül, a vizuális hierarchia gyenge, és több helyen **értékesítési, sürgető hangnem** váltja a gyászoló családnak szükséges nyugodt, együttérző kommunikációt. Mobilon a legfontosabb elem – egy azonnal hívható telefonszám – nem látható.

| Szempont | Értékelés (1–5) | Röviden |
|---|---|---|
| Vizuális hierarchia | 2 | minden doboz egyforma súlyú; a fő CTA nem emelkedik ki |
| Tipográfia, olvashatóság | 2 | desktopon 12 px, sorkizárt, piros/kék kézi kiemelések |
| Színek, kontraszt | 2 | élénk cián (#34def5) a gyász kontextusában hideg és rikító; kontraszthibák |
| Elrendezés, térközök | 2,5 | háromhasábos desktop rendben, mobilon túlcsordulás és üres sávok |
| Képek, grafika | 2 | stockfotók (számológép, urna), a nyitóképen „temetkezes.hu” logó |
| Navigáció, IA | 2 | 24 menüpont, duplikált célok |
| CTA-k | 2 | „Részletek” gombok; telefon mobilon mélyen; űrlapok hosszúak |
| Vizuális konzisztencia | 2 | eltérő fejlécszínek mobilon, inline stílusok |
| Empátia, méltóság, bizalom | 2,5 | a „Tisztelt Hozzátartozó!” nyitány jó, de sok sürgető/reklámízű szöveg |

## 2. Vizuális hierarchia

**Desktop – főoldal** (`screenshots/desktop-home-fold.png`):
- A fejléc bal oldalán a cián „Szomorúfűz Temetkezés Budapest” doboz, jobbra a slider, amelynek első képe egy másik márkanév („temetkezes.hu” logó) – két, egymással versengő márkajel (UX-02).
- A tartalmi hasábban 6 egyforma csempe („Részletek” gombokkal); a „Temetési árajánlatkérés” és az „Árjegyzék” ugyanakkora, mint a többi, az „Árjegyzék” ráadásul nem kattintható (FUN-09).
- A jobb oldalsáv 13 telefonszámot és 5 címet mutat azonos súllyal – nincs kiemelt „Hívjon most” elem (CNV-03).
- Az első képernyő alját a süti-sáv takarja.

**Mobil – főoldal** (`screenshots/mobile-home-fold.png`, `mobile-home-full.jpg`):
- Az első képernyőn: menüsáv → cégnév → szlogen → slider → süti-sáv (39%). **Telefonszám nincs**; az első `tel:` link 4 793 px mélyen (UX-01).
- A teljes oldal 6 064 CSS px hosszú (kb. 7 képernyő).

**Javaslat – új hierarchia:**
1. Fejléc: logó (egy márkanév) + kattintható 0–24 telefonszám + „Ajánlatkérés”.
2. Hero: rövid, együttérző üzenet („Részvétünk. Segítünk minden teendőben – éjjel-nappal.”), két gomb: **Hívás** és **Mit tegyek most?**
3. „Az első lépések” 3 pontban (kórházban / otthon / külföldön történt haláleset).
4. Szolgáltatások árral („-tól”) kártyákon.
5. Bizalom: munkatársak, vélemények, irodák fotói.
6. Irodák térképpel.

## 3. Tipográfia és olvashatóság

- Desktop törzsszöveg: **12 px Trebuchet MS**, `line-height: normal` – a mai ajánlás 16–18 px, 1,5–1,6 sormagasság (A11Y-09).
- Sorkizárt bekezdések nagy szóközökkel (desktopon jól látható: `desktop-hamvasztas-full.jpg`).
- Kézi kiemelések: piros mondatok, kék (#0000ff) „IDE”, nagybetűs címek, félkövér egész bekezdések – a hangsúly elveszik.
- Pozitív: mobilon a törzsszöveg 15–16 px, 28,8 px sormagassággal jól olvasható.
- **Javaslat:** egy humanista sans-serif (pl. Source Sans 3, Inter) vagy méltóságteljes serif címsorokhoz (pl. Lora) + sans törzsszöveg; 18 px alap, max. 70 karakteres sorhossz.

## 4. Színek és kontraszt

- Uralkodó szín az élénk cián (#34def5 / #33e0f6) és a fényes gradiens – a temetkezési szektorban megszokott, megnyugtató tónusokhoz (mély kék, zsálya-zöld, meleg szürke, krém) képest rikító.
- Kontraszthibák: 1,4:1 dobozcímek, fehér szöveg világosszürke mobilmenüben (A11Y-02).
- Mobilon a fejléc színe oldalanként eltér (sötét a főoldalon egy betöltésnél, cián a többin) – valószínűleg a hibásan kiszolgált CSS miatt (FUN-07).
- **Javaslat – minta paletta:** mélykék #1F3A4D (fejléc, gombok), zsálya #6B8F71 (kiemelés), meleg krém #F7F4EF (háttér), grafit #2B2B2B (szöveg); minden pár ≥ 4,5:1.

## 5. Elrendezés, térközök, igazítás

- Desktop: három hasáb (menü – tartalom – elérhetőség), fix ~980 px szélesség 1440 px-en; sok üres oldalsáv.
- Mobil:
  - /hamvasztas-urnakiadas/ 509 px, /elerhetoseg/ 408 px széles → vízszintes görgetés (UX-10).
  - A slider alatt kb. 200 px üres sáv (`mobile-hamvasztas-fold.png`, `mobile-elerhetoseg-fold.png`).
  - A hamvasztás oldalon a beágyazott elemek egy része (pl. térkép-kép) törött (`desktop-hamvasztas-full.jpg`: törött kép ikon) (FUN-06).
- Tablet (768 px): a mobil sablont kapja, nincs túlcsordulás; a hosszú egyhasábos oldalak itt is fárasztóak (főoldal 4 932 px).

## 6. Képek és grafikai elemek

- Stockfotók: számológép tollal (Árajánlat), kézben tartott urna, virágos koporsó – általános, személytelen.
- Nincs valós fotó az irodákról, munkatársakról, ravatalozóról a fő oldalakon (a galériában van ravatalozó-fotó – ez értékes, kiemelendő).
- A nyitókép „temetkezes.hu” logója elmosódott, tükröződő WordArt-stílusú, nem a cégnév (UX-02).
- Képméretek: a slider képei a megjelenítettnél jóval nagyobbak (Lighthouse: ~1,2 MB megtakarítás) (TEC-06).

## 7. Navigáció és információs architektúra

Jelenlegi szerkezet és problémái: lásd `technical-audit.md` 3. pont és UX-03.

**Javasolt IA:**
```
Azonnali teendők  (haláleset kórházban / otthon / külföldön · éjszakai ügyelet · iratok)
Szolgáltatások és árak
   ├── Hamvasztás (urna hazavitele, urnasír, szórás)
   ├── Koporsós temetés
   ├── Hajós temetés a Dunán
   ├── Búcsúztatás és ravatalozó
   └── Kegyeleti kellékek (urnák, sírjelző, textíliák)
Ügyintézés  (szükséges iratok · temetési segély · jogszabályok · GYIK)
Irodáink  (5 iroda külön oldalon)
Rólunk  (csapat · árgarancia · vélemények · céginformációk)
Kapcsolat / Ajánlatkérés
```

## 8. CTA-elemek

| CTA | Hely | Probléma | Javaslat |
|---|---|---|---|
| Telefonszámok | desktop oldalsáv; mobilon oldal alja | mobilon nem látható; 13 szám; 2 hibás link (FUN-01, FUN-02) | sticky „Hívás” sáv mobilon, egy kiemelt szám |
| „Árajánlat kérés – itt!” | felső menü | két külön oldal ugyanarra az űrlapra; a „– itt!” felkiáltás reklámízű | „Ajánlatkérés” egy URL-en |
| „Részletek” gombok | főoldali csempék | általános szöveg | „Hamvasztás részletei és árai” |
| „Elfogadom” (süti) | minden oldal | az egyetlen erős gomb a képernyőn | egyenrangú „Elutasítom” |
| Űrlapok | szolgáltatásoldalak alja | 24–37 mező, a beküldő gomb messze | 2 lépéses rövid űrlap (CNV-02) |
| „>>> IDE <<<” | főoldal, hamvasztás | elavult, nem leíró | „Útvonaltervezés a Google Térképen” |

## 9. Empatikus, méltóságteljes, bizalomépítő kommunikáció

**Ami jól működik:**
- „Tisztelt Hozzátartozó! Köszöntjük Önt honlapunkon…” – udvarias, személyes nyitány.
- A Szükséges iratok oldal megnyugtató üzenete: „nincs ok aggodalomra, ha néhány napon belül nem készül el a halotti anyakönyvi kivonat, emiatt a temetés nem marad el!”
- Részletes, gyakorlatias megközelítési leírás (trolibusz, parkolás).
- Árgarancia és „rejtett költségek nélkül” ígéret – ha árral párosul, erős bizalmi elem.

**Ami sérti a méltóságot vagy a bizalmat (UX-05, UX-06, UX-07, UX-08):**

| Idézet | Oldal | Miért probléma | Javasolt hangnem |
|---|---|---|---|
| „Kedvezmények csak Önnek! … Ön már láthatta honlapunkat … De valamilyen okból kifolyólag nem kért tőlünk árajánlatot” | /egyedi-kedvezmeny/ | a gyászoló látogatót követett „leadként” szólítja meg | „Ha bármilyen kérdése maradt, szívesen segítünk – kötelezettség nélkül.” |
| „Gondolja át miért van ez így?” | /figyelem-/ (title) | kioktató, gyanakvást kelt | tényszerű összehasonlítás címmel: „Mire figyeljen temetkezési szolgáltató választásakor?” |
| „Önnek egyetlen lényeges dolga van … költségeket, melyek az Ön pénztárcáját terhelnék” | /teendok-halaleset-utan/ | az első mondat a pénzről szól, nem a teendőkről | „Először is: őszinte részvétünk. Az alábbi lépésekben segítünk …” |
| „az egyébként is kifejezetten olcsónak mondható árainkból” | /egyedi-kedvezmeny/ | az „olcsó” szó a kegyeleti szolgáltatásnál értékcsökkentő | „kedvező, átlátható árak” |
| „Próbálja ki cégünket” | /argarancia/ | termékpróba-retorika temetésre | „Kérjen kötelezettség nélküli ajánlatot” |
| „85 éves lenne Grace Kelly”, „Gyászos ravatal helyett zenés-táncos búcsúparty” | Hírek (2014) | bulvár jelleg, elavult | hasznos útmutatók, megemlékezési tanácsok |
| „Még nincs hozzászólás.” | /uzenofal/ | üres vendégkönyv → „senki nem ajánl minket” üzenet | eltávolítás; helyette ellenőrzött vélemények |
| Elírások („statiszktikai”, „Árajálatkérés”, „Munkatársainkaz”) | több oldal | igénytelenség benyomása | korrektúra |

**Javasolt stílusalapelvek:**
1. Első mondat mindig a látogató helyzetéről szól, nem a cégről vagy az árról.
2. Rövid, nyugodt mondatok; felkiáltójel, csupa nagybetű és piros kiemelés nélkül.
3. Konkrét, ellenőrizhető ígéretek (válaszidő, ár, mit tartalmaz), szuperlatívuszok nélkül.
4. Választási szabadság hangsúlyozása („Ön dönti el…”), nyomásgyakorlás nélkül.
5. Valódi arcok és nevek – a bizalom személyekhez kötődik.

## 10. Elavult megoldások és fejlesztési lehetőségek

| Elavult | Korszerű megoldás |
|---|---|
| Automatikus fade-slider fejléc | statikus hero egy üzenettel és két gombbal |
| Külön mobil sablon `?mobile=1` kapcsolóval | egy reszponzív sablon |
| Táblázatos, inline stílusos tartalom | komponens alapú blokkok (kártya, lépéssor, ártáblázat, GYIK-harmonika) |
| 30+ mezős egyoldalas űrlap | 2 lépéses űrlap + visszahívás-kérés |
| Facebook Chat Plugin (megszűnt), Megosztás-doboz | „Visszahívást kérek” gomb, Messenger/WhatsApp link |
| Hírek 2014-ből | örökzöld útmutatók, dátumozva |
| 13 telefonszám az oldalsávban | egy 0–24 szám + „Irodáink” oldal |
| Galériák xajax popupban | natív, lusta betöltésű képgaléria |

## 11. Reszponzív összefoglaló

| Ellenőrzés | Mobil 390 | Tablet 768 | Desktop 1440 |
|---|---|---|---|
| Vízszintes túlcsordulás | ❌ 2 oldalon | ✅ | ✅ |
| Menü használhatósága | ⚠️ működik, de 24 elem, gyenge kontraszt | ⚠️ ugyanaz | ✅ látható |
| Telefonszám az első képernyőn | ❌ (Elérhetőség oldalon 866 px-en) | ❌ | ✅ oldalsáv |
| Süti-sáv takarás | ❌ 39%, áttetsző | ⚠️ | ⚠️ az alsó sáv |
| Olvashatóság | ✅ 15–16 px | ✅ | ❌ 12 px |
| Érintési célpontok | ❌ 16–30 kicsi elem / oldal | ❌ | – |
| Képernyőképek | `mobile-*` | `tablet-*` | `desktop-*` |
