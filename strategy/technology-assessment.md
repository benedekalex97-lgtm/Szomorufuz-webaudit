# Technológiai értékelés – jelenlegi rendszer

**Cél:** döntés-előkészítés. A megállapítások a meglévő auditra (`reports/`, `data/`) és egy 2026. 11. 02-i célzott kiegészítő vizsgálatra (DNS, IP-tulajdonos, platform-ujjlenyomat, a platformszolgáltató nyilvános ÁSZF-je) épülnek.

**Bizonyossági jelölések**

| Jelölés | Jelentés |
|---|---|
| ✅ **Bizonyított** | Publikus adattal közvetlenül igazolt (forráskód, HTTP-válasz, DNS, nyilvános dokumentum) |
| 🔶 **Valószínű** | Több egymástól független jel támasztja alá, de publikusan nem igazolható teljesen |
| ❔ **Ismeretlen** | Publikus hozzáféréssel nem dönthető el; a döntéshez be kell szerezni |

## 1. Vezetői összefoglaló

A budapest-temetkezes.hu **nem egyedi fejlesztés és nem nyílt forrású CMS**. Szinte biztosan a miskolci **Oleander Informatikai Kft.** zárt, hosztolt (SaaS) honlapkészítő platformján fut, annak **régebbi generációján**. A szolgáltató ma `honlap.hu` néven forgalmazza a platformot. Ebből három döntést befolyásoló következmény adódik:

1. **A javítások kb. kétharmada adminból vagy egyedi CSS-sel elvégezhető** (tartalom, linkek, űrlapok, menü, címek). **A sablon- és szerverszintű hibák** (viewport, H1, cache-fejléc, jQuery-verziók, biztonsági fejlécek, süti-sáv, űrlapmezők típusa) **csak a platformszolgáltatón keresztül** javíthatók – ha egyáltalán vállalja.
2. **Erős a szolgáltatói függés.** A nyilvános ÁSZF szerint az arculati elemek a szolgáltató tulajdonában maradnak, és „kizárólag a honlap.hu rendszerében” használhatók. Tartalomexportról nem rendelkezik.
3. A technikai adósság **nem a kód minőségéből, hanem a platformgeneráció elavultságából** fakad. Ezt az ügyfél a jelenlegi konstrukción belül nem tudja törleszteni.

## 2. Azonosított technológiai stack

| Réteg | Megállapítás | Bizonyosság | Bizonyíték |
|---|---|---|---|
| Platform | Oleander Informatikai Kft. hosztolt honlapkészítője (`honlap.hu` / „aweblap” platformcsalád) | 🔶 Valószínű (nagyon erős) | (1) /ceginformaciok/: „Tárhelyszolgáltató: Oleander Informatikai Kft. 3534 Miskolc, Gőz u. 7.” – ugyanez a honlap.hu üzemeltetője; (2) az SPF-rekord `v=spf1 redirect=spf.aweblap.hu`; (3) a www.budapest-temetkezes.hu és az aweblap.hu **ugyanarra az IP-re** (92.119.122.126) mutat, amelynek PTR-neve `mail2.honlap.hu`; (4) azonos útvonalminták: `pages/<oldalazonosító>/contents/…`, `common/google.js`, `design/…` a honlap.hu saját oldalán is |
| Platformgeneráció | Régi generáció: `design/13` sablon, **xajax 0.5 rc1**, jQuery 1.12.4, jQuery UI 1.8.24, XHTML 1.0 Transitional | ✅ Bizonyított | forráskód; a honlap.hu saját oldala már jQuery 3.4.1-et és `hajax` AJAX-réteget használ → létezik újabb generáció |
| Oldalazonosító | `avszomfuzbud` (`pages/avszomfuzbud/…`) | ✅ | forráskód |
| Szerver | Apache, PHP (PHPSESSID) | ✅ | HTTP-fejlécek |
| Adatközpont / IP | Rackforest Zrt. (AS62214), Budapest – osztott IP más platformoldalakkal | ✅ | ipinfo, DNS |
| DNS | `ns1/ns2.m.glbns.com` | ✅ | DNS |
| E-mail a domainen | MX: `mail.budapest-temetkezes.hu` → ugyanaz a platform-IP; a weboldalon használt cím viszont `budapest@temetkezes.hu` (másik domain, saját MX) | ✅ / ❔ (hogy a domain e-mail fiókjai használatban vannak-e) | DNS |
| Domain regisztráció | A platform ÁSZF-je szerint a .hu domain bejegyzése és fenntartása a csomag része | ❔ **Ismeretlen**, ki a domain **jogosultja** (ügyfél vagy szolgáltató) | ÁSZF 1.1.5.; .hu whois nem kérdezhető le automatizáltan |
| Mobilkezelés | User-Agent alapú külön mobil sablon (`?mobile=1` / `?mobile=no`), `Vary: User-Agent` nélkül | ✅ | audit TEC-04 |
| Analitika | GTM-NBJCMVB, Consent Mode v2 alapból `denied`; régi Google Ads konverziós kód (`http://`, blokkolva) | ✅ | `data/consent-check.json` |
| Egyedi CSS | Létezik oldal-specifikus stíluslap: `pages/avszomfuzbud/desing/style/addcss.css` | ✅ | forráskód → egyedi CSS-sel sok vizuális hiba javítható |
| Egyedi JS / `<head>`-kód beillesztése | A GTM-kód és a régi Ads-snippet jelenléte erre utal | 🔶 Valószínű | forráskód; a pontos jogosultság ❔ |
| Átirányítások kezelése adminból | Egyes URL-ek perjel nélkül 301-gyel, mások 200-zal válaszolnak → nincs egységes szabály | ✅ (viselkedés) / ❔ (van-e admin-felület egyedi 301-re) | audit TEC-08 |
| Rendelkezésre állás | ÁSZF: 99%, havonta legfeljebb 360 perc karbantartás; támogatás az előfizetés alatt összesen 24 óra | ✅ (a nyilvános ÁSZF-re) / ❔ (az ügyfél egyedi szerződése) | honlap.hu ÁSZF (2020. 02. 10-től) |
| Előfizetési díj | nem nyilvános (a honlap.hu árak oldala nem közöl árat) | ❔ **Ismeretlen** | honlap.hu/arak |
| Webáruház-modul | Maradványok (`#webshop`, `xajax_refresh_basket_header`, `/kegyeleti-webaruhaz/` 404) | ✅ | forráskód |

> **Miért nem 100%-os a platformazonosítás?** Mert az ügyfél szerződését és admin-felületét nem láttuk. Elméletileg az is lehetséges, hogy az Oleander egyedi konstrukcióban üzemelteti az oldalt, de a négy független egyezés alapján ez nem valószínű.

## 3. Korszerűsíthetőség

| Kérdés | Értékelés | Bizonyosság |
|---|---|---|
| Frissíthető-e a jelenlegi oldal a saját generációján belül (jQuery, sablon)? | Az ügyfél által **nem**; csak a szolgáltató tudná, platformszinten | 🔶 |
| Átvihető-e a platform újabb generációjára (honlap.hu jelenlegi motor)? | Technikailag van újabb generáció; hogy van-e **migrációs út**, és mennyibe kerül | ❔ – rá kell kérdezni |
| Átvihető-e a tartalom másik rendszerbe? | **Igen, de saját erőből**: az audit crawlere már letöltötte mind a 107 oldalt; a szöveg, a képek és az URL-ek kinyerhetők. Szerződéses export-garancia nincs | ✅ (technikai) / ❔ (szerződéses) |
| Átvihető-e a design? | **Nem.** Az ÁSZF 8.2 szerint az arculati elemek a szolgáltató tulajdonában vannak, a rendszeren kívül nem használhatók | ✅ (nyilvános ÁSZF) |
| Headless / API-alapú továbbépítés | Nincs ismert publikus API → **nem reális** | 🔶 |

**Összegzés:** a rendszer *tartalmilag* korszerűsíthető (szöveg, szerkezet, űrlapok), *technológiailag* csak a szolgáltató ütemezése szerint, vagy platformváltással.

## 4. Felhalmozott technikai adósság

| Terület | Adósság | Ki tudja törleszteni? |
|---|---|---|
| Front-end könyvtárak | jQuery 1.12.4 (2016), jQuery UI 1.8.24 (2012), xajax 0.5 rc1, 17 render-blokkoló script | Szolgáltató |
| Markup | XHTML 1.0 Transitional, táblázatos tartalom, ~25 inline stílus oldalanként, többszörösen escape-elt kódrészletek | Részben ügyfél (tartalom), részben szolgáltató (sablon) |
| Mobil-architektúra | Két külön sablon UA-alapon, a mobilon tiltott nagyítás, `Vary` nélkül | Szolgáltató |
| HTTP | 1 éves HTML-cache, hiányzó biztonsági fejlécek, időszakos 502-k | Szolgáltató |
| SEO-alapok | nincs H1 a sablonban, nincs canonical a fő oldalakon, nem szabványos sitemap-útvonal | Szolgáltató (sablon) + ügyfél (tartalom) |
| Tartalom | 2014-es hírek, üres oldalak, ellentmondások, elírások, hibás `tel:` linkek | **Ügyfél** |
| Mérés | régi Ads-snippet, megszűnt Facebook chat, nincs hívásmérés | Ügyfél (ha egyedi kód beilleszthető) |
| Adatvédelem | előre bepipált süti-sáv | Szolgáltató (platformfunkció) |

## 5. A 62 auditált hiba javíthatósága a jelenlegi rendszerben

Forrás: `scripts/strategy_model.py` → `FIX_A` besorolás (saját szakmai becslés, 🔶).

| Kategória | Darab | Arány | Példák |
|---|---|---|---|
| **Adminból / tartalomszerkesztéssel javítható** | 29 | 47% | FUN-01, FUN-02 (telefonlinkek), CNV-01 (ároldal), FUN-03/04/05, SEO-04 (NAP), SEO-05/06, UX-05/07/08, LEG-03 |
| **Részben javítható** (egyedi CSS/kód, ha a platform engedi) | 13 | 21% | UX-01 (sticky hívássáv), A11Y-02 (kontraszt), A11Y-04 (fókusz), SEO-03 (séma), TEC-06 (képek igen, scriptek nem), UX-10 |
| **Csak a platformszolgáltató javíthatja** | 20 | 32% | A11Y-01 (nagyítás), SEO-01 (H1), SEO-02 (canonical), TEC-02 (jQuery), TEC-03 (cache), LEG-01 (süti-sáv), FUN-12 (mezőtípusok), FUN-07 (502-k) |

**Kulcsmegállapítás:** a 4 kritikus hibából 3 (FUN-01, FUN-02, CNV-01) azonnal javítható adminból, a negyedik (UX-01) valószínűleg egyedi CSS-sel. **Az üzletileg legfontosabb javítások tehát nem igényelnek platformdöntést.** A mélyebb – akadálymentességi, biztonsági, teljesítménybeli és SEO-alap – hibák viszont a platformhoz kötöttek.

## 6. Egyszerűen javítható vs. architekturális problémák

### Egyszerűen javítható (napokban mérhető, platformfüggetlen)
- Hibás telefonlinkek, üres `<a href="+36…">`, térképlink (FUN-01, 02, 04, 10)
- Ároldal, GYIK, ÁSZF, árjegyzék-csempe (CNV-01, SEO-07, LEG-03, FUN-09)
- Hangnem, korrektúra, ellentmondások (UX-05, 07, 08)
- NAP-egységesítés (SEO-04), title/description (SEO-05, 06)
- Régi Ads-snippet, Facebook-chat eltávolítása (TEC-01, FUN-08) – ha a kódblokk adminból elérhető
- Slider kikapcsolása, menü rövidítése (UX-02, UX-03) – ha a sablon engedi

### Mélyebb architekturális hiányosságra utal
- **UA-alapú kettős sablon**, tiltott nagyítás, `Vary` nélküli kiszolgálás → a reszponzív alapelv hiánya (TEC-04, A11Y-01)
- **Sablonszintű SEO-hiányok** (H1, canonical, sitemap-hely) → az ügyfél nem rendelkezik a `<head>` és a sablon felett (SEO-01, 02, 08)
- **Elavult könyvtárak és cache-politika** platformszinten → biztonsági és üzemeltetési kockázat, amelyet csak a szolgáltató kezelhet (TEC-02, 03, 05, 07)
- **Időszakos 502-k és kapcsolatbontások** osztott infrastruktúrán (FUN-07) → nincs ügyfél által ellenőrizhető SLA a 99%-on túl
- **Akadálymentesség** (címkék, mezőtípusok, landmarkok) a platform űrlap- és sablonmotorjában (A11Y-03, 05, FUN-12)
- **Szolgáltatói függés**: design nem vihető át, export nincs szerződésben, a domain jogosultja ismeretlen

## 7. Ismeretlen tényezők, amelyeket a döntés előtt tisztázni kell

| # | Kérdés | Kitől | Miért kritikus |
|---|---|---|---|
| 1 | Ki a budapest-temetkezes.hu domain jogosultja (ügyfél vagy Oleander)? | domain.hu / Oleander | Platformváltásnál a domain-átvitel a legnagyobb jogi-technikai kockázat |
| 2 | Mennyi a jelenlegi éves díj, mikor jár le a 12 hónapos határozott idő? | Számlák / Oleander | TCO-alap, kilépési időzítés |
| 3 | Van-e átállási lehetőség a honlap.hu jelenlegi generációjára, és mennyibe kerül? | Oleander | A B forgatókönyv megvalósíthatósága |
| 4 | Vállalja-e a szolgáltató a sablonszintű javításokat (viewport, H1, canonical, cache, süti-sáv)? Mennyiért? | Oleander | Az A forgatókönyv lefedettsége |
| 5 | Van-e egyedi 301-átirányítás és `<head>`-kód beillesztési lehetőség az adminban? | Admin-hozzáférés | SEO-javítások A-ban |
| 6 | Kiadja-e a szolgáltató a tartalmat és a képeket strukturált exportként? | Oleander | Migrációs költség C-ben (−10–20 óra) |
| 7 | Használatban vannak-e `@budapest-temetkezes.hu` e-mail fiókok? | Ügyfél | Platformváltáskor az e-mailt is költöztetni kell |
| 8 | Mi a `temetkezes.hu` és a Szomorúfűz márka viszonya (logó, e-mail-domain, Debrecen/Nyíregyháza telephely)? | Ügyfél | Márka- és domainstratégia, több oldal közös platformja |
| 9 | Forgalmi és konverziós adatok (Search Console, GA4, Ads, hívásnapló) | Ügyfél | Megtérülési modell valós alapja |
