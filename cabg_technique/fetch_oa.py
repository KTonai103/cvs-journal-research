#!/usr/bin/env python3
"""Resolve OA status via Europe PMC and download every PDF we can legitimately get.

NCBI's own PMC web endpoints are behind reCAPTCHA and the oa_pdf FTP mirror 404s over
https, so Europe PMC's `?pdf=render` is the working route for PMC-hosted full texts.
Anything without a free full text is reported as "manual request needed".
"""
import json, os, re, subprocess, time, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
PDFDIR = os.path.join(HERE, "pdf")
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")


def curl_text(url):
    return subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, url],
                          capture_output=True, text=True).stdout


def curl_pdf(url, dest, referer=None):
    cmd = ["curl", "-sL", "--max-time", "240", "-A", UA]
    if referer:
        cmd += ["-e", referer]
    cmd += ["-o", dest, url]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        with open(dest, "rb") as f:
            if f.read(5).startswith(b"%PDF"):
                return True
    if os.path.exists(dest):
        os.remove(dest)
    return False


def slug(s, n=52):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")[:n].rstrip("-")


def epmc_meta(pmid):
    q = urllib.parse.urlencode({
        "query": f"EXT_ID:{pmid} AND SRC:MED",
        "resultType": "core", "format": "json", "pageSize": "1",
    })
    try:
        res = json.loads(curl_text(f"{EPMC}?{q}")).get("resultList", {}).get("result", [])
    except Exception:
        return {}
    if not res:
        return {}
    r = res[0]
    return {
        "pmcid": r.get("pmcid", ""),
        "is_oa": r.get("isOpenAccess", "N") == "Y",
        "in_epmc": r.get("inEPMC", "N") == "Y",
        "license": r.get("license", ""),
        "has_pdf": (r.get("fullTextUrlList", {}).get("fullTextUrl") or []),
    }


os.makedirs(PDFDIR, exist_ok=True)
recs = json.load(open(os.path.join(HERE, "raw/selected_verified.json")))
order = {p: i for i, p in enumerate(open(os.path.join(HERE, "selected.txt")).read().split())}
recs.sort(key=lambda r: order.get(r["pmid"], 999))

results = []
for idx, r in enumerate(recs, 1):
    meta = epmc_meta(r["pmid"])
    time.sleep(0.2)
    pmc = meta.get("pmcid") or r.get("pmc") or ""
    name = (f"{idx:02d}_{r['year']}_{slug(r['first_author'], 18)}_"
            f"{slug(r['journal'], 14)}_{slug(r['title'], 46)}_PMID{r['pmid']}.pdf")
    dest = os.path.join(PDFDIR, name)
    status, src = "manual", ""

    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        status, src = "ok", "cached"
    elif pmc:
        art = f"https://europepmc.org/article/PMC/{pmc}"
        if curl_pdf(f"https://europepmc.org/articles/{pmc}?pdf=render", dest, referer=art):
            status, src = "ok", "europepmc"
        time.sleep(0.4)

    results.append({**r, "pmcid": pmc, "epmc_license": meta.get("license", ""),
                    "is_oa": meta.get("is_oa", False),
                    "file": name if status == "ok" else "", "status": status, "source": src})
    size = os.path.getsize(dest) // 1024 if status == "ok" else 0
    print(f"[{idx:02d}/60] {status:<6} {src:<10} {pmc or '-':<12} "
          f"{meta.get('license','') or '-':<12} {size:>5}KB  {r['pmid']}  {r['title'][:52]}",
          flush=True)

json.dump(results, open(os.path.join(HERE, "raw/download_status.json"), "w"),
          ensure_ascii=False, indent=1)
ok = [r for r in results if r["status"] == "ok"]
print(f"\n=== 取得成功 {len(ok)}/60 ／ 手配依頼 {60 - len(ok)} ===")
