# Akadálymentességi audit

**Mérce:** WCAG 2.1 AA (kiegészítve a WCAG 2.2 2.5.8 érintési célpont-szabállyal).
**Módszer:** axe-core 4.10.2 automatikus teszt 12 oldalon desktopon és mobilon (25 futás), Lighthouse Accessibility, Playwright-alapú billentyűzetes és érintési célpont-mérés, képernyőképes szemrevételezés.
A hibakódok a [hibajegyzékre](issue-register.md) hivatkoznak.

> **Korlát:** valódi képernyőolvasós (NVDA/VoiceOver) teszt nem készült; az automatikus eszközök a WCAG-hibák kb. 30–40%-át találják meg. Az alábbi lista ezért minimum, nem teljes megfelelőségi nyilatkozat.

**Miért fontos itt?** A temetkezési oldal látogatói között sok az idős, gyengénlátó hozzátartozó, akik stresszhelyzetben, gyakran telefonon olvasnak. A nagyítás tiltása és a gyenge kontraszt nekik a legnagyobb akadály.

## 1. Pontszámok

| Oldal | Lighthouse Accessibility (mobil / desktop) |
|---|---|
| Főoldal | 80 / 77 |
| Hamvasztás urnakiadás | 70 / 73 |
| Koporsós temetés | 74 / 73 |
| Árajánlat kérés | 74 / 73 |
| Elérhetőség | **65** / 75 |
| Teendők haláleset után | 74 / – |

## 2. axe-core eredmények (összesítve, 25 futás)

| Szabály | Hatás | Érintett elemek | Oldalak | WCAG | Hibakód |
|---|---|---|---|---|---|
| `meta-viewport` – nagyítás tiltva | critical | 13 | 13 (minden mobil) | 1.4.4 | A11Y-01 |
| `label` – címke nélküli mező | critical | 88 | 14 | 1.3.1, 4.1.2 | A11Y-03 |
| `color-contrast` | serious | 69 | 13 | 1.4.3 | A11Y-02 |
| `link-name` – szöveg nélküli link | serious | 30 | 13 | 2.4.4, 4.1.2 | A11Y-06 |
| `frame-title` | serious | 16 | 14 | 4.1.2 | A11Y-08 |
| `aria-hidden-focus` | serious | 13 | 13 | 4.1.2 | A11Y-06 |
| `list` – hibás listaszerkezet | serious | 2 | 2 | 1.3.1 | A11Y-05 |
| `landmark-one-main` | moderate | 25 | 25 | best practice | A11Y-05 |
| `region` | moderate | 852 | 25 | best practice | A11Y-05 |
| `heading-order` | moderate | 20 | 16 | best practice | A11Y-05 |
| `page-has-heading-one` | moderate | 13 | 13 | best practice | SEO-01 |
| `empty-heading` | minor | 4 | 2 | best practice | A11Y-05 |

Nyers adatok: `data/browser-audit.json` → `axe`.

## 3. Kézi / szkriptes ellenőrzések

| Ellenőrzés | Eredmény | WCAG | Hibakód |
|---|---|---|---|
| Látható billentyűzetfókusz | ❌ 8 egymást követő Tab-lépésből 7-nél `outline: none`, `box-shadow: none` (`screenshots/desktop-keyboard-focus.png`) | 2.4.7 | A11Y-04 |
| „Ugrás a tartalomra” link | ❌ nincs | 2.4.1 | A11Y-04 |
| Mobilmenü gomb | ❌ `<a href="javascript:void(0)">` – nincs `button` szerep, `aria-expanded`, `aria-controls` | 4.1.2 | FUN-11 |
| Automatikus tartalomváltás | ❌ 8 mp-es slider, szünet csak egérrel (`pauseOnHover`) | 2.2.2 | A11Y-06 |
| Érintési célpontok (mobil) | ❌ oldalanként 16–30 elem 24 px alatt; rádiógombok 13×13 px, slider-nyilak 15×50 px | 2.5.8 (2.2) | A11Y-07 |
| Szövegméret | ⚠️ desktopon 12 px, `line-height: normal`; mobilon 15–16 px, 28,8 px sormagasság ✅ | 1.4.12 (ajánlás) | A11Y-09 |
| Sorkizárás | ⚠️ `text-align: justify` a főbb szövegeken – diszlexiás olvasóknak nehéz | 1.4.8 (AAA, ajánlás) | A11Y-09 |
| Színnel jelzett információ | ⚠️ piros szövegű kiemelések („Hogyan viheti haza…”), kék #0000ff „IDE” | 1.4.1 (részben) | A11Y-09 |
| Linkszövegek | ⚠️ „>>> IDE <<<”, „kattintson ide” | 2.4.4 | SEO-12 |
| Űrlaphibák jelzése | ⚠️ nincs `required`/`aria-required`, a kötelezőséget csak `*` jelzi; a hibakezelést beküldés nélkül nem tudtuk tesztelni | 3.3.1, 3.3.2 | FUN-12 |
| Süti-sáv | ⚠️ mobilon a képernyő 39%-át fedi, áttetsző háttér miatt a mögötte lévő szöveg átüt | 1.4.3, 1.4.10 | LEG-01 |
| Vízszintes görgetés 320–390 px-en | ❌ /hamvasztas-urnakiadas/ 509 px, /elerhetoseg/ 408 px széles | 1.4.10 | UX-10 |
| Nyelv | ✅ `lang="hu"` | 3.1.1 | – |
| Képek alt-szövege | ✅ nincs hiányzó `alt` attribútum; ⚠️ 202 üres `alt=""` (részben tartalmi képeken) | 1.1.1 | SEO-13 |

## 4. Kontraszt – konkrét példák

| Elem | Előtér | Háttér | Arány | Elvárt |
|---|---|---|---|---|
| Oldalsáv dobozcímek („Megosztás”, „Elérhetőségeink” egyes nézetekben) | #eeeeee | #34def5 | **1,4:1** | 4,5:1 (18 px félkövér: 3:1) |
| Mobilmenü elemei | fehér | világosszürke (~#bbb) | ≈ 1,9:1 (becslés képernyőkép alapján) | 4,5:1 |
| Mobil fejléc „Menü” felirat | fehér | #33e0f6 körüli cián | ≈ 1,5:1 (becslés) | 3:1 (nagy szöveg) |
| Szürke törzsszöveg mobilon | #666 körüli | #eee | ≈ 4,6:1 | határeset |

## 5. Javítási terv

| Lépés | Tartalom | Ráfordítás |
|---|---|---|
| 1. Gyors javítások (1 nap) | `maximum-scale=1` törlése; `:focus-visible` stílus; skip link; iframe `title`; slider-nyilak `aria-label`; a mobilmenü `<button aria-expanded>` | S |
| 2. Űrlapok (1–2 nap) | minden mezőhöz `<label for>`; `required` + `aria-required`; `type=email/tel`, `autocomplete`; hibaüzenetek `aria-live` régióban; nagyobb rádiógombok, teljes sor kattintható | S–M |
| 3. Színek és tipográfia (1–2 nap) | új színpaletta 4,5:1 felett; 16–18 px törzsszöveg; balra zárt szöveg; piros kiemelések megszüntetése | S |
| 4. Szerkezet (redesign részeként) | `header/nav/main/footer`; egy H1; slider megszüntetése; reszponzív, túlcsordulásmentes tördelés | M |
| 5. Ellenőrzés | axe + kézi NVDA/VoiceOver teszt a 6 kulcsoldalon; akadálymentességi nyilatkozat közzététele | S |
