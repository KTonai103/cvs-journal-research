---
title: Off-pump CABG（OPCAB）手技論文 網羅的レビュー
subtitle: 図表・ビデオ中心のオペレーティブ・テクニック文献サーベイ
date: 2026-05-30
scope: Off-pump CABG（OPCAB / MIDCAB / MICS-CABG / robotic-TECAB / anaortic 全動脈）の手技論文
journals:
  - JTCVS Techniques
  - Multimedia Manual of Cardio-Thoracic Surgery (MMCTS)
  - Annals of Cardiothoracic Surgery
  - Operative Techniques in Thoracic and Cardiovascular Surgery
  - Innovations (Technology and Techniques in CT & Vascular Surgery)
sources:
  - CrossRef REST API (ISSN別検索)
  - PubMed E-utilities (手技アングル別検索)
  - Europe PMC (abstract取得・タイトル照合)
tags:
  - OPCAB
  - off-pump
  - coronary-bypass
  - surgical-technique
  - MIDCAB
  - robotic-CABG
  - anaortic
  - journal-review
  - "2026"
---

# Off-pump CABG（OPCAB）手技論文 網羅的レビュー

> [!abstract] このレビューの要旨
> Off-pump CABG（OPCAB）の**手術手技（how-to）**に焦点を当て、**図表が豊富なオペレーティブ・テクニック論文**と**ビデオ解説論文**を中心に網羅的にサーベイした。CrossRef（雑誌ISSN別）＋PubMed（手技アングル別）で **3,154編** を収集 → off-pump系タイトルで **1,344編** に絞り込み → 手技系雑誌・手技系タイトルで **376編** をコア候補とし → 16体の分類エージェントで判定して最終的に **114編の手技論文**を確定した。媒体内訳は 🖼️図表豊富 67 / 📹ビデオ 16 / 📄標準 31、年代は 2001–2026、オープンアクセス 30編。**全114編のDOIは実在を確認済み（誤リンク0件）**。

## 0. この調査について（スコープと方法）

**目的** — OPCABの「やり方」を学ぶための一次文献を、**図解アトラス**と**手術ビデオ**を中心に体系的に集約する。臨床アウトカム（生存率比較等）が主題の研究は原則として対象外とし（§4に主要RCTのみ文脈として掲載）、手技の記述（展開・脱転・吻合・グラフト構成・デバイス・低侵襲/ロボットアプローチ・コツと落とし穴）を主眼とした論文を採録した。

**検索戦略（多段階・機械的収集）**
1. **CrossRef REST API** — 手技系5誌（JTCVS Techniques 2666-2507 / MMCTS 1813-9175 / Operative Techniques in Thoracic CV Surgery 1522-2942 / Annals of Cardiothoracic Surgery 2225-319X / Innovations 1559-0879）＋一般6誌（JTCVS, Ann Thorac Surg, EJCTS, ICVTS/Interdiscip, J Card Surg, J Cardiothorac Surg）を ISSN別に複数クエリ（off-pump / beating-heart / anaortic / MIDCAB / anastomosis）で検索。
2. **PubMed E-utilities** — 手技アングル別15クエリ（technique/how-to, anaortic, exposure-stabilization, MIDCAB, robotic-TECAB, shunt-flow, BITA, hybrid, video-multimedia, composite-graft, multivessel, review, conversion, special-population）。
3. **Europe PMC** — 各候補のabstract取得とDOI↔タイトル照合（一次検証）。
4. **分類** — 16体のエージェントが各論文を「手技論文か否か・サブトピック・媒体（video/figure-rich/standard）・重要度★1-5・日本語要約」に分類。
5. **DOI検証** — 確定114編の全DOIをCrossRef個別照会で再検証（タイトル一致確認、誤リンク0件）。検証ログ → [`output/doi_verification_opcab_technique.md`](../output/doi_verification_opcab_technique.md)。

**絞り込みの流れ:** 3,154編（収集）→ 1,344編（off-pump系タイトル）→ 376編（手技系雑誌/タイトル）→ **114編（手技論文確定・重複除去後）**。

**媒体バッジの凡例:** 🖼️ = 図表が豊富なオペテク（術中写真・シェーマ多数）／📹 = ビデオ解説論文（手術動画つき）／📄 = 標準的記述／🔓 = オープンアクセス／★ = 手技教材としての重要度（★5=ランドマーク的how-to・必読）。

## 1. サマリー統計

- **確定手技論文: 114編**（重複除去後）／年代 **2001–2026**／オープンアクセス **30編**
- 媒体内訳: 🖼️ 図表豊富 **67** ／ 📹 ビデオ **16** ／ 📄 標準 **31**
- 重要度内訳: ★5×17 ／ ★4×41 ／ ★3×49 ／ ★2×7

**掲載誌別**

| 雑誌 | 編数 |
|---|---:|
| Innovations | 47 |
| Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | 17 |
| JTCVS Techniques | 16 |
| Annals of Cardiothoracic Surgery | 14 |
| Operative Techniques in Thoracic and Cardiovascular Surgery | 6 |
| The Annals of Thoracic Surgery | 3 |
| European Journal of Cardio-Thoracic Surgery | 2 |
| Brazilian Journal of Cardiovascular Surgery | 2 |
| Interactive CardioVascular and Thoracic Surgery | 1 |
| Kyobu geka. The Japanese journal of thoracic surgery | 1 |
| Surgery Today | 1 |
| Zhonghua yi xue za zhi | 1 |
| Surgical Technology Online | 1 |
| General Thoracic and Cardiovascular Surgery | 1 |
| Vestnik khirurgii imeni I. I. Grekova | 1 |

## 2. 必読ガイド（横断キュレーション）

### 2-1. 📹 ビデオ解説論文（手術動画つき）

OPCABの手技を**動画で学べる**論文。MMCTS（EACTS公式マルチメディア手技マニュアル）が中心で、anaortic全動脈・MIDCAB・ロボットTECABの各アプローチを step-by-step 動画で提供する。

| ★ | 年 | 論文 | 雑誌 | DOI |
|:--:|:--:|---|---|---|
| 5 | 2025 |  Anaortic total arterial minimally invasive coronary artery bypass grafting: T… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2025.001](https://doi.org/10.1510/mmcts.2025.001) |
| 5 | 2025 |  Total arterial, anaortic, off-pump coronary artery bypass grafting | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2025.048](https://doi.org/10.1510/mmcts.2025.048) |
| 5 | 2025 |  Robotic-assisted, minimally invasive direct coronary artery bypass—preparatio… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2025.045](https://doi.org/10.1510/mmcts.2025.045) |
| 5 | 2020 |  Robotic off-pump totally endoscopic hand-sewn coronary artery bypass using in… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.001](https://doi.org/10.1510/mmcts.2020.001) |
| 5 | 2020 |  Off-pump bilateral internal thoracic artery grafting—surgical technique | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.047](https://doi.org/10.1510/mmcts.2020.047) |
| 5 | 2020 |  Mastering Off-Pump, Total Arterial Coronary Artery Bypass Grafting: A step-by… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.003](https://doi.org/10.1510/mmcts.2020.003) |
| 5 | 2013 |  Minimally invasive cardiac surgery—coronary artery bypass graft (MICS-CABG) | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1093/mmcts/mmt007](https://doi.org/10.1093/mmcts/mmt007) |
| 4 | 2024 |  Robotic-assisted minimally invasive multivessel coronary bypass surgery | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2023.105](https://doi.org/10.1510/mmcts.2023.105) |
| 4 | 2024 |  Minimally invasive off-pump bypass grafting—positioning the right posterior d… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2024.012](https://doi.org/10.1510/mmcts.2024.012) |
| 4 | 2023 |  Robotic redo totally endoscopic coronary artery bypass to the right coronary … | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2023.012](https://doi.org/10.1510/mmcts.2023.012) |
| 4 | 2022 |  Robotic-assisted MIDCAB procedure through a minithoracotomy: step-by-step ins… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2022.045](https://doi.org/10.1510/mmcts.2022.045) |
| 4 | 2020 |  MIDCAB: tips and tricks for a successful procedure | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.021](https://doi.org/10.1510/mmcts.2020.021) |
| 4 | 2019 |  Robotic-assisted minimally invasive direct coronary artery bypass grafting in… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2019.011](https://doi.org/10.1510/mmcts.2019.011) |
| 4 | 2015 |  Left anterior small thoracotomy for minimally invasive coronary artery bypass… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1093/mmcts/mmv022](https://doi.org/10.1093/mmcts/mmv022) |
| 4 | 2013 |  Minimally Invasive Coronary Bypass Using Internal Thoracic Arteries via a Lef… | Innovations | [10.1177/155698451300800607](https://doi.org/10.1177/155698451300800607) |
| 4 | 2011 |  Beating heart totally endoscopic coronary artery bypass | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2010.004663](https://doi.org/10.1510/mmcts.2010.004663) |

→ ビデオ解説論文 **計16編**。

### 2-2. ★★★★★ ランドマーク手技論文（媒体問わず）

手技教材として特に価値の高い★5論文。図解アトラスとビデオの双方を含む。

| 媒体 | 年 | 論文 | 雑誌 | DOI |
|:--:|:--:|---|---|---|
| 📹 | 2025 |  Anaortic total arterial minimally invasive coronary artery bypass grafting: T… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2025.001](https://doi.org/10.1510/mmcts.2025.001) |
| 📹 | 2025 |  Total arterial, anaortic, off-pump coronary artery bypass grafting | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2025.048](https://doi.org/10.1510/mmcts.2025.048) |
| 📹 | 2025 |  Robotic-assisted, minimally invasive direct coronary artery bypass—preparatio… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2025.045](https://doi.org/10.1510/mmcts.2025.045) |
| 📹 | 2020 |  Robotic off-pump totally endoscopic hand-sewn coronary artery bypass using in… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.001](https://doi.org/10.1510/mmcts.2020.001) |
| 📹 | 2020 |  Off-pump bilateral internal thoracic artery grafting—surgical technique | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.047](https://doi.org/10.1510/mmcts.2020.047) |
| 📹 | 2020 |  Mastering Off-Pump, Total Arterial Coronary Artery Bypass Grafting: A step-by… | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2020.003](https://doi.org/10.1510/mmcts.2020.003) |
| 📹 | 2013 |  Minimally invasive cardiac surgery—coronary artery bypass graft (MICS-CABG) | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1093/mmcts/mmt007](https://doi.org/10.1093/mmcts/mmt007) |
| 🖼️ | 2026 | 🔓 Complex composite conduits for anaortic off-pump coronary artery bypass graft… | JTCVS Techniques | [10.1016/j.xjtc.2026.102269](https://doi.org/10.1016/j.xjtc.2026.102269) |
| 🖼️ | 2026 |  All-arterial anaortic off-pump coronary bypass technique | Operative Techniques in Thoracic and Cardiovascular Surgery | [10.1053/j.optechstcvs.2026.05.001](https://doi.org/10.1053/j.optechstcvs.2026.05.001) |
| 🖼️ | 2025 | 🔓 Minimally invasive coronary artery bypass grafting via left anterior minithor… | JTCVS Techniques | [10.1016/j.xjtc.2024.10.022](https://doi.org/10.1016/j.xjtc.2024.10.022) |
| 🖼️ | 2024 | 🔓 Step-by-step technique of robotic-assisted minimally invasive direct coronary… | Annals of Cardiothoracic Surgery | [10.21037/acs-2024-rcabg-0034](https://doi.org/10.21037/acs-2024-rcabg-0034) |
| 🖼️ | 2024 | 🔓 Standardized exposure of the lateral and posterior wall in off-pump minimally… | JTCVS Techniques | [10.1016/j.xjtc.2024.06.002](https://doi.org/10.1016/j.xjtc.2024.06.002) |
| 🖼️ | 2024 | 🔓 How to perform distal anastomosis using a robotic platform: totally endoscopi… | Annals of Cardiothoracic Surgery | [10.21037/acs-2023-rcabg-0211](https://doi.org/10.21037/acs-2023-rcabg-0211) |
| 🖼️ | 2023 |  Minimally Invasive Off-Pump Anaortic Complete Arterial Coronary Artery Bypass… | Innovations | [10.1177/15569845231185333](https://doi.org/10.1177/15569845231185333) |
| 🖼️ | 2020 | 🔓 Totally robotic sutured coronary artery bypass grafting: How we do it | JTCVS Techniques | [10.1016/j.xjtc.2020.05.018](https://doi.org/10.1016/j.xjtc.2020.05.018) |
| 🖼️ | 2018 |  Dual inflow, total-arterial, anaortic, off-pump coronary artery bypass grafti… | Annals of Cardiothoracic Surgery | [10.21037/acs.2018.06.17](https://doi.org/10.21037/acs.2018.06.17) |
| 📄 | 2006 |  Off-pump myocardial revascularization | Multimedia Manual of Cardio-Thoracic Surgery (MMCTS) | [10.1510/mmcts.2004.000539](https://doi.org/10.1510/mmcts.2004.000539) |

→ ★5ランドマーク **計17編**。図表豊富なオペテク（★4・🖼️）は §3 各領域に収載。

## 3. 技術領域別レビュー

以下、11領域に分けて全114編を解説する（各領域内は重要度★降順）。

### 総説・概観（Off-pump CABGの全体像）

Off-pump CABG（OPCAB）は人工心肺を用いずに拍動下で冠動脈バイパスを行う術式であり、心臓の脱転（exposure）・局所固定（stabilization）・吻合構築という3つの基本要素を統合した手技哲学そのものが手術成績を左右する。本領域に集めた論文群は、標準的なOPCABの操作手順を図解で示すオペテク総説から、低侵襲・内視鏡・ハイブリッドへ拡張した現代的レビュー、さらに15年・数万例規模の経験に基づく手技進化の概観までを収載し、OPCABの適応・歴史・標準テクニックの全体像を俯瞰できる構成となっている。各論文は、脱転・固定デバイスの発展、近位／遠位吻合の順序、冠内シャント・ブロワーの使い分けといった実地のコツを横断的に提示する。

- ★4 🖼️ **OPCAB標準手技アトラス（Yanagawa-Puskas）** — オフポンプCABGの心臓脱転から局所固定、吻合構築に至る標準的操作手順を図解豊富に解説するオペテク総説。exposure・stabilization・anastomosisという基本3要素を段階的に提示し、拍動下血行再建の実地手技を体系的に示す。〔Yanagawa B, Puskas JD. *Off-Pump Coronary Artery Bypass Grafting.* Operative Techniques in Thoracic and Cardiovascular Surgery. 2016;21(1):2-19.〕 [DOI](https://doi.org/10.1053/j.optechstcvs.2016.10.003)
- ★4 🖼️ **低侵襲アプローチとしてのOPCAB（Myung-Halkos-Puskas）** — 低侵襲冠血行再建の文脈でオフポンプCABGの操作手技を図解で解説する総説。正中切開回避を含む低侵襲戦略のなかにOPCABを位置づけ、拍動下吻合の手技的ポイントを示す。〔Myung RJ, Halkos ME, Puskas JD. *Less Invasive Approaches to Coronary Artery Bypass Grafting: Off-Pump Coronary Artery Bypass.* Operative Techniques in Thoracic and Cardiovascular Surgery. 2010;15(3):186-193.〕 [DOI](https://doi.org/10.1053/j.optechstcvs.2010.08.005)
- ★4 🖼️ **オフポンプ冠血行再建の手術手技（Sabik）** — オフポンプ冠動脈血行再建の標準手術手技を図解豊富に解説するオペテク総説。心臓脱転・局所固定・吻合構築の標準手順を順を追って提示し、拍動下手技の基本を網羅する。〔Sabik JF. *Off-Pump Coronary Revascularization: Operative Technique.* Operative Techniques in Thoracic and Cardiovascular Surgery. 2006;11(2):90-104.〕 [DOI](https://doi.org/10.1053/j.optechstcvs.2006.06.002)
- ★3 📄🔓 **現代的低侵襲冠血行再建レビュー（MICS-CABG・TECAB・ハイブリッド）** — 正中切開を回避する低侵襲冠血行再建の主要3手技、すなわちMICS-CABG・完全内視鏡下CABG（TECAB）・ハイブリッド冠血行再建を網羅的に整理した技術レビュー。各手技の安全性・有効性に関するエビデンス、コストや技術的難度といった普及障壁、今後の展望を論じ、低侵襲手技の現状を俯瞰する。〔Fatehi Hassanabad A, Kang J, Maitland A, Adams C et al. *Review of Contemporary Techniques for Minimally Invasive Coronary Revascularization.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2021;16(3):231-243.〕 [DOI](https://doi.org/10.1177/15569845211010767)
- ★3 📄 **拍動下CABGの手技的特徴（847例の経験）** — 847例の拍動下CABG経験に基づき手技の要点を体系化した論文。高位胸部硬膜外麻酔、大動脈‐冠動脈バイパスの近位吻合を先行作成し遠位吻合を所定の順序で構築する戦略、バキュームスタビライザーによる局所固定と側壁・後壁へのアクセス確保、ブロワー（加湿器付）と冠内シャントの併用といった具体的手技を解説する。〔Volkov AM, Khubulava GG, Paĭvin AA, Iurchenko DL, Kravchuk VN, Liubimov AI. *Specific features of the technique of performing coronary bypass operations on the beating heart.* Vestnik khirurgii imeni I. I. Grekova. 2012;171(2):11-6.〕 [PMID:22774542](https://pubmed.ncbi.nlm.nih.gov/22774542/)
- ★3 📄 **OPCAB手技の15年進化（28,216例）** — 15年・28,216例（OPCAB 14,030例、on-pump 14,186例）の経験からOPCABの展開・固定手技の発展を5年ごと3期に分けて概観した手技進化レビュー。当初は石灰化大動脈・高齢者など高リスク症例に選択的に適用されたOPCABが、2000–2004年には多枝病変に対し待機例の96–98%で標準的に施行されるに至った経緯と、学習曲線および落とし穴を論じる。〔Mishra YK, Mishra M, Malhotra R, Meharwal ZS et al. *Evolution of Off-Pump Coronary Artery Bypass Grafting over 15 Years.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2005;1(2):88-91.〕 [DOI](https://doi.org/10.1177/155698450500100206)

**📌 この領域の必読:** まずは図解豊富なアトラス系オペテク総説である「OPCAB標準手技アトラス（Yanagawa-Puskas）」🖼️ と「オフポンプ冠血行再建の手術手技（Sabik）」🖼️ で脱転・固定・吻合の標準手順を押さえるとよい。現代的な低侵襲展開を俯瞰するにはオープンアクセスの「現代的低侵襲冠血行再建レビュー（MICS-CABG・TECAB・ハイブリッド）」が有用（本領域に動画チュートリアル📹は含まれない）。

### Anaortic / 全動脈・no-touch aorta OPCAB

上行大動脈への鉗子操作（部分遮断・プロキシマルクランプ）はOPCABにおける周術期脳梗塞の主要因であり、これを完全に回避する「anaortic（大動脈無操作）」かつ全動脈グラフトでの完全血行再建が本テーマの主眼である。流入源を在所両側内胸動脈に限定し、橈骨動脈やRITAを用いてT/Y・K・I・λ・π型などの複合動脈グラフトを構築することで、大動脈に一切触れずに多枝再建を達成する。収載論文は、胸骨正中切開・左小開胸（MICS）・ロボット支援に至る各アプローチでの段階的手技ビデオと図解アトラス、加えて大動脈操作をやむなく行う場合のクランプレス近位吻合デバイス（HeartString・Enclose II・自動パンチング等）の使い分けを横断的にカバーする。

- ★5 🖼️🔓 **複雑複合グラフト（λ型・π型）** — 両側内胸動脈のみを流入源とする完全動脈・anaortic OPCABで、限られた導管長で多枝再建を達成するための複雑な複数吻合複合グラフト（λ型・π型）の意思決定と作製手技を図解。13か月で115例のOPCAB（97例が全動脈、93例がanaortic）のうち17例18本にこれらの複合グラフトを使用し、λ型14本・π型4本を構築、13例は完全anaortic、3例はクランプレス近位吻合を併用した。全115例で院内および1年フォロー中のグラフト不全・死亡・心筋梗塞・脳梗塞・再血行再建・深部創感染はゼロであった。〔Hynes CF, Puskas JD. *Complex composite conduits for anaortic off-pump coronary artery bypass grafting: Lambda and pi grafts.* JTCVS Techniques. 2026;36:102269.〕 [DOI](https://doi.org/10.1016/j.xjtc.2026.102269)

- ★5 🖼️ **全動脈anaortic OPCABの標準手技** — 完全動脈・大動脈無操作（anaortic/clampless）のオフポンプCABG手技を体系的に図解する手技論文。動脈グラフトのみを用い上行大動脈への操作を排した血行再建の各ステップを示す（Puskasらのグループによる手技解説）。〔Hynes CF, Kalra K, Puskas JD. *All-arterial anaortic off-pump coronary bypass technique.* Operative Techniques in Thoracic and Cardiovascular Surgery. 2026.〕 [DOI](https://doi.org/10.1053/j.optechstcvs.2026.05.001)

- ★5 📹 **Leipzig方式 MICS全動脈anaortic** — Heart Center LeipzigがルーチンとするオフポンプMICS-CABG（左前外側小開胸・両側乳動脈による完全動脈血行再建）の手技をビデオで解説。過去8年間の臨床導入経験に基づき、患者の大半が適応となるとし、患者選択基準・術前プロトコル・段階的な手術手技をstep-by-stepで提示する。〔*Anaortic total arterial minimally invasive coronary artery bypass grafting: The Leipzig technique.* Multimedia Manual of Cardio-Thoracic Surgery. 2025;2025.〕 [DOI](https://doi.org/10.1510/mmcts.2025.001)

- ★5 📹 **全動脈anaortic OPCABの要素分解習得** — 一見複雑な全動脈・anaortic・オフポンプCABGを、スケルトン化乳動脈採取・複合動脈グラフト作製・オフポンプ心臓操作という再現可能な3要素に分解し、研修医が習得すべき技術として各要素を段階的にビデオ解説。これらを統合し心停止も大動脈操作も伴わずに罹患全冠動脈を動脈グラフトで再建する流れを示す。〔*Total arterial, anaortic, off-pump coronary artery bypass grafting.* Multimedia Manual of Cardio-Thoracic Surgery. 2025;2025.〕 [DOI](https://doi.org/10.1510/mmcts.2025.048)

- ★5 🖼️ **左小開胸 全動脈anaortic how-to** — 左小開胸からオフポンプ・anaortic（no-touch）・全動脈グラフトで多枝バイパスを行う代表的how-to論文。3枝＋分枝病変の64歳症例を例に、操作段階の順序・各ステップのコツ・落とし穴を提示し、低リスク再建戦略としての技術的留意点を整理する。経験豊富な術者向けで、シミュレーションシステムの発展が普及の鍵としている。〔Mavioglu I. *Minimally Invasive Off-Pump Anaortic Complete Arterial Coronary Artery Bypass: How to Do It?* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2023;18(4):376-379.〕 [DOI](https://doi.org/10.1177/15569845231185333)

- ★5 📹 **オフポンプBITAルーチン手技** — オフポンプ両側内胸動脈（BITA）グラフトの自施設ルーチン手技をビデオで詳説。BITAは単独ITAに対する成績優位が示される一方で周術期合併症や技術的難度が普及を妨げているとし、両側ITA採取と心拍動下吻合の具体的工夫、および過去20年にわたる血行再建術式の進化過程を提示する。〔*Off-pump bilateral internal thoracic artery grafting—surgical technique.* The Multimedia Manual of Cardio-Thoracic Surgery. 2020;2020.〕 [DOI](https://doi.org/10.1510/mmcts.2020.047)

- ★5 📹 **オフポンプ全動脈CABG習得（T/Y・K・I型）** — 多枝動脈CABGの長期的利点とno-touch aorta手技を両立する、技術的難度の高いオフポンプ完全動脈血行再建をstep-by-stepでビデオ解説。両側内胸動脈と橈骨動脈の採取法、ならびに大動脈操作を最小化するT/Y型・K型・I型複合グラフトの作製・配置の各オプションを詳述し、習得には専門的トレーニングとメンタリングが不可欠とする。〔*Mastering Off-Pump, Total Arterial Coronary Artery Bypass Grafting: A step-by-step approach.* The Multimedia Manual of Cardio-Thoracic Surgery. 2020;2020.〕 [DOI](https://doi.org/10.1510/mmcts.2020.003)

- ★5 🖼️ **デュアルインフロー全動脈anaortic（RIMA-橈骨タンデム）** — 上行大動脈を一切操作せず、両側内胸動脈と橈骨動脈による全動脈デュアルインフローで完全血行再建する代表的how-to論文。RIMA在所＋橈骨動脈を端々吻合したタンデムグラフトを横洞経由で側壁・下壁に通し複数の連続末梢吻合を行い、LIMA在所で前壁を再建する。術前は両側頸動脈・椎骨動脈・鎖骨下動脈のDuplex評価を行い、心臓ポジショニングを容易にする広範な心膜切開と4つの主要心位置・スタビライザー操作も詳述する。〔Ramponi F, Seco M, Edelman JB, Sherrah AG et al. *Dual inflow, total-arterial, anaortic, off-pump coronary artery bypass grafting: how to do it.* Annals of Cardiothoracic Surgery. 2018;7(4):552-560.〕 [DOI](https://doi.org/10.21037/acs.2018.06.17)

- ★4 🖼️ **ロボット支援BIMA全動脈（double-docking）** — BIMAによる全動脈血行再建をロボット支援で行うためのdouble-docking technique（DDT）を解説し、開胸正中切開との早期成績を傾向スコアマッチング（104ペア）で比較。BIMAは技術的負荷・手術時間延長・胸骨創合併症が普及を阻むとされるが、DDT群は遠位吻合数が有意に少ない一方、術後人工呼吸・ICU滞在・在院期間が短縮した。中央値1.5年での30日死亡とMACCEを評価している。〔Yusuf MM, Bansal V, Venkatesh A, Chandrasekharan GA et al. *Robot-Assisted Minimally Invasive Coronary Artery Bypass Grafting: Total Arterial Revascularization Using the Double-Docking Technique.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2024;19(4):402-408.〕 [DOI](https://doi.org/10.1177/15569845241266250)

- ★4 📄🔓 **クランプレス近位吻合デバイス2種の比較** — OPCABの脳卒中リスク低減を目的としたクランプレス近位吻合デバイス2方式、すなわち自動吻合パンチングデバイスと大動脈シーリングデバイスの周術期成績を2施設・3703例（傾向スコアマッチ後1150例、各群575例）で比較。全死亡・脳卒中・再開胸の複合一次エンドポイントは6.3%対5.9%（OR 0.9, 95%CI 0.58-1.53, P=.81）と有意差なく、両デバイス手技の使い分けを示す実用的リファレンス。〔Gerçek M, Skuljevic T, Deutsch M, Gummert J et al. *Off-pump coronary artery bypass grafting with clampless aortic anastomosis devices: Aortic sealing devices versus automated anastomosis punching.* JTCVS Techniques. 2024;24:92-104.〕 [DOI](https://doi.org/10.1016/j.xjtc.2024.01.010)

- ★4 📄 **RITA近位断端を流入源とするno-touch法** — 上行大動脈の操作を完全に回避するため、右内胸動脈の近位断端を胸腔内の動脈血流源として用い、ここに必要長の伏在静脈を吻合する新しいno-touch aorta手技を提示。静脈は必要なだけ長くとれ、2導管の口径マッチが良好となり、近位吻合部にかかるピーク圧が低くなる利点を述べる（神経保護を狙った動脈源OPCAB）。〔Cirillo M, Messina A, Tomba MD, Brunelli F et al. *A New No-Touch Aorta Technique for Arterial-Source, Off-Pump Coronary Surgery.* The Annals of Thoracic Surgery. 2009;88(4):e46-e47.〕 [DOI](https://doi.org/10.1016/j.athoracsur.2009.07.045)

- ★4 🖼️ **HEARTSTRING IIによる手縫いクランプレス近位吻合** — 部分遮断鉗子を用いず、HEARTSTRING IIプロキシマルシールシステム（大動脈カッター＋近位シール）で大動脈への手縫い近位吻合を行うクランプレス手技の経験報告。50例で84本の伏在静脈-大動脈近位吻合を施行し、部分遮断鉗子への移行は一例もなく、近位吻合の平均所要時間は5分（範囲4-14分）、フロープローブ値も全例良好で、有害事象なく安全かつ有効と結論する。〔Schoettle GP, Jones CB. *Hand-Sewn Proximal Anastomoses in Off-Pump Coronary Artery Bypass without the Need for Partial Occlusion Clamping: Experience with the HEARTSTRING II Proximal Seal System.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2007;2(4):198-200.〕 [DOI](https://doi.org/10.1177/155698450700200406)

- ★3 🖼️🔓 **オフポンプBITA併施の左心耳閉鎖クリップ** — オフポンプ両側内胸動脈CABGの際に左心耳閉鎖クリップ（Medtronic Penditure）を併施する手術手技を図示した記事。off-pump BITA再建に左心耳閉鎖を同時に行う併施手技の手順を示す。〔Torregrossa G, Baudo M, Yakobitis A, Murray C et al. *Surgical implant of Medtronic Penditure left atrial appendage exclusion clip during off-pump bilateral internal thoracic artery coronary artery bypass grafting.* Annals of Cardiothoracic Surgery. 2024;13(2):182-183.〕 [DOI](https://doi.org/10.21037/acs-2024-afm-23)

- ★3 📄 **Enclose II使用時の安全な大動脈切開・パンチ法** — OPCABでクランプレスの近位手縫い吻合を補助するEnclose II装置の使用時に、大動脈壁の切開とパンチ孔作成を簡便かつ安全に行う新手技を解説。複数の近位吻合補助デバイスのうち広く用いられるEnclose IIの操作を、より容易・安全にする具体的なコツを示す。〔Matsushita T, Masuda S, Kanzaki T. *A Safe Technique for Using an Enclose II Anastomosis Assist Device During Off-Pump Coronary Bypass.* The Annals of Thoracic Surgery. 2016;102(6):e581-e582.〕 [DOI](https://doi.org/10.1016/j.athoracsur.2016.05.102)

- ★3 🖼️ **オフポンプBITAグラフト手技** — 心拍動下（off-pump）での両側内胸動脈グラフトの手技を扱うAnnals of Cardiothoracic Surgery掲載論文。両側ITAを用いた多枝血行再建の採取・吻合手技を図解的に解説する。〔Saha KK. *Off-pump bilateral internal thoracic artery grafting.* Annals of cardiothoracic surgery. 2014;3(2):E1.〕 [DOI](https://doi.org/10.3978/j.issn.2225-319x.2014.02.09)

- ★3 📄 **Enclose II 178例のクランプレス近位吻合成績** — OPCAB 178例（6施設、2005-2009年）でEnclose II近位吻合デバイスを用いたクランプレス近位吻合の安全性と有効性を評価。222本の近位吻合（44例で2吻合）を施行し、デバイス起因の大動脈損傷はなく、新規脳梗塞2例（1.1%）もデバイスとは無関係、1年グラフト開存率96.4%と良好で、大動脈操作低減の有用な補助デバイスと結論する。〔Seto Y, Yokoyama H, Takase S, Tanji M et al. *The Results of the Enclose II Proximal Anastomotic Device in 178 Off-Pump Coronary Artery Bypass Surgeries.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2012;7(4):242-246.〕 [DOI](https://doi.org/10.1177/155698451200700402)

- ★3 🖼️ **HeartStringによる脳神経イベント低減** — side-biting aortic clampを用いずHeartString proximal anastomotic deviceでクランプレス手縫い近位吻合を行い、周術期脳血管イベント低減を狙ったOPCAB戦略を提示。227連続例で全例にHeartStringを使用し（大動脈性状を問わず）、平均3.4本のバイパス、98%で近位吻合は1本、連続グラフトを多用した経験を報告する。〔Sakopoulos AG, Jacobson JG, Wilson DR, Huse WM. *"Beyond Beating Heart Surgery": Heartstring Device Protects against Perioperative Neurological Events.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2010;5(2):118-121.〕 [DOI](https://doi.org/10.1177/155698451000500209)

- ★2 📄🔓 **高流量微小軸流ポンプの大動脈弓クランプレス吻合** — 困難な解剖において高流量微小軸流ポンプ（MCS）留置のため、上行大動脈ではなく大動脈弓へクランプレス吻合でアプローチする代替手技を提示する技術ノート。OPCABで用いられるクランプレス近位吻合の概念をMCS留置に応用した症例である。〔Nakahara Y, Iwakura T, Marui A, Sumi K et al. *Aortic arch approach using clampless anastomosis for high-flow microaxial pump: An alternative in challenging anatomy.* JTCVS Techniques. 2026;35:102182.〕 [DOI](https://doi.org/10.1016/j.xjtc.2025.102182)

- ★2 📄 **左主幹部欠損例のオフポンプ全動脈再建** — 左主幹部が欠損するという稀な冠動脈解剖変異に対し、オフポンプ完全動脈血行再建を行った術式を示すテクニック記事。特殊な解剖条件下での全動脈グラフト配置の工夫を提示する。〔Tavilla G, Ghamati M. *Off-Pump Total Arterial Revascularization in the Absence of the Left Main Coronary Artery.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2013;8(5):389-390.〕 [DOI](https://doi.org/10.1177/155698451300800513)

**📌 この領域の必読:** 図解アトラスとしては「複雑複合グラフト（λ型・π型）」🖼️（Puskasグループ、全115例で脳梗塞ゼロの最新エビデンス付き）と「デュアルインフロー全動脈anaortic（RIMA-橈骨タンデム）」🖼️（Ramponiらの定番how-to）がまず読むべき2編。手技を映像で学ぶなら「全動脈anaortic OPCABの要素分解習得」📹と「Leipzig方式 MICS全動脈anaortic」📹のビデオチュートリアルが、採取から複合グラフト作製・配置までを段階的に習得できる必読教材である。

### 心臓の脱転・展開・スタビライゼーション

OPCABの技術的成否は、拍動を維持したまま側壁・下壁・後壁の標的血管を安定的に露出できるか否かにかかっている。本テーマは、深部心膜牽引糸・心膜スリングによる心臓のverticalization（垂直化）、心尖部吸引型ポジショナー、組織スタビライザの工夫、そして脱転に伴う右室圧迫・心拍出低下を回避する血行動態管理を扱う。収集論文は、Leuven流の標準化手技から、MICS/TECABなど小開胸・閉胸環境での露出デバイス、心尖吸引と心膜牽引の血行動態比較、脂肪内・心筋内に埋没した冠動脈の同定・固定法まで、脱転と固定の全工程を横断的にカバーしている。

- ★5 🖼️🔓 **MICS-CABGにおける側壁・後壁の標準化展開** — オフポンプMICS-CABGで最も難度の高い側壁・後壁ターゲットへのアクセスを定型化した教育的リファレンス。心臓の脱転・展開ポジショニングを段階的に標準化し、追加切開を要さずに後壁吻合まで到達可能とする手技を図解で示す。MICS環境下での再現性ある露出のテンプレートとして位置づけられる。 〔Albert A, Petrov G, Smiris K, Angleitner P. *Standardized exposure of the lateral and posterior wall in off-pump minimally invasive cardiac surgical coronary artery bypass grafting.* JTCVS Techniques. 2024;26:61-63.〕 [DOI](https://doi.org/10.1016/j.xjtc.2024.06.002)

- ★5 📄 **Leuven標準化オフポンプ血行再建** — 胸骨正中切開下に両側内胸動脈を採取し、左側心膜の水平縫合で前面を展開、ルーチンシャント下に前壁を吻合する。側壁・下壁は房室軸を変形させずに段階的に展開し、まず左房直下の後部心膜にスリングを固定して徐々に吊り上げ、心臓をcradle状に支持する。zenith（天頂）まで挙上した後に心尖吸引デバイスで安定化・整形し、厳格なno-touch aorta下にin-situ動脈グラフトへfree graftを吻合する、再現性が高くポンプ転換を要さない完成された標準術式。 〔DeSimone J, Sergeant P. *Off-pump myocardial revascularization.* Multimedia Manual of Cardio-Thoracic Surgery. 2006;2006(1009):mmcts.2004.000539.〕 [DOI](https://doi.org/10.1510/mmcts.2004.000539)

- ★4 🖼️🔓 **ロボットTECABでの回旋枝領域展開** — ロボット支援完全内視鏡下CABG（TECAB）において、最も到達困難な回旋枝（circumflex）領域の側壁・下壁ターゲットを露出するための心臓ポジショニング手技を図解で提示。内視鏡的視野の制約下で標的血管を露出するための心臓の向き付け・展開の要点を示す。 〔Bonatti J, Ashraf SF, Seese L, Toma C et al. *Exposure technique for the circumflex artery territory in robotic totally endoscopic coronary artery bypass grafting.* Annals of Cardiothoracic Surgery. 2024;13(5):452-454.〕 [DOI](https://doi.org/10.21037/acs-2023-rcabg-12)

- ★4 📹 **小開胸オフポンプでのPDAポジショニング** — 小開胸からオフポンプで前壁のみならず側壁・下壁、特に右後下行枝（PDA）へ到達する際の心臓ポジショニングと安定化を動画で詳説する。多枝症例では胸腔鏡的冠動脈同定を併用し、ポンプ非使用下での挑戦的な心臓の向き付け手技を実演する。 〔. *Minimally invasive off-pump bypass grafting—positioning the right posterior descending coronary artery.* Multimedia Manual of Cardio-Thoracic Surgery. 2024;2024.〕 [DOI](https://doi.org/10.1510/mmcts.2024.012)

- ★4 🖼️ **ハートポジショナー直接牽引による露出** — 多枝MICS-CABG（6〜9cm左開胸）で困難な側壁・下壁の標的露出に対し、単/多吸引式心臓ポジショナーを標的血管の側方に装着し小開胸創へ直接牽引する手技。側壁心膜縁を胸壁へ牽引した上でポジショナーを引き、最終的にエピカルディアルスタビライザで吻合する。10例中9例をオフポンプ完遂し（平均2.8±0.8吻合、4枝逐次吻合も2例）、死亡・胸骨切開転換なしと報告。 〔Kikuchi K, Une D, Suzuki K, Endo Y et al. *Off-Pump Minimally Invasive Coronary Artery Bypass Grafting with a Heart Positioner Direct Retraction for a Better Exposure.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2015;10(3):183-187.〕 [DOI](https://doi.org/10.1177/155698451501000307)

- ★4 🖼️ **MICABGの深部心膜牽引糸バリエーション** — MICABGで側壁・下壁の心表面を露出するための深部心膜牽引縫合の有効な変法を提示。24例の多枝MICABGに適用し、LAD全例、鈍縁枝20例、PDA12例を吻合（平均2.3グラフト）、胸骨切開転換なし。追加切開を要さず多枝吻合に十分な操作空間と可動性を確保できる簡便な手技として記述される。 〔Pande S, Gupta D, Siddartha C, Bansal A et al. *Exposures of Lateral and Inferior Cardiac Surface for Coronary Anastomosis during Minimally Invasive Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2015;10(1):73-75.〕 [DOI](https://doi.org/10.1177/155698451501000114)

- ★4 🖼️ **閉胸下の低プロファイル心尖吸引ポジショナー** — 閉胸・拍動心モデル（ブタ6頭）で、ポート経由に挿入する低プロファイル心尖吸引型ポジショナーにより心後面を露出し、その際の右室機能・全身血行動態を5段階で評価。Trendelenburg体位なしでの脱転は心拍出量・冠血流・右室収縮期圧・平均動脈圧・右室拡張末期/収縮末期容量を有意に低下させ、Trendelenburg併用が血行動態維持に寄与することを定量的に示した、内視鏡的多枝CABGに向けた基礎的検討。 〔Mykytenko J, Vassiliades TA, Vinten-Johansen J. *Displacement of the Beating Heart with a Low-Profile Suction-Based Apical Positioning Device in a Closed Chest.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2007;2(1):14-19.〕 [DOI](https://doi.org/10.1177/155698450700200103)

- ★3 📄 **心外膜エコーによる埋没標的血管の同定** — OPCABで視診・触診では同定困難な心筋内・脂肪内埋没冠動脈を描出するため、高周波心外膜エコー（VeriQ/MediStim）を導入。89例中299吻合のうち12枝（4.0%）が埋没冠動脈で、ECUS群（10例）では手術時間が有意に延長したが術後成績に差はなく、全例ポンプ転換なくオフポンプ完遂。標的血管局在化の術中補助手技として提示される。 〔Hayakawa M, Asai T, Kinoshita T, Suzuki T et al. *Target Vessel Detection by Epicardial Ultrasound in Off-Pump Coronary Bypass Surgery.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2013;8(4):249-252.〕 [DOI](https://doi.org/10.1097/imi.0b013e3182a75e95)

- ★3 🖼️ **スタビライザの逆向き装着（reverse mounting）** — MIDCABでOctopusアーム型組織スタビライザを肋骨開創器に逆向きに装着する簡便な工夫。これにより胸腔内でアーム有効長を最大5cm延長でき、COPD・高BMI・胸腔が大きい症例でスタビライザアームの柔軟性と操作性を高める技術的tipとして紹介される。 〔Mourad F, Duncan AJ. *Tissue Stabilizer Reverse Mounting in Minimally Invasive Direct Coronary Artery Bypass, a Simple Tool in Difficult Times.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2009;4(2):117-117.〕 [DOI](https://doi.org/10.1177/155698450900400211)

- ★3 🖼️ **心尖吸引対心膜牽引の血行動態比較** — 三枝病変27例の拍動心血行再建で、側壁・下壁露出を心尖吸引デバイス（Xpose）と標準的心膜牽引糸の両法で各患者内対照として比較。LIMA-LAD吻合後に各法で血行動態（PiCCO心拍出量・Swan-Ganz・経食道心エコー）を測定。側壁露出時の心係数/平均動脈圧はXpose 1.8±0.6/67±12、心膜牽引1.9±0.6/68±12と有意差なく、いずれも合併症なく完遂。露出法選択の判断材料を提供する。 〔Gummert JF, Raumanns J, Opfermann UT, Bossert T et al. *Hemodynamic Assessment Using Apical Suction versus Pericardial Retraction in Beating Heart Surgery.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2008;3(3):125-130.〕 [DOI](https://doi.org/10.1097/imi.0b013e3182a75e95)

- ★3 📄 **脂肪内冠動脈の牽引糸固定法** — 吸引型スタビライザは脂肪組織が冠動脈とのクッションとなり、脂肪内に深く走行する血管の固定が不十分になる問題に対する工夫。標的血管剥離後、冠動脈両側の脂肪に5-0プロリンの連続over-and-over縫合を置いて側方へ牽引し、スタビライザ脚の下に通して吸引力で固定する。脂肪のbankが平坦化することで固定と可視化を同時に改善する簡便な手技。 〔Ito T, Nakayama M, Abe T, Hagiwara H, Nakayama T, Yoshizumi T. *Stabilizing technique of intra-fat coronary artery in off-pump coronary artery bypass grafting.* Kyobu geka. The Japanese journal of thoracic surgery. 2008;61(6):460-1.〕 [PMID:18536293](https://pubmed.ncbi.nlm.nih.gov/18536293/)

- ★3 🖼️ **アームレス多吸引式心臓ポジショナー** — アームを持たず3つの独立したシリコン製吸引カップで構成される新規多吸引式心臓ポジショナー。心尖だけでなく側壁・下壁・右室壁を含む心室の多様な面を-300mmHgで把持でき、術者の好みに応じて装着位置を選択可能。多枝OPCAB 15例に適用し、側壁・下壁を含む全標的を血行動態を損なわず露出・吻合でき、人工心肺下のCONVENTIONAL CABGと同等の視野が得られたと報告する、安価で可変性の高いデバイス。 〔Arai H, Mizuno T, Yoshizaki T, Itoh F et al. *A New Multisuction Cardiac Positioner for Multivessel Off-Pump Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2006;1(3):126-130.〕 [DOI](https://doi.org/10.1177/155698450600100307)

- ★3 📄 **有窓PTFEパッチによる心臓固定** — オフポンプ多枝CABGの機械的固定法として、吻合部周囲の心筋に4本の糸を深く通し、それを有窓PTFEパッチに通して緩徐に牽引することで固定・露出を得る簡便な手技。95例に施行し、全冠動脈領域で良好な固定が得られたと報告。専用スタビライザに依存しないローコストな固定法として提示される。 〔Rama A, Mohammadi S, Leprince P, Gandjbakhch I. *A simple method for heart stabilization during off-pump multi-vessel coronary artery bypass grafting: surgical technique and short term results.* European Journal of Cardio-Thoracic Surgery. 2001;19(1):105-107.〕 [DOI](https://doi.org/10.1016/s1010-7940(00)00604-7)

**📌 この領域の必読:** 段階的スリング挙上から心尖吸引による天頂展開までを完成させた **Leuven標準化オフポンプ血行再建**（📄）と、側壁・後壁露出を定型化した図解リファレンスである **MICS-CABGにおける側壁・後壁の標準化展開**（🖼️）が二大基本文献。実技イメージを掴むには、PDA到達のポジショニングを実演する動画 **小開胸オフポンプでのPDAポジショニング**（📹）が有用である。

### 吻合手技・グラフト構成

OPCABでは拍動心という制約下で、出血と心筋虚血を最小化しつつ確実な吻合を完成させる工夫が成績を左右する。本テーマは末梢（遠位）/中枢（近位）吻合の具体的手技、複合グラフト（Y/T/I/composite）やシーケンシャル配置によるconduit構成、さらに手縫いに代わる吻合コネクタ・デバイスの活用までを横断的に扱う。収集論文は、TECAB/MICSにおける吻合アクセスの克服法、no-touch aortaを志向した動脈導管・追加導管の選択、自動コネクタやレーザー支援sutureless吻合、無血視野・虚血軽減の補助手技と、臨床から実験モデルまで幅広い手技的知見を含む。

- ★5 🖼️🔓 **ロボットTECABの遠位吻合手技** — da Vinciプラットフォームを用いた完全内視鏡下CABG（TECAB）における内胸動脈-冠動脈の遠位吻合を、ステップごとに視覚的に解説した手技論文。閉胸下・拍動心という制約下での縫合運針とグラフト把持のコツを段階的に示し、ロボット吻合の標準化に資する。〔Bonatti J, Ashraf SF, Winter M, Rubino TE et al. *How to perform distal anastomosis using a robotic platform: totally endoscopic coronary artery bypass.* Annals of Cardiothoracic Surgery. 2024;13(4):382-384.〕 [DOI](https://doi.org/10.21037/acs-2023-rcabg-0211)

- ★4 📄🔓 **骨格化右胃大網動脈をMICS導管に** — 上行大動脈に partial clamp が困難な症例やRCA高度狭窄例に対し、骨格化右胃大網動脈（RGEA）をMICS-CABGの追加導管として用いることでno-touch aortaかつ完全動脈性血行再建を達成する手技。428例中78例（18.2%）でRGEAを使用し全例で大動脈非接触、総動脈化93.6%・完全血行再建98.7%、院内死亡ゼロと良好な成績を報告。〔Sakai H, Yamauchi A, Tachibana K, Masuda K et al. *Minimally invasive coronary artery bypass grafting using the skeletonized right gastroepiploic artery.* JTCVS Techniques. 2024;28:82-90.〕 [DOI](https://doi.org/10.1016/j.xjtc.2024.09.016)

- ★4 📄 **MICS CABGの中枢吻合補助手技** — 左小開胸MICS CABGで困難な上行大動脈アクセスを克服する近位吻合の補助手技。ThoraTrak開創器を頭側・右方へ牽引して大動脈を露出し、吸引先端を60度屈曲させたOctopusスタビライザーで肺動脈を尾側へ牽引、柔軟なside-bitingクランプを掛けて手縫い吻合を行う。本法で31箇所の近位吻合を全例問題なく完成させた。〔Kikuchi K, Endo Y. *Assistive Techniques for Proximal Anastomosis in Minimally Invasive Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2017;12(3):224-226.〕 [DOI](https://doi.org/10.1177/155698451701200312)

- ★3 🖼️🔓 **自動コネクタOctoconによるTECAB吻合** — オフポンプ・内視鏡環境向けの自動マイクロステープル式コネクタOctoconを用いた冠動脈吻合手技をex vivoブタ心で実証。自己整列するステープル技術で導管側・冠動脈側のコネクタ半体をそれぞれ装着し両者を接合する3ステップ法で、single/jump/Y-graft構成を作成。ロボット支援下で18吻合を施行し96%が一発成功と、閉胸条件下での操作性と標準化可能性を示した。〔Gianoli M, de Jong AR, Wassink HM, Gründeman PF et al. *Coronary Connector Facilitated Total Endoscopic Coronary Artery Bypass: An Ex Vivo Feasibility Study.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2024;19(6):640-647.〕 [DOI](https://doi.org/10.1177/15569845241288540)

- ★3 🖼️ **右前小開胸経由の近位吻合補助手技** — MICS CABGにおいて右前小開胸（right anterior small thoracotomy）を介して近位（中枢）吻合を行うための補助手技を図示した技術論文。標準的な左開胸とは異なるアクセス経路から上行大動脈への吻合を可能にする工夫を提示する。〔Sakai H, Kikuchi K, Masuda K, Sai Y et al. *Adjunctive Technique for Proximal Anastomosis via Right Anterior Small Thoracotomy in Minimally Invasive Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2024;19(2):210-212.〕 [DOI](https://doi.org/10.1177/15569845241237541)

- ★3 📄 **セグメンタルクランプ＋遠位灌流オンレイ吻合** — 拍動心下のオンレイ（onlay）吻合中の心筋虚血を軽減する手技。2〜3cmの冠動脈切開後にカニューレで遠位冠動脈へ大腿動脈血を灌流（外シャント）し、近位・遠位をスネアクランプした状態で踵側からカニューレ挿入部へ向けて吻合を進める。途中で近位クランプをオンレイ部へ移動しグラフトを開放して早期再灌流を得る。95例で周術期心筋梗塞・術中血行動態破綻・30日死亡なし。〔Minato N, Okada T, Kanemoto S, Zempo N. *Segmental clamp and distal perfusion technique for reducing myocardial ischemia during coronary onlay grafting on a beating heart.* Surgery Today. 2018;48(5):566-570.〕 [DOI](https://doi.org/10.1007/s00595-017-1623-6)

- ★3 📄 **No-touch大伏在静脈のシーケンシャル構成** — OPCABGにおけるNo-touch法（周囲組織付きで採取）大伏在静脈グラフトの早期成績を後方視的に評価。3枝病変124例で静脈グラフト144本・吻合284箇所、構成はNTSVG-OM-PDAシーケンシャル99例を中心にD・PLV・RCAへの各種シーケンシャル/単独配置を提示。No-touch静脈グラフトの平均血流量は51.9±2.4 ml/minで、院内死亡なし・吻合部出血再開胸1例（0.8%）と良好。〔Hua K, Liu TS, Li Y, Zhao Y, Zheng JB, Zhou N, Zhou SY, Dong R.. *Short-term clinical safety and efficacy of No-touch great saphenous vein harvesting technique for off-pump coronary artery bypass grafting.* Zhonghua yi xue za zhi. 2018;98(20):1601-1604.〕 [DOI](https://doi.org/10.3760/cma.j.issn.0376-2491.2018.20.015)

- ★3 🖼️ **Trinity Clipによる完全動脈性Y字グラフト** — 両側内胸動脈を用いた完全動脈性MIDCABで、Trinity Clip吻合コネクターを使い遊離RITAをLITAに接合してRITA-LITA Y字グラフトを構成し、標的冠動脈（LAD・OM・PLV・PDA）へ装着する吻合手技。ブタ急性モデル3頭で小開胸経由に迅速なY字グラフト作成と各標的への到達・開存を確認した実験的概念実証。〔Stecher D, Bronkers G, Hoefer IE, Pasterkamp G et al. *Total Arterial Minimally Invasive Direct Coronary Artery Bypass Surgery Facilitated by the Trinity Clip Connector.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2015;10(6):389-393.〕 [DOI](https://doi.org/10.1177/155698451501000604)

- ★3 📄 **ELANAレーザー支援sutureless冠動脈コネクタ** — Excimer Laser Assisted Nonocclusive Anastomosis（ELANA）冠動脈コネクタを用いたITA-LAD/RITA-RCA吻合をブタOPCABモデルで作成し、6ヶ月後の治癒を評価。全4吻合がFitzGibbon grade Aで完全開存、走査電顕で吻合面の完全な内皮化、OCT/IVUSで内腔側0.06mmの内膜被覆と最小限の内膜肥厚を確認。手縫いに代わる非閉塞型sutureless吻合デバイスの長期治癒性を示す。〔Stecher D, Agostoni P, Pasterkamp G, Hoefer IE et al. *Six-Month Healing of the Nonocclusive Coronary Anastomotic Connector in an Off-Pump Porcine Bypass Model.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2014;9(2):130-136.〕 [DOI](https://doi.org/10.1097/imi.0000000000000055)

- ★3 🖼️ **ポロキサマー407による無血視野の確保** — 拍動心OPCABの冠動脈切開部出血を制御する新材料として、室温では粘性液体・体温で即座にゲル化する非毒性のポロキサマー407逆熱応答ポリマーを冠動脈内に注入する手技をブタ6頭で評価。LITA-LAD吻合で注入前後の出血量を比較し、吻合後に冷生理食塩水でゲルを溶解、完成血管造影でグラフト開存と分枝閉塞・内腔欠損の有無を確認。スネアやシャントに代わる無血視野確保の補助法。〔Cohn WE, Tuzun E, Simonak R, Baimbridge F. *Hemostatic Control of Coronary Arteries with Poloxamer 407 Reverse-Thermal Polymer during Off-Pump Coronary Artery Bypass Surgery in a Pig Model.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2007;2(1):36-39.〕 [DOI](https://doi.org/10.1177/155698450700200108)

- ★3 🖼️ **経腹アプローチによる右胃大網動脈OPCAB** — 右胃大網動脈（RGEA）を導管に用いた経腹的（transabdominal）アプローチによるOPCABの手技論文。開胸せず腹部からRGEAを採取・配置し下壁系冠動脈へ吻合する非典型的な導管利用と conduit 配置の工夫を図示する。〔Tavilla G. *Transabdominal Off-Pump Coronary Artery Bypass Grafting Using the Right Gastroepiploic Artery.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2005;1(1):32-34.〕 [DOI](https://doi.org/10.1177/155698450500100104)

- ★2 📄🔓 **OPCABG併施box-lesionアブレーション** — オフポンプCABGに心房細動box-lesionアブレーションを併施する新手技。本来胸腔鏡下心外膜アブレーション用に設計された灌流電極付き両極性屈曲クランプデバイスを用い、拍動心下で完全血行再建とアブレーションを同時に施行。発作性/持続性AF 8例で死亡・重大合併症なく、中央値14ヶ月で7例（87.5%）が洞調律を維持。〔Zotov A, Borisov D, Troitskiy A, Khabazov R. *Novel Technique for Box-Lesion Ablation of Atrial Fibrillation Combined with Off-Pump Coronary Surgery.* Brazilian Journal of Cardiovascular Surgery. 2023;38(3):326-330.〕 [DOI](https://doi.org/10.21470/1678-9741-2022-0146)

**📌 この領域の必読:** 図解豊富な手技解説として最重要は **ロボットTECABの遠位吻合手技**（🖼️ ロボット遠位吻合の段階的アトラス）。臨床実装の観点では **骨格化右胃大網動脈をMICS導管に** がno-touch aorta・完全動脈化を実成績で裏づける必読論文であり、デバイス吻合の将来像としては図解実証の **自動コネクタOctoconによるTECAB吻合**（🖼️）が押さえどころ。

### 冠動脈シャント・血流評価・血行動態

OPCABでは心拍動下に冠動脈を一時遮断して吻合するため、遠位灌流の維持・無血視野の確保・血行動態の安定化が成否を分ける。冠内シャントは虚血を最小化しつつ吻合部の視認性を高める基本デバイスであり、その挿入法・止血法の工夫が標準化されている。本テーマの論文群は、冠内シャントの簡便な挿入・シーリング手技、blowerに依存しない止血、低心機能例での機械的循環補助（微小軸流ポンプ・ミニ体外循環）併用といった、血流評価と血行動態維持の具体的テクニックを横断的に扱う。

- ★3 🖼️🔓 **微小軸流ポンプ補助OPCAB（低心機能例）** — 人工心肺が相対的禁忌の低駆出率症例に対し、微小軸流ポンプで左室をアンロードし循環補助しながらOPCABを完遂する手技を提示する。心拍動下の冠動脈一時遮断・心臓脱転に伴う血行動態破綻を機械的補助で回避し、on-pump回避と確実な血行再建を両立させる戦略を示す。 〔Sun E, Stone M, Adams DH, Anyanwu A. *Microaxial flow pump-assisted off-pump coronary artery bypass for low ejection fraction with relative contraindication to cardiopulmonary bypass.* JTCVS Techniques. 2025;34:126-128.〕 [DOI](https://doi.org/10.1016/j.xjtc.2025.08.028)

- ★3 🖼️ **逆熱感受性ゲルによるシャントシーリング** — 冠内シャント周囲からの残存出血を、逆熱感受性ゲル（poloxamer P407）を冠動脈腔に注入してシールすることで止血する手技。縫合結紮前に吻合部へ氷片を当ててゲルを溶解・除去することで、blowerを使わず無血視野を維持する。5例19吻合での検討で、シャント操作後に再出血した1例を除き止血が得られ、CK-MB上昇や心電図・局所壁運動変化なく施行可能であった。 〔Agostini M, Lemut F, Di Gregorio V, Grossi C. *Thermosensitive Polymer Use for Shunt Sealing in Off-Pump Coronary Artery Bypass.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2010;5(2):122-124.〕 [DOI](https://doi.org/10.1177/155698451000500210)

- ★3 📄 **micro-bulldog鉗子併用シャント挿入法** — マイクロブルドッグ鉗子を補助に用いて冠動脈内シャントを簡便に挿入する手技。鉗子によるテストクランプで虚血プレコンディショニング効果を得つつ、シャントを迅速かつ容易に留置し、吻合部および遠位冠動脈の灌流を確保しながら明瞭な視野を得られる。 〔Yokoyama H, Takase S, Misawa Y, Takahashi K et al. *A simple technique of introducing intracoronary shunts for off-pump coronary artery bypass surgery.* The Annals of Thoracic Surgery. 2004;78(1):352-354.〕 [DOI](https://doi.org/10.1016/s0003-4975(03)01156-1)

- ★3 📄 **「Shunt shuffle」シャント挿入テクニック** — 限られた切開孔（arteriotomy）から冠動脈内シャントの両端を留置する際の煩雑さを解消する「shunt shuffle」という簡便な工夫。遠位灌流を維持し無血視野を確保するシャントを、迅速・無外傷・容易に挿入できる手順を示す。 〔Patel NC, Pullan D, Fabri BM. *'Shunt shuffle' - a simple technique of introducing intracoronary shunts for off-pump coronary artery bypass.* European Journal of Cardio-Thoracic Surgery. 2002;21(6):1121-1122.〕 [DOI](https://doi.org/10.1016/s1010-7940(02)00120-3)

- ★3 📄 **ポンプ補助下beating-heart血行再建** — ミニ体外循環装置とbeating-heartデバイスを併用したon-pump beating心筋血行再建の手技解説。心停止を行わずに循環補助下で吻合を行う方法の主要手技と臨床生理学的側面を提示し、低心機能例などでの血行動態維持戦略を扱う。 〔Glauber M, Farneti A, Bevilacqua S, Karimov J. *Pump-assisted beating heart surgery.* Multimedia Manual of Cardio-Thoracic Surgery. 2007;2007(0219).〕 [DOI](https://doi.org/10.1510/mmcts.2004.000943)

**📌 この領域の必読:** 低心機能・人工心肺禁忌例での血行動態維持戦略として「微小軸流ポンプ補助OPCAB（低心機能例）」（図解豊富 🖼️）、無血視野を得る止血の工夫として「逆熱感受性ゲルによるシャントシーリング」（図解豊富 🖼️）が要点。シャント挿入の実務では「micro-bulldog鉗子併用シャント挿入法」「『Shunt shuffle』シャント挿入テクニック」が定番の手技的工夫である（本テーマには動画チュートリアルは含まれない）。

### MIDCAB / MICS-CABG（低侵襲直視下）

胸骨正中切開を回避し、左前小開胸（LAST）を中心とした小切開から直視下に内胸動脈を採取してオフポンプ・拍動下に冠動脈吻合を行う低侵襲直視下OPCABの領域である。LITA-LAD単枝吻合を基本とするMIDCABから、両側内胸動脈・橈骨動脈を組み合わせた多枝完全動脈血行再建を目指すMICS-CABG、ロボット支援LITA採取やハイブリッド血行再建まで適応が拡大しており、創部疼痛・出血・感染の低減と早期回復が利点となる。収集した論文は、セットアップ・体位・ポート配置といった術式の確立過程から、直視下/胸腔鏡的/ロボット支援によるLITA採取、no-touch aorta複合グラフト戦略、導管損傷時のベイルアウト、再手術・併施手術への応用までを網羅し、図譜・ビデオによる教育的リファレンスを多数含む。

- ★5 🖼️🔓 **左前小開胸MICS-CABGの確立と進化** — 左前小開胸（左第4-5肋間）によるMICS-CABGのセットアップ、術野展開、グラフト採取と吻合までの一連の術式を、確立から発展の過程とともに体系的に提示する原著的手技論文。低侵襲冠動脈バイパスの定石的ワークフローを示す教育的リファレンスとして位置づけられる。〔Verevkin A, Dashkevich A, Gadelkarim I, Shaqu R et al. *Minimally invasive coronary artery bypass grafting via left anterior minithoracotomy: Setup, results, and evolution of a new surgical procedure.* JTCVS Techniques. 2025;29:28-39.〕 [DOI](https://doi.org/10.1016/j.xjtc.2024.10.022)
- ★5 📹 **ロボット支援MIDCAB（採取〜吻合の段階解説）** — ロボット支援によるLIMA採取と左前小開胸でのオフポンプLIMA-LAD直視下吻合を、患者体位・ロボットポート配置・鎮痛/局所麻酔戦略・導管採取・吻合手技まで段階的に解説するビデオチュートリアル。近位/びまん性単枝LAD病変、LAD慢性完全閉塞、ハイブリッド血行再建が適応で、胸骨切開回避による迅速な回復とLIMA-LADの生存利益を両立させる点と初期学習曲線への対処を強調する。〔*Robotic-assisted, minimally invasive direct coronary artery bypass—preparation, conduit harvest and execution.* Multimedia Manual of Cardio-Thoracic Surgery. 2025;2025.〕 [DOI](https://doi.org/10.1510/mmcts.2025.045)
- ★5 📹 **no-touch aorta完全動脈MICS-CABG（LITA-RA Y）** — 左小開胸からのオフポンプ・大動脈ノータッチで完全動脈血行再建を行うMICS-CABGの代表的ビデオ解説。多枚交換可能なブレード付き肋骨開創器で直視下にLITAを採取し、橈骨動脈は内視鏡的に採取してLITA-RA間にY吻合を作成、専用冠動脈スタビライザーと遠隔挿入シャフト付きハート・ポジショナーを用いてLADおよび鈍縁枝/後下行枝への多枝吻合を行う。〔Lemma M, Atanasiou T, Contino M. *Minimally invasive cardiac surgery—coronary artery bypass graft (MICS-CABG).* Multimedia Manual of Cardio-Thoracic Surgery. 2013;2013(0):mmt007-mmt007.〕 [DOI](https://doi.org/10.1093/mmcts/mmt007)
- ★4 📄🔓 **3本動脈・4吻合のMIDCAB（複合グラフト配置）** — 多枝病変に対し3本の動脈グラフトと4ヶ所の動脈吻合で完全血行再建を行うMIDCABをステップ毎に詳述する手技報告。まずLIMA-RAをendo-to-side「T」グラフトとして作成し、RIMAをLADへ、LIMA-OM1を側々吻合、続いてDg枝を加えたLIMA-OM1-Dgのジャンプ吻合、さらにPDAへLIMA-RA-PDAを構築するという複合動脈配置を提示する。〔Grujic D, Aleksic V, Gazibara T, Milicevic V et al. *Triple Arterial Minimally Invasive Direct Coronary Artery Bypass Grafting: Step-By-Step Technique Report.* Brazilian Journal of Cardiovascular Surgery. 2025;40(5):e20240193.〕 [DOI](https://doi.org/10.21470/1678-9741-2024-0193)
- ★4 🖼️🔓 **右側アプローチMIDCAB（術前計画と手技）** — 右冠動脈系を標的とした右小開胸直視下MIDCABの術前計画と手術手技を図譜的に解説する。標的血管に応じて左側ではなく右側からアプローチする際の切開部位・術野展開・吻合の要点を示し、左前小開胸では到達困難なRCA領域への低侵襲バイパスを可能にする工夫を提示する。〔Hecker F, Salem R, von Zeppelin M, Hlavicka J et al. *Right-sided minimally invasive direct coronary artery bypass: Preoperative planning and surgical technique.* JTCVS Techniques. 2024;25:94-96.〕 [DOI](https://doi.org/10.1016/j.xjtc.2024.02.015)
- ★4 🖼️🔓 **両肺換気下のBITA MICS-CABG** — 両側内胸動脈を用いたMICS-CABGを、片肺換気を要さず両肺換気下で施行する手技を図示する。片肺換気に伴う呼吸器合併症リスクや麻酔管理上の制約を回避しつつ、小開胸からのBITA採取・術野露出を成立させる展開上の工夫を解説する。〔Assmann AK, Sixt SU, Lichtenberg A, Assmann A. *Technique of bilateral internal thoracic artery minimally invasive coronary artery bypass grafting with double-lung ventilation.* JTCVS Techniques. 2023;20:87-91.〕 [DOI](https://doi.org/10.1016/j.xjtc.2023.05.008)
- ★4 🖼️🔓 **超音波メスによる内胸動脈完全スケルトン化MICS-CABG** — 左小開胸MICS-CABGで超音波メスを用いて内胸動脈を完全スケルトン化採取する手技を247例の連続経験とともに示す。両側ITA使用108例、in situグラフト393吻合、完全動脈血行再建126例、大動脈ノータッチ142例で、平均吻合数2.6±1.1、胸骨切開への転換は全例なし、人工心肺移行3例（1.2%）と良好な成績を報告する。〔Tachibana K, Kikuchi K, Narayama K, Okawa A et al. *Minimally invasive coronary artery bypass grafting with ultrasonically skeletonized internal thoracic artery.* JTCVS Techniques. 2022;14:107-113.〕 [DOI](https://doi.org/10.1016/j.xjtc.2022.05.010)
- ★4 📹 **小開胸ロボット支援MIDCAB（LITA-LAD・段階指示）** — 小開胸からのロボット支援MIDCAB（LITA-LAD）の手順をstep-by-stepでビデオ解説する。家族性高コレステロール血症・LAD慢性完全閉塞の若年男性例を提示し、PCI不適の重症冠病変に対する低侵襲代替として、ハイブリッド冠血行再建戦略の一環で外科リスクを最小化し高い開存と長期成績を狙う点を示す（術後3日で退院）。〔*Robotic-assisted MIDCAB procedure through a minithoracotomy: step-by-step instructions.* Multimedia Manual of Cardio-Thoracic Surgery. 2022;2022.〕 [DOI](https://doi.org/10.1510/mmcts.2022.045)
- ★4 📄 **MINI OPCAB（部分胸骨切開LIMA-LAD）** — 胸骨を第3-4肋間まで部分的に開く小切開（MINI OPCAB）でLIMA-LAD吻合を行う手技を詳述する。LIMAは約8cm静脈を温存せず剥離し、胸骨付着部のキンク回避のため上方の角度を20度未満に保つこと、心膜を心尖部・右方へ開放してLAD吻合部位を同定、ヘパリン化後に5-0プロリーンでLAD遮断、機械的スタビライザー設置後に吻合・結紮するまでの手順を示す（70例中10例がハイブリッド）。〔Benetti F, Scialacomo N, Mazzolino G. *MINI OPCAB Operation: Surgical Technique.* Surgical Technology Online. 2021;38:290-293.〕 [DOI](https://doi.org/10.52198/21.sti.38.cv1400)
- ★4 📹 **MIDCAB成功のためのtips and tricks** — MIDCAB（LIMA-LAD）を成功させるための実践的なコツをビデオで詳説する。20年以上の単施設経験に基づき、術野展開・心臓安定化・吻合といった手技的要点を提示し、孤立性近位LAD病変や多枝病変、ハイブリッド血行再建戦略の構成要素として第一選択たり得ることを論じる。〔*MIDCAB: tips and tricks for a successful procedure.* The Multimedia Manual of Cardio-Thoracic Surgery. 2020;2020.〕 [DOI](https://doi.org/10.1510/mmcts.2020.021)
- ★4 📹 **ロボット支援MIDCAB（単枝・da Vinci Xi）** — 近位LAD有意狭窄を伴う安定狭心症例に対するロボット支援MIDCAB（単枝）の手技ビデオ。ダブルルーメンチューブによる片肺換気下、左第3肋間にカメラポート、第5・7肋間にポートを直視下追加し、da Vinci Xiで内胸動脈を半骨格化採取（胸郭筋膜を剥離しつつ伴走静脈は動脈と温存）、ヘパリン投与後に心膜を開放し左前小開胸からオフポンプでLITA-LAD吻合を完成させる一連を提示する。〔*Robotic-assisted minimally invasive direct coronary artery bypass grafting in single vessel disease.* The Multimedia Manual of Cardio-Thoracic Surgery. 2019;2019.〕 [DOI](https://doi.org/10.1510/mmcts.2019.011)
- ★4 📹 **LAST（左前小開胸）MIDCABの標準手技** — LAST（左前小開胸）によるMIDCABの手技をビデオで詳説する。左乳頭下・左胸骨縁外側3-4cm、第4肋間上に6cm切開を置き、ダブルルーメンチューブで左肺を虚脱させて胸膜腔へ進入、専用開創器で直視下にLITAを採取し、オフポンプ同様に拍動下でLAD吻合を行う。肺ヘルニア予防のため肋間を編糸で閉鎖し、ロピバカイン局所浸潤を併用するなど合併症対策まで示す。〔*Left anterior small thoracotomy for minimally invasive coronary artery bypass grafting.* Multimedia Manual of Cardio-Thoracic Surgery. 2015.〕 [DOI](https://doi.org/10.1093/mmcts/mmv022)
- ★4 📹 **直視下BITA採取の多枝MICS-CABG（Nambiar法）** — ロボットや胸腔鏡を用いず、約2インチの左小開胸から両側内胸動脈を直視下に採取する世界初の手技「Nambiar Technique」を提示する。LITA-RITA Y複合グラフトのみでオフポンプ完全血行再建を行い、心外膜スタビライザーを小開胸から挿入して吻合、フロースタディで開存確認する多枝MICS-CABGを150例で実施した経験に基づく。〔Nambiar P, Mittal C. *Minimally Invasive Coronary Bypass Using Internal Thoracic Arteries via a Left Minithoracotomy.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2013;8(6):420-426.〕 [DOI](https://doi.org/10.1177/155698451300800607)
- ★3 🖼️🔓 **損傷右内胸動脈のベイルアウト再建** — 低侵襲冠動脈バイパス術中に損傷した右内胸動脈をレスキュー的に再建するベイルアウト手技を提示する症例報告。狭い術野で導管が損傷した際に、新たな導管採取に頼らず損傷ITAを修復・温存して血行再建を完遂するための具体的な再建テクニックを示す。〔Moriuchi H, Orii M, Fujii T, Shimabukuro N et al. *Bailout reconstruction of injured right internal thoracic artery in minimally invasive coronary artery bypass grafting.* JTCVS Techniques. 2025;34:123-125.〕 [DOI](https://doi.org/10.1016/j.xjtc.2025.08.023)
- ★3 🖼️ **非ロボット胸腔鏡的LIMA採取の習熟曲線** — ロボットを用いず汎用の胸腔鏡（VATS）器具で左内胸動脈を胸腔鏡的に採取するEndo-CAB手技を解説し、その習熟曲線を80例で評価する。平均LIMA採取時間は58±19分（15-113分）、平均手術時間150±39分で、経験の蓄積に伴い採取・手術時間が有意に短縮（対数回帰）し、採取中のLIMA損傷はなかったことを示し、ロボットなしでも低侵襲冠動脈手術を普及させ得ることを論じる。〔Akca F, ter Woorst J. *Learning Curve of Thoracoscopic Nonrobotic Harvest of the Left Internal Mammary Artery in Minimally Invasive Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2023;18(3):262-265.〕 [DOI](https://doi.org/10.1177/15569845231178012)
- ★3 📄 **MICS-CABGの標準化と発展（単一術者700例）** — 単一術者によるMICS-CABG連続700例の経験から、左前側方小開胸でのLIMA採取・上行大動脈への中枢吻合・遠位冠動脈吻合という多枝血行再建の標準化手技の発展を示す。前期200例と後期500例の比較で、後期は3枝病変例とバイパス本数（2.3±0.8→2.7±1.0）が増加する一方、胸骨切開への転換が6%から0.6%へ有意に低下し、再現性ある標準アプローチへの収束を学習曲線とともに示す。〔Andrawes PA, Shariff MA, Nabagiez JP, Steward R et al. *Evolution of Minimally Invasive Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2018;13(2):81-90.〕 [DOI](https://doi.org/10.1177/155698451801300202)
- ★3 🖼️ **覚醒多枝OPCAB（正中・部分胸骨切開）** — 高位胸部硬膜外麻酔下に人工呼吸を用いない覚醒多枝OPCABを、正中（中等度=部分胸骨切開）アプローチで行う際の技術的留意点を55例で解説する。吻合中はスタビライザーと心尖吸引デバイス、吻合部遠位の血流を保つ冠動脈アクティブ灌流システムを用い、胸膜開放による気胸はNeoveilシートとドレーンで対処する。LITA/RITA/胃大網動脈/橈骨動脈/伏在静脈を組み合わせ、平均手術時間177±35分・手術死亡ゼロを報告する。〔Watanabe G, Ohtake H, Tomita S, Yamaguchi S et al. *Multivessel Awake Off-Pump Coronary Bypass Grafting Using Median Approach: Technical Considerations.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2011;6(1):23-27.〕 [DOI](https://doi.org/10.1177/155698451100600105)
- ★3 🖼️ **再手術血行再建の一次戦略としてのMIDCAB** — 再開心術での冠血行再建の一次戦略として胸骨温存MIDCABを用いる手技アプローチを示す。技術的に可能な症例で胸骨再開創・開存グラフト損傷・病変グラフトからの塞栓・人工心肺の弊害を回避でき、ニューヨーク州心臓外科報告システムの再手術MIDCAB 369例と初回MIDCAB 822例（1996-2006）の比較で、再手術群は脳卒中・末梢/脳血管疾患・高度大動脈石灰化・腎不全・低EFといった高リスク背景を持つにもかかわらず、院内成績と在院日数に差がなかったことを報告する。〔Balacumaraswami L, Patel NC, Gorki H, Jennings J et al. *Minimally Invasive Direct Coronary Artery Bypass as a Primary Strategy for Reoperative Myocardial Revascularization.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2010;5(1):22-27.〕 [DOI](https://doi.org/10.1177/155698451000500106)
- ★3 📄 **MIDCABと胸腔鏡的肺静脈隔離の併施** — 胸骨切開を回避し、心房細動を合併する冠動脈疾患に対しMIDCABと胸腔鏡的（ビデオ補助下）両側肺静脈隔離を併施する低侵襲手技の症例報告。左第4肋間の左前側方開胸からLITAを直視下採取し、両極性高周波クランプで左肺静脈を電気的に隔離した後にLITA-LAD吻合、続いて右第4肋間小開胸から同様に右肺静脈を隔離し、左房天蓋に連結ラインを作成する。〔Totsugawa T, Kuinose M, Nishigawa K, Yoshitaka H et al. *Minimally invasive cardiac surgery for atrial fibrillation complicated by coronary artery disease: combination of video-assisted pulmonary vein isolation and minimally invasive direct coronary artery bypass.* General Thoracic and Cardiovascular Surgery. 2009;57(11):612-615.〕 [DOI](https://doi.org/10.1007/s11748-009-0441-1)

**📌 この領域の必読:** 左前小開胸MICS-CABGの確立と進化（🖼️図譜・オープンアクセスの体系的リファレンス）と、no-touch aorta完全動脈MICS-CABG（LITA-RA Y）（📹ビデオによるMICS-CABG術式の代表的解説）がまず外せない。手技習得には、ロボット支援MIDCAB（採取〜吻合の段階解説）や LAST（左前小開胸）MIDCABの標準手技、MIDCAB成功のためのtips and tricks といった📹ビデオチュートリアル群が実践的に有用である。

### ロボット支援・全内視鏡下（TECAB）

ロボット支援冠動脈バイパスは、ロボットでLIMA/BIMAを採取し小開胸下で吻合するR-MIDCABから、胸壁を開けず内視鏡下で全工程を完結する全内視鏡下CABG（TECAB）まで幅広く、低侵襲性と動脈グラフトによる完全血行再建の両立を目指す領域である。OPCABの文脈では、人工心肺を用いずに拍動心（beating-heart）で内視鏡的に遠位吻合を完遂する技術が核心となり、ポート（トロッカー）配置、冠動脈の安定化、標的同定、in-situ動脈グラフトの設計が成否を分ける。収集した論文群は、R-MIDCABの段階的標準化手技、手縫いTECABの「how I do it」、BIMA採取のダブルドッキング法、EndoWristスタビライザを使わない安定化の工夫、ICG蛍光による標的・グラフト評価、redo・多枝・弁同時手術への応用までを網羅し、本領域の発展史と現行の実践を体系的に提示している。

- ★5 🖼️🔓 **R-MIDCABの段階的標準化手技** — Lankenau Heart Instituteが2005年以降に2,850例超で洗練させたR-MIDCABの段階的プロトコルを詳述。ロボットでLIMAを採取し標的LADの直上に内視鏡ポートを精密配置、ロボット器具を抜去後にそのポート部位を小開胸（minithoracotomy）へ拡大してbeating-heartでLIMA-LAD吻合を行う。他2本のロボットポートはドレーン留置に転用し追加切開を不要とする工夫を示す。〔Wertan MC, Sicouri S, Yamashita Y, Baudo M, Senss TA, Spragan D, Torregrossa G, Sutter FP.. *Step-by-step technique of robotic-assisted minimally invasive direct coronary artery bypass.* Annals of Cardiothoracic Surgery. 2024;13(5):442-451.〕 [DOI](https://doi.org/10.21037/acs-2024-rcabg-0034)

- ★5 🖼️🔓 **完全ロボット手縫いCABG（how we do it）** — 完全ロボット支援・縫合（hand-sewn）吻合によるTECABの実践を「how we do it」形式で段階的に解説。患者準備・露出・グラフト採取から内視鏡下の縫合吻合までの一連の手順を要点化し、自動吻合器に頼らない手縫いTECABの再現性を示す。〔Torregrossa G, Amabile A, Balkhy HH. *Totally robotic sutured coronary artery bypass grafting: How we do it.* JTCVS Techniques. 2020;3:170-172.〕 [DOI](https://doi.org/10.1016/j.xjtc.2020.05.018)

- ★5 📹 **in-situ BIMAによるoff-pump手縫いTECAB** — in-situ両側内胸動脈（BIMA）を用いたロボットoff-pump完全内視鏡下手縫いCABGの手技をビデオで詳説。十分に記載されてこなかったTECABの「tips and tricks」を提示し、TECABプログラムを新規に立ち上げる術者向けの技術的考慮点を整理する。〔*Robotic off-pump totally endoscopic hand-sewn coronary artery bypass using in-situ bilateral internal mammary artery.* The Multimedia Manual of Cardio-Thoracic Surgery. 2020;2020.〕 [DOI](https://doi.org/10.1510/mmcts.2020.001)

- ★4 🖼️🔓 **多枝TECAB＋僧帽弁形成の同時手技** — ロボット支援完全内視鏡下の多枝冠動脈バイパスと僧帽弁形成術を一括で施行する複合手技を提示。TECABと弁手術を単一の内視鏡的アプローチで同時完遂できることを症例で示し、低侵襲での複合心臓手術の可能性を示唆する。〔Arai A, Kitahara H, Balkhy HH.. *Combined robotic totally endoscopic multivessel coronary artery bypass and mitral valve repair.* JTCVS Techniques. 2026;35:102169.〕 [DOI](https://doi.org/10.1016/j.xjtc.2025.102169)

- ★4 🖼️ **EndoWristスタビライザ不要の拍動心安定化** — ロボット完全内視鏡下のbeating-heart off-pump CABGにおいて、EndoWristスタビライザを使用せずに冠動脈を安定化する工夫的手技を解説。専用安定化器具に依存しない代替的固定法により、拍動下での内視鏡吻合を可能にするコツを示す。〔Murtaza G, Cheema NH, Enz J, Balkhy HH. *Robotic Totally Endoscopic Beating Heart Off-Pump Coronary Bypass: Improvising Coronary Artery Stabilization Without the EndoWrist Stabilizer.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2025;20(3):316-317.〕 [DOI](https://doi.org/10.1177/15569845251339158)

- ★4 🖼️🔓 **ロボットCABGのトロッカー配置流派** — ロボットbeating-heart CABGにおけるトロッカー（ポート）配置の各流派・スタイルを比較解説。標的冠動脈や術式に応じたポート設置の考え方を整理し、術中操作性と展開を左右する初期セットアップの要点を示す。〔Algoet M, Balkhy HH, Dewulf D, Oosterlinck W. *Different styles in trocar placement in robotic-assisted beating heart coronary artery bypass grafting.* Annals of Cardiothoracic Surgery. 2024;13(5):458-460.〕 [DOI](https://doi.org/10.21037/acs-2023-rcabg-0209)

- ★4 🖼️🔓 **GelPOINT Mini＋AirSeal＋Octopus NuvoによるTECAB** — EndoWristスタビライザを用いず、GelPOINT Mini・AirSeal・Octopus Nuvoの3デバイスを組み合わせてDaVinci Xiで行うTECABの技術的工夫を提示。市販の体腔アクセス・気腹・安定化デバイスを統合することで、専用スタビライザに頼らない拍動心吻合環境を構築する。〔Torregrossa G, Yakobitis A, Murray C, Baudo M. *Total endoscopic coronary artery bypass on a DaVinci Xi platform without an EndoWrist stabilizer combining the technology of GelPOINT Mini, AirSeal, and Octopus Nuvo.* Annals of Cardiothoracic Surgery. 2024;13(5):461-463.〕 [DOI](https://doi.org/10.21037/acs-2024-rcabg-0112)

- ★4 📹 **左前胸開胸からの多枝ロボットCABG** — 左前胸開胸（left anterior thoracotomy）からのロボット支援多枝冠動脈バイパスによる完全血行再建手技をビデオで詳説。術前CTで標的冠動脈を同定し、それをガイドにポート配置と複数枝吻合を行う再現性ある手順を示し、良好な成績が得られることを述べる。〔*Robotic-assisted minimally invasive multivessel coronary bypass surgery.* Multimedia Manual of Cardio-Thoracic Surgery. 2024;2024.〕 [DOI](https://doi.org/10.1510/mmcts.2023.105)

- ★4 📹 **既往CABG例へのredo TECAB（RITA-RCA）** — 既往CABG・既往開腹手術を有する患者に対し、ロボット完全内視鏡下で右内胸動脈（RITA）を右冠動脈へ再バイパスするredo TECAB手技をビデオで提示。再胸骨切開や、開存グラフト損傷を避けるための剣状突起下RGEAアプローチが適さない症例における代替手技として位置づける。〔*Robotic redo totally endoscopic coronary artery bypass to the right coronary artery in a patient with prior coronary bypass surgery.* Multimedia Manual of Cardio-Thoracic Surgery. 2023.〕 [DOI](https://doi.org/10.1510/mmcts.2023.012)

- ★4 🖼️ **動脈Y-graftによるLAD/RCA系TECAB** — ロボット支援完全内視鏡下CABGにおいて動脈Y-graft（複合動脈グラフト）を用いてLADおよび右冠動脈系を血行再建する手技を提示。in-situ動脈とY吻合を組み合わせることで、限られた内視鏡視野でも多枝の動脈血行再建を実現する設計を示す。〔Bonatti J, Göbölös L, Ramahi J, Bartel T. *Robotic totally endoscopic coronary artery bypass grafting (TECAB) of the left anterior descending and right coronary artery system using an arterial Y-graft technique.* Annals of Cardiothoracic Surgery. 2018;7(5):700-703.〕 [DOI](https://doi.org/10.21037/acs.2018.06.10)

- ★4 🖼️ **拍動心ロボットTECAB** — 心拍動下（off-pump/beating-heart）でのロボット完全内視鏡下CABGの手技を提示。人工心肺を用いずに内視鏡下で吻合を完遂するためのビーティングハート操作と安定化のポイントを解説する。〔Melly L, Douglas D, Jansens J. *Robotic beating-heart totally endoscopic coronary artery bypass.* Annals of Cardiothoracic Surgery. 2018;7(5):707-709.〕 [DOI](https://doi.org/10.21037/acs.2018.06.13)

- ★4 📄 **ダブルドッキング法によるロボットBIMA採取** — da Vinciを患者左側から右側へ再ドッキングする「ダブルドッキング」法により両側内胸動脈を採取する新規ロボット手技。12例で右IMAを左側設置、再配置に平均6.5±0.6分を要して左側へ転位し左IMAを採取、遠位吻合は小前側方開胸で行い、胸骨切開への移行なくBIMA採取を完遂したと報告する。〔Tarui T, Ishikawa N, Watanabe G. *A Novel Robotic Bilateral Internal Mammary Artery Harvest Using Double Docking Technique for Coronary Artery Bypass Grafting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2017;12(1):74-76.〕 [DOI](https://doi.org/10.1177/155698451701200115)

- ★4 🖼️ **BIMAを左室系へ留置するTECAB** — ロボット完全内視鏡下CABGで両側内胸動脈を左室（左前下行枝系）へ留置する手技を提示。動脈グラフトのみを用いた完全内視鏡的血行再建の手順を示す。〔Bonatti J, Vento A, Bonaros N, Traina M et al. *Robotic totally endoscopic coronary artery bypass grafting (TECAB)—placement of bilateral internal mammary arteries to the left ventricle.* Annals of Cardiothoracic Surgery. 2016;5(6):589-592.〕 [DOI](https://doi.org/10.21037/acs.2016.11.05)

- ★4 📹 **第二世代ロボットによる拍動心TECAB** — beating-heartでのロボット完全内視鏡下冠動脈バイパスの手技をビデオで解説。2007年以降の第二世代ロボット機器によって多くの技術的課題が解決され、より安全・確実・再現性のあるoff-pumpの内視鏡吻合が可能になったと述べ、低侵襲化と回復短縮の利点を強調する。〔Jansens J. *Beating heart totally endoscopic coronary artery bypass.* Multimedia Manual of Cardio-Thoracic Surgery. 2011;2011(0914).〕 [DOI](https://doi.org/10.1510/mmcts.2010.004663)

- ★4 🖼️ **ロボットCABGの図解アトラス** — ロボット支援冠動脈バイパス手技を図解で体系的に解説するoperative techniques論文。ロボットによる内胸動脈採取から吻合までの操作を図示し、TECABを含むロボットCABGの基本手技を概観する。〔Liao KK. *Robotic Coronary Artery Bypass Grafting.* Operative Techniques in Thoracic and Cardiovascular Surgery. 2010;15(3):194-205.〕 [DOI](https://doi.org/10.1053/j.optechstcvs.2010.08.002)

- ★4 🖼️ **U-clip吻合による拍動心TECABの経験と展望** — 拍動心ロボット支援TECABを、ポート挿入・エンドスタビライザー使用・単/両側内胸動脈グラフト・U-clip吻合で施行した93例の経験報告。院内死亡・心筋梗塞・脳卒中ゼロ、平均吻合時間13.8±3.7分、平均在院3.4±2.0日で、約19%は計画的ハイブリッド血行再建を併施したと報告し本術式の将来性を論じる。〔Srivastava S, Gadasalli S, Agusala M, Kolluru R et al. *Robotically Assisted Beating Heart Totally Endoscopic Coronary Artery Bypass (TECAB): Is There a Future?.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2008;3(2):52-58.〕 [DOI](https://doi.org/10.1177/155698450800300202)

- ★4 🖼️ **コンピュータ支援TECABの黎明期手技** — コンピュータ支援・ロボットによる完全内視鏡下冠動脈バイパスの手技を解説する初期の図解論文。内視鏡的なグラフト採取と吻合の手順を示し、TECABの基礎となる手技概念を提示する。〔WOLF R. *Computer-assisted or robotic totally endoscopic coronary artery bypass grafting.* Operative Techniques in Thoracic and Cardiovascular Surgery. 2001;6(3):177-188.〕 [DOI](https://doi.org/10.1016/s1522-2942(01)80029-5)

- ★3 🖼️🔓 **2本目動脈グラフトのためのスタビライザ不要安定化** — ロボットTECABで2本目の動脈グラフトを吻合する際に、EndoWristスタビライザを用いずに冠動脈を安定化する手技を示すブリーフレポート。専用スタビライザなしでも複数枝の拍動心吻合を可能にする実践的な工夫を提示する。〔Murtaza G, Zellner K, Wachowiak R, Corbit J et al. *Robotic Totally Endoscopic Coronary Artery Bypass: Coronary Artery Stabilization Without the EndoWrist Stabilizer for a Second Arterial Graft.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2025;20(6):594-595.〕 [DOI](https://doi.org/10.1177/15569845251388992)

- ★3 📄🔓 **ICG蛍光による壁内冠動脈の同定** — ロボット冠動脈バイパス中にインドシアニングリーン（ICG）蛍光イメージングを用いて、心筋内に埋没した壁内冠動脈を正確に同定する術中手技ノート。触覚フィードバックを欠くロボット環境で標的を視覚的に同定する工夫として有用性を示す。〔Khalpey Z, Kumar U, Khalpey Z, Phillips T et al. *Indocyanine green fluorescence imaging for accurate detection of an intramural coronary artery during robotic coronary artery bypass grafting.* JTCVS Techniques. 2025;30:94-97.〕 [DOI](https://doi.org/10.1016/j.xjtc.2025.01.018)

- ★3 🖼️🔓 **LAD心筋ブリッジのロボットunroofing** — LAD心筋ブリッジに対するロボット完全内視鏡下beating-heart unroofing（除圧・脱屋根化）手技を提示。バイパスを行わずTECABプラットフォーム上で拍動下に心筋ブリッジを解除する応用術式を実演する。〔Nisivaco S, Kitahara H, Balkhy HH. *Robotic totally endoscopic beating-heart unroofing of a left anterior descending artery myocardial bridge.* Annals of Cardiothoracic Surgery. 2024;13(4):385-387.〕 [DOI](https://doi.org/10.21037/acs-2023-rcabg-0193)

- ★3 🖼️ **Firefly蛍光によるLITA採取・グラフト評価** — R-MIDCABにおいてICG蛍光イメージング（Firefly）を用いてLITAの位置同定、採取後の血流評価、吻合後のグラフト血流評価を行うデバイス活用手技。触覚のないda Vinci Xiでの採取時LITA損傷リスクを補う目的で、30例中28例で良好な血流を視認、各評価は約20秒で副作用なく施行できたと報告する。〔Nakamura Y, Kuroda M, Ito Y, Masuda T et al. *Left Internal Thoracic Artery Graft Assessment by Firefly Fluorescence Imaging for Robot-Assisted Minimally Invasive Direct Coronary Artery Bypass.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2019;14(2):144-150.〕 [DOI](https://doi.org/10.1177/1556984519836810)

- ★3 🖼️ **新規3D内視鏡による拍動心TECAB** — 新規3D内視鏡システムを用いた拍動下完全内視鏡的CABGの手技。後腋窩線第4肋間から15mmポートで3D内視鏡を挿入しLITAをsemi-skeletonizedに内視鏡採取、独自の吸引スタビライザーでLADを固定し、8-0 Proleneの連続縫合で端側吻合を行う手順を示し、LITA採取時間の短縮を報告する。〔Tomita S, Watanabe G, Tabata S, Nishida S. *Total Endoscopic Beating-Heart Coronary Artery Bypass Grafting Using a New 3D Imaging System.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2006;1(5):243-246.〕 [DOI](https://doi.org/10.1177/155698450600100504)

- ★3 📄 **回旋枝系の新たな展開手技** — ロボット完全内視鏡下CABGにおける回旋枝系の新たな展開（exposure）手技を示す症例報告。左主幹孤立性狭窄の症例で、da VinciでRIMA-LAD吻合を心停止下に行い、Octopus-TE固定器で鈍縁枝（OM1）を展開してLIMAを吻合する方法を提示し、多枝TECABの発展に資すると述べる。〔Bonatti J, Schachner T, Bonaros N, Laufer G. *A new exposure technique for the circumflex coronary artery system in robotic totally endoscopic coronary artery bypass grafting.* Interactive CardioVascular and Thoracic Surgery. 2006;5(3):279-281.〕 [DOI](https://doi.org/10.1510/icvts.2005.123125)

- ★2 🖼️ **完全内視鏡下冠動脈瘤修復** — 完全内視鏡下での冠動脈瘤修復手技を示すケースレポート。内視鏡下冠動脈手術の手技を冠動脈瘤という非典型病変の修復へ応用した例を提示する。〔Kato R, Hosoba S, Ito T. *Totally Endoscopic Coronary Artery Aneurysm Repair.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2024;19(2):121-121.〕 [DOI](https://doi.org/10.1177/15569845241237803)

**📌 この領域の必読:** まず「R-MIDCABの段階的標準化手技」（🖼️、2,850例に基づく決定版アトラス）と「完全ロボット手縫いCABG（how we do it）」（🖼️）で術式の全体像を押さえ、実際の運針・拍動心操作は「in-situ BIMAによるoff-pump手縫いTECAB」（📹）と「左前胸開胸からの多枝ロボットCABG」（📹）のビデオチュートリアルで補完するとよい。

### ハイブリッド冠動脈血行再建

ハイブリッド冠動脈血行再建は、最も長期開存が期待できるLITA-LADバイパスを低侵襲・胸骨非切開アプローチ（MIDCAB/ロボットTECAB）で確実に行い、残る非LAD病変はPCI/薬剤溶出ステントで補完する戦略であり、OPCABの低侵襲化の到達点の一つである。本テーマで収集した論文は、ロボット支援の全内視鏡的アプローチや両側ITA使用、PCIと外科手技を同一手術室で同時に行うsimultaneous戦略、さらにTAVIとMIDCABの併施など、ハイブリッド手技の具体的な術式・手順とその工夫を扱っている。多枝病変や高リスク併存疾患症例における低侵襲血行再建の実際を示す内容である。

- ★4 🖼️🔓 **ロボット両側ITA + PCIによるadvanced hybrid血行再建** — ロボット支援の全内視鏡的CABG（TECAB）で両側内胸動脈グラフトを用い、非LAD病変には術前または術後に薬剤溶出ステントを留置するadvanced hybrid戦略を、8.5年・664例のTECAB経験から提示。ハイブリッド適応の293例のうち両側ITAを使用した156例を対象とし、94%が三枝病変、17%が左主幹70%以上というハイリスク群でもSTS予測死亡率1.26%と良好で、胸骨温存下の多枝低侵襲血行再建の実装と中期成績（最長8年）を示す。〔Balkhy HH, Nisivaco S, Kitahara H, AbuTaleb A et al. *Robotic advanced hybrid coronary revascularization: Outcomes with two internal thoracic artery grafts and stents.* JTCVS Techniques. 2022;16:76-88.〕 [DOI](https://doi.org/10.1016/j.xjtc.2022.08.012)

- ★4 🖼️ **ロボットハイブリッドCABGの実践手技（how do we do it）** — ロボット支援によるハイブリッド冠動脈血行再建（robotic MIDCAB/TECAB + PCI）の具体的手技を解説するACSの「how do we do it」形式の手技論文。LITA-LADを低侵襲・胸骨非切開で行い、残存病変をPCIで補完するワークフローと術式のコツを図示する。〔Torregrossa G, Kanei Y, Puskas J. *Hybrid robotic coronary artery bypass grafting: how do we do it.* Annals of Cardiothoracic Surgery. 2016;5(6):582-585.〕 [DOI](https://doi.org/10.21037/acs.2016.11.06)

- ★3 🖼️ **同一手術室でのTECABとPCI同時施行** — da Vinciロボットを用い4ポートから拍動下にLITA-LAD完全内視鏡的バイパス（TECAB）を行い、その直後に同一手術室内でC-arm下にRCAへの経皮的PCI（ステント留置）を施行する計画的simultaneousハイブリッドの初例報告。糖尿病合併の二枝病変例で、両手技合計165分・閉塞14分/吻合8分・PCI10分/透視3分という時間配分を提示し、術直後からクロピドグレル+アスピリンを開始する管理を示す。〔Srivastava S, Gadasalli S, Tijerina O, Barrera R et al. *Planned Simultaneous Beating-Heart Totally Endoscopic Coronary Artery Bypass (TECAB) and Percutaneous Intervention in a Single Operative Setting.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2006;1(5):239-242.〕 [DOI](https://doi.org/10.1177/155698450600100503)

- ★2 🖼️ **経心尖TAVIとMIDCABの同時オフポンプ手技** — 重症大動脈弁狭窄と重篤な冠動脈病変を併せ持つ高リスク女性に対し、ハイブリッド手術室で経心尖TAVIとMIDCABを同時に行ったオフポンプ低侵襲手技の症例報告。TAVI施行中の冠血流を維持するため、先に冠動脈バイパスを完成させてから経心尖弁植込みを行う手順が要点で、合併症なく第7病日に退院した。〔Baumbach H, Adili S, Ursulescu A, Franke UFW. *Concomitant Transapical Transcatheter Aortic Valve Implantation and Minimally Invasive Direct Coronary Artery Bypass.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2011;6(6):389-390.〕 [DOI](https://doi.org/10.1177/155698451100600609)

**📌 この領域の必読:** 「ロボット両側ITA + PCIによるadvanced hybrid血行再建」（🖼️、8.5年の大規模シリーズで多枝病変への胸骨温存戦略を体系化）と「ロボットハイブリッドCABGの実践手技（how do we do it）」（🖼️、ワークフローと吻合のコツを図示した手技アトラス）。いずれも図中心の手技解説で、本テーマには動画チュートリアル（📹）は含まれない。

### 特殊症例・再手術・高リスク

通常の正中切開・人工心肺下CABGが適さない高リスク病態（porcelain aorta、左室機能低下、胸骨創感染ハイリスク、他臓器同時手術を要する併存疾患）では、無心停止・無遮断のOPCABがもたらす大動脈操作回避・心筋保護温存・低侵襲性が決定的な利点となる。本テーマの収録論文は、片肺移植やアオルトバイフェモラルバイパスとの同時手術、慢性気管切開孔症例での胸骨温存MICS-CABG、低EF例での拍動下僧帽弁手術併施といった、いずれもOPCABを「逃げ道」として活用した特殊症例の手技を扱う。デバイス選択よりも、いかに大動脈・胸骨・心筋への侵襲を避けつつ完全血行再建を成立させるかという術式設計のコツが中心となる。

- ★3 🖼️🔓 **片肺移植同時のin situ RITA OPCAB（開胸アプローチ）** — 片肺移植と同時に、胸骨正中切開ではなく開胸アプローチを用い、in situの右内胸動脈（RITA）をグラフトとしたオフポンプCABGを施行した特殊症例。人工心肺・大動脈遮断を回避しつつ、移植側の開胸創を活用してRITAを温存・吻合する手技が図示されており、肺移植と冠動脈血行再建を一期的に両立させる工夫を示す。〔Toyoda Y, Kehara H, Kashem M, Leotta E et al. *Right single lung transplant with off-pump coronary artery bypass grafting using in situ right internal thoracic artery via thoracotomy.* JTCVS Techniques. 2023;19:157-159.〕 [DOI](https://doi.org/10.1016/j.xjtc.2023.02.011)

- ★3 🖼️ **OPCAB＋上行大動脈起始アオルトバイフェモラルバイパス同時手術** — 冠動脈疾患にしばしば併存する大動脈腸骨動脈閉塞性疾患に対し、OPCABと同時に上行大動脈を起始部とする腹側経路（ventral abdominal route）のアオルトバイフェモラルバイパスを一期的に施行した2例。別々の2回介入を避け、技術的に簡便な下肢バイパスをオフポンプ心臓手術と組み合わせることで、追加の合併症を増やさず心筋と両下肢を同時に血行再建できる手順と利点を解説する。〔Rajendran S, Prabhu AD, Thazhakuni I, Vellachamy KA et al. *Simultaneous Off-Pump Coronary Artery Bypass Grafting and Ascending Aortobifemoral Bypass Graft via Ventral Abdominal Route.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2007;2(2):84-85.〕 [DOI](https://doi.org/10.1177/155698450700200207)

- ★2 🖼️🔓 **慢性気管切開孔症例での胸骨温存MICS-CABG** — 慢性気管切開孔を有し胸骨創感染（SWI）リスクが著しく高い、frailで多併存疾患かつPCI不適の多枝病変症例に対し、胸骨正中切開を回避する低侵襲CABG（MICS-CABG）を適用した症例報告。胸骨を温存することでSWIや胸骨切開後の機能低下リスクを軽減しつつ完全血行再建を達成する代替戦略として、本術式の適応と手技を提示する。〔Nantsios A, Elmistekawy E, Ponnambalam M, Lambert AS et al. *Minimally Invasive Coronary Artery Bypass Grafting in a Patient With Chronic Tracheostoma: Alternative to Reduce Sternal Wound Complication Risk.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2022;17(6):574-576.〕 [DOI](https://doi.org/10.1177/15569845221137898)

- ★2 🖼️ **低EF例での拍動下僧帽弁手術＋OPCAB併施** — 平均EF 41±4.5%の左室機能低下例25例（うち急性心筋梗塞7例）に対し、大動脈遮断を行わず拍動下に僧帽弁形成・置換とCABGを併施した手技。CABGは人工心肺非使用で行い、僧帽弁手術中は灌流圧80-90mmHg・体温35-36℃を維持して心筋保護を図る。平均2.12±0.9枝のグラフトを施行し、術後EFは保持されたが、死亡率12%（3/25）・合併症率52%と高リスク病態を反映した成績を報告する。〔Di Luozzo G, Lombardi P, Maldonado A, Ricci M et al. *Concomitant Beating-Heart Mitral Valve Surgery and Coronary Artery Bypass in Patients with Compromised Ventricular Function.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2006;1(4):151-154.〕 [DOI](https://doi.org/10.1177/155698450600100404)

**📌 この領域の必読:** 図解の充実した手技アトラスとして、片肺移植と同時に行う「片肺移植同時のin situ RITA OPCAB（開胸アプローチ）」（🖼️、open access）と、胸骨温存戦略を示す「慢性気管切開孔症例での胸骨温存MICS-CABG」（🖼️、open access）がまず参照すべき2編。低EF併施手術の実務指標としては「低EF例での拍動下僧帽弁手術＋OPCAB併施」が灌流圧・体温管理の具体値とともに有用。なお本サブトピックには動画チュートリアル（📹）は含まれない。

### オンポンプ転換・安全性

OPCABにおけるオンポンプ転換は、血行動態破綻・致死的不整脈・心筋虚血・操作困難な吻合部位といった術中トラブルに対する重要なbailout手段であり、その判断遅れは予後を悪化させるため、転換理由の理解と緊急対応のための準備は安全な完全OPCAB施行の前提となる。本稿で収集した文献は、ルーチンOPCABにおける転換の発生要因とその回避・対処に関わる手技上のポイントを扱う。

- ★3 📄 **ルーチンOPCABのオンポンプ転換理由** — ルーチンに完全OPCABを志向する施設での経験から、術中にオンポンプへ転換せざるを得なかった症例の理由を後方視的に分析した安全性報告。血行動態の不安定化や標的血管・吻合操作上の問題など転換に至る要因を整理し、これらを予測・回避するための手技的配慮と、転換が必要となった際の対応の要点を論じている。完全OPCABを安全に遂行するうえでの転換リスクの認識に資する内容である。 〔Hirose H, Amano A. *Routine Off-Pump Coronary Artery Bypass: Reasons for On-Pump Conversion.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2005;1(1):28-31.〕 [DOI](https://doi.org/10.1177/155698450500100103)

**📌 この領域の必読:** 「ルーチンOPCABのオンポンプ転換理由」（Hirose & Amano, 標準論文📄）が本サブトピックで収集された唯一かつ中心的な文献であり、転換の発生要因を把握するうえで参照すべき。

### トレーニング・教育・シミュレーション

OPCAB・ロボット/MICS CABGでは拍動心下・狭い術野・限られた可視性のなかで安定した冠動脈吻合とin-situ動脈グラフト採取を再現性高く実施する必要があり、体系的な教育とシミュレーション環境が習得の鍵となる。本テーマの論文群は、ロボット支援CABG（R-MIDCAB／TECAB）の「how I teach it」型教育法、拍動心ボックスや自作低忠実度シミュレータ・ドライラボによる吻合自己練習、3D-VRを用いた術前グラフト設計シミュレーション、そしてHarmonic scalpelによる内胸動脈採取の安全なトレーニング法までを横断的にカバーする。いずれも段階的（incremental）学習・チーム体制・客観的スキル評価を共通の柱とし、低侵襲冠動脈再建への移行過程を技術的に支える内容である。

- ★4 🖼️🔓 **ロボット支援CABGのhow I teach it（R-MIDCAB教育プログラム）** — R-MIDCABを構成要素ごとに分解し、ロボットセットアップ・IMA採取・前側方小開胸からの冠動脈吻合を段階的に教える教育記事。術者個人だけでなく専従心臓チームと施設管理の支援を含む「チームアプローチ」を強調し、綿密な計画・漸進的学習・チームワークをプログラム成功の中心要因に挙げる。術中合併症のトラブルシューティングにも触れ、術後心房細動・輸血・脳卒中・ICU/在院日数の減少といった低侵襲化の利点とハイブリッド再建を含む長期成績の良好さを示す。〔Sutter FP, Wertan MC, Spragan D, Yamashita Y et al. *Robotic-assisted coronary artery bypass grafting: how I teach it.* Annals of Cardiothoracic Surgery. 2024;13(4):346-353.〕 [DOI](https://doi.org/10.21037/acs-2024-rcabg-0033)

- ★3 🖼️ **ロボット拍動下TECAB訓練用の新規シミュレータ** — ロボット拍動下TECAB（totally endoscopic CABG）の訓練を目的に開発された新規シミュレータを紹介する短報で、心拍動環境を再現した冠動脈吻合トレーニングを可能にする。拍動下・完全内視鏡という最も難度の高い再建を、患者外で安全に反復練習する環境を提示する点に意義がある。〔AlJamal YN, Crestanello J, Dearani J, Balkhy HH. *The Future of Coronary Bypass? A Novel Simulator for Robotic Beating-Heart TECAB Training.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2026;21(1):94-95.〕 [DOI](https://doi.org/10.1177/15569845251408006)

- ★3 🖼️ **自作低忠実度拍動心シミュレータによる吻合自己練習プログラム** — モーター駆動の玩具ブロックをスマートフォンアプリと無線連携させ拍動レート可変とした自作の低忠実度拍動心シミュレータを構築し、中級研修医に8週間の構造化自己練習プログラム（非拍動→拍動の2部構成、各部で客観的スキル評価）を課したproof of concept。プログラム終了時にはOPCAB（489対605秒）・MICS設定での吻合時間とスコアが指導医（junior consultant）に近づき、練習回数と吻合時間に逆相関を認めた。安価な機材で拍動下吻合を反復習得できる自己練習法を示す。〔Azmi MI, Nair AK, Hashim SA. *Self-Practice Program for Beating-Heart Minimally Invasive Coronary Anastomosis Using a Homemade Low-Fidelity Simulator: A Proof of Concept.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2024;19(2):175-183.〕 [DOI](https://doi.org/10.1177/15569845241238999)

- ★3 🖼️ **Harmonic scalpelによる内胸動脈採取の安全なトレーニング法** — 胸骨正中切開を介してHarmonic scalpelで内胸動脈（ITA）を採取する安全なトレーニング手技を解説した短報。正中切開という安定した視野・操作環境のもとで超音波凝固切開装置を用いたITA採取手技を習得させ、MICS CABGへの円滑な移行を図る段階的教育アプローチを示す。〔Kikuchi K, Yoshino K, Sakai H, Sai Y et al. *Safe Training Method for ITA Harvesting via Median Sternotomy in Minimally Invasive Coronary Artery Bypass Surgery Using Harmonic Scalpel.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2024;20(1):111-113.〕 [DOI](https://doi.org/10.1177/15569845241290240)

- ★3 🖼️ **3D-VRによるaortic no-touch total arterial MICS-CABGの術前シミュレーション** — 320列CTのstereolithographicファイルをワークステーションで変換し、没入型VRプラットフォーム上でin-situ動脈グラフト（LITA／RITA／胃大網動脈）の採取必要長と走行を術前にシミュレーションする手技。VRによる予測採取長は各グラフトで約21cm前後、所要長は14.5〜16.4cmと算出され、17例中16例でaortic no-touch total arterial MICS-CABGを完遂、3D解剖評価により11.8%で術戦略を修正した。グラフト設計を術前に最適化する計画シミュレーションの実用性を示す。〔Tachibana K, Kikuchi K, Sugimoto M, Osuda K et al. *Virtual Reality Simulation for Minimally Invasive Coronary Artery Bypass Grafting With Aortic No-Touch Total Arterial Grafting Technique.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2022;17(5):430-437.〕 [DOI](https://doi.org/10.1177/15569845221129212)

- ★3 🖼️ **拍動心モデルによる非ロボット完全内視鏡下吻合の訓練・評価** — 機械駆動のブタ心臓を内蔵した手製胸郭モデルで、市販内視鏡器具と2D内視鏡視野のみを用い、Prolene 7-0縫合またはU-clipでそれぞれ20吻合ずつ計40の静脈—冠動脈吻合を実施した訓練研究。吻合時間はProlene 51±14分・U-clip 48±10分で、流量測定・ICG造影・vinylpolysiloxane鋳型・内皮面評価による品質管理で吻合漏れと所要時間の減少という学習曲線を確認した。非ロボットTECABが技術的に過度に困難という通説に反論し、再現性ある手順を文書化した点に意義がある。〔Gorki H, Patel NC, Liewald C, Wildhirt S et al. *A Step toward Nonrobotic Total Endoscopic Coronary Bypass Grafting: 40 Coronary Anastomoses in a Biomechanical Beating Heart Model.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2012;7(5):359-367.〕 [DOI](https://doi.org/10.1177/155698451200700509)

- ★3 📄 **非ロボット拍動心内視鏡下吻合の4段階ドライラボ訓練システム** — 市販機材のみで構築したオリジナルのドライラボ訓練システムで、拍動可能なボックス装置の上面に2Dビデオカメラとモニターを設置し、多孔プレート越しに内視鏡器具を挿入して連続縫合で人工血管を吻合する。第1段階の従来型OPCAB吻合の習得から、非拍動（第2）・拍動（第3）、さらに極薄の脆弱な人工血管を用いる第4段階へ漸進する4段階構成で、研修医が第4段階で100吻合を施行し前後50例ずつの比較で学習曲線を評価した。非ロボット・拍動心内視鏡下吻合を段階的に習得させる実践的教育法を示す。〔Ujihira K, Yamada A. *Novel Dry-Lab Training Method for Totally Endoscopic Coronary Anastomosis.* Innovations: Technology and Techniques in Cardiothoracic and Vascular Surgery. 2017;12(5):363-369.〕 [DOI](https://doi.org/10.1177/155698451701200509)

**📌 この領域の必読:** 最重要は図解豊富なアトラス型（🖼️）の「ロボット支援CABGのhow I teach it（R-MIDCAB教育プログラム）」で、チーム体制と段階的学習を体系化した教育の中核。実技習得では「自作低忠実度拍動心シミュレータによる吻合自己練習プログラム」（🖼️）と「3D-VRによるaortic no-touch total arterial MICS-CABGの術前シミュレーション」（🖼️）が、それぞれ安価な反復練習と術前グラフト設計の実装例として押さえておきたい。

## 4. エビデンスの文脈（OPCABの主要RCT・コンセンサス）

本レビューは手技論文を主題とするが、術式選択の前提として大規模RCTの結論を要約する。**OPCABとon-pump CABGは死亡率がおおむね同等**である一方、OPCABでは**完全血行再建率・遠隔グラフト開存が術者の習熟度に依存**しやすいことが繰り返し示されてきた。ここから「OPCABの利益（脳梗塞・輸血・腎障害の低減）はハイボリューム術者・anaortic/全動脈手技で最大化される」という、本レビュー収載論文（特に §2・§3-2）の技術的動機が導かれる。

- **ROOBY**: Shroyer AL, et al. *On-pump versus off-pump coronary-artery bypass surgery.* N Engl J Med 2009;361:1827-37. [10.1056/NEJMoa0902905](https://doi.org/10.1056/NEJMoa0902905)
- **ROOBY-FS（5年）**: Shroyer AL, et al. *Five-Year Outcomes after On-Pump and Off-Pump Coronary-Artery Bypass.* N Engl J Med 2017;377:623-632. [10.1056/NEJMoa1614341](https://doi.org/10.1056/NEJMoa1614341)
- **CORONARY（30日）**: Lamy A, et al. *Off-pump or on-pump coronary-artery bypass grafting at 30 days.* N Engl J Med 2012;366:1489-97. [10.1056/NEJMoa1200388](https://doi.org/10.1056/NEJMoa1200388)
- **CORONARY（1年）**: Lamy A, et al. *Effects of off-pump and on-pump coronary-artery bypass grafting at 1 year.* N Engl J Med 2013;368:1179-88. [10.1056/NEJMoa1301228](https://doi.org/10.1056/NEJMoa1301228)
- **CORONARY（5年）**: Lamy A, et al. *Five-Year Outcomes after Off-Pump or On-Pump Coronary-Artery Bypass Grafting.* N Engl J Med 2016;375:2359-2368. [10.1056/NEJMoa1601564](https://doi.org/10.1056/NEJMoa1601564)
- **GOPCABE（高齢者）**: Diegeler A, et al. *Off-pump versus on-pump coronary-artery bypass grafting in elderly patients.* N Engl J Med 2013;368:1189-98. [10.1056/NEJMoa1211666](https://doi.org/10.1056/NEJMoa1211666)
- **ISMICS コンセンサス（RCTのSR/MA）**: *ISMICS Consensus Conference and Statements of Randomized Controlled Trials of Off-Pump versus Conventional CABG.* Innovations 2015;10(4):219-229. [10.1177/155698451501000401](https://doi.org/10.1177/155698451501000401)
- **ロボットCABG 二十年メタ解析**: *Systematic review and meta-analysis of two decades of reported outcomes.* Ann Cardiothorac Surg 2024. [10.21037/acs-2023-rcabg-0191](https://doi.org/10.21037/acs-2023-rcabg-0191)

> [!note] NEJMの4 RCT（ROOBY/CORONARY/GOPCABE）は本サーベイの対象誌（心臓外科手技系誌）外のため機械収集には含まれず、DOIはPubMed/CrossRefで個別に実在確認した一次論文である。

## 5. データソースと再現性

本レビューの生成物・中間データは `opcab_technique/` 配下に保存：

- `harvest.sh` — CrossRef/PubMed 収集スクリプト、`raw/` — 生JSON
- `candidates.json`（1,344）→ `core_candidates.json`（376）→ `core_with_abstracts.json`（Europe PMC付与）
- `classified/batch_*.json` — 16エージェントの分類結果
- `verified_technique.json`（114編・DOI検証済み）／`technique_grouped.json`
- `synth/*.json`（領域別入力）→ `synth_out/*.md`（領域別ドラフト）
- `tables/opcab_technique_papers.csv` — 全手技論文の一覧表
- `../output/doi_verification_opcab_technique.md` — DOI検証ログ

*検索実施日: 2026-05-30。CrossRef/PubMed/Europe PMC の収録状況により、ごく最近のOnline First論文が一部未反映の可能性がある。*
