# Képállomány – értékelés és ajánlások

**Vizsgált oldal:** https://www.budapest-temetkezes.hu · **Felmérés:** 2026. 11. 02.
**Kapcsolódó fájlok:** [`image-inventory.csv`](image-inventory.csv) (minden fájl, egy sor / URL) · [`image-catalog.html`](image-catalog.html) (vizuális katalógus szűrőkkel)
**Reprodukálás:** `scripts/image_harvest.py` → `image_gallery_probe.js` → `image_analyze.py <helyi_mappa>` → `image_dedup.py` → `image_catalog_build.py`

> ⚖️ **Felhasználási jogok:** egyetlen kép felhasználási joga sincs igazolva. A „megtartható” jelölés kizárólag minőségi és tartalmi alkalmasságot jelent. Jogi tisztázás nélkül egyik kép sem kerülhet az új weboldalra.
>
> 🔒 **Képmásolatok:** a repozitórium **nyilvános**, ezért egyetlen képfájl és bélyegkép sem került bele. A katalógus az eredeti URL-ekről tölti be a képeket; az elemzéshez készült másolatok csak a helyi munkakönyvtárban vannak (`.gitignore` védi). *Megjegyzés:* a korábbi audit `screenshots/` mappájának képernyőképein is láthatók a weboldal képei. Ha ez aggályos, érdemes a repót privátra állítani.

## 1. Összefoglaló

| Mutató | Érték |
|---|---|
| Átvizsgált oldalak | a 107-es audit 96 élő, egyedi HTML-oldala (1 perjel nélküli duplikátum átmeneti 503-at adott, tartalma a perjeles címen vizsgálva) + 8 CSS-fájl + 5 galéria popupjai |
| Hivatkozott képfájl (URL) | **659** |
| Sikeresen elemzett fájl | **649** (30,4 MB) |
| Nem elérhető hivatkozás | **10** – 7 tartalmi kép régi oldalazonosítóval (`pages/szomorufuz-temetkezes/…`, 404) a Hamvasztás oldalakon, 2 sablonkép (404), 1 külső PayPal-ikon |
| Duplikátum / méretváltozat | **226** (210 méretváltozat, 10 bájtazonos másolat, 6 közel-duplikátum) |
| **Egyedi kép** | **423** |
| Legnagyobb kép | **1052 × 359 px** (IMG-226) – az egyetlen, amely 1000 px fölött van |
| Formátumok (egyedi) | JPEG 344 · GIF 56 · PNG 22 · SVG 1 (betűkészlet) – **nincs WebP/AVIF** |
| Igazolt felhasználási jog | **0** |

**Fő megállapítás:** a képállomány **mennyiségben bőséges, minőségben és jogilag alkalmatlan** egy modern weboldalhoz. Nincs hero-méretű kép, a szolgáltatások képei 200–600 px-esek és nagyrészt stockfotók, a valódi helyszínekről (irodák, ravatalozó, munkatársak) alig van felvétel. Az új weboldalhoz **új, saját fotózás** szükséges; a meglévő képekből csak a termékfotók és néhány helyszínfotó használható átmenetileg, jogi tisztázás után.

## 2. Csoportosítás

| Kategória | Egyedi kép | Tartalom | Minőség röviden |
|---|---|---|---|
| **Arculat** | 6 | „temetkezes.hu” fejléc-logó (raszteres, 522 px), logó-slide, 3 db „100% Árgarancia” jelvény, „Visszahívjuk!” grafika | elavult, márkazavaró; nincs vektoros Szomorúfűz-logó |
| **Szolgáltatások** | 30 | főoldali kártyák, slider-képek, aloldalak illusztrációi (urna, koporsó, szórókút, hajó, iratok) | 1 db ≥ 1000 px, 5 db 600 px, 24 db 300 px alatt vagy bélyegkép; sok klisé (számológép, üzleti stock) |
| **Ravatalozók** | 8 | IX. ker., Ernő utcai ravatalozó (galéria: 6 db 432–600 px; aloldal: 2 db 200 px) | valós helyszín, de lila drapériás, vakus, dátumozott enteriőr |
| **Irodák** | 2 | iroda kirakata (IMG-397), koporsó-bemutatóterem (IMG-386) | **súlyos hiány**: 5 irodából gyakorlatilag nincs fotó |
| **Termékek** | 153 | 108 urna/koporsó (Urnák galéria), 7 Sephia urna-adatlap, 9 sírjelző, 22 urnaterítő/-háló, 6 sírjelző temetői környezetben, 1 üvegurna | az urnafotók egységes, profi katalógusképek (fehér háttér, 400×500); a textilfotók elavultak (fekete, elmosott vignetta) |
| **Dekorációk / sablongrafika** | 84 | 81 platform-sablonelem (gradiensek, gombok, ikonok – `design/13`, jQuery UI), 3 dekoratív stock (mécsesek, stég, „Thank you”) | nem migrálandó – a sablonelemek a platformszolgáltató tulajdonában vannak (ÁSZF 8.2) |
| **Hír-illusztráció (archív)** | 140 | 2013–2014-es hírek képei: hírességek (Grace Kelly, Bubik István, Grosics Gyula), rajzfilmkockák (Dargay Attila), külföldi sajtófotók, más oldalak vízjeles képei | **jogilag kockázatos**, nem használható fel újra |

> A felhasználó által kért hat kategória mellé két kiegészítő került: a **sablongrafika** a „Dekorációk” alá, a **hír-illusztrációk** pedig külön kategóriába, mert jogi helyzetük alapvetően eltér a többi képétől.

## 3. Minőségértékelés – alkalmasság modern weboldalra

### Mérce (retina-kijelzőkre, 2× pixelsűrűséggel)

| Felhasználás | Ajánlott minimum | Jelenleg ennek megfelelő kép |
|---|---|---|
| Főoldali nyitókép (hero), teljes szélesség | 2400 × 1350 px (min. 1920 px széles) | **0** |
| Szolgáltatáskártya / szekciókép | 1200 × 800 px | **0** (IMG-226: 1052 × 359, de panoráma-arányú) |
| Tartalmi kép a szövegben | 1600 px széles (800 px megjelenítés) | **0** |
| Termékkártya (rács, kb. 300 px) | 600 × 750 px | **0** – a termékfotók 400 × 500-asak: 1×-es kijelzőn elfogadhatók, retinán lágyak |
| Termék nagyítás / részletnézet | 1200 × 1500 px | **0** |
| Bélyegkép, ikon | – | sok |

### Minőségi szintek (egyedi képek)

| Szint | Darab | Jelentés |
|---|---|---|
| A – hero-képnek is alkalmas (≥ 1600 px) | 0 | – |
| B – kártyához / tartalomba (1000–1599 px) | 1 | IMG-226 (jogilag nem tiszta) |
| C – csak kis méretben (600–999 px) | 121 | termék- és ravatalozófotók, néhány helyszínfotó |
| D – csak bélyegképként (300–599 px) | 206 | termékfotók, hírképek, szolgáltatásképek |
| E – 300 px alatti (túl kicsi) | 94 | sablongrafika, 200 px-es tartalmi képek |

### Tartalmi és stílusbeli problémák
- **Klisék:** számológép tollal (IMG-224, 225, 382), „100% Árgarancia” jelvények (IMG-380, 400, 403), üzleti stockszereplők (IMG-411, 412, 415, 416), „Thank you” kézírás (IMG-392). Ezek a gyászoló látogatónak értékesítési, személytelen hatást keltenek.
- **Nem a hazai kínálatot mutató képek:** amerikai típusú ezüst koporsó (IMG-383), hidegtál-torony a hajós temetés oldalon (IMG-395).
- **Márkazavar:** a „temetkezes.hu” logó a fejlécben és a slider első diáján (IMG-418, 421), Szomorúfűz-logó nincs.
- **Elavult fotóstílus:** a textíliák fekete, elmosott vignettával (IMG-357–378); a ravatalozó vakus, lila drapériás képei (IMG-342–347).
- **Személyiségi jog:** azonosítható gyászolók és szónok (IMG-414, IMG-384), illetve hírességek a hírekben.
- **Technikai:** csak JPEG/GIF/PNG, nincs WebP/AVIF, nincs `srcset`; a slider képei 522 × 201 px-esek, mobilon felnagyítva jelennek meg.

## 4. Felhasználási jogok – nyilvántartás és teendők

Minden kép jogi státusza **„NEM ELLENŐRZÖTT”** (`image-inventory.csv` → `jog_ellenorzes_allapota`). A becsült eredet:

| Becsült eredet | Egyedi kép | Szükséges igazolás | Kitől |
|---|---|---|---|
| Beszállítói katalógusfotó (urnák, koporsók, sírjelzők, Sephia urnák) | 125 | írásos engedély a webes felhasználásra | urna- és koporsóbeszállítók |
| Saját vagy megrendelt fotó (ravatalozó, iroda, sírjelzők temetőben, textíliák) | 39 | a fotós neve + felhasználási szerződés vagy nyilatkozat | ügyfél / egykori fotós |
| Stockfotó | 19 | licencbizonylat (oldal, licenc típusa, webes használat) | ügyfél (vásárlási előzmények) |
| Eredet ismeretlen | 15 | eredet felderítése, különben csere | ügyfél |
| **Harmadik fél – EXIF: „www.judit-fotovideo.ro”** (IMG-226; valószínűleg ugyanez a fotó IMG-423) | 1 + 1 | írásos engedély a fotóstól | judit-fotovideo.ro |
| Márkajelzés („temetkezes.hu” logó) | 2 | a márka és a grafika tulajdonosa | ügyfél |
| Platform-sablongrafika (Oleander) | 81 | – nem szükséges, **nem migrálandó** | – |
| Hír-/sajtófotó, híresség, rajzfilm, más oldal képe | 140 | – **nem használható**, nem migrálandó | – |

**Az igazolás minimuma képenként:** forrás (fotós / beszállító / stockügynökség), licenc vagy engedély típusa, a webes felhasználás és módosítás joga, időbeli korlát, a bizonyíték helye. Javasolt egy közös táblában vezetni, a CSV `kep_id` oszlopára hivatkozva.

**Fordított képkeresés** (Google Lens / TinEye) ebben a munkamenetben nem volt elérhető. A 19 valószínű stock- és a 15 ismeretlen eredetű képnél ajánlott elvégezni, mert gyorsan kideríthető vele az eredeti forrás.

## 5. Ajánlások – főoldal

| Elem | Jelenlegi kép | Értékelés | Ajánlás |
|---|---|---|---|
| Fejléc / logó | IMG-418 (temetkezes.hu, 522 px raszter) | márkazavar, elmosódott | **új, vektoros (SVG) Szomorúfűz-logó**; a szomorúfűz-motívum megtartható, ha a jogok tisztázottak |
| Hero / slider | IMG-419–423 (522 × 201, automatikus slider) | túl kicsi, stock, márkazavar | **egyetlen nyugodt, valós fotó** – pl. a belvárosi iroda fogadótere természetes fényben, munkatárs a háttérben; vagy finom természeti motívum (szomorúfűz, Duna-part hajnalban). **Új fotózás szükséges** – a meglévő képek közül egyik sem alkalmas |
| Kártya: Hamvasztás | IMG-221 (472 px, stock) | kicsi | átmenetileg: IMG-389 vagy IMG-221 kis méretben; **végleges: új fotó** – urna átadása az irodában, kéz-közeli, nem színpadias |
| Kártya: Hajós temetés | IMG-226 (© judit-fotovideo.ro) | szép motívum, de idegen jog | **jog tisztázása**; vagy saját fotó a hajóról / a Dunáról (partnertől engedéllyel) |
| Kártya: Szórás temetőben | IMG-222 (270 px) | kicsi | átmenetileg **IMG-388** (kopjafák a szóróparcellánál, 600 px, valós helyszín) |
| Kártya: Koporsós temetés | IMG-223 (250 px, stock) | kicsi | átmenetileg **IMG-386** (koporsó-bemutatóterem, valós, 600 px) |
| Kártya: Árajánlat / Árjegyzék | IMG-224, 225 (számológép) | klisé | **kép nélkül** – ikon vagy árkártya-design; ha kép kell: munkatárs telefonál / beszélget ügyféllel (saját) |
| Ravatalozó galéria (főoldalon) | IMG-342–347 | valós, de dátumozott | 1 kép megtartható átmenetileg (IMG-345 vagy IMG-346, 600 px) – **új fotózás javasolt** |
| Bizalom-szekció (új) | nincs | – | **munkatársak portréi**, irodák bejárata (5 iroda), ravatalozó – mind új fotó, a munkatársak írásos hozzájárulásával |
| Dekoráció | IMG-379 (mécsesek) | stock | elhagyható; helyette visszafogott színfelület |

## 6. Ajánlások – aloldalak

| Aloldal | Jelenlegi képek | Teendő | Javasolt kép (átmeneti → végleges) |
|---|---|---|---|
| Hamvasztásos temetés | IMG-381 (üvegurna, 200 px) | Cserélendő | → urnaválaszték-részlet a bemutatóteremből (új) |
| Hamvasztás, urnakiadás | IMG-389 (200 px, stock) + 2 hiányzó kép (404) | Cserélendő, a 404-es hivatkozásokat törölni | → urna átadása az irodában (új) |
| Hamvasztás menete | IMG-404 (600 px, eredete ismeretlen) + 5 hiányzó kép (404) | Ellenőrizendő; a 404-eket törölni | → ha a krematórium engedélyezi: búcsúterem; különben folyamatábra-illusztráció (rajzolt, nem fotó) |
| Koporsós temetés | IMG-383, 384, 385, 386, 380 | 386 megtartható átmenetileg; 383/384 csere; 380 törlés; 385 ellenőrizendő (saját jármű?) | → bemutatóterem (új, nagy felbontás), saját halottszállító jármű (új) |
| Hamvak szórása – temető | IMG-387 (200 px), IMG-388 (600 px) | 388 átmenetileg | → szóróparcella / szórókút saját fotója, ember nélkül (új) |
| Hamvak szórása Dunába (hajós) | IMG-226, 393, 394, 395 | 226 jog; 393 kollázs csere; 394 ellenőrizendő; 395 törlés | → hajó a Dunán, koszorú a vízen (partnertől, engedéllyel) |
| Hamvak temetése | IMG-390, 391 (200 px) | Cserélendő | → urnafal / urnasír budapesti temetőben (saját, ember nélkül) |
| Ravatalozó terem / galéria | IMG-401, 402 (200 px); IMG-342–347 (600 px) | átmenetileg 345/346; **újrafotózás** | → az Ernő utcai terem nappali, természetes fénnyel, kétféle elrendezésben (koporsós / urnás), 8–10 kép |
| Polgári búcsúztatás | IMG-396 (stég, stock) | Cserélendő | → szónok a ravatalozóban hátulról / részlet (beleegyezéssel) |
| Teendők haláleset után | IMG-411 (stock) | Cserélendő | → kép nélkül vagy nyugodt irodai részlet; a lépéssor ikonokkal |
| Szükséges iratok | IMG-398 (régi iratok, 200 px) | Cserélendő | → kép nélkül; ellenőrzőlista-ikonok |
| Elérhetőség / irodák | IMG-397 (egyetlen irodafotó) | átmenetileg megtartható | → **5 iroda bejárata és belső tere** (irodánként 2–3 kép), térkép mellé |
| Urnák | 108 termékfotó (400 × 500) | megtartható termékrácsba, **beszállítói engedéllyel** | → nagyobb felbontású változatot a beszállítótól kérni (min. 1200 × 1500) |
| Sírjelző | 9 termékfotó + 6 temetői fotó (szociális temetés oldal) | megtartható | → ugyanaz, nagyobb felbontásban |
| Textíliák | 22 urnaterítő/-háló fotó (fekete vignetta) | Újrafotózandó | → semleges (világos) háttér, egységes megvilágítás |
| Szociális temetés | IMG-405–410 | átmenetileg | → – |
| Fiumei úti temető | IMG-413 (200 px), IMG-414 (azonosítható személyek) | 414 ellenőrizendő (személyiségi jog) | → a temető saját, emberek nélküli fotója |
| Árgarancia / Egyedi kedvezmény | IMG-403, 400 (jelvények) | Törlendő | → kép nélkül |
| Hírek (36 cikk) | 140 hír-illusztráció | **Nem migrálandó** | → ha a hírek archívumként megmaradnak: kép nélkül, vagy saját, jogtiszta illusztráció |

## 7. Cserére szoruló képek – összesítő lista

### Törlendő (nem illik, klisé vagy elavult) – 11 kép
IMG-224, IMG-225, IMG-382 (számológép) · IMG-380, IMG-400, IMG-403 (árgarancia-jelvények) · IMG-399 („Visszahívjuk!” grafika) · IMG-392 („Thank you”) · IMG-395 (hidegtál-torony) · IMG-412 (gondolkodó nő, stock) · IMG-421 (logó a sliderből)

### Túl kicsi – cserélendő (600 px alatti tartalmi kép) – 26 kép
IMG-221 (472 px), IMG-222, IMG-223, IMG-379, IMG-381, IMG-383, IMG-384, IMG-385, IMG-387, IMG-389, IMG-390, IMG-391, IMG-396, IMG-398, IMG-401, IMG-402, IMG-409, IMG-411, IMG-413, IMG-415, IMG-416 + a slider 5 képe (IMG-419–423, 522 × 201)

### Elavult stílus – újrafotózandó – 29 kép
IMG-357–378 (22 textilfotó, fekete vignetta) · IMG-342–347 (ravatalozó, dátumozott enteriőr) · IMG-418 (raszteres logó)

### Jogilag tisztázandó, mielőtt bármire felhasználnák – kiemelt
IMG-226 és IMG-423 (EXIF: judit-fotovideo.ro) · IMG-414 és IMG-384 (azonosítható személyek) · IMG-385 (jármű – saját?) · IMG-394 (hajós partner?) · IMG-404 (krematórium?)

### Hiányzó, de hivatkozott képek (404) – a hivatkozást törölni kell
7 kép a `pages/szomorufuz-temetkezes/…` útvonalon (/hamvasztas-urnakiadas/, /hamvasztas-menete/) · 2 sablonkép (`pic.jpg`, `tabs.gif`)

### Nem migrálandó
81 platform-sablongrafika · 140 hír-illusztráció

## 8. Fotózási terv (javaslat az új weboldalhoz)

| Téma | Képek száma | Megjegyzés |
|---|---|---|
| 5 iroda: bejárat (utcáról) + fogadótér | 10–15 | NAP-adatokkal egyező címtábla látszódjon; nappali fény |
| Munkatársak portréi (egyéni + csoport) | 8–12 | írásos hozzájárulás (GDPR), visszafogott öltözet, természetes mosoly |
| Ügyfélfogadás-jelenet (modellekkel vagy munkatársakkal) | 4–6 | arcok nélkül vagy hozzájárulással; empatikus, nem „üzleti” |
| Ravatalozó (Ernő u.): üres terem, koporsós és urnás elrendezés | 8–10 | széles látószög, természetes fény |
| Koporsó-bemutatóterem, urnaválaszték | 6–8 | részletek, anyagok |
| Szóróparcella, urnafal, budapesti temetők (emberek nélkül) | 6–10 | a temetők fotózási szabályainak betartásával |
| Hajós temetés (partnerrel) | 4–6 | partner engedélyével |
| Hero-hangulatképek (szomorúfűz, Duna-part, fény) | 4–6 | 2400 px+, csendes, reményt sugalló |
| Termékek újrafotózása (textíliák) / nagy felbontású beszállítói képek | 20–30 | világos, semleges háttér |

**Formátum és szállítás:** RAW + JPEG (min. 4000 px hosszú oldal), sRGB. A webre WebP/AVIF és `srcset` (400 / 800 / 1200 / 1600 / 2400 px). **A szerződésben rögzíteni kell** a korlátlan webes és marketing-felhasználási jogot és a módosítás jogát, valamint a fotós nevének feltüntetési igényét.

**Becsült költség:** a stratégiai elemzés K-csomagjában szereplő fotózási tétel (150–600 ezer Ft nettó) **legfeljebb az 1–2 napos alapfotózást** fedezi (irodák, munkatársak, ravatalozó). A teljes terv kb. 2–3 fotósnapot igényel – ez a költségbecslés „magas” sávjához közelít.

**Stílusirány:** természetes, meleg fény; csend és nyugalom; valódi emberek és helyek; semmi színpadias gyász, semmi üzleti stock; egységes színkezelés (meleg semleges tónusok), hogy a képek az új, nyugodt arculati palettához illeszkedjenek.

## 9. Javasolt következő lépések

1. **Jogi tisztázás indítása (1–2 hét):** beszállítói engedélyek (125 kép), a stockvásárlások bizonylatai (19), megkeresés a judit-fotovideo.ro felé (IMG-226/423), a saját fotók szerzői.
2. **Fordított képkeresés** a 34 stock- és ismeretlen eredetű képre.
3. **A beszállítóktól nagyobb felbontású termékfotók** bekérése (min. 1200 × 1500 px).
4. **Fotózás megrendelése** a fenti terv szerint, felhasználási szerződéssel – lehetőleg a design-fázissal párhuzamosan (a stratégiai ütemterv 31–60. napja).
5. A jelenlegi oldalon azonnal: a **9 hiányzó képhivatkozás** és a **törlendő klisék** eltávolítása (az audit FUN-06 tételéhez kapcsolódik).
