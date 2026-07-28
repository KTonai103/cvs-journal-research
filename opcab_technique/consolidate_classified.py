#!/usr/bin/env python3
"""Merge agent classifications with full metadata; group by subtopic; emit CSV + grouped JSON."""
import json, glob, os, csv, re
from collections import Counter, defaultdict
os.chdir(os.path.dirname(os.path.abspath(__file__)))

core = {(_norm := lambda d: (d or "").lower())(r.get("doi")) or f"pmid:{r.get('pmid')}": r
        for r in json.load(open("core_with_abstracts.json"))}

VALID_SUB = {'anaortic_total_arterial','exposure_stabilization','anastomosis_grafts','midcab_mics',
             'robotic_tecab','hybrid','shunt_flow_hemodynamics','special_population_redo',
             'conversion_safety','general_overview_review','training_simulation','other'}

cls = {}
problems = []
for fp in sorted(glob.glob("classified/batch_*.json")):
    try:
        txt = open(fp).read().strip()
        # tolerate markdown fences if any
        txt = re.sub(r'^```(json)?|```$', '', txt, flags=re.M).strip()
        arr = json.loads(txt)
        if not isinstance(arr, list):
            problems.append((fp, "not a list")); continue
        for o in arr:
            d = (o.get("doi") or "").lower()
            key = d or f"pmid:{o.get('pmid')}"
            cls[key] = o
    except Exception as e:
        problems.append((fp, f"{type(e).__name__}: {e}"))

print(f"classified files: {len(glob.glob('classified/batch_*.json'))}/16")
print(f"classifications loaded: {len(cls)}  | core records: {len(core)}")
if problems:
    print("!! PROBLEM FILES:")
    for p in problems: print("   ", p)

missing = [k for k in core if k not in cls]
if missing:
    print(f"!! {len(missing)} core records have NO classification (first 5): {missing[:5]}")

# merge
merged = []
for key, c in cls.items():
    base = core.get(key, {})
    m = dict(base)
    m.update({
        "en_title": c.get("en_title") or base.get("title"),
        "is_technique": bool(c.get("is_technique")),
        "subtopic": c.get("subtopic") if c.get("subtopic") in VALID_SUB else "other",
        "media": c.get("media", "standard"),
        "importance": c.get("importance", 0),
        "ja_summary": c.get("ja_summary", ""),
        "key_features": c.get("key_features", []),
    })
    merged.append(m)

tech = [m for m in merged if m["is_technique"]]
print(f"\nis_technique=TRUE: {len(tech)}  | FALSE: {len(merged)-len(tech)}")
print("\n-- technique papers by subtopic --")
for s, n in Counter(m["subtopic"] for m in tech).most_common():
    print(f"{n:4d}  {s}")
print("\n-- technique papers by media --")
for s, n in Counter(m["media"] for m in tech).most_common():
    print(f"{n:4d}  {s}")
print("\n-- importance distribution (technique) --")
for s, n in sorted(Counter(m["importance"] for m in tech).items(), reverse=True):
    print(f"  ★{s}: {n}")

# save grouped json (technique only)
grouped = defaultdict(list)
for m in tech:
    grouped[m["subtopic"]].append(m)
for s in grouped:
    grouped[s].sort(key=lambda m: (-(m.get("importance") or 0), -(m.get("year") or 0)))
json.dump(grouped, open("technique_grouped.json", "w"), ensure_ascii=False, indent=1)
json.dump(merged, open("all_classified.json", "w"), ensure_ascii=False, indent=1)

# CSV of all technique papers
with open("tables/opcab_technique_papers.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["subtopic","importance","media","year","journal","en_title","doi","pmid","open_access","key_features"])
    for m in sorted(tech, key=lambda m:(m["subtopic"], -(m.get("importance") or 0))):
        w.writerow([m["subtopic"], m.get("importance"), m.get("media"), m.get("year"),
                    m.get("journal"), m.get("en_title"), m.get("doi"), m.get("pmid"),
                    "yes" if m.get("isOpenAccess")=="Y" else "", "; ".join(m.get("key_features") or [])])
print("\nwrote technique_grouped.json, all_classified.json, tables/opcab_technique_papers.csv")
print(f"\n== HIGH-VALUE (importance>=4) per subtopic ==")
for s in sorted(grouped):
    hi = [m for m in grouped[s] if (m.get('importance') or 0)>=4]
    print(f"\n### {s}  ({len(hi)} high-value of {len(grouped[s])})")
    for m in hi[:12]:
        badge = {'video':'📹','figure_rich':'🖼️','standard':'·','unknown':'?'}.get(m.get('media'),'·')
        print(f"  ★{m.get('importance')} {badge} [{m.get('year')}] {m.get('journal','')[:28]:28s} | {(m.get('en_title') or '')[:70]}")
