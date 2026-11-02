# SEO-migrációs terv

**Alap:** az auditban feltérképezett 113 URL (107 élő, 6 hibás) – `data/crawl.json`, `reports/site-map.md`.
**URL-szintű javaslat:** [`strategy/redirect-map.csv`](redirect-map.csv) – 121 sor: 91 megtartott URL, 22 db 301, 8 új oldal.
**Generálás:** `python3 scripts/build_redirect_map.py`

> ❔ **Ismeretlen:** külső hivatkozások (backlinkek) és oldalankénti organikus forgalom. Search Console- és backlink-adat (pl. Ahrefs) nélkül a „mely oldalak értékesek” kérdést óvatosan, URL-megőrzéssel kell kezelni. Ez a terv ezért **alapértelmezésben minden URL-t megtart**, és csak a bizonyítottan hibás vagy duplikált URL-eket irányítja át.

## 1. URL-megőrzési stratégia

**Alapelv: az URL a SEO-tőke hordozója – ne változzon, ha nem muszáj.**

| Szabály | Alkalmazás |
|---|---|
| 1. Minden indexelendő, 200-as URL **változatlan útvonalon** él tovább (perjellel a végén) | 91 URL – a szolgáltatás-, információs, jogi és hír-URL-ek, a terméklapok |
| 2. A hibás és duplikált URL-ek 301-et kapnak a legrelevánsabb élő oldalra | 22 URL (ld. 3. pont) |
| 3. Új oldalak csak új URL-en jönnek létre, régit nem írnak felül | `/arak/`, `/irodak/` + 5 irodaoldal, `/rolunk/` |
| 4. Tartalmi összevonás csak adat alapján | Pl. `/hamvasztas-urnakiadas/` ↔ `/hamvasztasos-temetes/` – csak ha a Search Console szerint a két oldal ugyanarra a lekérdezésre versenyez |
| 5. Hírek: URL marad, `noindex` csak backlink-ellenőrzés után | 36 archív hír (2013–2014) |
| 6. Paraméteres változatok: `?mobile=*` → 301 a paraméter nélküli URL-re (szabályként, nem egyenként) | 106 belső link érintett |

**Forgatókönyvenként:**
- **A:** az URL-ek nem változnak; csak a hibás URL-ek javítása (ha a platform enged egyedi 301-et ❔).
- **B:** ❔ – a szolgáltatótól írásban meg kell kérdezni, hogy az új generáción **megmaradnak-e a slugok** (`/koporsos-temetes/` stb.) és a hír-/jogszabály-URL-ek numerikus azonosítói (`/hirek-aktualitasok/…/32213/`). Ha nem, a teljes 301-térkép kell.
- **C:** a fenti szabályok teljes egészében. WordPressben a hír- és jogszabály-URL-ek (`/…/slug/12345/`) egyedi permalink-szabállyal vagy átirányítással kezelhetők.

## 2. Tartalommigrációs terv

| Tartalomtípus | Darab | Teendő | Felelős |
|---|---|---|---|
| Szolgáltatásoldalak | 17 | Új szöveg (K-csomag), H1, ár, FAQ-blokk, belső linkek; URL marad | szövegíró + SEO |
| Ajánlatkérés, kapcsolat, kedvezmények | 13 | Egy ajánlatkérő oldal (a duplikátum 301), új rövid űrlap; a remarketing-oldal `noindex` | UX + fejlesztő |
| Információ, ügyintézés | 6 + 7 jogszabály | Teendők és Iratok átstrukturálva (lépések, ellenőrzőlista), jogszabályok dátumozva | szövegíró + jogi átnézés |
| Galériák, terméklapok | 10 | Képek átvétele optimalizálva (WebP, alt-szöveg); a terméklapok URL-je marad | fejlesztő |
| Hírek | 36 + gyűjtő | Változatlan átvétel, „archív” jelölés, belső linkek javítása (`/koporsok/` → `/koporsos-temetes/`) | fejlesztő |
| Jogi oldalak | 4 | ÁSZF feltöltése, adatkezelés frissítése | jogász |
| Képek | ~400–500 (becslés ❔) | Automatizált letöltés a crawl alapján, tömörítés, értelmes fájlnév | fejlesztő |

**Technikai kinyerés:** a platform nem garantál exportot (❔), ezért a migráció a meglévő crawler kiterjesztésével (szöveg + képek + metaadatok) **saját erőből** elvégezhető; a becslés ezt tartalmazza (C: 24–70 óra).

## 3. 301-es átirányítási követelmények

### Kötelező átirányítások (a `redirect-map.csv`-ből)

| Régi URL | Cél | Ok |
|---|---|---|
| `/arlista/` | `/arak/` | 404, a főoldalról linkelve |
| `/koporsok/` | `/koporsos-temetes/` | 404, 16 belső link |
| `/hamvak-szorasa-templom/` | `/hamvak-temetese/` | 404 |
| `/kegyeleti-webaruhaz/urna-13172/13172/` | `/urnak/` | 404 |
| `/temetkezesi-hirek/a-szocialis-temetesi-torveny-szovege/23495/` | `/hirek-aktualitasok/a-szocialis-temetesi-torveny-szovege/23495/` | 404 |
| `/arajanlatkeres/` | `/arajanlat-keres-itt/` | duplikált űrlapoldal |
| `/argarancia` | `/argarancia/` | perjel-duplikátum |
| `/index.php/` | `/` | duplikált főoldal |
| `/?mobile=no`, `/?mobile=1` (és minden `?mobile=*`) | paraméter nélkül | duplikátum |
| `/elerhetoseg/+36305767206/…` (8 szint) | `/elerhetoseg/` | URL-csapda |
| `/temetkezesi-szolgaltata/` | `/` | csonka slug, vékony tartalom |
| `/uzenofal/` | `/visszajelzes-kuldese/` | üres vendégkönyv |
| `/rss/`, régi RSS-XML | `/feed/` | új hírfolyam (ha nincs: 410) |

### Technikai követelmények
1. **Egylépéses 301** – lánc nélkül (ma: http → https → www két lépés; TEC-09). Szabály: `http://`, nem-www, perjel nélküli és `index.php` változatok egyetlen 301-gyel a végleges `https://www.…/útvonal/` címre.
2. **Szerveroldali 301** (nem JavaScript, nem meta refresh).
3. **Ismeretlen útvonalra valódi 404** (ma a csapda-URL-ek 200-at adnak – FUN-04); megszüntetett tartalomra 410.
4. Az átirányítások **legalább 12 hónapig** éljenek, a hír- és termék-URL-eké tartósan.
5. A belső linkek az élesítéskor **közvetlenül a végleges URL-re** mutassanak, ne átirányításon keresztül.
6. Élesítés előtt automatizált teszt: a CSV minden sorára várt státusz + cél (ld. 6. pont).

## 4. Canonical-stratégia

| Szabály | Részletek |
|---|---|
| Minden indexelendő oldalon **önhivatkozó, abszolút** canonical | `https://www.budapest-temetkezes.hu/<útvonal>/` – mindig `https`, `www`, perjellel |
| Paraméteres URL-ek (`?mobile=`, UTM, `?page=`) | a paraméter nélküli URL a canonical; a lapozott hírlista oldalai önhivatkozók |
| `noindex`-es oldalak (remarketing, köszönőoldal) | nincs canonical más oldalra; `noindex, follow` |
| Egy mobil- és desktop-HTML | reszponzív sablon esetén nincs külön mobil-URL, így `alternate` / `Vary` sem kell |
| Ellenőrzés | a canonical URL 200-at adjon, ne átirányítást (ma a hírek canonicalja `http://` → 301) |

## 5. Strukturált adat terv

| Oldaltípus | Séma | Kötelező mezők | Prioritás |
|---|---|---|---|
| Főoldal | `Organization` (+ `logo`, `sameAs`, `taxID`) + `WebSite` | name, url, logo, contactPoint (0–24, ha van) | 1 |
| 5 irodaoldal | `FuneralHome` (LocalBusiness altípus) | name, address, geo, telephone, openingHoursSpecification, parentOrganization | 1 |
| Szolgáltatásoldalak | `Service` + `Offer` / `AggregateOffer` (ár „-tól”, HUF) | name, provider, areaServed: Budapest, offers.price / priceCurrency | 2 |
| Ároldal | `OfferCatalog` | itemListElement | 2 |
| GYIK | `FAQPage` | mainEntity (Question / acceptedAnswer) | 2 |
| Minden aloldal | `BreadcrumbList` | itemListElement | 3 |
| Hírek | `Article` | headline, datePublished, author | 3 |
| Ravatalozó | `Place` / `FuneralHome` alrészleg | address, maximumAttendeeCapacity (40+40–50) | 3 |

Minta-JSON-LD: `reports/seo-audit.md` 6.3. pont. **Validálás:** Schema Markup Validator + Search Console „Továbbfejlesztések” jelentés.

**NAP-előfeltétel (SEO-04):** a séma csak egységesített adatokkal kerüljön élesbe – telefonszám (720-2710 vs. 919-0170), Thököly út irányítószáma (1146 vs. 1147), Izabella u. 65. A Google Cégprofilokat ugyanezekre kell frissíteni.

## 6. Indexelési ellenőrzőlista

**Élesítés előtt**
- [ ] Search Console tulajdonjog (domain-szintű DNS-ellenőrzés) – **most**, a régi oldalon, hogy legyen kiinduló adat (legalább 4–8 hét)
- [ ] Kiinduló mentés: Search Console top 1 000 lekérdezés és oldal, a teljes crawl (`data/crawl.json`), Lighthouse
- [ ] Staging `noindex` + HTTP-alapú jelszavas védelem (ne kerüljön indexbe)
- [ ] `robots.txt`: élesben nem tilt semmi fontosat; `Sitemap: https://www.budapest-temetkezes.hu/sitemap.xml`
- [ ] XML-sitemap: csak 200-as, indexelendő, canonical URL-ek, `lastmod`-dal
- [ ] Minden oldalon egy H1, egyedi title (≤ 60 karakter) és description (≤ 155 karakter)
- [ ] Hreflang nem szükséges (egynyelvű)

**Élesítés napján**
- [ ] A DNS TTL-jét 48 órával korábban 300 s-ra csökkenteni
- [ ] 301-szabályok élesítése a DNS-váltással egy időben
- [ ] A staging `noindex` eltávolítása az éles oldalról (!)
- [ ] Sitemap beküldése a Search Console-ban; a 10 legfontosabb URL indexelési kérése
- [ ] GA4/GTM-mérés és consent ellenőrzése élesben

**Élesítés után**
- [ ] 1., 3., 7., 14., 30. nap: Search Console – lefedettség, 404-ek, „Feltérképezve – jelenleg nincs indexelve”
- [ ] Hetente: a top 50 lekérdezés pozíciója a kiinduló értékhez képest
- [ ] A régi sitemap URL-jeinek ellenőrzése: mind 200 vagy 301 – soha nem 404
- [ ] A Google Cégprofilok weboldal-linkjei a megfelelő irodaoldalra mutatnak

## 7. Tesztelési terv

| Fázis | Teszt | Eszköz | Elfogadási kritérium |
|---|---|---|---|
| Staging | Átirányítás-teszt a teljes `redirect-map.csv`-re | szkript (curl/Python) | 100% egyezés: státusz + cél, nincs lánc |
| Staging | Crawl-összevetés régi ↔ új | `scripts/crawl.py` stagingre | minden „megtart” URL 200, title/H1/canonical kitöltve |
| Staging | Strukturált adat | Schema Markup Validator | 0 hiba a prioritás-1 sémákon |
| Staging | Akadálymentesség | axe-core (`scripts/browser-audit.js`) | 0 critical/serious |
| Staging | Teljesítmény | Lighthouse mobil | LCP ≤ 2,5 s, CLS ≤ 0,1, Performance ≥ 85 |
| Staging | Funkcionális | Playwright | minden `tel:` a látható számot hívja; űrlapok mobilon; sticky CTA |
| Élesítés | Smoke-teszt | curl + böngésző | top 20 URL 200, 10 régi URL helyes 301 |
| +1 hét | Index és hibák | Search Console | 404 < 1% a régi URL-ekre |
| +4 hét | Forgalom | Search Console | organikus kattintás ≥ 85% a kiinduló értékhez képest |
| +8–12 hét | Forgalom | Search Console | organikus kattintás ≥ 100% a kiinduló értékhez képest |

**Visszaállítási terv (C):** a régi platform-előfizetés az élesítés után **legalább 30 napig maradjon aktív** (a DNS visszaállítható); a domain-átvitel csak sikeres stabilizáció után záruljon le.

## 8. SEO-kockázat forgatókönyvenként

| Kockázati tényező | A | B | C |
|---|---|---|---|
| URL-változás | nincs | ❔ (a szolgáltatótól függ) | kontrollált (megőrzés + 301) |
| Sablonszintű SEO-hibák (H1, canonical) | maradnak, ha a szolgáltató nem javít | részben javulnak ❔ | megszűnnek |
| Átmeneti forgalomesés az élesítés után | nincs | 0–15% ❔ | 0–15%, 4–12 hét alatt helyreáll (jó végrehajtással) |
| Mobil/desktop kettős HTML | marad | valószínűleg megszűnik 🔶 | megszűnik |
| Tartalmi minőség (vékony / üres oldalak) | javul (K) | javul (K) | javul (K) |
| Strukturált adat | feltételes (egyedi kód ❔) | feltételes | teljes |
| Kontroll a technikai SEO felett | alacsony | alacsony–közepes | teljes |
| **Összesített SEO-kockázat** | **Alacsony** (de korlátozott potenciál) | **Közepes** (sok ismeretlen) | **Közepes, jól kezelhető** (a legnagyobb potenciál) |
| **SEO-potenciál 12 hónap után** | korlátozott | közepes | magas |
