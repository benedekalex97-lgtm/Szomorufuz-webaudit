"""4. lépés – duplikátumszűrés (szigorított) és egyedi azonosítók kiosztása.

Szabályok:
  - Pontos duplikátum: azonos MD5.
  - Méretváltozat: azonos fájlazonosító (pl. 279349_pic_100x100.jpg <-> 279349_pic_600x500.jpg,
    1353162436_200x.jpg <-> 1353162436.jpg) és vizuálisan egyező (dHash-távolság <= 10).
  - Közel-duplikátum eltérő azonosítóval: dHash-távolság <= 2, mindkét kép >= 150 px, azonos képarány (±5%).
  - Mesterpéldány: a csoport legnagyobb felbontású tagja.
Bemenet: data/images/analysis.json · Kimenet: data/images/dedup.json
"""
import json, re
A = json.load(open('data/images/analysis.json'))
ok = {u: r for u, r in A.items() if r.get('status') == 'ok'}


def fid(u):
    f = u.rsplit('/', 1)[1].split('?')[0]
    f = re.sub(r'\.(jpe?g|png|gif|webp|svg)$', '', f, flags=re.I)
    f = re.sub(r'_(pic_)?\d+x\d*$', '', f)
    f = re.sub(r'_pic$', '', f)
    folder = u.rsplit('/', 1)[0]
    return folder.replace('/pics', '') + '/' + f


def ham(a, b):
    return bin(int(a, 16) ^ int(b, 16)).count('1')


area = lambda r: (r.get('width') or 0) * (r.get('height') or 0)
parent = {u: u for u in ok}


def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]; u = parent[u]
    return u


def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        # a nagyobb felbontású legyen a gyökér
        if area(ok[ra]) >= area(ok[rb]): parent[rb] = ra
        else: parent[ra] = rb


reason = {}
by_md5, by_fid = {}, {}
for u, r in ok.items():
    by_md5.setdefault(r['md5'], []).append(u)
    by_fid.setdefault(fid(u), []).append(u)
for g in by_md5.values():
    for u in g[1:]:
        union(g[0], u); reason[u] = 'pontos duplikátum (MD5)'
for g in by_fid.values():
    for u in g[1:]:
        a, b = ok[g[0]], ok[u]
        if a.get('dhash') and b.get('dhash') and ham(a['dhash'], b['dhash']) <= 10:
            union(g[0], u); reason.setdefault(u, 'méretváltozat (azonos fájlazonosító)')
big = [u for u, r in ok.items() if r.get('dhash') and min(r.get('width') or 0, r.get('height') or 0) >= 150]
for i, u in enumerate(big):
    for v in big[i + 1:]:
        if find(u) == find(v):
            continue
        a, b = ok[u], ok[v]
        ra, rb = a['width'] / a['height'], b['width'] / b['height']
        if ham(a['dhash'], b['dhash']) <= 2 and abs(ra - rb) / ra < 0.05:
            union(u, v); reason.setdefault(v, 'közel-duplikátum (dHash ≤ 2)')

groups = {}
for u in ok:
    groups.setdefault(find(u), []).append(u)
masters = sorted(groups, key=lambda m: (m.split('/contents/')[0], m))
out = {'masters': {}, 'members': {}}
for i, m in enumerate(masters, 1):
    iid = f'IMG-{i:03d}'
    mem = sorted(groups[m])
    out['masters'][m] = {'id': iid, 'members': mem}
    for u in mem:
        if u == m:
            why = None
        elif ok[u]['md5'] == ok[m]['md5']:
            why = 'pontos duplikátum (MD5)'
        elif fid(u) == fid(m):
            why = 'méretváltozat (azonos fájlazonosító)'
        else:
            why = reason.get(u, 'közel-duplikátum (dHash)')
        out['members'][u] = {'id': iid, 'is_master': u == m, 'dup_reason': why}
json.dump(out, open('data/images/dedup.json', 'w'), ensure_ascii=False, indent=1)
print('ok files', len(ok), 'unique images (masters)', len(masters),
      'duplicates', len(ok) - len(masters))
from collections import Counter
print(Counter(v['dup_reason'] for v in out['members'].values()))
