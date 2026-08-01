#!/usr/bin/env python3
"""PMID のリストを受け取り、取れる PDF は全部取り、取れないものを一覧にする。

Europe PMC の `?pdf=render` が PMC 全文の実質唯一の安定ルート（NCBI 側は reCAPTCHA、
oa_pdf の https ミラーは 404）。PMC に無いものは Unpaywall で OA リンクを探し、
それでも駄目なら "manual"（＝タイトル+PMID で手配依頼）とする。

usage: python3 fetch_oa.py raw/pmids.json
       raw/pmids.json = [{"pmid": "...", "title": "...", "journal": "...", "year": "...",
                          "first_author": "...", "doi": "...", "why": "..."}, ...]
"""
import json, os, re, subprocess, sys, time, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
PDFDIR = os.path.join(HERE, "pdf")
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")
MAILTO = "ktonai.cs@gmail.com"


def curl_text(url, timeout="60"):
    return subprocess.run(["curl", "-sL", "--max-time", timeout, "-A", UA, url],
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
    return re.sub(r"[^A-Za-z0-9]+", "-", s or "").strip("-")[:n].rstrip("-")


def esummary(pmids):
    """PubMed から著者・雑誌・年・DOI を補完する。"""
    out = {}
    for i in range(0, len(pmids), 100):
        chunk = ",".join(pmids[i:i + 100])
        url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
               f"?db=pubmed&id={chunk}&retmode=json")
        try:
            res = json.loads(curl_text(url)).get("result", {})
        except Exception:
            continue
        for pid in res.get("uids", []):
            r = res[pid]
            doi = ""
            for aid in r.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid.get("value", "")
            out[pid] = {
                "title": r.get("title", "").rstrip("."),
                "journal": r.get("source", ""),
                "year": (r.get("pubdate", "") or "")[:4],
                "first_author": (r.get("authors") or [{}])[0].get("name", ""),
                "doi": doi,
            }
        time.sleep(0.34)
    return out


def epmc_meta(pmid):
    q = urllib.parse.urlencode({"query": f"EXT_ID:{pmid} AND SRC:MED",
                                "resultType": "core", "format": "json", "pageSize": "1"})
    try:
        res = json.loads(curl_text(f"{EPMC}?{q}")).get("resultList", {}).get("result", [])
    except Exception:
        return {}
    if not res:
        return {}
    r = res[0]
    return {"pmcid": r.get("pmcid", ""), "license": r.get("license", "") or "",
            "is_oa": r.get("isOpenAccess", "N") == "Y"}


def unpaywall_pdf(doi):
    if not doi:
        return ""
    try:
        j = json.loads(curl_text(
            f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={MAILTO}"))
    except Exception:
        return ""
    loc = j.get("best_oa_location") or {}
    return loc.get("url_for_pdf") or ""


def main(path):
    os.makedirs(PDFDIR, exist_ok=True)
    recs = json.load(open(path))
    pmids = [r["pmid"] for r in recs if r.get("pmid")]
    meta = esummary(pmids)

    results = []
    for idx, r in enumerate(recs, 1):
        pmid = r.get("pmid", "")
        m = {**meta.get(pmid, {}), **{k: v for k, v in r.items() if v}}
        e = epmc_meta(pmid) if pmid else {}
        time.sleep(0.2)
        pmc = e.get("pmcid", "") or r.get("pmcid", "")
        name = (f"{idx:03d}_{m.get('year','')}_{slug(m.get('first_author',''),18)}_"
                f"{slug(m.get('journal',''),14)}_{slug(m.get('title',''),44)}_PMID{pmid}.pdf")
        dest = os.path.join(PDFDIR, name)
        status, src = "manual", ""

        if os.path.exists(dest) and os.path.getsize(dest) > 20000:
            status, src = "ok", "cached"
        else:
            if pmc:
                if curl_pdf(f"https://europepmc.org/articles/{pmc}?pdf=render", dest,
                            referer=f"https://europepmc.org/article/PMC/{pmc}"):
                    status, src = "ok", "europepmc"
                time.sleep(0.4)
            if status != "ok":
                up = unpaywall_pdf(m.get("doi", ""))
                if up and curl_pdf(up, dest):
                    status, src = "ok", "unpaywall"
                time.sleep(0.3)

        results.append({**m, "pmid": pmid, "pmcid": pmc, "license": e.get("license", ""),
                        "is_oa": e.get("is_oa", False), "file": name if status == "ok" else "",
                        "status": status, "source": src})
        size = os.path.getsize(dest) // 1024 if status == "ok" else 0
        print(f"[{idx:03d}/{len(recs)}] {status:<6} {src:<10} {pmc or '-':<13} "
              f"{size:>5}KB  {pmid:<9} {m.get('title','')[:56]}", flush=True)

    json.dump(results, open(os.path.join(HERE, "raw/download_status.json"), "w"),
              ensure_ascii=False, indent=1)
    ok = [r for r in results if r["status"] == "ok"]
    print(f"\n=== 取得成功 {len(ok)}/{len(results)} ／ 手配依頼 {len(results)-len(ok)} ===")
    for r in results:
        if r["status"] != "ok":
            print(f"  PMID {r['pmid']:<9} {r.get('journal','')} {r.get('year','')}  {r.get('title','')}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "raw/pmids.json"))
