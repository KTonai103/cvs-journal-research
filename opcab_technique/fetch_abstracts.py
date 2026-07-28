#!/usr/bin/env python3
"""Fetch abstracts + verify titles via Europe PMC (by DOI, fallback PMID)."""
import json, os, urllib.parse, urllib.request, concurrent.futures as cf, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

core = json.load(open("core_candidates.json"))
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

def fetch(rec):
    doi = rec.get("doi"); pmid = rec.get("pmid")
    q = f'DOI:"{doi}"' if doi else (f'EXT_ID:{pmid} AND SRC:MED' if pmid else None)
    out = {"doi": doi, "pmid": pmid}
    if not q:
        out["epmc_status"] = "no-id"; return out
    url = f"{EPMC}?query={urllib.parse.quote(q)}&resultType=core&format=json&pageSize=1"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "OPCAB-research/1.0 (mailto:ktonai.cs@gmail.com)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            res = (data.get("resultList") or {}).get("result") or []
            if not res:
                out["epmc_status"] = "not-found"; return out
            it = res[0]
            out.update({
                "epmc_title": it.get("title", "").rstrip("."),
                "abstract": it.get("abstractText", ""),
                "epmc_pmid": it.get("pmid"),
                "epmc_year": it.get("pubYear"),
                "epmc_journal": (it.get("journalInfo") or {}).get("journal", {}).get("title") or it.get("journalTitle"),
                "pubtypes": [p for p in (it.get("pubTypeList") or {}).get("pubType", [])],
                "authorString": it.get("authorString", ""),
                "isOpenAccess": it.get("isOpenAccess"),
                "epmc_status": "ok",
            })
            return out
        except Exception as e:
            if attempt == 2:
                out["epmc_status"] = f"err:{type(e).__name__}"; return out
            time.sleep(1.0)
    return out

results = {}
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    futs = {ex.submit(fetch, r): i for i, r in enumerate(core)}
    done = 0
    for fut in cf.as_completed(futs):
        i = futs[fut]; res = fut.result()
        results[i] = res
        done += 1
        if done % 50 == 0:
            print(f"  fetched {done}/{len(core)}")

# merge
merged = []
for i, r in enumerate(core):
    m = dict(r); m.update({k: v for k, v in results[i].items() if k not in ("doi", "pmid")})
    if not m.get("pmid") and m.get("epmc_pmid"):
        m["pmid"] = m["epmc_pmid"]
    merged.append(m)

json.dump(merged, open("core_with_abstracts.json", "w"), ensure_ascii=False, indent=1)

from collections import Counter
st = Counter(m.get("epmc_status") for m in merged)
print("status:", dict(st))
print("with abstract:", sum(1 for m in merged if m.get("abstract")))
# title-match verification flag
mism = []
for m in merged:
    if m.get("epmc_title") and m.get("title"):
        a = "".join(c.lower() for c in m["title"] if c.isalnum())[:50]
        b = "".join(c.lower() for c in m["epmc_title"] if c.isalnum())[:50]
        if a and b and a != b and a not in b and b not in a:
            mism.append((m.get("doi"), m["title"][:60], m["epmc_title"][:60]))
print("possible title mismatches:", len(mism))
for x in mism[:15]:
    print("  ", x)
