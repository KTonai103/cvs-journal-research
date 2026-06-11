---
title: "Sensitivity Analysis in Observational Research: Introducing the E-Value"
authors: "Tyler J. VanderWeele, Peng Ding"
journal: "Annals of Internal Medicine"
citation: "Ann Intern Med 2017;167(4):268-274"
doi: "10.7326/M16-2607"
pmid: "28693043"
pdf: "[[small_annulus_avr/Reference/CatJ_Methods/VanderWeele_EValueSensitivityAnalysis_AnnInternMed_2017.pdf]]"
tags:
  - small-annulus
  - savr
  - methodology
  - e-value
  - unmeasured-confounding
  - sensitivity-analysis
  - anninternmed
date: 2026-06-11
category: "方法論"
journal-abbr: "AnnInternMed"
paper-type: "methods"
annulus-size: "n/a"
patient-bsa: "n/a"
valve-type: "n/a"
enlargement-technique: "n/a"
asian-cohort: "no"
ppm-rate: "n/a"
viv-discussion: "no"
sample-size: "n/a"
follow-up: "n/a"
---

> [!NOTE] Key Message
> 観察研究で「未測定交絡（unmeasured confounding）」がどれだけ強ければ観察された関連を完全に説明し尽くせるかを、**リスク比スケール上の最小の関連強度**として表す指標 **E-value** を提唱した原著チュートリアル。RR>1 の場合、**E-value = RR + √{RR×(RR−1)}** で手計算できる。点推定値だけでなく**帰無側に最も近い信頼区間の限界**についても E-value を報告すべきとする。例：RR=3.9（95%CI 1.8–8.7）→ 点推定の E-value=7.2、CI下限の E-value=3.0（=未測定交絡が曝露・アウトカム両方とRR 3.0倍以上で関連しないと帰無に戻せない）。E-value が大きいほど因果性の頑健性が高い。閾値（カットオフ）は設けず、p値と同様に連続指標として併記すべきと主張。

---

## 1. 背景・目的

- 観察データでは association ≠ causation が常に問題で、中心的脅威は**未測定・未制御交絡**（測定共変量で調整しても残る、曝露とアウトカム双方に関連する第3因子）。
- 従来の感度分析（sensitivity analysis / bias analysis）は批判されてきた：(1) 感度パラメータを研究者が恣意的に選べる（結果が頑健に見えるよう選択可能）、(2) 未測定交絡子が「二値」「単一」「交互作用なし」等の単純化仮定を要する。
- 本論文は **Ding & VanderWeele (Epidemiology 2016, 文献37) の「仮定を置かない感度分析（sensitivity analysis without assumptions）」** に基づき、未測定交絡子の数・分布・型に仮定を置かず計算できる新指標 **E-value** を導入。「すべての因果性を主張する観察研究で E-value（または他の感度分析）を報告すべき」と提言する。
- E-value は **Bradford Hill の "strength of association" 基準**を定量化したものと位置づけられる。

## 2. 中身（定義・手順・閾値＝SAKURAで引用する具体値）

**【定義】** E-value とは「測定共変量で調整した上で、観察された曝露–アウトカム関連を**完全に説明し尽くす（explain away）**ために、未測定交絡子が**曝露とアウトカムの両方**と持たねばならない、**リスク比スケール上の最小の関連強度**」。

**【bias factor B（背景式）】** 未測定交絡子 U について
- RRUD = U とアウトカムDの最大リスク比（U がアウトカムにとってどれだけ重要か）
- RREU = 曝露群間で U がどれだけ偏っているか（例：非授乳母40%喫煙 vs 授乳母20%喫煙 → RREU=2）
- 観察RRを下げ得る最大バイアス：**B = RRUD × RREU / (RRUD + RREU − 1)**
- 真の効果の下限は観察RRをBで割って得る（RR<1なら掛ける）。

**【E-value 公式（RR>1）】**
- **E-value = RR + √{RR×(RR−1)}**
- 導出：B式で RRUD=RREU=E と置き B=RR を解く → E²−2·RR·E+RR=0 の正の解。
- RR<1（保護的）の場合：まず逆数 RR*=1/RR をとってから公式適用。

**【信頼区間の E-value】（Table 1）**
- 下限LL：LL≤1 なら E-value=1（交絡不要）／LL>1 なら LL+√{LL×(LL−1)}
- 上限UL（RR<1側）：UL≥1 なら E-value=1／UL<1 なら UL*=1/UL として公式適用
- **CIが帰無（RR=1）を含む場合、CIのE-valueは自動的に1**。

**【数値例（本文）】**

| 例 | 効果指標 | 点推定E-value | CI限界E-value |
|---|---|---|---|
| 授乳 vs 呼吸器死 (Victora) | RR=3.9 (1.8,8.7) | **7.2** | 3.0 (LL=1.8から) |
| 授乳 vs 小児白血病 (AHRQ) | RR=0.80 (0.71,0.91) | 1.8 | 1.4 (UL側) |
| 授乳 vs 卵巣癌 (Moorman) | OR=0.5 (0.3,0.8) | 3.4 | 1.8 |

**【他の効果指標への変換】（Table 2）**
- **Rare outcome（<15%）のOR/HR**：そのままTable 1の公式に代入可。
- **Common outcome（>15%）のOR**：**RR ≈ √OR** で近似してから公式（例：OR=1.47→RR≈1.21→E-value=1.71、CI下限1.06→1.31）。
- **Common outcome の HR**：RR ≈ (1−0.5√HR)/(1−0.5√(1/HR)) で近似。
- **Rate ratio（count/連続）**：リスク比をrate ratioに置換。
- **連続アウトカムの標準化効果量 d**：RR ≈ exp(0.91×d)、CI=exp{0.91d ± 1.78sd}（例：d=−0.42→RR≈1.46→E-value=2.28）。
- **Risk difference**：p1/p0 を代入（CIはR関数 `evaluesRD()` で計算、付録に提供）。

**【解釈上の重要ポイント】（Table 3／Discussion）**
- E-valueの最小値は1（=交絡不要で説明できる＝頑健性ゼロ）。大きいほど頑健。
- **閾値・カットオフは設けない**。p値の0.05のような恣意的基準の弊害を避けるため、連続指標として扱う。
- E-valueは**調整した測定共変量の文脈に依存**：同じE-value=2.5でも、多数のSES指標を調整した研究の方が単一指標のみの研究より頑健（「上乗せ」の意味が異なる）。
- **p値とE-valueは別概念**：p値は標本サイズに依存し大標本で任意に小さくできるが、E-valueは関連の大きさに依存し標本サイズで任意に大きくできない（CIのE-valueは標本依存だが上限は関連の強さで頭打ち＝"design sensitivity"）。両方を併記すべき。
- E-valueは未測定交絡のみを扱い、**測定誤差・選択バイアス・欠測・選択的報告は評価しない**。
- 小さいE-value＝「効果がない証拠」ではなく「効果の証拠が弱い」だけ（absence of evidence ≠ evidence of absence）。
- 非帰無E-value：RR/RRT の比に公式を適用すれば、推定値を任意の値RRTへ動かすのに必要な交絡強度も算出可。

## 3. 本研究での使い方（SAKURA-AVRでの採用・§対応）

SAKURA-AVRは**後ろ向き観察コホート**であり、Arm1（no-AAE SAVR）vs Arm2（AAE-SAVR）の主要比較を **PSM/IPTW** で行う。PSMで観察可能な共変量はバランスできても、**未測定交絡（術者の選好・解剖学的微差・施設方針・フレイルティ等）の残存リスクは原理的に消えない**。E-valueはまさにこの残存未測定交絡への頑健性を定量化するために、プロトコルで**STROBE・VARC-3・多重代入とともに前指定された感度分析**である。

- **どの解析に**：PSM/IPTWで調整後の主要効果推定値（co-primary：severe PPM、1年平均圧較差／key secondary：中期生存・MACE）について、**点推定値と帰無側CI限界の双方にE-valueを算出**して報告する。HR/RR（rare outcome なら直接、common outcome の OR/HR は §2 の近似変換）を用いる。
- **報告様式**：本文Key Pointsのテンプレート文（「観察されたHR=X.Xに対し、曝露・アウトカム両方とRR E.E倍ずつで関連する未測定交絡があれば説明し尽くせるが、それより弱い交絡では不可。CIを帰無に動かすにはRR e.e倍ずつが必要」）をそのまま投稿原稿の感度分析パラグラフに使う。
- **解釈の文脈づけ**：SAKURAでは年齢・BSA・LVEF・併存症など主要交絡を調整済みであることを明記し、「測定共変量を上乗せした上での最小交絡強度」であることを強調（§2の文脈依存性に対応）。E-valueが2–3倍を超えれば、Asian small-bodyコホートで未測定交絡がそれほど強い因子を想定しにくく、因果的解釈が補強される。
- **閾値を設けない方針の踏襲**：E-valueに合否基準は設けず、p値・効果量と並置して総合的に頑健性を論じる（査読での恣意的閾値要求を避ける根拠にもなる）。

## 4. 注意点

- E-valueは**未測定交絡のみ**を対象。SAKURAで別途問題となる**測定誤差（measured EOA / annulus径の測定）・選択バイアス・欠測（多重代入で対処）**は別個に議論が必要。
- common outcome（>15%）の OR/HR は **√OR 近似・HR近似**を用いるため、アウトカム確率が0.1–0.9（理想は0.2–0.8）で良好に機能する近似であることを脚注する。SAKURAの severe PPM・MACE 等は頻度が高くなり得るため近似の前提を確認。
- E-valueは「ある強度の交絡が存在すれば必ず効果を説明し尽くす」ことを保証せず、「**そういうシナリオを構築可能**」を示すのみ。希少な未測定交絡子はそこまでバイアスを生まない。
- 小さいE-value（弱い頑健性）でも研究を不採択にする理由にはならない（観察データで可能な最善の場合がある）。逆に大きいE-valueも他の限界（デザイン・バイアス源）と併せて解釈すべき。
- 計算は手計算可（RD のCIのみR関数 `evaluesRD()` が必要）。

---

## 引用ハイライト

- 定義：「The E-value is the minimum strength of association on the risk ratio scale that an unmeasured confounder would need to have with both the treatment and the outcome, conditional on the measured covariates, to fully explain away a specific treatment-outcome association.」
- 公式：「E-value = RR + sqrt{RR×(RR−1)}」（RR>1）。RR<1 はまず逆数をとる。
- 推奨：「we suggest calculating the E-value for both the observed association estimate ... and for the limit of the confidence interval closest to the null.」
- 閾値否定：「We do not propose any threshold cut-off for the E-value. ... The E-value, like the p-value, is a continuous measure.」
- 限界：「unmeasured confounding is not the only source of potential bias ... measurement error, selection bias, and missing data must also be carefully considered.」
