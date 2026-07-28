#!/usr/bin/env python3
"""Assemble the final OPCAB technique review markdown."""
import json, os, re
from collections import Counter
os.chdir(os.path.dirname(os.path.abspath(__file__)))

d = json.load(open("verified_technique.json"))
BADGE = {"video": "📹", "figure_rich": "🖼️", "standard": "📄", "unknown": "📄"}

def jnorm(j):
    j = j or ""
    if "Multimedia Manual" in j: return "Multimedia Manual of Cardio-Thoracic Surgery (MMCTS)"
    if j.startswith("Innovations"): return "Innovations"
    if "Operative Techniques in Thoracic" in j: return "Operative Techniques in Thoracic and Cardiovascular Surgery"
    if "Annals of Cardiothoracic" in j or "Annals of cardiothoracic" in j: return "Annals of Cardiothoracic Surgery"
    if "JTCVS Techniques" in j: return "JTCVS Techniques"
    if "Annals of Thoracic" in j or "Annals of thoracic" in j: return "The Annals of Thoracic Surgery"
    return j

def doilink(p):
    if p.get("doi"):
        return f"[{p['doi']}](https://doi.org/{p['doi']})"
    if p.get("pmid"):
        return f"[PMID:{p['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{p['pmid']}/)"
    return "—"

def oamark(p): return "🔓" if p.get("isOpenAccess") == "Y" else ""

def short(p, n=78):
    t = p.get("en_title") or p.get("title") or ""
    return t if len(t) <= n else t[:n-1] + "…"

# ---- stats ----
N = len(d)
media_c = Counter(p.get("media") for p in d)
jcount = Counter(jnorm(p.get("c_journal") or p.get("journal")) for p in d)
yrs = [p.get("c_year") for p in d if p.get("c_year")]
oa_n = sum(1 for p in d if p.get("isOpenAccess") == "Y")

# ---- curated lists ----
videos = sorted([p for p in d if p.get("media") == "video"],
                key=lambda p: (-(p.get("importance") or 0), -(p.get("c_year") or 0)))
land5 = sorted([p for p in d if (p.get("importance") or 0) >= 5],
               key=lambda p: (BADGE.get(p.get("media")) != "📹", -(p.get("c_year") or 0)))

SECTION_ORDER = [
    "general_overview_review", "anaortic_total_arterial", "exposure_stabilization",
    "anastomosis_grafts", "shunt_flow_hemodynamics", "midcab_mics", "robotic_tecab",
    "hybrid", "special_population_redo", "conversion_safety", "training_simulation",
]

out = []
W = out.append

W("""---
title: Off-pump CABG（OPCAB）手技論文 網羅的レビュー
subtitle: 図表・ビデオ中心のオペレーティブ・テクニック文献サーベイ
date: 2026-05-30
scope: Off-pump CABG（OPCAB / MIDCAB / MICS-CABG / robotic-TECAB / anaortic 全動脈）の手技論文
journals:
  - JTCVS Techniques
  - Multimedia Manual of Cardio-Thoracic Surgery (MMCTS)
  - Annals of Cardiothoracic Surgery
  - Operative Techniques in Thoracic and Cardiovascular Surgery
  - Innovations (Technology and Techniques in CT & Vascular Surgery)
sources:
  - CrossRef REST API (ISSN別検索)
  - PubMed E-utilities (手技アングル別検索)
  - Europe PMC (abstract取得・タイトル照合)
tags:
  - OPCAB
  - off-pump
  - coronary-bypass
  - surgical-technique
  - MIDCAB
  - robotic-CABG
  - anaortic
  - journal-review
  - "2026"
---

# Off-pump CABG（OPCAB）手技論文 網羅的レビュー

> [!abstract] このレビューの要旨
> Off-pump CABG（OPCAB）の**手術手技（how-to）**に焦点を当て、**図表が豊富なオペレーティブ・テクニック論文**と**ビデオ解説論文**を中心に網羅的にサーベイした。CrossRef（雑誌ISSN別）＋PubMed（手技アングル別）で **3,154編** を収集 → off-pump系タイトルで **1,344編** に絞り込み → 手技系雑誌・手技系タイトルで **376編** をコア候補とし → 16体の分類エージェントで判定して最終的に **""" + str(N) + """編の手技論文**を確定した。媒体内訳は 🖼️図表豊富 """ + str(media_c.get('figure_rich',0)) + """ / 📹ビデオ """ + str(media_c.get('video',0)) + """ / 📄標準 """ + str(media_c.get('standard',0)) + """、年代は """ + f"{min(yrs)}–{max(yrs)}" + """、オープンアクセス """ + str(oa_n) + """編。**全""" + str(N) + """編のDOIは実在を確認済み（誤リンク0件）**。
""")

# ---- Section 0: scope/method ----
W("""## 0. この調査について（スコープと方法）

**目的** — OPCABの「やり方」を学ぶための一次文献を、**図解アトラス**と**手術ビデオ**を中心に体系的に集約する。臨床アウトカム（生存率比較等）が主題の研究は原則として対象外とし（§4に主要RCTのみ文脈として掲載）、手技の記述（展開・脱転・吻合・グラフト構成・デバイス・低侵襲/ロボットアプローチ・コツと落とし穴）を主眼とした論文を採録した。

**検索戦略（多段階・機械的収集）**
1. **CrossRef REST API** — 手技系5誌（JTCVS Techniques 2666-2507 / MMCTS 1813-9175 / Operative Techniques in Thoracic CV Surgery 1522-2942 / Annals of Cardiothoracic Surgery 2225-319X / Innovations 1559-0879）＋一般6誌（JTCVS, Ann Thorac Surg, EJCTS, ICVTS/Interdiscip, J Card Surg, J Cardiothorac Surg）を ISSN別に複数クエリ（off-pump / beating-heart / anaortic / MIDCAB / anastomosis）で検索。
2. **PubMed E-utilities** — 手技アングル別15クエリ（technique/how-to, anaortic, exposure-stabilization, MIDCAB, robotic-TECAB, shunt-flow, BITA, hybrid, video-multimedia, composite-graft, multivessel, review, conversion, special-population）。
3. **Europe PMC** — 各候補のabstract取得とDOI↔タイトル照合（一次検証）。
4. **分類** — 16体のエージェントが各論文を「手技論文か否か・サブトピック・媒体（video/figure-rich/standard）・重要度★1-5・日本語要約」に分類。
5. **DOI検証** — 確定""" + str(N) + """編の全DOIをCrossRef個別照会で再検証（タイトル一致確認、誤リンク0件）。検証ログ → [`output/doi_verification_opcab_technique.md`](../output/doi_verification_opcab_technique.md)。

**絞り込みの流れ:** 3,154編（収集）→ 1,344編（off-pump系タイトル）→ 376編（手技系雑誌/タイトル）→ **""" + str(N) + """編（手技論文確定・重複除去後）**。

**媒体バッジの凡例:** 🖼️ = 図表が豊富なオペテク（術中写真・シェーマ多数）／📹 = ビデオ解説論文（手術動画つき）／📄 = 標準的記述／🔓 = オープンアクセス／★ = 手技教材としての重要度（★5=ランドマーク的how-to・必読）。
""")

# ---- Section 1: stats ----
W("## 1. サマリー統計\n")
W(f"- **確定手技論文: {N}編**（重複除去後）／年代 **{min(yrs)}–{max(yrs)}**／オープンアクセス **{oa_n}編**")
W(f"- 媒体内訳: 🖼️ 図表豊富 **{media_c.get('figure_rich',0)}** ／ 📹 ビデオ **{media_c.get('video',0)}** ／ 📄 標準 **{media_c.get('standard',0)}**")
W(f"- 重要度内訳: " + " ／ ".join(f"★{s}×{c}" for s, c in sorted(Counter(p.get('importance') for p in d).items(), reverse=True)))
W("\n**掲載誌別**\n")
W("| 雑誌 | 編数 |\n|---|---:|")
for j, c in jcount.most_common():
    W(f"| {j} | {c} |")
W("")

# ---- Section 2: curated ----
W("## 2. 必読ガイド（横断キュレーション）\n")
W("### 2-1. 📹 ビデオ解説論文（手術動画つき）\n")
W("OPCABの手技を**動画で学べる**論文。MMCTS（EACTS公式マルチメディア手技マニュアル）が中心で、anaortic全動脈・MIDCAB・ロボットTECABの各アプローチを step-by-step 動画で提供する。\n")
W("| ★ | 年 | 論文 | 雑誌 | DOI |\n|:--:|:--:|---|---|---|")
for p in videos:
    W(f"| {p.get('importance')} | {p.get('c_year')} | {oamark(p)} {short(p)} | {jnorm(p.get('c_journal'))} | {doilink(p)} |")
W(f"\n→ ビデオ解説論文 **計{len(videos)}編**。\n")

W("### 2-2. ★★★★★ ランドマーク手技論文（媒体問わず）\n")
W("手技教材として特に価値の高い★5論文。図解アトラスとビデオの双方を含む。\n")
W("| 媒体 | 年 | 論文 | 雑誌 | DOI |\n|:--:|:--:|---|---|---|")
for p in land5:
    W(f"| {BADGE.get(p.get('media'),'📄')} | {p.get('c_year')} | {oamark(p)} {short(p)} | {jnorm(p.get('c_journal'))} | {doilink(p)} |")
W(f"\n→ ★5ランドマーク **計{len(land5)}編**。図表豊富なオペテク（★4・🖼️）は §3 各領域に収載。\n")

# ---- Section 3: per-subtopic (demote ## -> ###) ----
W("## 3. 技術領域別レビュー\n")
W(f"以下、{len(SECTION_ORDER)}領域に分けて全{N}編を解説する（各領域内は重要度★降順）。\n")
for key in SECTION_ORDER:
    fp = f"synth_out/{key}.md"
    if not os.path.exists(fp):
        continue
    body = open(fp).read().strip()
    body = re.sub(r"^## ", "### ", body, count=1)  # demote top header
    W(body)
    W("")

# ---- Section 4: evidence context ----
W("""## 4. エビデンスの文脈（OPCABの主要RCT・コンセンサス）

本レビューは手技論文を主題とするが、術式選択の前提として大規模RCTの結論を要約する。**OPCABとon-pump CABGは死亡率がおおむね同等**である一方、OPCABでは**完全血行再建率・遠隔グラフト開存が術者の習熟度に依存**しやすいことが繰り返し示されてきた。ここから「OPCABの利益（脳梗塞・輸血・腎障害の低減）はハイボリューム術者・anaortic/全動脈手技で最大化される」という、本レビュー収載論文（特に §2・§3-2）の技術的動機が導かれる。

- **ROOBY**: Shroyer AL, et al. *On-pump versus off-pump coronary-artery bypass surgery.* N Engl J Med 2009;361:1827-37. [10.1056/NEJMoa0902905](https://doi.org/10.1056/NEJMoa0902905)
- **ROOBY-FS（5年）**: Shroyer AL, et al. *Five-Year Outcomes after On-Pump and Off-Pump Coronary-Artery Bypass.* N Engl J Med 2017;377:623-632. [10.1056/NEJMoa1614341](https://doi.org/10.1056/NEJMoa1614341)
- **CORONARY（30日）**: Lamy A, et al. *Off-pump or on-pump coronary-artery bypass grafting at 30 days.* N Engl J Med 2012;366:1489-97. [10.1056/NEJMoa1200388](https://doi.org/10.1056/NEJMoa1200388)
- **CORONARY（1年）**: Lamy A, et al. *Effects of off-pump and on-pump coronary-artery bypass grafting at 1 year.* N Engl J Med 2013;368:1179-88. [10.1056/NEJMoa1301228](https://doi.org/10.1056/NEJMoa1301228)
- **CORONARY（5年）**: Lamy A, et al. *Five-Year Outcomes after Off-Pump or On-Pump Coronary-Artery Bypass Grafting.* N Engl J Med 2016;375:2359-2368. [10.1056/NEJMoa1601564](https://doi.org/10.1056/NEJMoa1601564)
- **GOPCABE（高齢者）**: Diegeler A, et al. *Off-pump versus on-pump coronary-artery bypass grafting in elderly patients.* N Engl J Med 2013;368:1189-98. [10.1056/NEJMoa1211666](https://doi.org/10.1056/NEJMoa1211666)
- **ISMICS コンセンサス（RCTのSR/MA）**: *ISMICS Consensus Conference and Statements of Randomized Controlled Trials of Off-Pump versus Conventional CABG.* Innovations 2015;10(4):219-229. [10.1177/155698451501000401](https://doi.org/10.1177/155698451501000401)
- **ロボットCABG 二十年メタ解析**: *Systematic review and meta-analysis of two decades of reported outcomes.* Ann Cardiothorac Surg 2024. [10.21037/acs-2023-rcabg-0191](https://doi.org/10.21037/acs-2023-rcabg-0191)

> [!note] NEJMの4 RCT（ROOBY/CORONARY/GOPCABE）は本サーベイの対象誌（心臓外科手技系誌）外のため機械収集には含まれず、DOIはPubMed/CrossRefで個別に実在確認した一次論文である。
""")

# ---- Section 5: reproducibility ----
W("""## 5. データソースと再現性

本レビューの生成物・中間データは `opcab_technique/` 配下に保存：

- `harvest.sh` — CrossRef/PubMed 収集スクリプト、`raw/` — 生JSON
- `candidates.json`（1,344）→ `core_candidates.json`（376）→ `core_with_abstracts.json`（Europe PMC付与）
- `classified/batch_*.json` — 16エージェントの分類結果
- `verified_technique.json`（""" + str(N) + """編・DOI検証済み）／`technique_grouped.json`
- `synth/*.json`（領域別入力）→ `synth_out/*.md`（領域別ドラフト）
- `tables/opcab_technique_papers.csv` — 全手技論文の一覧表
- `../output/doi_verification_opcab_technique.md` — DOI検証ログ

*検索実施日: 2026-05-30。CrossRef/PubMed/Europe PMC の収録状況により、ごく最近のOnline First論文が一部未反映の可能性がある。*
""")

final = "\n".join(out)
open("md/OPCAB_technique_review.md", "w").write(final)
print(f"wrote md/OPCAB_technique_review.md  ({len(final)} chars, {final.count(chr(10))} lines)")
print(f"DOI links in doc: {final.count('https://doi.org')}")
