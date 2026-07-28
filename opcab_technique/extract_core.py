#!/usr/bin/env python3
"""Extract the core technique/multimedia candidate set from candidates.json."""
import json, re, os
from collections import Counter
os.chdir(os.path.dirname(os.path.abspath(__file__)))

cands = json.load(open("candidates.json"))

CORE_JOURNAL = re.compile(r"""(
    jtcvs\s+techniques | multimedia\s+manual | mmcts |
    operative\s+techniques\s+in\s+thoracic | annals\s+of\s+cardiothoracic\s+surgery |
    \binnovations\b
)""", re.I | re.X)

# technique / figure / video signal in TITLE (for any journal)
TECH_RX = re.compile(r"""(
    how\s+i\s+do\s+it | how\s+to\s+do\s+it | how\s+we\s+do | operative\s+technique |
    surgical\s+technique | technique\s+of | technique\s+for | technical\s+(note|aspect|tip|consideration|modification) |
    tips?\s+and\s+tricks | step[\s\-]by[\s\-]step | \bvideo\b | tutorial | illustrat | \batlas\b |
    maneuver | manoeuvre | demonstrat | our\s+approach | our\s+technique | a\s+novel\s+technique |
    new\s+technique | modified\s+technique | simplified | \"how\b | teaching | masterclass
)""", re.I | re.X)

core = []
for r in cands:
    j = r.get("journal") or ""
    t = r.get("title") or ""
    is_core_j = bool(CORE_JOURNAL.search(j))
    is_tech_t = bool(TECH_RX.search(t))
    if is_core_j or is_tech_t:
        r = dict(r)
        r["core_journal"] = is_core_j
        r["tech_title"] = is_tech_t
        core.append(r)

core.sort(key=lambda r: (not r["core_journal"], r.get("journal") or "", -(r.get("year") or 0)))
json.dump(core, open("core_candidates.json", "w"), ensure_ascii=False, indent=1)

print(f"core set: {len(core)}  (of {len(cands)} anchored)")
print(f"  core-journal items: {sum(1 for r in core if r['core_journal'])}")
print(f"  technique-title items (any journal): {sum(1 for r in core if r['tech_title'])}")
print(f"  lacking PMID: {sum(1 for r in core if not r.get('pmid'))}")
print(f"  lacking DOI : {sum(1 for r in core if not r.get('doi'))}")
print("\n-- core by journal --")
for j, c in Counter((r.get('journal') or 'NA') for r in core).most_common(20):
    print(f"{c:4d}  {j}")
