#!/usr/bin/env python3
"""Verify selected PMIDs: full title, journal, year, DOI, PMC(OA) status, dup check."""
import json, subprocess, urllib.parse, os, sys

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
HERE = os.path.dirname(os.path.abspath(__file__))


def curl(url):
    return subprocess.run(["curl", "-sL", "--max-time", "60", url],
                          capture_output=True, text=True).stdout


pmids = [l.strip() for l in open(os.path.join(HERE, "selected.txt")) if l.strip()]
have = set(l.strip() for l in open(os.path.join(HERE, "raw/have_pmids.txt")) if l.strip())

res = {}
for i in range(0, len(pmids), 30):
    chunk = pmids[i:i + 30]
    q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(chunk), "retmode": "json"})
    res.update(json.loads(curl(f"{BASE}/esummary.fcgi?{q}") or "{}").get("result", {}))

out = []
missing = []
for p in pmids:
    it = res.get(p)
    if not it or "error" in it:
        missing.append(p)
        continue
    ids = {a.get("idtype"): a.get("value") for a in it.get("articleids", [])}
    out.append({
        "pmid": p,
        "title": it.get("title", "").rstrip("."),
        "journal": it.get("source", ""),
        "year": (it.get("pubdate") or "")[:4],
        "vol_pages": f"{it.get('volume','')}({it.get('issue','')}):{it.get('pages','')}",
        "doi": ids.get("doi", ""),
        "pmc": ids.get("pmc", ""),
        "type": ";".join(it.get("pubtype", [])),
        "first_author": (it.get("authors") or [{}])[0].get("name", ""),
        "already_have": p in have,
    })

json.dump(out, open(os.path.join(HERE, "raw/selected_verified.json"), "w"),
          ensure_ascii=False, indent=1)

print(f"verified {len(out)}/{len(pmids)}  missing={missing}")
for r in out:
    flag = "DUP" if r["already_have"] else "   "
    pmc = r["pmc"] or "-"
    print(f"{flag} {r['pmid']}\t{r['year']}\t{pmc:<12}\t{r['journal'][:26]:<26}\t{r['title'][:95]}")
