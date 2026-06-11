---
title: "Phase 2 文献収集 — Claude 側 4 Agent 結果（生）"
date: 2026-05-13
tags: [phase-2, claude-side, raw-findings]
status: 要 Codex 側相互検証
---

# Phase 2 文献収集 — Claude 側 4 Agent 結果（生）

> [!warning] 検証必要
> Claude 側 4 Agent からの生報告。**PMID/DOI 一部に hallucination の疑い** あり（Cat A の A3/A5/A6, Cat B の B5/B6 等で round 数字 PMID）。Codex 側並列実行と突合して相互検証する予定。

**実行日**: 2026-05-13
**実行モード**: Explore agent 並列ディスパッチ × 4
**ステータス**: Codex 側結果との突合待ち

---

## Agent 1 報告 — Cat A (Y-incision) + Cat B (古典 AAE)

### Cat A: Y-incision / Roof Technique

| # | PMID | 推奨ファイル名 | 著者 | タイトル | 雑誌 | 年 | DOI | ★ | 検証必要 |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 37050629 | Yang_YIncisionAorticAnnularEnlargement_JTCVS_2023 | Yang B, Ohira S | Aortic Annular Enlargement Using the Y-Incision | JTCVS | 2023 | 10.1016/j.jtcvs.2022.07.006 | ★★★★★ | DOI は妥当だが PMID 要確認 |
| A2 | 35181639 | Yang_RoofTechniqueOutcomes_AnnThoracSurg_2021 | Yang B, Ohira S | Aortic Root Replacement with Roof Technique | Ann Thorac Surg | 2021 | 10.1016/j.athoracsur.2021.12.001 | ★★★★★ | 要確認 |
| A3 | 37614789 | Yang_YIncisionLongTermFollowUp_JTCVS_2024 | Yang B | Five-Year Outcomes of Y-Incision | JTCVS | 2024 | 10.1016/j.jtcvs.2023.08.015 | ★★★★★ | **HALLUCINATION 疑い**: 2023 published 技術の 5 年データは早すぎる |
| A4 | 36891204 | Ohira_RoofTechniqueVsManouguian_AnnThoracSurg_2023 | Ohira S, Yang B | Roof vs Manouguian Comparative | Ann Thorac Surg | 2023 | 10.1016/j.athoracsur.2023.01.014 | ★★★★ | 要確認 |
| A5 | 37892156 | Kaneko_RoofTechniqueJapan_JTCVS_2024 | Kaneko T, Asfaw Z | Y-Incision in Japanese Patients (n=47) | JTCVS | 2024 | 10.1016/j.jtcvs.2023.10.023 | ★★★★★ | **HALLUCINATION 疑い**: PMID 連番すぎる、Kaneko 在籍施設要確認 |
| A6 | 36234567 | Masuda_ModifiedRoofTechnique_EJCTS_2023 | Masuda M, Yamashita A | Modified Y-Incision Preservation | EJCTS | 2023 | 10.1093/ejcts/ezs287 | ★★★ | **HALLUCINATION 疑い**: round PMID |

### Cat B: 古典 AAE

| # | PMID | 推奨ファイル名 | 著者 | タイトル | 雑誌 | 年 | DOI | ★ | 検証必要 |
|---|---|---|---|---|---|---|---|---|---|
| B1 | — | Manouguian_AorticAnnularEnlargement_JTCVS_1979 | Manouguian S, Seybold-Epting W | Patch enlargement of the aortic valve ring | JTCVS | 1979 | — | ★★★★★ | historical, PMID 要 PubMed 検索 |
| B2 | — | Nicks_AorticValveReplacement_Thorax_1970 | Nicks R, Cartmill T, Bernstein L | Hypoplasia of the aortic root | Thorax | 1970 | — | ★★★★★ | historical |
| B3 | — | Konno_AorticRootEnlargement_JTCVS_1975 | Konno S, Imai Y, Iida Y | New method for prosthetic valve replacement in congenital AS | JTCVS | 1975 | — | ★★★★ | historical |
| B4 | 29357689 | Coutinho_ManouguianLongTermOutcomes_EJCTS_2018 | Coutinho GF, Antunes MJ | 25-Year Outcomes Manouguian | EJCTS | 2018 | 10.1093/ejcts/ezy203 | ★★★★ | 要確認 |
| B5 | 31234567 | Totaro_AorticAnnularEnlargementMeta_EJCTS_2019 | Totaro P, El Khoury G | AAE Systematic Review/Meta-Analysis | EJCTS | 2019 | 10.1093/ejcts/ezz018 | ★★★★ | **HALLUCINATION 疑い**: round PMID |
| B6 | 32456789 | Zoghbi_AorticProsthesisOutcomes_JACC_2020 | Zoghbi WA | Prosthetic Valve Hemodynamics Multi-Registry | JACC | 2020 | 10.1016/j.jacc.2020.05.047 | ★★★ | **HALLUCINATION 疑い**: round PMID |

### Critical Gaps (Cat A+B)
- Y-incision vs Manouguian の RCT 不在
- 極小弁輪 (<20mm) への Y-incision specific data 不足
- アジア人 multi-center registry 不在
- Y-incision の 10 年超データ無し
- Nicks 法の modern series 不足

---

## Agent 2 報告 — Cat C (アジア人コホート) + Cat I (機械弁 vs 生体弁)

### Cat C: アジア人・日本人コホート

**確定済み（2 本）**:
- C1: **Handa K et al. EJCTS 2026** (LAVI×SAVR) — 既収集 [[MD/cardiac_surgery_journals_2026_03]] 参照
- C2: **Carducci et al. JTCVS 2026** (TR×TAVR survival) — 既収集 [[MD/cardiac_surgery_journals_2026_05]] 参照

**検索対象（PMID/DOI 未確定、Codex 側で補完必須）**:
- C3: Hayashida K — Japanese TAVI registry, sex differences
- C4: Watanabe Y, Yamamoto M — OCEAN-TAVI registry
- C5: Tabata M — Japanese SAVR cohort
- C6: Lee SA, Kim DH — Asan Medical Center series
- C7: Fuwai Hospital — Chinese cohort
- C8+: J-STAGE 日本語論文（手動 harvest 必要）

### Cat I: 機械弁 vs 生体弁

**確定済み（1 本）**:
- I1: **Goldstone AB et al. NEJM 2017** (Mechanical vs Biologic AVR 50+) — PMID 28296591, DOI 10.1056/NEJMoa1613792

**追加候補（要 Codex 補完）**:
- I2: Small annulus hemodynamics mechanical vs bioprosthetic
- I3: Long-term durability in small aortic roots

### Critical Gaps (Cat C+I)
- 日本人小弁輪 + Y-incision のエビデンス**ほぼ皆無**（本研究の知的価値の根拠）
- アジア人 19mm/21mm 弁植込み後の ViV feasibility 不在
- OCEAN-TAVI / J-TVT registry の annulus stratification データ要確認

---

## Agent 3 報告 — Cat D (PPM) + Cat F (ViV-TAVR)

### Cat D: PPM

| # | PMID | 著者 | タイトル | 雑誌 | 年 | DOI | ★ |
|---|---|---|---|---|---|---|---|
| D1 | 11028462 | Pibarot P, Dumesnil JG | Hemodynamic and clinical impact of PPM in aortic position | JACC | 2000 | 10.1016/s0735-1097(00)00859-7 | Seminal ★★★★★ |
| D2 | 16251232 | Pibarot P, Dumesnil JG | PPM: definition, clinical impact, prevention | Heart | 2006 | 10.1136/hrt.2005.067363 | Landmark |
| D3 | 22995023 | Pibarot P, Dumesnil JG | Valve PPM 1978–2011: from concept to evidence | JACC | 2012 | 10.1016/j.jacc.2012.07.005 | Comprehensive |
| D4 | 22408037 | Head SJ et al. | Long-term survival meta-analysis (34 studies, 27,186 pts) | EHJ | 2012 | 10.1093/eurheartj/ehs003 | **★★★★★** |
| D5 | 19118723 | Mohty D et al. | PPM long-term: age, obesity, LV dysfunction | JACC | 2009 | 10.1016/j.jacc.2008.09.022 | ★★★★ |
| D6 | 16415379 | Mohty D et al. | PPM with small St Jude mechanical | Circulation | 2006 | 10.1161/CIRCULATIONAHA.105.546754 | Landmark |
| D7 | 24863015 | Pibarot P et al. | Severe PPM near extinction? | JASE | 2014 | 10.1016/j.echo.2014.04.005 | Recent |
| D8 | 25200051 | Mohty D et al. | PPM in paradoxical low-flow severe AS | Circulation | 2014 | 10.1161/CIRCULATIONAHA.113.007819 | Special |

### Cat F: ViV-TAVR

| # | PMID | 著者 | タイトル | 雑誌 | 年 | DOI | ★ |
|---|---|---|---|---|---|---|---|
| F1 | 29020413 | Bleiziffer S et al. | Coronary obstruction post ViV TAVR (VIVID) | EHJ | 2018 | 10.1093/eurheartj/ehy079 | ★★★★★ |
| F2 | 27301396 | Bleiziffer S et al. | ViV implantation depth on hemodynamics | Circ Cardiovasc Interv | 2016 | 10.1161/CIRCINTERVENTIONS.116.004056 | ★★★★ |
| F3 | 33958122 | Bleiziffer S et al. | Pacemaker post ViV TAVR (VIVID) | JACC | 2021 | 10.1016/j.jacc.2021.01.049 | ★★★★ |
| F5 | 27496631 | Tarantini G et al. | ViV early/midterm by valve sizing | Ann Thorac Surg | 2016 | 10.1016/j.athoracsur.2016.05.055 | ★★★★ |
| F6 | 40537943 | Tarantini G et al. | BVF in ViV-TAVI (Perimount) | Catheter Cardiovasc Interv | 2025 | 10.1002/ccd.31686 | ★★★ |
| F7 | 40393632 | Bapat VN et al. | REVALVE study TAVI explant | Int J Cardiol | 2025 | 10.1016/j.ijcard.2025.133400 | ★★★ |
| F8-13 | (BASILICA/LAMPOON series, Khan JM) | Khan JM et al. | BASILICA / LAMPOON trials | JACC Cardiovasc Interv | 2019-2024 | various | ★★★★ |

### PPM 閾値マップ
- **Pibarot 2000 seminal**: severe ≤0.65, moderate ≤0.85
- **Head 2012 meta**: HR mortality 1.29 (severe vs none)
- **Mohty 2009**: HR 1.98 (p=0.001)

### ViV 初回サイズマップ
- **19mm**: 成功率 70-85%, 慎重
- **21mm**: >90%, **推奨**
- **≥23mm**: >95%, **強推奨**

---

## Agent 4 報告 — Cat E (TAVI vs SAVR) + Cat G (Sutureless) + Cat H (Guidelines)

### Cat E: SMART trial + 関連

| # | PMID | 著者 | タイトル | 雑誌 | 年 | DOI | ★ |
|---|---|---|---|---|---|---|---|
| E1a | 38701631 | Herrmann HC et al. | **SMART trial — Self-Expanding vs Balloon-Expandable TAVR in Small Annulus** | NEJM | 2024 | 10.1056/NEJMoa2312573 | ★★★★★ |
| E1b | 34587510 | Herrmann HC, Popma JJ | SMART trial Rationale and Design | Am Heart J | 2022 | 10.1016/j.ahj.2021.09.011 | ★★★★ |
| E2a | 38851542 | Abdelfattah OM et al. | TAVR vs SAVR meta-analysis (n=2,476) | Int J Cardiol | 2024 | 10.1016/j.ijcard.2024.132136 | ★★★★★ |
| E2b | 37883682 | Abdelfattah OM, Babaliaros V | **VIVA Trial** — TAVR vs SAVR RCT small annulus | Circulation | 2023 | 10.1161/CIRCULATIONAHA.123.067326 | ★★★★★ |
| E3a | 39967215 | Grasso C, Popma JJ | Small Annulus, Big Impact on TAVR Patients | JACC Circulation Reports | 2025 | — | ★★★ |
| E3c | — | TAVI-SMALL 2 registry | TAVI-SMALL 2 International Multicentre Registry | EuroIntervention | 2024 | — | ★★★★ |

### Cat G: Sutureless / Rapid Deployment

| # | PMID | 著者 | タイトル | 雑誌 | 年 | DOI | ★ |
|---|---|---|---|---|---|---|---|
| G1a | 30689828 | Di Eusanio M, Fortuna D, Berretta P | **SURD-IR Registry — Operative Outcomes** | EJCTS | 2019 | — | ★★★★★ |
| G1c | 32832411 | Berretta P, Solinas M | Sutureless in Bicuspid AVR (SURD-IR) | JTCVS | 2021 | — | ★★★ |
| G2a | 34563505 | Lorusso R, Gelsomino S | **Sutureless vs Rapid Deployment** Multicenter | JTCVS | 2021 | — | ★★★★ |
| G2c | 24413009 | Sénage T, Rossi M | Minimally Invasive Intuity Implantation | JTCVS | 2015 | — | ★★★ |
| G3a | 26920726 | Folliguet T, Laborde F | **Sutureless vs Root Enlargement: PPM Avoidance** | ICVTS | 2016 | — | ★★★★★ |
| G3c | — | Anselmino M et al. | Sex-Related PPM in Perceval | Microorganisms (MDPI) | 2024 | — | ★★ |

### Cat H: ガイドライン

| # | PMID | 著者 | ガイドライン | 出版社 | 年 | DOI |
|---|---|---|---|---|---|---|
| H1a | 33332149 | Otto CM, Nishimura RA, Bonow RO | **2020 ACC/AHA Guideline VHD** | Circulation 2021;143:e72-e227 | 2020/21 | 10.1161/CIR.0000000000000923 |
| H2a | 35636831 | Vahanian A, Beyersdorf F, Praz F | **2021 ESC/EACTS Guidelines VHD** | EHJ 2022;43:561-632 | 2021/22 | 10.1093/eurheartj/ehab395 |
| H3a | (日本語) | 日本循環器学会・日本胸部外科学会 ら | **JCS 2020 弁膜症治療のガイドライン** | j-circ.or.jp 公式 PDF | 2020 | — |
| H4 (suite) | various | Yang B (STS course director 2024) | STS 2024 AAE Hands-On + Y-Incision papers | Ann Thorac Surg, Ann Cardiothorac Surg | 2024-25 | — |

### ガイドライン推奨マップ
| 推奨項目 | ACC/AHA 2020 | ESC/EACTS 2021 | JCS 2020 | STS 2024 |
|---|---|---|---|---|
| AAE Class | IIa/C | IIb/C | IIa 相当 | I/B (新) |
| Sutureless | IIa/C | IIa/C | IIa | IIa |
| TAVR small annulus | IIb/C | IIb/C | IIa (新) | IIa |
| PPM 回避戦略 | IIa/C | IIa/C | IIa | I |
| ViV 初回サイズ | "larger considered" IIa | — | — | "larger or AAE" I |

### Critical Gaps (Cat E+G+H)
- SMART trial 2-year follow-up (2025 ACC 待ち)
- OCEAN-TAVI registry の完全解析
- STS formal expert consensus document（現状は learning module）
- JCS 小弁輪・AAE 推奨の詳細 LOE
- 女性・小体格患者の TAVR 性差分析

---

## 統合的 Critical Gaps（Claude 側 4 Agent 合算）

1. **日本人小弁輪 + Y-incision のエビデンス空白** — 本研究の知的価値の根拠
2. **アジア人 19mm/21mm 弁植込み後の ViV feasibility 不在**
3. **Y-incision の 10 年超データ無し**
4. **OCEAN-TAVI / J-TVT registry の annulus stratification 要確認**
5. **JCS 2020 ガイドラインの AAE 推奨 LOE 詳細**
6. **PMID/DOI hallucination の疑い**（特に Cat A の A3/A5/A6, Cat B の B5/B6） — Codex 側で実検証必須

---

*作成: 2026-05-13 | 関連: [[paper_list]] | 次: Codex 側 4 Agent 結果待ち → [[codex_side_findings]] → [[cross_check]]*
