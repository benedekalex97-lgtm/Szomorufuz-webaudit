# Ügyfélélmény és konverzió

A forgatókönyveket valós böngészős bejárással és képernyőképekkel vizsgáltuk (mobilon 390 × 844, desktopon 1440 × 900). Űrlapot nem küldtünk be, hívást nem indítottunk – a `tel:` linkek célját a forráskódból ellenőriztük.
A hibakódok a [hibajegyzékre](issue-register.md) hivatkoznak.

**Értékelési skála:** 1 = nagyon nehéz · 5 = kiváló

## Összefoglaló

| Forgatókönyv | Tájékozódás | Bizalom | Érthetőség | Kapcsolatfelvétel | Átlag |
|---|---|---|---|---|---|
| A. Azonnali segítség haláleset után | 2 | 2,5 | 3 | 2 | **2,4** |
| B. Hamvasztási árak | 2 | 2 | 2,5 | 3 | **2,4** |
| C. Koporsós temetés szervezése | 3 | 3 | 3 | 3 | **3,0** |
| D. Kapcsolatfelvétel mobilról | 1,5 | 2,5 | 3 | 2 | **2,3** |
| E. Szükséges dokumentumok | 3,5 | 3 | 2,5 | 3 | **3,0** |

---

## A. Haláleset után azonnali segítséget kereső hozzátartozó

**Helyzet:** este 23 órakor otthon meghalt az édesapja; telefonon keres „temetkezés Budapest” kifejezésre.

**Út a jelenlegi oldalon:**
1. Főoldal mobilon: menüsáv, cégnév, szlogen, slider, süti-sáv – **telefonszám nincs az első képernyőn** (UX-01).
2. A „Menü” megnyitása után a „Teendők haláleset után” a 6. elem (`screenshots/mobile-menu-open.png`).
3. A Teendők oldal első mondata: „Önnek egyetlen lényeges dolga van, mielőbb felvenni munkatársunkkal a kapcsolatot!” – majd költségekről szól; a „Lakáson történt halálozás esetén” rész a szöveg közepén van, alcímek és lépések nélkül.
4. Telefonszám keresése: az oldalsáv 13 száma mobilon az oldal alján; nyitvatartás 8–16, ügyelet „6:00 – 22:00 óra között hívható”. **23 órakor mi a teendő? Nem derül ki** (UX-09).
5. Ha a felhasználó a „Információ: +36 (30) 847-1915” számra koppint, a telefon a **+36 30 313 7920**-at tárcsázza (FUN-01).

**Erősségek:** a Teendők oldal tartalmilag hasznos (kórházi és otthoni haláleset eltérő menete, boncolás mellőzése); a „Halottszállítás” külön szám létezik.

**Akadályok:** UX-01, UX-09, FUN-01, CNV-03, UX-05 (pénzközpontú nyitány).

**Javaslat:**
- Sticky „📞 Hívjon – 0–24 ügyelet” sáv mobilon, egyetlen számmal.
- Főoldali blokk: „Most hunyt el szerette? – 3 lépés”: 1) orvos hívása / halottvizsgálat 2) hívjon minket bármikor 3) ezeket az iratokat készítse elő.
- A Teendők oldalt lépéssorként (1–2–3), helyzetenként harmonikában (kórház / otthon / idősotthon / külföld).

---

## B. Hamvasztási árakról érdeklődő látogató

**Helyzet:** a család hamvasztást szeretne, és összehasonlítaná az árakat.

**Út a jelenlegi oldalon:**
1. A főoldali slider: „Hamvasztási szolgáltatás **rejtett költségek nélkül**!” → „További információ”.
2. /hamvasztas-urnakiadas/: hosszú leírás, tételes lista a szolgáltatás elemeiről (hamvasztási díj, kellékek, szállítás, ügyintézés) – **de egyetlen ár sincs** (CNV-01).
3. A főoldal szövege: „Erről a tényről az **Árlista** menüpont alatt, egy kattintással meggyőződhet” → **404** (FUN-03).
4. A főoldali „Árjegyzék – Temetkezési és hamvasztási szolgáltatási árak pontos részletezése” csempe nem kattintható (FUN-09).
5. Egyetlen út: 30–37 mezős ajánlatkérő űrlap (CNV-02).

**Hatás:** az „árgarancia” és a „rejtett költségek nélkül” állítás ár nélkül hiteltelen; az árérzékeny látogató a következő találathoz megy, ahol „-tól” árat lát.

**Javaslat:**
- `/arak/` oldal: hamvasztás (alapcsomag, -tól ár, mit tartalmaz / mit nem: pl. temetői díjak, urna, gyászjelentés), szórás temetőben, hajós temetés, urnás temetés, koporsós temetés – összehasonlító táblázatban.
- Árkalkulátor 3 kérdéssel (temetés típusa, hamvak helye, búcsúztatás igen/nem) → irányár, majd „Pontos ajánlatot kérek”.
- A tételes lista mellé ártartomány minden szolgáltatásoldalon.

---

## C. Koporsós temetést szervező hozzátartozó

**Út a jelenlegi oldalon:**
1. Felső menü „Koporsós temetés” vagy főoldali csempe → /koporsos-temetes/.
2. Az oldalon **ár szerepel**: „Koporsós temetési díj: 232.288 Ft-tól. Az ár tartalmazza a 27%-os ÁFA-t!” ✅, leírás a koporsóválasztékról (laminált → tömörfa → szarkofág), budapesti és vidéki temetés.
3. A „koporsóválaszték” részletei nem elérhetők: a hírekből linkelt `/koporsok/` oldal 404 (FUN-05); nincs képes koporsó-katalógus.
4. Nem derül ki, mit tartalmaz a 232 288 Ft (koporsó típusa? temetői díjak? sírnyitás? ravatalozás?).
5. A ravatalozó terem (IX. ker., Ernő u., 40 ülő + 40–50 állóhely) jól bemutatott, galériával ✅.
6. 24 mezős űrlap az oldal alján.

**Javaslat:** a „-tól” ár tartalmának tételes kibontása; koporsó-galéria 3 árkategóriával; a temetői díjak (sírhely, sírnyitás) forrásmegjelöléssel külön; „A temetés menete napról napra” idővonal.

---

## D. Mobiltelefonról kapcsolatfelvételt kezdeményező látogató

**Mérések (390 × 844):**

| Oldal | Első `tel:` link pozíciója | Első képernyőn? |
|---|---|---|
| Főoldal | 4 793 px | ❌ |
| Hamvasztás urnakiadás | 3 640 px | ❌ |
| Elérhetőség | 866 px | ❌ (épp a 844 px-es képernyő alatt) |

**Problémák:**
- A süti-sáv a képernyő 39%-át foglalja el, áttetsző (LEG-01).
- Két hibás hívólink: „Információ” (FUN-01) és az árajánlat-oldali „Ügyelet” (FUN-02 – nem létező szám).
- 13 szám közül kell választani (CNV-03).
- Az e-mail-cím `mailto:` link ✅, de az űrlapokon nincs `type="email"`/`type="tel"`, így nem jön fel a megfelelő billentyűzet (FUN-12).
- A rádiógombok 13×13 px-esek (A11Y-07); az árajánlat-űrlap mobilon 2 201 px magas.
- Nincs visszahívás-kérés, nincs üzenetküldő (a Facebook chat megszűnt, FUN-08).
- Az oldalak mobilon 1,5–5,7 s alatt rajzolják ki a fő tartalmat (TEC-06).

**Javaslat:** sticky hívássáv; „Visszahívást kérek” 2 mezős űrlap (név, telefonszám + opcionális időpont); a teljes űrlap 2. lépésként; nagy érintési felületek.

---

## E. Temetkezési ügyintézéshez szükséges dokumentumokat kereső látogató

**Út a jelenlegi oldalon:**
1. Bal menü → „Szükséges iratok” (14. elem; mobilon a menü második felében).
2. Az oldal tartalmazza a listát (személyi igazolvány, lakcímkártya, születési / házassági anyakönyvi kivonat, válási ítélet, házastárs halotti kivonata, jogosítvány, útlevél) ✅ és megnyugtató információt (a temetés nem marad el a kivonat hiánya miatt) ✅.
3. **Problémák:**
   - Az első bekezdés („Egy haláleset a legnagyobb tragédia…”) kétszer szerepel egymás után.
   - Ellentmondás: „a születési, házassági … kivonat beszerzésében … sajnos nem [tudunk segíteni]”, majd ugyanott: „Díjmentesen ránk bízhatja az ügyintézést teljes körűen, hiányos alap iratok esetében is” (UX-08).
   - A lista folyó szövegben, nem nyomtatható/letölthető ellenőrzőlista.
   - A GYIK üres (SEO-07), a „Jogszabályok” oldalak 1999–2013-as szövegek hivatkozásai, aktualitás-jelölés nélkül (SEO-09).
   - Nincs külön útmutató a temetési/önkormányzati támogatásról (a hírek között 2014-es cikk van róla).

**Javaslat:** „Iratok ellenőrzőlista” nyomtatható PDF-ként és kipipálható listaként; helyzet szerinti bontás (házas / özvegy / elvált / külföldön született); „Ezeket mi intézzük – ezeket Önnek kell” kétoszlopos táblázat; utolsó felülvizsgálat dátuma.

---

## Konverziós tölcsér – mérhetőség

| Elem | Állapot |
|---|---|
| Google Tag Manager | van (GTM-NBJCMVB), Consent Mode `denied` alapállapottal ✅ |
| Régi Ads-konverziós kód | `http://` miatt blokkolva → valószínűleg nem mér (TEC-01) |
| Hívásmérés (`tel:` kattintás esemény) | nem látható a forráskódban (F – a GTM-konténer tartalma nem volt vizsgálható) |
| Űrlap-beküldés mérés | xajax AJAX-beküldés – külön esemény nélkül nehezen mérhető (F) |

**Javaslat:** GTM-ben `tel:` és `mailto:` kattintás-, űrlap-elküldés- és ároldal-megtekintés események; GA4 konverziók; havi riport irodánként (melyik szám hány hívást kap).

## A javasolt célállapot – mobil főoldal vázlata

```
┌──────────────────────────────┐
│ Szomorúfűz Temetkezés   ☰    │
├──────────────────────────────┤
│ Őszinte részvétünk.          │
│ Minden teendőben segítünk –  │
│ éjjel-nappal.                │
│ [ 📞 Hívás: 06 30 … ]        │
│ [ Mit tegyek most? ]         │
├──────────────────────────────┤
│ Hamvasztás      …… Ft-tól  › │
│ Koporsós temetés 232 288 Ft› │
│ Hajós temetés   …… Ft-tól  › │
├──────────────────────────────┤
│ ★ 4,8 – 120 Google-vélemény  │
│ 5 iroda Budapesten         › │
└──────────────────────────────┘
│ 📞 Hívás 0–24  │ ✉ Ajánlat  │  ← rögzített alsó sáv
```
