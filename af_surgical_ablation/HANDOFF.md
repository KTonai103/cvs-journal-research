# HANDOFF — 外科的心房細動治療レビュー (af_surgical_ablation)

最終更新: 2026-07-25 / フェーズ: **全フェーズ完了（A〜E 精読 ＋ F 統合・HTML化）**

> ## ✅ 完了（2026-07-25、セッションF）
> - 統合レビュー `md/AF_surgical_ablation_review.md`（全15章＋精読文献リスト72本、197KB / 1,215行）
> - HTML `output/af_surgical_ablation_review.html`（257KB、全文検索窓＋3階層サイドバー目次、
>   h2 17／h3 79／表29／callout／PubMed リンク204）
>
> ⚠️ **ビルド時の依存**: このHTMLは `convert_to_html.py` の `fix_cjk_emphasis()`（CJK文字に挟まれた
> `**…**` を pandoc が太字化できない問題の救済）が入った状態で生成した。**この関数はコミット時点で
> 未コミットの作業変更だった**ため、`convert_to_html.py` が古い状態のまま再ビルドすると本文に
> リテラルの `**` が残る。再ビルド前に `grep -c fix_cjk_emphasis ../convert_to_html.py` で確認すること
> （生成後のHTMLで `literal ** pairs = 0` を確認するのが確実）。
> - ビルダー `build_html.py`（`robotic_cpb/build_html.py` を雛形に複製・meta/既定パスのみ変更）
> - `index.html` に **不整脈外科（`#arrhythmia`, `--c-arrhythmia`）section を新設**＋カード追加、
>   catnav リンク追加、ヘッダの「トピックレビュー」件数を 10→11 に更新
>
> **セッションF で有効だった読み方（次に同種の統合をする場合の推奨）**
> 全ノート 1.9MB は一度に読めないが、**各ノートから「## 論文別ノート」節だけを機械的に除去**すると
> 276KB（≒100k tok）に落ち、1コンテキストで通読できる。論文別見出し（`### [PMID ...]`）だけは残すと
> 出典の当たりが付く。抽出スクリプトの要点は「`## 論文別ノート` から次の `## ` までを落とし、
> その区間の `### ` 行だけ残す」。サブエージェント要約は不要だった（数値精度が落ちるリスクを回避できる）。
>
> **ファクトチェック（セッションFで実施）**
> 1. レビュー本文の**全数値トークン 1,183個**を正規化（全角/ダッシュ/空白/カンマ）して notes_S*.md に
>    grep 照合 → **未検出 0件**。
> 2. 高リスク主張 **95件**について「数値の組（点推定＋95%CI＋P値など）が原ノートの同一行に共起するか」を
>    検証 → **95/95 一致**（＝数値の取り違え・他論文からの混入がないことの確認）。
> どちらもスクリプト1本で再実行できる。**次に本文を改訂したら必ず再実行すること。**

<details>
<summary>以下は精読フェーズ（A〜E）の記録 — 追加選定・追補時の参照用</summary>

## 1. このプロジェクトの目的

Ancona Live Virtual Course 2026 の講演（AFMR + 胸腔鏡下/ハイブリッドAFアブレーション）を
起点に、**近年のMaze手術・外科的AFアプローチの動向**を統合レビューHTMLとしてまとめる。
PVIなど欧米の最新トレンド、新規デバイスを含める。

読者は心臓外科医。他レビュー（`hemostatic_agents/`, `robotic_cpb/`, `hocm_myectomy/`）と同じ体裁。

## 2. 確定済みの方針（ユーザー承認済み）

- **AFMR/AFTRは分割せず1本に統合**する。講演の因果ストーリー
  （AF持続 → 左房・弁輪拡大 → AFMR → 洞調律維持の意義）をレビューの背骨にする。
- **★必読は全文精読、○推奨はAbstract参照**。
- **JACC系・BMJ系（Heart含む）は権利の関係でDL不可**。該当9編は★から降格しAbstract運用。
  一覧は `corpus/pmid_excluded_rights.txt`。代替は下記「6. 権利上欠落した文献の埋め方」参照。
  - JACC系8編: 42212987 36752455 36754519 41389071 42461200 42319332 39084744 41949521
  - BMJ系1編: 40780827 (Heart)

## 3. ディレクトリ構成

```
af_surgical_ablation/
  harvest.py / harvest2.py   PubMed収集（55検索式・総ヒット42,044）
  triage.py                  ジャーナル/publication type/新しさでスコアリング
  curate.py                  SECTIONS定義 → reading_list.md 生成（唯一の正）
  corpus/records.json        5,051編の全メタデータ（追加選定時の母集団）
  corpus/search_index.json   55検索式の全文＋ヒット数（再現性の記録）
  corpus/pmid_missing.txt    未取得★のPMID（現在1編のみ）
  corpus/pmid_excluded_rights.txt  権利上DL不可の9編（JACC系8＋BMJ系1）
  md/reading_list.md         全177編（★81/○96）注釈付き
  md/reading_list_must.md    ★のみ
  md/still_missing.md        未取得★＋権利上除外の一覧
  md/notes_S*.md             ★精読ノート S1〜S13 の13本（作成済・計約1.9MB）
  md/frag/                   セッションAの中間生成物（1論文=1ファイル、17本）。Fでは読まなくてよい
  HANDOFF.md                 本ファイル。末尾の付録にセクション別の精読対象ファイル一覧
  pdf/  pdf_text/            取得済71編（.gitignoreで公開リポジトリ除外済み）
```

**セクション定義は `curate.py` の `SECTIONS` が唯一の正。** 追加/変更はここを編集して
`python3 curate.py` を再実行する。

PDF命名規約: `PMID<番号>_<筆頭著者>_<年>_<誌略号>_<内容-ハイフン>.pdf`（hocm_myectomyと同じ）

## 4. 進捗 — 権利上除外9編を差し引いた実質必読72編中 **71編取得済**

| Sec | 内容 | 取得 | 全文量 |
|---|---|---|---|
| S1 | ガイドライン・コンセンサス | 6/6 ✅ | 707k tok ※抽出のみ |
| S2 | 総論・歴史 | 2/2 ✅ | 22k |
| S3 | 同時手術アブレーション（中核） | 9/9 ✅ | 120k |
| S4 | Lesion set | 8/8 ✅ | 91k |
| S5 | エネルギー源・新規デバイス（nsPFA） | 5/5 ✅ | 36k |
| S6 | 左房サイズ・縮小術 | 3/3 ✅ | 27k |
| S7 | LAA閉鎖 | 6/6 ✅ | 60k |
| S8 | 胸腔鏡下・ハイブリッド・Convergent | 10/10 ✅ | 121k |
| S9 | 外科 vs カテーテル | 1/2 | 14k |
| S10 | PFA時代の位置づけ | 5/5 ✅ | 112k |
| S11 | AFMR / AFTR | 12/12 ✅ | 147k |
| S12 | 合併症・安全性 | 1/1 ✅ | 9k |
| S13 | 洞調律維持の意義・POAF予防 | 3/3 ✅ | 37k |
| S14 | 日本・アジア（○のみ） | — | — |

**未取得は 40587868 の1編のみ**（Catheter and Surgical Ablation for AF: SR+MA. Ann Intern Med 2025）。
S9は取得済の 32653280（JTCVS 2022 SR+MA）で代替可能なので、**このまま精読を開始してよい**。

○推奨96編はAbstract参照のみ（DL不要）。`md/reading_list.md` に注釈付きで収録。

## 5. 精読フェーズの分割計画（重要）

取得済71編の全文は **5.7 MB ≒ 1.50M トークン**で、1セッションでは読み切れない。
以下のように分割し、各セッションが `md/notes_S*.md` を書き出す。
最終セッションはノートのみ読めばよいのでコンテキストが破綻しない。

| セッション | 対象 | 編数 | 実質量 | 状況 |
|---|---|---|---|---|
| **A** | S1（下記の注意）＋S2＋S3 | 17 | ≒150k tok（S1抽出後） | **✅ 完了 2026-07-23**（notes_S1/S2/S3.md、計833KB） |
| **B** | S4＋S5＋S6＋S9 | 17 | ≒167k tok | **✅ 完了 2026-07-23**（notes_S4/S5/S6/S9.md、計298KB） |
| **C** | S7＋S8 | 16 | ≒181k tok | **✅ 完了 2026-07-23**（notes_S7/S8.md、計345KB） |
| **D** | S10＋S12＋S13 | 9 | ≒158k tok | **✅ 完了 2026-07-23**（notes_S10/S12/S13.md、計219KB） |
| **E** | S11（AFMR/AFTR） | 12 | ≒147k tok | **✅ 完了 2026-07-23**（notes_S11.md、234KB） |
| **F** | ノート統合 → 統合レビューMD → HTML化 → index.html更新 | — | 小 | **✅ 完了 2026-07-25**（論文別ノート節を除去した 276KB のダイジェストを1コンテキストで通読。冒頭の完了メモ参照） |

**A〜Eで有効だった進め方**: Workflowで
「①1論文=1エージェントで全文精読→構造化JSON（原文英語引用を必須にする）→②セクション別ノート執筆→
③敵対的ファクトチェッカーが全数値をGrepで原文照合しEditで直接修正」の3段パイプライン。
B（17編/25エージェント/1.85Mトークン/30分）、C+D+E（37編/49エージェント/4.27Mトークン/98分）、
A（17編/40エージェント/4.94Mトークン/111分）。

**Aで改良した点（次に同じことをするなら踏襲）**:
- ①の出力を JSON ではなく **`md/frag/<SEC>_PMID<PMID>.md` への書き出し**にし、②はそれを Read する。
  JSONをプロンプトに詰め込む必要がなくなり、1論文20–75KBの密度を落とさずに渡せた。
- ③のチェッカーには**ファイル編集をさせず訂正JSONだけ返させ**、④として**1ファイル=1エージェント**が適用する
  4段構成にした。複数エージェントが同一ノートを同時Editする衝突が原理的に起きない。
  実績: 2,769数値を照合 → 訂正90件（S1 26/S2 21/S3 43）、適用89件・skip 1件（誤検知）。

**③が実際に捕まえた誤りの型（＝②だけでは必ず残る。省略禁止）**:
- **表の行/列ずれによる数値の取り違え**（最頻。OPINIONのIABP/ECMO/30日死亡、Zhengのサブグループ OR が
  実は糖尿病の有無の行、CEASE-AFの気胸、S12のTable 2 P値列）。pdftotextで列が崩れた表が主因。
- **他論文の数値の混入＝捏造**（S11でMATTERHORNに「126施設」＝CABANAの施設数が混入していた）。
- **デザインの誤ラベル**（S13でCABANA Bunch 2024 を post hoc としていたが原文は prespecified）。
- **原文の帰属先の誤り**（「著者が施設間ばらつきを認めた」等、文脈を取り違えた引用）。
- **存在しない「原文内不整合」の指摘**（取り違えに由来する幻の矛盾）。

**メインのコンテキストは枯れない**（全文はサブエージェントが読み、メインは完了通知のみ）。
1セッションで複数の分割をまとめて回してよい。**ただしFだけは必ず新セッション**（全ノートを読むため）。

A〜Eは互いに独立、順不同・並行可。**Fは必ず最後**。
S11(AFMR)を単独セッションにしているのは、講演の主題であり本レビューの背骨だから。

**S1の注意**: ガイドライン6本だけで707k トークン（ESC 2024・ACC/AHA 2023 は本文100ページ級）。
**全文通読してはいけない。** 推奨表を狙い撃ちで抽出すること。例:

```bash
grep -n -A5 -B2 -iE "surgical ablation|left atrial appendage|Cox-maze|appendage occlusion" \
  pdf_text/PMID38286206_*.txt | head -100
grep -n -iE "^\s*(I|IIa|IIb|III)\s|Class of recommendation|LOE" pdf_text/PMID39210723_*.txt
```

### 各ノートに必ず記録する項目
研究デザイン / N数 / 追跡期間（median） / 主要エンドポイントの定義（洞調律の判定方法・
モニタリング手段は特に重要、CASA-AFは連続モニタリング） / 効果量（HR/OR/RR + 95%CI） /
限界。**推奨クラスは一次資料でどう書かれているかを必ず確認する**
（過去に「Class I表記が二次資料依拠だった」訂正が発生している）。

## 6. 権利上欠落した文献の埋め方

DL不可の9編は、いずれも取得済文献で論旨を維持できる。**「入手できなかったので触れない」ではなく、
下表の代替で記述し、必要なら本文中でAbstract依拠であることを明示する。**

| 落ちた文献 | 代替（すべて取得済） |
|---|---|
| PV再伝導 PFA vs RF (42461200) / PFA後AT registry (42319332) / MANIFEST-US (41389071) | **41968953** EHRA/HRS PFA科学声明 ＋ **41652117** ADVENT-LTO 4年 ＋ **41568658** BEAT PAROX-AF |
| AFMR統一定義 (41949521) | **42092503** AATS 2026コンセンサスが定義章を持つ |
| Hybrid vs 再カテーテルRCT (36752455) | **41801607** ベイジアンMAが本試験を組み入れ済み |
| JACC総説 低侵襲外科+経皮併用 (36754519) | **40574669** EJCTS state-of-the-art review |
| 左房拡大とアブレーション成績 (42212987) | **24183909** Ad 2014 ＋ **33713828** 左房縮小術 |
| 非僧帽弁手術の外科アブレーション メタ解析 (40780827, Heart/BMJ) | **40720587** オランダ全国レジストリ（CABG/AVR単独例）＋ **39471966** 遠隔生存メタ解析 |
| 外科 vs カテーテル SR+MA (40587868, Ann Intern Med・未取得) | **32653280** JTCVS 2022 の SR+MA |

## 7. 統合・HTML化フェーズ（セッションF）で踏むべき手順

0. `md/notes_S*.md` 13本を読む（本文PDFも `md/frag/` も読まない）→ 統合レビュー `md/AF_surgical_ablation_review.md` を書く
   - 総量 ≒1.9MB（S1 305KB / S2 125KB / S3 403KB / S4 131KB / S5 70KB / S6 65KB / S7 118KB /
     S8 227KB / S9 32KB / S10 117KB / S11 234KB / S12 40KB / S13 62KB）。**一度に全部は読めない。**
   - 各ノート冒頭の「このセクションの結論（3-5行）」と末尾の「セクション横断の論点」だけで骨格は組める。
     数値を引くときだけ該当ノートの論文別ノートを開く、という読み方をする。

1. `robotic_cpb/build_html.py` を雛形にする（`convert_to_html.py` 再利用＋全文検索追加）
2. 出力は `output/af_surgical_ablation_review.html`
3. `index.html` の該当セクションにカード追加＋件数更新
4. **outputのHTMLとMDソースの両方をcommitする**（でないとGitHub Pagesが404）
5. Playwright検証は `file://` 不可 → localhost配信して確認
6. git push が400で失敗する場合は `git config http.postBuffer` を拡大

## 8. 環境上の注意（過去の教訓）

- 背景bashはネットワーク不可。PubMed/curlは**前景**で実行する。
- PDFは `pdftotext` で事前にテキスト化してから読む（PDF読み込みフック回避）。
- `*/pdf/`, `*/pdf_text/` は `.gitignore` 済み。著作権物を公開リポジトリに入れない。

---

## 付録: セクション別 精読対象ファイル一覧（`pdf_text/` 内）

各セッションはここに挙がったファイルだけを読めばよい。○推奨はAbstract参照のため対象外。


### S1. ガイドライン・コンセンサス（土台）  — セッション**A**（6編）

- `PMID38286206_WylervonBallmoosMC_2024_ATS_STS2023-Surgical-AF-Guideline.txt`  
  <sub>Ann Thorac Surg 2024 — The Society of Thoracic Surgeons 2023 Clinical Practice Guidelines for the Surgical Treatment o</sub>
- `PMID39210723_VanGelderIC_2024_EHJ_2024-ESC-EACTS-AF-Guideline.txt`  
  <sub>Eur Heart J 2024 — 2024 ESC Guidelines for the management of atrial fibrillation developed in collaboration with t</sub>
- `PMID38597857_TzeisS_2024_HeartRhythm_2024-EHRA-HRS-Ablation-Consensus.txt`  
  <sub>Heart Rhythm 2024 — 2024 European Heart Rhythm Association/Heart Rhythm Society/Asia Pacific Heart Rhythm Society/L</sub>
- `PMID38043043_WritingCommitteeMembers_2024_JACC_2023-ACC-AHA-ACCP-HRS-AF-Guideline.txt`  
  <sub>J Am Coll Cardiol 2024 — 2023 ACC/AHA/ACCP/HRS Guideline for the Diagnosis and Management of Atrial Fibrillation: A Repo</sub>
- `PMID42092503_MoriM_2026_JTCVS_AATS2026-AFMR-Consensus.txt`  
  <sub>J Thorac Cardiovasc Surg 2026 — The 2026 American Association for Thoracic Surgery Expert Consensus Document: Management of atr</sub>
- `PMID42009116_ChatterjeeS_2026_ATS_STS2026-POAF-Guideline.txt`  
  <sub>Ann Thorac Surg 2026 — The Society of Thoracic Surgeons 2026 Clinical Practice Guidelines for the Prevention and Treat</sub>

### S2. 総論・歴史・現在地  — セッション**A**（2編）

- `PMID41176374_CoxJL_2025_HeartRhythm_Cox-Story-Behind-Maze.txt`  
  <sub>Heart Rhythm 2025 — The story behind the Maze procedure</sub>
- `PMID40574669_KowalewskiM_2025_EJCTS_SurgicalAblation-Concomitant-StateOfTheArt.txt`  
  <sub>Eur J Cardiothorac Surg 2025 — Surgical ablation of atrial fibrillation with concomitant cardiac surgery: a state-of-the-art r</sub>

### S3. 同時手術アブレーションのエビデンス（中核）  — セッション**A**（9編）

- `PMID25853744_GillinovAM_2015_NEJM_CTSN-RCT-SA-During-MVSurgery.txt`  
  <sub>N Engl J Med 2015 — Surgical ablation of atrial fibrillation during mitral-valve surgery</sub>
- `PMID30557941_BlackstoneEH_2019_JTCVS_CTSN-Biatrial-vs-PVI-Reanalysis.txt`  
  <sub>J Thorac Cardiovasc Surg 2019 — Biatrial maze procedure versus pulmonary vein isolation for atrial fibrillation during mitral v</sub>
- `PMID39471966_SakuraiY_2025_AmJCardiol_LateSurvivalBenefit-ConcomitantSA-SRMA.txt`  
  <sub>Am J Cardiol 2025 — Late Survival Benefits of Concomitant Surgical Ablation for Atrial Fibrillation During Cardiac </sub>
- `PMID37848175_GemelliM_2023_AmJCardiol_SA-During-MVSurgery-SRMA-RCTs.txt`  
  <sub>Am J Cardiol 2023 — Surgical Ablation for Atrial Fibrillation During Mitral Valve Surgery: A Systematic Review and </sub>
- `PMID40720587_BayónMA_2025_EJCTS_Netherlands-Registry-CABG-AVR-ConcomitantSA.txt`  
  <sub>Eur J Cardiothorac Surg 2025 — Concomitant Surgical Ablation in Atrial Fibrillation Patients Undergoing Cardiac Surgery for Is</sub>
- `PMID40383232_YiJJ_2025_JTCVS_CoxMazeIV-MitralDisease-LongTerm.txt`  
  <sub>J Thorac Cardiovasc Surg 2025 — The long-term outcomes of concomitant Cox-Maze IV procedure in patients with mitral valve disea</sub>
- `PMID33840467_MehaffeyJH_2023_JTCVS_Barriers-to-AF-Ablation-MV-Surgery.txt`  
  <sub>J Thorac Cardiovasc Surg 2023 — Barriers to atrial fibrillation ablation during mitral valve surgery</sub>
- `PMID42092502_DamianoRJ_2026_JTCVS_Damiano-iRF-Cryo-Prospective-Multicenter.txt`  
  <sub>J Thorac Cardiovasc Surg 2026 — A prospective, multicenter trial of irrigated radiofrequency ablation and cryoablation to treat</sub>
- `PMID41138810_AdN_2026_JTCVS_ICE-AFIB-Cryo-IDE-Trial.txt`  
  <sub>J Thorac Cardiovasc Surg 2026 — The ICE-AFIB trial: A multicenter prospective investigational device exemption (IDE) trial usin</sub>

### S4. Lesion set：biatrial vs 左房 vs PVI／Box lesion  — セッション**B**（8編）

- `PMID39481591_PyoWK_2025_JTCVS_LesionSet-LongTerm-Multicenter-PSW.txt`  
  <sub>J Thorac Cardiovasc Surg 2025 — The long-term influence of lesion set in the surgical ablation of atrial fibrillation during mi</sub>
- `PMID34164872_GuoQ_2021_JCE_Biatrial-vs-LA-Bayesian-NMA.txt`  
  <sub>J Cardiovasc Electrophysiol 2021 — Bi-atrial or left atrial ablation of atrial fibrillation during concomitant cardiac surgery: A </sub>
- `PMID40061540_NittaT_2025_JTCVSOpen_Incomplete-Ablation-Mechanism-PostMaze.txt`  
  <sub>JTCVS Open 2025 — Incomplete ablation as a mechanism of atrial fibrillation recurrence and atrial tachycardia dev</sub>
- `PMID41242589_GoingsD_2025_HeartRhythm_PostMaze-Recurrence-CatheterMapping.txt`  
  <sub>Heart Rhythm 2025 — Atrial arrhythmia recurrence after the Maze procedure: Insights from catheter-based mapping</sub>
- `PMID39215996_WilliamJ_2025_EHJ_CAPLA-LongTerm-PWI.txt`  
  <sub>Eur Heart J 2025 — Radiofrequency catheter ablation of persistent atrial fibrillation by pulmonary vein isolation </sub>
- `PMID42319794_MiyazakiS_2026_EHJ_CORNERSTONE-AF-PWI-Trial.txt`  
  <sub>Eur Heart J 2026 — Adjunctive posterior wall isolation for persistent and long-standing persistent atrial fibrilla</sub>
- `PMID39556379_SangC_2025_JAMA_PROMPT-AF-RCT-PVI-plus-Linear.txt`  
  <sub>JAMA 2025 — Pulmonary Vein Isolation With Optimized Linear Ablation vs Pulmonary Vein Isolation Alone for P</sub>
- `PMID40392905_DervalN_2025_CircAE_MarshallPlan-vs-PVI-RCT.txt`  
  <sub>Circ Arrhythm Electrophysiol 2025 — Marshall-Plan Ablation Strategy Versus Pulmonary Vein Isolation in Persistent AF: A Randomized </sub>

### S5. エネルギー源とデバイス／新規デバイス（nsPFA含む）  — セッション**B**（5編）

- `PMID39674689_BaudoM_2025_HeartLungCirc_RF-vs-Cryo-CoxMaze-MetaAnalysis.txt`  
  <sub>Heart Lung Circ 2025 — Radiofrequency and Cryoablation as Energy Sources in the Cox-Maze Procedure: A Meta-Analysis of</sub>
- `PMID41005435_YiJ_2026_JTCVS_nsPFA-CoxMaze-LesionSet-BeatingHeart.txt`  
  <sub>J Thorac Cardiovasc Surg 2026 — Nanosecond pulsed field ablation: Feasibility of creating the Cox-maze lesion set on the beatin</sub>
- `PMID39644967_DunningtonGH_2025_JTCVS_nsPFA-Surgical-Clamp-Chronic-Porcine.txt`  
  <sub>J Thorac Cardiovasc Surg 2025 — The performance of a new nanosecond pulsed-field ablation surgical clamp in the ablation of car</sub>
- `PMID37920983_SerraF_2023_CircAE_nsPFA-Bipolar-Clamp-Durable-Transmural.txt`  
  <sub>Circ Arrhythm Electrophysiol 2023 — Nanosecond Pulsed Electric Field Ablation With a Bipolar Clamp Creates Durable Transmural Lesio</sub>
- `PMID39066781_MusikantowDR_2024_JACCEP_Epicardial-PFA-During-Cardiac-Surgery.txt`  
  <sub>JACC Clin Electrophysiol 2024 — Epicardial Pulsed Field Ablation for the Treatment of Paroxysmal Atrial Fibrillation During Car</sub>

### S6. 左房サイズ・左房縮小術（講演の「LAが大きくても諦めるな」）  — セッション**B**（3編）

- `PMID24183909_AdN_2014_JTCVS_Enlarged-LA-Should-We-Ablate.txt`  
  <sub>J Thorac Cardiovasc Surg 2014 — Should surgical ablation for atrial fibrillation be performed in patients with a significantly </sub>
- `PMID33713828_ChoiW_2022_SeminTCVS_LA-Reduction-During-SurgicalAblation.txt`  
  <sub>Semin Thorac Cardiovasc Surg 2022 — The Impact of Left Atrial Reduction During Surgical Ablation of Atrial Fibrillation</sub>
- `PMID37821261_BaudoM_2023_HeartLungCirc_LA-VolumeReduction-with-CoxMaze-MetaAnalysis.txt`  
  <sub>Heart Lung Circ 2023 — Left Atrium Volume Reduction Procedure Concomitant With Cox-Maze Ablation in Patients Undergoin</sub>

### S7. 左心耳（LAA）閉鎖  — セッション**C**（6編）

- `PMID33999547_WhitlockRP_2021_NEJM_LAAOS-III.txt`  
  <sub>N Engl J Med 2021 — Left Atrial Appendage Occlusion during Cardiac Surgery to Prevent Stroke</sub>
- `PMID37732457_ConnollySJ_2023_Circulation_LAAOSIII-OAC-Use-Interaction.txt`  
  <sub>Circulation 2023 — Oral Anticoagulation Use and Left Atrial Appendage Occlusion in LAAOS III</sub>
- `PMID41247709_KatsanosAH_2026_JAMANeurol_LAAOSIII-StrokeMechanism-Severity.txt`  
  <sub>JAMA Neurol 2026 — Stroke Mechanism and Severity After Left Atrial Appendage Occlusion: Insights From the LAAOS II</sub>
- `PMID40888584_YuanX_2026_EHJ_OPINION-Trial-LAAO-NoAF.txt`  
  <sub>Eur Heart J 2026 — Surgical left atrial appendage occlusion in valvular heart disease without atrial fibrillation:</sub>
- `PMID40132739_BurtonS_2025_HeartRhythm_SurgicalLAAO-SinusRhythm-MetaAnalysis.txt`  
  <sub>Heart Rhythm 2025 — Clinical impact of surgical left atrial appendage occlusion during cardiac surgery in patients </sub>
- `PMID41965066_VadR_2026_EJCTS_SurgicalLAAC-SuccessCriteria-SR.txt`  
  <sub>Eur J Cardiothorac Surg 2026 — Methods and Criteria for Evaluating the Success of Surgical Left Atrial Appendage Closure: A Sy</sub>

### S8. スタンドアロン低侵襲：胸腔鏡下／ハイブリッド／Convergent  — セッション**C**（10編）

- `PMID32860414_HaldarS_2020_EHJ_CASA-AF-RCT-Original.txt`  
  <sub>Eur Heart J 2020 — Catheter ablation vs. thoracoscopic surgical ablation in long-standing persistent atrial fibril</sub>
- `PMID38763376_BoyallaV_2024_HeartRhythm_CASA-AF-LongTerm-CostEffectiveness.txt`  
  <sub>Heart Rhythm 2024 — Long-term clinical outcomes and cost-effectiveness of catheter vs thoracoscopic surgical ablati</sub>
- `PMID33185144_DeLurgioDB_2020_CircAE_CONVERGE-Trial.txt`  
  <sub>Circ Arrhythm Electrophysiol 2020 — Hybrid Convergent Procedure for the Treatment of Persistent and Long-Standing Persistent Atrial</sub>
- `PMID40711852_DollN_2025_EJCTS_CEASE-AF-2yr-RCT.txt`  
  <sub>Eur J Cardiothorac Surg 2025 — Durable effectiveness and safety of hybrid ablation versus catheter ablation: 2-year results fr</sub>
- `PMID38306687_BulavaA_2024_Europace_SURHYB-SequentialHybrid-vs-CryoMaze-RCT.txt`  
  <sub>Europace 2024 — Sequential hybrid ablation vs. surgical CryoMaze alone for treatment of atrial fibrillation: re</sub>
- `PMID39226147_ZhengZ_2024_Europace_SimultaneousHybrid-vs-Thoracoscopic-RCT.txt`  
  <sub>Europace 2024 — Comparing simultaneous hybrid ablation with stand-alone thoracoscopic surgical ablation for the</sub>
- `PMID39255332_AertsL_2024_Europace_Isolated-vs-Hybrid-Thoracoscopic-IPDMA.txt`  
  <sub>Europace 2024 — Short- and long-term outcomes in isolated vs. hybrid thoracoscopic ablation in patients with at</sub>
- `PMID41801607_KhanraD_2026_JICE_Hybrid-vs-Endocardial-BayesianMA.txt`  
  <sub>J Interv Card Electrophysiol 2026 — Hybrid versus endocardial ablation for persistent atrial fibrillation: a systematic review and </sub>
- `PMID41314536_WeiningerG_2026_JTCVS_HybridAblation-LongTerm-SingleCenter.txt`  
  <sub>J Thorac Cardiovasc Surg 2026 — Long-term outcomes for patients undergoing hybrid ablation for atrial fibrillation</sub>
- `PMID40971527_VroomenM_2025_Europace_EORP-EHAFA-Registry-1yr.txt`  
  <sub>Europace 2025 — Epicardial and hybrid surgical ablation of atrial fibrillation: 1-year follow-up outcomes of th</sub>

### S9. 外科 vs カテーテル（直接比較のエビデンス）  — セッション**B**（1編）

- `PMID32653280_HuangH_2022_JTCVS_Catheter-vs-Surgical-SRMA-RCTs.txt`  
  <sub>J Thorac Cardiovasc Surg 2022 — Comparison of catheter and surgical ablation of atrial fibrillation: A systemic review and meta</sub>

### S10. PFA時代における外科の位置づけ（新規エネルギー源）  — セッション**D**（5編）

- `PMID42041224_WazniOM_2026_NEJM_AVANTGUARD-PFA-InitialTherapy-PersistentAF.txt`  
  <sub>N Engl J Med 2026 — Pulsed Field Ablation as Initial Therapy for Persistent Atrial Fibrillation</sub>
- `PMID41652117_ReddyVY_2026_NatMed_ADVENT-LTO-PFA-4yr.txt`  
  <sub>Nat Med 2026 — Pulsed field ablation versus conventional thermal ablation for paroxysmal atrial fibrillation: </sub>
- `PMID42186803_OsmancikP_2026_Circulation_PFA-SHAM-RCT.txt`  
  <sub>Circulation 2026 — Pulsed Field Ablation Versus Sham to Treat Atrial Fibrillation: The PFA-SHAM Randomized Clinica</sub>
- `PMID41568658_JaisP_2026_EHJ_BEAT-PAROX-AF-PFA-vs-RF.txt`  
  <sub>Eur Heart J 2026 — Pulsed field vs radiofrequency ablation for paroxysmal atrial fibrillation: the BEAT PAROX-AF t</sub>
- `PMID41968953_KühneM_2026_Europace_EHRA-HRS-PFA-ScientificStatement.txt`  
  <sub>Europace 2026 — Pulsed field ablation for the interventional treatment of atrial fibrillation: a scientific sta</sub>

### S11. AFMR（心房性機能性MR）／AFTR  — セッション**E**（12編）

- `PMID36480974_FarhanS_2022_JACC_AFMR-Pathophysiology-SOTA-Review.txt`  
  <sub>J Am Coll Cardiol 2022 — Pathophysiology, Echocardiographic Diagnosis, and Treatment of Atrial Functional Mitral Regurgi</sub>
- `PMID38879118_SongK_2025_JTCVS_AFMR-vs-Degenerative-MVSurgery-Outcome.txt`  
  <sub>J Thorac Cardiovasc Surg 2025 — Surgical outcome of mitral valve surgery in atrial functional mitral regurgitation compared wit</sub>
- `PMID40986391_PyeatteSR_2025_EJCTS_AFMR-vs-VFMR-MVSurgery-WashU.txt`  
  <sub>Eur J Cardiothorac Surg 2025 — Outcomes of Mitral Valve Surgery for Atrial Functional Mitral Regurgitation vs Ventricular Func</sub>
- `PMID39197816_BakirNH_2025_JTCVS_AFMR-Annuloplasty-Durability-Cleveland.txt`  
  <sub>J Thorac Cardiovasc Surg 2025 — Durability of annuloplasty in patients with atrial functional mitral regurgitation associated w</sub>
- `PMID41339275_BerrettaP_2025_EJCTS_MiniMitral-International-Registry-AFMR.txt`  
  <sub>Eur J Cardiothorac Surg 2025 — Surgical Techniques and Outcomes for Atrial Functional Mitral Regurgitation: Insights From the </sub>
- `PMID38987787_SongK_2024_JCTS_Maze-plus-MVSurgery-in-AFMR.txt`  
  <sub>J Cardiothorac Surg 2024 — Outcomes of maze procedure and mitral valve surgery in atrial functional mitral regurgitation: </sub>
- `PMID41442445_KhairallahS_2026_ICVTS_AFMR-SurgicalRepair-vs-TEER-MetaComparison.txt`  
  <sub>Interdiscip Cardiovasc Thorac Surg 2026 — Comparison of Meta-Analytical Estimates Between Surgical Repair and Transcatheter Edge-to-Edge </sub>
- `PMID39475706_RudolphF_2025_Circulation_MATTERHORN-PostHoc-Atrial-vs-Ventricular.txt`  
  <sub>Circulation 2025 — Transcatheter Repair Versus Surgery for Atrial Versus Ventricular Functional Mitral Regurgitati</sub>
- `PMID40629531_KanekoT_2026_EHJ_OCEAN-Mitral-REVEAL-AFMR-TEER-vs-Medical.txt`  
  <sub>Eur Heart J 2026 — Transcatheter edge-to-edge repair vs medical therapy in atrial functional mitral regurgitation:</sub>
- `PMID40256860_DhontS_2025_EJHF_CABANA-AF-MR-Interaction.txt`  
  <sub>Eur J Heart Fail 2025 — The interaction between atrial fibrillation and mitral regurgitation: Insights from the CABANA </sub>
- `PMID39094723_OkazakiRA_2025_HeartRhythm_CA-for-AF-with-SignificantMR-SRMA.txt`  
  <sub>Heart Rhythm 2025 — Catheter ablation for atrial fibrillation in patients with significant mitral regurgitation: A </sub>
- `PMID38441886_MuraruD_2024_EHJ_AtrialSecondaryTR-Pathophys-Definition.txt`  
  <sub>Eur Heart J 2024 — Atrial secondary tricuspid regurgitation: pathophysiology, definition, diagnosis, and treatment</sub>

### S12. 合併症・安全性  — セッション**D**（1編）

- `PMID40184218_IvertT_2025_ICVTS_PPM-After-CoxMazeIV-NationwideRegistry.txt`  
  <sub>Interdiscip Cardiovasc Thorac Surg 2025 — High incidence of permanent pacemaker after Cox-maze IV and mitral valve surgery: a nationwide </sub>

### S13. 洞調律維持の意義・POAF予防（周辺だが議論に必須）  — セッション**D**（3編）

- `PMID38629286_BunchTJ_2024_CircAE_CABANA-SinusRhythm-PrognosticImpact.txt`  
  <sub>Circ Arrhythm Electrophysiol 2024 — Prognostic Impact of Sinus Rhythm in Atrial Fibrillation Patients: Separating Rhythm Outcomes F</sub>
- `PMID34447995_WillemsS_2022_EHJ_EAST-AFNET4-EarlyRhythmControl.txt`  
  <sub>Eur Heart J 2022 — Systematic, early rhythm control strategy for atrial fibrillation in patients with or without s</sub>
- `PMID39550720_YangZ_2025_JAMACardiol_pCAD-POAF-PartialDenervation-RCT.txt`  
  <sub>JAMA Cardiol 2025 — Partial Cardiac Denervation to Prevent Postoperative Atrial Fibrillation After Coronary Artery </sub>
</details>
