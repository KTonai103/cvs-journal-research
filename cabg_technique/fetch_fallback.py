#!/usr/bin/env python3
"""Second pass: publisher-direct OA routes for papers Europe PMC could not render.

AME journals (Ann Cardiothorac Surg / J Thorac Dis / ...) expose a direct /pdf href on the
article page reached via DOI. MDPI needs a referer. MMCTS serves its payload as Inertia JSON.
"""
import json, os, re, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
PDFDIR = os.path.join(HERE, "pdf")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")


def curl_text(url, referer=None):
    cmd = ["curl", "-sL", "--max-time", "90", "-A", UA]
    if referer:
        cmd += ["-e", referer]
    return subprocess.run(cmd + [url], capture_output=True, text=True).stdout


def curl_pdf(url, dest, referer=None):
    cmd = ["curl", "-sL", "--max-time", "240", "-A", UA]
    if referer:
        cmd += ["-e", referer]
    subprocess.run(cmd + ["-o", dest, url], capture_output=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        with open(dest, "rb") as f:
            if f.read(5).startswith(b"%PDF"):
                return True
    if os.path.exists(dest):
        os.remove(dest)
    return False


def try_ame(doi, dest):
    """AME Publishing (amegroups / annalscts): article page carries a /pdf link."""
    html = curl_text(f"https://doi.org/{doi}")
    for m in re.finditer(r'href="(https?://[^"]*?/article/view/\d+/pdf)"', html):
        if curl_pdf(m.group(1), dest, referer="https://doi.org/"):
            return "ame"
    return ""


def try_mdpi(doi, dest):
    """www.mdpi.com/.../pdf is Cloudflare-blocked; res.mdpi.com serves the deploy copy."""
    m = re.match(r"10\.3390/([a-z]+)(\d+)0*(\d+)$", doi)
    if m:
        jrn, vol, art = m.group(1), m.group(2), m.group(3)
        stem = f"{jrn}-{vol}-{int(art):05d}"
        url = f"https://res.mdpi.com/d_attachment/{jrn}/{stem}/article_deploy/{stem}.pdf"
        if curl_pdf(url, dest, referer="https://www.mdpi.com/"):
            return "mdpi"
    return ""


def try_epmc_alt(pmcid, dest, tries=3):
    """europepmc pdf=render is flaky under load - retry before giving up."""
    for _ in range(tries):
        if curl_pdf(f"https://europepmc.org/articles/{pmcid}?pdf=render", dest,
                    referer=f"https://europepmc.org/article/PMC/{pmcid}"):
            return "epmc_retry"
        time.sleep(2)
    return ""


rows = json.load(open(os.path.join(HERE, "raw/download_status.json")))
todo = [r for r in rows if r["status"] != "ok"]
print(f"再試行対象 {len(todo)} 件\n")

for r in todo:
    idx = rows.index(r) + 1
    name = r["file"] or (
        f"{idx:02d}_{r['year']}_"
        f"{re.sub(r'[^A-Za-z0-9]+','-',r['first_author'])[:18].strip('-')}_"
        f"{re.sub(r'[^A-Za-z0-9]+','-',r['journal'])[:14].strip('-')}_"
        f"{re.sub(r'[^A-Za-z0-9]+','-',r['title'])[:46].strip('-')}_PMID{r['pmid']}.pdf")
    dest = os.path.join(PDFDIR, name)
    doi = r.get("doi") or ""
    src = ""
    if doi.startswith("10.21037"):
        src = try_ame(doi, dest)
    elif doi.startswith("10.3390"):
        src = try_mdpi(doi, dest)
    if not src and r.get("pmcid"):
        src = try_epmc_alt(r["pmcid"], dest)
    if src:
        r["status"], r["source"], r["file"] = "ok", src, name
        print(f"  OK  {src:<9} {r['pmid']}  {r['title'][:60]}", flush=True)
    time.sleep(0.3)

json.dump(rows, open(os.path.join(HERE, "raw/download_status.json"), "w"),
          ensure_ascii=False, indent=1)
ok = sum(1 for r in rows if r["status"] == "ok")
print(f"\n=== 累計 取得 {ok}/60 ／ 手配依頼 {60 - ok} ===")
