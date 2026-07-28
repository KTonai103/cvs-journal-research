#!/usr/bin/env python3
"""Harvest hemostatic agent / surgical sealant literature from PubMed E-utilities."""
import json, time, urllib.parse, urllib.request, sys, re, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")

QUERIES = [
    # --- product-specific: sealants (polymer / glue) ---
    '"Hydrofit"',
    '"hydrophilic polymer sealant" AND (aorta OR aortic OR cardiac)',
    '"urethane prepolymer" AND (aortic OR vascular OR hemostasis)',
    '"BioGlue"',
    '"BioGlue" AND (complication OR pseudoaneurysm OR necrosis OR stenosis OR embolism)',
    '"glutaraldehyde" AND "albumin" AND (aortic OR aorta) AND (glue OR sealant OR adhesive)',
    '"gelatin-resorcinol-formaldehyde" OR "GRF glue"',
    '"GRF glue" AND (redissection OR pseudoaneurysm OR complication OR late)',
    '"CoSeal"', '"Progel"', '"Duraseal"', '"Adherus"',
    '"cyanoacrylate" AND (cardiac surgery OR aortic OR vascular anastomosis)',
    '"Glubran"',
    # --- product-specific: fibrin sealants ---
    '"fibrin sealant" AND (cardiac surgery OR cardiothoracic OR aortic OR sternotomy)',
    '"Bolheal"', '"Beriplast"', '"Tisseel"', '"Tissucol"', '"Evicel"', '"Artiss"',
    '"TachoSil"', '"TachoComb"', '"fibrin sealant patch" AND (cardiac OR aortic)',
    '"Vivostat"',
    # --- product-specific: flowable gelatin-thrombin ---
    '"FloSeal"', '"Surgiflo"',
    '"gelatin-thrombin matrix"',
    '"FloSeal" AND (complication OR granuloma OR embolism OR infection OR foreign body)',
    # --- topical hemostats: oxidized cellulose, collagen, polysaccharide ---
    '"Surgicel" OR "oxidized regenerated cellulose"',
    '"oxidized regenerated cellulose" AND (granuloma OR foreign body OR mimicking OR abscess OR complication)',
    '"Arista" AND hemostat', '"PerClot"', '"microporous polysaccharide hemospheres"',
    '"HemoPatch"', '"Veriset"', '"Tachotop"', '"EndoClot"',
    '"microfibrillar collagen" AND (cardiac OR hemostasis)',
    '"gelatin sponge" AND (cardiac surgery OR neurosurgery) AND (complication OR granuloma)',
    '"polyglycolic acid" AND (felt OR sheet) AND (aortic OR cardiac)',
    '"Neoveil"',
    # --- generic: topical hemostats in cardiac surgery ---
    '"topical hemostatic agent" AND cardiac surgery',
    '"topical hemostat" AND (cardiac OR cardiovascular OR aortic)',
    '"surgical sealant" AND (aortic OR cardiac OR anastomosis)',
    '"hemostatic agent" AND "cardiac surgery" AND (randomized OR trial OR comparative)',
    'sealant AND aortic AND (anastomosis OR suture line) AND hemostasis',
    'hemostatic AND "cardiac surgery" AND (cost OR cost-effectiveness OR economic)',
    # --- adverse events / complications (cross-cutting) ---
    'pseudoaneurysm AND (glue OR sealant OR adhesive) AND (aorta OR aortic)',
    '"anastomotic pseudoaneurysm" AND (BioGlue OR sealant OR glue)',
    '(sealant OR "hemostatic agent" OR glue) AND (mediastinitis OR "graft infection" OR "prosthetic infection")',
    '(hemostatic OR sealant) AND "foreign body reaction" AND (cardiac OR aortic OR thoracic)',
    '"aortic wall necrosis" AND (glue OR adhesive OR sealant)',
    'thrombin AND (bovine OR "topical") AND (antibody OR coagulopathy OR anaphylaxis)',
    '"hemostatic agent" AND (embolization OR embolism) AND (surgery OR vascular)',
    '(sealant OR hemostat) AND "coronary" AND (compression OR occlusion OR graft)',
    # --- guidelines / systematic reviews ---
    '"topical hemostatic" AND (guideline OR consensus OR "systematic review" OR meta-analysis)',
    'bleeding AND "cardiac surgery" AND (STS OR EACTS) AND guideline AND (blood conservation OR hemostasis)',
]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "cvs-research/1.0 (ktonai.cs@gmail.com)"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")

def esearch(term):
    q = urllib.parse.quote(term)
    url = f"{BASE}/esearch.fcgi?db=pubmed&term={q}&retmax=150&retmode=json"
    data = json.loads(get(url))
    return data["esearchresult"].get("idlist", [])

pmids, seen, hits = [], set(), {}
for term in QUERIES:
    try:
        ids = esearch(term)
        new = [i for i in ids if i not in seen]
        for i in new:
            seen.add(i)
        pmids.extend(new)
        hits[term] = len(ids)
        print(f"[{len(ids):>3}] {term}  (+{len(new)} new)", file=sys.stderr)
    except Exception as e:
        print(f"ERR {term}: {e}", file=sys.stderr)
    time.sleep(0.35)

print(f"TOTAL unique PMIDs: {len(pmids)}", file=sys.stderr)

records = []
for i in range(0, len(pmids), 100):
    batch = pmids[i:i+100]
    url = f"{BASE}/efetch.fcgi?db=pubmed&id={','.join(batch)}&retmode=xml"
    try:
        xml = get(url)
    except Exception as e:
        print(f"efetch err: {e}", file=sys.stderr)
        continue
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
        abst_parts = re.findall(r"<AbstractText[^>]*>(.*?)</AbstractText>", a, re.DOTALL)
        label_parts = re.findall(r'<AbstractText Label="([^"]*)"[^>]*>(.*?)</AbstractText>', a, re.DOTALL)
        if label_parts:
            abstract = "\n".join(f"{l}: {re.sub(r'<[^>]+>','',t).strip()}" for l, t in label_parts)
        else:
            abstract = " ".join(re.sub(r"<[^>]+>", "", p).strip() for p in abst_parts)
        doi_m = re.search(r'<ArticleId IdType="doi">(.*?)</ArticleId>', a)
        doi = doi_m.group(1).strip() if doi_m else ""
        pubtype = ", ".join(re.findall(r"<PublicationType[^>]*>(.*?)</PublicationType>", a))
        records.append({
            "pmid": pmid, "year": year, "journal": journal, "title": title,
            "doi": doi, "pubtype": pubtype, "abstract": abstract,
        })
    time.sleep(0.35)

records.sort(key=lambda r: (r["year"] or "0"), reverse=True)
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "hemostat_pubmed.json"), "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
with open(os.path.join(OUT, "hemostat_pubmed.txt"), "w", encoding="utf-8") as f:
    for r in records:
        f.write(f"### PMID {r['pmid']} ({r['year']}) — {r['journal']}\n")
        f.write(f"TITLE: {r['title']}\n")
        f.write(f"DOI: {r['doi']}  | TYPE: {r['pubtype']}\n")
        f.write(f"ABSTRACT: {r['abstract'] or '(no abstract)'}\n\n")
print(f"WROTE {len(records)} records to {OUT}", file=sys.stderr)
