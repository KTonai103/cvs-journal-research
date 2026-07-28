#!/usr/bin/env python3
"""PubMed E-utilities search for CABG technique papers (curl-based)."""
import json, subprocess, sys, time, urllib.parse, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")


def curl(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "60", url],
                       capture_output=True, text=True)
    return r.stdout


def esearch(term, retmax=40, sort="relevance"):
    q = urllib.parse.urlencode({
        "db": "pubmed", "term": term, "retmax": retmax,
        "retmode": "json", "sort": sort,
    })
    d = json.loads(curl(f"{BASE}/esearch.fcgi?{q}") or "{}")
    return d.get("esearchresult", {}).get("idlist", [])


def esummary(pmids):
    if not pmids:
        return {}
    q = urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids), "retmode": "json",
    })
    d = json.loads(curl(f"{BASE}/esummary.fcgi?{q}") or "{}")
    return d.get("result", {})


QUERIES = json.load(open(sys.argv[1]))

allrec = {}
for key, term in QUERIES.items():
    ids = esearch(term)
    res = esummary(ids)
    rows = []
    for pid in ids:
        it = res.get(pid)
        if not it:
            continue
        rec = {
            "pmid": pid,
            "title": it.get("title", "").rstrip("."),
            "journal": it.get("source", ""),
            "year": (it.get("pubdate", "") or "")[:4],
            "type": ";".join(it.get("pubtype", [])),
            "doi": next((a["value"] for a in it.get("articleids", [])
                         if a.get("idtype") == "doi"), ""),
            "authors": ", ".join(a["name"] for a in it.get("authors", [])[:2]),
        }
        rows.append(rec)
        allrec.setdefault(pid, rec).setdefault("queries", []).append(key)
        if key not in allrec[pid]["queries"]:
            allrec[pid]["queries"].append(key)
    print(f"### {key}  ({len(rows)})", flush=True)
    for r in rows:
        print(f"{r['pmid']}\t{r['year']}\t{r['journal'][:28]}\t{r['title'][:120]}")
    print(flush=True)
    time.sleep(0.4)

os.makedirs(OUT, exist_ok=True)
tag = sys.argv[2] if len(sys.argv) > 2 else "search"
with open(os.path.join(OUT, f"{tag}.json"), "w") as f:
    json.dump(allrec, f, ensure_ascii=False, indent=1)
print(f"\n[saved] {len(allrec)} unique -> raw/{tag}.json")
