# DOI検証ログ — 2026年7月号まとめ（＋6月号EJCTS追補）

> 検証日: 2026-07-26
> 対象: `MD/cardiac_surgery_journals_2026_07.md`（7月号）および `MD/cardiac_surgery_journals_2026_06.md` EJCTS追補分
> 手法: PubMed E-utilities で各号TOCを取得 → 全DOIを CrossRef `/works/{DOI}` で個別照合し、
> 返却タイトル・巻・号・頁を PubMed 由来メタデータと突合

## サマリ

| 項目 | 件数 |
|---|---|
| 検証対象DOI（重複除去後） | **148** |
| ✅ タイトル一致 | 147 |
| ⚠️ CrossRef未登録（新着・PubMedで確認） | 1 |
| ❌ 別論文を指していたDOI | **0** |

### 注記

1. **CrossRef未登録 1件**: `10.1016/j.healun.2026.07.023`（Gomes DO, et al. *When "Not A Candidate" Becomes a Verdict*, JHLT Online-First 2026-07-25）
   — 公開直後のためCrossRefに未反映（HTTP 404）。PubMed（PMID 42501876）でタイトル・著者・DOIを確認済み。
2. **副題表記差 1件**: `10.1016/j.jtcvs.2026.07.003`（Sellke FW. *Commentary: Why do we still not know what causes vasoplegia?*）
   — PubMedは対象論文名を含む長い副題を保持、CrossRefは本題のみ。**同一論文**であることを著者・巻号で確認。
3. **EJCTSの頁番号**: OUPは連続頁ではなく論文ID（`ezagXXX`）を用いるため、CrossRefの `article-number` を頁欄に記載。
4. **JTCVSの巻**: JTCVSは半年ごとに巻が変わるため、2026年7月号は **Vol.172 Issue 1**（6月号 Vol.171(6) の次）。
   当初 `171[volume] AND 7[issue]` で検索した際に0件となった原因であり、次回以降も注意。
5. **EJCTS Issue 7 は組版継続中**: 2026-07-26時点で確定10編（Issue 5=23編、Issue 6=14編）。8月に追補予定。

## 検証テーブル（全148件）

| # | 号 | タイトル（短縮） | DOI | CrossRef巻(号) 頁 | 検証結果 |
|---|---|---|---|---|---|
| 1 | EJCTS 68(6) | Corrigendum to: Colchicine prevents perioperative myocardial inj | 10.1093/ejcts/ezag172 | 68(6) ezag172 | ✅ タイトル一致 |
| 2 | EJCTS 68(6) | Oncologic Safety of Omitting Mediastinal Lymph Node Dissection i | 10.1093/ejcts/ezag184 | 68(6) ezag184 | ✅ タイトル一致 |
| 3 | EJCTS 68(6) | Progress in Thymic Malignancy Care: The Imperative for Global St | 10.1093/ejcts/ezag178 | 68(6) ezag178 | ✅ タイトル一致 |
| 4 | EJCTS 68(6) | The EACTS Innovation Committee's Perspective on the "Heart Valve | 10.1093/ejcts/ezag185 | 68(6) ezag185 | ✅ タイトル一致 |
| 5 | EJCTS 68(6) | Why Should the Current Generation of Surgical Residents be Acade | 10.1093/ejcts/ezag113 | 68(6) ezag113 | ✅ タイトル一致 |
| 6 | EJCTS 68(6) | Artificial Pancreas and Continuous Insulin Infusion for Preventi | 10.1093/ejcts/ezag166 | 68(6) ezag166 | ✅ タイトル一致 |
| 7 | EJCTS 68(6) | How Did I Came Up With the Idea of Using the Right Gastroepiploi | 10.1093/ejcts/ezag180 | 68(6) ezag180 | ✅ タイトル一致 |
| 8 | EJCTS 68(6) | The Austrian Adult Cardiac Surgery Registry: Structure and Gover | 10.1093/ejcts/ezag179 | 68(6) ezag179 | ✅ タイトル一致 |
| 9 | EJCTS 68(6) | A Conversation in Baltimore: The Origins of EACTS. | 10.1093/ejcts/ezag181 | 68(6) ezag181 | ✅ タイトル一致 |
| 10 | EJCTS 68(6) | Valve-sparing Aortic Root Replacement: Defining High-volume Cent | 10.1093/ejcts/ezag177 | 68(6) ezag177 | ✅ タイトル一致 |
| 11 | EJCTS 68(6) | Robotic-Assisted Paediatric Lung Anatomical Resection: A Safe Al | 10.1093/ejcts/ezag176 | 68(6) ezag176 | ✅ タイトル一致 |
| 12 | EJCTS 68(6) | Full Micro-Axial Flow Pump, With or Without V-A ECLS, Towards Du | 10.1093/ejcts/ezag173 | 68(6) ezag173 | ✅ タイトル一致 |
| 13 | EJCTS 68(6) | Pulmonary Artery Sarcoma Study: A Multi-Centre European Society  | 10.1093/ejcts/ezag133 | 68(6) ezag133 | ✅ タイトル一致 |
| 14 | EJCTS 68(6) | Early Outcomes of Extracorporeal Membrane Oxygenation in Congeni | 10.1093/ejcts/ezag123 | 68(6) ezag123 | ✅ タイトル一致 |
| 15 | EJCTS 68(7) | Which Patient- and Procedure-Related Factors Predict Spinal Cord | 10.1093/ejcts/ezag196 | 68(7) ezag196 | ✅ タイトル一致 |
| 16 | EJCTS 68(7) | What Is the 20-Year Durability of a Surgical Tricuspid Bioprosth | 10.1093/ejcts/ezag191 | 68(7) ezag191 | ✅ タイトル一致 |
| 17 | EJCTS 68(7) | From Organizations to People-Rethinking Leadership. | 10.1093/ejcts/ezag186 | 68(7) ezag186 | ✅ タイトル一致 |
| 18 | EJCTS 68(7) | Corrigendum to: 2025 ESC/EACTS Guidelines for the management of  | 10.1093/ejcts/ezag193 | 68(7) ezag193 | ✅ タイトル一致 |
| 19 | EJCTS 68(7) | Corrigendum to: EACTS/STS Guidelines for Diagnosing and Treating | 10.1093/ejcts/ezag194 | 68(7) ezag194 | ✅ タイトル一致 |
| 20 | EJCTS 68(7) | The Imperative of Excellence: Why Average Is No Longer the Measu | 10.1093/ejcts/ezag192 | 68(7) ezag192 | ✅ タイトル一致 |
| 21 | EJCTS 68(7) | The Radial Artery in Melbourne: Introduction, Evolution, Lessons | 10.1093/ejcts/ezag197 | 68(7) ezag197 | ✅ タイトル一致 |
| 22 | EJCTS 68(7) | Colchicine for Prevention of Perioperative Atrial Fibrillation a | 10.1093/ejcts/ezag190 | 68(7) ezag190 | ✅ タイトル一致 |
| 23 | EJCTS 68(7) | Mitral Valve Anomalies in Transposition of the Great Arteries. | 10.1093/ejcts/ezag189 | 68(7) ezag189 | ✅ タイトル一致 |
| 24 | EJCTS 68(7) | Association Between Interventional Cardiologist Practice Charact | 10.1093/ejcts/ezag188 | 68(7) ezag188 | ✅ タイトル一致 |
| 25 | EJCTS OF | The role of selective multidetector computed tomography after tr | 10.1093/ejcts/ezag200 | () ezag200 | ✅ タイトル一致 |
| 26 | EJCTS OF | My journey of internal thoracic artery grafting. | 10.1093/ejcts/ezag195 | () ezag195 | ✅ タイトル一致 |
| 27 | JTCVS 172(1) | Reply: Importance of clinical context in choice of analytical me | 10.1016/j.jtcvs.2026.02.033 | 172(1) e10-e11 | ✅ タイトル一致 |
| 28 | JTCVS 172(1) | Pulmonary carcinoid tumors and diffuse idiopathic pulmonary neur | 10.1016/j.jtcvs.2026.03.609 | 172(1) 24-31 | ✅ タイトル一致 |
| 29 | JTCVS 172(1) | Prospectively screening for venous thromboembolism in patients w | 10.1016/j.jtcvs.2026.02.038 | 172(1) 43-50.e11 | ✅ タイトル一致 |
| 30 | JTCVS 172(1) | Impact of reoperation on very long-term survival in patients wit | 10.1016/j.jtcvs.2026.03.595 | 172(1) 84-94.e2 | ✅ タイトル一致 |
| 31 | JTCVS 172(1) | Itaconate supplementation leads to improvement in donor lung fun | 10.1016/j.jtcvs.2026.03.570 | 172(1) 51-65.e7 | ✅ タイトル一致 |
| 32 | JTCVS 172(1) | Mid-term outcomes after aortic valve repair with the internal ge | 10.1016/j.jtcvs.2026.03.573 | 172(1) 76-83 | ✅ タイトル一致 |
| 33 | JTCVS 172(1) | Surgery versus definitive radiotherapy after induction immunoche | 10.1016/j.jtcvs.2026.03.567 | 172(1) 11-23.e9 | ✅ タイトル一致 |
| 34 | JTCVS 172(1) | Reply: The simplicity trap: Why simplest answers are not always  | 10.1016/j.jtcvs.2026.02.008 | 172(1) e17-e18 | ✅ タイトル一致 |
| 35 | JTCVS 172(1) | Reply: Tricuspid annulus repair-Quo vadis? | 10.1016/j.jtcvs.2026.01.028 | 172(1) e4-e6 | ✅ タイトル一致 |
| 36 | JTCVS 172(1) | Large airway bronchial wash lipidomics as novel biomarkers for c | 10.1016/j.jtcvs.2026.02.029 | 172(1) 66-75.e4 | ✅ タイトル一致 |
| 37 | JTCVS 172(1) | Biventricular repair in symptomatic neonates with Ebstein anomal | 10.1016/j.jtcvs.2026.02.023 | 172(1) 185-190 | ✅ タイトル一致 |
| 38 | JTCVS 172(1) | Using preoperative cardiac computed tomographic conduction axis  | 10.1016/j.jtcvs.2026.02.028 | 172(1) 176-184.e2 | ✅ タイトル一致 |
| 39 | JTCVS 172(1) | Considerations on methodologic aspects of the Impella 5.5 study  | 10.1016/j.jtcvs.2026.01.029 | 172(1) e9 | ✅ タイトル一致 |
| 40 | JTCVS 172(1) | Reply: Not so fast! The case against a definitive shift to vasop | 10.1016/j.jtcvs.2026.01.014 | 172(1) e15-e16 | ✅ タイトル一致 |
| 41 | JTCVS 172(1) | Pathologic response and nodal status guide adjuvant immunotherap | 10.1016/j.jtcvs.2026.02.025 | 172(1) 1-10.e14 | ✅ タイトル一致 |
| 42 | JTCVS 172(1) | Diaphragm dysfunction following congenital heart surgery: Epidem | 10.1016/j.jtcvs.2026.02.024 | 172(1) 200-208.e3 | ✅ タイトル一致 |
| 43 | JTCVS 172(1) | Oxygen extraction trajectories during cardiopulmonary bypass imp | 10.1016/j.jtcvs.2026.02.018 | 172(1) 104-113.e6 | ✅ タイトル一致 |
| 44 | JTCVS 172(1) | Pathologic complete response after neoadjuvant immunochemotherap | 10.1016/j.jtcvs.2026.02.017 | 172(1) 32-42.e8 | ✅ タイトル一致 |
| 45 | JTCVS 172(1) | A decade of reoperative adult cardiac surgery with Del Nido card | 10.1016/j.jtcvs.2026.02.006 | 172(1) 118-127.e9 | ✅ タイトル一致 |
| 46 | JTCVS 172(1) | Commentary: May the best intervention win: Nuances when interpre | 10.1016/j.jtcvs.2026.02.007 | 172(1) 138-139 | ✅ タイトル一致 |
| 47 | JTCVS 172(1) | Vasopressin leads to a lower pulmonary vascular resistance than  | 10.1016/j.jtcvs.2026.01.015 | 172(1) e17 | ✅ タイトル一致 |
| 48 | JTCVS 172(1) | Long-term outcomes of aortic valve repair in children after infa | 10.1016/j.jtcvs.2026.01.034 | 172(1) 164-175.e7 | ✅ タイトル一致 |
| 49 | JTCVS 172(1) | Optimizing safety in same-day discharge after video-assisted tho | 10.1016/j.jtcvs.2026.01.007 | 172(1) e2 | ✅ タイトル一致 |
| 50 | JTCVS 172(1) | The association between the Distressed Communities Index and fai | 10.1016/j.jtcvs.2026.01.025 | 172(1) 150-158.e7 | ✅ タイトル一致 |
| 51 | JTCVS 172(1) | Internal mammary artery grafting: The gold standard of coronary  | 10.1016/j.jtcvs.2026.01.021 | 172(1) 114-117 | ✅ タイトル一致 |
| 52 | JTCVS 172(1) | Septal annular remodeling and durability of tricuspid repair in  | 10.1016/j.jtcvs.2025.12.023 | 172(1) e4 | ✅ タイトル一致 |
| 53 | JTCVS 172(1) | Randomized, sham-controlled trial of intraoperative ticagrelor r | 10.1016/j.jtcvs.2026.01.012 | 172(1) 128-137.e4 | ✅ タイトル一致 |
| 54 | JTCVS 172(1) | Multidisciplinary blood conservation practices for transfusion-f | 10.1016/j.jtcvs.2026.01.011 | 172(1) 209-215.e2 | ✅ タイトル一致 |
| 55 | JTCVS 172(1) | Reply: RITA is identical to LITA, and only the surgeon can inter | 10.1016/j.jtcvs.2025.11.023 | 172(1) e7-e8 | ✅ タイトル一致 |
| 56 | JTCVS 172(1) | Reply: From perfusion to precision: Integrating real-time monito | 10.1016/j.jtcvs.2025.12.010 | 172(1) e13-e14 | ✅ タイトル一致 |
| 57 | JTCVS 172(1) | Distinguishing mechanism from efficacy: Clinical trial evidence  | 10.1016/j.jtcvs.2025.12.006 | 172(1) e14-e15 | ✅ タイトル一致 |
| 58 | JTCVS 172(1) | Clinical outcomes after COVID-19-positive donor heart transplant | 10.1016/j.jtcvs.2025.12.022 | 172(1) 191-199.e5 | ✅ タイトル一致 |
| 59 | JTCVS 172(1) | From Declaration to Delivery: Cardiac Surgery Unites for Global  | 10.1016/j.jtcvs.2025.12.011 | 172(1) 159-162 | ✅ タイトル一致 |
| 60 | JTCVS 172(1) | Arterial revision and recycling of coronary bypasses for longevi | 10.1016/j.jtcvs.2025.11.012 | 172(1) e7 | ✅ タイトル一致 |
| 61 | JTCVS 172(1) | Tricuspid annular remodeling in tachycardia induced cardiomyopat | 10.1016/j.jtcvs.2025.12.008 | 172(1) 95-103 | ✅ タイトル一致 |
| 62 | JTCVS 172(1) | Artificial intelligence-based prediction of cardiothoracic inten | 10.1016/j.jtcvs.2025.11.020 | 172(1) 140-149.e5 | ✅ タイトル一致 |
| 63 | JTCVS 172(1) | Beyond perfusion strategy: The case for real-time multimodal neu | 10.1016/j.jtcvs.2025.11.003 | 172(1) e12-e13 | ✅ タイトル一致 |
| 64 | JTCVS OF | Survivorship bias and utility of the black box in preoperative F | 10.1016/j.jtcvs.2026.02.021 | () | ✅ タイトル一致 |
| 65 | JTCVS OF | Reply: Compensation without resection: Volume changes and functi | 10.1016/j.jtcvs.2026.06.017 | () | ✅ タイトル一致 |
| 66 | JTCVS OF | Commentary: When Does Size Matter? | 10.1016/j.jtcvs.2026.06.022 | () | ✅ タイトル一致 |
| 67 | JTCVS OF | Incidence and outcomes of left atrioventricular valve reoperatio | 10.1016/j.jtcvs.2026.07.009 | () | ✅ タイトル一致 |
| 68 | JTCVS OF | Sex Differences in Postoperative Atrial Fibrillation and Posteri | 10.1016/j.jtcvs.2026.07.008 | () | ✅ タイトル一致 |
| 69 | JTCVS OF | What Twenty-Five Years Teach Us About Surgery for Infective Endo | 10.1016/j.jtcvs.2026.07.007 | () | ✅ タイトル一致 |
| 70 | JTCVS OF | Factors Associated With Tracheoplasty in Children With Pulmonary | 10.1016/j.jtcvs.2026.07.006 | () | ✅ タイトル一致 |
| 71 | JTCVS OF | Aortic Root Replacement in Adult Patients with Repaired Congenit | 10.1016/j.jtcvs.2026.05.029 | () | ✅ タイトル一致 |
| 72 | JTCVS OF | Proteomic, Transcriptomic, and Metabolic Mediators of Post-Cardi | 10.1016/j.jtcvs.2026.06.026 | () | ✅ タイトル一致 |
| 73 | JTCVS OF | Outcomes and treatment of early detectable donor-specific anti-H | 10.1016/j.jtcvs.2026.07.002 | () | ✅ タイトル一致 |
| 74 | JTCVS OF | Twenty-Five Year Outcomes of Patients Undergoing Valve Surgery f | 10.1016/j.jtcvs.2026.06.025 | () | ✅ タイトル一致 |
| 75 | JTCVS OF | Beyond Dogma and Data: What I Learned after 50 Years of Cardiac  | 10.1016/j.jtcvs.2026.06.024 | () | ✅ タイトル一致 |
| 76 | JTCVS OF | Factors associated with acute intestinal ischemia after cardiac  | 10.1016/j.jtcvs.2026.07.001 | () | ✅ タイトル一致 |
| 77 | JTCVS OF | Commentary: Why do we still not know what causes vasoplegia?: On | 10.1016/j.jtcvs.2026.07.003 | () | ✅ タイトル一致（副題表記差のみ） |
| 78 | JTCVS OF | Association or confounding? Reassessing pulmonary outcomes after | 10.1016/j.jtcvs.2026.06.010 | () | ✅ タイトル一致 |
| 79 | JTCVS OF | Resection Outcomes According to Pathologic Risk in ≤2 cm Invasiv | 10.1016/j.jtcvs.2026.06.023 | () | ✅ タイトル一致 |
| 80 | JTCVS OF | Oncological Outcomes of Left Upper Tri-segmentectomy vs. Lobecto | 10.1016/j.jtcvs.2026.06.015 | () | ✅ タイトル一致 |
| 81 | JTCVS OF | Pushing the Age Limit: Mitral Valve Surgery Is Safe and Effectiv | 10.1016/j.jtcvs.2026.06.020 | () | ✅ タイトル一致 |
| 82 | JTCVS OF | Bridging Pediatric and Young Adult Cancer Survivorship: Defining | 10.1016/j.jtcvs.2026.06.021 | () | ✅ タイトル一致 |
| 83 | JTCVS OF | Beyond compensatory expansion: Extending 3-dimensional computed  | 10.1016/j.jtcvs.2026.06.004 | () | ✅ タイトル一致 |
| 84 | JTCVS OF | A CALL FOR STANDARDIZATION OF HYBRID ARCH FROZEN ELEPHANT TRUNK  | 10.1016/j.jtcvs.2026.06.014 | () | ✅ タイトル一致 |
| 85 | JTCVS OF | Pediatric Mitral Valve Surgery: Current Practice from the Europe | 10.1016/j.jtcvs.2026.06.013 | () | ✅ タイトル一致 |
| 86 | JTCVS OF | Rethinking Failure to Rescue in Cardiac Surgery. | 10.1016/j.jtcvs.2026.06.016 | () | ✅ タイトル一致 |
| 87 | JTCVS OF | Undersized Fontan conduits are not without risk. | 10.1016/j.jtcvs.2026.05.021 | () | ✅ タイトル一致 |
| 88 | JHLT 45(7) | Unexpected lesions in lung transplantation beyond radiological s | 10.1016/j.healun.2026.03.001 | 45(7) 1178-1179 | ✅ タイトル一致 |
| 89 | JHLT 45(7) | From association to stratification? Caution in sex-specific card | 10.1016/j.healun.2026.03.012 | 45(7) 1168-1169 | ✅ タイトル一致 |
| 90 | JHLT 45(7) | A Perspective Summary of the ISHLT Consensus Statement on Acute  | 10.1016/j.healun.2026.02.1676 | 45(7) 1019-1021 | ✅ タイトル一致 |
| 91 | JHLT 45(7) | ISHLT Consensus Statement on Acute Lung Allograft Dysfunction (A | 10.1016/j.healun.2026.02.1677 | 45(7) e173-e195 | ✅ タイトル一致 |
| 92 | JHLT 45(7) | Early United States experience with donation after circulatory d | 10.1016/j.healun.2026.02.1673 | 45(7) 1035-1043 | ✅ タイトル一致 |
| 93 | JHLT 45(7) | Heart transplantation in the GLP-1 Era: Time to catch up? Invite | 10.1016/j.healun.2026.04.017 | 45(7) 1033-1034 | ✅ タイトル一致 |
| 94 | JHLT 45(7) | Methamphetamine-associated PAH in the United States: A signal we | 10.1016/j.healun.2026.03.033 | 45(7) 1133-1134 | ✅ タイトル一致 |
| 95 | JHLT 45(7) | Improving access without compromise: Policy reform and outcomes  | 10.1016/j.healun.2026.03.031 | 45(7) 1121-1122 | ✅ タイトル一致 |
| 96 | JHLT 45(7) | Corrigendum to "Combined heart-lung organ allocation: A glitch i | 10.1016/j.healun.2026.03.022 | 45(7) 1180 | ✅ タイトル一致 |
| 97 | JHLT 45(7) | When rejection leaves a molecular scar: Histologic resolution is | 10.1016/j.healun.2026.03.027 | 45(7) 1162-1164 | ✅ タイトル一致 |
| 98 | JHLT 45(7) | Finding the limits of hypothermic oxygenated perfusion. | 10.1016/j.healun.2026.03.028 | 45(7) 1147-1148 | ✅ タイトル一致 |
| 99 | JHLT 45(7) | Response to "From association to stratification? Caution in sex- | 10.1016/j.healun.2026.03.029 | 45(7) 1170-1171 | ✅ タイトル一致 |
| 100 | JHLT 45(7) | Early right ventricular failure following HeartMate 3 left ventr | 10.1016/j.healun.2026.03.025 | 45(7) 1081-1090 | ✅ タイトル一致 |
| 101 | JHLT 45(7) | When coverage is not access: A heart transplant recipient's pers | 10.1016/j.healun.2026.03.024 | 45(7) 1022-1023 | ✅ タイトル一致 |
| 102 | JHLT 45(7) | Reply to "Donor-derived cell-free DNA associated with increased  | 10.1016/j.healun.2026.03.023 | 45(7) 1175-1177 | ✅ タイトル一致 |
| 103 | JHLT 45(7) | Twenty-four-hour hypothermic oxygenated perfusion preserves graf | 10.1016/j.healun.2026.03.021 | 45(7) 1135-1146 | ✅ タイトル一致 |
| 104 | JHLT 45(7) | Initial pediatric experience of preserving cardiac allografts in | 10.1016/j.healun.2026.03.019 | 45(7) 1108-1111 | ✅ タイトル一致 |
| 105 | JHLT 45(7) | When seronegativity does not mean silence: DSA-negative antibody | 10.1016/j.healun.2026.03.018 | 45(7) 1058-1059 | ✅ タイトル一致 |
| 106 | JHLT 45(7) | Donor-derived cell-free DNA associated with increased risk of ch | 10.1016/j.healun.2026.02.1662 | 45(7) 1172-1174 | ✅ タイトル一致 |
| 107 | JHLT 45(7) | Safety and immunogenicity of varicella-zoster vaccination in ped | 10.1016/j.healun.2026.03.010 | 45(7) 1095-1102 | ✅ タイトル一致 |
| 108 | JHLT 45(7) | Supporting the forgotten ventricle: Hybrid strategies for right  | 10.1016/j.healun.2026.03.015 | 45(7) 1078-1080 | ✅ タイトル一致 |
| 109 | JHLT 45(7) | The donation after circulatory death heart deserves a second cha | 10.1016/j.healun.2026.03.013 | 45(7) 1044-1045 | ✅ タイトル一致 |
| 110 | JHLT 45(7) | Advancing ABO-histocompatibility: Impact of multiplexed ABO anti | 10.1016/j.healun.2026.03.003 | 45(7) 1103-1107 | ✅ タイトル一致 |
| 111 | JHLT 45(7) | Influence of U.S. lung composite allocation score components on  | 10.1016/j.healun.2026.03.016 | 45(7) 1064-1067 | ✅ タイトル一致 |
| 112 | JHLT 45(7) | Multi-center open-label tacrolimus inhalation powder trial evalu | 10.1016/j.healun.2026.03.007 | 45(7) 1060-1063 | ✅ タイトル一致 |
| 113 | JHLT 45(7) | Pediatric lung transplantation in Japan across legislative and a | 10.1016/j.healun.2026.03.009 | 45(7) 1112-1120 | ✅ タイトル一致 |
| 114 | JHLT 45(7) | Comparing DSA-negative and DSA-positive antibody-mediated reject | 10.1016/j.healun.2026.03.004 | 45(7) 1046-1057 | ✅ タイトル一致 |
| 115 | JHLT 45(7) | Respond to "Comments and opinions regarding: High antiphospholip | 10.1016/j.healun.2026.03.005 | 45(7) 1167 | ✅ タイトル一致 |
| 116 | JHLT 45(7) | Comments and opinions regarding "High antiphospholipid antibody  | 10.1016/j.healun.2026.02.1669 | 45(7) 1165-1166 | ✅ タイトル一致 |
| 117 | JHLT 45(7) | Hidden danger of microaxial flow pumps: Five cases of aortic and | 10.1016/j.healun.2026.02.1679 | 45(7) 1091-1094 | ✅ タイトル一致 |
| 118 | JHLT 45(7) | Methamphetamine-associated PAH on the rise in the US: geographic | 10.1016/j.healun.2026.02.1678 | 45(7) 1123-1132 | ✅ タイトル一致 |
| 119 | JHLT 45(7) | Hybrid durable biventricular assist device implantation with Ber | 10.1016/j.healun.2026.02.1674 | 45(7) 1068-1077 | ✅ タイトル一致 |
| 120 | JHLT 45(7) | Human lung allografts experience persistent fibrogenic shift fol | 10.1016/j.healun.2026.02.1666 | 45(7) 1149-1161 | ✅ タイトル一致 |
| 121 | JHLT 45(7) | The association between glucagon-like peptide 1 receptor agonist | 10.1016/j.healun.2026.01.003 | 45(7) 1024-1032 | ✅ タイトル一致 |
| 122 | JHLT OF | Donor Disposition and Lung Utilization Following 'Not Expected t | 10.1016/j.healun.2026.07.018 | () | ✅ タイトル一致 |
| 123 | JHLT OF | Misdiagnosed as Idiopathic PAH: Methylmalonic Acidemia as a Reve | 10.1016/j.healun.2026.07.021 | () | ✅ タイトル一致 |
| 124 | JHLT OF | When "Not A Candidate" Becomes a Verdict: Reframing Intensive Ca | 10.1016/j.healun.2026.07.023 | () | ⚠️ CrossRef未登録（新着）→ PubMedで確認 |
| 125 | JHLT OF | Toward Integrated Molecular Monitoring of the Lung Allograft: Fr | 10.1016/j.healun.2026.07.020 | () | ✅ タイトル一致 |
| 126 | JHLT OF | Pulmonary-Abdominal Normothermic Regional Perfusion Enables In S | 10.1016/j.healun.2026.07.011 | () | ✅ タイトル一致 |
| 127 | JHLT OF | Out-of-Sequence Lung Allocation and Outcomes for Bypassed Candid | 10.1016/j.healun.2026.07.016 | () | ✅ タイトル一致 |
| 128 | JHLT OF | Molecular Insights into Allograft Rejection and the ISHLT Pulmon | 10.1016/j.healun.2026.07.017 | () | ✅ タイトル一致 |
| 129 | JHLT OF | Do we need consensus on Consensus? | 10.1016/j.healun.2026.07.015 | () | ✅ タイトル一致 |
| 130 | JHLT OF | Persistent Primary Graft Dysfunction Stratifies Risk After Heart | 10.1016/j.healun.2026.07.007 | () | ✅ タイトル一致 |
| 131 | JHLT OF | The International Thoracic Organ Transplant Registry of the Inte | 10.1016/j.healun.2026.07.006 | () | ✅ タイトル一致 |
| 132 | JHLT OF | Elevated Donor-Derived Cell-Free DNA Correlates with Donor-Speci | 10.1016/j.healun.2026.07.010 | () | ✅ タイトル一致 |
| 133 | JHLT OF | Understanding the Impact of Heart Allocation on Durable LVAD Use | 10.1016/j.healun.2026.07.003 | () | ✅ タイトル一致 |
| 134 | JHLT OF | Pediatric VADs in the ACTION Era: From Survival to Strategy. | 10.1016/j.healun.2026.07.005 | () | ✅ タイトル一致 |
| 135 | JHLT OF | Short term heart transplant outcomes with heart organ procuremen | 10.1016/j.healun.2026.07.004 | () | ✅ タイトル一致 |
| 136 | JHLT OF | Could transbronchial biopsies tell us more? Searching for deeper | 10.1016/j.healun.2026.06.020 | () | ✅ タイトル一致 |
| 137 | JHLT OF | Can We Turn a Trifecta into a Superfecta? | 10.1016/j.healun.2026.06.019 | () | ✅ タイトル一致 |
| 138 | JHLT OF | Compassionate Use of Hypothermic Oxygenated Perfusion for Donor  | 10.1016/j.healun.2026.06.015 | () | ✅ タイトル一致 |
| 139 | JHLT OF | Safety and Immunogenicity of Live-Attenuated Measles-Mumps-Rubel | 10.1016/j.healun.2026.07.013 | () | ✅ タイトル一致 |
| 140 | JHLT OF | Time, Tissue, and Team: Reframing Transbronchial Biopsy in Lung  | 10.1016/j.healun.2026.07.012 | () | ✅ タイトル一致 |
| 141 | JHLT OF | Dynamic contrast-enhanced MRI quantifies microvascular changes i | 10.1016/j.healun.2026.07.001 | () | ✅ タイトル一致 |
| 142 | JHLT OF | Navigating the New Lung CAS Framework: A Critical Look at Geogra | 10.1016/j.healun.2026.07.014 | () | ✅ タイトル一致 |
| 143 | JHLT OF | MAPPING THE MTOR PATHWAY IN LUNG TRANSPLANTATION: IS IT TIME FOR | 10.1016/j.healun.2026.07.009 | () | ✅ タイトル一致 |
| 144 | JHLT OF | Primary graft dysfunction after lung transplant in mechanically  | 10.1016/j.healun.2026.07.002 | () | ✅ タイトル一致 |
| 145 | JHLT OF | On the differential hemodynamic effects of prostacyclins and sot | 10.1016/j.healun.2026.06.006 | () | ✅ タイトル一致 |
| 146 | JHLT OF | Alveolar macrophage activation and polarization signatures in st | 10.1016/j.healun.2026.06.016 | () | ✅ タイトル一致 |
| 147 | JHLT OF | Distinct metabolomic and lipidomic profiles across donation afte | 10.1016/j.healun.2026.06.017 | () | ✅ タイトル一致 |
| 148 | JHLT OF | Antibody-mediated rejection after heart transplantation: Diagnos | 10.1016/j.healun.2026.06.018 | () | ✅ タイトル一致 |
---

## 収集条件（再現用）

```
# 号TOC（PubMed E-utilities）
esearch: "J Thorac Cardiovasc Surg"[jour] AND 172[volume] AND 1[issue]     -> 37件
esearch: "J Heart Lung Transplant"[jour] AND 45[volume] AND 7[issue]       -> 34件
esearch: "Eur J Cardiothorac Surg"[jour] AND 68[volume] AND 6[issue]       -> 14件（6月号追補用）
esearch: "Eur J Cardiothorac Surg"[jour] AND 68[volume] AND 7[issue]       -> 10件
# Online-First（当月edat・巻未割当）
esearch: "<jour>"[jour] AND 2026/07/01:2026/07/31[edat] NOT <vol>[volume]  -> JTCVS 24 / JHLT 27 / EJCTS 2
# DOI照合
GET https://api.crossref.org/works/{DOI}  （title / volume / issue / page / license を突合）
```

> **注意（次回への申し送り）**: CrossRefの `filter=from-index-date` は再索引された旧論文（1990年代の論文まで）を
> 大量に拾い、1000件上限に達しても当該号を網羅できない。**号のTOCはPubMed esearch（volume/issue指定）が確実**。
> また PubMed XML を自作パースする場合、`.//ArticleIdList/ArticleId` は **ReferenceList内のIDも拾ってしまう**ため、
> PMIDは `MedlineCitation/PMID`、DOIは `PubmedData/ArticleIdList` から明示的に取得すること（本セッションで実害を確認）。
