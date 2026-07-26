#!/usr/bin/env python3
"""Fetch PubMed metadata (title/journal/year/abstract/pubtypes/DOI) for the union PMID set."""
import json
import os
import time
import urllib.parse
import urllib.request
try:  # harden against XXE / entity-expansion; stdlib is the fallback
    import defusedxml.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "corpus")


def post(path, params):
    params = dict(params)
    params.setdefault("tool", "cvs_journal_research")
    params.setdefault("email", "ktonai.cs@gmail.com")
    data = urllib.parse.urlencode(params).encode()
    url = f"{BASE}/{path}"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if attempt == 3:
                raise
            print(f"    retry {attempt+1}: {e}")
            time.sleep(4 * (attempt + 1))


def text_of(node):
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def parse(xml):
    recs = []
    root = ET.fromstring(xml)
    for art in root.findall(".//PubmedArticle"):
        cit = art.find("MedlineCitation")
        pmid = text_of(cit.find("PMID"))
        a = cit.find("Article")
        title = text_of(a.find("ArticleTitle"))
        journal = text_of(a.find("./Journal/ISOAbbreviation")) or text_of(
            a.find("./Journal/Title"))
        year = text_of(a.find("./Journal/JournalIssue/PubDate/Year"))
        if not year:
            md = text_of(a.find("./Journal/JournalIssue/PubDate/MedlineDate"))
            year = md[:4]
        volume = text_of(a.find("./Journal/JournalIssue/Volume"))
        issue = text_of(a.find("./Journal/JournalIssue/Issue"))
        pages = text_of(a.find("./Pagination/MedlinePgn"))
        abst = " ".join(text_of(x) for x in a.findall("./Abstract/AbstractText"))
        ptypes = [text_of(x) for x in a.findall("./PublicationTypeList/PublicationType")]
        authors = []
        for au in a.findall("./AuthorList/Author"):
            ln = text_of(au.find("LastName"))
            ini = text_of(au.find("Initials"))
            if ln:
                authors.append(f"{ln} {ini}".strip())
        doi = ""
        pmc = ""
        # ArticleIdList directly under PubmedData only (avoid ReferenceList IDs)
        pd = art.find("PubmedData")
        if pd is not None:
            for aid in pd.findall("./ArticleIdList/ArticleId"):
                t = aid.get("IdType")
                if t == "doi" and not doi:
                    doi = text_of(aid)
                elif t == "pmc" and not pmc:
                    pmc = text_of(aid)
        if not doi:
            for eid in a.findall("./ELocationID"):
                if eid.get("EIdType") == "doi":
                    doi = text_of(eid)
                    break
        recs.append({
            "pmid": pmid, "title": title, "journal": journal, "year": year,
            "volume": volume, "issue": issue, "pages": pages,
            "abstract": abst, "ptypes": ptypes,
            "authors": authors[:6], "n_authors": len(authors),
            "doi": doi, "pmc": pmc,
        })
    return recs


def main():
    ids = json.load(open(os.path.join(OUT, "pmids_union.json")))["ids"]
    print(f"fetching {len(ids)} records")
    all_recs = []
    B = 200
    for i in range(0, len(ids), B):
        chunk = ids[i:i + B]
        xml = post("efetch.fcgi", {"db": "pubmed", "id": ",".join(chunk),
                                   "retmode": "xml"})
        recs = parse(xml)
        all_recs.extend(recs)
        print(f"  {i + len(chunk)}/{len(ids)}  (+{len(recs)})")
        time.sleep(0.4)
    with open(os.path.join(OUT, "meta.json"), "w") as f:
        json.dump(all_recs, f, indent=1, ensure_ascii=False)
    print(f"wrote {len(all_recs)} records")


if __name__ == "__main__":
    main()
