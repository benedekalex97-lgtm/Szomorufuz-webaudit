# Hibajegyzék (Issue Register)

**Vizsgált oldal:** https://www.budapest-temetkezes.hu · **Audit dátuma:** 2026. november 2.
**Módszer:** kizárólag publikus, olvasó jellegű vizsgálat (crawler, Playwright/Chromium, axe-core, Lighthouse 12.8.2, HTTP-fejlécek). Űrlap nem lett beküldve.

## Jelmagyarázat

**Súlyosság**

| Szint | Jelentés |
|---|---|
| 🔴 Kritikus | Közvetlenül megakadályozza a kapcsolatfelvételt / ügyfélvesztést okoz, azonnal javítandó |
| 🟠 Magas | Jelentős üzleti, jogi, SEO- vagy akadálymentességi kockázat, 1–4 héten belül javítandó |
| 🟡 Közepes | Érezhetően rontja az élményt vagy a láthatóságot, 1–3 hónapon belül |
| 🟢 Alacsony | Minőségi, karbantartási kérdés |

**Bizonyítottság**

| Jelölés | Jelentés |
|---|---|
| **B** – Bizonyított | Méréssel, képernyőképpel vagy forráskóddal igazolt hiba |
| **F** – Feltételezett | Erős jelek utalnak rá, de a publikus oldalról nem igazolható teljes bizonyossággal (pl. proxy mögötti mérés, szerveroldali ok) |
| **J** – Javaslat | Nem hiba, hanem fejlesztési lehetőség |

**Ráfordítás** (becsült fejlesztői/szerkesztői idő): XS < 1 óra · S 1–4 óra · M 0,5–2 nap · L 3–10 nap · XL > 2 hét

**Bizonyítékfájlok:** `data/crawl.json` (crawl), `data/browser-audit.json` (Playwright + axe), `data/functional-test.json`, `data/consent-check.json`, `data/lighthouse/*.html|json`, `screenshots/*`.

---

## Összesítő táblázat

| ID | Rövid leírás | Súlyosság | Bizonyítottság | Ráfordítás |
|---|---|---|---|---|
| FUN-01 | „Információ: +36 30 847-1915” felirat más számot (313-7920) hív – minden oldalon | 🔴 Kritikus | B | XS |
| FUN-02 | Az árajánlatkérő oldalakon az „Ügyelet” link nem létező számot hív (`tel:+3638471915`) | 🔴 Kritikus | B | XS |
| CNV-01 | Nincs elérhető árlista; hamvasztási ár sehol nem szerepel, az „Árlista” link 404 | 🔴 Kritikus | B | M |
| UX-01 | Mobilon nincs látható hívás-gomb; az első telefonszám 4 793 px mélyen van | 🔴 Kritikus | B | S |
| FUN-03 | `/arlista/` 404 – a főoldal szövege és hírek erre hivatkoznak | 🟠 Magas | B | XS |
| FUN-04 | `tel:` előtag nélküli link végtelen URL-láncot (crawl-csapdát) generál | 🟠 Magas | B | XS |
| LEG-01 | Süti-sáv: előre bepipált marketing-süti, nincs „Elutasítom”, ráutaló hozzájárulás | 🟠 Magas | B | S–M |
| UX-09 | Nem egyértelmű, hogy éjjel / hétvégén kit lehet hívni (0–24 elérhetőség) | 🟠 Magas | B | XS–S |
| CNV-02 | 30–37 mezős ajánlatkérő űrlapok, mobilon 2 200 px magasak | 🟠 Magas | B | M |
| CNV-03 | 13 különböző telefonszám, nincs egyértelmű elsődleges szám | 🟠 Magas | B | S |
| SEO-04 | NAP-ellentmondások (telefonszám, irányítószám, házszám, márkanév) | 🟠 Magas | B | S |
| SEO-03 | Nincs strukturált adat (LocalBusiness / FuneralHome) | 🟠 Magas | B | S–M |
| SEO-01 | Az aloldalakon nincs H1 címsor | 🟠 Magas | B | S |
| SEO-02 | A belső oldalak felén nincs canonical; a hírek canonicalja `http://` | 🟠 Magas | B | S |
| SEO-07 | Üres / „feltöltés alatt” oldalak indexelhetők (GYIK, ÁSZF, Üzenőfal…) | 🟠 Magas | B | S |
| TEC-01 | Mixed content: a Google Ads konverziókód (`http://…conversion.js`) blokkolva | 🟠 Magas | B | S |
| TEC-02 | Elavult, ismert sérülékenységű JS-könyvtárak (jQuery 1.12.4, jQuery UI 1.8.24) | 🟠 Magas | B | M–L |
| TEC-03 | A HTML 1 évig gyorsítótárazható (`max-age=31536000`) ellentmondó fejlécekkel | 🟠 Magas | B | XS |
| TEC-06 | Gyenge mobil teljesítmény (LCP 3,5–5,7 s, CLS 0,23–0,35, 1,7 MB főoldal) | 🟠 Magas | B | M |
| FUN-07 | Időszakos 502-es hibák és kapcsolatbontások, CSS rossz MIME-típussal | 🟠 Magas | B/F | M |
| FUN-12 | Űrlapmezők: nincs `type=email/tel`, `required`, `autocomplete` | 🟠 Magas | B | S |
| UX-02 | A nyitó slider első képe a „temetkezes.hu” logó; automatikus forgatás | 🟠 Magas | B | S |
| UX-03 | Túlzsúfolt, logikátlan navigáció (24 menüpont, duplikált oldalak) | 🟠 Magas | B | M |
| UX-05 | Gyászoló családhoz nem illő, értékesítési hangnem több oldalon | 🟠 Magas | B | M |
| UX-06 | Hiányzó bizalomépítő elemek (munkatársak, vélemények, valós fotók) | 🟠 Magas | B | M |
| A11Y-01 | A nagyítás tiltva (`maximum-scale=1`) | 🟠 Magas | B | XS |
| A11Y-02 | Elégtelen színkontraszt (akár 1,4:1) | 🟠 Magas | B | S |
| A11Y-03 | Űrlapmezők címke nélkül (88 elem) | 🟠 Magas | B | S |
| A11Y-04 | Nem látható billentyűzetfókusz, nincs „ugrás a tartalomra” link | 🟠 Magas | B | S |
| FUN-05 | További belső 404-ek (`/koporsok/` 16 linkkel stb.) | 🟡 Közepes | B | S |
| FUN-06 | Hiányzó / törött képek (régi útvonal, 404) | 🟡 Közepes | B | S |
| FUN-08 | Megszűnt Facebook Messenger chat-bővítmény töltődik | 🟡 Közepes | B | XS |
| FUN-10 | A főoldali térképlink rossz házszámra (Izabella u. 68.) mutat | 🟡 Közepes | B | XS |
| FUN-11 | Mobilmenü: lapos 24 elemű lista, nincs `aria-expanded`, gyenge kontraszt | 🟡 Közepes | B | S |
| TEC-04 | User-Agent alapú kiszolgálás `Vary: User-Agent` nélkül | 🟡 Közepes | B | XS |
| TEC-05 | Hiányzó biztonsági HTTP-fejlécek (HSTS, CSP, X-Content-Type-Options…) | 🟡 Közepes | F | S |
| TEC-07 | 17 render-blokkoló script a `<head>`-ben, duplikált xajax | 🟡 Közepes | B | M |
| TEC-08 | Duplikált URL-ek 200-as válasszal (`/argarancia`, `/index.php/`, `?mobile=`) | 🟡 Közepes | B | S |
| SEO-05 | Title-hibák: elírások, túl hosszú, duplikált címek | 🟡 Közepes | B | S |
| SEO-06 | Gyenge vagy hiányzó meta description-ök (pl. „Remarketing”) | 🟡 Közepes | B | S |
| SEO-08 | Sitemap / robots.txt hiányosságok | 🟡 Közepes | B | XS–S |
| SEO-09 | Elavult tartalom: a legfrissebb hír 2014. 12. 11-i | 🟡 Közepes | B | M |
| SEO-10 | Nincsenek irodánkénti / kerületi helyi landoló oldalak | 🟡 Közepes | J | L |
| SEO-11 | A remarketing-landoló oldal indexelhető és a sitemapben van | 🟡 Közepes | B | XS |
| UX-04 | Elavult (≈2012-es) vizuális megjelenés, inkonzisztens színek | 🟡 Közepes | B | L–XL |
| UX-07 | Helyesírási és gépelési hibák | 🟡 Közepes | B | S |
| UX-08 | Tartalmi ellentmondások (iratbeszerzés, kedvezményrendszer) | 🟡 Közepes | B | S |
| UX-10 | Mobilon vízszintes túlcsordulás és üres sáv a slider alatt | 🟡 Közepes | B | S |
| A11Y-05 | Hiányzó landmarkok (`main`, `nav`), hibás címsor-sorrend | 🟡 Közepes | B | S |
| A11Y-06 | Automatikusan forgó slider szüneteltetés nélkül, névtelen nyilak | 🟡 Közepes | B | S |
| A11Y-07 | Kis érintési célpontok (13×13 px rádiógomb, 15×50 px nyíl) | 🟡 Közepes | B | S |
| A11Y-09 | Desktopon 12 px-es betűméret, sorkizárt szöveg, piros kiemelések | 🟡 Közepes | B | S |
| LEG-02 | Facebook- és régi Ads-erőforrások töltődnek a hozzájárulás előtt | 🟡 Közepes | B | S |
| LEG-03 | Az ÁSZF oldal üres („A tartalom feltöltés alatt.”) | 🟡 Közepes | B | S |
| CNV-04 | Nincs egyértelmű „mi történik ezután” / válaszidő az űrlapoknál | 🟡 Közepes | B | XS |
| FUN-09 | „Árjegyzék” csempe a főoldalon kattinthatatlan | 🟢 Alacsony | B | XS |
| FUN-13 | Angol nyelvű `alert()` hibaüzenet xajax-hiba esetén | 🟢 Alacsony | F | XS |
| TEC-09 | Kétlépcsős átirányítás (http, nem-www → https www) | 🟢 Alacsony | B | XS |
| TEC-10 | Elavult markup: XHTML 1.0 Transitional, inline stílusok, többszörösen escape-elt kód | 🟢 Alacsony | B | L (redesignban) |
| SEO-12 | Gyenge horgonyszövegek („IDE”), kulcsszóhalmozott `title` attribútumok | 🟢 Alacsony | B | S |
| SEO-13 | 202 üres alt-szöveg, Open Graph hiányzik a fő oldalakon | 🟢 Alacsony | B | S |
| A11Y-08 | Iframe-ek `title` nélkül | 🟢 Alacsony | B | XS |

Összesen: **4 kritikus, 25 magas, 26 közepes, 7 alacsony** tétel (62 db).

---

## Részletes hibalapok

### 🔴 Kritikus

#### FUN-01 – Az „Információ” telefonszám mögött más szám van
- **Érintett URL:** minden oldal jobb oldalsávja (106/107 vizsgált oldal), pl. https://www.budapest-temetkezes.hu/
- **Súlyosság:** Kritikus · **Bizonyítottság:** B · **Ráfordítás:** XS (5 perc)
- **Bizonyíték:** forráskód: `<p>Információ: <a href="tel:+36303137920">+36 (30) 847-1915</a></p>` – a látható szám 847-1915, a link a rákoskeresztúri iroda 313-7920-as számát tárcsázza. Lásd `data/crawl.json` → `tel_links`.
- **Probléma és hatás:** a mobilon a számra koppintó hozzátartozó nem azt a vonalat hívja, amit lát. Ha a 313-7920 nem a központi információs vonal, a hívás rossz helyre fut, vagy foglalt/nem fogadott marad – a legsürgősebb helyzetben (haláleset után) ez közvetlen ügyfélvesztés.
- **Javítás:** a linket `tel:+36308471915`-re javítani. Utána az összes `tel:` linket automatikusan összevetni a látható számmal (ld. `scripts/crawl.py` kimenete).

#### FUN-02 – Hibás „Ügyelet” telefonlink az árajánlatkérő oldalakon
- **Érintett URL:** https://www.budapest-temetkezes.hu/arajanlat-keres-itt/ , https://www.budapest-temetkezes.hu/arajanlatkeres/
- **Súlyosság:** Kritikus · **Bizonyítottság:** B · **Ráfordítás:** XS
- **Bizonyíték:** `Ügyelet: <a href="tel:+3638471915">+36 30 847 1915</a>` – a hívószámból hiányzik a „0” (30 helyett 3 körzetszám), a tárcsázott szám nem létező/rossz szám. Képernyőkép: `screenshots/desktop-arajanlat-fold.png` (alul „Ügyelet: +36 30 847 1915”).
- **Probléma és hatás:** pont azon az oldalon, ahol a látogató ajánlatot kérne, és pont az ügyeleti számnál nem jön létre a hívás.
- **Javítás:** `tel:+36308471915`. A WYSIWYG-szerkesztőben az összes telefonszám-linket egyetlen központi beállításból kellene generálni.

#### CNV-01 – Nincs árlista, a hamvasztási ár nem szerepel az oldalon
- **Érintett URL:** https://www.budapest-temetkezes.hu/ , /hamvasztas-urnakiadas/ , /hamvasztasos-temetes/ , /arlista/ (404)
- **Súlyosság:** Kritikus · **Bizonyítottság:** B · **Ráfordítás:** M (tartalom + ároldal)
- **Bizonyíték:** a teljes publikus oldalon egyetlen ár szerepel: „Koporsós temetési díj: 232.288 Ft-tól” (/koporsos-temetes/). Hamvasztási ár sehol. A főoldal szerint „Erről a tényről az **Árlista** menüpont alatt, egy kattintással meggyőződhet” – a link 404 (`screenshots/desktop-arlista-fold.png`). A főoldali „Árjegyzék – Temetkezési és hamvasztási szolgáltatási árak pontos részletezése” csempe nem kattintható.
- **Probléma és hatás:** a hamvasztás a fő szolgáltatás (slider: „rejtett költségek nélkül”), de az árérzékeny látogató (B forgatókönyv) nem talál kiindulási árat, ezért összehasonlító oldalra vagy versenytárshoz megy. Az „árgarancia” ígéret ár nélkül hiteltelen.
- **Javítás:** önálló, indexelhető `/arak/` oldal csomagárakkal („-tól” árak, mit tartalmaz / mit nem), hamvasztás, szórás, hajós temetés, koporsós temetés bontásban; a főoldali „Árlista” és „Árjegyzék” erre mutasson; 301-es átirányítás `/arlista/` → `/arak/`.

#### UX-01 – Mobilon nincs látható, azonnali hívás-lehetőség
- **Érintett URL:** minden oldal mobilnézetben; kiemelten https://www.budapest-temetkezes.hu/
- **Súlyosság:** Kritikus · **Bizonyítottság:** B · **Ráfordítás:** S
- **Bizonyíték:** 390×844 viewporton a főoldalon az első `tel:` link 4 793 px mélyen van (`data/browser-audit.json` → `mobile:home.metrics.telLinks`), a hamvasztás oldalon 3 640 px-en. Az első képernyőt a cím, a slider és a 39%-os süti-sáv tölti ki (`screenshots/mobile-home-fold.png`).
- **Probléma és hatás:** a haláleset után azonnal segítséget kereső hozzátartozó (A és D forgatókönyv) 5–6 képernyőnyit görget, mire telefonszámot talál.
- **Javítás:** rögzített (sticky) alsó sáv mobilon: „📞 Hívjon most – 0–24 ügyelet” + „Ajánlatkérés” gomb; a fejlécben is kattintható szám. Min. 48 px magas érintési felület.

### 🟠 Magas

#### FUN-03 – Az „Árlista” oldal nem létezik (404)
- **Érintett URL:** https://www.budapest-temetkezes.hu/arlista/ ← hivatkozik rá: `/`, `/?mobile=no`, `/?mobile=1`, `/hirek-aktualitasok/mateszsz-taggyules/27899/`, `/hirek-aktualitasok/temetkezesi-kultura/26254/`
- **Bizonyíték:** HTTP 404, „Az oldal nem található – Hiba 404” (`screenshots/*-arlista-*.png`).
- **Hatás:** a legfontosabb döntési információ (ár) zsákutcába vezet; bizalomvesztés.
- **Javítás:** lásd CNV-01; addig 301 átirányítás egy létező ároldalra vagy az ajánlatkérésre. **Ráfordítás:** XS

#### FUN-04 – Végtelen URL-lánc az Elérhetőség oldalon
- **Érintett URL:** https://www.budapest-temetkezes.hu/elerhetoseg/
- **Bizonyíték:** `<a href="tel:+36305767206">06 (30) 576-7206</a><a href="+36305767206"></a>` – az üres, `tel:` nélküli link relatív URL-ként értelmeződik: `/elerhetoseg/+36305767206/`, `/elerhetoseg/+36305767206/+36305767206/` … és mindegyik **200-as** választ ad az Elérhetőség tartalmával (a crawler 8 ilyen szintet talált, `data/crawl.json`).
- **Hatás:** crawl-csapda és duplikált tartalom (9 azonos title „Iroda megközelíthetőség”), pazarolt crawl-keret.
- **Javítás:** az üres `<a>` törlése; szerveroldalon nem létező útvonal-szegmensekre 404. **Ráfordítás:** XS

#### LEG-01 – Nem megfelelő süti-hozzájárulás
- **Érintett URL:** minden oldal
- **Bizonyíték:** `<input type="checkbox" name="marketing_statistics" checked="checked">`; szöveg: „Ha tovább használja honlapunkat azzal hozzájárul a cookie-k használatához.”; nincs elutasítás gomb (`data/functional-test.json` → `cookieBanner`). Mobilon a sáv a képernyő 39%-át takarja és áttetsző, a mögötte lévő szöveggel összefolyik (`screenshots/mobile-elerhetoseg-fold.png`). Elírás: „statiszktikai”.
- **Hatás (jogi kockázat, nem jogi tanács):** az EUB C-673/17. (Planet49) ítélete és a GDPR szerint az előre bejelölt jelölőnégyzet és a „továbblépés = hozzájárulás” nem érvényes hozzájárulás; NAIH-bírság kockázat. Mobilon olvashatatlan és zavaró.
- **Javítás:** „Elfogadom mind” / „Elutasítom” / „Beállítások” egyenrangú gombokkal, alapból üres marketing-jelölővel, Google Consent Mode v2 `denied` alapállapottal; tömör, nem átlátszó háttér. **Ráfordítás:** S–M

#### UX-09 – Tisztázatlan 0–24 órás elérhetőség
- **Érintett URL:** /elerhetoseg/, főoldal, /teendok-halaleset-utan/
- **Bizonyíték:** „Hétfő – Péntek 8:00–16:00, Szombat–Vasárnap zárva”; „Ügyelet: +36 30 847 1915 (6:00 – 22:00 óra között hívható)”; „Ügyeleti halottszállítás: 06 (30) 849-3538 (06-30-ÜGYELET)”. Sehol nem szerepel, hogy 22 és 6 óra között vagy hétvégén mi a teendő.
- **Hatás:** az éjszaka, otthon bekövetkezett haláleset (A forgatókönyv) a leggyakoribb sürgős helyzet. Ha nem egyértelmű, hogy hívható-e a cég, a család a következő találatot hívja.
- **Javítás:** ha van 0–24 halottszállítási ügyelet: egyetlen, mindenhol kiemelt „0–24 órás ügyelet” szám. Ha nincs: egyértelmű útmutató („22 és 6 óra között hívja a … számot / ezt tegye”). **Ráfordítás:** XS–S

#### CNV-02 – Túl hosszú ajánlatkérő űrlapok
- **Érintett URL:** /arajanlat-keres-itt/, /arajanlatkeres/, /argarancia/, /egyedi-kedvezmeny/ (form_1465 – 37 mező); /hamvasztas-urnakiadas/ és 4 további (form_1483 – 30 mező); /ravatalozo-terem/ (27); /hamvak-szorasa-temeto/ (25); /koporsos-temetes/ (24); /visszajelzes-kuldese/ (37)
- **Bizonyíték:** mobilon az árajánlat-űrlap 2 201 px magas és 1 615 px-nél kezdődik (`data/functional-test.json`, `screenshots/mobile-arajanlat-form.png`).
- **Hatás:** gyászoló hozzátartozótól 8–10 kérdéscsoport (sírhely típusa, elhalálozás helye stb.) megválaszolása magas lemorzsolódást okoz; sok kérdésre a látogató nem tudja a választ.
- **Javítás:** kétlépcsős űrlap: 1. lépés név + telefon + temetés típusa + „Visszahívást kérek” (3–4 mező); 2. lépés opcionális részletek. Minden kérdésnél „Nem tudom / megbeszélnénk” opció. **Ráfordítás:** M

#### CNV-03 – Túl sok telefonszám, nincs elsődleges
- **Érintett URL:** minden oldal oldalsávja
- **Bizonyíték:** oldalanként 11–13 egyedi `tel:` link (5 iroda × vezetékes + mobil, információ, iroda, halottszállítás). A főoldalon emellett +36 1 720 2710 is szerepel, ami az oldalsávban nincs (`data/crawl.json`).
- **Hatás:** döntési teher stresszhelyzetben („melyiket hívjam?”).
- **Javítás:** egy kiemelt központi szám (0–24), az irodák számai az Elérhetőség oldalon, irodánkénti kártyákon. **Ráfordítás:** S

#### SEO-04 – NAP (név–cím–telefon) ellentmondások
- **Érintett URL:** /, /elerhetoseg/, /ceginformaciok/, oldalsáv
- **Bizonyíték:**
  - Telefon: főoldal és /ceginformaciok/: „+36 1 720 2710” ; oldalsáv, /elerhetoseg/: „+36 1 919 0170” (és fax is 919 0170).
  - Zuglói iroda: oldalsáv „**1147** Budapest, Thököly út 167.”, /elerhetoseg/ „**1146** Budapest, Thököly út 167.”
  - Központi iroda: szöveg „Izabella utca **65.**”, de a főoldali térképlink „Izabella u. **68**”-ra mutat.
  - Márkanév: „Szomorúfűz Temetkezés”, de a nyitóképen „temetkezes.hu” logó, e-mail-domain `@temetkezes.hu`.
  - /ceginformaciok/: telephelyként csak Debrecen és Nyíregyháza szerepel, az 5 budapesti iroda nem.
- **Hatás:** a Google helyi rangsorolása a NAP-konzisztenciára épül (Cégprofil vs. weboldal vs. katalógusok); ellentmondás bizalomvesztést és gyengébb helyi helyezést okoz (F – a Cégprofil adatai nem voltak vizsgálhatók).
- **Javítás:** irodánként egyetlen hiteles NAP-adat, ugyanúgy a weboldalon, a Google Cégprofilban és a katalógusokban. **Ráfordítás:** S

#### SEO-03 – Nincs strukturált adat
- **Érintett URL:** összes oldal (0/107 oldalon van JSON-LD)
- **Bizonyíték:** `data/crawl.json` → `jsonld` mindenhol üres.
- **Hatás:** nincs gépileg olvasható cégnév, nyitvatartás, iroda-címek, telefonszám; elmaradó helyi és rich-result lehetőségek.
- **Javítás:** `FuneralHome` (LocalBusiness altípus) a főoldalon `Organization`-nel, irodánként külön `FuneralHome` `department`/`location` blokk (cím, geo, telefon, nyitvatartás), `BreadcrumbList`, a GYIK elkészülte után `FAQPage`; szolgáltatásoldalakon `Service` + `Offer` ár-tartománnyal. Mintakód: `reports/seo-audit.md`. **Ráfordítás:** S–M

#### SEO-01 – Hiányzó H1 az aloldalakon
- **Érintett URL:** minden aloldal (az axe 13/13 vizsgált aloldalon jelezte: `page-has-heading-one`)
- **Bizonyíték:** csak a főoldal desktop-változatában van H1 („Szomorúfűz Temetkezés Budapest”, a logó szövege); az aloldalakon a fő cím H2 (pl. „Koporsós temetés”), a crawl szerint a H1 üres.
- **Hatás:** gyengébb téma-jelzés a keresőknek, képernyőolvasós navigáció nehezebb.
- **Javítás:** oldalanként egy H1 az oldal fő témájával („Koporsós temetés Budapesten – teljes körű ügyintézés”); a logó ne legyen H1. **Ráfordítás:** S (sablon)

#### SEO-02 – Canonical hiány és rossz protokoll
- **Érintett URL:** 57/107 oldalon nincs canonical, köztük a főoldal és minden szolgáltatásoldal (/hamvasztas-urnakiadas/, /koporsos-temetes/, /elerhetoseg/ …); 50 hír/jogszabály/termékoldal canonicalja `http://www.…`
- **Bizonyíték:** `data/crawl.json` → `canonical`.
- **Hatás:** a `?mobile=no`, `?mobile=1`, `/index.php/`, `/argarancia` és a FUN-04 duplikátumok között a Google maga dönt; a http canonical egy átirányított URL-re mutat.
- **Javítás:** minden oldalon önhivatkozó, `https://www.` canonical. **Ráfordítás:** S

#### SEO-07 – Üres vagy „feltöltés alatt” oldalak indexelhetők
- **Érintett URL:** /gyakori-kerdesek/ („Még nincs tartalom feltöltve.”), /a-sz-f/ („A tartalom feltöltés alatt.”), /uzenofal/ („Még nincs hozzászólás.”), /textiliak/ (4 szó), /sirjelzo/ (21), /temetkezesi-szolgaltata/ (22 szó, csonka cím), /temetkezesi-galeria/ (10), /ravatalozo-galeria/ (25)
- **Bizonyíték:** `data/crawl.json` → `word_count_center`; mind a sitemapben.
- **Hatás:** vékony tartalom, rossz minőségjelzés; a látogatónak elhagyatott oldal benyomását kelti (különösen az üres GYIK és az üres vendégkönyv).
- **Javítás:** a GYIK megírása (≥15 kérdés, lásd conversion-audit), a többi tartalom feltöltése vagy `noindex` + sitemapből törlés, az Üzenőfal megszüntetése. **Ráfordítás:** S (tartalommal M)

#### TEC-01 – Blokkolt Google Ads konverziókód (mixed content)
- **Érintett URL:** minden oldal, ahol a régi konverziós snippet van (főoldal, szolgáltatás- és ajánlatoldalak)
- **Bizonyíték:** konzol: „Mixed Content: … requested an insecure script 'http://www.googleadservices.com/pagead/conversion.js'. This request has been blocked” (24 betöltésből 24, `data/browser-audit.json`). A `<noscript>` blokk többszörösen escape-elt (`&amp;amp;amp;…`).
- **Hatás:** ha a hirdetési fiók még erre a címkére épít, a konverziómérés nem működik → a kampányoptimalizálás vakon fut. Lighthouse „Does not use HTTPS” hibát jelez.
- **Javítás:** a régi snippet eltávolítása; konverziókövetés a GTM-ben (GTM-NBJCMVB) gtag/Google Ads címkével, consent-alapon. **Ráfordítás:** S

#### TEC-02 – Elavult, sérülékeny JavaScript-könyvtárak
- **Érintett URL:** minden oldal
- **Bizonyíték:** `common/jquery/1.12.4/jquery-1.12.4.min.js`, `common/jquery/1.8.24ui/jquery-ui.min.js`, `xajax 0.5 rc1`, jquery.tools, galleria, qtip, uploadifive – összesen 17 script a `<head>`-ben.
- **Hatás:** a jQuery 1.12.4-hez publikus CVE-k tartoznak (CVE-2019-11358, CVE-2020-11022, CVE-2020-11023), a jQuery UI 1.8.24-hez is (pl. CVE-2016-7103, CVE-2021-41182/41183/41184). A tényleges kihasználhatóság a használattól függ (**F**), de a biztonsági auditokon és a Lighthouse Best Practices pontszámon is rontó tényező.
- **Javítás:** rövid távon jQuery 3.7.x + jQuery UI 1.13.x + jQuery Migrate; hosszabb távon a CMS-sablon cseréje (ld. roadmap). **Ráfordítás:** M–L

#### TEC-03 – Egy évre gyorsítótárazható HTML
- **Érintett URL:** minden HTML-oldal
- **Bizonyíték:** válaszfejlécek: `cache-control: max-age=31536000`, `expires: Thu, 19 Nov 1981`, `pragma: no-cache`, `set-cookie: PHPSESSID=…`.
- **Hatás:** a `Cache-Control` elsőbbséget élvez, így böngészők/köztes cache-ek akár egy évig régi HTML-t mutathatnak (pl. javított telefonszám helyett a hibásat). Munkamenet-sütivel együtt köztes cache-ben adatszivárgás kockázata.
- **Javítás:** HTML-re `Cache-Control: no-cache` (vagy rövid `max-age` + `private`), statikus fájlokra hosszú cache verziózott URL-lel. **Ráfordítás:** XS

#### TEC-06 – Gyenge mobil teljesítmény
- **Érintett URL:** főoldal és kulcsoldalak
- **Bizonyíték (Lighthouse mobil, laborkörnyezet):** főoldal Performance 49, FCP 4,4 s, LCP 5,7 s, CLS 0,234, Speed Index 26,3 s, 1 758 KiB; koporsós temetés CLS 0,353; árajánlat CLS 0,315. Képoptimalizálással ~1,2 MB megtakarítás, render-blokkoló erőforrások ~2,4 s. Részletek: `reports/technical-audit.md`.
- **Hatás:** a Google „jó” küszöbe LCP ≤ 2,5 s, CLS ≤ 0,1; lassú mobil élmény → visszafordulás, rosszabb rangsor.
- **Javítás:** slider-képek WebP/AVIF-be és méretre vágva, `width/height` attribútumok, lusta betöltés, scriptek `defer`, a slider eltávolítása mobilon. **Ráfordítás:** M

#### FUN-07 – Időszakos szerverhibák (502, kapcsolatbontás)
- **Érintett URL:** képek és CSS-ek, pl. `/pages/avszomfuzbud/contents/static/17/1321219915_200x.jpg` (502), `/design/13/colors/1/style/pics/menuside_li_hover.gif` (502), `/design/mobile/colors/20.css` (`text/plain` MIME → a böngésző nem alkalmazta)
- **Bizonyíték:** `data/browser-audit.json` (7 db 502, 1 MIME-hiba); a curl-lel végzett mérések során többször „Connection reset by peer”. Egy mobilos betöltésnél a fejléc más színnel jelent meg (`mobile-home-fold.png` sötét, a többi oldalon cián), ami a hiányzó CSS-sel konzisztens.
- **Megjegyzés (F):** a mérés egy kimenő proxyn keresztül történt; a kapcsolatbontások egy része a szerver tűzfalából / rate-limitjéből vagy a proxyból is eredhet. A 502-es státuszkódokat és a `text/plain` MIME-t a böngésző a szerver válaszaként kapta.
- **Javítás:** szervernaplók és tárhely-erőforrások ellenőrzése, `.css` → `text/css` MIME, monitorozás (pl. UptimeRobot). **Ráfordítás:** M

#### FUN-12 – Űrlapmezők technikai hiányosságai
- **Érintett URL:** valamennyi űrlap
- **Bizonyíték:** a 37 mezős űrlapon 0 `required`, 0 `type="email"`, 0 `type="tel"`, 0 `autocomplete` (`data/functional-test.json`); a kötelező mezőket csak `*` jelzi.
- **Hatás:** mobilon nem jön fel a megfelelő billentyűzet, nincs automatikus kitöltés, a hibák csak beküldés után derülnek ki.
- **Javítás:** `type="email"`, `type="tel"`, `autocomplete="name|email|tel"`, `required` + `aria-required`, inline hibaüzenetek. **Ráfordítás:** S

#### UX-02 – A nyitókép a „temetkezes.hu” logó, automatikus slider
- **Érintett URL:** minden oldal fejléce (desktopon és mobilon)
- **Bizonyíték:** a slider első diája `404_slide_header.jpg`, alt: „temetkezes.hu logo” (`screenshots/desktop-home-fold.png`, `mobile-hamvasztas-fold.png`); 8 mp-es automatikus váltás.
- **Hatás:** a legértékesebb képernyőterületet egy másik márkanév foglalja el; a látogató bizonytalan, „jó helyen jár-e”. Mobilon a slider alatt ~200 px üres sáv.
- **Javítás:** statikus, nyugodt hero: egy mondatos ígéret („Mellettük állunk az első perctől – 0–24 ügyelet Budapesten”), hívás- és ajánlatkérés-gomb, valós fotó az irodáról/munkatársakról. **Ráfordítás:** S

#### UX-03 – Túlzsúfolt, logikátlan navigáció
- **Érintett URL:** minden oldal
- **Bizonyíték:** felső menü 4 pont + bal oldali menü 20 pont + lábléc; duplikált célok: „Árajánlat kérés – itt!” és „Árajánlatkérés” (ugyanaz az űrlap két URL-en), „Hamvasztásos temetés” / „Hamvasztás urnakiadás” / „Hamvak hazavitele” / „Hamvasztás menete” / „Hamvak temetése”; a „Kezdőoldal” a mobilmenü közepén (5. helyen) van (`screenshots/mobile-menu-open.png`).
- **Hatás:** a hozzátartozó nem tudja eldönteni, hol kezdje.
- **Javítás:** 5 fő menüpont: *Azonnali teendők* · *Szolgáltatások és árak* (Hamvasztás, Koporsós temetés, Szórás/Hajós temetés, Búcsúztatás) · *Ügyintézés és iratok* · *Irodáink* · *Kapcsolat*. **Ráfordítás:** M

#### UX-05 – Nem empatikus, értékesítési hangnem
- **Érintett URL:** /egyedi-kedvezmeny/, /figyelem-/, /teendok-halaleset-utan/, /argarancia/, /online-kedvezmeny/, hírek
- **Bizonyíték (idézetek):**
  - /egyedi-kedvezmeny/: „Kedvezmények csak Önnek! … Ön már láthatta honlapunkat … De valamilyen okból kifolyólag nem kért tőlünk árajánlatot … az egyébként is kifejezetten olcsónak mondható árainkból”
  - /figyelem-/ címe: „Gondolja át miért van ez így?”
  - /teendok-halaleset-utan/: „Önnek egyetlen lényeges dolga van, mielőbb felvenni munkatársunkkal a kapcsolatot! … költségeket, melyek az Ön pénztárcáját terhelnék”
  - /argarancia/: „Próbálja ki cégünket”
  - Hírek: „85 éves lenne Grace Kelly”, „Szokatlan temetési járművek”, „Gyászos ravatal helyett zenés-táncos búcsúparty”
- **Hatás:** a gyászoló látogató manipulatívnak vagy tapintatlannak érezheti; a méltóság és a bizalom sérül.
- **Javítás:** tartalmi stílusútmutató (együttérző, nyugodt, tényszerű; „Ön nincs egyedül – végigvezetjük”), a remarketing-szöveg teljes átírása, a celebhírek archiválása. **Ráfordítás:** M

#### UX-06 – Hiányzó bizalomépítő elemek
- **Érintett URL:** főoldal, „Rólunk” oldal hiányzik
- **Bizonyíték:** nincs munkatárs-bemutatás, nincs alapítási év / tapasztalat, nincs ügyfélvélemény (az Üzenőfal üres: „Még nincs hozzászólás”), stockfotók (számológép, urna), a céginformáció csak a láblécben.
- **Hatás:** temetkezési szolgáltatásnál a bizalom a fő döntési tényező.
- **Javítás:** „Rólunk” oldal arcokkal, valós iroda-/ravatalozófotókkal; Google-vélemények beágyazása; szakmai tagság, engedélyszám (Tem/1/2023) jól látható helyen. **Ráfordítás:** M

#### A11Y-01 – Nagyítás tiltva
- **Érintett URL:** minden oldal mobil-sablonja
- **Bizonyíték:** `<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">`; axe `meta-viewport` (critical), Lighthouse jelzi.
- **Hatás:** WCAG 1.4.4 sérül; idős, gyengénlátó hozzátartozók nem tudják nagyítani a szöveget.
- **Javítás:** `maximum-scale=1` törlése. **Ráfordítás:** XS

#### A11Y-02 – Elégtelen színkontraszt
- **Érintett URL:** 13/13 vizsgált oldal
- **Bizonyíték:** axe `color-contrast` (serious, 69 elem): pl. `.box_share > h3` #eeeeee a #34def5 háttéren = **1,4:1** (elvárt 4,5:1); mobilmenü fehér szöveg világosszürke (#bbb körüli) háttéren (`screenshots/mobile-menu-open.png`).
- **Javítás:** sötétebb kék/szürke háttér vagy sötét szöveg; design tokenek 4,5:1 felett. **Ráfordítás:** S

#### A11Y-03 – Címke nélküli űrlapmezők
- **Érintett URL:** 14 oldal; pl. /tajekoztatas-keres/ (6 mezőből 1 címkézett), terméklapok (0/5), /elerhetoseg/ (1/7)
- **Bizonyíték:** axe `label` (critical) 88 elem.
- **Javítás:** minden mezőhöz `<label for>`. **Ráfordítás:** S

#### A11Y-04 – Nem látható fókusz, nincs átugró link
- **Érintett URL:** minden oldal
- **Bizonyíték:** Tab-bal léptetve a linkek `outline: none`, `box-shadow: none` (`data/functional-test.json` → `keyboardFocus`, `screenshots/desktop-keyboard-focus.png`); nincs „Ugrás a tartalomra” link.
- **Hatás:** WCAG 2.4.7 és 2.4.1 sérül; billentyűzettel használhatatlan.
- **Javítás:** `:focus-visible { outline: 3px solid … }`, skip link. **Ráfordítás:** S

### 🟡 Közepes

#### FUN-05 – További belső 404-ek
- **Érintett URL / hivatkozó oldalak:** `/koporsok/` ← 16 hír; `/hamvak-szorasa-templom/` ← /szocialis-temetes/, /hamvasztasos-temetes/; `/kegyeleti-webaruhaz/urna-13172/13172/` ← /hirek-aktualitasok/a-kegyeleti-diszurnak-torteneterol/31581/; `/temetkezesi-hirek/a-szocialis-temetesi-torveny-szovege/23495/` ← /hirek-aktualitasok/szocialis-temetes-helyett-kegyeleti-jarandosagot-/23529/
- **Bizonyíték:** `data/crawl.json`. **Hatás:** zsákutcák, SEO-értékvesztés. A „Templomban” opció az űrlapon szerepel, de az erről szóló oldal 404.
- **Javítás:** 301 átirányítások a legközelebbi létező oldalra / tartalom pótlása. **Ráfordítás:** S

#### FUN-06 – Hiányzó és törött képek
- **Érintett URL:** /hamvasztas-urnakiadas/ (`/pages/szomorufuz-temetkezes/contents/static/19/1433065839_200x.jpg`, `…/1427461502_200x.jpg` → 404 – régi oldalazonosító az útvonalban)
- **Bizonyíték:** `data/browser-audit.json`; törött kép ikon a desktop képernyőképen (Elérhetőségek blokk mellett).
- **Javítás:** képek újrafeltöltése / hivatkozás javítása. **Ráfordítás:** S

#### FUN-08 – Megszűnt Facebook chat-bővítmény
- **Érintett URL:** minden oldal
- **Bizonyíték:** `https://connect.facebook.net/hu_HU/sdk/xfbml.customerchat.js` – a kérés minden betöltésnél blokkolva (`ERR_BLOCKED_BY_ORB`). A Meta a Messenger Chat Plugint 2024-ben megszüntette (külső tény).
- **Hatás:** felesleges kérés, a látogató nem kap chat-lehetőséget, holott a kód erre utal.
- **Javítás:** eltávolítás; helyette pl. „Visszahívást kérek” vagy WhatsApp/Messenger link. **Ráfordítás:** XS

#### FUN-10 – Rossz házszámra mutató térképlink
- **Érintett URL:** https://www.budapest-temetkezes.hu/ („Az iroda megközelíthetősége térképpel >>> IDE <<<”)
- **Bizonyíték:** a link célja `…/Budapest,+Izabella+u.+68,+1064/…`, a cím az oldalon „Izabella utca 65.”.
- **Javítás:** link javítása a Cégprofil-helyre. **Ráfordítás:** XS

#### FUN-11 – Mobilmenü
- **Érintett URL:** minden oldal, mobil
- **Bizonyíték:** `<a onclick="$('#mobile_menu').slideToggle()…" href="javascript:void(0)">Menü</a>` – nincs `button`, `aria-expanded`, `aria-controls`; a lenyíló lista 24 egyforma súlyú elem; fehér szöveg világosszürkén (`screenshots/mobile-menu-open.png`).
- **Javítás:** `<button aria-expanded>`, csoportosított, rövidebb menü (UX-03), kontraszt. **Ráfordítás:** S

#### TEC-04 – UA-alapú kiszolgálás `Vary` nélkül
- **Bizonyíték:** desktop és mobil User-Agent eltérő HTML-t kap (36 042 B vs. 36 867 B; csak a mobilon van viewport-meta), de a válasz `Vary: Accept-Encoding` – nincs `Vary: User-Agent`. A TEC-03 1 éves cache-sel együtt köztes cache rossz változatot adhat ki.
- **Javítás:** reszponzív sablon (egy HTML minden eszközre), vagy addig `Vary: User-Agent`. **Ráfordítás:** XS (fejléc) / redesign

#### TEC-05 – Hiányzó biztonsági fejlécek (F)
- **Bizonyíték:** a megfigyelt válaszokban nincs `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options`/`frame-ancestors`, `Referrer-Policy`. **Korlát:** a mérés TLS-bontó proxyn keresztül történt, ezért a TLS-tanúsítvány nem volt vizsgálható; a fejlécek hiányát ajánlott közvetlen kapcsolattal (pl. securityheaders.com) megerősíteni.
- **Javítás:** fejlécek beállítása `.htaccess`-ben. **Ráfordítás:** S

#### TEC-07 – Render-blokkoló scriptek
- **Bizonyíték:** 17 szinkron `<script>` a `<head>`-ben; az `xajax_core.js` kétszer töltődik be; Lighthouse „Eliminate render-blocking resources” ~2,4 s becsült megtakarítás.
- **Javítás:** `defer`, nem használt bővítmények (galleria, qtip, uploadifive, elevatezoom, raty) oldalankénti betöltése. **Ráfordítás:** M

#### TEC-08 – Duplikált URL-ek
- **Bizonyíték:** `/argarancia` (perjel nélkül) → 200, miközben `/koporsos-temetes` → 301; `/index.php/` → 200 a főoldal tartalmával; 106 belső link `?mobile=no` paraméterrel (ezek `noindex`-esek, ami rendben van, de canonical nincs).
- **Javítás:** egységes perjel-szabály 301-gyel, `/index.php*` → `/` 301, canonical (SEO-02). **Ráfordítás:** S

#### SEO-05 – Title-hibák
- **Bizonyíték:** „Árajálatkérés” (/arajanlatkeres/), „Temetkezési szolgáltatá” (/temetkezesi-szolgaltata/), „Gondolja át miért van ez így?” (/figyelem-/), „Köszönjük bizalmát!” (/egyedi-kedvezmeny/); 51 title 65 karakter felett a hosszú, dupla szóközös utótag miatt („ - Szomorúfűz Temetkezés  Budapest”); a /hamvak-temetese/ title-je „Hamvasztásos temetés” (ütközik a /hamvasztasos-temetes/ oldallal); az Elérhetőség title-je „Iroda megközelíthetőség”.
- **Javítás:** egyedi, keresési szándékra írt címek, pl. „Hamvasztás Budapesten – árak és teljes ügyintézés | Szomorúfűz”. **Ráfordítás:** S

#### SEO-06 – Gyenge meta description-ök
- **Bizonyíték:** 71/107 oldal 70 karakter alatt, sokszor csak a cím ismétlése („Teendők haláleset után”, „Szükséges iratok”, „Árajálatkérés”); /egyedi-kedvezmeny/: „**Remarketing**”; /figyelem-/: „Irodáink”; /uzenofal/: nincs.
- **Javítás:** 140–155 karakteres, együttérző, CTA-t tartalmazó leírások. **Ráfordítás:** S

#### SEO-08 – Sitemap és robots.txt
- **Bizonyíték:** `robots.txt` → `Sitemap: http://www.budapest-temetkezes.hu/pages/avszomfuzbud/sitemap.xml` (http, nem szabványos útvonal); `/sitemap.xml` → 404; a sitemapben nincs `lastmod`; tartalmaz üres, remarketing- és RSS-oldalakat (/gyakori-kerdesek/, /egyedi-kedvezmeny/, /rss/, /temetkezesi-szolgaltata/).
- **Javítás:** https sitemap a gyökérben, `lastmod`, csak indexelendő oldalakkal; Search Console-ban beküldeni. **Ráfordítás:** XS–S

#### SEO-09 – Elavult tartalom
- **Bizonyíték:** a Hírek oldal legfrissebb bejegyzése **2014.12.11.**; „2015 márciusában temetik újra III. Richárdot”, „Hajós emlékezés napja 2013”, a /szocialis-temetes/ a 2014-es szabályozást tárgyalja; a hamvasztás oldalon „a 2015 szeptemberében megnyitott, modern krematóriumban” (piros kiemeléssel).
- **Hatás:** elhanyagolt oldal benyomása; jogszabályi tartalomnál félrevezetés kockázata.
- **Javítás:** a jogi tartalmak szakmai felülvizsgálata és dátumozása; a hírek archiválása (`noindex`) vagy aktuális, hasznos útmutatókra cserélése. **Ráfordítás:** M

#### SEO-10 – Hiányzó helyi landoló oldalak (J)
- **Bizonyíték:** 5 budapesti iroda (VI., XII., XIV., XVII., XX. ker.), de nincs irodánkénti oldal; a kerületi információ csak az Elérhetőség oldalon, egy hosszú szövegben.
- **Javítás:** `/irodak/zuglo/` stb. – cím, térkép, nyitvatartás, megközelítés, fotó, helyi temetők, `FuneralHome` séma. **Ráfordítás:** L

#### SEO-11 – Indexelhető remarketing-oldal
- **Érintett URL:** https://www.budapest-temetkezes.hu/egyedi-kedvezmeny/
- **Bizonyíték:** nincs `noindex`, benne van a sitemapben, meta description: „Remarketing”.
- **Javítás:** `noindex`, sitemapből törlés, szöveg átírása (UX-05). **Ráfordítás:** XS

#### UX-04 – Elavult vizuális megjelenés
- **Bizonyíték:** ≈2012-es sablon (`design/13`, fényes gradiens gombok, árnyékolt dobozok), átlagosan 24,6 inline `style` oldalanként, piros és kék (#0000ff) kézi kiemelések, sorkizárt szöveg, mobilon oldalanként eltérő fejlécszín.
- **Javítás:** új, nyugodt arculati rendszer (ld. ui-ux-audit). **Ráfordítás:** L–XL

#### UX-07 – Helyesírási hibák
- **Bizonyíték:** „statiszktikai”, „Árajálatkérés”, „Temetkezési szolgáltatá”, „bürökratikus”, „Pestrezsébet”, „Vörösmarthy”, „legforgalmassabb”, „Munkatársainkaz”, „Fontosnak tarjuk”, „Koporsó választékunk at”, „boncolás mellőzés ét”, „Dél-pesti Centrum Kórház tól”, „hamvasztásal”.
- **Hatás:** minőségérzet és bizalom csökken.
- **Javítás:** teljes korrektúra. **Ráfordítás:** S

#### UX-08 – Tartalmi ellentmondások
- **Bizonyíték:**
  - /szukseges-iratok/: „a születési, házassági … anyakönyvi kivonat beszerzésében – rajtunk kívülálló okokból – sajnos nem [tudunk segíteni]”, ugyanazon az oldalon: „Díjmentesen ránk bízhatja az ügyintézést teljes körűen, hiányos alap iratok esetében is”; a főoldal: „anyakönyv beszerzésével”. Az oldal első bekezdése kétszer szerepel.
  - Főoldal: „Cégünknél nincs egyedi kedvezményrendszer”, miközben létezik „Egyedi kedvezmény” és „Online kedvezmény” oldal.
  - Főoldal: „árajánlat akár 2 órán belül” – az űrlapoknál nincs válaszidő.
- **Javítás:** egységes, jogilag ellenőrzött szolgáltatásleírás. **Ráfordítás:** S

#### UX-10 – Mobil tördelési hibák
- **Bizonyíték:** /hamvasztas-urnakiadas/ mobilon 509 px széles (390 px viewport), /elerhetoseg/ 408 px (`data/browser-audit.json` → `horizontalOverflow`); a slider alatt ~200 px üres sáv (`screenshots/mobile-hamvasztas-fold.png`); a mobil főoldal 6 064 CSS px hosszú.
- **Javítás:** fix szélességű táblázatok/képek (`max-width:100%`), slider eltávolítása. **Ráfordítás:** S

#### A11Y-05 – Landmarkok és címsorstruktúra
- **Bizonyíték:** axe `landmark-one-main` (25/25 oldal), `region` (852 elem), `heading-order` (16 oldal), `empty-heading` (2 oldal), `list` (2 oldal).
- **Javítás:** `<header>`, `<nav>`, `<main>`, `<footer>`; logikus H1–H3. **Ráfordítás:** S

#### A11Y-06 – Automatikus slider
- **Bizonyíték:** `slideshowSpeed: 8000`, `pauseOnHover` csak egérrel; „Previous/Next” linkek szöveg nélkül (axe `link-name`); a klónozott diák fókuszálhatók `aria-hidden` mellett (axe `aria-hidden-focus`).
- **Hatás:** WCAG 2.2.2 (Szüneteltetés), 4.1.2.
- **Javítás:** slider elhagyása (UX-02) vagy szünet gomb + akadálymentes vezérlők. **Ráfordítás:** S

#### A11Y-07 – Kis érintési célpontok
- **Bizonyíték:** rádiógombok 13×13 px, slider-nyilak 15×50 px, szövegközi linkek 17 px magasak (mobil oldalanként 16–30 elem, `data/browser-audit.json` → `smallTargets`).
- **Javítás:** min. 24×24 px (WCAG 2.5.8), ideálisan 44–48 px; a teljes címke legyen kattintható. **Ráfordítás:** S

#### A11Y-09 – Olvashatóság
- **Bizonyíték:** desktopon a törzsszöveg 12 px Trebuchet MS, `line-height: normal`; sorkizárt bekezdések (`text-align: justify`); piros figyelemfelhívó szövegek.
- **Javítás:** 16–18 px törzsszöveg, 1,5–1,6 sormagasság, balra zárt szöveg. **Ráfordítás:** S

#### LEG-02 – Harmadik feles erőforrások a hozzájárulás előtt
- **Érintett URL:** https://www.budapest-temetkezes.hu/ (és minden oldal)
- **Bizonyíték:** `data/consent-check.json` – kattintás nélkül, 6 mp várakozás után: a Google Consent Mode alapállapota helyesen `denied` (`ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`), és a GTM-konténer nem töltődik be (**pozitívum**). Ugyanakkor elindul két `static.xx.fbcdn.net` kérés (Facebook SDK-erőforrás) és a régi `http://www.googleadservices.com/pagead/conversion.js` (ezt csak a mixed-content blokkolás állítja meg, ld. TEC-01).
- **Hatás (F, jogi szakértő ellenőrizze):** a Meta szervereire hozzájárulás nélkül jut el a látogató IP-címe és a hivatkozó oldal; temetkezési kontextusban ez különösen érzékeny.
- **Javítás:** a Facebook SDK és a régi Ads-snippet eltávolítása vagy GTM-be, hozzájáruláshoz kötött címkébe helyezése. **Ráfordítás:** S

#### LEG-03 – Üres ÁSZF
- **Érintett URL:** https://www.budapest-temetkezes.hu/a-sz-f/
- **Bizonyíték:** teljes tartalom: „Á. Sz. F. A tartalom feltöltés alatt.”
- **Hatás (F, jogi szakértő ellenőrizze):** ha a cég online ajánlatot ad / szerződést köt, hiányoznak a fogyasztói tájékoztatás feltételei.
- **Javítás:** ÁSZF feltöltése vagy az oldal eltávolítása. **Ráfordítás:** S (jogi szöveggel M)

#### CNV-04 – Nincs „mi történik ezután”
- **Bizonyíték:** az űrlapok felett „Kérjük, töltse ki … pontos temetési árkalkulációt tudunk küldeni”, de nincs válaszidő, nincs leírás a következő lépésről; a főoldalon „akár 2 órán belül”.
- **Javítás:** az űrlap mellett: „Munkatársunk munkanapokon 2 órán belül felhívja. Sürgős esetben hívja: …”. **Ráfordítás:** XS

### 🟢 Alacsony

#### FUN-09 – Kattinthatatlan „Árjegyzék” csempe
- **URL:** főoldal · **Bizonyíték:** a `contentbox_199` doboznak nincs linkje és gombja (a többi 5 csempének van). · **Javítás:** link az ároldalra. · **Ráfordítás:** XS

#### FUN-13 – Angol `alert()` hiba esetén (F)
- **URL:** minden oldal · **Bizonyíték:** inline script: ha az xajax nem töltődik be 2 mp-en belül, `alert("Error: the xajax Javascript component could not be included…")`. A FUN-07 szerinti időszakos hibák mellett előfordulhat. · **Javítás:** az alert törlése. · **Ráfordítás:** XS

#### TEC-09 – Kétlépcsős átirányítás
- **Bizonyíték:** `http://budapest-temetkezes.hu/` → `https://budapest-temetkezes.hu/` → `https://www.budapest-temetkezes.hu/`. · **Javítás:** egy lépésben a végső URL-re. · **Ráfordítás:** XS

#### TEC-10 – Elavult markup
- **Bizonyíték:** `XHTML 1.0 Transitional` doctype, `xmlns="https://www.w3.org/1999/xhtml"` (hibás névtér-URI, `http://` kellene), táblázatos tartalomelrendezés (72 táblázat), `align` attribútumok, többszörösen escape-elt `<noscript>`. · **Javítás:** HTML5-sablon a redesign során. · **Ráfordítás:** L

#### SEO-12 – Horgonyszövegek és title attribútumok
- **Bizonyíték:** „>>> IDE <<<”, „kattintson IDE”, „A válaszért kattintson ide”; a főoldali csempék `title`-je kulcsszóhalmozás („hajóstemetés, hajós temetés, dunai temetés, dunai hajóstemetés…”). · **Javítás:** leíró linkszövegek. · **Ráfordítás:** S

#### SEO-13 – Képek és megosztási metaadatok
- **Bizonyíték:** 202 kép üres `alt`-tal (tartalmi képek is), a csempeképek CSS-háttérként (nem indexelhetők); Open Graph csak 50 (hír/termék) oldalon, a fő oldalakon nincs `og:image`. · **Javítás:** leíró alt-szövegek, OG-címkék. · **Ráfordítás:** S

#### A11Y-08 – Iframe-ek cím nélkül
- **Bizonyíték:** axe `frame-title` (14 oldal: GTM noscript, Google Térkép, YouTube). · **Javítás:** `title="Térkép – Izabella u. 65."`. · **Ráfordítás:** XS
