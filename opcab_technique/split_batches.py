#!/usr/bin/env python3
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
core = json.load(open("core_with_abstracts.json"))

# trim to fields needed for classification
def trim(r):
    ab = (r.get("abstract") or "")[:1600]
    return {
        "doi": r.get("doi"), "pmid": r.get("pmid"),
        "title": r.get("title"), "journal": r.get("journal"),
        "year": r.get("year") or r.get("epmc_year"),
        "pubtypes": r.get("pubtypes") or [], "oa": r.get("isOpenAccess"),
        "core_journal": r.get("core_journal"), "tech_title": r.get("tech_title"),
        "abstract": ab,
    }

recs = [trim(r) for r in core]
os.makedirs("batches", exist_ok=True)
B = 24
n = 0
for i in range(0, len(recs), B):
    batch = recs[i:i+B]
    fn = f"batches/batch_{n:02d}.json"
    json.dump(batch, open(fn, "w"), ensure_ascii=False, indent=1)
    n += 1
print(f"wrote {n} batches of up to {B} ({len(recs)} papers)")
