---
title: 文献入手状況（P1/P2）
date: 2026-07-26
---

# 文献入手状況

## 入手済み・フルテキスト（Europe PMC / PMC OA）

`pdf_text/refs/*.txt`

| ファイル | 文献 |
|---|---|
| ref05_Sarikouch2026_decell20y | 脱細胞化肺homograft 20年（EJCTS 2026;68(2):ezag087） |
| ref06_Horke2024_ARISE5y | ARISE 5年（EJCTS 2024;65(4):ezae121） |
| ref10_DodgeKhatami2025_ECHSA | ECHSA 3,007例 小児低侵襲 |
| ref12_Arabkhani2023_AVIATOR | AVIATOR PSM（EJCTS 2023;63(2):ezac514） |
| ref17_Arabkhani2023_AVPD | 術中加圧可視化device（ezad291） |
| ref20_Sarikouch2016_decell10y | 脱細胞化10年（ezw050） |
| ref21_Morales2020_Xeltis | Xeltis XPV 2試験（Front Cardiovasc Med） |
| ref22_Kasahara2024_hybridfabric | 自己組織化ハイブリッド生地（ATS Short Rep） |
| ozaki1196_JACCAdv2025 | **Ozaki 1,196例 中期成績（JACC Adv 2025）** ← シードは未引用 |
| sarnaik2024_decision | Ross vs 機械弁 18歳の意思決定解析（JTCVS Open 2024） |

## 入手済み・抄録

- `pdf_text/refs/seed25_abstracts.txt` … シード引用25本のうち24本（ref[13] MMCTSはPMIDなし）
- `abs_ch2〜ch9`（scratchpad）… P2の系統検索で特定した主要50本

## WebFetch で本文相当を取得（OUPはcurl 403だがWebFetchは通る）

- ezae427 Wilbring 経腋窩1000例 … 主要数値取得（**ペースメーカ率のみ未取得**）
- ezae197 Squiers/Brinkman 脱細胞化への批判的論評 … 論旨取得（ARISE registry 再手術回避 5年92.4%→10年69.5% の指摘はARISE原文Table 2で照合済）
- ehaf038 De Paulis EHJ 2025 … **Table 4の計測カットオフのみ取得**（eH>9mm / gH>17mm TAV・>20mm BAV / coaptation>4mm / commissural orientation>140°）

## ★未入手（本人にDL依頼中）

| 優先 | 文献 | PMID | 何が必要か |
|---|---|---|---|
| 1 | De Paulis R, et al. Current status of aortic valve repair surgery. Eur Heart J 2025;46(15):1394-1411 | **39950993** | 耐久性データ表・annuloplasty術式比較。第3・4章の土台 |
| 2 | 2025 ESC/EACTS Guidelines for the management of VHD | **40878291**(EJCTS) / **40878295**(EHJ) | Recommendation Table（AR手術／人工弁の年齢閾値／Heart Valve Centre症例数）。Class/Levelの一次確認 |
| 3 | Vojacek J, et al. EACTS Expert Consensus Statement on the Ross Procedure in Adult Patients. EJCTS 2026;68(2):ezaf295 | **41063405** | clinical statements本文。第5章の中核 |
| 4 | Badhwar V, et al. Outcomes following initial multicenter experience with robotic AVR. JTCVS 2024;167(4):1244-1250 | **38246340** | **PubMedに抄録が無く数値ゼロ**。ロボットAVRの唯一の多施設データ |
| 5 | George I, et al. 1-Year results, polymer surgical mitral valve. JACC 2025;86(7):515-526 | **40589299** | 1年死亡9.1%の内訳、INR実測値 |
| 6 | Wilbring M, et al. transaxillary AVR 1000例. EJCTS 2024;66(6):ezae427 | **39602603** | ペースメーカ植込み率のみ |
| 7 | Squiers JJ, Brinkman WT. EJCTS 2024;65(6):ezae197 | **38830037** | 原文（1–2ページ）確認用 |

置き場所: `future_cardiac_surgery/pdf/` に `YYYY_Author_Journal_Topic-Hyphenated.pdf` 命名で保存 → `pdftotext -layout` で `pdf_text/` に展開して使う。


---

## 追加取得（2026-07-26）— §6.1「凍結保存 vs 脱細胞化」用

本人がDLし、`pdf/` に規約名でrename・move、`pdf_text/` に `pdftotext -layout` 済み。DOIはCrossRefで全件解決確認。

| 分類 | 文献 | PMID | DOI | 用途 |
|---|---|---|---|---|
| ① 凍結保存・肺位 | Dekens E, et al. Interact CardioVasc Thorac Surg 2019;28:503-9 | 30476047 | 10.1093/icvts/ivy316 | 10年PHG置換回避82±6%、多変量で残る唯一の因子＝サイズ |
| ① 凍結保存・大動脈位 | Nappi F, et al. J Thorac Cardiovasc Surg 2018;156:1357-1365.e6 | 29759737 | 10.1016/j.jtcvs.2018.04.040 | 210例、再手術32.8%・SVD再手術27.1% |
| ① 凍結保存の免疫 | Hawkins JA, et al. J Thorac Cardiovasc Surg 2000;119:324-30 | 10649208 | 10.1016/S0022-5223(00)70188-7 | **PRA 1.9%→92%（3.3か月）。樹状細胞が術後9年まで残存** |
| ② 脱細胞化＋凍結（同種） | Ruzmetov M, et al. J Thorac Cardiovasc Surg 2012;143:543-9 | 22340029 | 10.1016/j.jtcvs.2011.12.032 | SG 39 vs SCA 61 の同一施設比較 |
| ③ 脱細胞化ブタ弁 | Simon P, et al. Eur J Cardiothorac Surg 2003;23:1002-6 | 12829079 | 10.1016/s1010-7940(03)00094-0 | 小児4例中3例死亡・異物型反応 |
| ④ 脱細胞化＋非凍結 | Cebotari S, et al. Circulation 2011;124(11 Suppl):S115-23 | 21911800 | 10.1161/CIRCULATIONAHA.110.012161 | ④の原典プロトコル・5年 explant回避100%・zスコア収束 |
| ④ 残存免疫原性 | Ebken JMN, et al. Eur J Cardiothorac Surg 2021;59:773-82 | 33544830 | 10.1093/ejcts/ezaa393 | **OA (PMC8083949, CC BY-NC)**。18-25歳＞48-73歳、個人差10倍 |
| ④ 残存免疫原性（経時） | Oripov F, et al. Front Cardiovasc Med 2022;9:895943 | 36017105 | 10.3389/fcvm.2022.895943 | **OA (PMC9395941, CC BY)**。28日で術前値へ復帰 |

日本の凍結保存手順（プログラムフリーザー・液体窒素）は福嶌ら Organ Biology 2017;24(1):29-36（J-STAGE OA、
doi:10.11378/organbio.24.29）から。制度確認と同一文献。
