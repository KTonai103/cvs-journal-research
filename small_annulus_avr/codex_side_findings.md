---
title: "Phase 2 文献収集 — Codex (GPT-5) 側 + Claude 独立 PubMed 検証結果"
date: 2026-05-13
tags: [phase-2, codex-side, pubmed-verified, raw-findings]
status: 統合済み、cross_check.md 参照
---

# Phase 2 文献収集 — Codex 側 + Claude 独立 PubMed 検証

> [!important] 概要
> Claude 側 4 Agent の生報告（`claude_side_findings.md`）に対し、**Codex (GPT-5)** で独立検証＋発見を行った。Codex は curl が DNS resolution failure（サンドボックス制約）だったため、内部知識ベース + publisher/repository metadata 照合で検証。Cat A+B は Codex が 22 分 stuck したため、Claude メインスレッドが直接 PubMed E-utilities curl で実検証した。
>
> **結論**: Claude 側 4 Agent の PMID/DOI は **多数が hallucination**。Codex 側の検証は致命的な誤りを多数発見。

---

## 0. 実検証の制約まとめ

| 側 | ツール | 結果 |
|---|---|---|
| Claude 4 Agent (Explore) | 内部知識ベース | **多数の PMID/DOI/著者が hallucination** |
| Codex 4 task (GPT-5) | 内部知識 + publisher pages（curl は DNS で blocked） | Claude side の誤りを多数発見、修正版を提示 |
| **Claude メインスレッド** | **PubMed E-utilities curl 直接実行** | **Cat A+B を実 API で検証完了** |

---

## 1. Cat A+B — Y-incision / 古典 AAE（Claude メインスレッド PubMed 実検証）

### 1-1. Yang group の **本物の** Y-incision 論文（全 PMID PubMed 実検証）

| # | PMID | 著者 | 年 | 雑誌 | タイトル | DOI |
|---|---|---|---|---|---|---|
| A1 | **36031424** | Yang B | 2024 Apr | **J Thorac Cardiovasc Surg** | Early outcomes of the Y-incision technique to enlarge the aortic annulus 3 to 4 valve sizes | 10.1016/j.jtcvs.2022.07.006 |
| A2 | **38841090** | Yang B | 2024 May | Ann Cardiothorac Surg | Updates on Y-incision aortic annular enlargement | (検索 needed) |
| A3 | **38841092** | Yang B | 2024 May | Ann Cardiothorac Surg | Aortic annular enlargement with Y-incision/rectangular patch | (検索 needed) |
| A4 | **40098828** | Yang B | 2025 Mar | Ann Thorac Surg Short Rep | "Arc" Modification of the Patch for Y-Incision AAE | (検索 needed) |
| A5 | **41619928** | Yang B | 2026 Jan | Ann Thorac Surg | The 5 Misconceptions of Y-Incision Aortic Annular Enlargement | (検索 needed) |
| A6 | **38841083** | Makkinejad A (Yang group) | 2024 May | Ann Cardiothorac Surg | Comparison of short-term outcomes between Y-incision AAE and traditional AAE | (検索 needed) |
| A7 | **38841089** | Truesdell W (Yang group) | 2024 May | Ann Cardiothorac Surg | Changes in aortic root dimensions post AAE with Y-incision and modified aortotomy | (検索 needed) |
| A8 | **40403905** | Makkinejad A | 2025 Oct | Ann Thorac Surg | Nicks, Manouguian, and Y-incision AAE: Do All Roads Lead to Rome? | (検索 needed) |
| A9 | **41473041** | Makkinejad A | 2025 Dec | JTCVS Open | Effect of surgeon experience on Y-incision AAE short-term outcomes | (検索 needed) |
| A10 | **39892843** | Chen SA | 2025 Jun | Ann Thorac Surg | AAE: Y-Incision Rationale, Technique, and Outcomes | (検索 needed) |
| A11 | **40500547** | Bonini M | 2025 Aug | J Cardiovasc Transl Res | Modeling Hemodynamic Impact of Y-incision AAE on AVR and ViV | (検索 needed) |
| A12 | **40641760** | Wang GX | 2025 Jun | JTCVS Tech | Y-incision with a new roof technique to enlarge the aortic root | (検索 needed) |
| A13 | **41856503** | Fikani A | 2026 Mar | Thorac Cardiovasc Surg | Technical Modifications to the Y-Incision AAE Technique | (検索 needed) |
| A14 | **41781359** | Do-Nguyen CC | 2026 Mar | Asian Cardiovasc Thorac Ann | Y-incision aortic root enlargement — Common mistakes and update of early outcomes | (検索 needed) |
| A15 | **41658927** | Cangut B | 2026 Feb | JTCVS Tech | Mitral valve surgery with concomitant Y-incision AAE | 10.1016/j.xjtc.2025.10.003 |
| A16 | **41100181** | Yin K | 2025 Nov | Eur J Cardiothorac Surg | Y-Incision AAE in Patients With Anomalous Left Circumflex Artery | (検索 needed) |
| A17 | **40270847** | Yin K | 2025 Mar | Ann Cardiothorac Surg | Y-incision AAE after surgical explantation of TAVI bioprosthesis | (検索 needed) |
| A18 | **41843014** | Masaki N | 2026 Mar | Pediatr Cardiol | Modification of Nicks Technique for AAE in Children | (検索 needed) |
| A19 | **41621561** | Gan LX | 2026 Jan | Ann Thorac Surg | Y-Incision AAE + Chimney MVR for Double Small Annuli: Alternative to Commando? | (検索 needed) |
| A20 | **41425437** | Kitamura T | 2025 Dec | Ann Thorac Surg Short Rep | Y Incision + Anterior Extended Aortoplasty: The "Y and I" Incision | (検索 needed) |
| A21 | **42083003** | Özçelik S | 2026 May | J Cardiothorac Surg | Severe MR after AAE with Y-incision: case report | (検索 needed) |

### 1-2. 古典 AAE 原著・長期成績（PubMed 実検証）

| # | PMID | 著者 | 年 | 雑誌 | タイトル |
|---|---|---|---|---|---|
| B1 | **470420** | **Manouguian S** | 1979 Sep | **J Thorac Cardiovasc Surg** | Patch enlargement of the aortic valve ring by extending into anterior mitral leaflet (**seminal**) |
| B2 | **470419** | Manouguian S | 1979 Sep | J Thorac Cardiovasc Surg | Patch enlargement of aortic and mitral valve rings (experimental study, companion paper) |
| B3 | **5452289** | **Nicks R** | 1970 May | **Thorax** | Hypoplasia of the aortic root. The problem of aortic valve replacement (**seminal**) |
| B4 | **127094** | **Konno S** | 1975 Nov | **J Thorac Cardiovasc Surg** | A new method for prosthetic valve replacement in congenital aortic stenosis (**seminal**) |
| B5 | **38841083** | Makkinejad A (Yang group) | 2024 May | Ann Cardiothorac Surg | Y-incision vs traditional AAE short-term comparison |
| B6 | **38522868** | Hassler KR | 2024 | Semin Thorac Cardiovasc Surg Pediatr Card Surg Annu | How-I-Do-It: AAE — Are Nicks and Manouguian Obsolete? |
| B7 | **34970789** | Malfitano MJ | 2022 Mar | J Card Surg | Modified Manouguian technique for aortic root enlargement: case series |
| B8 | **1434702** | **Kawachi Y** | 1992 Nov | **J Thorac Cardiovasc Surg** | **Eleven-year follow-up of aortic/aortic-mitral annulus-enlarging by Manouguian's technique (Japanese)** ★ |
| B9 | **8953456** | **Kitamura M** | 1996 Nov | **J Heart Valve Dis** | **Aortic valve replacement in small aortic annulus with or without annular enlargement (Japanese)** ★ |
| B10 | **12296921** | **Maekawa A** | 2002 Oct | **Artif Organs** | **Optimal size of prostheses in AVR + MVR with Manouguian (Japanese)** ★ |

★ = **日本人著者の Manouguian 系列**（本研究 RQ への直接寄与）

### 1-3. Claude 側 Cat A+B PMID の検証結果

**全 9 件の Claude 側 PMID が PubMed で検証された結果、全て無関係な論文と判明**:

| Claude 提示 PMID | 実際の論文 (PubMed) | 判定 |
|---|---|---|
| 37050629 (Yang B JTCVS 2023) | Sensors 2023 「射出成形モニタリング」 | ❌ **HALLUCINATION** |
| 35181639 (Yang B Ann Thorac Surg 2021) | J Immunol 2022 「魚類ウイルス免疫」 | ❌ **HALLUCINATION** |
| 37614789 (Yang B JTCVS 2024 5-yr) | RSC Adv 2023 「撥水繊維」 | ❌ **HALLUCINATION** |
| 36891204 (Ohira S 2023) | Front Psychol 2023 「Latinx COVID 心理」 | ❌ **HALLUCINATION** |
| 37892156 (Kaneko T 2024) | Biomolecules 2023 「ナツメヤシ生化学」 | ❌ **HALLUCINATION** |
| 36234567 (Masuda M 2023) | Nanomaterials 2022 「廃水処理」 | ❌ **HALLUCINATION** |
| 31234567 (Totaro P 2019) | Sensors 2019 「電気インピーダンス」 | ❌ **HALLUCINATION** |
| 32456789 (Zoghbi WA 2020) | Can J Ophthalmol 2020 「結膜炎」 | ❌ **HALLUCINATION** |
| 29357689 (Coutinho 2018) | Clin Child Psychol 2018 「養子縁組心理」 | ❌ **HALLUCINATION** |

**Yang B 2023 JTCVS の真の PMID**: 36031424（実際は 2024 Apr 発行、Claude は 2023 と誤記、DOI は偶然正しい）

---

## 2. Cat C+I — Codex 側（独立検証＋発見）

Codex 報告原文: `/tmp/codex_small_annulus/result_c_i.txt`

### 2-1. アジア人・日本人コホート（Codex が発見した実 PMID 群）

| # | PMID | DOI | 著者 | 国 | タイトル | 雑誌 | 年 | n | Key data |
|---|---|---|---|---|---|---|---|---|---|
| C1 | **28606674** | 10.1016/j.ijcard.2017.01.076 | Yashima / Yamamoto / Watanabe / Hayashida | JPN | TAVI in patients with extremely small native aortic annulus: OCEAN-TAVI | Int J Cardiol | 2017 | 20mm SXT 19; 23mm SXT 492; matched 18+18 | annulus area `<314mm²`; moderate PPM higher with 20mm SXT, severe PPM rare |
| C2 | **32926552** | 10.1002/ccd.29259 | Hase / Watanabe / Yamamoto / Hayashida | JPN | Evolut R vs SAPIEN 3 in Japanese small annulus: OCEAN-TAVI | Catheter Cardiovasc Interv | 2021 | 576 | Evolut R lower 1y mPG, higher iEOA; mortality similar |
| C3 | **39967214** | 10.1016/j.jacasi.2024.09.005 | Okuno / Watanabe / Yamamoto / Hayashida | JPN | Extremely small 20mm vs standard balloon-expandable THV: OCEAN-TAVI | JACC Asia | 2025 | 5086 eligible; 284 received 20mm; matched 276 vs 828 | PPM higher with 20mm THV |
| C4 | **41243775** | 10.4244/EIJ-D-25-00682 | Yamamoto | JPN | Long-term outcomes/durability of balloon-expandable TAVI in small and large annuli | EuroIntervention | 2025 | 2,699 | SAA `≤430mm²`; sex/PPM/mPG subanalyses |
| C5 | **33642425** | 10.1253/circj.CJ-20-1084 | Meguro | JPN | TAVR in small annulus: J-TVT Japanese nationwide registry | Circ J | 2021 | 5,870; SAA 647 | SAA `≤314mm²`; SAA 93.2% female; moderate PPM 15.6%, severe 2.6% |
| C6 | **33907051** | 10.1253/circj.CJ-20-1095 | Shishido / Hayashida | JPN | Effect of sex on mortality and LV remodeling after TAVI | Circ J | 2021 | 2,588; female 1,793 | Female survival advantage after TAVI |
| C7 | **23228405** | 10.1016/j.jtcvs.2012.11.020 | Tabata | JPN | Simple interrupted suturing increases valve performance after AVR with small supra-annular bioprosthesis | J Thorac Cardiovasc Surg | 2014 | 152 | **19/21mm Magna; PPM 29% vs 56% by suture technique** |
| C8 | **30464118** | 10.1536/ihj.17-656 | Kamioka | JPN | Valve hemodynamics and clinical outcomes after TAVR for small aortic annulus | Int Heart J | 2019 | 94; TAVR 35, SAVR 59 | **Japanese SAA `≤20mm`; severe PPM 2.9% TAVR vs 22.0% SAVR** |
| C9 | **22130314** | 10.1253/circj.CJ-11-0733 | Okamura | JPN | Mid-term outcomes after AVR with 17mm St. Jude Regent valve | Circ J | 2012 | 78 | PPM at discharge did not influence survival/LV mass regression |
| C10 | **19101276** | 10.1016/j.athoracsur.2008.09.051 | Okamura | JPN | 17mm St. Jude Regent valve is valid for small annulus | Ann Thorac Surg | 2009 | 23 | Small BSA cohort |
| C11 | **33806531** | 10.3390/jcm10051063 | Kim DJ / Lee S | KOR | Two differently designed aortic bioprostheses for small aortic annuli | J Clin Med | 2021 | n/a | Korean SAVR small-annulus bioprosthesis comparison |
| C12 | (Not in PubMed) | 10.54912/jci.2023.0001 | Moon / Kang | KOR | Features and outcomes of small annulus TAVR: Korean TAVR Registry | J Cardiovasc Interv | 2023 | 660; SAA 70 | Korean cohort SAA `<20mm`; SAA 80% female; 1y comparable |
| C13 | (Not in PubMed) | 10.4070/kcj.2020.0409 | Yong-Joon Lee | KOR | Self-expanding vs balloon-expandable TAVR in small annulus | Korean Circ J | 2021 | n/a | Korean SAA TAVR device comparison |
| C14 | **23745280** | (no DOI) | Liu / Zhang | CHN | Mid-long-term AVR with 17mm St. Jude Regent | Sichuan Univ Med Sci | 2013 | 44 | **PPM 82.1%, severe 30.8% (Chinese)** |
| C15 | (Not indexed) | 10.1186/1749-8090-9-17 | Hu / Qian / Zhang | CHN | 17mm Regent in small annulus: does moderate PPM matter? | J Cardiothorac Surg | 2014 | 114 | West China; moderate PPM 43.4% |
| C16 | (Not indexed) | 10.1186/1749-8090-7-88 | Zhao / Wang / Guo | CHN | Regent mechanical valve in small annulus 3y follow-up | J Cardiothorac Surg | 2012 | 40 | Chinese SAA `≤19mm`; 17/19mm mech |
| C17 | **41491442** | 10.1007/s12928-025-01215-5 | Mao / Zhang / Pan / Wu / Yang | CHN (incl Fuwai) | ML algorithm predicting PPM during TAVR in small annuli | Cardiovasc Interv Ther | 2026 | 273 + 118 validation | Chinese multicenter incl Fuwai investigators |

### 2-2. Cat I 訂正

| Claude 提示 | 訂正後（Codex） |
|---|---|
| Goldstone AB NEJM 2017, PMID 28296591 | ✅ DOI 10.1056/NEJMoa1613792 正、**PMID 正は 29117490** |

### 2-3. Cat C+I Critical Gaps（Codex 認定）

1. **日本人 Y-incision のアウトカム cohort**: **存在せず** — 本研究の知的価値の核心ギャップ
2. **アジア人 19mm SAVR 後の ViV feasibility**: **未報告**
3. **アジア人小弁輪 mechanical vs biologic RCT**: 不在（Goldstone は西洋データのみ）
4. **PPM definition heterogeneity**: ≤314mm² / ≤20mm / ≤430mm² / <72mm 周囲 — pool 化困難
5. **Sex/BSA × annulus × long-term outcomes** を 1 cohort で扱った Asian study が稀少
6. **Asan Med Center (Lee SA / Kim DH)** には小弁輪 AVR cohort 確認できず（severe AS timing 系の Lee/Kim 論文は存在）

---

## 3. Cat D+F — Codex 側（PPM / ViV-TAVR）

Codex 報告原文: `/tmp/codex_small_annulus/result_d_f.txt`

### 3-1. Cat D 検証結果

| Claude 提示 | Codex 検証 |
|---|---|
| Pibarot P JACC 2000, PMID 11028462 | ✅ DOI 10.1016/S0735-1097(00)00859-7 (大文字 S 注意) |
| Pibarot P Heart 2006, PMID 16251232 | ✅ verified |
| Pibarot P JACC 2012, PMID 22995023 | ⚠️ DOI plausible, review type |
| **Head SJ EHJ 2012, PMID 22408037** | ✅ **抽出 HR**: severe PPM HR 1.84, moderate HR 1.19, overall 1.34 |
| Mohty D JACC 2009, PMID 19118723 | ⚠️ plausible, HR 未抽出 |
| Mohty D Circulation 2006, PMID 16415379 | ❌ PMID 不充分検証 |
| Pibarot P JASE 2014, PMID 24863015 | ⚠️ plausible, editorial/review |
| Mohty D Circulation 2014, PMID 25200051 | ⚠️ title/DOI 正、PMID 別 record の可能性 |

### 3-2. Cat F 検証結果（**重要訂正**）

| Claude 提示 | Codex 訂正 |
|---|---|
| **Bleiziffer S EHJ 2018, PMID 29020413, DOI 10.1093/eurheartj/ehy079** | ⚠️ **first author は Ribeiro, DOI は ehx455**（Claude DOI 誤り） |
| **Bleiziffer S Circ Cardiovasc Interv 2016, PMID 27301396** | ⚠️ **first author は Simonato**, DOI 10.1161/CIRCINTERVENTIONS.115.003651 |
| Alperi (Bleiziffer group) JACC 2021, PMID 33958122 | ✅ **PPI 6.4%; 30d mortality 4.7% w/PPI vs 2.7%** |
| **D'Onofrio (not Tarantini) Ann Thorac Surg 2016, PMID 27496631** | ✅ valve ID groups: `<20`, 21-23, `>23mm`; 30d mortality 6% overall, 4.5% aortic ViV |
| **Tarantini BVF 2025 PMID 40537943** | ⚠️ **first author は Ruge**, REDUCE registry, 240 pts, 60% true ID ≤21mm, 30d survival 93.3% |
| **Bapat REVALVE 2025 PMID 40393632** | ⚠️ **first author は Blackman**, **design paper only, no outcomes yet** |
| Khan JM BASILICA series | ✅ all PMIDs verified, detailed outcomes extracted |

### 3-3. Cat F 新規発見（Codex）

🆕 **Dvir D JAMA 2014 VIVID original** — **PMID 25005653**, DOI 10.1001/jama.2014.7246
- 459 patients, surgical valve labels: small ≤21mm, intermediate >21<25mm, large ≥25mm
- 30d mortality 7.6-8%, 1y survival 83.2%, **worse with small valves and stenotic failure**

🆕 **EXPLANT-TAVR series**:
- PMID 38224255 — EXPLANT-TAVR valve-type analysis
- PMID 38677492 — TAVR-explant operative consensus
- PMID 38440208 — TAV-in-TAV review
- PMID 38761972 — TAV-in-TAV embolization outcomes
- PMID 41136054 — TAV-in-TAV rescue case

---

## 4. Cat E+G+H — Codex 側（TAVI / Sutureless / Guidelines）

Codex 報告原文: `/tmp/codex_small_annulus/result_e_g_h.txt`

### 4-1. Cat E 検証結果（**重要訂正**）

| Claude 提示 | Codex 訂正 |
|---|---|
| **Herrmann HC NEJM 2024 SMART, PMID 38701631** | ⚠️ **正 PMID は 38587261**, DOI 10.1056/NEJMoa2312573 正、NEJM 2024;390:1959-1971 |
| Herrmann HC Am Heart J 2022 PMID 34587510 | ✅ verified |
| **Abdelfattah Int J Cardiol 2024 PMID 38851542** | ⚠️ PMID verified、**DOI は 10.1016/j.ijcard.2024.132243**（Claude の 132136 誤り）、**著者 Abdelfattah 未確認** |
| **VIVA Trial Circulation 2023 PMID 37883682** | ⚠️ **first author は Rodés-Cabau**（Abdelfattah/Babaliaros でない）、Circulation 2024;149:644-655 (epub Oct 26, 2023) |
| **TAVI-SMALL 2 registry EuroIntervention 2024** | ✅ 実は **2023, PMID 36950893, DOI 10.4244/EIJ-D-22-00843** |
| **OCEAN-TAVI 20mm 2024-2025** | ✅ Okuno JACC Asia 2025, PMID 39967214（Cat C と重複） |

### 4-2. SMART Trial 関連最新

🆕 **PMID 40452601** — "Evaluation of Bioprosthetic Valve Dysfunction in SMART Randomized Clinical Trial" (2025 secondary analysis)
❌ **SMART 2-year follow-up peer-reviewed paper 存在せず**（manufacturer page のみ）

### 4-3. Cat G 検証結果（**全件大きな訂正**）

| Claude 提示 | Codex 訂正 |
|---|---|
| **Di Eusanio SURD-IR EJCTS 2019 PMID 30689828** | ⚠️ **first author は Santarpino**, EJCTS 2019;56:38-43, DOI ezy477 |
| **Berretta P JTCVS 2021 bicuspid PMID 32832411** | ❌ **正は Annals of Cardiothoracic Surgery 2020;9:298-304**, DOI 10.21037/acs-2020-surd-33 |
| **Lorusso R JTCVS 2021 sutureless vs rapid PMID 34563505** | ❌ **正は Berretta**, Ann Thorac Surg 2022;114:758-765, DOI ezy039 |
| **Sénage T JTCVS 2015 Intuity PMID 24413009** | ❌ **正は Borger**, MMCTS 2013, DOI 10.1093/mmcts/mmt011 |
| **Folliguet T ICVTS 2016 PMID 26920726** | ❌ **正は Beckmann**, ICVTS 2016;22:744-749, DOI 10.1093/icvts/ivw041 |

### 4-4. Cat H ガイドライン検証（**最重要訂正**）

| ガイドライン | Codex 検証 |
|---|---|
| **ACC/AHA 2020 VHD** | ⚠️ Claude PMID 33332149 は **executive summary**（DOI 10.1161/CIR.0000000000000932）、**full guideline は PMID 33332150** (DOI 10.1161/CIR.0000000000000923) |
| **ESC/EACTS 2021 VHD** | ❌ Claude PMID 35636831 は **Rev Esp Cardiol reprint**、**EHJ guideline 正 PMID は 34453165** |
| **JCS 2020 弁膜症** | ✅ 「JCS/JSCS/JATS/JSVS 2020 Guidelines on Management of VHD」 Circ J 2020;84:2037-2119, DOI 10.1253/circj.CJ-20-0135 — J-STAGE で公開 |
| **STS expert consensus on AAE 2024-2025** | ❌ **formal peer-reviewed consensus document は存在しない** — STS Learning Center hands-on course のみ（教育コンテンツ） |

### 4-5. ガイドライン推奨マトリクス（Codex 抽出）

| 推奨項目 | ACC/AHA 2020 | ESC/EACTS 2021 | JCS 2020 | STS |
|---|---|---|---|---|
| AAE / root enlargement | **specific Class/LOE 無し**。PPM/ViV feasibility は議論 | **formal Class/LOE 無し**。root enlargement / stentless valve を mention | **Table 33**: small annulus + expected PPM が **TAVI を SAVR より favor** | **formal guideline 存在せず** |
| Sutureless / Rapid deployment | 推奨無し | 「invasiveness/CPB 時間短縮」言及、長期 RCT 不足 | Perceval/Intuity 新しい、長期不明 | guideline 無し |
| TAVR in small annulus | small annulus 特定推奨無し（一般的 SAVR vs TAVR 推奨適用） | small annulus は anatomic factor として登場、severe PPM (AVA<0.65 cm²/m²) が TAVI を favor | **Table 33**: small annulus + expected PPM → TAVI | none |
| PPM 回避 | 認識あり、standalone Class/LOE 無し | 「PPM 予防に重点を置くべき」明記、Class/LOE なし | severe PPM 閾値定義、prevention の Class/LOE 無し | none |
| **ViV 初回サイズ** | 「small aortic root が ViV を妨げる可能性」言及、Class/LOE 無し | ViV は確立、small aortic root では redo SAVR を考慮 | **明示的記載**: 初回 SAVR の弁 size/type が重要、small bioprosthesis での ViV は予後悪い、ViV を **Class IIa** とする | none |

---

## 5. 統合 Critical Gaps（Claude + Codex 合算）

1. ❌ **日本人 Y-incision のアウトカム cohort: 存在せず** → 本研究の最大の知的価値
2. ❌ **アジア人 19mm 弁植込み後の ViV feasibility: 未報告**
3. ❌ **STS formal AAE consensus document: 存在せず**（学習モジュールのみ）
4. ⚠️ **PPM definition 不統一**: pool 化困難
5. ⚠️ **Sex/BSA × annulus × long-term outcomes を 1 cohort で扱った Asian study が稀少**
6. ✅ **既存 Manouguian 系日本人論文**: Kawachi 1992 (PMID 1434702), Kitamura 1996 (8953456), Maekawa 2002 (12296921), Okamura 2009/2012 (19101276/22130314), Tabata 2014 (23228405) — これらが本研究の歴史的 baseline

---

## 6. Cat A+B Codex retry の結果

Codex Cat A+B task (task-mp3ca3ap-r3uep2) は **22 分間 stuck**（おそらく curl DNS retry loop）。手動 cancel し、代わりに **Claude メインスレッドが直接 PubMed E-utilities curl で検証**（上記 1 節）。

---

## 7. 重要な教訓

- Claude (Sonnet/Opus base) の **literature recall は信頼できない**（PMID/DOI/著者の hallucination 多発）
- Codex (GPT-5 base) は **知識が新しく正確**だが、サンドボックスで実 API curl 不可、知識ベース依存
- **唯一信頼できる検証は直接 API**（Claude メインスレッドからの PubMed E-utilities curl）
- **本研究で paper_list.md に載せる PMID/DOI は、Claude/Codex のどちらの knowledge にも依存せず、必ず PubMed 実検証を経たもののみとする**

---

*作成: 2026-05-13 | 関連: [[claude_side_findings]] | [[cross_check]] | [[paper_list]]*
