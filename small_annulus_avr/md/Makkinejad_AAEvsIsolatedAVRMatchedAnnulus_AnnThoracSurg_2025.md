---
title: "Aortic Annular Enlargement vs Isolated Aortic Valve Replacement in Patients With Matched Annulus"
authors: "Alexander Makkinejad et al. (Bo Yang)"
journal: "The Annals of Thoracic Surgery"
citation: "Ann Thorac Surg 2025;119(3):568-575"
doi: "10.1016/j.athoracsur.2024.07.022"
pmid: "39102933"
pdf: "[[small_annulus_avr/Reference/CatA_YIncision/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025.pdf]]"
tags:
  - small-annulus
  - savr
  - aae
  - ppm
  - y-incision
  - psm
  - annthoracsurg
date: 2026-06-11
category: "弁輪拡大術"
journal-abbr: "AnnThoracSurg"
paper-type: "cohort"
annulus-size: "21-23mm"
patient-bsa: ">1.8"
valve-type: "mixed"
enlargement-technique: "Nicks"
asian-cohort: no
ppm-rate: "moderate/severe 19% (AAE) vs 31% (AVR), P=.16"
viv-discussion: yes
sample-size: "n=224 (112 PSM pairs; 元 cohort 1328)"
follow-up: "median 3.6 yr (KM 6yr / reop 10yr)"
---

> [!NOTE] Key Message
> University of Michigan 単一施設、**native aortic annulus を ≤23 mm に揃えた** isolated AVR 1328 例を propensity score matching で 112 pair に整え、AAE 群 vs no-AAE 群を直接比較した retrospective cohort。AAE 群は prosthesis size の中央値が 1 サイズ大きく (25 vs 23)、内径も 24 mm vs 21.4 mm。周術期成績（operative mortality 1.8% vs 3.6%, P=.68）は同等だが、**6 年生存率は 98% vs 74% (P=.016)、AAE は midterm 死亡の独立保護因子 (HR 0.19, 95% CI 0.06-0.62, P=.006)**。moderate/severe PPM は 19% vs 31% (P=.16, NS)。「同サイズ弁輪同士を比較する」という設計が従来研究（小弁輪 vs 大弁輪の不適切比較）の交絡を解消した点が最大の novelty。**SAKURA-AVR の主要対比（matched 狭小弁輪での AAE vs no-AAE PSM）の最も近い既発表 analog**。

---

## 1. 背景

- AAE は半世紀以上前から「より大きな prosthesis を留置し LVOT 閉塞を防ぐ」目的で行われてきたが、その真の便益は依然 ambiguous。
- 従来研究は、experimental 群＝小弁輪で AAE を要した患者、control 群＝大弁輪で AAE 不要だった患者、という **不適切な比較**（apples to oranges）になっており、survival benefit を示せず、せいぜい noninferiority を示すにとどまっていた。AAE の使用率は近年の AVR 臨床試験でも <5% と極めて低い。
- 本研究の premise：AAE の outcome は **native annulus size を揃えた文脈**でのみ正しく評価できる。同サイズ弁輪（≤23 mm）の患者集団を PSM で揃え、「より大きな弁を入れること」の純粋効果を分離する。
- 仮説：同サイズ native annulus の患者間で、AAE は midterm outcome を改善する。
- 著者グループの先行研究：AS に対する AVR で **小さい prosthesis を留置された患者は短期・長期とも死亡リスクが高い**（Fallon ATS 2018, Yang ATS 2022）。size 25 未満の stented valve では native annulus に対し prosthesis 内径が小さく、EOA がおよそ半減する（Yang JTCVS 2024）。

## 2. 対象・方法

- 期間：2011 年 1 月-2022 年 6 月、Michigan Medicine。AS または AR に対する **isolated AVR 1328 例**（active endocarditis 除外）。
  - AVR 群（no-AAE）：1163 例
  - AVR+AAE 群：165 例（Nicks / Manouguian / Y-incision）
- **Propensity score matching**：optimal matching without replacement、standardized difference <0.1 を許容。**native aortic annulus diameter（術中実測）**、年齢、性別、糖尿病、慢性肺疾患、透析、EF、心臓手術既往、indication、高血圧、脂質異常、valve type、脳卒中既往、MI 既往、case status で調整 → **112 pair (n=224)** を抽出。
- データソース：STS Data Warehouse + カルテレビュー。生存/再手術は Michigan Death Index（2023/2/9 まで）と National Death Index（2018/12/31 まで）で補完、追跡 completeness は ≈100%。
- **PPM 定義（現行ガイドライン準拠）**：iEOA = AVA / BSA。非肥満では iEOA <0.85 cm²/m² を moderate、**<0.65 cm²/m² を severe**。肥満では <0.70 で moderate、<0.55 で severe。
- 統計：matched cohort で **Cox 比例ハザード**（annular enlargement, 年齢, 性別, BSA, 慢性肺疾患, AS as primary indication で調整）で late mortality の調整 HR を算出。Kaplan-Meier で生存推定、再手術は death を競合リスクとした cumulative incidence function（Gray test）。SAS 9.4、有意水準 .05。
- 術式：Nicks/Manouguian は全期間、Y-incision は 2020 年 8 月以降導入。Nicks/Manouguian は 1-2 サイズ up、Y-incision は 1-5（典型的に 3-4）サイズ up を目的。AAE 実施可否は術者の subjective judgment（体格・予想活動度を考慮）。

## 3. 主要結果

**ベースライン（PSM 後 224 例）**：年齢中央値 64-66 歳、男性 46-47%、両群とも median native annulus diameter 23 mm。唯一の有意差は **BSA（AAE 2.1 m² vs AVR 1.9 m², P<.001）** — AAE 群の方が体格が大きい（後述のとおり AAE に不利な交絡）。術前 mean gradient・AVA・MR 分布は同等。

| 項目 | AVR (no-AAE, n=112) | AVR+AAE (n=112) | P |
|---|---|---|---|
| Native annulus 径（中央値, mm） | 23 (21-23) | 23 (21-23) | >.99 |
| **Implanted valve size（中央値）** | **23 (21-23)** | **25 (23-27)** | **<.001** |
| Implanted valve 内径（mm） | 21.4 (20-22) | 24 (22-26) | <.001 |
| BSA (m²) | 1.9 (1.7-2.1) | 2.1 (1.9-2.3) | <.001 |
| Bioprosthetic / Mechanical | 90% / 9.8% | 92% / 8.0% | .37 |
| CPB time (min) | 111 (92-141) | 143 (122-172) | <.001 |
| Cross-clamp time (min) | 82 (70-102) | 115 (98-137) | <.001 |
| STS-PROM (%) | 1.4 | 1.4 | .64 |
| **Operative mortality** | **4 (3.6%)** | **2 (1.8%)** | **.68** |
| Pacemaker 植込み | 2.7% | 1.8% | >.99 |
| Stroke | 0% | 0% | >.99 |
| Reop for bleeding | 1.8% | 1.8% | >.99 |
| 1yr mean AV gradient (mmHg) | 11 (8-14) | 9 (8-12) | .08 |
| 1yr AVA (cm²) | 1.8 | 1.9 | .08 |
| 1yr iEOA (cm²/m²) | 0.94 | 0.99 | .53 |
| **Moderate/severe PPM** | **31% (18/59)** | **19% (10/53)** | **.16** |
| **6yr KM 生存率** | **74% (61-83%)** | **98% (93-100%)** | **.016** |
| 5yr 再手術率（CIF） | 1.9% (0.2-9.0%) | 9.1% (2.4-21%) | — |
| 10yr 再手術率（CIF） | 25% (7.8-46%) | 14% (4.2-31%) | .27 |

**Cox 比例ハザード（late mortality, matched cohort）**：

| Variable | HR (95% CI) | P |
|---|---|---|
| **Annular enlargement** | **0.19 (0.06-0.62)** | **.006** |
| Age | 1.04 (1.00-1.07) | .026 |
| Male sex | 1.00 (0.43-2.34) | >.99 |
| **Body surface area** | **5.77 (1.02-32.8)** | **.048** |
| Chronic lung disease | 2.79 (1.22-6.37) | .015 |
| Aortic stenosis (primary indication) | 0.94 (0.28-3.20) | .92 |

- 追跡中央値 3.6 年。**AAE は midterm 死亡の独立保護因子（HR 0.19）**。一方 BSA は HR 5.77 のリスク因子であり、AAE 群はその不利を抱えながらも生存優位を示した。
- 感度解析：BSA を PSM に組み込むと 6yr 生存は 98% vs 73%（P=.067, サンプル縮小による）と方向性は保持。
- 死因：AVR 群は退院後 18 例死亡（既知死因の 2/3 が cardiac death）、**AAE 群は退院後 2 例のみ（cardiac death ゼロ）**。
- 再手術：AVR 群は SVD（structural valve degeneration）が主因、AAE 群は endocarditis が主因だが、AAE 群の endocarditis 5 例中 4 例は感染高リスク背景（自己免疫疾患 2、術中汚染 1、皮膚 S. aureus colonization 1）。

## 4. 議論

- **本研究の核心**：native annulus 径を 23 mm に揃えたことで、「AAE そのもの」ではなく「より大きい弁を入れること」の純粋効果を抽出。両群の唯一の実質差は prosthesis size（25 vs 23, 1 フルサイズ差）と、AAE 群に不利な BSA。
- 著者は survival benefit の主機序を **prosthesis EOA が native AVA により近づくこと**と解釈（弁モデル・サイズの厳密一致によらず）。安静時 gradient 差は小さくとも運動時には EOA 1.5 vs 2.5 cm² で gradient 差 50 mmHg に達するという古典データ（Gorlin 1955）を引用。
- 周術期安全性：AF・脳卒中・再開胸・pacemaker・operative mortality いずれも同群。**術後 MR の悪化なし**（術前分布と比較して増悪せず）→ AAE 自体が合併症リスクを増やさないと結論。従来研究で AAE がリスク増と報告された差は、native annulus を揃えなかったことに起因すると主張。
- 従来「survival 差なし」研究はむしろ間接的に AAE の便益を確認している：小弁輪 + AAE 群が大弁輪 + AVR 群と同等生存を達成しているなら、AAE なしなら inferior だったはず。
- **ViV への含意（viv-discussion = yes）**：初回手術での AAE は consecutive な valve-in-valve TAVR を通じて gradient 最適化が persist し、理論上 long-term outcome を改善しうる。ただし本研究 scope 外で、prior surgical AAE あり/なしの ViV-TAVR 大規模集団でのみ検証可能と明言。

## 5. 本研究RQへの含意（最重要）

> **本論文は SAKURA-AVR の Primary contrast（matched 狭小弁輪での AAE-SAVR vs no-AAE SAVR を PSM で比較）の、現時点で最も直接的な既発表 analog**。設計思想（native annulus を揃える）が SAKURA の inclusion stratum（measured annulus ≤23 mm）とほぼ一致する。

- **Primary RQ（AAE-SAVR は no-AAE SAVR / TAVI より優れるか）**：本論文は **no-AAE SAVR(Arm1) vs AAE-SAVR(Arm2) を ≤23 mm matched で直接比較**し、AAE の **midterm survival 優位（6yr 98% vs 74%, HR 0.19）と PPM 低減傾向（19% vs 31%）** を示す。SAKURA の主要仮説（AAE 群が outcome を改善）を支持する最有力先行エビデンス。ただし (1) アジア系・小 BSA でなく **むしろ AAE 群が BSA 大**、(2) co-primary が survival 中心で SAKURA の co-primary（measured iEOA による severe PPM ≤0.65 と 1yr mean gradient）は副次的・非有意（P=.08）、(3) TAVI reference アームを欠く点で SAKURA が補完すべき gap を示す。SAKURA は **measured EOA ベースの severe PPM (≤0.65 cm²/m²) を co-primary に据える**ことで、本研究が「postop echo の不足で gradient/iEOA 差が有意化しなかった」限界（P=.08）を克服する設計的意義をもつ。
- **Secondary RQ（将来 ViV を見据えた最小初回弁サイズ；19 mm は許容可能か）**：本論文は size 25 vs 23 という比較で、ViV を「scope 外」としつつも **初回 AAE による gradient 最適化が ViV 後も persist し long-term に有利**と理論的に主張。SAKURA の「ViV 用に最低どこまで upsize すべきか」という問いに対し、**「同サイズ弁輪でも 1 サイズ up（23→25）で survival 差が出る」**という閾値感覚を提供。19 mm の是非には直接答えないが、small valve = poor outcome の先行根拠（Yang ATS 2022, size <25 で EOA 半減）が AAE で 19 mm 回避を支持する文脈を補強。
- **Tertiary RQ（アジア解剖特異戦略）**：本 cohort は **米国・BSA 2.0 m² 級で asian-cohort = no**。AAE 群が BSA 大という構図は SAKURA の small-body アジア集団と真逆であり、**本研究の survival 効果がより小 BSA・小 annulus のアジア集団でも再現するかは未検証の gap**。SAKURA が埋めるべき external validity の核心を明示する反証材料/対照として有用。
- **方法論**：native annulus（術中実測）を最優先 covariate に据えた PSM 設計は、SAKURA の PSM/IPTW 設計の直接 template。STROBE 準拠・VARC-3・E-value はないため、SAKURA はこれらを上乗せして robustness を高める位置づけ。

## 6. 限界

- 単施設・retrospective、AAE 実施は無作為化でなく **術者の subjective judgment**（選択バイアス）。
- PSM 後サンプルが比較的小（112 pair）。
- prosthesis model/type（機械弁 vs 生体弁）は標準化されず（valve type は PSM に含むが）。
- **postop echo（EOA 算出可能なもの）の follow-up 率が低い** → gradient/iEOA/PPM 差が有意化せず（P=.08, .16）。SAKURA の co-primary が hemodynamics である点で、ここが最大の補完対象。
- 死亡は MDI/NDI 補完でも過小評価の可能性、long-term の死因が全例で得られていない。
- 再手術率も過小評価の可能性。
- AAE 群 BSA が大きく、survival 効果がより小 BSA 集団へ一般化できるか不明（アジア small-body への外挿の限界）。

## 7. 引用ハイライト

- Nicks R, Cartmill T, Bernstein L. *Thorax* 1970;25:339-46 — Nicks 原著（root hypoplasia）。
- Manouguian S, Seybold-Epting W. *J Thorac Cardiovasc Surg* 1979;78:402-12 — Manouguian 原著。
- Yang B, Naeem A. *Ann Thorac Surg* 2021;112:e139-41 — Y-incision 原著（3 サイズ up）。
- Yang B, Ghita C, Makkinejad A, et al. *J Thorac Cardiovasc Surg* 2024;167:1196-1205 — Y-incision で 3-4 サイズ up の早期成績（size <25 で EOA 半減の根拠）。
- Yang B. *Ann Thorac Surg* 2024;117:479-480 — 本研究の理論的前提となる editorial（"apples to oranges"：AAE 研究は native annulus を揃えるべき）。
- Fallon JM, et al. *Ann Thorac Surg* 2018;106:14-22 — SAVR 後 PPM の頻度と帰結（小弁＝予後不良の根拠）。
- Yang B, Makkinejad A, Fukuhara S, et al. *Ann Thorac Surg* 2022;114:728-734 — stentless vs stented AVR（小 prosthesis = 高死亡）。
- Pibarot P, Dumesnil JG. *J Am Coll Cardiol* 2000;36:1131-41 — PPM の血行動態・臨床的影響と予防（SAKURA の PPM 定義の源流）。
- Herrmann HC, et al. *J Am Coll Cardiol* 2018;72:2701-11 — STS/ACC TVT registry の TAVR 後 PPM（ViV 文脈）。
- 同号 Invited Commentary "How Big Is Good? Just Enough" (doi:10.1016/j.athoracsur.2024.09.029) — 内径は実測でなくメーカーラベル由来、早期 outcome 差なしは想定どおり、と論評。
