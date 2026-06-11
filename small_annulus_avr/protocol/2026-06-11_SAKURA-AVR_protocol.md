---
title: "SAKURA-AVR 研究プロトコル — 日韓多施設 狭小弁輪 SAVR 戦略比較コホート"
subtitle: "Small Annulus aortic valve replacement: Korea–japan United Research Analysis"
acronym: SAKURA-AVR
version: 0.1 (draft for collaborator review)
date: 2026-06-11
status: draft
design: retrospective multicenter comparative cohort (ambispective-extensible)
sites: ["Osaka University", "NCVC (国立循環器病研究センター)", "Korean center #1", "Korean center #2"]
corpus: "small_annulus_avr/ (69 papers + 統合レビュー)"
related:
  - "[[../md/_IntegratedReview_SmallAnnulusAVR_2026]]"
  - "[[../_index]]"
tags: [protocol, small-annulus, savr, aortic-annulus-enlargement, ppm, asian-cohort, multicenter]
---

# SAKURA-AVR 研究プロトコル（草案 v0.1）

> **Small Annulus aortic valve replacement: Korea–japan United Research Analysis**
> 日韓多施設・後ろ向き比較コホート研究プロトコル
> 作成: 2026-06-11 / ステータス: **共同研究者レビュー用 draft**

本プロトコルは `small_annulus_avr/` 統合レビュー（69本精読）が同定したエビデンス・ギャップ §10.2 のうち、**「Asian小体格における AAE-SAVR vs no-AAE SAVR の直接比較が存在しない」**（ギャップ①③④）を、当コンソーシアムが保有する臨床データで埋めることを目的とする原著研究の設計書である。

---

## 1. 背景と研究の根拠（Rationale）

### 1.1 臨床的問題

Yang ら（Univ Michigan）の **Y-incision aortic annular enlargement (AAE)**（JTCVS 2024）を契機に、欧米では「狭小弁輪に 3–4 弁サイズ大の人工弁を植え込み、severe PPM を回避し将来の ViV-TAVR margin を確保する」"Bigger is better" パラダイムが急速に標準化しつつある。ACC/AHA 2020・ESC/EACTS 2021 は狭小弁輪に対する root enlargement を narrative で支持する。

一方、**JCS 2020（日本）は同じ狭小弁輪＋予想 PPM に対して TAVI を推奨**しており、ガイドラインの方向性が逆転している。この乖離は、欧米コホート（BSA ≥1.8 m²、annulus mean 21mm）と Asian 小体格（BSA 1.3–1.5 m²、annulus 17–20mm、AM continuity 平均 8mm vs Caucasian 12–15mm）の解剖学的前提の差に根ざすと考えられる。

### 1.2 何が未解決か（統合レビューが同定したギャップ）

- **Y-incision/AAE vs no-AAE SAVR の直接比較 RCT が存在しない**（観察研究 PSM のみ、いずれも単施設・欧米）。
- **Asian 小体格における AAE の中期成績データがない**（Wang Fuwai n=53 が最大、早期のみ）。
- **AAE 後の僧帽弁機能/MR の系統的データがない**（Özçelik による severe central MR 初報告のみ。機序＝short aorto-mitral curtain は Asian 解剖でより顕在化しうる）。

### 1.3 新規性の確認（2026-06 時点）

最新文献検索の結果、Asian 多施設で外科的 **AAE vs no-AAE SAVR** を血行動態・中期予後で直接比較した研究は**存在しない**。近接研究はいずれも対象が異なる:

- East Asian の TAVI device 選択（self vs balloon、supra vs intra-annular）— JACC: Asia 2024 ほか。
- Sutureless SAVR vs TAVI（multi-institutional, 2024）。
- BE-TAVI small vs large annulus（2026, n=3,182; small で mean PG ≥20mmHg 14.1% vs 2.9%、severe PPM 9.8% vs 5.2%）。

→ **外科戦略（AAE か否か）を Asian 小体格で比較する空白は開いたまま**であり、本研究が初となる。

### 1.4 必須追加文献（**取得・要約済み 2026-06**）

以下は corpus 未収載だった必須文献で、**2026-06 に取得・精読 MD 化して corpus に統合済み**（[[../_index]] §5「2026-06 追加」）:

1. **Sá MP et al. JAHA 2024**（[[../md/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024]]）— SAVR 後 PPM の reconstructed time-to-event meta（**122,989例・592,952 patient-years**）。Head 2012 を更新。severe 20yr 全死亡 HR 1.29・心臓死 HR 2.04。**primary outcome（severe PPM 回避）の臨床的正当化**。
2. **VARC-3 2021**（[[../md/Genereux_VARC3EndpointDefinitions_EHJ_2021]]）— エンドポイント標準化（PPM・HVD/SVD・出血）。
3. **Makkinejad AnnThoracSurg 2025**（[[../md/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025]]）— **本研究に最も近い先行研究**：matched ≤23mm 弁輪で AAE vs isolated AVR を PSM 112 pair 比較、6yr 生存 98% vs 74%・AAE 中期死亡 HR 0.19。SAKURA が補完すべき gap（measured-EOA PPM co-primary・Asian small-body・TAVI reference・postop echo 完備）を明確化。
4. **Tanaka AnnCardiothoracSurg 2024**（[[../md/Tanaka_AorticAnnularEnlargementOutcomesMetaAnalysis_AnnCardiothoracSurg_2024]]）— AAE メタ解析：マッチ後死亡差なし・**severe PPM RR 0.61**。AAE アームの morbidity/mortality ベンチマーク。
5. **Abushouk JACC CI 2023**（[[../md/Abushouk_MeasuredVsPredictedPPM_JACCCardiovascInterv_2023]]）— measured vs predicted iEOA：予測は PPM を系統的過小評価。**co-primary を measured iEOA とする設計の citable authority**。
6. **RHEIA / Tchétché EHJ 2025**（[[../md/Tchetche_RHEIAtrialTAVIvsSAVRWomen_EHJ_2025]]）— 女性限定 TAVI vs SAVR RCT。外科群は AAE ゼロ＝実質 no-AAE 対照。TAVI 参照アームの最良級 RCT ベンチマーク。
7. 比較考察用: [[../md/Suruga_SmallVsLargeAnnulusBalloonExpandableTAVR_JAHA_2026]]（BE-TAVR small vs large）、[[../md/DiBacco_SuturelessVsTAVISmallAnnulusMultiInstitutional_BrazJCardiovascSurg_2024]]（sutureless vs TAVI）、[[../md/Chen_EastAsianTAVRdeviceSelectionSmallAnnulus_JACCAsia_2025]]（East Asian device 選択）。
8. 統計方法論（CatJ_Methods）: E-value（[[../md/VanderWeele_EValueSensitivityAnalysis_AnnInternMed_2017]]）、PSM バランス診断 SMD<0.1（[[../md/Austin_PSMbalanceDiagnostics_StatMed_2009]]）、STROBE（[[../md/vonElm_STROBEStatement_PLoSMed_2007]]）。

**未取得（DL困難・後日）**: Yamamoto EuroIntervention 2025（PCRログイン／PMC OA 2026-11-14解除）、Do-Nguyen ACTA 2026（SAGE）。

---

## 2. 研究目的と仮説

### 2.1 Primary objective

狭小弁輪（measured annulus diameter ≤23mm、≤21mm を主要層）かつ小体格の AS 患者で、**AAE-SAVR は no-AAE SAVR と比較して severe PPM を減らし術後 mean gradient を低下させるか**を、日韓多施設データの傾向スコア調整下で定量する。

### 2.2 Primary hypothesis（co-primary、階層的検定）

- **H1（血行動態）**: AAE-SAVR は no-AAE SAVR と比較して **severe PPM 率が低い**（measured iEOA ≤0.65 cm²/m²、術後退院前/30日 echo）。
- **H2（血行動態）**: AAE-SAVR は no-AAE SAVR と比較して **1年 mean transvalvular gradient が低い**。
- 検定順序: H1 → H2 の階層的（gatekeeping）。H1 有意でなければ H2 は探索的扱い。

### 2.3 Secondary / safety objectives

- **主要副次（臨床）**: 中期（最長5年）全死亡・MACE を Cox/Kaplan–Meier で比較。
- **安全性副次（事前規定・Özçelik signal）**: AAE 群における **新規 ≥moderate MR 発生率・僧帽弁再介入率・僧帽弁幾何（available なら echo 指標）**。AM continuity が短い Asian 解剖での AAE 安全域を検証する本研究固有の論点。
- **参照比較（TAVI arm）**: self-expanding TAVI を事前規定の参照群とし、血行動態（severe PPM、mean gradient）を no-AAE / AAE 各群と記述的＋IPTW 補正下で比較（因果結論ではなく landscape 提示）。
- **探索的**: ViV feasibility surrogate（植込み弁 internal diameter ≥21mm 達成割合、D'Onofrio 2016 閾値）、PPI 率、AAE 群の術式別（Nicks/Manouguian/Y-incision/Y-and-I）サブ解析。

---

## 3. 研究デザイン

- **デザイン**: 後ろ向き多施設比較コホート（第1弾）。将来の前向き registry 拡張を見据えた ambispective-extensible 設計。
- **施設**: 阪大、NCVC、韓国2施設（計4施設、日韓）。lead/coordinating center は別途決定。
- **観察期間（症例登録対象）**: **2015-01-01 〜 2024-12-31（10年）**。理由＝modern bioprosthesis（Inspiris 2017–、Avalus）、Evolut/Sapien 3、および Y-incision（2021–）の時代を包含。
  - 注意: Y-incision は 2021 年以降に偏るため、**暦年を共変量＋感度解析で調整**（§7.5）。
- **追跡**: 各施設の最終 echo・生存情報まで。最低 1 年 echo を血行動態 co-primary の窓とする。

---

## 4. 対象集団

### 4.1 包含基準

1. 成人（≥18歳）。
2. **狭小弁輪**に対する初回 AVR（SAVR または TAVI）。狭小弁輪の定義（harmonized、§4.3）:
   - SAVR: 術中サイザー実測 or 術前 CT/TTE で **aortic annulus diameter ≤23mm**（**≤21mm を事前規定の主要層**）。
   - TAVI: CT 計測 **annulus area ≤430mm²**（SMART 基準）または derived diameter ≤23mm。
3. 主病態が **大動脈弁狭窄（AS 優位、AS/AR mixed 含む）**。

### 4.2 除外基準

- 活動性感染性心内膜炎、急性大動脈解離。
- **大動脈基部置換（Bentall/root replacement）**、David/Yacoub。
- **同時施行の他弁手術（僧帽弁・三尖弁置換/形成）**（※ CABG 同時は許容、共変量化）。
  - 例外検討: AAE + concomitant MV は corpus の重要トピック（Cangut/Gan）だが、主要解析の arm 純度を保つため**主要解析から除外し、別途記述**。
- 純粋 AR（AS 要素なし）、先天性/小児、redo（既存人工弁に対する手術＝ViV/explant は別解析）。

### 4.3 狭小弁輪定義の調和（方法論的論点）

SAVR（術中サイザー/外科弁ラベルサイズ）と TAVI（CT annulus area）で計測モダリティが異なる。**各症例の生データ（measured annulus diameter, area, 計測法）を eCRF に記録**し、解析時に diameter ベースで統一。主要解析は SAVR 2 群間（同一モダリティ）で行うため、この調和問題は TAVI 参照比較に限局する。

---

## 5. 曝露（アーム）定義

| Arm | 定義 | 主要解析での位置づけ |
|---|---|---|
| **Arm 1: no-AAE SAVR** | 弁輪拡大を伴わない外科的 AVR。supra-annular 生体弁、interrupted suturing、機械弁、**sutureless/rapid-deployment** を含む | **主要対比（対照）** |
| **Arm 2: AAE-SAVR** | Nicks / Manouguian / Konno / **Y-incision / Y-and-I** を伴う外科的 AVR | **主要対比（曝露）** |
| **Arm 3: TAVI（参照）** | self-expanding TAVI を主参照（BE-TAVI はサブ） | **事前規定の参照群（副次・記述）** |

**事前規定の感度解析**（§7.5）:
- 生体弁限定（機械弁除外）— 血行動態 primary を弁種で純化。
- sutureless 除外（Arm 1 を従来縫着生体弁に限定）。
- Y-incision 限定 vs 古典 AAE（Arm 2 内サブ）。

---

## 6. エンドポイント定義

### 6.1 Co-primary（血行動態）

1. **Severe PPM**: **measured iEOA ≤0.65 cm²/m²**（退院前/30日 echo）。
   - **重要な方法論的選択**: corpus の Pibarot 2020（EHJ-CI）が示す通り、**reference-chart projected EOA は約30%を誤分類**する。本研究は **doppler 実測 EOA / BSA（measured iEOA）を一次採用**し、projected iEOA は感度解析でのみ用いる。これは本研究の方法論的強みであり、査読対応の核。
2. **1年 mean transvalvular gradient**（TTE)。

### 6.2 主要副次（臨床、VARC-3 準拠）

- 全死亡（30日、1年、中期最長5年）、心臓関連死。
- MACE（死亡・脳卒中・弁関連再入院の複合）。
- SVD（VARC-HBV/VARC-3 hemodynamic valve deterioration）、弁再介入。

### 6.3 安全性副次（事前規定）

- **新規 ≥moderate MR 発生**（退院前・1年）、**僧帽弁再介入**。AAE 群で重点評価（Özçelik signal）。
- PPI（恒久ペースメーカー）、術後 AKI、脳卒中、出血（VARC-3）。

### 6.4 探索的

- 植込み弁 internal diameter ≥21mm 達成割合（ViV margin surrogate）。
- 術式別（AAE 4 法）血行動態・MR。
- CPB/遮断時間（AAE の侵襲コスト）。

---

## 7. 統計解析計画

### 7.1 主要対比と交絡調整

- **主要対比**: Arm 2 (AAE) vs Arm 1 (no-AAE)、**1:1 傾向スコアマッチング（caliper 0.2×SD of logit PS）**を主、**IPTW を感度解析**。
- バランス評価: 標準化平均差（SMD）<0.10 を目標。
- PS モデル共変量（Asian 特異性を重視）: 年齢、**性別**、**BSA**、**measured annulus diameter**、LVEF、NYHA、STS-PROM/EuroSCORE II、AF、CKD/透析、糖尿病、COPD、冠動脈疾患/同時 CABG、**暦年**、**施設**、弁種（生体/機械）。

### 7.2 Co-primary の検定

- 階層的 gatekeeping（H1: severe PPM → H2: 1年 gradient）で多重性を制御、両側 α=0.05。
- severe PPM: マッチ後 conditional logistic / クラスタ頑健 GEE。1年 gradient: 線形混合モデル（施設変量効果）。

### 7.3 生存・時間依存アウトカム

- Kaplan–Meier ＋ マッチ層別 Cox。competing risk（弁関連 vs 非弁関連死）には Fine–Gray。

### 7.4 欠測

- echo 欠測・追跡欠測は **multiple imputation（MICE）**。1年 echo 欠測率を記述し、complete-case を感度解析。

### 7.5 事前規定の感度・サブ解析

1. 生体弁限定 / sutureless 除外 / Y-incision 限定。
2. annulus ≤21mm 主要層に限定。
3. 暦年調整（2021 以降の Y-incision 偏りを補正）、施設別ランダム効果。
4. projected iEOA による severe PPM 再分類（measured との一致度＝Pibarot 2020 検証）。
5. TAVI 参照群 vs 各外科 arm（IPTW、記述）。

### 7.6 サンプルサイズ／検出力（暫定・要 feasibility census）

corpus 由来の効果量で暫定設計（最終値は §9 の census 後に確定）:

- severe PPM: no-AAE ≈ **15–25%**（Asian 小弁輪 SAVR; Tabata の moderate-severe 29–56% 等から保守的推定）vs AAE ≈ **5–7%**（Makkinejad PSM: 5.5%）。
  - 差 15% vs 5% を α=0.05・power 0.80 で検出 → 各群 **≈130例（計260）**。差 20% vs 6% なら 各群 ≈70。
- **制約は AAE 群の症例数**（Y-incision は 2021–）。4 施設 ×（AAE 年間例数）が律速。**§9 feasibility census で AAE 実数を最優先確認**。
- 1年 gradient（連続量）は同 N で十分な検出力（Makkinejad 7 vs 10mmHg, SD≈4）。

---

## 8. データ管理・ガバナンス

- **eCRF**: REDCap 等で共通項目を統一（annulus 生計測、弁種/サイズ/モデル、術式詳細、全 echo 時系列、追跡）。
- **匿名化**: 各施設で de-identify 後にプール。患者識別子は施設内に留置。
- **倫理**: 各施設 IRB 承認（後ろ向き・オプトアウト想定）、**日韓間データ共有契約（DTA）** と各国個人情報法（日本: 次世代医療基盤法/個情法、韓国: PIPA）遵守。
- **echo 標準化**: 可能なら **core-lab 中央判定** または標準化 re-read プロトコル（iEOA・gradient 計測の施設間ばらつきが co-primary の最大バイアス源）。
- **登録**: UMIN-CTR / ClinicalTrials.gov 事前登録。報告は **STROBE** 準拠。

---

## 9. 実行計画（マイルストン）

| Phase | 内容 | 主目的 |
|---|---|---|
| **P0: Feasibility census（最優先）** | 4施設で 2015–2024 の小弁輪 AVR 概数・**特に AAE 実例数**・echo 追跡可用性を集計 | サンプルサイズ確定・実現可能性判定 |
| P1: プロトコル確定・SAP | 本草案を共同研究者レビュー→統計解析計画（SAP）固定 | 事前登録 |
| P2: IRB / DTA | 各施設 IRB、日韓 DTA、事前登録 | 法的整備 |
| P3: eCRF 構築・データ収集 | REDCap・echo 収集（core-lab 検討） | データセット構築 |
| P4: 解析 | PSM/IPTW・co-primary・感度解析 | 結果 |
| P5: 論文化 | 原著（target: JTCVS / EJCTS / Circ J / Semin TCVS / JACC: Asia） | 出版 |

---

## 10. 限界・想定バイアスと対策

- **残存交絡**（非無作為）→ PSM＋IPTW、E-value による頑健性評価。
- **時代効果**（Y-incision 2021–）→ 暦年共変量・感度解析。
- **echo 計測の施設間異質性** → core-lab/標準化 re-read。
- **適応バイアス**（誰に AAE/TAVI を選ぶか）→ PS モデルに術前重症度・解剖を厚く投入、適応情報を eCRF 化。
- **AAE 群の N 不足リスク** → P0 census で早期判定、不足時は Arm 2 を「AAE 全法プール」で運用、または前向き拡張へ移行。
- **measured vs projected EOA** → measured を一次、両者一致度を報告（corpus Pibarot 2020 を直接活用）。

---

## 11. 期待されるインパクト

1. **ガイドライン乖離（JCS vs ACC/ESC）に Asian 実データで一次エビデンスを提供**。
2. Asian 小体格における **AAE の真の上乗せ効果と安全域（MR signal 含む）** を世界で初めて多施設比較。
3. corpus 統合レビューの中心命題（「一律 AAE は正当化されない」）を、当該集団そのもので検証する確証研究。

---

## 12. 共同研究者レビューで決めるべき open items

1. **狭小弁輪の閾値**: 主要層 ≤21mm で確定か、≤23mm 主軸に広げるか。
2. **機械弁の扱い**: 主要解析に含めるか（Asian 若年女性で 17–19mm Regent が一定数）、生体弁限定を主にするか。
3. **sutureless の配置**: Arm 1 内か、独立 arm か。
4. **TAVI 参照群**: self-expanding 限定か BE 含むか。
5. **追跡窓**: co-primary を「退院前 severe PPM」のみにして N を最大化するか、「1年 echo 必須」を堅持するか。
6. **lead center / 著者順 / オーサーシップ規約**。
7. **echo core-lab** を置くか（コスト vs バイアス低減）。

---

## 付録 A: corpus 由来ベンチマーク（設計根拠）

| 指標 | 値 | 出典（corpus） |
|---|---|---|
| Y-incision vs Nicks/Manouguian severe PPM（PSM 103 pair） | 5.5% vs 23.0% (P=0.039) | Makkinejad AnnCardiothoracSurg 2024 |
| Y-incision vs traditional AAE severe PPM（n=202） | 6.9% vs 26% (P=0.005) | Makkinejad AnnThoracSurg 2025 |
| Y-incision postop mean gradient | 6–7 mmHg | Yang JTCVS 2024 / Chen 2025 |
| Nicks ARE vs sutureless severe PPM | 11% vs 6% (n.s.) | Beckmann ICVTS 2016 |
| 日本人 interrupted suturing moderate-severe PPM | 29% vs mattress 56% | Tabata JTCVS 2014 |
| severe PPM 長期全死亡 HR | 1.84 (1.38–2.45)；**Sá 2024: severe 20yr HR 1.29・心臓死 HR 2.04** | Head EHJ 2012 / [[../md/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024]] |
| **AAE vs isolated AVR（matched ≤23mm, PSM 112pair）6yr 生存** | **98% vs 74%**（AAE 中期死亡 HR 0.19, 0.06–0.62） | [[../md/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025]] |
| **AAE メタ severe PPM（iEOA≤0.65）** | **RR 0.61 (0.40–0.93)** | [[../md/Tanaka_AorticAnnularEnlargementOutcomesMetaAnalysis_AnnCardiothoracSurg_2024]] |
| AAE 後 severe central MR | 初報告（POD50 で MVR） | Özçelik 2026 |

## 付録 B: 関連内部資料

- 統合レビュー: [[../md/_IntegratedReview_SmallAnnulusAVR_2026]]（§10.2 ギャップ、§9 アルゴリズム）
- ハブ: [[../_index]]（§6 Key Numbers, §4 参照マップ）
- 抽出データ: `../tables/outcomes_master.csv` / `ppm_landscape.csv` / `asian_cohort_subset.csv`

---

*草案 v0.1 / 2026-06-11 / SAKURA-AVR / 次段階: feasibility census（P0）と共同研究者レビュー*
