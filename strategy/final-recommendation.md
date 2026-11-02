# Végső szakmai ajánlás

## 1. Ajánlás röviden

> **Kétlépcsős út: azonnali gyorsjavítás a jelenlegi rendszeren (A-gyors), majd egy 30 napos adatgyűjtés után döntési kapu, és – a feltételek teljesülése esetén – teljes újraépítés (C) saját, hordozható rendszeren, a 4–6. hónapra tervezett élesítéssel.**

| Időtáv | Javaslat | Indoklás |
|---|---|---|
| **Rövid táv (0–30 nap)** | **A-gyors**: a 4 kritikus hiba és a legolcsóbb, nagy hatású javítások a jelenlegi platformon (≈ 40 óra, ≈ 0,7 M Ft nettó) + a közös tartalmi csomag (K) elindítása | A hibás telefonlinkek és a hiányzó mobilos hívásgomb most is ügyfeleket veszít. A javítás ≈ 9 többletmegrendelésből megtérül 3 év alatt, és a tartalmi munka a C-be átvihető |
| **Hároméves táv** | **C – teljes újraépítés**, WordPress vagy Astro alapon (a választás a szerkesztési modelltől függ) | A döntési mátrixban 6,85 vs. 5,85 (A) és 5,80 (B); az egyetlen forgatókönyv, amely mind a 62 hibát kezeli, megszünteti a szolgáltatói függést, és 5 éves távon olcsóbb, mint az A + későbbi újraépítés (≈ 11,8–12,4 M vs. ≈ 14,3 M Ft) |
| **Nem javasolt** | B2 (hibrid proxy) | Kettős üzemeltetés, törékeny SEO, a C költségének 60–70%-a |
| **Feltételesen** | B1 (a platform újabb generációja) | Csak akkor, ha a szolgáltató írásban garantálja a sablonszintű javításokat és az URL-megőrzést (ld. 3. pont) |

**Költségkeret (reális, nettó):** A-gyors 0,7 M + C 7,6 M (benne K-csomag és 20% tartalék) = **≈ 8,3 M Ft egyszeri**; 3 éves TCO ≈ **10,7 M Ft**. A minimum–magas sáv 5,0–24,3 M Ft – a magas szint prémium ügynökséget feltételez; **2–3 árajánlat bekérése erősen javasolt**.

## 2. Miért nem az A hosszú távon, és miért nem a B?

- **A:** a hibák kb. 32%-a (20 tétel) – köztük a nagyítás tiltása, a H1/canonical hiánya, az elavult könyvtárak, a cache és a süti-sáv – **csak a platformszolgáltató tudja javítani**. A platformgeneráció öregszik, a design nem hordozható, és 3 év múlva nagy valószínűséggel mégis újraépítés kell.
- **B1:** a C költségének kb. kétharmadáért jobb sablont ad, de a függés, a zárt motor és a korlátozott SEO- és akadálymentességi kontroll marad, miközben a megvalósíthatósága ❔ ismeretlen.

## 3. Milyen feltételek mellett változna a döntés?

| Ha… | …akkor |
|---|---|
| a weboldalas érdeklődés **< 20 / hó**, és az organikus forgalom elhanyagolható | **A + K**, a C elhalasztása 12 hónappal; a pénzt inkább helyi jelenlétre (Cégprofil, vélemények) érdemes fordítani |
| a weboldalas érdeklődés **> 50 / hó** | C mielőbb; a megtérülés 3 éven belül valószínű (ROI alapeset ≥ 0) |
| a szolgáltató írásban vállalja: H1, canonical, viewport, cache, süti-sáv javítása + átállás az új generációra az URL-ek megtartásával, ≤ 2,5 M Ft-ért | **B1** újraértékelendő (a döntési mátrixban 6,40 – a C-hez közelít) |
| a domain jogosultja a szolgáltató, és az átvitel vitás | **jogi tisztázás** a C előtt; addig A |
| 12–24 hónapon belül online árkalkulátor, foglalás vagy ügyfélfiók a cél | C **Next.js**-sel (+25–40% fejlesztés) |
| a tartalmat kizárólag külső partner szerkeszti, ritkán | C **Astro**-val |
| a munkatársak maguk frissítik az árakat, híreket | C **WordPress**-szel |
| a `temetkezes.hu` egy közös márka több oldallal (Debrecen, Nyíregyháza) | **közös platform több oldalra** → a C fajlagos költsége csökken, a döntés erősödik |

## 4. A legnagyobb ismeretlen tényezők

| # | Ismeretlen | Hatás a döntésre | Kockázat, ha nem tisztázzuk |
|---|---|---|---|
| 1 | **Weboldalas érdeklődési volumen** (hívás + űrlap) | A ROI teljes egészében ettől függ | Túl- vagy alulberuházás |
| 2 | **Domain-jogosult** és a platformszerződés lejárata | A C ütemezése és jogi megvalósíthatósága | Élesítési csúszás, kettős díj |
| 3 | A platform **újabb generációjának képességei és ára** | A B1 versenyképessége | Egy olcsóbb jó megoldás figyelmen kívül marad |
| 4 | **Organikus forgalom és backlinkek** oldalanként | Az SEO-migráció prioritásai, mely URL-ek érinthetetlenek | Forgalomvesztés a migrációnál |
| 5 | Megrendelésenkénti **fedezet** | ROI | Téves megtérülési kép |
| 6 | Az **e-mail** a domainen (használatban van-e) | Migrációs feladat | E-mail-kiesés élesítéskor |
| 7 | **Márkaarchitektúra** (Szomorúfűz vs. temetkezes.hu) | Egy vagy több oldal, közös platform | Kétszeres fejlesztés |
| 8 | Ki szerkeszti a tartalmat, milyen gyakran | WordPress vs. Astro | Rossz technológiai választás |

## 5. A végleges döntéshez beszerzendő információk

**Az ügyféltől (1–2 hét):**
1. Platformszámlák (éves díj), a szerződés lejárata, a felmondási feltételek.
2. Domain-jogosult igazolása (domain.hu regisztrációs adatok).
3. Hívásnapló 3 hónapra irodánként; űrlapbeérkezések száma; „honnan hallott rólunk” adat.
4. Hozzáférés: Google Search Console, GA4/GTM, Google Ads, Google Cégprofilok.
5. Átlagos fedezet megrendelésenként (könyvelés).
6. Ki és milyen gyakran módosítja ma a tartalmat; kik lennének a jövőbeli szerkesztők.
7. A `temetkezes.hu` szerepe, a vidéki telephelyek online jelenléte.

**A platformszolgáltatótól (Oleander Informatikai Kft., írásban):**
1. Vállalja-e a sablonszintű javításokat (viewport, H1, canonical, cache-fejléc, süti-sáv, űrlapmezők típusa, jQuery)? Határidő és ár?
2. Van-e átállási út a jelenlegi honlap.hu generációra? Megmaradnak-e az URL-ek? Ár, átfutás?
3. Ad-e strukturált tartalomexportot (szöveg, képek, metaadatok)?
4. Domain-átvitel menete, költsége; az e-mail fiókok exportja.
5. Van-e egyedi 301-átirányítás és `<head>`-kód beillesztési lehetőség az adminban?

**Külső:**
1. 2–3 ügynökségi árajánlat a C-re (ez a repozitórium specifikációként használható: hibajegyzék, URL-térkép, migrációs terv).
2. Backlink-profil (pl. Ahrefs / Semrush) – a migrációs prioritásokhoz.

## 6. 30–60–90 napos megvalósítási terv

### 1–30. nap – „Állítsuk el a vérzést, és mérjünk”

| Hét | Teendő | Hibakódok | Felelős | Eredmény |
|---|---|---|---|---|
| 1. | Telefonlinkek, URL-csapda, `/arlista/` ideiglenes oldal/átirányítás, térképlink, árjegyzék-csempe | FUN-01–04, FUN-09, FUN-10 | admin / fejlesztő | 0 hibás hívólink |
| 1. | „0–24 / éjszakai elérhetőség” üzenet minden oldalon; egy kiemelt központi szám | UX-09, CNV-03 | ügyfél + admin | egyértelmű sürgősségi út |
| 1–2. | Sticky hívássáv mobilon egyedi CSS-sel (ha a platform engedi); kontraszt, fókusz | UX-01, A11Y-02, A11Y-04 | fejlesztő | első képernyős CTA |
| 1–2. | Régi Ads-snippet és Facebook-chat eltávolítása; GA4-események (`tel:` kattintás, űrlap); Search Console | TEC-01, FUN-08, LEG-02 | fejlesztő | mérhető alapállapot |
| 1–2. | Írásos kérdések a platformszolgáltatónak (5. pont); a domain-jogosult tisztázása | – | ügyfél | döntési input |
| 2–4. | K-csomag indítása: ároldal-szöveg, GYIK, NAP-egységesítés, Cégprofilok frissítése | CNV-01, SEO-07, SEO-04 | szövegíró + ügyfél | az ároldal élesben (a jelenlegi platformon) |
| 2–4. | Ajánlatkérés a C-re 2–3 ügynökségtől | – | ügyfél | összehasonlítható ajánlatok |
| 4. | Adatgyűjtés: hívásnapló, űrlapok, Search Console-kiindulás | – | ügyfél | ROI-modell valós adattal |

**A-gyors költség:** ≈ 0,4–1,45 M Ft (reális: 0,7 M) + a K-csomag első része.

### 31–60. nap – „Döntés és tervezés”

| Hét | Teendő | Kimenet |
|---|---|---|
| 5. | **Döntési kapu:** ROI-modell valós adatokkal, a szolgáltató válaszai, az ajánlatok összevetése → A / B1 / C (+ WordPress vagy Astro) | írásos döntés, keretösszeg |
| 5–6. | (C esetén) Szerződés: fix ár + változáskezelés; a kód, a design és a tartalom tulajdonjoga az ügyfélé; karbantartási SLA | aláírt szerződés |
| 6–7. | Discovery: IA, oldaltípusok, a `redirect-map.csv` véglegesítése Search Console-adat alapján | jóváhagyott URL-térkép |
| 7–8. | Drótvázak (mobile-first), design system, akadálymentességi követelmények (WCAG 2.1 AA) | jóváhagyott design |
| 5–8. | K-csomag folytatása: szolgáltatásoldalak, irodaoldalak, Rólunk; fotózás | jóváhagyott szövegek |

### 61–90. nap – „Építés és tesztelés”

| Hét | Teendő | Kimenet |
|---|---|---|
| 9–12. | Fejlesztés stagingen (`noindex` + jelszó), sablonok, űrlapok, sticky CTA, séma, GTM/consent | működő staging |
| 10–12. | Tartalommigráció (107 URL, képek), 301-szabályok | teljes tartalom stagingen |
| 12–13. | Tesztek: átirányítás (100% CSV-egyezés), axe (0 critical/serious), Lighthouse (LCP ≤ 2,5 s), Playwright (minden `tel:` helyes) | tesztjegyzőkönyv |
| 13. | Élesítési terv: DNS TTL, domain/e-mail átvitel, visszaállítási terv, 30 napos párhuzamos régi előfizetés | élesítési „go/no-go” |

**Élesítés:** a 14–20. hét között (a reális C-ütemezés 16 hét), utána 8–12 hetes SEO-monitorozás a [migrációs terv](seo-migration-plan.md) szerint.

### Sikermutatók (a 90. napon és az élesítés után 3 hónappal)

| Mutató | 90. nap | Élesítés + 3 hónap |
|---|---|---|
| Hibás `tel:` linkek | 0 | 0 |
| Mérhető hívás- és űrlapkonverzió | igen | irodánkénti havi riport |
| Mobil LCP (labor) | – (régi oldal) | ≤ 2,5 s |
| axe critical/serious | – | 0 |
| Organikus kattintás a kiinduló értékhez képest | baseline | ≥ 100% |
| Weboldalas érdeklődés a kiinduló értékhez képest | baseline + gyorsjavítás-hatás | +15–25% (alapeset 🟨) |
