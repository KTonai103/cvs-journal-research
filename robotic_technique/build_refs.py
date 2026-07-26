#!/usr/bin/env python3
"""Build the reference list and video/link appendix for the review.

Sources: corpus/link_inventory.json (the original 59) + corpus/link_inventory_extra.json
(added while writing) + the MMCTS tutorials, whose canonical link is the
`source:` line in the md frontmatter (mmcts.org/tutorial/NNNN).
"""
import json
import os
import re
import time
import urllib.request
import xml.etree.ElementTree as ET

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# added after link_inventory.json was frozen
EXTRA = {
    "Arai_2026_Combined_TECAB_Multivessel_and_Mitral_Repair_JTCVSTech": "41658920",
    "Goto_2025_DualCamera_Port_Setup_Endoscopic_Aortic_Mitral_Cureus": "40671980",
    "Murtaza_2025_SingleIncision_Transaxillary_Robotic_Valve_CABG_ACS": "40547429",
    "Murtaza_2025_Lateral_Approach_RAVR_Visualization_ACS": "40547428",
    "Bonatti_2024_Circumflex_Territory_Exposure_TECAB_ACS": "39434978",
    "Kitahara_2025_RapidDeployment_AVR_plus_MitralRepair_MMCTS": "40799111",
    "Noda_2024_Robotic_CoronarySinus_ASD_Tricuspid_Annuloplasty_GTCSCases": "39517038",
    "Pitsis_2021_Endoscopic_AVR_with_TransAortic_Mitral_Repair_JCS": "34742341",
    "Rowse_2024_Concomitant_Tricuspid_Repair_Robotic_Mitral_JTCVSOpen": "39780833",
    "Rufa_2023_Robotic_vs_MinimalAccess_Mitral_with_Cryoablation_JTD": "38249871",
    "Stelzmueller_2024_MICS_Mitral_plus_Tricuspid_Concomitant_FrontCVM": "39185133",
    "Wei_2025_Combined_Aortic_Mitral_Robotic_Endoscopic_NTUH_ACS": "40547423",
    "Wei_2025_RAVR_Beyond_Isolated_Multivalve_Platform_ACS": "40547424",
    "Rowse_2025_Concomitant_Procedures_Robotic_Mitral_STCVS_ABSTRACT": "39672523",
    "NCVC_2026_Robotic_Mitral_plus_OnPump_CABG_LAD_ATS_ABSTRACT": "41690664",
    "Robotic_TAVR_Explant_and_AVR_ATS_2025_ABSTRACT": "40750037",
}

# full text not obtainable (subscription); cited from the abstract only
ABSTRACT_ONLY = {
    "40913323",  # Qi, port-site balloon tamponade
    "41622650",  # Algoet, hinotori BITA cadaver
    "37753828",  # AlJamal, TECAB simulator
    "39672523",  # Rowse, concomitant procedures review
    "41690664",  # NCVC, robotic MV + on-pump CABG
    "40750037",  # robotic TAVR explant + AVR
}


def strip_ext(p):
    return re.sub(r"\.(pdf|md)$", "", os.path.basename(p))


def collect_ids():
    ids = {}
    for e in json.load(open("corpus/link_inventory.json")):
        ids[strip_ext(e["file"])] = e["pmid"]
    ids.update(EXTRA)
    return ids


def mmcts_links():
    """slug -> mmcts.org tutorial/case-report URL, read from md frontmatter."""
    out = {}
    for f in sorted(os.listdir("md")):
        if not f.endswith(".md"):
            continue
        head = open(f"md/{f}", errors="replace").read(1200)
        m = re.search(r'source:\s*"(https?://(?:www\.)?mmcts\.org/\S+?)"', head)
        if m:
            out[strip_ext(f)] = m.group(1)
    return out


def fetch(pmids):
    recs = {}
    for i in range(0, len(pmids), 150):
        chunk = pmids[i:i + 150]
        url = f"{EUTILS}/efetch.fcgi?db=pubmed&id={','.join(chunk)}&retmode=xml"
        root = ET.fromstring(urllib.request.urlopen(url).read())
        for a in root.findall(".//PubmedArticle"):
            pmid = a.findtext(".//MedlineCitation/PMID")
            authors = []
            for au in a.findall(".//AuthorList/Author"):
                ln, ini = au.findtext("LastName"), au.findtext("Initials")
                if not ln:
                    continue
                # MMCTS records sometimes carry the full name in <LastName>
                # ("Yazan N AlJamal" + Initials "YN"); keep only the surname.
                ln = ln.split()[-1] if " " in ln else ln
                authors.append(f"{ln} {ini or ''}".strip())
            doi = ""
            for x in a.findall(".//PubmedData/ArticleIdList/ArticleId"):
                if x.get("IdType") == "doi":
                    doi = x.text
            pub = a.find(".//JournalIssue/PubDate")
            year = (pub.findtext("Year") or (pub.findtext("MedlineDate") or "")[:4]) if pub is not None else ""
            recs[pmid] = {
                "pmid": pmid,
                "authors": authors,
                "title": "".join(a.find(".//ArticleTitle").itertext()).rstrip("."),
                "journal": a.findtext(".//Journal/ISOAbbreviation") or a.findtext(".//Journal/Title"),
                "year": year,
                "volume": a.findtext(".//JournalIssue/Volume") or "",
                "issue": a.findtext(".//JournalIssue/Issue") or "",
                "pages": a.findtext(".//Pagination/MedlinePgn") or "",
                "doi": doi,
            }
        time.sleep(0.4)
    return recs


def authors_str(a):
    if not a:
        return ""
    if len(a) <= 3:
        return ", ".join(a)
    return f"{a[0]}, et al"


def main():
    ids = collect_ids()
    links = mmcts_links()
    pmids = sorted({p for p in ids.values() if p})
    recs = fetch(pmids)

    rows = []
    for slug, pmid in ids.items():
        r = dict(recs.get(pmid, {"pmid": pmid, "authors": [], "title": slug,
                                 "journal": "", "year": "", "volume": "",
                                 "issue": "", "pages": "", "doi": ""}))
        r["slug"] = slug
        r["mmcts"] = links.get(slug, "")
        rows.append(r)
    rows.sort(key=lambda r: (r["authors"][0] if r["authors"] else r["slug"]).lower())

    lines = ["| # | 文献 | リンク |", "|---:|:--|:--|"]
    for n, r in enumerate(rows, 1):
        cite = f"{authors_str(r['authors'])}. {r['title']}. *{r['journal']}* {r['year']}"
        if r["volume"]:
            cite += f";{r['volume']}"
            if r["issue"]:
                cite += f"({r['issue']})"
            if r["pages"]:
                cite += f":{r['pages']}"
        cite += "."
        if r["pmid"] in ABSTRACT_ONLY:
            cite += " ※抄録のみ引用（本文未取得）"
        ln = []
        if r["mmcts"]:
            ln.append(f"[MMCTS]({r['mmcts']})")
        if r["doi"]:
            ln.append(f"[DOI](https://doi.org/{r['doi']})")
        if r["pmid"]:
            ln.append(f"[PubMed](https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/)")
        lines.append(f"| {n} | {cite} | {' ・ '.join(ln)} |")

    open("corpus/references.md", "w").write("\n".join(lines) + "\n")
    json.dump(rows, open("corpus/references.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(rows)} references -> corpus/references.md")
    missing = [r["slug"] for r in rows if not r["title"] or not r["journal"]]
    if missing:
        print("INCOMPLETE:", missing)


if __name__ == "__main__":
    main()
