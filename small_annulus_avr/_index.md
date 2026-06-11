---
title: "狭小弁輪 SAVR と弁輪拡大術 — 文献参照コレクション"
date: 2026-05-13
updated: 2026-05-16
tags:
  - small-annulus
  - savr
  - aortic-annulus-enlargement
  - y-incision
  - manouguian
  - nicks
  - konno
  - ppm
  - viv-tavr
  - japanese-cohort
  - asian-cohort
  - procedure-collection
category: 弁膜症外科
---

# 狭小弁輪 SAVR と弁輪拡大術（AAE: Aortic Annulus Enlargement）— 文献コレクション

> **このノートの使い方**: 知りたい論点（手技選択・PPM・ViV戦略・アジア人エビデンス等）について → セクション4「参照マップ」で対応論文を特定 → 個別論文サマリー（`md/`）を参照 → PDF で全文確認。
>
> **統合レビューノート（最新 v2, 2026-06）**: `[[md/_IntegratedReview_SmallAnnulusAVR_v2_2026-06]]` — 84 本コーパス＋SAKURA-AVR を反映した改訂版（9 章）。**HTML（PMID/DOI ハイパーリンク・サイドバー目次付き）**: `output/small_annulus_avr_integrated_review_2026-06.html`（ビルダー: `build_review_html.py`）。
> 旧版: `[[md/_IntegratedReview_SmallAnnulusAVR_2026]]`（2026-05, 69 本）。

> [!info] **2026-05-16 Phase 3b 完了**
> 69 個別MD作成・3つのCSV (outcomes_master / ppm_landscape / asian_cohort_subset) 完成。本ファイルは実データを反映済（Key Numbers・参照マップ・全 wikilinks）。

---

## 1. 研究背景・問題意識（Research Question）

> [!info] なぜ今この研究が必要か
> 欧米では Yang らによる **Y-incision（Roof technique, JTCVS 2023）** を契機に **大動脈弁輪拡大術 (AAE)** が大流行。"Bigger the better" の風潮で、将来の Valve-in-Valve TAVR を見据え、初回 SAVR で 23–25mm 弁を入れるべきとされる。
> 一方、**小体格・狭小弁輪患者（特に日本人・アジア人）** に対して、追加侵襲が本当に正当化されるかは検証不足。19mm 弁しか入らない症例で、Y-incision/Manouguian/Nicks を加えることは妥当か？

### Primary / Secondary / Tertiary RQ

| | RQ |
|---|---|
| **Primary** | 狭小弁輪（≤23mm）+ 小体格（BSA <1.6–1.8）で、AAE 付き SAVR は AAE なし SAVR / TAVI と比較してアウトカムを改善するか |
| **Secondary** | ViV-TAVR を見据えた initial valve size は何 mm 必要か。19mm 弁植込みは long-term で許容されるか |
| **Tertiary** | 日本人・アジア人特有の解剖を反映した手術戦略はどうあるべきか |

### Operational Definitions
- **狭小弁輪**: annulus diameter ≤23mm（21mm 主軸、21–23mm も functional small annulus として取り込む）
- **小体格**: BSA <1.6 m²（厳密）または <1.8 m²（広義）
- **PPM**: Severe = iEOA ≤0.65 cm²/m²、Moderate = iEOA ≤0.85 cm²/m²（Pibarot 定義）

---

## 2. 解剖学的基礎・手技概要

> [!note] 大動脈弁輪拡大術 (AAE) の主要 4 法 + 最新変法
> 弁輪拡大術は **後方拡大（posterior, non-coronary cusp 側）** と **前方拡大（anterior, septal 側）** に大別される。Y-incision は前者の発展型、Konno は後者の代表。

| 手技 | 切開部位 | 拡大量 | 代表文献 |
|---|---|---|---|
| **Nicks** (1970) | NCC → 大動脈起始部に向け、僧帽弁切らない | 1–2 弁サイズ | Nicks R. Thorax 1970 |
| **Manouguian** (1979) | NCC → anterior mitral leaflet base まで切開 | 2–3 弁サイズ | Manouguian S. JTCVS 1979 |
| **Konno** (1975) | RCC ↔ ventricular septum 前方 + 心筋切除 | 大幅（小児・LVOT 狭窄） | Konno S. JTCVS 1975 |
| **Y-incision (Yang)** (2021–) | NCC → LFT/RFT 両側に Y 字、僧帽弁不可侵 | **3–4 弁サイズ** | [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]] |
| **Y-and-I (Kitamura)** (2025) | 後方 Y + 前方 I（septum 側） | 小柄日本人女性で size 21 達成 | [[md/Kitamura_YandIIncisionTechnique_AnnThoracSurgShortRep_2025]] |

> [!tip] Y-incision の利点と懸念（本コレクションのエビデンスから）
> **利点**: 僧帽弁前尖を切らない / 3–4 サイズ大の弁植込み可 / Univ Michigan 累積コホートで **PPM 0%, 30d mortality 0.8%, postop mean PG 6–7 mmHg**（[[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]] 他）
> **懸念**: 既存 Manouguian + LVOT myectomy より長い CPB 時間 / **Severe central MR 初報告**（[[md/Ozcelik_SevereMRAfterYIncisionCaseReport_JCardiothoracSurg_2026]]、short aorto-mitral curtain 機序）/ 再手術困難性 / **小体格 + 既存 short AM continuity（日本人で平均 8mm）への過拡大リスク**

---

## 3. 患者選択アルゴリズム（エビデンスベース推奨）

```
[術前 CT/Echo: annulus diameter, AM continuity 長, BSA]
   ↓
annulus ≤21mm (severe small) かつ BSA <1.6 m² ?
   ├── Yes（典型的日本人女性小弁輪）
   │    ↓
   │   [年齢・侵襲耐性評価]
   │    ├── 高齢/高リスク → **TAVI 優先**（JCS 2020 Table 33 推奨方向 — 但し small <20mm は OCEAN 20mm THV エビデンスあり [[md/Okuno_ExtremelySmall20mmTHV_JACCAsia_2025]]）
   │    └── 若年/低リスク
   │         ↓
   │        [初回 valve size 戦略]
   │         ├── Future ViV 重視 → **AAE で size ≥23mm 達成**（Y-incision; D'Onofrio 2016 で ID ≥21mm が ViV 成功閾値 [[md/DOnofrio_ViVValveSizing_AnnThoracSurg_2016]]）
   │         └── 侵襲最小化 → **interrupted suturing + supra-annular bioprosthesis**（Tabata 2014: PPM 29% vs mattress 56% [[md/Tabata_InterruptedSuturingSmallSupraAnnular_JTCVS_2014]]）
   │
   └── No → 通常 SAVR / TAVI（既存ガイドライン準拠）
```

> [!warning] **エビデンス・ガイドラインの逆向き推奨に注意**
> - **ACC/AHA 2020** + **ESC/EACTS 2021**: 小弁輪 → AAE 考慮を narrative で示唆（[[md/Otto_2020ACCAHAVHDGuideline_Circulation_2021]] / [[md/Vahanian_2021ESCEACTSVHDGuideline_EHJ_2022]]）
> - **JCS 2020 (日本)**: 小弁輪 + 予想 PPM → **TAVI 推奨**（[[md/Izumi_JCS2020VHDGuideline_CircJ_2020]] Table 33）— 日本人小体格・施設経験を反映、本研究 RQ の motivation そのもの

---

## 4. 参照マップ（Reference Map）

### A. 手技・テクニック

| 知りたいこと | 参照論文 |
|---|---|
| **Y-incision の手技ステップ・最新総説** | [[md/Yang_UpdatesYIncisionAAE_AnnCardiothoracSurg_2024]] / [[md/Yang_5MisconceptionsYIncisionAAE_AnnThoracSurg_2026]] / [[md/Chen_YIncisionRationaleTechniqueOutcomes_AnnThoracSurg_2025]] |
| **Y-incision vs Nicks/Manouguian 直接比較（PSM）** | [[md/Makkinejad_YIncisionVsTraditionalAAE_AnnCardiothoracSurg_2024]] / [[md/Makkinejad_NicksManouguianYIncisionComparison_AnnThoracSurg_2025]] |
| **Nicks / Manouguian は obsolete か** | [[md/Hassler_AreNicksManouguianObsolete_SeminThoracCardiovascSurg_2024]] |
| **Manouguian 変法・改良** | [[md/Malfitano_ModifiedManouguianTechnique_JCardSurg_2022]] / [[md/Maekawa_OptimalProsthesisSizeManouguian_ArtifOrgans_2002]] |
| **Y-incision パッチ形状・Arc 改良** | [[md/Yang_YIncisionRectangularPatch_AnnCardiothoracSurg_2024]] / [[md/Yang_ArcModificationPatch_AnnThoracSurgShortRep_2025]] / [[md/Fikani_TechnicalModificationsYIncision_ThoracCardiovascSurg_2026]] |
| **Y-incision + 同時 MV 手術** | [[md/Cangut_MitralValveYIncisionConcomitant_JTCVSTech_2026]] |
| **Y-incision + Chimney MVR（Commando代替）** | [[md/Gan_YIncisionChimneyMVRDoubleAnnuli_AnnThoracSurg_2026]] |
| **異常 LCX 走行 + Y-incision** | [[md/Yin_YIncisionAnomalousLCX_EJCTS_2025]] |
| **TAVI explant 後の Y-incision AAE** | [[md/Yin_YIncisionAfterTAVIExplant_AnnCardiothoracSurg_2025]] |
| **Y-AAE 後の解剖学的変化（aortic root）** | [[md/Truesdell_AorticRootDimensionsPostYIncision_AnnCardiothoracSurg_2024]] |
| **Y-incision の血行動態モデリング** | [[md/Bonini_HemodynamicModelingYIncisionAAE_JCardiovascTranslRes_2025]] |
| **Y-incision 術者経験曲線** | [[md/Makkinejad_SurgeonExperienceAAE_JTCVSOpen_2025]] |
| **Y-AAE の合併症: severe central MR** | [[md/Ozcelik_SevereMRAfterYIncisionCaseReport_JCardiothoracSurg_2026]] |
| **Sutureless valve による AAE 回避戦略** | [[md/Beckmann_SuturelessVsRootEnlargement_ICVTS_2016]] / [[md/Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]] / [[md/Santarpino_SURDIROperativeOutcomes_EJCTS_2019]] |

### B. 適応・患者選択

| 知りたいこと | 参照論文 |
|---|---|
| **狭小弁輪 operational definition** | [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]]（≤21mm Y-AAE 適応の根拠） |
| **小体格 + 狭小弁輪（Asian cohort）** | [[md/Tabata_InterruptedSuturingSmallSupraAnnular_JTCVS_2014]] / [[md/Okuno_ExtremelySmall20mmTHV_JACCAsia_2025]] / [[md/Kitamura_YandIIncisionTechnique_AnnThoracSurgShortRep_2025]] |
| **TAVI vs AAE-SAVR の使い分け（RCT）** | [[md/Herrmann_SMARTTrial_NEJM_2024]] / [[md/RodesCabau_VIVATrialSmallAnnulus_Circulation_2024]] / [[md/Leone_TAVISMALL2Registry_EuroIntervention_2023]] |
| **将来 ViV を見据えた initial sizing** | [[md/DOnofrio_ViVValveSizing_AnnThoracSurg_2016]] / [[md/Dvir_VIVIDOriginalAorticViV_JAMA_2014]] / [[md/Simonato_ViVImplantationDepth_CircCardiovascInterv_2016]] |
| **小児 / 先天性での Nicks 改良** | [[md/Masaki_NicksModificationChildren_PediatrCardiol_2026]] |

### C. アジア人・日本人コホート（**最重点**）

| 知りたいこと | 参照論文 |
|---|---|
| **日本人 SAVR + AAE 戦略（古典コホート）** | [[md/Maekawa_OptimalProsthesisSizeManouguian_ArtifOrgans_2002]]（名古屋、AM continuity 8mm 起点） / [[md/Tabata_InterruptedSuturingSmallSupraAnnular_JTCVS_2014]]（interrupted suturing による PPM 半減） |
| **日本人 17mm 機械弁 mid-term** | [[md/Okamura_17mmStJudeRegentValid_AnnThoracSurg_2009]] / [[md/Okamura_17mmStJudeRegentMidterm_CircJ_2012]] |
| **日本人 TAVR registry（OCEAN）** | [[md/Hase_EvolutRvsSAPIEN3JapaneseSmallAnnulus_CCI_2021]] / [[md/Yashima_OCEANTAVIExtremelySmallAnnulus_IntJCardiol_2017]] / [[md/Shishido_SexEffectMortalityTAVI_CircJ_2021]] / [[md/Okuno_ExtremelySmall20mmTHV_JACCAsia_2025]] |
| **日本人 J-TVT registry（全国）** | [[md/Meguro_JTVTSmallAnnulus_CircJ_2021]] |
| **日本人 "Y and I" 法（新変法）** | [[md/Kitamura_YandIIncisionTechnique_AnnThoracSurgShortRep_2025]] |
| **韓国 TAVR registry** | [[md/Moon_KoreanTAVRRegistrySmallAnnulus_JCardiovascInterv_2023]] / [[md/Lee_SelfvsBalloonExpandableTAVRSmallAnnulus_KoreanCircJ_2021]] / [[md/Kim_TwoBioprosthesesSmallAnnuli_JClinMed_2021]] / [[md/Kamioka_TAVRvsSAVRSmallAnnulus_IntHeartJ_2019]] |
| **中国コホート** | [[md/Hu_17mmRegentPPMMatter_JCardiothoracSurg_2014]] / [[md/Zhao_RegentMechValveSmallAnnulus3yr_JCardiothoracSurg_2012]] / [[md/Wang_YIncisionNewRoofTechnique_JTCVSTech_2025]] / [[md/Mao_MLPPMTAVRSmallAnnulus_CardiovascIntervTher_2026]] / [[md/Gan_YIncisionChimneyMVRDoubleAnnuli_AnnThoracSurg_2026]] |
| **JCS 2020 弁膜症ガイドライン（日本）** | [[md/Izumi_JCS2020VHDGuideline_CircJ_2020]] |

### D. 術後成績・予後

| 知りたいこと | 参照論文 |
|---|---|
| **30 日死亡（Y-AAE）** | [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]] / [[md/Makkinejad_YIncisionVsTraditionalAAE_AnnCardiothoracSurg_2024]] |
| **長期生存 / Severe PPM の生存影響（meta）** | [[md/Head_PPMLongTermSurvivalMeta_EHJ_2012]] / [[md/Mohty_PPMLongTermAgeObesityLVD_JACC_2009]] / [[md/Mohty_PPMParadoxicalLowFlow_Circulation_2014]] |
| **PPM 概念史・閾値の根拠** | [[md/Pibarot_PPMHemodynamicClinical_JACC_2000]] / [[md/Pibarot_PPMConceptToCompellingEvidence_JACC_2012]] |
| **機械弁 vs 生体弁（小弁輪関連）** | [[md/Goldstone_MechanicalBiologicAVR_NEJM_2017]] |
| **Pacemaker 率（特に Y-AAE）** | [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]] / [[md/Alperi_PPIPostViVTAVR_JACC_2021]] |
| **Mean transvalvular gradient 推移** | [[md/Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]] / [[md/Hase_EvolutRvsSAPIEN3JapaneseSmallAnnulus_CCI_2021]] |

### E. ViV-TAVR / Future Strategy

| 知りたいこと | 参照論文 |
|---|---|
| **VIVID registry オリジナル** | [[md/Dvir_VIVIDOriginalAorticViV_JAMA_2014]] |
| **ViV 適応の最小弁サイズ（≥21mm 閾値）** | [[md/DOnofrio_ViVValveSizing_AnnThoracSurg_2016]] |
| **ViV implantation depth 最適化** | [[md/Simonato_ViVImplantationDepth_CircCardiovascInterv_2016]] |
| **ViV 後の coronary obstruction** | [[md/Ribeiro_VIVIDCoronaryObstruction_EHJ_2018]] |
| **BASILICA（coronary obstruction 予防）** | [[md/Khan_BASILICATrial_JACCCardiovascInterv_2019]] / [[md/Khan_BASILICA1yrOutcomes_CircCardiovascInterv_2021]] / [[md/Khan_BASILICARegistry_JACCCardiovascInterv_2021]] / [[md/Lederman_BASILICAReview_JACCCardiovascInterv_2019]] |
| **BVF/REDUCE による hemodynamics 改善** | [[md/Ruge_BVFPerimountREDUCE_CCI_2025]] |
| **TAVI explant 後の手術選択肢** | [[md/Yin_YIncisionAfterTAVIExplant_AnnCardiothoracSurg_2025]] / [[md/Blackman_REVALVEDesign_IntJCardiol_2025]] |
| **PPI post ViV-TAVR** | [[md/Alperi_PPIPostViVTAVR_JACC_2021]] |

### F. ガイドライン

| ガイドライン | リンク |
|---|---|
| **ACC/AHA 2020 VHD（Otto）— Guideline 本文** | [[md/Otto_2020ACCAHAVHDGuideline_Circulation_2021]] |
| **ACC/AHA 2020 VHD（Otto）— Executive Summary** | [[md/Otto_2020ACCAHAVHDExecSummary_JACC_2021]] |
| **ESC/EACTS 2021 VHD（Vahanian）** | [[md/Vahanian_2021ESCEACTSVHDGuideline_EHJ_2022]] |
| **JCS 2020 弁膜症（Izumi）— 日本** | [[md/Izumi_JCS2020VHDGuideline_CircJ_2020]] |

---

## 5. 論文一覧（カテゴリ別・全 84 本）

> 詳細は [[paper_list]]（全 81 本検証済リスト）。2026-06 に研究プロトコル [[protocol/2026-06-11_SAKURA-AVR_protocol]] 補強のため 15 本を追加取得・要約（下記「2026-06 追加」）。本セクションでは取得済 84 本に wikilink。

### Category A: Y-incision / Roof technique（20 本）
- [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]]（Yang seminal, n=50+）
- [[md/Yang_UpdatesYIncisionAAE_AnnCardiothoracSurg_2024]]
- [[md/Yang_YIncisionRectangularPatch_AnnCardiothoracSurg_2024]]
- [[md/Yang_ArcModificationPatch_AnnThoracSurgShortRep_2025]]
- [[md/Yang_5MisconceptionsYIncisionAAE_AnnThoracSurg_2026]]
- [[md/Makkinejad_YIncisionVsTraditionalAAE_AnnCardiothoracSurg_2024]]（**PSM 直接比較**）
- [[md/Makkinejad_NicksManouguianYIncisionComparison_AnnThoracSurg_2025]]
- [[md/Makkinejad_SurgeonExperienceAAE_JTCVSOpen_2025]]
- [[md/Truesdell_AorticRootDimensionsPostYIncision_AnnCardiothoracSurg_2024]]
- [[md/Chen_YIncisionRationaleTechniqueOutcomes_AnnThoracSurg_2025]]
- [[md/Yin_YIncisionAnomalousLCX_EJCTS_2025]]
- [[md/Yin_YIncisionAfterTAVIExplant_AnnCardiothoracSurg_2025]]
- [[md/Bonini_HemodynamicModelingYIncisionAAE_JCardiovascTranslRes_2025]]
- [[md/Wang_YIncisionNewRoofTechnique_JTCVSTech_2025]]（中国 Fuwai n=53）
- [[md/Fikani_TechnicalModificationsYIncision_ThoracCardiovascSurg_2026]]
- [[md/Cangut_MitralValveYIncisionConcomitant_JTCVSTech_2026]]
- [[md/Masaki_NicksModificationChildren_PediatrCardiol_2026]]
- [[md/Gan_YIncisionChimneyMVRDoubleAnnuli_AnnThoracSurg_2026]]（Commando 代替）
- [[md/Kitamura_YandIIncisionTechnique_AnnThoracSurgShortRep_2025]]（日本人新変法）
- [[md/Ozcelik_SevereMRAfterYIncisionCaseReport_JCardiothoracSurg_2026]]（**合併症初報告**）

### Category B: 古典 AAE（3 本取得 / Manouguian・Nicks・Konno 原著は未取得）
- [[md/Hassler_AreNicksManouguianObsolete_SeminThoracCardiovascSurg_2024]]
- [[md/Maekawa_OptimalProsthesisSizeManouguian_ArtifOrgans_2002]]（**日本、AM continuity 解析**）
- [[md/Malfitano_ModifiedManouguianTechnique_JCardSurg_2022]]
- ⏸ 未取得（図書館 ILL 必要）: Manouguian 1979 / Nicks 1970 / Konno 1975 / Kawachi 1992 / Kitamura M 1996

### Category C: 狭小弁輪 + 小体格（アジア人重点）— 15 本
- [[md/Hase_EvolutRvsSAPIEN3JapaneseSmallAnnulus_CCI_2021]]（OCEAN-TAVI 日本）
- [[md/Hu_17mmRegentPPMMatter_JCardiothoracSurg_2014]]（中国 17mm Regent）
- [[md/Kamioka_TAVRvsSAVRSmallAnnulus_IntHeartJ_2019]]（日本 TAVR vs SAVR）
- [[md/Kim_TwoBioprosthesesSmallAnnuli_JClinMed_2021]]（韓国）
- [[md/Lee_SelfvsBalloonExpandableTAVRSmallAnnulus_KoreanCircJ_2021]]（韓国 Self vs BE）
- [[md/Mao_MLPPMTAVRSmallAnnulus_CardiovascIntervTher_2026]]（中国 ML-PPM）
- [[md/Meguro_JTVTSmallAnnulus_CircJ_2021]]（**J-TVT 全国 n=5870**）
- [[md/Moon_KoreanTAVRRegistrySmallAnnulus_JCardiovascInterv_2023]]
- [[md/Okamura_17mmStJudeRegentValid_AnnThoracSurg_2009]]（日本 17mm 機械弁）
- [[md/Okamura_17mmStJudeRegentMidterm_CircJ_2012]]（同 mid-term）
- [[md/Okuno_ExtremelySmall20mmTHV_JACCAsia_2025]]（**OCEAN extremely small ≤20mm 5y**）
- [[md/Shishido_SexEffectMortalityTAVI_CircJ_2021]]（OCEAN sex-specific）
- [[md/Tabata_InterruptedSuturingSmallSupraAnnular_JTCVS_2014]]（**interrupted suturing PPM 29% vs 56%**）
- [[md/Yashima_OCEANTAVIExtremelySmallAnnulus_IntJCardiol_2017]]
- [[md/Zhao_RegentMechValveSmallAnnulus3yr_JCardiothoracSurg_2012]]（中国 mech valve）
- ⏸ 未取得: Yamamoto 2025 EuroIntervention（**長期 BE-TAVI、最優先**）/ Liu 2013 Sichuan

### Category D: Prosthesis-Patient Mismatch (PPM)（10 本）
- [[md/Pibarot_PPMHemodynamicClinical_JACC_2000]]（**PPM 定義 seminal**）
- [[md/Pibarot_PPMConceptToCompellingEvidence_JACC_2012]]
- [[md/Pibarot_PPMDefinitionClinicalImpactPrevention_Heart_2006]]（**Table 3: 12 弁モデル × 6 サイズ参照 EOA**）
- [[md/Pibarot_FallacyIEOAChartPPMPrediction_EHJCardiovascImag_2020]]（**Pibarot 本人による reference chart approach の自己否定、誤分類 30%**） ★★★★★
- [[md/Klautz_PERIGONPivotalAvalus_EJCTS_2017]]（**Avalus pivotal trial、1y severe PPM 25.6%, moderate 50%**） ★★★★
- [[md/Bavaria_RESILIAvsContemporaryPARTNER2ADurability_JCompEffRes_2023]]（**Inspiris RESILIA durability 5y SVD 1.0%, hemodynamic 1y EOA 1.7 cm² pooled**） ★★★★
- [[md/Mohty_PPMLongTermAgeObesityLVD_JACC_2009]]
- [[md/Mohty_PPMParadoxicalLowFlow_Circulation_2014]]
- [[md/Head_PPMLongTermSurvivalMeta_EHJ_2012]]（**meta n=27186、severe HR 1.84**）

> [!info] **派生資料**: [[tables/modern_valve_eoa_reference]]（v2 hybrid 設計、**§0 Pibarot 2020 fallacy 警告** + §1 reference chart (ranking 目的) + §2 measured cohort 分布 + §3 日本人 BSA 1.34 focus + §4 Pibarot 2006 Table 3 保持）

### Category E: TAVI vs SAVR in small annulus（6 本）
- [[md/Herrmann_SMARTTrial_NEJM_2024]]（**SMART RCT primary**）
- [[md/Herrmann_SMARTRationaleDesign_AmHeartJ_2022]]
- [[md/Herrmann_SMARTBioprostheticValveDysfunction_2025]]（SMART BVD 2y）
- [[md/Abdelfattah_TAVRvsSAVRSmallAnnuliMeta_IntJCardiol_2024]]（meta）
- [[md/Leone_TAVISMALL2Registry_EuroIntervention_2023]]
- [[md/RodesCabau_VIVATrialSmallAnnulus_Circulation_2024]]（**VIVA RCT**）

### Category F: ViV-TAVR / TAVI explant（11 本）
- [[md/Dvir_VIVIDOriginalAorticViV_JAMA_2014]]（**VIVID 原著**）
- [[md/DOnofrio_ViVValveSizing_AnnThoracSurg_2016]]（**ID ≥21mm threshold**）
- [[md/Ribeiro_VIVIDCoronaryObstruction_EHJ_2018]]（CO 2.3%、30d mortality 52.9%）
- [[md/Simonato_ViVImplantationDepth_CircCardiovascInterv_2016]]
- [[md/Khan_BASILICATrial_JACCCardiovascInterv_2019]]
- [[md/Khan_BASILICA1yrOutcomes_CircCardiovascInterv_2021]]
- [[md/Khan_BASILICARegistry_JACCCardiovascInterv_2021]]
- [[md/Lederman_BASILICAReview_JACCCardiovascInterv_2019]]
- [[md/Alperi_PPIPostViVTAVR_JACC_2021]]
- [[md/Ruge_BVFPerimountREDUCE_CCI_2025]]
- [[md/Blackman_REVALVEDesign_IntJCardiol_2025]]

### Category G: Sutureless / Rapid deployment（4 本）
- [[md/Beckmann_SuturelessVsRootEnlargement_ICVTS_2016]]（**sutureless vs ARE 直接比較**）
- [[md/Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]]（**SURD-IR PSM**）
- [[md/Berretta_SuturelessBicuspidSURDIR_AnnCardiothoracSurg_2020]]
- [[md/Santarpino_SURDIROperativeOutcomes_EJCTS_2019]]
- ⏸ 未取得: Borger MMCTS 2013

### Category H: ガイドライン（4 本）
- [[md/Otto_2020ACCAHAVHDGuideline_Circulation_2021]]
- [[md/Otto_2020ACCAHAVHDExecSummary_JACC_2021]]
- [[md/Vahanian_2021ESCEACTSVHDGuideline_EHJ_2022]]
- [[md/Izumi_JCS2020VHDGuideline_CircJ_2020]]（**日本、唯一 TAVI 推奨方向**）

### Category I: 機械弁 vs 生体弁（1 本）
- [[md/Goldstone_MechanicalBiologicAVR_NEJM_2017]]

### 2026-06 追加（SAKURA-AVR プロトコル補強・15 本）
> プロトコル [[protocol/2026-06-11_SAKURA-AVR_protocol]] の背景・エンドポイント・方法論を補強するため追加取得・要約。

**弁輪拡大術（AAE）**
- [[md/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025]]（**SAKURA に最も近い先行研究**：matched ≤23mm 弁輪で AAE vs isolated AVR を PSM 112 pair 比較、**6yr 生存 98% vs 74%、AAE 中期死亡 HR 0.19**）
- [[md/Tanaka_AorticAnnularEnlargementOutcomesMetaAnalysis_AnnCardiothoracSurg_2024]]（**AAE メタ解析** 15研究216,654例：マッチ後死亡差なし、**severe PPM RR 0.61**）
- [[md/Manouguian_PatchEnlargementAorticValveRing_JTCVS_1979]]（**Manouguian 原著** n=8、拡大量 10–25mm。前尖切開の安全閾値と failure mode=パッチ破断 MR）
- [[md/Nicks_HypoplasiaAorticRoot_Thorax_1970]]（**Nicks 原著**：size9 以上確保で死亡 9% vs 8A 強行 45%）
- [[md/Konno_NewMethodProstheticValveReplacementCongenitalAorticStenosisHypoplasia_JTCVS_1975]]（**Konno 原著**：弁輪を原径約2倍に拡大）

**PPM**
- [[md/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024]]（**PPM after SAVR 最新メタ** 122,989例：severe 20yr 全死亡 HR 1.29・心臓死 HR 2.04。Head 2012 更新版）
- [[md/Abushouk_MeasuredVsPredictedPPM_JACCCardiovascInterv_2023]]（**measured vs predicted iEOA**：予測法は PPM を系統的過小評価＝measured 一次採用の根拠）

**TAVI vs SAVR / small annulus**
- [[md/Tchetche_RHEIAtrialTAVIvsSAVRWomen_EHJ_2025]]（**RHEIA**：女性限定 TAVI vs SAVR RCT、1y 複合 8.9% vs 15.6%。外科群は AAE ゼロ＝実質 no-AAE 対照）
- [[md/Suruga_SmallVsLargeAnnulusBalloonExpandableTAVR_JAHA_2026]]（BE-TAVR small vs large、**severe PPM 9.8% vs 5.2%**、5y 死亡同等）
- [[md/DiBacco_SuturelessVsTAVISmallAnnulusMultiInstitutional_BrazJCardiovascSurg_2024]]（Perceval vs TAVI、3yr 全死亡 12.2% vs 21.0%、PPM/MACCE 増）

**アジア人コホート**
- [[md/Chen_EastAsianTAVRdeviceSelectionSmallAnnulus_JACCAsia_2025]]（East Asian small annulus device 選択：SEV>BEV 血行動態）

**Category J: エンドポイント定義・統計方法論（新設、`Reference/CatJ_Methods/`）**
- [[md/Genereux_VARC3EndpointDefinitions_EHJ_2021]]（**VARC-3** エンドポイント定義＝SAKURA 採用標準）
- [[md/VanderWeele_EValueSensitivityAnalysis_AnnInternMed_2017]]（**E-value** 未測定交絡の感度解析）
- [[md/Austin_PSMbalanceDiagnostics_StatMed_2009]]（**PSM バランス診断** SMD<0.1）
- [[md/vonElm_STROBEStatement_PLoSMed_2007]]（**STROBE** 観察研究報告基準）

---

## 6. Key Numbers — エビデンスベンチマーク

> 出典は [[tables/outcomes_master.csv]]（69 本一括抽出）/ [[tables/ppm_landscape.csv]] / [[tables/asian_cohort_subset.csv]]

### Y-incision AAE の核心数値

| 指標 | 値 | 出典 |
|---|---|---|
| Y-incision 30 日 / operative mortality | **0–1%** (Univ Michigan cumulative) | [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]] / [[md/Chen_YIncisionRationaleTechniqueOutcomes_AnnThoracSurg_2025]] |
| Y-incision postop mean gradient | **6–7 mmHg** | 同上 |
| Y-incision Severe PPM 率 | **0–5.5%** | Yang seminal n=50 で 0%; Makkinejad PSM で 5.5% |
| Y-incision vs Nicks/Manouguian PPM（PSM 103 pair） | **5.5% vs 23.0%** (P=0.039) | [[md/Makkinejad_YIncisionVsTraditionalAAE_AnnCardiothoracSurg_2024]] |
| Y-incision 弁サイズ upsize median | **3 弁サイズ** | [[md/Yang_YIncisionEarlyOutcomes3to4ValveSizes_JTCVS_2024]] |
| Y-incision での severe central MR | **初報告 1 例**（POD50 で MVR 必要） | [[md/Ozcelik_SevereMRAfterYIncisionCaseReport_JCardiothoracSurg_2026]] |

### PPM 長期予後への影響

| 指標 | 値 | 出典 |
|---|---|---|
| Any PPM all-cause mortality HR | **1.34 (1.18–1.51)** | [[md/Head_PPMLongTermSurvivalMeta_EHJ_2012]] meta n=27,186 |
| Severe PPM all-cause mortality HR | **1.84 (1.38–2.45)** | 同上 |
| Severe PPM cardiac-related mortality HR | **6.46 (2.79–14.97)** | 同上 |
| PPM 閾値（severe / moderate） | iEOA ≤0.65 / ≤0.85 | [[md/Pibarot_PPMHemodynamicClinical_JACC_2000]] |
| JCS 2020 PPM 閾値（日本独自） | BMI <30: ≤0.65 / BMI >30: ≤0.55 | [[md/Izumi_JCS2020VHDGuideline_CircJ_2020]] |

### 日本人 / アジア人 SAVR / TAVR 数値

| 指標 | 値 | 出典 |
|---|---|---|
| 日本 J-TVT 全国 small annulus 割合 | **11%**（女性 93.2%, BSA 1.34 m²） | [[md/Meguro_JTVTSmallAnnulus_CircJ_2021]] |
| 韓国 TAVR registry 女性比率 | **80%**, mean annular diameter **18.7 mm** | [[md/Moon_KoreanTAVRRegistrySmallAnnulus_JCardiovascInterv_2023]] |
| 日本人 interrupted suturing PPM | **29% (interrupted) vs 56% (mattress)** | [[md/Tabata_InterruptedSuturingSmallSupraAnnular_JTCVS_2014]] |
| OCEAN extremely small ≤20mm THV 5y mortality | **同等（vs ≥20mm）** ; moderate PPM 29% | [[md/Okuno_ExtremelySmall20mmTHV_JACCAsia_2025]] |
| 日本人女性 TAVR 後生存（vs 男性） | **HR 0.62** sex-specific advantage | [[md/Shishido_SexEffectMortalityTAVI_CircJ_2021]] |
| 日本人 OCEAN Evolut R vs Sapien 3 1y mPG | **9.0 vs 12.0 mmHg** (P<.001) | [[md/Hase_EvolutRvsSAPIEN3JapaneseSmallAnnulus_CCI_2021]] |
| 日本人 AM continuity 平均（Manouguian 上限指標） | **8 mm** | [[md/Maekawa_OptimalProsthesisSizeManouguian_ArtifOrgans_2002]] |

### TAVI vs SAVR RCT（SMART / VIVA）

| 指標 | TAVI | SAVR (AAE 含む) | P |
|---|---|---|---|
| SMART 1y bioprosthetic valve dysfunction | 9.4% | **41.6%** | <0.001 |
| SMART 30d mortality | ~1% | ~1% | NS |
| VIVA severe PPM | **5.6%** | 10.3% | 0.30 (NS) |
| VIVA 2y all-cause mortality | NS | NS | NS |
| Abdelfattah meta TAVR severe PPM OR | **0.53** (有利) | — | sig |
| Abdelfattah meta SAVR PPI OR | — | **0.36** (有利) | sig |

### ViV-TAVR feasibility

| 指標 | 値 | 出典 |
|---|---|---|
| ViV 後 mean gradient（≤21mm vs ≥23mm 初回弁） | **>35 mmHg 6.8% in ID <20mm** | [[md/DOnofrio_ViVValveSizing_AnnThoracSurg_2016]] |
| ViV 1y mortality（≤21mm 初回弁） | **25.2%**, HR 2.04 | [[md/Dvir_VIVIDOriginalAorticViV_JAMA_2014]] |
| ViV coronary obstruction 率 | **2.3%**, 30d mortality 52.9% | [[md/Ribeiro_VIVIDCoronaryObstruction_EHJ_2018]] |
| BASILICA registry success | 高、30d MACE 低減 | [[md/Khan_BASILICARegistry_JACCCardiovascInterv_2021]] |

### Sutureless / Rapid deployment

| 指標 | 値 | 出典 |
|---|---|---|
| Sutureless vs Nicks ARE CPB time | **-38 min**（sutureless 有利） | [[md/Beckmann_SuturelessVsRootEnlargement_ICVTS_2016]] |
| Intuity vs Perceval mean gradient（小弁輪 PSM） | **11.6 vs 14.5 mmHg**（Intuity 有利） | [[md/Berretta_SuturelessVsRapidDeployment_AnnThoracSurg_2022]] |
| Sutureless severe PPM 率 | **<6%** | 同上 / [[md/Beckmann_SuturelessVsRootEnlargement_ICVTS_2016]] |

### 追加エビデンス（2026-06、SAKURA-AVR 設計根拠）

| 指標 | 値 | 出典 |
|---|---|---|
| AAE vs isolated AVR（matched ≤23mm, PSM 112pair）6yr 生存 | **98% vs 74%**（AAE 中期死亡 HR 0.19, 0.06–0.62） | [[md/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025]] |
| AAE メタ解析 severe PPM（iEOA≤0.65） | **RR 0.61 (0.40–0.93)**；マッチ後死亡差なし | [[md/Tanaka_AorticAnnularEnlargementOutcomesMetaAnalysis_AnnCardiothoracSurg_2024]] |
| PPM after SAVR（最新メタ n=122,989）severe 20yr 全死亡 / 心臓死 | **HR 1.29 / HR 2.04** | [[md/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024]] |
| RHEIA（女性 TAVI vs SAVR RCT）1y 複合 | **8.9% vs 15.6%**（差 −6.8%, P=0.034；外科群 AAE ゼロ） | [[md/Tchetche_RHEIAtrialTAVIvsSAVRWomen_EHJ_2025]] |
| BE-TAVR small vs large severe PPM | **9.8% vs 5.2%**（5y 死亡同等 HR 0.75） | [[md/Suruga_SmallVsLargeAnnulusBalloonExpandableTAVR_JAHA_2026]] |
| Perceval vs TAVI（small annulus）3yr 全死亡 | **12.2% vs 21.0%**（P=0.058） | [[md/DiBacco_SuturelessVsTAVISmallAnnulusMultiInstitutional_BrazJCardiovascSurg_2024]] |
| predicted iEOA は PPM を過小評価（measured 一次採用根拠） | 予測 severe 1% vs 実測 17%（Ternacle） | [[md/Abushouk_MeasuredVsPredictedPPM_JACCCardiovascInterv_2023]] |

---

## 7. PDF ファイル一覧

### 取得済み（**84 本**、2026-06 に SAKURA-AVR 補強で 15 本追加）

PDF は `Reference/Cat*/` に整理済（[[Reference/README]] 参照）。下表の本数は 2026-05 baseline（CatA–I）。2026-06 追加分の内訳は §5「2026-06 追加」を参照。10 カテゴリ:

| カテゴリ | 本数 | 配置先 |
|---|---|---|
| CatA Y-incision | 20 | `Reference/CatA_YIncision/` |
| CatB 古典 AAE | 3 | `Reference/CatB_ClassicalAAE/` |
| CatC アジア人 | 15 | `Reference/CatC_AsianCohort/` |
| CatD PPM | 5 | `Reference/CatD_PPM/` |
| CatE TAVI vs SAVR | 6 | `Reference/CatE_TAVIvsSAVR_SmallAnnulus/` |
| CatF ViV-TAVR | 11 | `Reference/CatF_ViVTAVR/` |
| CatG Sutureless | 4 | `Reference/CatG_Sutureless/` |
| CatH Guidelines | 4 | `Reference/CatH_Guidelines/` |
| CatI Mech vs Bio | 1 | `Reference/CatI_MechVsBio/` |
| **CatJ Methods（新）** | 3 | `Reference/CatJ_Methods/`（VARC-3 は CatH） |

### 未取得（11 / 81 = 14%、図書館 ILL or 言語/有料による）
- **CatA**: Do-Nguyen 2026 ACTA
- **CatB**: Manouguian 1979 / Nicks 1970 / Konno 1975 / Kawachi 1992 / Kitamura M 1996（**全て 1970s–1990s の古典原著、ILL 必要**）
- **CatC-1**: Yamamoto 2025 EuroIntervention（**長期 BE-TAVI 小弁輪 sex/PPM 解析、最優先**）
- **CatC-3**: Liu 2013 Sichuan（中国語誌）
- **CatG**: Borger MMCTS 2013

### 部分取得（PDF binary 未入手、データ抽出済）
- **CatD**: Pibarot Heart 2006（PMID 16251232, PMCID PMC1861088）— PMC HTML フルテキストから Table 3 + 全章節データ抽出済、PDF binary は BMJ Cloudflare 保護で未取得

---

## 8. 既存資源との連携（read-only 参照）

### commando_procedure からの参照
- [[commando_procedure/md/Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025]] — Manouguian の歴史記述
- [[commando_procedure/md/Matsuzaki_ModifiedCommandoAortoAnnuloSeptotomy_ICVTS_2024]] — Aorto-annulo-septotomy 変法
- [[commando_procedure/md/Kakavand_CommandoMitralAnnularCalcification_JTCVSOpen_2024]] — PPM 7.8% データ
- [[commando_procedure/md/Pettersson_FibrousSkeletonReconstruction_MMCTS_2014]] — Fibrous skeleton 解剖の reference

### 既存月別ジャーナル MD への wikilink
- `[[MD/cardiac_surgery_journals_2026_03]]` — Handa et al.（日本人 LAVI×SAVR）
- `[[MD/cardiac_surgery_journals_2026_05]]` — Carducci（TAVR vs SAVR）

---

## 9. 進捗・次のステップ

| フェーズ | 内容 | 状態 |
|---|---|---|
| Phase 0 | 計画策定 | ✅ 2026-05-13 |
| Phase 1 | スケルトン構築 | ✅ 2026-05-13 |
| Phase 2 | paper_list.md 完成（84 本検証済） | ✅ 2026-05-13 |
| Phase 3a | PDF 収集（69/81、85%） | ✅ 2026-05-13 |
| **Phase 3b** | **個別 MD 69 本作成** | ✅ **2026-05-16** |
| **Phase 4-a** | **outcomes_master.csv + サブテーブル** | ✅ **2026-05-16** |
| **Phase 4-b** | **_index.md 統合更新** | ✅ **2026-05-16** |
| Phase 4-c | **日本語統合レビュー執筆** | ⏳ 次タスク |
| Phase 5 | （任意）HTML レポート化・GitHub Pages | ⏸ |

**次の作業**: [[md/_IntegratedReview_SmallAnnulusAVR_2026]] の執筆（5,000–8,000 語、PLAN §7 構成）。

---

*作成: 2026-05-13 | 更新: 2026-05-16 (Phase 3b + 4a/b 完了) | 関連: [[paper_list]] | [[HANDOFF]] | [[search_queries]] | [[PLAN]] | 個別論文: [[md/]]*
