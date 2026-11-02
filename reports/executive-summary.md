# Vezetői összefoglaló

**Weboldal:** https://www.budapest-temetkezes.hu – Szomorúfűz Temetkezés (Szomorúfűz Temetkezési Hálózat Kft.)
**Audit dátuma:** 2026. november 2. · **Terjedelem:** 107 publikus oldal, 3 eszközméret, 62 azonosított tétel

## A lényeg egy bekezdésben

A weboldal tartalmilag sokat ad (öt budapesti iroda, részletes leírás a hamvasztásról, az iratokról és a megközelítésről), de **pont a legfontosabb pillanatban hagyja cserben a látogatót**: két telefonlink rossz számot hív, mobilon nincs látható hívásgomb, nem derül ki, kit lehet éjszaka hívni, a hamvasztásnak nincs feltüntetett ára, és az „Árlista” link hibaoldalra visz. Emellett a megjelenés kb. 12 éves, a hangnem helyenként reklámízű, a jogi oldalak (ÁSZF, süti-hozzájárulás) hiányosak. A kritikus hibák többsége **néhány óra alatt javítható**, és azonnal több beérkező hívást hozhat.

## Állapot egy pillantásra

| Terület | Állapot | Legfontosabb megállapítás |
|---|---|---|
| Kapcsolatfelvétel | 🔴 | 2 hibás telefonlink; mobilon az első szám 4 793 px mélyen |
| Árak, átláthatóság | 🔴 | hamvasztási ár nincs, „Árlista” → 404 |
| Ügyfélélmény (mobil) | 🟠 | 39%-os süti-sáv, 30–37 mezős űrlapok, vízszintes görgetés |
| Bizalom és hangnem | 🟠 | értékesítési szövegek, üres GYIK/Üzenőfal, 2014-es hírek, elírások |
| Helyi SEO | 🟠 | nincs strukturált adat, NAP-ellentmondások (telefon, irányítószám, házszám) |
| Technikai SEO | 🟠 | aloldalakon nincs H1, a fő oldalakon nincs canonical, URL-csapda |
| Teljesítmény (mobil, labor) | 🟠 | Lighthouse 49–74; LCP 3,5–5,7 s; CLS akár 0,35 |
| Akadálymentesség | 🟠 | nagyítás tiltva, kontraszt 1,4:1, nem látható fókusz; Lighthouse 65–80 |
| Biztonság, platform | 🟠 | jQuery 1.12.4 / jQuery UI 1.8.24, egyéves HTML-cache, időszakos 502-k |
| Adatvédelem | 🟠 | előre bepipált marketing-süti, nincs elutasítás (a Consent Mode alapállapota viszont helyes) |
| Lighthouse SEO | 🟢 | 92/100 minden mért oldalon |

## A 4 kritikus hiba

1. **FUN-01 – Rossz szám az „Információ” link mögött (minden oldalon).** A látható szám +36 30 847-1915, a telefon a +36 30 313-7920-at hívja.
2. **FUN-02 – Nem létező szám az árajánlatkérő oldalak „Ügyelet” linkjén** (`tel:+3638471915`).
3. **CNV-01 – Nincs ár a hamvasztásra, az „Árlista” link 404.** Az „árgarancia” és a „rejtett költségek nélkül” ígéret így nem hihető.
4. **UX-01 – Mobilon nincs látható hívásgomb.** A haláleset után azonnal segítséget kereső hozzátartozónak 5–6 képernyőt kell görgetnie.

## Bizonyított hibák, feltételezések és javaslatok

| Kategória | Darab | Példa |
|---|---|---|
| Bizonyított hiba (B) | 58 | hibás `tel:` linkek, 404-ek, axe-hibák, Lighthouse-mérések |
| Feltételezett probléma (F) | 2 tétel teljesen, 1 részben (+ egyes hatásbecslések a bizonyított hibáknál) | biztonsági fejlécek (TEC-05, proxy miatt), `alert()` hibaág (FUN-13), a 502-k szerveroldali oka (FUN-07) |
| Fejlesztési javaslat (J) | 1 önálló tétel + minden hibalap javítási része | irodánkénti helyi oldalak |

## Üzleti hatás (becslés, F)

- A sürgős hívások jelentős része mobilról érkezik; a rossz `tel:` célok és a nem látható szám **közvetlenül elvesztett megrendelést** jelentenek – ennek mértéke csak hívásméréssel számszerűsíthető, amely jelenleg nincs.
- Az árak hiánya és a hosszú űrlap miatt az ajánlatkérési arány valószínűleg alacsony; a régi Ads-konverziós kód blokkolva van, így a hirdetések megtérülése nem mérhető megbízhatóan.
- A NAP-ellentmondások és a hiányzó strukturált adat gyengítik a „temetkezés + kerület” típusú helyi kereséseket.

## Javasolt első 30 nap

| Hét | Teendő | Hibakód |
|---|---|---|
| 1. hét | telefonlinkek, üres link, `/arlista/` átirányítás, cache-fejléc, nagyítás engedése | FUN-01–04, TEC-03, A11Y-01 |
| 1–2. hét | sticky hívássáv, 0–24 elérhetőség kiírása, egy központi szám | UX-01, UX-09, CNV-03 |
| 2–3. hét | süti-sáv, Facebook/régi Ads-kód eltávolítása, NAP-egységesítés, strukturált adat | LEG-01/02, TEC-01, SEO-03/04 |
| 3–4. hét | ároldal, rövid 2 lépéses űrlap + visszahívás | CNV-01, CNV-02 |

A teljes TOP 20 lista és a 6 hónapos ütemterv: [improvement-roadmap.md](improvement-roadmap.md).

## Korlátok

- Csak publikus oldal; forráskód, admin, Search Console, Google Cégprofil, hívásnapló nem volt elérhető.
- A teljesítményadatok laboradatok (Lighthouse, kimenő proxyn keresztül); terepi (CrUX) adat a PageSpeed API kvótája miatt nem volt lekérhető.
- A TLS-tanúsítvány és a HTTP/2 a proxy miatt nem volt vizsgálható.
- Űrlapot nem küldtünk be (a szerveroldali validáció és a visszaigazoló e-mail nem tesztelt).
- Valódi képernyőolvasós teszt nem készült.
- A jogi megállapítások kockázatjelzések, nem jogi tanácsadás.
