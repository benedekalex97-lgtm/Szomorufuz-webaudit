# Weboldal-audit – Szomorúfűz Temetkezés (budapest-temetkezes.hu)

Független, külső audit a https://www.budapest-temetkezes.hu publikus weboldaláról.
**Dátum:** 2026. november 2. · **Nyelv:** magyar · **Hozzáférés:** kizárólag publikus oldal (nincs forráskód, admin vagy analitika).

> Ez a repozitórium csak az audit dokumentációját tartalmazza. Az éles weboldal nem lett módosítva.

## Eredmény röviden

- **107** publikus oldal feltérképezve, **62** tétel azonosítva: **4 kritikus**, **25 magas**, **26 közepes**, **7 alacsony**.
- Legsúlyosabb: két telefonlink rossz/nem létező számot hív; mobilon nincs látható hívásgomb; nincs hamvasztási ár, az „Árlista” 404.
- Lighthouse (mobil): Performance **49–74**, Accessibility **65–80**, Best Practices **71–96**, SEO **92**.
- A kritikus hibák nagy része **néhány óra** munkával javítható.

👉 Kezdje itt: **[Vezetői összefoglaló](reports/executive-summary.md)** · **[TOP 20 és ütemterv](reports/improvement-roadmap.md)**

## Jelentések

| Fájl | Tartalom |
|---|---|
| [reports/executive-summary.md](reports/executive-summary.md) | Vezetői összefoglaló, kritikus hibák, első 30 nap |
| [reports/issue-register.md](reports/issue-register.md) | **Hibajegyzék** – minden hiba egyedi kóddal, URL-lel, súlyossággal, bizonyítékkal, hatással, javítással, ráfordítással |
| [reports/ui-ux-audit.md](reports/ui-ux-audit.md) | Vizuális hierarchia, tipográfia, színek, CTA-k, IA, hangnem, reszponzivitás |
| [reports/technical-audit.md](reports/technical-audit.md) | HTTP, cache, crawl, HTML-szemantika, konzolhibák, követőkódok, Lighthouse/Core Web Vitals |
| [reports/seo-audit.md](reports/seo-audit.md) | Indexelhetőség, szolgáltatásoldalak, címsorok, helyi SEO, NAP, strukturált adat mintával |
| [reports/accessibility-audit.md](reports/accessibility-audit.md) | WCAG 2.1 AA – axe-core, billentyűzet, kontraszt, érintési célpontok |
| [reports/conversion-audit.md](reports/conversion-audit.md) | Az 5 felhasználói forgatókönyv (A–E) értékelése, javasolt mobil célállapot |
| [reports/improvement-roadmap.md](reports/improvement-roadmap.md) | **TOP 20 prioritás**, fázisolt ütemterv, KPI-k |
| [reports/site-map.md](reports/site-map.md) | Oldaltérkép: mind a 113 lekért URL státusszal, szószámmal, title-lel |

## Hibakód-rendszer

| Előtag | Terület |
|---|---|
| `FUN` | Funkcionális hibák (linkek, telefonszámok, menük, űrlapok) |
| `CNV` | Konverzió, ügyfélút |
| `UX` | Felhasználói élmény, vizuális megjelenés, tartalom, hangnem |
| `TEC` | Technikai (HTTP, cache, könyvtárak, teljesítmény) |
| `SEO` | Keresőoptimalizálás, helyi keresés |
| `A11Y` | Akadálymentesség |
| `LEG` | Adatvédelmi / jogi kockázat (nem jogi tanács) |

Bizonyítottság: **B** = bizonyított · **F** = feltételezett · **J** = javaslat.

## Bizonyítékok és nyers adatok

| Útvonal | Tartalom |
|---|---|
| `screenshots/` | 63 képernyőkép: `{mobile,tablet,desktop}-{oldal}-fold.png` (első képernyő), `…-full.jpg` (teljes oldal), mobilmenü, űrlap, fókusz |
| `data/crawl.json` | Crawl: státuszok, átirányítások, title, meta, canonical, H1–H2, linkek, `tel:`/`mailto:`, űrlapok |
| `data/browser-audit.json` | Playwright: konzolhibák, hibás erőforrások, túlcsordulás, érintési célpontok, axe-core eredmények |
| `data/functional-test.json` | Mobilmenü, süti-sáv, űrlap-szerkezet, billentyűzetfókusz |
| `data/consent-check.json` | Harmadik feles kérések és sütik a hozzájárulás előtt |
| `data/lighthouse/` | 12 Lighthouse-riport (HTML + JSON), összesítő: `data/lighthouse-summary.md` |

## Módszertan és eszközök

| Eszköz | Verzió | Használat |
|---|---|---|
| Python crawler (`scripts/crawl.py`) | requests + BeautifulSoup | teljes belső bejárás, 1,2 s késleltetéssel |
| Playwright + Chromium | előtelepített | 3 viewport, képernyőképek, konzol, hálózat |
| axe-core | 4.10.2 | WCAG 2.0/2.1 A/AA + best practice |
| Lighthouse | 12.8.2 | mobil és desktop, 6 kulcsoldal |
| curl | – | HTTP-fejlécek, átirányítások, User-Agent összehasonlítás |

Újrafuttatás:
```bash
cd tools && npm install && cd ..        # axe-core
python3 scripts/crawl.py data/crawl.json 1.2
node scripts/browser-audit.js
node scripts/functional-test.js
node scripts/consent-check.js
./scripts/lighthouse.sh                 # npm i -g lighthouse
python3 scripts/build_inventory.py
```

### Etikai és biztonsági keretek
- Csak olvasó GET-kérések, kérésenként késleltetéssel; a `robots.txt` által tiltott `/admin/` kihagyva.
- Űrlap nem lett beküldve, hívás nem lett indítva, süti-hozzájárulás nem lett megadva.
- Hozzáférésvédelem megkerülése, terheléses vagy destruktív teszt nem történt.

### Korlátok
- Terepi Core Web Vitals (CrUX) nem volt lekérhető (PageSpeed API kvóta) – csak laboradat.
- A forgalom TLS-bontó kimenő proxyn ment át: a tanúsítvány, a HTTP/2 és részben a biztonsági fejlécek nem vizsgálhatók megbízhatóan; a kapcsolatbontások egy része a proxyból is eredhet.
- A Teendők oldal desktop Lighthouse-futása `NO_FCP` hibával leállt (headless környezet); a mobil futás sikeres.
- Search Console, Google Cégprofil, analitika és hívásnapló nem volt elérhető, ezért a forgalmi és üzleti hatások becslések.

---

## Stratégiai és gazdaságossági elemzés (2. fázis)

Döntés-előkészítő anyag az auditra építve – az audit dokumentumai változatlanok.

👉 Kezdje itt: **[strategy/EXECUTIVE-DECISION.md](strategy/EXECUTIVE-DECISION.md)** (kétoldalas vezetői összefoglaló)

| Fájl | Tartalom |
|---|---|
| [technology-assessment.md](strategy/technology-assessment.md) | Platformazonosítás (Oleander / honlap.hu), technikai adósság, a 62 hiba javíthatósága |
| [scenario-comparison.md](strategy/scenario-comparison.md) | A / B / C forgatókönyv; WordPress, Astro, Next.js összevetése |
| [cost-estimation.md](strategy/cost-estimation.md) | Egyszeri költségek (min / reális / magas), források és feltételezések |
| [three-year-tco.md](strategy/three-year-tco.md) | Éves üzemeltetés, 3 és 5 éves TCO |
| [roi-model.md](strategy/roi-model.md) | Hipotetikus megtérülési modell, fedezeti pont, érzékenység |
| [seo-migration-plan.md](strategy/seo-migration-plan.md) + [redirect-map.csv](strategy/redirect-map.csv) | URL-megőrzés, 301, canonical, séma, tesztelés |
| [decision-matrix.md](strategy/decision-matrix.md) | Súlyozott döntési mátrix, érzékenység |
| [final-recommendation.md](strategy/final-recommendation.md) | Ajánlás, ismeretlenek, 30–60–90 napos terv |

Modell: `python3 scripts/strategy_model.py` · URL-térkép: `python3 scripts/build_redirect_map.py`
