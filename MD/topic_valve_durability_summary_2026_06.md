---
title: 外科用AVR人工弁 耐久性 — 取得論文11本の精読サマリー（弁別・最長フォロー）
date: 2026-06-09
type: topic-review
parent_review: "[[topic_savr_vs_tavr_longterm_2026_05]]"
parent_list: "[[topic_valve_durability_by_valve_2026_06]]"
focus:
  - bioprosthetic valve durability
  - longest published follow-up per valve
  - age- and size-stratified SVD
  - actuarial vs actual freedom
papers_read: 11
valves_covered:
  - Perceval (sutureless)
  - INTUITY (rapid-deployment)
  - PERIMOUNT Magna Ease
  - Hancock II (porcine)
  - Freestyle (stentless porcine)
  - Mitroflow
  - Soprano
  - Crown PRT
  - St Jude mechanical
sources:
  - 取得PDF全文（pdftotext）→ 11並列エージェントで構造化抽出
verification: "2026-06-09 抽出ワークフロー（11エージェント）。数値はPDF本文から逐語抽出"
tags:
  - cardiac-surgery
  - aortic-valve-prosthesis
  - durability
  - SVD
  - perceval
  - intuity
  - hancock-ii
  - freestyle
  - mitroflow
  - soprano
  - mechanical-valve
  - 2026
---

# 【A弁・大動脈位】外科用AVR人工弁 耐久性 — 取得論文11本 精読サマリー

> [!info]
> **🅰 本サマリーは全て大動脈位（A弁 / AVR）のデータです。** 僧帽位（M弁 / MVR）版は別途調査中 → [[topic_mitral_valve_durability_2026_06]]（Perceval・INTUITY・Inspiris・Avalus・Freestyle・Crown・Soprano は大動脈専用でM弁版なし）。
>
> **対象**：2026-06-09に取得した弁耐久性論文 **11本（10弁）** を全文精読し、SVD・再手術・生存・血行動態を時点別に抽出したもの。
> PDFは [valve_durability/pdf/](../valve_durability/pdf/)、抽出テキストは [valve_durability/pdf_text/](../valve_durability/pdf_text/)。
> 親レビュー [[topic_savr_vs_tavr_longterm_2026_05]]（RCT＋Inspiris/Avalus/Epic）と、DLリスト [[topic_valve_durability_by_valve_2026_06]] を補完する。
>
> **未取得**：Mosaic 20年（Celiento *J Heart Valve Dis* 2018, DOI非付与誌, PMID 30560605）は今回入手できず。本サマリーは取得11本＋既存レビュー値で構成。

---

## 0. エグゼクティブサマリー — 精読で確定した4つの軸

> [!important]
> **① 耐久性を決める最大因子は「弁種」より「植込み時年齢」**
> Hancock II・Freestyle・Mitroflow・Soprano の4本すべてで、**<60〜65歳 vs >70歳でSVD回避率が劇的に分かれる**。
> 例：Hancock II 20年SVD回避 **<60歳 29.2% vs >70歳 99.8%**／Soprano 15年重度SVD累積 **≤65歳 48.4% vs 全体 22.1%**。
> → 「この弁は何年もつ？」の答えは年齢で全く変わる。**高齢者の長期成績を若年者に外挿してはいけない。**
>
> **② 「最長フォロー年数」は生存者バイアスに汚染される**
> 高齢コホートでは10年生存が Perceval 25.2%・Hancock II（25年で6.7%）と激減するため、**actuarial（カプランマイヤー）とactual（実発生＝競合リスク）でSVD回避率が大きく乖離**する。
> 例：Mitroflow 20年SVD回避 ≥70歳で **actuarial 84.8% vs actual 96.6%**。"何年成績が出ているか"を読むときは必ずこの2値を区別する。
>
> **③ 小弁輪・外付けウシ心膜は早期劣化の地雷**
> **Sorin/LivaNova 外付けウシ心膜系列（Mitroflow → Soprano → Crown PRT）は一貫して早期・高率SVD**、特に19–22mmの小サイズ。Mitroflow 19mmは5年SVD 20%、Soprano 18–22mmはSVD HR 2.31。
>
> **④ Sutureless（Perceval）の中長期耐久性は"従来弁並み"が確立、ただしPPM率に注意**
> Perceval は10年再手術回避 95–97.6%・重度SVD 0.74%/患者年で**従来生体弁と遜色なし**。一方で**ペースメーカー率は初期8–11%**（新サイジング/Plusで4–6%に改善）。Intuityも7年SVD回避97.5%だが**PPI 21.8%@7年と高い**。

---

## 1. マスター比較表（PDF精読・実数値ベース）

| 弁 | 論文 | n | 最長FU | 耐久性の主要値 | 年齢/サイズ依存 | 取得 |
|---|---|---|---|---|---|---|
| **Perceval/S** | Lamberigts 2025（Leuven） | 1,136 | **15年**（中央値7.2y） | 再手術回避 **97.8%@5y / 95.3%@10y**、重度SVD **0.74%/患者年** | 年齢・サイズとも有意差なし（高齢コホート） | ✅ |
| **Perceval** | Concistré 2023（Massa） | 1,157 | **10年**（平均4.5y） | 再介入回避 **97.6%**、SVD実数 **2.4%**（平均5.6年） | 早期oversizing→2017是正 | ✅ |
| **INTUITY** | Malaisrie 2023（TRANSFORM） | 885 | **7年** | SVD回避 **97.5%**、再介入回避95.7%、explant回避97.8% | 層別報告なし／**PPI 21.8%@7y** | ✅ |
| **Magna Ease** | Anselmi 2024（Rennes） | 1,016 | **13.4年**（中央値9.8y） | SVD回避 **96.3%@10y(KM)/97.2%(competing)**、再介入回避97.8%@10y | <65歳でSVD/再手術↑（有意） | ✅ |
| **Hancock II** | David 2010（Toronto） | 1,134 | **25年**（20年が主軸） | 20年SVD回避 全体63.4% / **<60歳29.2% / 60–70歳85.2% / >70歳99.8%** | **年齢が唯一の独立予測因子** | ✅ |
| **Freestyle**（stentless） | Mohammadi 2012（Québec） | 430 | **18年** | SVD再手術回避 **95.9%@10y / 82.3%@15y**（<60歳62.6% vs ≥60歳88.4%@15y, P=0.002） | **age<60: HR 8.2**／劣化様式は弁尖tear 77.8% | ✅ |
| **Mitroflow** ⚠️ | Yankah 2008（Berlin） | 1,513 | **21年** | 20年SVD回避 全体62.3%(actuarial)／**≥70歳 84.8%(actuarial)/96.6%(actual)** | <65歳 SVD 2.1%/患者年 vs ≥70歳0.34% | ✅ |
| **Mitroflow** ⚠️ | Sénage 2014（Nantes） | 617 | 5年 | **5年SVD累積8.4%**、SVD 1.66%/患者年、**33%が加速劣化** | **19mm SVD回避79.8% vs 21mm 94%@5y** | ✅ |
| **Soprano** ⚠️ | Holmgren 2026（瑞典全国） | 1,054 | **17.5年**（15年報告） | 重度SVD累積 **22.1%@15y（全体）/ 48.4%@15y（≤65歳）**、SVD再介入7.2%@10y | **≤65歳 HR 1.95／18–22mm HR 2.31** | ✅ |
| **Crown PRT** ⚠️ | Montero Cruces 2023（BEST-VALVE RCT） | 51 | 5年（6年） | 重度SVD累積 **2.63%@6y**、再介入9.8%@5y、**平均圧較差15mmHg（Magna Easeより有意に高い）** | >80歳が保護因子／Crown自体がSVD独立危険因子 | ✅ |
| **St Jude（機械弁）** | Sawa 2024（東京女子医大） | 519 | **30年** | 心臓死回避 **85.2%@30y**、再手術回避92.6%@30y、**SVDなし（定義上）** | INR 1.6–2.5で塞栓0.35%/患者年・出血0.16%/患者年 | ✅ |
| *Mosaic（porcine）* | *Celiento 2018（未取得）* | *254* | *20年* | *SVD回避96±2%@20y（既存レビュー値）* | *<60歳で劣化↑* | ❌ |

---

## 2. 弁種別ディープダイブ

### A. Sutureless / Rapid-deployment — Perceval・INTUITY

#### A-1. Perceval（最長15年, Lamberigts 2025／10年, Concistré 2023）

> [!success] **要点：Sutureless Percevalの中長期耐久性は"従来生体弁と同等"がほぼ確立。**

**Lamberigts 2025（Leuven 1,136例, 2007–2022, 累積3,775患者年, 中央値FU 7.2年, 最長15年）**
- 再手術回避 **97.8%@5年 / 95.3%@10年**、重度SVD発生率 **0.74%/患者年**（ESC/EACTS/EAPCI基準）
- ViV-TAVR は10例（0.88%）で平均5.4年後に施行 → **将来のViV戦略が現実的**
- **PPM**：退院時 moderate 24.6% / severe 12.3%。ただし **旧サイジング50.1% → 新サイジング32.2% → Perceval Plus 22.1%** と改善
- **PPI（30日）8.1%**（旧11.0% → 新6.1% → Plus 6.8%、XLはPlusで12.8%→4.0%）
- 院内死亡3.4%、5年生存71.1%、**10年生存25.2%**（中央年齢79歳・43%が80歳以上のため生存者バイアス大）

**Concistré 2023（Massa 1,157例, 2011–2021, 平均FU 4.5年）**
- 再介入回避 **97.6%**、構造劣化 **2.4%**（27例：ViV 19・redo 8、平均5.6年）
- 競合リスクでの再手術累積：1年0.1% → 5年1.2% → **10年3.4%**
- 30日死亡 **1.38%**、PPI 4%@30日、平均圧較差 54.4→13.7 mmHg、LV mass 152.8→116.1 g/m²

> [!warning] **Perceval の留保**：両者とも**高齢・後ろ向き・単施設・対照群なし**。VARC基準でないSVD定義。10年生存が低い（25%）ため真の弁耐久性は過小評価の可能性（=実際はもっと持つ）。Perceval Plus（2020〜FREE抗石灰化）の長期データはまだ無い。

#### A-2. INTUITY（最長7年, TRANSFORM, Malaisrie 2023）

- 885例・29施設・前向き単群（NCT01700439）。**SVD回避 97.5%@7年**、再介入回避95.7%、explant回避97.8%
- 血行動態良好：平均圧較差 43.7（術前）→ 11.1 mmHg@7年、EOA 1.6 cm²@7年、moderate以上PVL 0%
- **最大の弱点＝ペースメーカー**：isolated AVRで **PPI 21.8%@7年**（完全房室ブロック単独でも10.9%）。独立予測因子は術前右脚ブロック（OR 7.35）。市販後の経験施設では低下（2年累積10.1%）

> [!warning] **TRANSFORM の留保**：7年到達は**160/885（18%）のみ**と脱落が大きく、長期エコーは101–160例。Akins基準（VARC前）。Edwards社が解析関与。**balloon-expandable frameのためViV不可。**

---

### B. 現行ステント付きウシ心膜 — PERIMOUNT Magna Ease

#### Anselmi 2024（Rennes 1,016例, 2008–2014, 中央値FU 9.8年・最長13.4年, エコー追跡100%）

> [!success] **Magna Ease は10年でSVD回避96–97%。「10–12年の余命の患者に適する」が著者結論。**

- **SVD回避 96.3%±0.8%@10年（KM）/ 97.2%±0.6%（competing risks）**、5年は99.3%
- SVD 28例（2.9%）平均6.9±3.3年（最長12.7年）。SVD再介入 1.5%（redo-SAVR 10・ViV 5）、再介入回避97.8%@10年
- 全生存 83.2%@5年 / **56.8%@10年**、弁関連死回避97.8%@10年
- **PPM**：moderate 26.8% / severe 5.4%（小弁輪多用の施設特性）だが**死亡とは無関係**（P=0.12/0.70）
- **年齢依存**：<65歳でSVD/再手術が有意に高い（余命が長く劣化に到達するため）。サイズ別では小弁輪で圧較差↑だが**弁関連イベント発生率に有意差なし**
- 劣化様式は**石灰化／狭窄が主体**でporcineより早期発生 → 15–20年データで最終評価が必要

---

### C. ブタ弁 — Hancock II（25年）・Freestyle stentless（18年）

#### C-1. Hancock II（David 2010, Toronto 1,134例, 1982–2004, 中央値FU 12.2年・最長25年）

> [!important] **"年齢が全て"を最も鮮明に示すランドマーク。SVDの唯一の独立予測因子は年齢（Cox）。**

| 20年SVD回避 | <60歳 | 60–70歳 | >70歳 | 全体 |
|---|---|---|---|---|
| **値** | **29.2%±5.7%** | **85.2%±3.7%** | **99.8%±0.2%**（18年で打切り） | 63.4%±4.2% |

- 再AVR回避@20年も同様（<60歳29.8% / >70歳98.3%）
- 全生存 19.2%@20年・6.7%@25年（25年は3例のみ）→ **25年は数値的に信頼薄、20年が実質的上限**
- 著者が明記する重要点：**SVD 87例中13例は手術不能で再手術せず** → 「再手術回避」は真のSVD発生を過小評価する（文献で混同されがちな点）
- 血行動態・PPIの報告なし

#### C-2. Freestyle stentless（Mohammadi 2012, Québec 430例, subcoronary, 最長18年, 追跡100%）

- **SVD再手術回避 95.9%@10年 / 82.3%@15年**（全体）
- **年齢で二分**：<60歳 62.6% vs ≥60歳 88.4%@15年（P=0.002）。独立危険因子 **age<60 HR 8.2**、脂質異常症 HR 3.1
- **劣化様式が特徴的**：explant 27例の **77.8%が弁尖tearによる急性ARで発症**（石灰化狭窄は22.2%）。組織は石灰化軽微・ECM変性主体 → porcine stentedとは異なる失敗形態
- 圧較差は15.1（退院）→12.1 mmHg@15年と安定。PPM 36.6%（小弁輪・女性に多い）だが**生存に影響せず**

---

### D. 反面教師 — Sorin/LivaNova 外付けウシ心膜系列（Mitroflow → Soprano → Crown PRT）

> [!danger] **この3弁は系譜的に「外付けウシ心膜」で、いずれも早期・高率SVD（特に小サイズ・若年）。耐久性議論の警告例。**

#### D-1. Mitroflow（Yankah 2008 21年 ＋ Sénage 2014 早期SVD）

- **Yankah（Berlin 1,513例, 最長21年）**：20年SVD回避は **≥70歳 actuarial 84.8%／actual 96.6%** と高齢では良好に見えるが、**全体actuarialは62.3%**。<65歳でSVD 2.1%/患者年（≥70歳0.34%の6倍）
- **Sénage（Nantes 617例, 12A/LX, 抗石灰化処理なし）**：**5年SVD累積8.4%**、SVD 1.66%/患者年、初発14か月。**19mm 5年SVD回避79.8%（≒20%劣化）vs 21mm 94%**。SVDの**33%が加速劣化**（12か月で圧較差22→61 mmHg）。SVDは死亡の最強予測因子 **HR 7.7**
- → 抗石灰化処理の欠如＋外付け設計＋小サイズが重なると破局的

#### D-2. Soprano（Holmgren 2026, スウェーデン全国 1,054例, 最長17.5年）

> [!danger] **新データ（EJCTS 2026）。重度SVD累積は15年で全体22.1%、≤65歳では48.4%。著者は「エコー欠測24%によりむしろ過小評価」と明言。**

- 重度SVD累積（Dvir 2018基準）：5年3.1% → 10年13.7% → **15年22.1%（全体）**／≤65歳は5年7.4% → **15年48.4%**
- SVD再介入累積：**10年7.2%（全体）/ 19.0%（≤65歳）**、15年11.5%/35.1%
- 危険因子（Cox）：**小サイズ18–22mm HR 2.31**、**≤65歳 HR 1.95**、女性 HR 1.42、BMI>30 HR 1.71
- 抗石灰化（homocysteic acid）は現行モデルで既に置換済み。Magna Ease（10年SVD再介入1.9%）より**明確に劣る**、Mitroflow並み

#### D-3. Crown PRT（Montero Cruces 2023, BEST-VALVE RCT, n=51）

- 3弁RCT（Crown PRT vs Magna Ease vs Trifecta）。**重度SVD累積2.63%@6年**だが、**平均圧較差15 mmHg@5年とMagna Ease(12.3)より有意に高い**（P<0.001）、EOA 0.68 cm²
- **Crown PRT自体がSVDの独立危険因子（P=0.001）**、>80歳が保護因子。再介入9.8%@5年
- RCTは2017年に初代Trifecta製造中止で中断（n=396予定→154）。**PRT抗石灰化の長期有効性は5年止まりで未確立**

---

### E. 機械弁 — St Jude（30年）

#### Sawa 2024（東京女子医大 519例, 洞調律・単独AVR, 平均FU 19.9年, 最長30年）

> [!success] **構造劣化（SVD）が定義上なく、30年級の生涯耐久性。低強度INR（1.6–2.5）で塞栓・出血とも低率。**

- 心臓死回避 **100%@5年 → 93.6%@20年 → 85.2%@30年**、再手術回避92.6%@30年（再手術3.7%・0.19%/患者年）
- 全生存 49.9%@30年（平均年齢53歳・若年コホート）
- **塞栓0.35%/患者年・出血0.16%/患者年**、平均INR 2.03。**INR<2.0は心臓死・MACCEの危険因子ではない**（低強度抗凝固が安全）
- 唯一の心臓死危険因子は**70歳以上（HR 6.44）**

> [!warning] **留保**：INR完全データのある519/774例（67%）のみ＝コンプライアンス良好例への選択バイアスで耐久性が良く出る方向。日本人・SJM限定。**ただし「若年で抗凝固許容なら機械弁が生涯耐久性で圧倒」という結論は揺るがない。**

---

## 3. 横断的考察 — この11本から読み取れること

### 3-1. 年齢層別の「実用耐久年数」マップ（SVD回避が概ね>90%を保てる目安）

| 弁 | <60–65歳 | >70歳 |
|---|---|---|
| **機械弁（SJM）** | 生涯（構造劣化なし） | 生涯 |
| **Hancock II（porcine）** | ❌ 20年で29% | ✅ 20年で99.8% |
| **Freestyle（stentless）** | △ 15年で62.6% | ✅ 15年で88.4% |
| **Magna Ease** | △（<65歳で有意に劣化↑） | ✅ 10年で96%超 |
| **Perceval（sutureless）** | データ乏（高齢中心） | ✅ 10年で再手術回避95%超 |
| **INTUITY** | データ乏 | ✅ 7年でSVD回避97.5% |
| **Mitroflow / Soprano / Crown PRT** | ❌❌（19–22mm・若年で破局的） | △（高齢でのみ許容） |

### 3-2. 「最長何年データがあるか」と「その年数で実際もつか」は別問題

- **生存者バイアス**：高齢コホートは10年で60–75%、20年で6–20%しか生存せず、SVDに到達する前に他因死する。よって **actuarial（KM）よりactual（競合リスク）SVD回避が高く出る**（Mitroflow ≥70歳で84.8% vs 96.6%が典型）。
- **若年データこそ弁の真価**：Hancock II <60歳29%・Freestyle <60歳62.6%・Soprano ≤65歳48.4%劣化 が示すように、**長期耐久性の本当の試金石は若年症例**。高齢の好成績を若年に外挿しない。

### 3-3. 「再手術回避 ≠ SVD回避」（David 2010の警告）

SVDを来しても手術不能・患者拒否で再手術しない例が相当数（Hancock 87例中13例、Soprano 206例中49.5%、Sénage 39例中90%）。**「再手術回避率」は真の構造劣化を大きく過小評価する**。弁間比較ではエンドポイント定義（actuarial SVD vs reintervention）を必ず確認する。

### 3-4. 弁選択への含意（2026年6月・本11本ベース）

> [!important]
> - **<60–65歳・抗凝固許容 → 機械弁（SJM/On-X, 低強度INRで安全・生涯耐久）**
> - **<65歳・生体弁希望 → Magna Ease/Inspiris等の現行ステント付きウシ心膜、将来ViV前提**。porcine単独（Hancock II/Mosaic）やstentless Freestyleは若年でSVD早い
> - **高齢・低侵襲/小弁輪 → Perceval/INTUITY（耐久性は10年級で従来弁並み、ただしPPM/PPIに留意）**
> - **避ける → Mitroflow全般・Soprano・Crown PRT（外付けウシ心膜系列、特に19–22mm・若年）。Trifecta初代も同様（cusp tear）**

---

## 4. 取得状況と限界

- **取得・精読済（11本）**：[valve_durability/pdf/](../valve_durability/pdf/) に格納、テキスト [valve_durability/pdf_text/](../valve_durability/pdf_text/)
- **未取得（1本）**：Mosaic 20年（Celiento *J Heart Valve Dis* 2018）はDOI非付与誌で今回入手できず。porcine 20年データとして価値があり、PMID 30560605 で別途取得推奨
- **DLリスト値からの訂正**（PDF精読で確定）：
  - **Soprano**：最長「14年」→ **17.5年（15年エンドポイント報告）**、重度SVD「19.5%@8.6年（粗率）」→ **累積22.1%@15年（全体）/48.4%@15年（≤65歳）**
  - **Magna Ease**：10年SVD回避「96.5%」→ **96.3%（KM）/97.2%（competing risks）**
  - **Freestyle**：取得論文は Mohammadi 2012（Québec単施設n=430, subcoronary）。Bach 2014（多施設）は別論文
- **横断比較の注意**：SVD定義が論文間で不統一（Akins/EAPCI/VARC-2/VARC-3/Dvir 2018）、actuarial vs actual混在、単施設・後ろ向き多数。**直接の弁間比較は同一基準のRCT（例：BEST-VALVE）以外は慎重に。**

---

*作成: 2026-06-09 ／ 親: [[topic_savr_vs_tavr_longterm_2026_05]] ／ DLリスト: [[topic_valve_durability_by_valve_2026_06]]*
*データソース: 取得PDF全文（pdftotext）→ 11並列抽出エージェント。数値はPDF本文から逐語抽出・構造化*
