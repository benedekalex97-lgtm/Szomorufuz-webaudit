"""Stratégiai modell: költség, 3 éves TCO, megtérülés (hipotetikus), döntési mátrix,
valamint a 62 auditált hiba javíthatósága forgatókönyvenként.

Minden összeg NETTÓ forint (ÁFA nélkül), ha másként nincs jelölve. ÁFA: 27%.
Futtatás: python3 scripts/strategy_model.py  -> data/strategy-model.json + kiírás
"""
import json, math

VAT = 0.27
LEVELS = ["min", "real", "high"]

# --- Óradíjak (saját becslés, piaci támpont: financera.hu szabadúszó 6–15 eFt/óra) ---
DEV_RATE = {"min": 12_000, "real": 16_000, "high": 22_000}      # fejlesztő/ügynökségi átlag
COPY_RATE = {"min": 8_000, "real": 12_000, "high": 18_000}      # szövegíró / tartalom

# --- Közös tartalmi csomag (K): minden forgatókönyvben szükséges ---
K_HOURS = {"min": 40, "real": 60, "high": 90}  # kulcsoldalak, ároldal, GYIK, 5 iroda, hangnem
K_FIXED = {  # külső szolgáltatás, Ft
    "Fotózás (irodák, csapat, ravatalozó)": {"min": 150_000, "real": 300_000, "high": 600_000},
    "Jogi szövegek (ÁSZF, adatkezelés, süti) felülvizsgálata": {"min": 100_000, "real": 200_000, "high": 400_000},
}

# --- Technikai munkacsomagok (óra) ---
PACKAGES = {
    "A": {
        "Kritikus hibák (tel:, 404, URL-csapda, NAP)": (4, 6, 10),
        "Tartalom beépítése adminban (ároldal, GYIK, űrlapok, menü, title/description 107 oldal, alt)": (24, 36, 60),
        "Egyedi CSS (sticky hívássáv, kontraszt, fókusz, tipográfia, slider ki)": (8, 16, 30),
        "Mérés, consent, strukturált adat (ha a platform enged egyedi kódot)": (8, 14, 24),
        "Képoptimalizálás és újrafeltöltés": (8, 12, 20),
        "Egyeztetés a platformszolgáltatóval, QA, projektvezetés": (10, 16, 28),
    },
    "B": {
        "Felmérés, információs architektúra": (8, 12, 20),
        "Sablon testreszabása / arculat az új platformgenerációban": (16, 30, 50),
        "Oldalak újraépítése az oldalépítőben (~60 indexelendő oldal + űrlapok)": (40, 60, 90),
        "SEO-migráció (ha az URL-ek változnak), átirányítások": (8, 16, 30),
        "Akadálymentesség, teljesítmény, QA": (8, 14, 24),
        "Mérés, consent, strukturált adat": (8, 12, 20),
    },
    "C": {
        "Felmérés, IA, URL-térkép, tartalomstratégia": (16, 24, 40),
        "UX/UI tervezés (drótváz, design system, 8–10 sablon)": (30, 50, 80),
        "Fejlesztés (téma/komponensek, űrlapok, sticky CTA, irodaoldalak, árak, GYIK, séma)": (60, 100, 160),
        "Tartalommigráció (107 URL, képek, archív hírek)": (24, 40, 70),
        "SEO-migráció (301-térkép, canonical, sitemap, élesítési teszt, 8 hetes monitorozás)": (16, 24, 40),
        "Akadálymentesség, teljesítmény, cross-device QA": (16, 24, 40),
        "Mérés, consent (GTM, GA4, hívásmérés)": (8, 12, 20),
    },
}
PM_SHARE = {"A": 0.0, "B": 0.10, "C": 0.15}  # A-nál a PM benne van a csomagban
ONE_OFF_FIXED = {  # Ft, külső / szolgáltatói díjak (saját feltételezés)
    "A": {"Platformszolgáltatói kiegészítő díjak (sablonszintű módosítás, ha vállalja)": {"min": 0, "real": 150_000, "high": 500_000}},
    "B": {"Platformszolgáltatói díj (új generáció / Pro csomag / migrációs segítség)": {"min": 100_000, "real": 300_000, "high": 700_000}},
    "C": {"Licencek, első év (pl. prémium bővítmények / CMS)": {"min": 50_000, "real": 100_000, "high": 200_000}},
}
RISK_RESERVE = {"A": 0.10, "B": 0.25, "C": 0.20}
DURATION_WEEKS = {"A": (2, 4, 6), "B": (8, 12, 16), "C": (12, 16, 24)}

# --- Éves üzemeltetés (Ft/év) ---
ANNUAL = {
    "A": {
        "Platform-előfizetés (honlap.hu / Oleander; ár nem nyilvános – FELTÉTELEZÉS)": {"min": 60_000, "real": 150_000, "high": 300_000},
        "Karbantartás, tartalomfrissítés (1 / 2 / 4 óra/hó)": {"min": 1 * 12 * 12_000, "real": 2 * 12 * 16_000, "high": 4 * 12 * 22_000},
        "Harmadik fél (consent-eszköz, uptime-monitor, hívásmérés)": {"min": 0, "real": 60_000, "high": 250_000},
    },
    "B": {
        "Platform-előfizetés, magasabb csomag (FELTÉTELEZÉS)": {"min": 100_000, "real": 200_000, "high": 400_000},
        "Karbantartás, tartalomfrissítés (1 / 2 / 4 óra/hó)": {"min": 1 * 12 * 12_000, "real": 2 * 12 * 16_000, "high": 4 * 12 * 22_000},
        "Harmadik fél (consent-eszköz, uptime-monitor, hívásmérés)": {"min": 0, "real": 60_000, "high": 250_000},
    },
    "C": {
        "Hosting (menedzselt WordPress / statikus hosting) + domain": {"min": 30_000, "real": 90_000, "high": 240_000},
        "Licencek (bővítmények / CMS)": {"min": 50_000, "real": 100_000, "high": 200_000},
        "Karbantartás: frissítések, mentés, biztonság, kis módosítások (2 / 3 / 5 óra/hó)": {"min": 2 * 12 * 12_000, "real": 3 * 12 * 16_000, "high": 5 * 12 * 22_000},
        "Harmadik fél (consent-eszköz, uptime-monitor, hívásmérés)": {"min": 0, "real": 60_000, "high": 250_000},
    },
}


def lvl(t, i):
    return t[i] if isinstance(t, tuple) else t


def one_off(s):
    out = {}
    for i, L in enumerate(LEVELS):
        h = sum(v[i] for v in PACKAGES[s].values())
        h = h * (1 + PM_SHARE[s])
        tech = h * DEV_RATE[L]
        fixed = sum(v[L] for v in ONE_OFF_FIXED[s].values())
        k = K_HOURS[L] * COPY_RATE[L] + sum(v[L] for v in K_FIXED.values())
        base = tech + fixed + k
        reserve = base * RISK_RESERVE[s]
        out[L] = {"hours": round(h), "tech": tech, "fixed": fixed, "content": k, "base": base,
                  "reserve": reserve, "total": base + reserve}
    return out


def annual(s):
    return {L: sum(v[L] for v in ANNUAL[s].values()) for L in LEVELS}


def tco(s):
    o, a = one_off(s), annual(s)
    return {L: o[L]["total"] + 3 * a[L] for L in LEVELS}


# --- A -> C útvonal: A gyorsjavítások most, C 6. hónapban; a tartalmi csomag egyszer fizetendő ---
def path_a_quick_then_c():
    quick = {"min": 30 * DEV_RATE["min"], "real": 40 * DEV_RATE["real"], "high": 60 * DEV_RATE["high"]}
    o_c, a_a, a_c = one_off("C"), annual("A"), annual("C")
    return {L: quick[L] * 1.10 + o_c[L]["total"] + 0.5 * a_a[L] + 2.5 * a_c[L] for L in LEVELS}, quick


# --- Megtérülés: HIPOTETIKUS alapadatok (nincs valós forgalmi adat) ---
HYPO = {
    "web_leads_per_month": 40,      # hívás + űrlap, a weboldalról
    "close_rate": 0.35,             # érdeklődésből megrendelés
    "contribution_per_order": {"kons": 60_000, "alap": 80_000, "opt": 100_000},  # fedezet / megrendelés
    "ads_spend_per_month": 300_000, # Google Ads, hipotetikus
}
UPLIFT = {  # érdeklődések növekedése 12 hónap után (feltételezés, audit alapján indokolva)
    "A": {"kons": 0.05, "alap": 0.12, "opt": 0.20},
    "B": {"kons": 0.08, "alap": 0.18, "opt": 0.30},
    "C": {"kons": 0.10, "alap": 0.25, "opt": 0.40},
}
RAMP = {"A": [0.8, 1.0, 1.0], "B": [0.5, 1.0, 1.0], "C": [0.35, 1.0, 1.0]}  # év1 részarány (bevezetési idő, SEO-átmenet)


STATUS_QUO_ANNUAL = {"min": 60_000, "real": 150_000, "high": 300_000}  # jelenlegi platformdíj (feltételezés)


def incremental_tco(s, L="real"):
    """3 éves TCO mínusz a 'nem csinálunk semmit' alternatíva költsége (3 év platformdíj)."""
    return tco(s)[L] - 3 * STATUS_QUO_ANNUAL[L]


def roi(leads=None):
    leads = leads or HYPO["web_leads_per_month"]
    base_orders = leads * HYPO["close_rate"] * 12
    res = {}
    for s in "ABC":
        res[s] = {}
        t = incremental_tco(s)
        for case in ["kons", "alap", "opt"]:
            extra_orders_y = base_orders * UPLIFT[s][case]
            gain3 = sum(extra_orders_y * r * HYPO["contribution_per_order"][case] for r in RAMP[s])
            cpl_old = HYPO["ads_spend_per_month"] / (leads * 0.4)  # tegyük fel: a leadek 40%-a fizetett
            cpl_new = cpl_old / (1 + UPLIFT[s][case])
            res[s][case] = {"extra_orders_per_year": round(extra_orders_y, 1), "gain_3y": gain3,
                            "roi_3y": (gain3 - t) / t, "cpl_old": cpl_old, "cpl_new": cpl_new,
                            "ads_saving_per_year_if_leads_constant": HYPO["ads_spend_per_month"] * 12 * (1 - 1 / (1 + UPLIFT[s][case]))}
        res[s]["incremental_tco"] = t
        # fedezeti pont: hány többlet megrendelés kell havonta a 3 éves TCO-hoz (alap fedezettel)
        res[s]["breakeven_orders_per_month"] = t / HYPO["contribution_per_order"]["alap"] / 36
    return base_orders, res


# --- Döntési mátrix ---
CRITERIA = [  # (név, súly a 3 éves nézetben, súly a rövid távú nézetben)
    ("Fejlesztési költség", 15, 25),
    ("Fejlesztési idő", 10, 25),
    ("Technikai fenntarthatóság", 15, 5),
    ("SEO-kockázat (10 = alacsony kockázat)", 15, 15),
    ("Mobilos felhasználói élmény", 15, 15),
    ("Biztonság", 10, 5),
    ("Üzemeltethetőség", 10, 5),
    ("Jövőbeni bővíthetőség", 10, 5),
]
SCORES = {
    "A": [9, 9, 3, 9, 4, 3, 7, 2],
    "B": [6, 6, 5, 6, 7, 5, 7, 4],
    "C": [4, 4, 9, 5, 9, 8, 7, 9],
}


def matrix():
    out = {}
    for s, sc in SCORES.items():
        out[s] = {
            "3y": sum(c[1] * v for c, v in zip(CRITERIA, sc)) / 100,
            "short": sum(c[2] * v for c, v in zip(CRITERIA, sc)) / 100,
        }
    return out


# --- 62 hiba javíthatósága: a = adminból / egyedi CSS-sel megoldható; v = platformszolgáltató kell; p = részben ---
FIX_A = {
    "FUN-01": "a", "FUN-02": "a", "CNV-01": "a", "UX-01": "p", "FUN-03": "a", "FUN-04": "a", "LEG-01": "v",
    "UX-09": "a", "CNV-02": "a", "CNV-03": "a", "SEO-04": "a", "SEO-03": "p", "SEO-01": "v", "SEO-02": "v",
    "SEO-07": "a", "TEC-01": "p", "TEC-02": "v", "TEC-03": "v", "TEC-06": "p", "FUN-07": "v", "FUN-12": "v",
    "UX-02": "a", "UX-03": "a", "UX-05": "a", "UX-06": "a", "A11Y-01": "v", "A11Y-02": "p", "A11Y-03": "v",
    "A11Y-04": "p", "FUN-05": "a", "FUN-06": "a", "FUN-08": "p", "FUN-10": "a", "FUN-11": "v", "TEC-04": "v",
    "TEC-05": "v", "TEC-07": "v", "TEC-08": "v", "SEO-05": "a", "SEO-06": "a", "SEO-08": "v", "SEO-09": "a",
    "SEO-10": "a", "SEO-11": "p", "UX-04": "p", "UX-07": "a", "UX-08": "a", "UX-10": "p", "A11Y-05": "v",
    "A11Y-06": "a", "A11Y-07": "p", "A11Y-09": "p", "LEG-02": "p", "LEG-03": "a", "CNV-04": "a", "FUN-09": "a",
    "FUN-13": "v", "TEC-09": "v", "TEC-10": "v", "SEO-12": "a", "SEO-13": "a", "A11Y-08": "v",
}


def fmt(x):
    return f"{x/1_000_000:,.2f}".replace(",", " ").replace(".", ",") + " M Ft"


if __name__ == "__main__":
    result = {"one_off": {s: one_off(s) for s in "ABC"}, "annual": {s: annual(s) for s in "ABC"},
              "tco": {s: tco(s) for s in "ABC"}}
    p, quick = path_a_quick_then_c()
    result["path_A_quick_then_C"] = p
    base_orders, r = roi()
    result["roi"] = r; result["base_orders_per_year"] = base_orders
    result["matrix"] = matrix()
    from collections import Counter
    result["fixability_A"] = dict(Counter(FIX_A.values())); result["fixability_count"] = len(FIX_A)
    json.dump(result, open("data/strategy-model.json", "w"), indent=1, ensure_ascii=False)
    for s in "ABC":
        o = result["one_off"][s]
        print(s, "egyszeri:", {L: (o[L]["hours"], fmt(o[L]["base"]), fmt(o[L]["total"])) for L in LEVELS})
        print("   éves:", {L: fmt(result["annual"][s][L]) for L in LEVELS}, " TCO:", {L: fmt(result["tco"][s][L]) for L in LEVELS})
    print("A gyors -> C:", {L: fmt(p[L]) for L in LEVELS}, "quick:", {L: fmt(quick[L]) for L in LEVELS})
    print("base orders/yr", base_orders)
    for s in "ABC":
        print(s, {c: (r[s][c]["extra_orders_per_year"], fmt(r[s][c]["gain_3y"]), round(r[s][c]["roi_3y"] * 100), round(r[s][c]["cpl_old"]), round(r[s][c]["cpl_new"])) for c in ["kons", "alap", "opt"]}, "breakeven/hó:", round(r[s]["breakeven_orders_per_month"], 2))
    sens = {}
    for leads in (20, 40, 80):
        _, rr = roi(leads)
        sens[leads] = {s: round(rr[s]["alap"]["roi_3y"] * 100) for s in "ABC"}
    result["roi_sensitivity_alap"] = sens
    print("incremental TCO:", {s: fmt(r[s]["incremental_tco"]) for s in "ABC"})
    print("ads saving/yr alap:", {s: fmt(r[s]["alap"]["ads_saving_per_year_if_leads_constant"]) for s in "ABC"})
    print("sensitivity (leads/hó -> ROI% alap):", sens)
    json.dump(result, open("data/strategy-model.json", "w"), indent=1, ensure_ascii=False)
    print(result["matrix"])
    print(result["fixability_A"], result["fixability_count"])
