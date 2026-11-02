"""3. lépés – képek letöltése ELEMZÉSRE (csak helyi munkakönyvtárba, nem a repóba),
metaadatok, duplikátumszűrés.

Futtatás: python3 scripts/image_analyze.py <helyi_kepkonyvtar>
  A <helyi_kepkonyvtar> a repón KÍVÜL legyen (a képek nem kerülnek gitbe / nyilvános tárhelyre).
Bemenet: data/images/refs.json, data/images/gallery.json
Kimenet: data/images/analysis.json
"""
import hashlib, io, json, os, re, sys, time
from urllib.parse import urlparse
import requests
from PIL import Image, ExifTags

OUT_DIR = sys.argv[1]
os.makedirs(OUT_DIR, exist_ok=True)
DELAY = 0.6
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36 (site-audit; read-only)'
s = requests.Session(); s.headers['User-Agent'] = UA

refs = json.load(open('data/images/refs.json'))['refs']
gal = json.load(open('data/images/gallery.json')) if os.path.exists('data/images/gallery.json') else {'large': {}}
urls = {}
for u, d in refs.items():
    urls[u] = d
for u, d in gal['large'].items():
    e = urls.setdefault(u, {'pages': [], 'contexts': [], 'alts': [], 'titles': []})
    e['pages'] = sorted(set(e['pages']) | {d['page']}); e['contexts'] = sorted(set(e['contexts']) | {'gallery-popup'})
    if d.get('title'): e['titles'] = sorted(set(e['titles']) | {d['title']})


def dhash(im, size=8):
    g = im.convert('L').resize((size + 1, size), Image.LANCZOS)
    px = list(g.getdata())
    bits = 0
    for r in range(size):
        for c in range(size):
            bits = (bits << 1) | (1 if px[r * (size + 1) + c] > px[r * (size + 1) + c + 1] else 0)
    return f'{bits:016x}'


def exif_info(im):
    out = {}
    try:
        ex = im.getexif()
        for k, v in ex.items():
            tag = ExifTags.TAGS.get(k, str(k))
            if tag in ('Artist', 'Copyright', 'Software', 'DateTime', 'Make', 'Model', 'ImageDescription', 'XPAuthor'):
                out[tag] = str(v)[:120]
    except Exception:
        pass
    try:
        xmp = im.info.get('xmp') or b''
        if isinstance(xmp, bytes):
            xmp = xmp.decode('utf-8', 'ignore')
        for tag in ('dc:rights', 'dc:creator', 'photoshop:Credit', 'xmpRights:WebStatement', 'Iptc4xmpCore:CreatorContactInfo'):
            m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', xmp, re.S)
            if m:
                out['XMP ' + tag] = re.sub(r'<[^>]+>', ' ', m.group(1)).strip()[:160]
    except Exception:
        pass
    return out


res = {}
for i, (u, meta) in enumerate(sorted(urls.items())):
    rec = {'url': u, **meta}
    host = urlparse(u).netloc
    rec['external'] = host not in ('www.budapest-temetkezes.hu', 'budapest-temetkezes.hu')
    if rec['external']:
        rec['status'] = 'külső – nem töltöttük le'
        res[u] = rec; continue
    time.sleep(DELAY)
    try:
        r = s.get(u, timeout=40)
    except requests.RequestException as e:
        rec['status'] = 'hiba: ' + str(e)[:80]; res[u] = rec; continue
    rec['http'] = r.status_code
    rec['content_type'] = r.headers.get('content-type')
    rec['last_modified'] = r.headers.get('last-modified')
    if r.status_code != 200:
        rec['status'] = f'HTTP {r.status_code}'; res[u] = rec; print(i, r.status_code, u, flush=True); continue
    data = r.content
    rec['bytes'] = len(data)
    rec['md5'] = hashlib.md5(data).hexdigest()
    ext = os.path.splitext(urlparse(u).path)[1].lower() or '.bin'
    fn = hashlib.sha1(u.encode()).hexdigest()[:16] + ext
    open(os.path.join(OUT_DIR, fn), 'wb').write(data)
    rec['local_file'] = fn
    if ext == '.svg' or 'svg' in (rec['content_type'] or ''):
        t = data.decode('utf-8', 'ignore')
        w = re.search(r'width="([\d.]+)', t); h = re.search(r'height="([\d.]+)', t)
        rec.update(format='SVG', width=float(w.group(1)) if w else None, height=float(h.group(1)) if h else None, status='ok')
    else:
        try:
            im = Image.open(io.BytesIO(data))
            rec['format'] = im.format
            rec['width'], rec['height'] = im.size
            rec['mode'] = im.mode
            rec['frames'] = getattr(im, 'n_frames', 1)
            rec['progressive'] = bool(im.info.get('progressive') or im.info.get('progression'))
            rec['exif'] = exif_info(im)
            im.seek(0)
            rec['dhash'] = dhash(im.convert('RGB') if im.mode in ('P', 'LA', 'RGBA', 'CMYK', 'I;16') else im)
            # JPEG minőségbecslés a kvantálási táblából
            if im.format == 'JPEG' and getattr(im, 'quantization', None):
                q0 = im.quantization.get(0)
                if q0:
                    rec['jpeg_q_avg'] = round(sum(q0) / len(q0), 1)
            rec['status'] = 'ok'
        except Exception as e:
            rec['status'] = 'nem értelmezhető: ' + str(e)[:80]
    res[u] = rec
    print(i, rec.get('status'), rec.get('width'), rec.get('height'), u, flush=True)

# --- duplikátumok ---
ok = [r for r in res.values() if r.get('status') == 'ok' and r.get('md5')]
by_md5 = {}
for r in ok:
    by_md5.setdefault(r['md5'], []).append(r['url'])
for r in ok:
    grp = by_md5[r['md5']]
    r['exact_dup_of'] = sorted(grp)[0] if len(grp) > 1 and sorted(grp)[0] != r['url'] else None


def ham(a, b):
    return bin(int(a, 16) ^ int(b, 16)).count('1')


# közel-duplikátum: azonos tartalom eltérő méretben / tömörítéssel (dHash távolság <= 6)
masters = []
for r in sorted([r for r in ok if r.get('dhash') and not r.get('exact_dup_of')], key=lambda r: -(r.get('width', 0) * r.get('height', 0))):
    hit = None
    for m in masters:
        if ham(r['dhash'], m['dhash']) <= 6 and abs((r['width'] / max(r['height'], 1)) - (m['width'] / max(m['height'], 1))) < 0.08:
            hit = m; break
    if hit and hit['url'] != r['url']:
        r['near_dup_of'] = hit['url']
    else:
        r['near_dup_of'] = None
        masters.append(r)
json.dump(res, open('data/images/analysis.json', 'w'), ensure_ascii=False, indent=1)
print('DONE', len(res), 'ok', len(ok), 'unique md5', len(by_md5), 'masters', len(masters))
