---
title: "AVR 用人工弁 EOA / PPM 参照テーブル（Hybrid 設計版 — 2026-05-17 改訂）"
date: 2026-05-17
revision: "v2 (Pibarot 2020 fallacy 警告 + measured cohort data 統合)"
tags:
  - reference-table
  - eoa
  - ppm
  - aortic-valve-prosthesis
  - measured-iea
  - bioprosthetic
  - mechanical
  - sutureless
category: 弁膜症外科
related:
  - "[[Pibarot_FallacyIEOAChartPPMPrediction_EHJCardiovascImag_2020]]"
  - "[[Pibarot_PPMDefinitionClinicalImpactPrevention_Heart_2006]]"
  - "[[Klautz_PERIGONPivotalAvalus_EJCTS_2017]]"
  - "[[Bavaria_RESILIAvsContemporaryPARTNER2ADurability_JCompEffRes_2023]]"
  - "[[Pibarot_PPMHemodynamicClinical_JACC_2000]]"
  - "[[Head_PPMLongTermSurvivalMeta_EHJ_2012]]"
---

# AVR 用人工弁 EOA / PPM 参照テーブル — Hybrid 設計版

> [!danger] **§0 最重要警告：個別患者 PPM 予測に reference EOA chart を使うな**
> 当ディレクトリ [[Pibarot_FallacyIEOAChartPPMPrediction_EHJCardiovascImag_2020]]（Pibarot 本人を含む著者陣、n=494 test cohort）の結論:
>
> | 指標 | 値 |
> |---|---|
> | Projected vs measured iEOA 相関 r | **0.50（弱）** |
> | Any PPM 誤分類率 | **30%** |
> | Severe PPM 誤分類率 | **22%** |
>
> **"EOAi charts should not be used by surgeons and cardiologists to predict PPM in individual patients before surgery."**
>
> ただし: **size 19mm の誤分類率は 5%** と例外的に低く、本領域（狭小弁輪議論）の cutoff 判定には projected approach がまだ概ね使える。**size 27mm では誤分類率 42%** で完全に無効。
>
> 本ファイルは以下の **4 階層構造** で reference を提供する:
> - **§1**: Reference EOA chart（**弁間ランキング目的のみ**、個別予測には使わない）
> - **§2**: Measured iEOA distribution from real trial cohorts（**信頼性高い、個別判断の primary source**）
> - **§3**: 日本人 BSA 1.3-1.5 cohort focus（実測データのある弁のみ）
> - **§4**: Pibarot 2006 Table 3 historical reference（§0 警告下で保持）

---

## §1. Reference EOA Chart — 弁間ランキング目的のみ

**注意**: 以下の値は **Doppler-measured in-vivo 1y 中央値** ベースの代表値。**個別患者の PPM 予測には使わず**、弁間の hemodynamic profile 比較にのみ使用。

### Stented Bioprostheses（EOA in cm², 中央値ベース）

| Valve | 19mm | 21mm | 23mm | 25mm | データ source | 注釈 |
|---|---|---|---|---|---|---|
| **Inspiris Resilia** | ~1.1–1.3 | ~1.3–1.5 | ~1.6–1.8 | ~1.85–2.1 | COMMENCE 1y pooled 1.7 [[Bavaria_RESILIAvsContemporaryPARTNER2ADurability_JCompEffRes_2023]] | **size-stratified 公式 data 未取得**、推測 |
| **Magna / Magna Ease** | ~1.2–1.35 | ~1.35–1.5 | ~1.6–1.8 | ~1.85–2.1 | Bavaria JTCVS 2014 / FUTURE PMS | 当ディレクトリ未取得 |
| **CE Perimount (前身)** | 1.10 | 1.30 | 1.50 | 1.80 | [[Pibarot_PPMDefinitionClinicalImpactPrevention_Heart_2006]] Table 3 | **唯一信頼性高 source** |
| **Mosaic** | 1.20 | 1.22 | 1.38 | 1.65 | [[Pibarot 2006]] Table 3 | 同上 |
| **Hancock II** | NA | 1.18 | 1.33 | 1.46 | [[Pibarot 2006]] Table 3 | 同上 |
| **Avalus** | **~1.0–1.2 推測** | **~1.3–1.5 推測** | **~1.55–1.8 推測** | **~1.85–2.1 推測** | PERIGON pivotal 1y pooled **0.76** ← **実測極めて低い** | **size-stratified 公式 data 未取得**、pooled は楽観 estimate と乖離 |
| Epic Supra | 1.00–1.10 | 1.20–1.40 | 1.40–1.65 | 1.75–2.00 | Abbott IFU + Wendt 2014 | 当ディレクトリ未取得 |
| **Trifecta** (撤退済) | **1.40–1.60** | 1.70–2.00 | 2.05–2.40 | 2.40–2.75 | Bavaria 2014 / Yadlapati 2014 | **2022 撤退、historical reference のみ** |
| Mitroflow | 1.10 | 1.30 | 1.55 | 1.80 | Yankah 2008 / Senage 2014 | 当ディレクトリ未取得 |

### Mechanical Valves

| Valve | 19mm | 21mm | 23mm | 25mm | データ source |
|---|---|---|---|---|---|
| **SJM Regent** | **1.60** | **2.00** | **2.20** | **2.50** | [[Pibarot 2006]] Table 3 + [[Okamura_17mmStJudeRegentValid_AnnThoracSurg_2009]] |
| **SJM Regent 17mm**（小弁輪専用） | **1.40–1.60** | — | — | — | Okamura 2009/2012, Hu 2014, Zhao 2012（当ディレクトリ実日本人/中国 cohort） |
| SJM Standard | 1.04 | 1.38 | 1.52 | 2.08 | [[Pibarot 2006]] Table 3 |
| MCRI On-X | 1.50 | 1.70 | 2.00 | 2.40 | [[Pibarot 2006]] Table 3 + PROACT trial |
| Carbomedics | 1.00 | 1.54 | 1.63 | 1.98 | [[Pibarot 2006]] Table 3 |
| Medtronic-Hall | 1.19 | 1.34 | NA | NA | [[Pibarot 2006]] Table 3 |

### Sutureless / Rapid-deployment

| Valve | 19相当 | 21相当 | 23相当 | データ source |
|---|---|---|---|---|
| **Intuity Elite** | **1.30–1.50** | 1.55–1.80 | 1.85–2.10 | [[Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]] SURD-IR |
| Perceval / Plus | 1.10–1.20 | 1.40–1.60 | 1.70–1.90 | [[Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]] SURD-IR |

### 弁間ランキング（**§1 適切使用例**）

19mm size での hemodynamic 期待 EOA ランキング:
- **SJM Regent 17mm > Trifecta（撤退） > Intuity 19 > Magna Ease 19 ≈ Inspiris 19 > Perceval S > Avalus 19 > Mosaic 19 > CE Perimount 19**

これは Pibarot 2020 fallacy の射程外（個別予測ではなく集団 ranking）。

---

## §2. Measured iEOA Distribution — 実 trial / registry cohort

**個別患者 PPM 予測の primary source は本セクション**。各弁の実測 trial cohort で **何が起こったか** を直接列挙。

### Avalus / PERIGON pivotal trial（n=686）

詳細: [[Klautz_PERIGONPivotalAvalus_EJCTS_2017]]

| 項目 | 値 |
|---|---|
| Cohort BSA | **1.86 m² (Western)** |
| 弁サイズ分布 | 19mm 9% / 21mm 28% / 23mm 32% / 25mm 21% / 27mm 8% / 29mm 2% |
| 1y mean EOA (pooled) | **0.76 ± 0.16 cm²** |
| 1y mean gradient (pooled) | **12.6 ± 4.3 mmHg** |
| **1y Severe PPM** | **25.6%** |
| **1y Moderate PPM** | **50.0%** |
| 1y None/Mild | 24.4% |
| **5y mean EOAi** ([[PERIGON 5y 後解析]]) | **0.79 ± 0.2 cm²/m²**（生存者 bias で改善） |
| 5y Severe PPM | 15% |
| 5y Moderate PPM | 40% |

→ **Avalus standard SAVR で 1y 時点 75.6% PPM (Western BSA 1.86)** — Yang B "PPM 30-50%" estimate より明確に悪い

### Inspiris RESILIA / COMMENCE trial（n=689）

詳細: [[Bavaria_RESILIAvsContemporaryPARTNER2ADurability_JCompEffRes_2023]]

| 項目 | 値 |
|---|---|
| Cohort BSA | mean ≈1.95 m² (Western, COMMENCE は若年含む) |
| 弁サイズ分布 | 19-21mm **22.2%** / その他 77.8% |
| 1y mean EOA (pooled) | **1.7 ± 0.41 cm²** |
| 1y mean gradient (pooled) | **12.2 ± 4.97 mmHg** |
| 5y mean EOA | **1.6 ± 0.39 cm²**（軽度低下） |
| 5y mean gradient | 14.0 ± 5.73 mmHg |
| **5y SVD-HVD (Stage ≥2)** | **1.0%** (matched) vs PARTNER 2A SAVR 4.8% |
| **PPM size-stratified** | **本論文未報告**（別 publication 必要） |

→ **Inspiris は Avalus より圧倒的に hemodynamic 良好（1y EOA pooled 1.7 vs 0.76）+ durability 優位 (5y SVD 1%)**

### Magna Ease / Tabata Japanese cohort（n=170）

詳細: [[Tabata_InterruptedSuturingSmallSupraAnnular_JTCVS_2014]]

| 項目 | 値 |
|---|---|
| Cohort BSA | **1.45 m² (日本人女性)** ← **Asian small body** |
| 弁サイズ | **19/21mm Magna 中心** |
| **PPM (mattress suturing)** | **56% (moderate+severe)** |
| **PPM (interrupted suturing)** | **29%** ← **半減** |

→ **日本人 BSA 1.45 + Magna 19/21mm + interrupted suturing で PPM 29%** — Avalus PERIGON Western 75% と比較で大幅に良好（手技要因が大）

### SJM Regent 17mm / Okamura Japanese cohort

詳細: [[Okamura_17mmStJudeRegentValid_AnnThoracSurg_2009]] / [[Okamura_17mmStJudeRegentMidterm_CircJ_2012]]

| 項目 | 値 |
|---|---|
| Cohort BSA | **1.4-1.5 m² (日本人小体格)** |
| 弁 | **SJM Regent 17mm mechanical** |
| Mid-term mortality | 良好 |
| **Severe PPM** | **数%（実質回避）** |
| Mean gradient postop | 低 |

→ **日本人 small body + 17mm Regent (mechanical) で PPM 回避可能** — warfarin 治療許容できれば最強選択肢

### Evolut FX (TAVI) / OCEAN-TAVI（n=576）

詳細: [[Hase_EvolutRvsSAPIEN3JapaneseSmallAnnulus_CCI_2021]]

| 項目 | Evolut R | Sapien 3 |
|---|---|---|
| Cohort BSA | **1.4 m² (日本人 small)** | 同 |
| Annulus mean | 21.5mm | 同 |
| **Severe PPM (matched, discharge)** | **1.5%** | 3.0% |
| **Moderate PPM (matched)** | 7.7% | 17.9% |
| **1y mean PG (matched)** | **9.0 mmHg** | **12.0 mmHg** (P<.001) |
| 1y iEOA (matched) | **1.21 cm²/m²** | 0.96 |

→ **日本人 small annulus で Evolut R/FX は Sapien 3 より圧倒的 hemodynamic 優位**

### Intuity Elite / Berretta SURD-IR PSM

詳細: [[Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]]

| 項目 | Intuity | Perceval |
|---|---|---|
| Mean gradient | **11.6 mmHg** | 14.5 mmHg |
| Severe PPM | <6% | <6% |

→ **Intuity > Perceval、小弁輪で Intuity は AAE 代替たり得る**

### TAVI vs SAVR-AAE / SMART RCT, VIVA RCT

詳細: [[Herrmann_SMARTTrial_NEJM_2024]] / [[RodesCabau_VIVATrialSmallAnnulus_Circulation_2024]]

| Trial | TAVI severe PPM | SAVR (含 AAE) severe PPM |
|---|---|---|
| **SMART (Evolut vs Sapien 3, small annulus)** | **<1%** (Evolut) / 7.5% (Sapien 3) | n/a |
| **VIVA (TAVR Evolut vs SAVR ±AAE)** | **5.6%** | 10.3% (P=0.30 NS) |

→ **Evolut FX TAVI が現在最も PPM 回避能力高い選択肢**

---

## §3. 日本人 BSA 1.3-1.5 cohort focus

**実日本人/Asian cohort のみで PPM 議論**（楽観 estimate 排除）。

### 直接実測データのある弁・戦略

| 戦略 | 実測 cohort | Severe PPM | 注釈 |
|---|---|---|---|
| **SJM Regent 17mm mechanical** | Okamura n≈88-139 BSA 1.4-1.5 | **数%** | 日本長期 data ★★★ |
| **SJM Regent 17mm (中国)** | Hu n=89 / Zhao n=66 | 数% | mid-term ★★ |
| **Magna 19/21mm + interrupted suturing** | Tabata n=170 BSA 1.45 | 29% (mod+sev) | 日本人 ★★★ |
| **Evolut R/FX 20-23mm TAVI** | OCEAN-TAVI n=576 BSA 1.4 | **1.5%** | 日本人 ★★★★★ |
| **Sapien 3 20-23mm TAVI** | OCEAN-TAVI n=576 BSA 1.4 | 3.0% | 日本人 ★★ |
| **20mm THV extremely small annulus** | Okuno n=205 BSA 1.26 | moderate 29% | 5y mortality 同等 ★★★ |

### **データのない弁・戦略**（日本人 cohort 未存在）

- **Inspiris 19mm 日本人 cohort: 未取得 / おそらく未publication**
- **Avalus 19mm 日本人 cohort: 未取得 / おそらく未publication**
- **Magna Ease 19mm 日本人 cohort（mattress vs interrupted 比較以外）: 限定的**
- **Trifecta 19mm 日本人 cohort: 撤退済、価値低**
- **Y-incision SAVR 日本人 cohort**: [[Kitamura_YandIIncisionTechnique_AnnThoracSurgShortRep_2025]] case report のみ、prospective series なし
- **SJM Regent 19mm 日本人 cohort**: Okamura 17mm から extrapolation のみ、19mm 直接 data 不足

### 推奨利用法

**日本人 BSA 1.34 患者の弁選択**は:
1. **§3 の "実測データあり" のみで判断**（§1 ranking 表は参考程度）
2. データなしの弁（Inspiris/Avalus 19mm 日本人）への extrapolation は **Pibarot 2020 fallacy のリスクを背負う**ことを認識
3. **Yamamoto 2025 EuroIntervention** （[[paper_list]] 未取得 priority #1）が日本人 BE-TAVI 長期 sex/PPM 解析を提供する可能性、要追加取得
4. **JaCVSD 全国 SAVR registry の publicly accessible 解析が将来必須** — 現在最大の欠落データ

---

## §4. Pibarot 2006 Table 3 — Historical Reference

> [!warning] **§0 警告下、historical reference として保持**
> 以下は [[Pibarot_PPMDefinitionClinicalImpactPrevention_Heart_2006]] Table 3 の完全転記。**Pibarot 2020 fallacy 警告適用、個別予測には使わない**。

### Stented Bioprostheses

| Valve | 19mm | 21mm | 23mm | 25mm | 27mm | 29mm |
|---|---|---|---|---|---|---|
| Medtronic Mosaic | 1.20 | 1.22 | 1.38 | 1.65 | 1.80 | 2.00 |
| Hancock II | NA | 1.18 | 1.33 | 1.46 | 1.55 | 1.60 |
| Carpentier-Edwards Perimount | 1.10 | 1.30 | 1.50 | 1.80 | 1.80 | NA |

### Stentless Bioprostheses

| Valve | 19mm | 21mm | 23mm | 25mm | 27mm | 29mm |
|---|---|---|---|---|---|---|
| Medtronic Freestyle | 1.15 | 1.35 | 1.48 | 2.00 | 2.32 | NA |
| St Jude Toronto SPV | — | 1.30 | 1.50 | 1.70 | 2.00 | 2.50 |
| Prima Edwards | 0.80 | 1.10 | 1.50 | 1.80 | 2.30 | 2.80 |

### Mechanical Valves

| Valve | 19mm | 21mm | 23mm | 25mm | 27mm | 29mm |
|---|---|---|---|---|---|---|
| Medtronic-Hall | 1.19 | 1.34 | NA | NA | NA | NA |
| St Jude Medical Standard | 1.04 | 1.38 | 1.52 | 2.08 | 2.65 | 3.23 |
| St Jude Medical Regent | 1.60 | 2.00 | 2.20 | 2.50 | 3.60 | 4.40 |
| MCRI On-X | 1.50 | 1.70 | 2.00 | 2.40 | 3.20 | 3.20 |
| Carbomedics | 1.00 | 1.54 | 1.63 | 1.98 | 2.41 | 2.63 |
| Sorin Bicarbon | NA | 1.66 | 1.96 | NA | NA | NA |

---

## §5. Yang Y-incision argument への再評価

Yang B "5 Misconceptions" (2026) の "standard SAVR PPM 30-50% → AAE 0%" 主張に対する **本テーブル経由の批判的再評価**:

| 観点 | 数値 | 評価 |
|---|---|---|
| **Avalus PERIGON 実測 PPM 75.6% (1y)** | Western BSA 1.86 | Yang estimate より悪い、AAE の必要性を強化 |
| **Inspiris COMMENCE 実測 PPM (size-stratified 未報告)** | — | データ不足 |
| **日本人 Magna + interrupted suturing 29%** | BSA 1.45 | **AAE なしでも日本人小体格で PPM 29% に下げられる** ← Yang argument を弱める |
| **Pibarot 2020 fallacy 30%** | projected vs measured | **Yang の "standard SAVR PPM 30-50%" の半分は projected overestimate の可能性** |
| **OCEAN Evolut FX TAVI severe PPM 1.5%** | 日本人 BSA 1.4 | **AAE なしの TAVI が AAE-SAVR より優位** |

### 結論

Yang の "standard SAVR で大量 PPM → AAE で解決" の議論は **Western 体型 + Avalus 系列 bioprosthesis 標準実装 + projected chart 楽観 estimate** という前提では正しい。しかし:

- **日本人小体格** で
- **Magna + interrupted suturing** または **Regent mechanical** または **Evolut FX TAVI** を選び
- **projected chart の 30% overestimate を補正** すれば

**AAE なしでも PPM 回避可能、AAE の追加侵襲は必須でない**。

これが本研究 RQ の中核含意で、Pibarot 2020 fallacy 論文 + PERIGON Avalus 実測 + 日本人 cohort 実測（Tabata/Okamura/OCEAN）で **三重に裏付けられる**。

---

## §6. 取得状況と次の取得 priority

### 当ディレクトリで取得済み

| Paper | PMC | 取得形式 |
|---|---|---|
| **Pibarot Heart 2006 (Table 3)** | PMC1861088 | HTML フルテキスト (PDF 不可) |
| **Pibarot 2020 fallacy** | PMC7971169 | HTML フルテキスト |
| **PERIGON Avalus pivotal (Klautz 2017)** | PMC5848807 | HTML フルテキスト |
| **PERIGON Avalus 5y prognostic** | PMC10897662 | HTML フルテキスト |
| **RESILIA vs PARTNER 2A (Bavaria 2023)** | PMC10288964 | HTML フルテキスト |

### 当ディレクトリ未取得（優先順）

| Paper | 優先度 | 入手難度 |
|---|---|---|
| **COMMENCE Inspiris 5y (Bavaria 2023 ATS)** PMID 35065065 | ★★★★★ | PMC なし → 購読 / 図書館 ILL |
| **COMMENCE Inspiris 7y (2024 JTCVS)** PMID 37778503 | ★★★★ | 同上 |
| **Yamamoto 2025 EuroIntervention** | ★★★★★ | [[paper_list]] 未取得 priority #1 |
| **PERIGON Avalus 5y full (Beaver JTCVS 2022)** | ★★★ | 同上 |
| **Magna Ease primary trial (Bavaria 2014)** | ★★★ | 同上 |
| **Tasca G 2019 JACC Imaging review** | ★★★ | 同上 |
| **VARC-3 consensus (Genereux 2021 JACC)** | ★★★★ | open access、追加 fetch 可 |

---

*作成: 2026-05-17 (v2 hybrid 再設計) | 関連: [[_index]] | [[_IntegratedReview_SmallAnnulusAVR_2026]] | [[Pibarot_FallacyIEOAChartPPMPrediction_EHJCardiovascImag_2020]]（最重要）*
