#!/usr/bin/env python3
"""Resolve PMID -> PMCID (ID converter) and check PMC-OA license via oa.fcgi."""
import json, subprocess, os, re, time

HERE = os.path.dirname(os.path.abspath(__file__))
IDCONV = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
OAFCGI = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36"


def curl(url):
    return subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, url],
                          capture_output=True, text=True).stdout


recs = json.load(open(os.path.join(HERE, "raw/selected_verified.json")))
pmids = [r["pmid"] for r in recs]

# 1) PMID -> PMCID
pmcmap = {}
for i in range(0, len(pmids), 50):
    chunk = pmids[i:i + 50]
    d = curl(f"{IDCONV}?ids={','.join(chunk)}&format=json")
    try:
        for rec in json.loads(d).get("records", []):
            if rec.get("pmcid"):
                pmcmap[rec.get("pmid")] = rec["pmcid"]
    except Exception as e:
        print("idconv parse error", e, d[:200])
    time.sleep(0.3)

# 2) oa.fcgi -> license + direct file links
out = []
for r in recs:
    pmc = pmcmap.get(r["pmid"]) or r.get("pmc") or ""
    lic, pdf_link, tgz_link = "", "", ""
    if pmc:
        x = curl(f"{OAFCGI}?id={pmc}")
        m = re.search(r'license="([^"]*)"', x)
        lic = m.group(1) if m else ""
        for mm in re.finditer(r'<link format="([^"]+)" href="([^"]+)"', x):
            fmt, href = mm.group(1), mm.group(2)
            href = href.replace("ftp://ftp.ncbi.nlm.nih.gov", "https://ftp.ncbi.nlm.nih.gov")
            if fmt == "pdf":
                pdf_link = href
            elif fmt == "tgz":
                tgz_link = href
        time.sleep(0.25)
    out.append({**r, "pmcid": pmc, "oa_license": lic,
                "oa_pdf": pdf_link, "oa_tgz": tgz_link})

json.dump(out, open(os.path.join(HERE, "raw/oa_status.json"), "w"),
          ensure_ascii=False, indent=1)

n_pmc = sum(1 for r in out if r["pmcid"])
n_oa = sum(1 for r in out if r["oa_license"])
print(f"PMC あり: {n_pmc}/60   OAサブセット(license付き): {n_oa}/60\n")
for r in out:
    print(f"{r['pmid']}\t{r['pmcid'] or '-':<12}\t{r['oa_license'] or '-':<14}"
          f"\t{'PDF' if r['oa_pdf'] else ('TGZ' if r['oa_tgz'] else '-'):<4}\t{r['title'][:70]}")
