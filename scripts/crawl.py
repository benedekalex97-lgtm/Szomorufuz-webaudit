"""Udvarias, csak olvasó crawler a budapest-temetkezes.hu publikus oldalaihoz.

- Csak GET kérések, kérésenként késleltetéssel (alapértelmezés: 1.2 s).
- Tiszteletben tartja a robots.txt Disallow szabályait (/admin/).
- Űrlapot nem küld el, nem jelentkezik be.
Kimenet: data/crawl.json
"""
import json, re, sys, time
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from bs4 import BeautifulSoup

BASE = "https://www.budapest-temetkezes.hu/"
HOST = "www.budapest-temetkezes.hu"
DELAY = float(sys.argv[2]) if len(sys.argv) > 2 else 1.2
OUT = sys.argv[1] if len(sys.argv) > 1 else "data/crawl.json"
MAX_PAGES = 400
SAMPLE_QS = [BASE + "?mobile=no", BASE + "?mobile=1"]
qs_seen = set()
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36 (site-audit; read-only)"
SKIP_EXT = re.compile(r"\.(jpg|jpeg|png|gif|webp|svg|pdf|docx?|xlsx?|zip|mp4|mp3|css|js|ico)(\?|$)", re.I)

s = requests.Session()
s.headers["User-Agent"] = UA


def norm(u):
    u, _ = urldefrag(u)
    p = urlparse(u)
    if p.scheme not in ("http", "https"):
        return None
    host = p.netloc.lower()
    if host in ("budapest-temetkezes.hu", HOST):
        return u
    return None


def get(url, tries=3):
    for i in range(tries):
        try:
            return s.get(url, timeout=30, allow_redirects=True)
        except requests.RequestException as e:
            err = str(e)
            time.sleep(4 * (i + 1))
    return err


def parse(url, r):
    soup = BeautifulSoup(r.text, "lxml")
    d = {}
    d["title"] = soup.title.get_text(strip=True) if soup.title else None
    md = soup.find("meta", attrs={"name": "description"})
    d["meta_description"] = md.get("content") if md else None
    mr = soup.find("meta", attrs={"name": "robots"})
    d["meta_robots"] = mr.get("content") if mr else None
    mv = soup.find("meta", attrs={"name": "viewport"})
    d["viewport"] = mv.get("content") if mv else None
    can = soup.find("link", rel="canonical")
    d["canonical"] = can.get("href") if can else None
    d["og"] = {m.get("property"): m.get("content") for m in soup.find_all("meta", attrs={"property": re.compile("^og:")})}
    d["html_lang"] = soup.html.get("lang") if soup.html else None
    d["doctype_xhtml"] = "XHTML 1.0" in r.text[:600]
    d["h1"] = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]
    d["h2"] = [h.get_text(" ", strip=True) for h in soup.find_all("h2")][:20]
    d["h3_count"] = len(soup.find_all("h3"))
    d["jsonld"] = [x.get_text() for x in soup.find_all("script", type="application/ld+json")]
    imgs = soup.find_all("img")
    d["img_count"] = len(imgs)
    d["img_no_alt"] = [i.get("src") for i in imgs if i.get("alt") is None]
    d["img_empty_alt"] = [i.get("src") for i in imgs if i.get("alt") == ""]
    d["img_http"] = [i.get("src") for i in imgs if (i.get("src") or "").startswith("http://")]
    center = soup.find(id="center") or soup.body
    txt = center.get_text(" ", strip=True) if center else ""
    d["word_count_center"] = len(txt.split())
    links, tel, mail, ext = [], [], [], []
    for a in soup.find_all("a", href=True):
        h = a["href"].strip()
        if h.startswith("tel:"):
            tel.append(h)
        elif h.startswith("mailto:"):
            mail.append(h)
        elif h.startswith("javascript") or h.startswith("#"):
            continue
        else:
            full = urljoin(url, h)
            n = norm(full)
            if n:
                links.append(n)
            elif urlparse(full).scheme in ("http", "https"):
                ext.append(full)
    d["internal_links"] = sorted(set(links))
    d["external_links"] = sorted(set(ext))
    d["tel_links"] = sorted(set(tel))
    d["mailto_links"] = sorted(set(mail))
    d["http_links"] = sorted({l for l in links + ext if l.startswith("http://")})
    forms = []
    for f in soup.find_all("form"):
        forms.append({
            "id": f.get("id"), "action": f.get("action"), "method": f.get("method"),
            "fields": [(i.name, i.get("type"), i.get("name"), bool(i.get("id") and soup.find("label", attrs={"for": i.get("id")}))) for i in f.find_all(["input", "select", "textarea"]) if i.get("type") != "hidden"],
        })
    d["forms"] = forms
    d["iframes"] = [i.get("src") for i in soup.find_all("iframe")]
    d["scripts_ext"] = [x.get("src") for x in soup.find_all("script", src=True)]
    d["inline_styles"] = len(soup.find_all(style=True))
    d["tables"] = len(soup.find_all("table"))
    d["font_tags"] = len(soup.find_all("font"))
    d["target_blank_no_rel"] = len([a for a in soup.find_all("a", target="_blank") if not a.get("rel")])
    return d


def main():
    queue, seen, results = [BASE] + SAMPLE_QS, set(), {}
    try:
        sm = s.get(BASE + "pages/avszomfuzbud/sitemap.xml", timeout=30).text
        sitemap_urls = re.findall(r"<loc>(.*?)</loc>", sm)
    except Exception:
        sitemap_urls = []
    queue += sitemap_urls
    while queue and len(results) < MAX_PAGES:
        u = queue.pop(0)
        if u in seen or "/admin/" in u or SKIP_EXT.search(u):
            continue
        if "?" in u and u not in SAMPLE_QS:
            # query-stringes duplikátumok (pl. ?mobile=no): csak rögzítjük
            qs_seen.add(u)
            continue
        seen.add(u)
        time.sleep(DELAY)
        r = get(u)
        rec = {"url": u, "in_sitemap": u in sitemap_urls}
        if isinstance(r, str):
            rec["error"] = r
            results[u] = rec
            print("ERR", u, r[:80], flush=True)
            continue
        rec["status"] = r.status_code
        rec["final_url"] = r.url
        rec["redirects"] = [(h.status_code, h.headers.get("location")) for h in r.history]
        rec["elapsed_ms"] = int(r.elapsed.total_seconds() * 1000)
        rec["bytes"] = len(r.content)
        rec["content_type"] = r.headers.get("content-type")
        rec["x_robots"] = r.headers.get("x-robots-tag")
        print(r.status_code, len(results), u, flush=True)
        if r.status_code == 200 and "html" in (r.headers.get("content-type") or ""):
            rec.update(parse(r.url, r))
            for l in rec["internal_links"]:
                if l not in seen and not SKIP_EXT.search(l):
                    queue.append(l)
        results[u] = rec
    json.dump({"sitemap_urls": sitemap_urls, "query_variants_not_fetched": sorted(qs_seen), "pages": results}, open(OUT, "w"), ensure_ascii=False, indent=1)
    print("DONE", len(results))


main()
