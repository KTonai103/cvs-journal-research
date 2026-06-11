---
title: "Balance diagnostics for comparing the distribution of baseline covariates between treatment groups in propensity-score matched samples"
authors: "Peter C. Austin"
journal: "Statistics in Medicine"
citation: "Stat Med 2009;28(25):3083-3107"
doi: "10.1002/sim.3697"
pmid: "19757444"
pdf: "[[small_annulus_avr/Reference/CatJ_Methods/Austin_PSMbalanceDiagnostics_StatMed_2009.pdf]]"
tags:
  - small-annulus
  - savr
  - methodology
  - propensity-score
  - standardized-difference
  - balance-diagnostics
  - statmed
date: 2026-06-11
category: "方法論"
journal-abbr: "StatMed"
paper-type: "methods"
annulus-size: "n/a"
patient-bsa: "n/a"
valve-type: "n/a"
enlargement-technique: "n/a"
asian-cohort: "no"
ppm-rate: "n/a"
viv-discussion: "no"
sample-size: "n=9104 (AMI cohort; matched n=2430 pairs)"
follow-up: "n/a"
---

> [!NOTE] Key Message
> **PSM後の群間バランスを評価する診断法の決定版（最多引用の方法論論文）**。中心指標は **標準化差 (standardized difference, SMD)** で、p値・有意検定に依存せず（サンプルサイズに非依存）、**SMD>0.1（10%）を意味のある残存不均衡の閾値**とする慣行を確立した。ただし本論文の主張は「平均のバランスだけでは不十分」で、**分散比（F分布の2.5/97.5%点=2429自由度で0.92–1.08）、five-number summary、Q-Qプロット・密度プロット、交互作用項のSMD**を併用すべきとする。実データ（Ontario AMI 9104例、スタチン処方をexposureにPSM後 2430 matched pairs）では全SMD≤0.030だが、分散比は6/11変数で閾値を逸脱し、平均では見えない不均衡を検出した。**傾向スコア分布の比較やc統計量（ROC面積）はモデル誤特定を検出できず不適**と明示。

---

## 1. 背景・目的

- 傾向スコア (propensity score, PS) = 観測共変量で条件づけた治療確率。**真のPSで条件づければ治療群・非治療群の観測共変量分布は等しくなる**（balancing score; Rosenbaum & Rubin 1983）。
- PSの利用法は4つ（共変量調整・層別化・**マッチング**・IPTW）で、本論文はPSマッチング（最頻実装=1:1）に焦点。
- マッチング後の因果推論が妥当なのは、マッチング後標本で両群の観測共変量分布が類似している場合のみ。Ho et al. の "propensity-score tautology"＝「生の共変量がバランスしたとき、PSを正しく推定できたとわかる」を採用。
- **目的**: ①PSマッチング後のバランス評価法を一論文に集約、②モデル特定の妥当性を評価する枠組み提示、③従来法（PS分布比較・有意検定・ROC面積）の限界を明示。

## 2. 中身（定義・手順・閾値＝SAKURAで引用する具体値）

### 2-1. 標準化差 (standardized difference / SMD) — 中核指標
- 連続変数: `d = (x̄_treat − x̄_control) / √[(s²_treat + s²_control)/2]`（プールSDで割った平均差）。
- 二値変数: `d = (p̂_treat − p̂_control) / √[(p̂_t(1−p̂_t) + p̂_c(1−p̂_c))/2]`。
- **t検定等と異なりサンプルサイズに非依存**→マッチ前後・異なる単位の変数間でバランスを比較可能。
- 起源は心理学の **Cohen's Effect Size Index**（0.2/0.5/0.8 = small/medium/large）。
- **閾値: SMD=0.1（10%）を「意味のある不均衡」とする提案（Normand 2001を引用）**。本論文自身は「閾値は共変量の予後重要度に依存しうる」と留保（明確なコンセンサスは無いと明記）。
- d=0.10のとき2群分布の非重複は7.7%（Cohenの U1）。d=0.10で群所属が共変量分散の0.25%を説明するのみ。

### 2-2. SMDのサンプリング分布（許容範囲の決め方）
- 真のSMD=0かつ両群同数nのとき、SMDの分散=2/n、SD=√(2/n)。95%の標本で推定SMDは **±1.96·√(2/n)** に入る。
- マッチングは独立性を壊す（マッチ対は相関）ため、**ペア内値の置換によるリサンプリング（1000回反復）で帰無分布を経験的に導出**することを提案。
- 実データ: 年齢のSMD帰無分布SD=0.017（2.5–97.5%点≈±0.033）、他の連続10変数はSD 0.024–0.029（≈±0.047〜0.057）。二値変数も概ね±0.051〜0.057。→Table IIの全SMD（最大0.030）は帰無範囲内＝モデル誤特定の証拠なし。
- **バランスは大標本特性**: matched pair=100ではhemoglobinのSMD許容域が±0.234、200で±0.166。小標本では0.20超のSMDでも正しいモデルと整合しうる。

### 2-3. 平均のバランスだけでは不十分（Monte Carlo 3シナリオ）
- 真のPSが2次項/交互作用を含むとき、誤特定モデルでも**平均はバランスする**が交絡バイアスは残る。
- Scenario B（X3=X1·X2の交互作用）: X3のSMDは誤特定0.45→正特定0.05、X3分散比0.46→1.08。治療効果バイアス（差Y）0.35→0.02。
- 結論: **「主効果の平均がバランス」≠「バイアス除去」**。分散比・交互作用も見るべき。

### 2-4. 分散比 (variance ratio)
- 連続変数の treated/untreated 分散比＝2次モーメントの比較。等分散ならF分布。
- **2430 matched pairsのF分布(自由度2429,2429)の2.5/97.5%点＝0.92–1.08**を目安。
- 実データ: 11連続変数中 **6変数が閾値外**（最も極端なのはsodium 0.77）。平均SMDでは見えない不均衡を検出。
- 6連続変数にrestricted cubic splineを導入しPS再構築→分散比10/11変数が0.93–1.03に改善（sodium 0.91のみ例外）。

### 2-5. その他の分布比較法
- **Five-number summary**（min/Q1/median/Q3/max）: 分布の粗い質的比較。ただし許容変動量を定量できない限界。
- **グラフィカル法**: side-by-side boxplot、Q-Qプロット、経験累積分布(ECDF)、ノンパラ密度プロット。年齢の上位裾の残差を検出（平均比較では隠れる）。
- **交互作用項のSMD**: 11連続×11=55の2変数交互作用→SMD 0.0003–0.0274（中央値0.0098）。13二値の78組（3つ未定義→75組）→0–0.048。連続×二値143組→0.000–0.036（中央値0.003）。全て無視できる不均衡。

### 2-6. 使ってはいけない/限界のある従来法
- **推定PS分布の群間比較（boxplot/ECDF/Q-Q）は無情報**: 誤特定モデルでもPS分布は両群でほぼ同一になりうる（共変量がバランスしていないのに）。重複(overlap)確認には有用だが特定の妥当性判定には不可。
- **有意検定は不適（Imai et al.）**: ①マッチ後はサンプルサイズ減でパワー低下→balance改善が見かけ上、②balanceは標本の性質で超母集団に言及しない。本論文の全推奨指標はサンプルサイズ非依存・検定非依存。
- **c統計量/ROC面積は誤特定を検出できない**: Scenario Bで誤特定0.81 vs 正特定0.83、Scenario Cで0.820 vs 0.826とほぼ不変。

### 2-7. 推奨ワークフロー（要約）
1. 連続変数の平均・カテゴリ変数の頻度を表で記述。
2. 平均・有病率のSMDを報告（マッチ前後）。
3. 連続変数の分散比（または2乗項のSMD＝2次モーメント）を比較。
4. 2変数交互作用の平均を比較。
5. 予後重要変数のQ-Qプロット。
6. PS分布比較は限定的価値と認識。
（多対1マッチングへはサンプル重み導入で拡張可。）

## 3. 本研究での使い方（SAKURA-AVR §対応）

SAKURA-AVR は **measured annulus ≤23mm（≤21mm primary stratum）のアジア人小柄AS患者で Arm1 no-AAE SAVR vs Arm2 AAE-SAVR を PSM/IPTW で比較**するretrospective cohort。本論文は **Methods §（PSM/IPTW・バランス評価）の引用根拠そのもの**。

- **Primary RQ（AAE-SAVR vs no-AAE SAVRの優劣）の交絡調整の妥当性検証**: PSMで両アームをマッチした後、**全共変量のSMD<0.1**を「バランス達成」の規準として報告する根拠としてこの論文を引用（§統計手法）。Co-primary（severe PPM by measured iEOA ≤0.65 cm²/m²、1年平均圧較差）の群間比較がバイアスフリーであることの担保。
- **TAVI reference arm との比較でも同じバランス表**: AAE-SAVR vs TAVI のPSM/IPTW後にSMDテーブル（Love plot 形式; Fig.1）とE-value（別途）を併記。
- **分散比・交互作用の確認を補助診断として記載**: 本論文の核心メッセージ「平均SMDのみでは不十分」を受け、SAKURAでも主要予後共変量（年齢・BSA・annulus径・EF）について**分散比0.92–1.08 目安**または2乗項SMDを副次的に確認することを推奨（§Sensitivity/Methods）。
- **小標本警告**: SAKURAは小柄アジア人・≤21mm primary stratumで**マッチ対数が小さくなりうる**。本論文の「バランスは大標本特性／matched pair=100で±0.234」を引用し、層別解析で残存SMDが閾値を超えてもモデル誤特定とは限らない点・必要なら回帰での残差調整を行う点を方法論的根拠とする。
- **やってはいけない事の根拠**: 「マッチ後の有意検定でバランス主張」「c統計量でモデル妥当性主張」「PS分布の重なりだけでバランス主張」を避ける根拠として引用（査読対応・STROBE準拠）。

## 4. 注意点

- **SMD<0.1は便宜的閾値**であり絶対基準ではない（本論文は「コンセンサスなし」「予後重要度依存」と明記）。小標本では0.10–0.25のSMDでも正しいモデルと整合しうるため、機械的に「全SMD<0.1で合格」と書くと過剰主張になる。経験的サンプリング分布（リサンプリング）で群サイズに応じた許容域を示すのが本論文の本来の主張。
- **平均のバランス＝バイアス除去ではない**。SAKURAでは分散比・交互作用・分布形（Q-Q）まで確認しないと、2次項・交互作用に起因する残存交絡を見落とす。
- 本論文は **1:1マッチング** を前提（多対1はサンプル重みで拡張）。IPTWのバランス評価には別法（weighted SMD等）が必要で、本論文だけでIPTWアームを完全には正当化できない。
- 残存不均衡があれば**マッチ後標本内での回帰調整**が選択肢だが、二値/time-to-event アウトカムでは marginal と conditional の治療効果が一致しない点に注意（連続アウトカム＋線形効果のときのみ一致）。SAKURAのMACE/生存（time-to-event）では効果尺度の解釈に留意。
- データは Ontario AMI（スタチン処方をexposure）で、心臓外科・弁膜症・アジア人とは無関係（方法論の例示用）。**数値（SMD閾値0.1、分散比0.92–1.08、Cohen 0.2/0.5/0.8）のみを引用し、臨床数値は引用しない**こと。
