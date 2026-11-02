# Vezetői döntési összefoglaló – budapest-temetkezes.hu

**Dátum:** 2026. november 2. · **Alap:** 107 oldalas audit (62 hiba), technológiai azonosítás, költség-, TCO- és megtérülési modell. Minden összeg **nettó** forint; bruttó = × 1,27.

## A helyzet

- A weboldal egy **külső szolgáltató (Oleander Informatikai Kft., honlap.hu) zárt, hosztolt honlapkészítőjének régi generációján** fut (🔶 nagyon erős, négy független bizonyítékkal). A design a szolgáltató tulajdona, és nem vihető át; a szerződés nem garantál tartalomexportot.
- **4 kritikus hiba** valószínűleg ma is ügyfelekbe kerül: két telefonlink rossz vagy nem létező számot hív, mobilon nincs látható hívásgomb, a hamvasztásnak nincs ára, és az „Árlista” hibaoldalra visz.
- A 62 hibából **29 a jelenlegi adminból javítható, 13 részben, 20 csak a szolgáltatón keresztül** (viewport, H1, canonical, elavult jQuery, cache, süti-sáv).

## A három lehetőség

| | **A – Felújítás** a jelenlegi rendszeren | **B – Részleges modernizáció** (a szolgáltató újabb platformja) | **C – Teljes újraépítés** (WordPress / Astro) |
|---|---|---|---|
| Egyszeri költség (min – **reális** – magas) | 1,5 – **3,3** – 7,6 M Ft | 2,3 – **5,1** – 11,2 M Ft | 3,6 – **7,6** – 17,0 M Ft |
| Átfutás | 2–6 hét | 8–16 hét | 12–24 hét |
| 3 éves TCO (reális) | **5,1 M Ft** | **7,0 M Ft** | **10,1 M Ft** |
| Kezelt hibák | ≈ 55–68% | ≈ 75–80% ❔ | 100% |
| Szolgáltatói függés | marad | marad | megszűnik |
| SEO-kockázat | alacsony | közepes ❔ | közepes, kezelhető |
| Döntési pontszám – 3 éves / rövid távú nézet | 5,85 / **7,20** | 5,80 / 6,00 | **6,85** / 5,75 |

Minden változat tartalmazza a **közös tartalmi csomagot** (szövegek, ároldal, GYIK, fotók, jogi szövegek; reálisan 1,2 M Ft), amely később bármely rendszerbe átvihető.

## Megtérülés – amit biztosan tudunk, és amit nem

- **Valós forgalmi adat nincs.** Hipotetikus alapesetben (havi 40 weboldalas érdeklődés, 35% megrendelés, 80 000 Ft fedezet) a 3 éves ROI: A −2%, B −8%, C −18%; havi 80 érdeklődésnél: +96% / +85% / +63%.
- **Robusztus mutató – a fedezeti pont:** a 3 éves többletköltség megtérüléséhez havonta **A: 1,6, B: 2,3, C: 3,4 többlet megrendelés** kell.
- **A kritikus hibák gyorsjavítása (≈ 0,7 M Ft) ≈ 9 megrendelésből megtérül 3 év alatt** – ez gyakorlatilag kockázatmentes.
- 5 éves távon a C (≈ 11,8 M) olcsóbb, mint az A + egy későbbi újraépítés (≈ 14,3 M).

## Ajánlás

1. **Most (1–4. hét): A-gyorsjavítás** – telefonlinkek, mobil hívássáv, 0–24 elérhetőség, ároldal, mérés. ≈ **0,7 M Ft**. Ezzel párhuzamosan indul a tartalmi csomag.
2. **30. nap: döntési kapu** valós adatok alapján: hívásnapló, Search Console, a szolgáltató írásos válaszai, a domain-jogosult, 2–3 ügynökségi ajánlat.
3. **Javasolt hároméves irány: C – teljes újraépítés**, élesítés a 4–6. hónapban, tudatos SEO-migrációval (91 URL változatlan, 22 db 301-es átirányítás – kész URL-térkép).
   - **WordPress**, ha a munkatársak maguk szerkesztenek.
   - **Astro**, ha a tartalmat egy partner kezeli, és a minimális karbantartás a cél.
   - **Next.js** csak alkalmazásszerű funkciók (online árkalkulátor, foglalás) esetén.
4. **Teljes keret (reális):** ≈ **8,3 M Ft egyszeri** (gyorsjavítás + C, tartalékkal), 3 éves TCO ≈ **10,7 M Ft**.

## A döntés megváltozik, ha…

| Feltétel | Új javaslat |
|---|---|
| < 20 weboldalas érdeklődés / hó, alacsony organikus forgalom | **A + tartalmi csomag**, C elhalasztva 12 hónappal |
| A szolgáltató írásban vállalja a sablonszintű javításokat + URL-megőrzést, ≤ 2,5 M Ft-ért | **B1** újraértékelése |
| A domain jogosultja a szolgáltató, és az átvitel vitás | Jogi tisztázás előbb, addig **A** |
| A Szomorúfűz több oldalt üzemeltet (temetkezes.hu, vidéki irodák) | **C közös platformon** – a fajlagos költség csökken |

## Döntést igénylő kérdések a vezetés felé

1. Jóváhagyja-e az **A-gyorsjavítást (≈ 0,7 M Ft)** és a **tartalmi csomag** indítását most?
2. Ki szerez be **30 napon belül** hívás- és forgalmi adatot, a szerződéses / domain-információkat és a szolgáltató válaszait?
3. Elfogadható-e **≈ 8–9 M Ft-os** keret a C-re, ha a 30. napi adatok igazolják a megtérülést?

*Részletek: `strategy/` könyvtár – technology-assessment, scenario-comparison, cost-estimation, three-year-tco, roi-model, seo-migration-plan (+ redirect-map.csv), decision-matrix, final-recommendation.*
