---
title: "Impact of Prosthesis-Patient Mismatch After Surgical Aortic Valve Replacement: Systematic Review and Meta-Analysis of Reconstructed Time-to-Event Data of 122,989 Patients With 592,952 Patient-Years"
authors: "Michel Pompeu Sá, Xander Jacquemyn, Jef Van den Eynde, et al."
journal: "Journal of the American Heart Association"
citation: "J Am Heart Assoc 2024;13(7):e033176"
doi: "10.1161/JAHA.123.033176"
pmid: "38533939"
pdf: "[[small_annulus_avr/Reference/CatD_PPM/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024.pdf]]"
tags:
  - small-annulus
  - savr
  - ppm
  - severe-ppm
  - moderate-ppm
  - meta-analysis
  - reconstructed-ipd
  - aae
  - jaha
date: 2026-06-11
category: "PPM"
journal-abbr: "JAHA"
paper-type: "meta-analysis"
annulus-size: "not specified（集約; 小弁輪文献では女性88-91%が19/21mm弁と言及）"
patient-bsa: "mixed（集約; iEOA算出にBSA使用）"
valve-type: "mixed（bioprosthetic 16研究 / mechanical 7研究 / mix 42研究）"
enlargement-technique: "言及あり（PPM予防策としてNicks/Manouguian/Yang Y-incisionを考察）"
asian-cohort: "partial（1998-2023の65研究を統合、地域横断）"
ppm-rate: "any 55.6% / moderate 51.4% / severe 9.3%（重症度分離30研究）"
viv-discussion: "yes（index SAVRで大型弁を入れることが将来のViV-TAVRに有利と明記）"
sample-size: "n=122,989 patients (592,952 patient-years), 65 studies"
follow-up: "最大20-25年（study横断）"
---

> [!NOTE] Key Message
> 65研究・**122,989例 / 592,952 patient-years** のreconstructed IPD meta-analysisにより、Head 2012を大幅に更新。25年で any PPM の生存率は 11.8% vs 20.6%（**HR 1.16, 1.13-1.18**）。20年で重症度依存性が明瞭：moderate **HR 1.09 (1.06-1.11)**、**severe HR 1.29 (1.24-1.35)**。PPMは心臓死(any HR 1.57)・HF再入院(any HR 1.24)・severe弁再介入(HR 1.75)も増加させ、生体弁/機械弁・iEOA測定法（in vitro/in vivo/Doppler）を問わず一貫。女性比率が高い集団ほどPPMの死亡HRが上昇（メタ回帰 P=0.018）。

---

## 1. 背景
PPM（prosthesis-patient mismatch）は Rahimtoola(1978) が提唱、Pibarot/Dumesnil(2000) が iEOA で再定義した概念。iEOA <0.85 cm²/m² を回避すべき閾値とし、moderate=0.65-0.85、severe=<0.65（VARC-3ではBMI>30で severe <0.55）と定義。moderate PPMの予後影響は議論が続いており、SWEDEHEART(Dismorr 2023)は moderate を「臨床的に無視できる」、severe は10年で +4.6%死亡と報告した一方、STS DB は both moderate/severe で生存悪化を示し対立していた。本研究はKaplan-Meier曲線を再構成したreconstructed time-to-event data の pooled analysisで、moderate/severe PPMが SAVR後アウトカムに与える影響を最長20-25年で再評価。

## 2. 対象・方法
- N: 122,989患者 / 592,952 patient-years、**65 observational studies**（1998-2023; 全て非ランダム化、うち4研究はRCTの二次解析、11研究多施設、23研究前向き）
- 検索: PRISMA準拠、2023年3月15日まで（PubMed/MEDLINE, Embase, SciELO, LILACS, CENTRAL/CCTR, Google Scholar）。TAVR単独研究は除外、KM曲線必須。
- 年齢: 平均 約60-70歳、両群とも女性の代表性良好
- 弁種: mix 42研究 / 生体弁のみ 16研究 / 機械弁のみ 7研究
- iEOA測定法: in vitro 11研究 / in vivo 38研究 / Doppler心エコー 17研究
- PPM定義の時代変遷: cut-off 0.9→0.8 cm² から Pibarot 2000閾値、近年はBMI調整(VARC-3)へ
- 統計: IPDfromKM(v0.1.10)でKM曲線をデジタル化→IPD再構成（再構成曲線は全て99% CI内、RMSE≤0.05・MAE≤0.02達成）。Cox frailty model（γフレイルティ項）、RMST、Grambsch-Therneau検定、jackknife（leave-one-out）、線形混合効果メタ回帰、Begg検定（publication bias）。
- バイアス: 全体としてmoderate risk of bias 判定。

## 3. 主要結果

| Outcome | Result |
|---|---|
| 1年生存 (PPM有 vs 無) | 92.0% vs 93.4% |
| **25年生存 any PPM vs none** | **11.8% vs 20.6%（HR 1.16, 1.13-1.18, P<0.001）** |
| RMST差 (any PPM) | **-2年（11 vs 13年, P<0.001）** |
| 20年生存 none/mod/severe | 19.5% / 12.1% / 8.8% |
| **Moderate vs none (20y)** | **HR 1.09 (1.06-1.11), P<0.001** |
| **Severe vs none (20y)** | **HR 1.29 (1.24-1.35), P<0.001** |
| RMST差 mod / severe | -0.8年 / **-2.1年**（10.2・8.9 vs 11.0年） |
| HF再入院 any PPM (15y FFE 76.7%→70.9%) | HR 1.24 (1.19-1.30) |
| HF再入院 moderate / severe (15y) | 1.18 (1.13-1.24) / **1.59 (1.49-1.71)** |
| 心臓死 any PPM (15y) | **HR 1.57 (1.33-1.86)** |
| 心臓死 moderate / severe (15y) | 1.41 (1.11-1.79) / **2.04 (1.52-2.77)** |
| 弁再介入 moderate / severe (15y) | 0.98 (0.85-1.13, **n.s.**) / **1.75 (1.41-2.17)** |
| 生体弁 any PPM 全死亡 | HR 1.10 (1.06-1.15) |
| 機械弁 any PPM 全死亡 | **HR 1.63 (1.36-1.94)** |
| 機械弁 severe vs none | **HR 2.58 (1.80-3.69)** |
| in vitro / in vivo / Doppler (any) | 1.43 (1.31-1.56) / 1.13 (1.11-1.16) / 1.36 (1.18-1.57) |
| VARC-3 BMI調整定義 (2研究, any) | HR 1.07 (1.02-1.12), P=0.006 |

- **incidence**: any PPM 68,332例(55.6%)、重症度分離30研究で moderate 51.4% / severe 9.3%。生体弁50.9% vs 機械弁41.5%でPPM発生（P<0.001）。測定法別 incidence: in vitro 25.8% / in vivo 58.6% / Doppler 63.8%。
- **leave-one-out**: HR 1.14-1.21の範囲で安定。
- **メタ回帰**: 女性比率が高い集団ほど全死亡HR上昇（P=0.018）。年齢・PPM率・HTN・DM・腎不全・concomitant CABGは有意な修飾なし。

## 4. 議論
- Head 2012(34研究/27,186例)の決定版アップデート。フォローを20-25年へ延伸したことで、SWEDEHEART(15年で moderate -1.6% / severe -4.4%)より絶対差が拡大（20年で **moderate -7.4% / severe -10.7%**）。「追跡が長いほどPPMの悪影響は大きく顕在化する」と主張。
- RMST: SWEDEHEARTでは no PPMが mod より約2か月・severe より7か月長命にとどまったが、本研究では **mod より約10か月・severe より25か月** 長命。Mack/Adamsの「PPM回避の過熱を冷ますべき」論への直接反論。
- FinnValveが moderate PPMで有意差を出せなかったのは検出力不足と解釈。
- 機械弁でPPM発生は少ないが影響(HR)はむしろ大きい→「弁種より大EOA弁の植込みが重要」。
- **Doppler測定iEOAは低流量・pressure recovery未補正でPPMを過大評価**（severe率17%→1%へ予測iEOAで激減し得る）。これが測定法間の絶対差の違い(in vitro 4.4% / in vivo 8.4% / Doppler 28.3%)を説明。
- 女性はPPMリスクが高く、かつPPMの悪影響も増幅される（精密医療/性差の文脈）。

## 5. 本研究RQへの含意（最重要）
- **Primary RQ（Arm1 no-AAE SAVR vs Arm2 AAE-SAVR）**: 本meta-analysisは「severe PPM回避の臨床的正当化」の一次根拠。狭小弁輪・小柄アジア患者は構造的にsevere PPMに陥りやすく、severe PPMは20年全死亡HR 1.29・心臓死HR 2.04・HF再入院HR 1.59・弁再介入HR 1.75と一貫して悪化。AAE（Nicks/Manouguian/Konno/Y-incision）で大EOA弁を入れsevere PPMを避ける戦略の生存便益を間接支持する。著者自身が "How to Avoid PPM" 節でAREを主要手段と位置づけ、Yang Y-incision（2-5弁サイズ拡大、LA/MV非侵襲、median増分3サイズ、合併症ほぼ無し）を高評価しており、**SAKURA Arm2の技術的正当化**に直結。本研究のco-primary endpoint「severe PPM（measured iEOA ≤0.65）」はこの論文のsevere定義と完全一致。
- **重要な注意点（測定法）**: SAKURAは measured indexed EOA を採用するが、本論文は「Doppler measured iEOAは過大評価」と警告。SAKURAのsevere PPM率解釈・E-value感度分析で測定法バイアスを明示すべき根拠。in vivo HR 1.13に対しDoppler HR 1.36と効果量も異なる。
- **Secondary RQ（将来ViVのための最小初期弁サイズ／19mm可否）**: 著者は "index SAVRで大型弁を植えることがfailed bioprosthesisへのViV-TAVRで大きなTHVを入れられ予後改善につながる" と明記。さらにPPMはSVDを加速し弁再介入を増やす（severe弁再介入HR 1.75）。→ 初期に小弁(19mm)を許容するとPPM＋将来ViV failure双方を悪化させ、**初期に十分なEOAを確保すべき**論拠。
- **Tertiary RQ（アジア解剖特異戦略）**: メタ回帰で女性比率がPPM死亡HRを増幅。小弁輪文献では19/21mm弁受領者の88-91%が女性と引用されており、女性・小柄が多いアジア小弁輪集団でPPMの悪影響が最も顕在化しやすいことを示唆。SAKURAのアジア特異的AAE戦略の妥当性を支える。
- co-primary endpointのうち「1年平均圧較差」は本論文の直接対象外（生存/再入院/再介入/心臓死中心）。

## 6. 限界
- 全65研究が観察研究（非盲検・脱落あり）。PSMを試みた研究は少数で残余交絡は不可避。
- reconstructed IPDはKM由来で個人レベル共変量にアクセス不可→より頑健な調整解析が不能。
- HF再入院・弁再介入の解析対象はそれぞれ機械弁が3.3%・3.2%のみ（生体弁圧倒的優位）で、機械弁への外挿は要注意。
- 著明な between-study heterogeneity（全死亡・再介入でstudy×PPM交互作用P<0.001）→frailty model・stratified Coxで対処。
- TAVR患者は除外（ただしTAVRでもsevere PPMは死亡増加のエビデンスありと付言）。
- VARC-3 BMI調整定義を用いた研究は2本のみ。

## 7. 引用ハイライト
- Pibarot P, Dumesnil JG. JACC 2000;36:1131-1141（iEOA severe ≤0.65 閾値の原典）
- Dismorr et al. SWEDEHEART（moderate PPMは無視できると主張、本研究が反論）
- STS Adult Cardiac Surgery DB（moderate/severe ともに死亡・HF再入院・再介入増加; 10年生存 none 46% / mod 43% / severe 35%）
- Yang et al. Y-incision技術（median弁サイズ27、54%が29以上、median増分3弁サイズ、18か月生存100%）
- Ternacle/Pibarot（predicted iEOA使用でsevere率17%→1%; Doppler過大評価の補正）
- Tasoudis et al.（60-70歳で機械弁が生体弁に生存優位; n=17,983 meta-analysis）
