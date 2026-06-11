---
title: "The fallacy of indexed effective orifice area charts to predict prosthesis-patient mismatch after prosthesis implantation"
authors: "Bilkhu R, Borger MA, Briffa NP, Jahangiri M, Pibarot P, Dahou A, Hahn RT et al."
journal: "European Heart Journal — Cardiovascular Imaging"
citation: "Eur Heart J Cardiovasc Imaging 2020 Oct 1;21(10):1115-1123"
doi: "10.1093/ehjci/jeaa092"
pmid: "32243493"
pmcid: "PMC7971169"
pdf: "[[（PDF binary 未取得：PMC HTML フルテキストから抽出 2026-05-17）]]"
tags:
  - small-annulus
  - ppm
  - reference-eoa
  - methodology-critique
  - fallacy
  - measured-vs-projected
date: 2026-05-17
category: "PPM"
journal-abbr: "EHJ Cardiovasc Imaging"
paper-type: "methodology-critique"
annulus-size: "mixed"
patient-bsa: "mixed"
valve-type: "bioprosthetic + mechanical (各サイズ)"
enlargement-technique: NA
asian-cohort: no
ppm-rate: "誤分類 30% (any PPM) / 22% (severe PPM)"
viv-discussion: no
sample-size: "n=494 (test set)"
follow-up: "in-hospital + discharge echo"
source-note: "PMC HTML フルテキスト経由抽出"
---

> [!NOTE] Key Message
> **Pibarot 本人を含む著者陣による、Pibarot 2006 Table 3 型 reference EOA chart approach の自己否定論文**。Test set 494 例で **projected iEOA 値 vs measured iEOA 値の相関 r = 0.50（弱）**、**PPM 誤分類率 30%（severe PPM 22%）**。結論: 「**EOAi charts should not be used by surgeons and cardiologists to predict PPM**」。本研究 RQ の核心—弁選択ガイドの方法論—に根本的修正を要求する critical paper。

---

## 1. 背景・問題設定

Pibarot 2000 JACC / 2006 Heart で確立された **projected iEOA = reference EOA / patient BSA** approach は世界的に普及（Edwards/Medtronic/Abbott の IFU、各国ガイドライン、Society 推奨文すべてに反映）。**Yang B JTCVS 2024 Y-incision 論文** も「standard SAVR で projected PPM 30-50%」という根拠でこのアプローチを使う。

しかし 2010 年代に蓄積した **post-implant Doppler measured EOA registry data** で、**reference EOA 値と patient 個別 measured EOA の乖離が大きい**ことが分かってきた。本論文は **prospective valve registry で projected iEOA charts の予測精度を直接測定** した検証研究。

## 2. 患者集団 / 方法

- Test set: **n=494**（多施設 prospective valve registry）
- 弁種: bioprosthetic + mechanical 混合、19-29mm 全サイズ
- Projected iEOA: 各弁モデル × サイズの **published reference EOA** (Pibarot 2000/2006 系列) / patient BSA
- Measured iEOA: **post-implant 1-3 month echocardiography** で **continuity equation** より計算
- PPM 分類: Pibarot cutoff (severe ≤0.65, moderate 0.65-0.85, none >0.85)
- 比較: projected vs measured で PPM 分類が一致するか

## 3. 手法詳細

### Projected iEOA chart の典型例
弁モデル 21mm Magna Ease: reference EOA = 1.30 cm² (Pibarot 2006 Table 3 / Edwards IFU)
患者 BSA 1.80 m² → projected iEOA = 1.30/1.80 = **0.72 → moderate PPM**

### Measured iEOA
同じ患者で post-op echo → measured EOA 1.05 cm² → measured iEOA = 1.05/1.80 = **0.58 → severe PPM**

→ **projected = moderate なのに measured = severe**、つまり projected chart は楽観的方向に誤分類

## 4. アウトカム（中核データ）

### 予測精度

| Metric | Any PPM 予測 | Severe PPM 予測 |
|---|---|---|
| Sensitivity | 87% | 13% |
| **Specificity** | **37%** | 98% |
| **Misclassification rate** | **30%** | **22%** |
| False positives | 106/494 (21%) | 6/494 (1%) |
| False negatives | 42/494 (9%) | 105/494 (21%) |

### 相関

| 指標 | 値 |
|---|---|
| **Projected vs measured iEOA 相関 r** | **0.50（弱）** |
| 30% の patient で reference と measured EOA の差が PPM 分類変更レベル |  |

### Size 別精度（**注目**）

| Valve size | Misclassification 率 |
|---|---|
| 19mm | **5%（良好）** |
| 21mm | 中程度 |
| 23mm | 中程度 |
| 25mm | 中程度 |
| **27mm** | **42%（最悪）** |

→ **小弁輪では projected chart は意外と当たる、大弁輪では大きく外れる**。19mm valve 議論には projected chart が比較的有用、しかし 25mm 以上の "AAE で大型化" 戦略の妥当性評価には projected chart は無効。

## 5. 議論ポイント

### Reference EOA の何が問題か

1. **In vitro vs in vivo の乖離**: manufacturer IFU 値は in-vitro が多く、in-vivo より 0.1-0.3 cm² 高い
2. **Patient-specific factors**: annulus calcium 残存、suture line 緊張、leaflet pinning、root geometry 個別差
3. **Reference 値は cohort 中央値**: ±SD 0.1-0.3 cm² の variance を抱え、個別予測には不十分

### 著者推奨

> "**EOAi charts should not be used by surgeons and cardiologists to predict PPM in individual patients before surgery.**"

代替:
1. **Measured EOA from post-implant TTE** を使う（術後検証）
2. PPM 予防は **valve type 全体傾向**（Trifecta/Regent > Magna > Avalus > Mosaic 等の rank）の参考程度
3. 個別患者では **annulus size, BSA, 弁種 全体傾向、surgical 技術** の総合判断

### Yang Y-incision 戦略への含意（**最重要**）

**Yang B "5 Misconceptions" (2026)** の論法は:
- standard SAVR で projected PPM 30-50%
- AAE で 0% (measured)

これを本論文の方法論で再評価すると:
- **standard SAVR の 30-50% は projected で計算**、ところが本論文は projected が **30% 誤分類** → 実 measured PPM 率は **15-50% の幅** の可能性
- **AAE 0% は measured**（Yang コホート core lab echo）→ 信頼性高
- つまり **「30-50% → 0%」という差分の半分は projected の overestimate 由来の可能性**

→ **Yang argument の definitive 強度は本論文で弱体化**。AAE の優位性は依然示唆されるが、"projected PPM 30%" を rhetorical な根拠に使うことは methodological に脆弱。

## 6. 本研究 RQ への含意

### Primary RQ (狭小弁輪+AAE vs no AAE vs TAVI)

**Reference chart で AAE の利益を主張する根拠は弱体化**。AAE-SAVR の妥当性評価は **measured PPM 値（registry 報告）** を直接使うべき。

### Secondary RQ (19mm 弁許容性)

**19mm size では projected chart の misclassification 率 5% と最も低い** ので、本領域の議論には projected approach がまだ使える。**「BSA 1.34 日本人女性に 19mm Inspiris → moderate PPM 予想」は projected chart で計算してもおおむね信頼可能**。

### Tertiary RQ (Asian-specific 戦略)

Pibarot 2020 cohort は欧米中心。**Asian BSA 1.3 m² cohort での chart 妥当性は別検証必要**。日本人の小弁輪 + 19mm Inspiris/Avalus に対する projected chart の予測精度は **未検証** で、JaCVSD / OCEAN-TAVI 級の日本 registry が必要。

## 7. 限界

- Test set 494 は適度なサイズだが prospective single cohort
- BSA 範囲（≤1.5 m² Asian, ≥2.2 m² obese）の extreme は test set に少数しか含まれない
- Long-term clinical outcome correlation は本論文の scope 外（PPM 分類精度のみ）
- 著者陣に Pibarot 含む → self-critique の strong evidence、ただし bias 完全排除ではない
- ViV-TAVR sizing への chart application は本論文の scope 外

## 8. 引用文献ハイライト

- Pibarot P, Dumesnil JG. **Heart 2006;92:1022-9** （本論文の批判対象、当ディレクトリ [[Pibarot_PPMDefinitionClinicalImpactPrevention_Heart_2006]]）
- Bilkhu R et al. **Eur J Cardiothorac Surg 2017** (small annulus PPM)
- Head SJ et al. **EHJ 2012;33:1518-29** (meta、当ディレクトリ [[Head_PPMLongTermSurvivalMeta_EHJ_2012]])
- Genereux P et al. **VARC-3 consensus, JACC 2021** (TAVI/SAVR endpoint 標準化)

---

*作成: 2026-05-17 | PDF 入手: PMC HTML フルテキスト経由 (PMID 32243493, PMCID PMC7971169) | 関連: [[_index]] | [[tables/modern_valve_eoa_reference]] | [[Pibarot_PPMDefinitionClinicalImpactPrevention_Heart_2006]] | [[Pibarot_PPMHemodynamicClinical_JACC_2000]]*
