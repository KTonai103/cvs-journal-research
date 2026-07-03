#!/usr/bin/env python3
"""Harvest Cor-Knot literature from PubMed E-utilities (foreground, network OK)."""
import json, time, urllib.parse, urllib.request, sys, re, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")

QUERIES = [
    '"Cor-Knot"',
    '"Cor Knot"',
    'CorKnot',
    '"automated titanium fastener"',
    '"automated fastener" AND (valve OR annuloplasty OR cardiac)',
    '"titanium fastener" AND (mitral OR aortic OR tricuspid OR valve)',
    '"automated knot" AND cardiac surgery',
    '"fastener" AND annuloplasty',
    '"Cor-Knot" AND (complication OR perforation OR hemolysis OR embolization OR leaflet OR dehiscence OR endocarditis)',
]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "cvs-research/1.0 (ktonai.cs@gmail.com)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")

def esearch(term):
    q = urllib.parse.quote(term)
    url = f"{BASE}/esearch.fcgi?db=pubmed&term={q}&retmax=200&retmode=json"
    data = json.loads(get(url))
    return data["esearchresult"].get("idlist", [])

pmids = []
seen = set()
for term in QUERIES:
    try:
        ids = esearch(term)
        new = [i for i in ids if i not in seen]
        for i in new:
            seen.add(i)
        pmids.extend(new)
        print(f"[{len(ids):>3}] {term}  (+{len(new)} new)", file=sys.stderr)
    except Exception as e:
        print(f"ERR {term}: {e}", file=sys.stderr)
    time.sleep(0.4)

print(f"TOTAL unique PMIDs: {len(pmids)}", file=sys.stderr)

# efetch abstracts in batches
records = []
for i in range(0, len(pmids), 100):
    batch = pmids[i:i+100]
    ids = ",".join(batch)
    url = f"{BASE}/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"
    try:
        xml = get(url)
    except Exception as e:
        print(f"efetch err: {e}", file=sys.stderr)
        continue
    # crude split per PubmedArticle
    arts = re.findall(r"<PubmedArticle>.*?</PubmedArticle>", xml, re.DOTALL)
    for a in arts:
        def tag(name):
            m = re.search(rf"<{name}[^>]*>(.*?)</{name}>", a, re.DOTALL)
            return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
        pmid = tag("PMID")
        title = tag("ArticleTitle")
        journal = tag("Title")
        year_m = re.search(r"<PubDate>.*?<Year>(\d{4})</Year>", a, re.DOTALL)
        year = year_m.group(1) if year_m else ""
        # abstract may have multiple AbstractText
        abst_parts = re.findall(r"<AbstractText[^>]*>(.*?)</AbstractText>", a, re.DOTALL)
        label_parts = re.findall(r'<AbstractText Label="([^"]*)"[^>]*>(.*?)</AbstractText>', a, re.DOTALL)
        if label_parts:
            abstract = "\n".join(f"{l}: {re.sub(r'<[^>]+>','',t).strip()}" for l,t in label_parts)
        else:
            abstract = " ".join(re.sub(r"<[^>]+>", "", p).strip() for p in abst_parts)
        doi_m = re.search(r'<ArticleId IdType="doi">(.*?)</ArticleId>', a)
        doi = doi_m.group(1).strip() if doi_m else ""
        pubtype = ", ".join(re.findall(r"<PublicationType[^>]*>(.*?)</PublicationType>", a))
        records.append({
            "pmid": pmid, "year": year, "journal": journal, "title": title,
            "doi": doi, "pubtype": pubtype, "abstract": abstract,
        })
    time.sleep(0.4)

records.sort(key=lambda r: (r["year"] or "0"), reverse=True)
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "corknot_pubmed.json"), "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

# also a readable text digest
with open(os.path.join(OUT, "corknot_pubmed.txt"), "w", encoding="utf-8") as f:
    for r in records:
        f.write(f"### PMID {r['pmid']} ({r['year']}) — {r['journal']}\n")
        f.write(f"TITLE: {r['title']}\n")
        f.write(f"DOI: {r['doi']}  | TYPE: {r['pubtype']}\n")
        f.write(f"ABSTRACT: {r['abstract'] or '(no abstract)'}\n\n")

print(f"WROTE {len(records)} records to {OUT}", file=sys.stderr)
