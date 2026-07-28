#!/usr/bin/env python3
"""Consolidate CrossRef + PubMed harvest into a deduped, relevance-filtered candidate set."""
import json, glob, re, os, html

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Off-pump-anchored relevance: title must hint at off-pump / beating-heart / MIDCAB / TECAB / anaortic family.
ANCHOR = re.compile(r"""(
    off[\s\-]?pump | \bOPCAB\b | beating[\s\-]?heart |
    an[\s\-]?aortic | no[\s\-]?touch\s+aorta | clampless | aortic\s+no[\s\-]?touch |
    \bMIDCAB\b | minimally\s+invasive\s+(direct\s+)?coronary | minimally\s+invasive\s+cardiac\s+surg.*coronary |
    \bTECAB\b | totally\s+endoscopic\s+coronary | robotic.*coronary\s+(artery\s+)?bypass | endoscopic\s+coronary\s+(artery\s+)?bypass |
    hybrid\s+coronary\s+revasculariz | left\s+anterior\s+small\s+thoracotomy
)""", re.I | re.X)
# broaden: also catch "coronary bypass" technique items if they also say off-pump-ish words handled by ANCHOR.

def norm_doi(d):
    return d.strip().lower() if d else None

records = {}  # key -> record

def add(key, rec):
    if not key:
        return
    if key in records:
        # merge: prefer record with more fields; keep pmid+doi crosslink
        old = records[key]
        for k, v in rec.items():
            if v and not old.get(k):
                old[k] = v
        old["src"] = sorted(set(old.get("src", []) + rec.get("src", [])))
    else:
        records[key] = rec

# ---- CrossRef ----
for fp in glob.glob("raw/cr_*.json"):
    qtag = os.path.basename(fp)[3:-5]
    try:
        items = json.load(open(fp)).get("message", {}).get("items", [])
    except Exception:
        continue
    for it in items:
        doi = norm_doi(it.get("DOI"))
        if not doi:
            continue
        title = (it.get("title") or [""])[0]
        title = html.unescape(re.sub("<[^>]+>", "", title)).strip()
        journal = (it.get("container-title") or [""])[0]
        yr = None
        for dk in ("published", "published-print", "published-online", "issued"):
            dp = (it.get(dk) or {}).get("date-parts")
            if dp and dp[0] and dp[0][0]:
                yr = dp[0][0]; break
        au = it.get("author") or []
        first = (au[0].get("family") if au and au[0].get("family") else "")
        add(doi, {
            "doi": doi, "pmid": None, "title": title, "journal": journal,
            "year": yr, "type": it.get("type"), "first_author": first,
            "volume": it.get("volume"), "issue": it.get("issue"), "page": it.get("page"),
            "src": [f"cr:{qtag}"],
        })

# ---- PubMed esummary ----
for fp in glob.glob("raw/pm_*.json"):
    qtag = os.path.basename(fp)[3:-5]
    try:
        res = json.load(open(fp)).get("result", {})
    except Exception:
        continue
    for uid in res.get("uids", []):
        it = res.get(uid, {})
        title = html.unescape(re.sub("<[^>]+>", "", it.get("title", ""))).strip()
        journal = it.get("fulljournalname") or it.get("source", "")
        pubdate = it.get("pubdate", "")
        m = re.search(r"\b(19|20)\d{2}\b", pubdate)
        yr = int(m.group()) if m else None
        doi = None
        for aid in it.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = norm_doi(aid.get("value"))
        au = it.get("authors") or []
        first = au[0]["name"].split()[0] if au else ""
        key = doi or f"pmid:{uid}"
        add(key, {
            "doi": doi, "pmid": uid, "title": title, "journal": journal,
            "year": yr, "type": ",".join(it.get("pubtype", [])), "first_author": first,
            "volume": it.get("volume"), "issue": it.get("issue"), "page": it.get("pages"),
            "src": [f"pm:{qtag}"],
        })

# ---- relevance filter ----
kept = [r for r in records.values() if r.get("title") and ANCHOR.search(r["title"])]

# sort by journal then year desc
kept.sort(key=lambda r: (r.get("journal") or "", -(r.get("year") or 0)))

json.dump(kept, open("candidates.json", "w"), ensure_ascii=False, indent=1)

# stats
from collections import Counter
print(f"total unique harvested: {len(records)}")
print(f"kept (off-pump anchored): {len(kept)}")
print("\n-- by journal (kept) --")
for j, c in Counter((r.get('journal') or 'NA') for r in kept).most_common():
    print(f"{c:4d}  {j}")
print("\n-- with PMID:", sum(1 for r in kept if r.get('pmid')),
      "| with DOI:", sum(1 for r in kept if r.get('doi')))
