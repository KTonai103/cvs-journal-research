#!/usr/bin/env python3
"""download_status.json から「取得済み」「未取得（手配依頼）」の一覧を Markdown で出す。"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
recs = json.load(open(os.path.join(HERE, "raw/download_status.json")))
sel = {r["pmid"]: r.get("cat", "") for r in json.load(open(os.path.join(HERE, "raw/pmids.json")))}

ok = [r for r in recs if r["status"] == "ok"]
ng = [r for r in recs if r["status"] != "ok"]

lines = [f"# 文献取得状況（{len(ok)}/{len(recs)} 取得, 未取得 {len(ng)}）\n"]
lines.append("## 未取得（購読誌等 — タイトル + PMID）\n")
lines.append("| # | 分類 | 著者 | 年 | 雑誌 | タイトル | PMID | DOI |")
lines.append("|---|---|---|---|---|---|---|---|")
for i, r in enumerate(sorted(ng, key=lambda x: sel.get(x["pmid"], "")), 1):
    doi = r.get("doi", "")
    lines.append(f"| {i} | {sel.get(r['pmid'],'')} | {r.get('first_author','')} | {r.get('year','')} | "
                 f"{r.get('journal','')} | {r.get('title','')} | "
                 f"[{r['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/) | "
                 f"{'[doi](https://doi.org/'+doi+')' if doi else ''} |")

lines.append("\n## 取得済み\n")
lines.append("| # | 分類 | 著者 | 年 | 雑誌 | タイトル | PMID | ライセンス |")
lines.append("|---|---|---|---|---|---|---|---|")
for i, r in enumerate(sorted(ok, key=lambda x: sel.get(x["pmid"], "")), 1):
    lines.append(f"| {i} | {sel.get(r['pmid'],'')} | {r.get('first_author','')} | {r.get('year','')} | "
                 f"{r.get('journal','')} | {r.get('title','')} | "
                 f"[{r['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/) | {r.get('license','')} |")

out = os.path.join(HERE, "md/download_status.md")
open(out, "w").write("\n".join(lines) + "\n")
print(f"取得 {len(ok)} / 未取得 {len(ng)} → {out}")
for r in ng:
    print(f"  PMID {r['pmid']:<9} {r.get('journal','')} {r.get('year','')}  {r.get('title','')[:80]}")
