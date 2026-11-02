# SEO és helyi keresési audit

**Fókusz:** budapesti temetkezési szolgáltatások (hamvasztás, koporsós temetés, szórás, hajós temetés), 5 budapesti iroda.
A hibakódok a [hibajegyzékre](issue-register.md) hivatkoznak.

> **Korlát:** kulcsszó-forgalmi és rangsor-adatok (Search Console, Ahrefs/Semrush), valamint a Google Cégprofil adatai nem voltak hozzáférhetők. Az értékelés az oldal publikus tartalmán és technikai jelein alapul; a keresési relevanciára vonatkozó állítások ezért szakmai becslések (**F/J**), nem mért helyezések.

## 1. Összkép

| Terület | Értékelés | Fő megállapítás |
|---|---|---|
| Indexelhetőség | 🟡 | indexelhető, de duplikátumok, csapda-URL-ek, hiányzó canonical |
| Tartalmi relevancia | 🟡 | jó témalefedettség (hamvasztás, szórás, iratok), de árak és GYIK hiányoznak, sok elavult/vékony oldal |
| On-page | 🟠 | nincs H1, gyenge title/description, elírások |
| Helyi SEO | 🟠 | 5 iroda, de nincs irodánkénti oldal, nincs séma, NAP-ellentmondások |
| Strukturált adat | 🔴 | egyáltalán nincs |
| Belső linkelés | 🟡 | erős oldalsáv-menü, de 404-ek és „IDE” horgonyok |
| Lighthouse SEO | 92/100 minden mért oldalon | a hiányzók: crawlolható linkek (`javascript:void(0)`), nagyítás |

## 2. Indexelhetőség

- **Pozitív:** a robots.txt nem tilt fontos tartalmat; a sitemap 95 URL-je mind 200-as; a mobil User-Agent (Googlebot Smartphone) indexelhető HTML-t kap; a `?mobile=` változatok `noindex`-esek.
- **Problémák:**
  - FUN-04 – végtelen `/elerhetoseg/+36305767206/…` URL-lánc 200-as válasszal.
  - SEO-02 – a fő oldalakon nincs canonical; a hírek canonicalja `http://`.
  - TEC-08 – `/argarancia` és `/index.php/` 200-as duplikátumok.
  - SEO-07 – üres oldalak (GYIK, ÁSZF, Üzenőfal) a sitemapben.
  - SEO-11 – a remarketing-oldal (`/egyedi-kedvezmeny/`) indexelhető.
  - SEO-08 – a sitemap nem szabványos helyen, `http://` hivatkozással, `lastmod` nélkül.

## 3. Szolgáltatásoldalak elemzése

| Oldal | Szó | Title | H1 | Ár | Űrlap | Fő hiány |
|---|---|---|---|---|---|---|
| `/hamvasztas-urnakiadas/` | 528 | Hamvasztás és a hamvak kiadása | ❌ | ❌ | 30 mezős | ár, „Budapest” a title-ben, elavult „2015” kiemelés |
| `/hamvasztasos-temetes/` | 306 | Hamvasztásos temetés | ❌ | ❌ | 30 mezős | átfedés az előzővel (kannibalizáció), ár |
| `/hamvak-temetese/` | 396 | **Hamvasztásos temetés** (!) | ❌ | ❌ | 30 mezős | title ütközik a fentivel |
| `/koporsos-temetes/` | 647 | Koporsós temetés | ❌ | ✅ 232.288 Ft-tól | 24 mezős | „Budapest” a title-ben, árbontás |
| `/hamvak-szorasa-temeto/` | 478 | Hamvak szórása temetőben | ❌ | ❌ | 25 mezős | ár, Új köztemető említése a title-ben |
| `/hamvak-szorasa-dunaba/` | 414 | Hamvak Dunába szórása hajóról | ❌ | ❌ | 25 mezős | „hajós temetés” kulcsszó a title-ben, ár, menetrend |
| `/ravatalozo-terem/` | 624 | Ravatalozó terem | ❌ | ❌ | 27 mezős | cím (IX. ker., Ernő u.) a title-ben |
| `/polgari-bucsuztatas/` | 234 | Búcsúztatás | ❌ | ❌ | – | vékony |
| `/teendok-halaleset-utan/` | 693 | Teendők haláleset után | ❌ | – | – | lépésenkénti struktúra, éjszakai teendők |
| `/szukseges-iratok/` | 649 | Szükséges iratok | ❌ | – | – | ismétlődő bekezdés, ellentmondás (UX-08), letölthető ellenőrzőlista |
| `/gyakori-kerdesek/` | 10 | Gyakori kérdések | ❌ | – | – | **üres** |

**Kannibalizáció:** három oldal verseng a „hamvasztás” / „hamvasztásos temetés” témáért (`/hamvasztasos-temetes/`, `/hamvasztas-urnakiadas/`, `/hamvak-temetese/` – utóbbi title-je szó szerint „Hamvasztásos temetés”). Javaslat: egy erős pillér-oldal („Hamvasztás Budapesten”) + alárendelt aloldalak (urna hazavitele, urnasírba temetés, szórás) egyértelmű, eltérő szándékkal.

## 4. Címsorstruktúra

- Az aloldalakon **nincs H1** (SEO-01); a fő cím H2.
- A főoldal H1-e a logó szövege („Szomorúfűz Temetkezés Budapest”), a H2 „Hamvasztásos temetkezési szolgáltatás” – a főoldal fő témája így nem „temetkezés Budapest”.
- A sliderben minden diának H3+H4 címe van, az oldalsáv „Megosztás” és „Elérhetőségeink” H3 – a címsorok egy része dekoráció.
- **Javaslat (minta, Hamvasztás oldal):**
  ```
  H1  Hamvasztás Budapesten – teljes körű ügyintézéssel
   H2  Mit tartalmaz a hamvasztási szolgáltatás?
   H2  Mennyibe kerül a hamvasztás? (ártáblázat)
   H2  A hamvasztás menete lépésről lépésre
   H2  Hová kerülhetnek a hamvak? (otthon, urnasír, szórás, Duna)
   H2  Szükséges iratok
   H2  Gyakori kérdések
   H2  Irodáink és elérhetőség (0–24)
  ```

## 5. Title és meta description

Részletek: SEO-05, SEO-06. Javasolt minták:

| Oldal | Javasolt title (≤ 60 kar.) | Javasolt description (≤ 155 kar.) |
|---|---|---|
| Főoldal | Temetkezés Budapesten – 0–24 ügyelet \| Szomorúfűz | Hamvasztás és koporsós temetés teljes ügyintézéssel, 5 budapesti irodában. Átlátható árak, árgarancia. Hívjon bizalommal, segítünk. |
| Hamvasztás | Hamvasztás Budapest – árak, ügyintézés \| Szomorúfűz | Hamvasztás teljes körű ügyintézéssel, urna hazavitele vagy temetése. Kiindulási ár és tételes tartalom, rejtett költség nélkül. |
| Koporsós temetés | Koporsós temetés Budapesten 232 288 Ft-tól \| Szomorúfűz | Koporsós temetés budapesti temetőkben, teljes ügyintézéssel. Mit tartalmaz az ár, hogyan zajlik a szervezés – kérjen ajánlatot. |
| Hajós temetés | Hajós temetés a Dunán – hamvak szórása \| Szomorúfűz | Méltó búcsú a Dunán: hamvak szórása hajóról, vízben lebomló urnával. Időpontok, menet, árak és ügyintézés egy helyen. |
| Teendők | Teendők haláleset után – lépésről lépésre \| Szomorúfűz | Mit kell tenni haláleset után kórházban vagy otthon? Egyszerű útmutató, iratlista és 0–24 elérhetőség. Végigvezetjük. |
| Elérhetőség | Irodáink Budapesten – címek, nyitvatartás \| Szomorúfűz | 5 budapesti iroda: VI. Izabella u., XII. Nagyenyed u., XIV. Thököly út, XVII. Pesti út, XX. Szivacs u. Telefon, térkép, nyitvatartás. |

## 6. Helyi SEO

### 6.1 Telephelyadatok – NAP-konzisztencia (SEO-04)

| Iroda | Oldalsáv | /elerhetoseg/ | Egyéb |
|---|---|---|---|
| VI., Izabella u. 65. | +36 1 919 0170 / +36 30 847-1915 | 06 1 919 0170 / 06 30 847-1915 | főoldal: **+36 1 720 2710**, térképlink: **Izabella u. 68** |
| XII., Nagyenyed u. 1. | +36 1 919-0886 / +36 30 203-2300 | egyezik | |
| XIV., Thököly út 167. | **1147** · +36 1 919-0172 / +36 30 965-1783 | **1146** | |
| XVII., Pesti út 41/A. | +36 1 919 0171 / +36 30 313-7920 | egyezik | |
| XX., Szivacs u. 5. | +36 1 919-0173 / +36 30 576-7206 | egyezik (+ hibás üres link, FUN-04) | |
| Központ | „Információ: +36 30 847-1915” → valójában 313-7920-at hív (FUN-01) | | /ceginformaciok/: telefon 1/720-2710; telephely csak Debrecen, Nyíregyháza |

### 6.2 Javasolt helyi struktúra (SEO-10)
- `/irodak/` gyűjtőoldal térképpel + 5 irodaoldal (`/irodak/belvaros-izabella-utca/`, `/irodak/buda-nagyenyed-utca/`, `/irodak/zuglo-thokoly-ut/`, `/irodak/rakoskeresztur-pesti-ut/`, `/irodak/pesterzsebet-szivacs-utca/`).
- Irodaoldal tartalma: pontos cím, beágyazott térkép, megközelítés (a meglévő jó szöveg!), nyitvatartás, közvetlen szám, fotó a bejáratról, közeli kórházak/temetők (pl. Uzsoki utcai kórház, Új köztemető, Rákoskeresztúri temető), `FuneralHome` séma.
- Google Cégprofil irodánként, azonos NAP-pal; értékelések gyűjtése a temetés után (tapintatos, késleltetett kéréssel).
- Témaoldalak a budapesti temetőkről (Fiumei úti temető oldal már van – 145 szó, bővítendő; Új köztemető, Óbudai temető, Farkasréti temető): gyakorlati tudnivalók, sírhelyárak forrásmegjelöléssel.

### 6.3 Strukturált adat – minta (SEO-03)

```json
{
  "@context": "https://schema.org",
  "@type": "FuneralHome",
  "@id": "https://www.budapest-temetkezes.hu/#izabella",
  "name": "Szomorúfűz Temetkezés – Belvárosi iroda",
  "parentOrganization": {
    "@type": "Organization",
    "@id": "https://www.budapest-temetkezes.hu/#org",
    "name": "Szomorúfűz Temetkezési Hálózat Kft.",
    "taxID": "26704450-2-42",
    "url": "https://www.budapest-temetkezes.hu/"
  },
  "url": "https://www.budapest-temetkezes.hu/irodak/belvaros-izabella-utca/",
  "telephone": "+36-1-919-0170",
  "email": "budapest@temetkezes.hu",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Izabella utca 65.",
    "postalCode": "1064",
    "addressLocality": "Budapest",
    "addressCountry": "HU"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 47.508766, "longitude": 19.066038 },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00", "closes": "16:00"
  }],
  "areaServed": { "@type": "City", "name": "Budapest" }
}
```
A koordináták a weboldal saját Google Térkép-linkjéből származnak; élesítés előtt a Cégprofillal egyeztetendő. Ha van 0–24 halottszállítási ügyelet, azt külön `ContactPoint`-ként (`contactType: "emergency"`) célszerű jelölni.

## 7. Belső linkelés

- **Erősség:** a bal oldali menü minden oldalról eléri a fő szolgáltatásokat; a főoldali szöveg kulcsszavas belső linkeket tartalmaz.
- **Gyengeségek:**
  - 404-re mutató linkek: „Árlista” (főoldal), `/koporsok/` (16 hír), `/hamvak-szorasa-templom/` (FUN-03, FUN-05).
  - Nem leíró horgonyszövegek: „IDE”, „kattintson ide” (SEO-12).
  - A GYIK, Árgarancia, Teendők nincs kiemelve a szolgáltatásoldalakon; a szolgáltatásoldalak nem linkelnek egymásra kontextusban (pl. hamvasztás → szórás → hajós temetés).
  - 106 belső link `?mobile=no` paraméterrel.
  - A mobilmenü `javascript:void(0)` linkje a Lighthouse szerint nem crawlolható (a menü tartalma ettől még a HTML-ben van).

## 8. Tartalmi lehetőségek (J)

| Téma | Keresési szándék | Javasolt oldal |
|---|---|---|
| hamvasztás ára Budapest | tranzakciós | `/arak/` + Hamvasztás pillér |
| temetés költségei, temetési segély | információs | „Mennyibe kerül egy temetés?” útmutató (önkormányzati temetési támogatás, kegyeleti járadék) |
| mi a teendő ha otthon hal meg valaki | sürgős információs | Teendők oldal átírása lépésenként, éjszakai útmutatóval |
| halotti anyakönyvi kivonat ügyintézés | információs | Szükséges iratok – letölthető ellenőrzőlista |
| urna otthon tartása szabályai | információs | Hamvak hazavitele – jogszabályi összefoglaló, dátummal |
| hajós temetés Duna | tranzakciós | Hajós temetés oldal: időpontok, árak, fotók |
| polgári búcsúztatás szövegminta | információs | Búcsúztatás oldal bővítése |
| GYIK | vegyes | 15–20 kérdés, `FAQPage` séma |

A 2013–2014-es hírek (celebritások, külföldi érdekességek) helyett ezek az örökzöld útmutatók hoznak releváns forgalmat és bizalmat (SEO-09).

## 9. Képek és megosztás
- 202 kép üres `alt`-tal; a főoldali csempeképek CSS-háttérként (nem indexelhetők).
- Képfájlnevek számok (`1353162436_200x.jpg`).
- A fő oldalakon nincs Open Graph (`og:title`, `og:image`) → megosztáskor (pl. gyászjelentés megosztása Facebookon) rossz előnézet.
- Lásd SEO-13.
