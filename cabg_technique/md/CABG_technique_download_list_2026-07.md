---
title: CABG 手技レビュー「これから冠動脈外科をやる外科医のために」— DL対象論文60編
date: 2026-07-28
purpose: 図表入りHTML手技レビュー（Ross/ロボット手術レビュー同形式）の一次文献リスト
scope: 心臓の脱転・展開／導管採取／グラフトデザイン／多枝バイパスの実践／吻合／術中評価／トレーニング
verification: 全60件のPMIDをPubMed esummaryでタイトル・雑誌・年・DOI・PMC(OA)を照合済み（2026-07-28）
related:
  - "[[OPCAB_technique_review]]"        # opcab_technique/ 114編（DOIベース・MEDLINE非採録誌中心）
  - "[[CABG_evidence_reading_list_2026-07]]"  # cabg_evidence/ 265 PMID（臨床エビデンス）
---

# CABG 手技レビュー DL対象論文 60編

## 取得状況（2026-07-28 時点）

| 区分 | 件数 | 置き場所 |
|---|---:|---|
| ✅ PDF取得済み（OA自動取得 20 ＋ 購読誌 手動DL 28） | **48** | `cabg_technique/pdf/` |
| ✅ 本文キャプチャ済み（MMCTS＝PDFが存在しない動画教材） | **3** | `cabg_technique/md/mmcts/` |
| ⏳ 未取得 | **9** | → [`CABG_technique_remaining_9.md`](CABG_technique_remaining_9.md)（優先「高」は2件のみ） |

全48 PDF は1ページ目ヘッダのタイトル照合で本人確認済み（誤ファイル0）。

**取得ルートの知見** — NCBI の PMC ウェブ（`pmc.ncbi.nlm.nih.gov/articles/PMCxxxx/pdf/`）は **reCAPTCHA でブロック**、`oa.fcgi` が返す `oa_pdf` の ftp パスも **https では404**。実際に通るのは **Europe PMC の `https://europepmc.org/articles/PMCxxxxx?pdf=render`**（負荷時に失敗するのでリトライ必須）。AME系（Ann Cardiothorac Surg / J Thorac Dis）は DOI 解決先ページの `/article/view/<id>/pdf`、MDPI は Cloudflare を避けて `res.mdpi.com/d_attachment/...` から取得できる。MMCTS は `data-page` の Inertia JSON で全文取得可（購読不要）。

## 0. 選定の考え方

**目的** — 「これから冠動脈外科をやる外科医」が読むべき **how-to（手技）** 文献を、図表・動画が期待できるものを優先して集める。臨床アウトカム比較（OPCAB vs ONCAB の生存率など）は既存の `cabg_evidence/`（265 PMID・PDF 54本DL済み）が担当するため、本リストは意図的に **手技記述** に振っている。

**既存資産との関係**

| 既存 | 内容 | 本リストとの関係 |
|---|---|---|
| `~/Documents/All Papers/Clinical/Coronary/` | PDF 28本 | ほぼ **グラフト生物学・臨床エビデンス**。手技論文は事実上ゼロ → 本リストと重複なし |
| `cabg_evidence/` | 265 PMID / PDF 54本 | 臨床エビデンス。**重複は 1件のみ（PMID 27298393・PDF未取得）** |
| `opcab_technique/` | 114編（DOIベース） | Innovations/MMCTS/Op Tech 中心。**MEDLINE非採録誌が多くPMIDなし** → 本リスト（PMID付き・on-pump含む）と相補 |

**絞り込み** — PubMed E-utilities で34クエリ（展開/脱転・導管採取・グラフト構成・吻合・術中評価・教育など）→ 重複除去後 1,238編 → 手技記述性・図表期待値・教育的価値で 60編を確定。

**凡例** — 🔓 = PMC でオープンアクセス（原典図の引用が可能）／📹 = 動画教材（MMCTS）／★ = 章の中核

---

## Batch 1（1–20）総論・解剖 ＋ 心臓の脱転・展開・血行動態

### §1. 総論・冠動脈外科の全体像と解剖（4編）

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 1 | 39484768 | Comprehensive Review of Coronary Artery Anatomy Relevant to Cardiac Surgery | Curr Cardiol Rev 2025;21(2) | 🔓 |
| 2 | 12813693 | Beating heart coronary artery bypass: operative strategy and technique | Semin Thorac Cardiovasc Surg 2003;15(1):83-91 | |
| 3 | 28972063 | Current Practice of State-of-the-Art Surgical Coronary Revascularization | Circulation 2017;136(14):1331-45 | |
| 4 | 41977076 | Complex Coronary Artery Bypass Grafting: Intraoperative Challenges and Surgical Strategies in Contemporary Practice | J Clin Med 2026;15(7) | 🔓 |

### §2. 心臓の脱転・展開・スタビライゼーション（13編）★本レビューの核心

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 5 | 10875598 | Techniques of exposure and stabilization in off-pump coronary artery bypass graft | J Card Surg 1999;14(5):392-400 | |
| 6 | 11093536 | Exposure and mechanical stabilization in off-pump CABG via sternotomy | Ann Thorac Surg 2000;70(5):1736-40 | |
| 7 | 10543532 | "Single suture" for circumflex exposure in off-pump CABG | Ann Thorac Surg 1999;68(4):1428-30 | |
| 8 | 14514548 | Deep pericardial stitch enables hemodynamically stable exposure of beating heart | Asian Cardiovasc Thorac Ann 2003;11(3):203-7 | |
| 9 | 15561035 | Hemodynamic changes during posterior vessel off-pump CABG: deep pericardial suture vs apical suction | Ann Thorac Surg 2004;78(6):2057-62 | |
| 10 | 17387194 | Deep pericardial suture vs apical suction for off-pump bypass grafting | Asian Cardiovasc Thorac Ann 2007;15(2):123-6 | |
| 11 | 15276546 | Ninety-degree anterior cardiac displacement in OPCAB: the Starfish cardiac positioner | Ann Thorac Surg 2004;78(2):679-84 | |
| 12 | 10969664 | Heart displacement during off-pump CABG: how well is it tolerated? | Ann Thorac Surg 2000;70(2):466-72 | |
| 13 | 10800817 | Hemodynamic changes and right heart support during vertical displacement of the beating heart | Ann Thorac Surg 2000;69(4):1188-91 | |
| 14 | 9594865 | Vertical displacement of the beating heart by the octopus tissue stabilizer: influence on coronary flow | Ann Thorac Surg 1998;65(5):1348-52 | |
| 15 | 21658018 | Cardiac displacement-induced hemodynamic instability during OPCAB and its predictors | Acta Anaesthesiol Scand 2011;55(7):870-7 | |
| 16 | 36824043 | Hemodynamic management during off-pump CABG: narrative review of proper targets for safe execution | Korean J Anesthesiol 2023;76(4):267-79 | 🔓 |
| 17 | 39156549 | Standardized exposure of the lateral and posterior wall in off-pump minimally invasive CABG | JTCVS Tech 2024;26:61-63 | 🔓 |

> §2 は「深部心膜牽引糸（Lima stitch / single suture）」「心尖吸引ポジショナー（Starfish/Xpose）」「垂直脱転の血行動態と右心支持」の3系統を、原典（1998–2007）＋現代の標準化（2023–24）で押さえる構成。

*（Batch 1 の20編 = §1 の #1–4 ＋ §2 の #5–17 ＋ §3 の #18–20）*

---

## Batch 2（21–40）導管採取 ＋ グラフトデザイン

### §3. 導管採取（14編）

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 18 | 34961523 | All we need to know about internal thoracic artery harvesting and preparation for myocardial revascularization | J Cardiothorac Surg 2021;16(1):354 | 🔓 |
| 19 | 34787965 | Step-by-step harvesting of various grafts for coronary artery bypass surgery | MMCTS 2021 | 📹 |
| 20 | 32979482 | Skeletonized or Pedicled Harvesting of LITA: Systematic Review and Meta-analysis | Semin Thorac Cardiovasc Surg 2021;33(1):10-18 | |
| 21 | 38775645 | How to harvest the left internal mammary artery — a randomized controlled trial | Interdiscip Cardiovasc Thorac Surg 2024;38(5) | 🔓 |
| 22 | 33171172 | Left Internal Mammary Artery Skeletonization Reduces Bleeding — A Randomized Controlled Trial | Ann Thorac Surg 2021;112(3):794-801 | |
| 23 | 42025666 | Open vs Intact Pleura During Internal Thoracic Artery Harvesting: Meta-Analysis of RCTs | Ann Thorac Surg 2026;122(2):498-508 | |
| 24 | 30505758 | Robotic-assisted bilateral internal thoracic artery harvest | Ann Cardiothorac Surg 2018;7(5):704-6 | 🔓 |
| 25 | 40589185 | The 10 Commandments of Robotic Bilateral Internal Thoracic Artery Harvesting | Innovations 2025;20(6):511-16 | 🔓 |
| 26 | 34318106 | The radial artery: an important component of multiarterial coronary surgery and considerations for its optimal harvest | JTCVS Tech 2021;5:46-55 | 🔓 |
| 27 | 30552888 | Technical Aspects of the Use of the Radial Artery in Coronary Artery Bypass Surgery | Ann Thorac Surg 2019;108(2):613-22 | |
| 28 | 41432491 | Endoscopic or Open Radial Artery Harvest in Coronary Artery Bypass Surgery | NEJM Evid 2026;5(1) | |
| 29 | 31376117 | No-touch saphenous vein graft harvesting technique for CABG | Gen Thorac Cardiovasc Surg 2020;68(3):248-53 | |
| 30 | 33155775 | The endoscopic no-touch saphenous vein harvesting technique | MMCTS 2020 | 📹 |
| 31 | 27525230 | The Right Gastroepiploic Artery Graft for CABG: A 30-Year Experience | Korean J Thorac Cardiovasc Surg 2016;49(4):225-31 | 🔓 |

### §4. グラフトデザイン・多枝バイパスの設計（12編）★

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 32 | 30505752 | Bilateral internal thoracic artery grafting: in situ or composite? | Ann Cardiothorac Surg 2018;7(5):673-80 | 🔓 |
| 33 | 32439394 | Optimal Configuration for Bypass of the LAD During Bilateral ITA Grafting | Ann Thorac Surg 2020;110(6):1917-25 | |
| 34 | 27406988 | Bilateral Internal Thoracic Artery Configuration for CABG: A Prospective Randomized Trial | Circ Cardiovasc Interv 2016;9(7):e003518 | 🔓 |
| 35 | 36983276 | Reconstruction Technique Options for Achieving Total Arterial Revascularization and Multiple Arterial Grafting | J Clin Med 2023;12(6):2275 | 🔓 |
| 36 | 39718243 | Arterial conduits for coronary bypass grafting: the set-point concept | Eur Heart J 2025;46(10):922-25 | |
| 37 | 24973924 | Saphenous Vein vs Right ITA as a Y-Composite Graft (SAVE RITA trial) | J Thorac Cardiovasc Surg 2014;148(3):901-7 | |
| 38 | 31539513 | Sequential Versus Individual Saphenous Vein Grafting During CABG | Ann Thorac Surg 2020;109(4):1165-73 | |
| 39 | 30838388 | A single sequential "snake" saphenous vein graft versus separate left and right vein grafts | Eur J Cardiothorac Surg 2019 | |
| 40 | 28651939 | Competitive flow in coronary bypass surgery: the roles of FFR and arterial graft configuration | J Thorac Cardiovasc Surg 2017;154(5):1570-75 | |

---

## Batch 3（41–60）吻合・難病変・術中評価 ＋ トレーニング

### §4（続き）

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 41 | 36094465 | How to deal with nonsevere stenoses in CABG — a critical perspective on competitive flow | Curr Opin Cardiol 2022;37(6):468-73 | |
| 42 | 33247735 | How to build a multi-arterial coronary artery bypass programme: a stepwise approach | Eur J Cardiothorac Surg 2020;58(6):1111-17 | 🔓 |
| 43 | 41779085 | Bypass graft design assisted by virtual reality simulation in multi-vessel CABG | Gen Thorac Cardiovasc Surg 2026 | |

### §5. 吻合手技・難病変・術中評価（9編）

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 44 | 34705350 | Myocardial revascularization: Tips and tricks for performing a coronary anastomosis | MMCTS 2021 | 📹 |
| 45 | 39617372 | ［冠動脈吻合の方法］Methods of Coronary Anastomosis（和文） | 胸部外科 2024;77(10):777-80 | |
| 46 | 34977715 | Coronary endarterectomy for diffusely diseased coronary artery: an ace in the hole | JTCVS Tech 2021;10:133-37 | 🔓 |
| 47 | 28315286 | Coronary Endarterectomy or Patch Angioplasty for Diffuse LAD Disease | Thorac Cardiovasc Surg 2018;66(6):491-97 | |
| 48 | 33689738 | New Proximal Anastomosis Technique for Calcified Ascending Aorta in CABG | Ann Thorac Surg 2021;112(4):e307-10 | |
| 49 | 34589167 | Surgical strategies for severely atherosclerotic (porcelain) aorta during CABG | World J Cardiol 2021;13(8):309-24 | 🔓 |
| 50 | 31421104 | Epiaortic Ultrasound to Prevent Stroke in Coronary Artery Bypass Grafting | Ann Thorac Surg 2020;109(1):294-301 | |
| 51 | 27298393 | Techniques and standards in intraoperative graft verification by transit time flow measurement | Eur J Cardiothorac Surg 2017;51(1):26-33 | |
| 52 | 35242366 | Transit time flow measurement and outcome in CABG for surgeon and trainee | J Thorac Dis 2022;14(1):36-42 | 🔓 |

> #51 は `cabg_evidence` のリストに PMID のみ収載（PDF未取得）。本プロジェクトで実体を取得する。

### §6. トレーニング・ラーニングカーブ（8編）★

| # | PMID | 論文 | 出典 | OA |
|---:|---|---|---|:--:|
| 53 | 19114195 | Improvement in coronary anastomosis with cardiac surgery simulation | J Thorac Cardiovasc Surg 2008;136(6):1486-91 | |
| 54 | 32891660 | Coronary Anastomosis Simulation: Directed Interventions to Optimize Success | Ann Thorac Surg 2021;111(6):2072-77 | |
| 55 | 23456683 | How to build your own coronary anastomosis simulator from scratch | Interact Cardiovasc Thorac Surg 2013;16(6):772-76 | 🔓 |
| 56 | 34647125 | Humanoids for teaching and training coronary artery bypass surgery to the next generation of cardiac surgeons | Interact Cardiovasc Thorac Surg 2022;34(2):185-92 | 🔓 |
| 57 | 38307118 | Is Single LIMA-LAD Bypass Appropriate for OPCAB Training? | Thorac Cardiovasc Surg 2024;72(6):458-62 | |
| 58 | 39820718 | Safety and efficiency of trainees performing bilateral ITA coronary bypass grafting using the T-graft technique | Eur J Cardiothorac Surg 2024;67(1) | |
| 59 | 37425436 | Quality control in a training course of off-pump coronary artery bypass grafting surgery | JTCVS Open 2023;14:252-60 | 🔓 |
| 60 | 14643813 | Safe evolution towards routine off-pump CABG: negotiating the learning curve | Eur J Cardiothorac Surg 2003;24(6):947-52 | |

---

## 一括取り込み用 PMID ブロック

**Batch 1**
```
39484768 12813693 28972063 41977076 10875598 11093536 10543532 14514548 15561035 17387194 15276546 10969664 10800817 9594865 21658018 36824043 39156549 34961523 34787965 32979482
```

**Batch 2**
```
38775645 33171172 42025666 30505758 40589185 34318106 30552888 41432491 31376117 33155775 27525230 30505752 32439394 27406988 36983276 39718243 24973924 31539513 30838388 28651939
```

**Batch 3**
```
36094465 33247735 41779085 34705350 39617372 34977715 28315286 33689738 34589167 31421104 27298393 35242366 19114195 32891660 23456683 34647125 38307118 39820718 37425436 14643813
```

**全60件**
```
39484768 12813693 28972063 41977076 10875598 11093536 10543532 14514548 15561035 17387194 15276546 10969664 10800817 9594865 21658018 36824043 39156549 34961523 34787965 32979482 38775645 33171172 42025666 30505758 40589185 34318106 30552888 41432491 31376117 33155775 27525230 30505752 32439394 27406988 36983276 39718243 24973924 31539513 30838388 28651939 36094465 33247735 41779085 34705350 39617372 34977715 28315286 33689738 34589167 31421104 27298393 35242366 19114195 32891660 23456683 34647125 38307118 39820718 37425436 14643813
```

## 補足

- **OA（PMC）は 18/60**。原典図の転載可否は PMC の license で個別確認（CC BY / CC BY-NC-ND のみ引用可）。
- **MMCTS 3編（📹）** は動画教材。過去の調査どおり `mmcts.org` は curl のみで全文（Inertia JSON）取得可。
- 予備候補（枠が空いたとき用）: 18442527（stabilization/exposure）, 25662959（研修医のOPCAB安全性）, 16242504（OPCAB習熟と品質管理）, 23977628（GEA・ACS OA）, 30094221（dual inflow anaortic how-to・ACS OA）, 30505754（SVGを ITA からの composite に）。
