#!/usr/bin/env python3
"""Adversarially verify every technique-paper DOI against CrossRef, dedupe, enrich citations,
   and write per-subtopic synthesis input files + a verification log."""
import json, os, urllib.parse, urllib.request, concurrent.futures as cf, re, html
from collections import defaultdict
os.chdir(os.path.dirname(os.path.abspath(__file__)))

grouped = json.load(open("technique_grouped.json"))
papers = [p for lst in grouped.values() for p in lst]

def norm(s):
    return "".join(c.lower() for c in (s or "") if c.isalnum())

UA = {"User-Agent": "OPCAB-research/1.0 (mailto:ktonai.cs@gmail.com)"}

def verify(p):
    doi = p.get("doi")
    out = {"doi": doi, "verify": "no-doi"}
    if not doi:
        return out
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto=ktonai.cs@gmail.com"
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            m = json.load(r)["message"]
        ct = html.unescape(re.sub("<[^>]+>", "", (m.get("title") or [""])[0])).strip()
        out["cr_title"] = ct
        out["cr_journal"] = (m.get("container-title") or [""])[0]
        out["cr_type"] = m.get("type")
        out["volume"] = m.get("volume"); out["issue"] = m.get("issue"); out["page"] = m.get("page")
        yr = None
        for dk in ("published","published-print","published-online","issued"):
            dp = (m.get(dk) or {}).get("date-parts")
            if dp and dp[0] and dp[0][0]:
                yr = dp[0][0]; break
        out["cr_year"] = yr
        au = m.get("author") or []
        out["authors"] = ", ".join(
            f"{a.get('family','')} {''.join(w[0] for w in a.get('given','').split())}".strip()
            for a in au[:4]) + (" et al" if len(au) > 4 else "")
        a, b = norm(p.get("en_title") or p.get("title")), norm(ct)
        out["verify"] = "match" if (a and b and (a == b or a in b or b in a or a[:40] == b[:40])) else "MISMATCH"
    except Exception as e:
        out["verify"] = f"err:{type(e).__name__}"
    return out

ver = {}
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    futs = {ex.submit(verify, p): p.get("doi") for p in papers}
    for fut in cf.as_completed(futs):
        r = fut.result(); ver[r["doi"]] = r

# merge verification into papers + dedupe by normalized title
by_title = {}
for p in papers:
    v = ver.get(p.get("doi"), {})
    p = dict(p)
    p["verify"] = v.get("verify", "no-doi")
    p["authors"] = v.get("authors", p.get("authorString",""))
    # prefer crossref citation metadata, fall back to harvested
    p["c_journal"] = v.get("cr_journal") or p.get("journal")
    p["c_year"] = v.get("cr_year") or p.get("year") or p.get("epmc_year")
    p["c_vol"] = v.get("volume") or p.get("volume")
    p["c_issue"] = v.get("issue") or p.get("issue")
    p["c_page"] = v.get("page") or p.get("page")
    p["cr_type"] = v.get("cr_type")
    nt = norm(p.get("en_title") or p.get("title"))
    if nt in by_title:
        # merge duplicate: keep best importance/abstract, record alt doi
        ex0 = by_title[nt]
        ex0.setdefault("alt_dois", [])
        if p.get("doi") and p["doi"] != ex0.get("doi"):
            ex0["alt_dois"].append(p["doi"])
        if (p.get("importance") or 0) > (ex0.get("importance") or 0):
            ex0["importance"] = p["importance"]
        if len(p.get("abstract") or "") > len(ex0.get("abstract") or ""):
            ex0["abstract"] = p["abstract"]
        if p.get("verify") == "match" and ex0.get("verify") != "match":
            ex0["verify"] = "match"; ex0["doi"] = p["doi"]
    else:
        by_title[nt] = p

dedup = list(by_title.values())
print(f"papers: {len(papers)} -> deduped: {len(dedup)}")

from collections import Counter
print("verify:", dict(Counter(p["verify"] for p in dedup)))
mm = [p for p in dedup if p["verify"] == "MISMATCH"]
print(f"MISMATCHES: {len(mm)}")
for p in mm:
    print("  DOI", p["doi"], "\n    stored:", (p.get('en_title') or p.get('title'))[:70],
          "\n    crossref:", ver.get(p['doi'],{}).get('cr_title','')[:70])

# regroup deduped by subtopic, sort
g2 = defaultdict(list)
for p in dedup:
    g2[p["subtopic"]].append(p)
for s in g2:
    g2[s].sort(key=lambda m: (-(m.get("importance") or 0), -(m.get("c_year") or 0)))

os.makedirs("synth", exist_ok=True)
for s, lst in g2.items():
    slim = [{
        "doi": p.get("doi"), "alt_dois": p.get("alt_dois", []), "pmid": p.get("pmid"),
        "title": p.get("en_title") or p.get("title"), "authors": p.get("authors"),
        "journal": p.get("c_journal"), "year": p.get("c_year"),
        "vol": p.get("c_vol"), "issue": p.get("c_issue"), "page": p.get("c_page"),
        "media": p.get("media"), "importance": p.get("importance"),
        "oa": p.get("isOpenAccess"), "verify": p.get("verify"),
        "ja_summary": p.get("ja_summary"), "key_features": p.get("key_features"),
        "abstract": (p.get("abstract") or "")[:1400],
    } for p in lst]
    json.dump(slim, open(f"synth/{s}.json", "w"), ensure_ascii=False, indent=1)

json.dump(dedup, open("verified_technique.json", "w"), ensure_ascii=False, indent=1)

# verification log
with open("../output/doi_verification_opcab_technique.md", "w") as f:
    f.write("# OPCAB Technique 論文 DOI検証ログ\n\n")
    f.write(f"- 技術論文（重複除去後）: **{len(dedup)}** 件\n")
    f.write(f"- CrossRef照合 match: {sum(1 for p in dedup if p['verify']=='match')} / "
            f"MISMATCH: {len(mm)} / DOIなし(PMIDのみ): {sum(1 for p in dedup if p['verify']=='no-doi')} / "
            f"取得エラー: {sum(1 for p in dedup if p['verify'].startswith('err'))}\n\n")
    f.write("| # | subtopic | media | ★ | year | journal | title | DOI | 検証 |\n")
    f.write("|---|---|---|---|---|---|---|---|---|\n")
    for i, p in enumerate(sorted(dedup, key=lambda m:(m['subtopic'], -(m.get('importance') or 0))), 1):
        em = {"match":"✅","MISMATCH":"❌","no-doi":"—"}.get(p['verify'], "⚠️")
        f.write(f"| {i} | {p['subtopic']} | {p.get('media')} | {p.get('importance')} | {p.get('c_year')} | "
                f"{(p.get('c_journal') or '')[:30]} | {(p.get('title') or '')[:60]} | "
                f"{p.get('doi') or '(PMID:'+str(p.get('pmid'))+')'} | {em} {p['verify']} |\n")
print("\nwrote verified_technique.json, synth/*.json, ../output/doi_verification_opcab_technique.md")
print("subtopic counts (deduped):", {s: len(v) for s, v in sorted(g2.items())})
