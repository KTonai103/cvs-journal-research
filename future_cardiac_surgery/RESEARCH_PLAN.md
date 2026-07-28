---
title: リサーチ計画 — 心臓弁膜症外科の未来（Future of Heart Valve Surgery）
date: 2026-07-26
status: planning-complete / execution-not-started
seed: 10.1093/ejcts/ezag185
tags:
  - future-cardiac-surgery
  - research-plan
---

# リサーチ計画：心臓弁膜症外科の未来

## 0. このプロジェクトは何か

EACTS Innovation Committee の Editorial **「Heart Valve of the Future」**（EJCTS 2026;68(6):ezag185）を
**出発点＝仮説の一覧**として扱い、そこに書かれた各主張を **一次文献で定量的に裏取りし、エビデンス段階で格付けし直した
包括レビューページ**を作る。

**目的**：自分の知識整理と戦略立案。「どの技術に時間と症例を投じるか」を判断できる状態にすること。
したがって **数字・一次文献リンク・批判的評価（誇大 vs 本物）を最優先**する。読み物としての面白さは二の次でよい。

### 決定済みのスコープ（2026-07-26、本人確認済み）

| 項目 | 決定 |
|---|---|
| スコープ | **弁膜症にフォーカス**（冠動脈・大動脈・移植/MCS・不整脈は「触れる程度」に留め、深掘りしない） |
| 用途 | **自分の知識整理・戦略立案**（数字と一次文献を厚く、批判的評価を明示） |
| 未来予測の踏み込み | **エビデンス準拠＋明示ラベル付きの自分の見立て**（推測部分は視覚的に分離する） |
| 図 | **論文PDFから実図を切り出して貼る。自作SVG・無理な図示は作らない**（2026-07-26 追加指示） |

### 既存資産との関係（重複を作らないこと）

このリポジトリには弁膜症の蓄積が既にある。**未来ページは「現在の到達点」を既存レビューに委ね、そこから先だけを書く**。

| 既存 | 何が書いてあるか | 未来ページでの扱い |
|---|---|---|
| `small_annulus_avr/` ＋ `output/small_annulus_avr_integrated_review_2026-06.html` | 小径弁輪AVRの適応論、PPM、AAE適応、SAKURA-AVRプロトコル | **リンクして委譲**。未来ページでは「lifetime managementの中でのAAE/ViV」だけ扱う |
| `aae_technique_atlas/` | Nicks/Manouguian/Konno/Y-incisionのhow-to、日本人小体格の術式選択 | リンクして委譲 |
| `topic_valve_durability_by_valve_2026_06.md` ＋ summary | 弁別の最長フォロー、actuarial vs actual、**Sorin外付け系列＝反面教師** | **第9章「失敗した未来」の一次資料として再利用** |
| `topic_savr_vs_tavr_longterm_2026_05.md` | SAVR vs TAVR長期 | 第8章 lifetime management の土台 |
| `robotic_cpb/` | ロボット支援CPBのpitfall 283項目（外科医/臨工/麻酔の3視点） | 第2章ロボットの「現実の落とし穴」として引用 |
| `cor_knot/` | 自動チタンファスナーの合併症と打ち方 | 第2章「低侵襲を支える器具」の実例＋反例 |
| `MD/cardiac_surgery_journals_2026_06.md` / `_07.md` | Govers VSARR年12例閾値、Yokoyama HAART 44%再介入、EACTS position paper | **最重要の新着ソース。既に日本語要約済み**なので流用 |

---

## 1. 中心となる問い（この5つに答えられれば成功）

1. **1960年代以降「破壊的変化がなかった」というEACTSの歴史認識は正しいか。** 正しいとすれば、次の破壊的変化はどこから来るか。
2. **「弁形成 > 弁置換」はどこまで一般化できるか。** 大動脈弁形成の再介入率（Yokoyama 44%）をどう受け止めるか。施設症例数（Govers ≥12/年）の壁は何を意味するか。
3. **living valve（脱細胞化homograft・組織工学弁・ポリマー弁）は、いつ・どの適応で標準になるか。** 現在のエビデンス段階は本当はどこか。
4. **低侵襲/ロボットは「未来」なのか、それとも既に決着した現在なのか。** 経腋窩AVRやロボットAVRは日本で意味を持つか。
5. **日本で、自分の施設で、次の5年に何をやるべきか。** 症例数・償還・デバイスラグ・人材を踏まえた実行可能な結論。

---

## 2. 章立て（案・全10章）

各章の末尾に必ず **「エビデンス格付け表」** と **「🔮 私の見立て」** ブロックを置く。

| 章 | タイトル | 中身 | 主要ソース |
|---|---|---|---|
| 1 | 弁手術の60年と「破壊的変化の不在」 | Starr-Edwards→tilting disc→bileaflet→生体弁→TAVI。Carpentier機能分類・David/Yacoub・Rossの位置づけ。**なぜ人工弁は反復改良に留まったのか** | ref[1][2][3]、Fig.1 |
| 2 | 低侵襲とロボット：もう「未来」ではない領域 | MIMVS/ロボット僧帽弁の現代データ（引用が2008/2011で古い→更新）、経腋窩AVR 1,000例、ロボットAVRの実像、小児の低侵襲開胸（ECHSA 3,000例）。**器具（自動縫合ファスナー・shafted tools）と落とし穴** | ref[7][8][9][10][11]、`robotic_cpb/`、`cor_knot/` |
| 3 | 自己弁温存とVSARR：技術は完成し、問題は普及になった | David vs Yacoub、AVIATOR PSM、**Govers ezag177の「年12例」閾値**、El Khoury分類、Valsalva graft、caliper、外部リング、術中加圧可視化device | ref[12][13][14][15][16][17][19]、EJCTS 68(6) |
| 4 | 大動脈弁形成のデバイス：HAARTは何を教えたか | Rankin原典 → **Yokoyama/Fukuhara 2026（5年再介入40.8%、44%が再介入、剛性intra-annular設計と過度のdownsizing）**。「デバイスで再現性を上げる」戦略の限界事例として正面から扱う | ref[18]、JTCVS 2026;172(1):76-83 |
| 5 | Ross手術の復権 | El-Hamamsy JACC 2022、centers of excellence論、生涯管理・自家肺動脈の耐久性、日本での実施可能性 | ref[4]＋系統検索 |
| 6 | 脱細胞化homograft：最も臨床に近い「living valve」 | Sarikouch 20年成績（EJCTS 2026;68(2):ezag087）、ARISE 5年、10年経験。**ドナー反応・入手性・規制**。RVOTから大動脈位へ広がるか | ref[5][6][20] |
| 7 | 組織工学弁とポリマー弁：本当はどこまで来ているか | ex vivo バイオリアクター vs in situ smart scaffold の2戦略、電界紡糸conduit、**Kasahara自己組織化ハイブリッド生地（日本）**、**Tria/Foldax ポリマー僧帽弁 JACC 2025 の1年成績**。製造・規制の壁 | ref[21][22][23]、Fig.4 |
| 8 | Ozaki手術と「日本発術式」の国際的評価 | Baird 2021（小児）とKaramlou論評、成人の長期成績（尾崎ら本体＝本Editorialは引用していない）、Rossへのbridge論。**日本発術式がどう評価され、どこで止まるか**という構造の考察 | ref[24][25]＋補完検索 |
| 9 | 失敗した未来から学ぶ | Sorin外付け系列など、かつて「未来」とされ淘汰された弁。actuarial vs actual の読み違い、単施設中期成績の楽観。**新技術の評価チェックリスト**を作る | `topic_valve_durability_by_valve_2026_06.md` |
| 10 | 次の5年：エビデンス格付け一覧と、日本での実行戦略 | 全技術のE段階マトリクス、EACTSの6提言への賛否、日本の償還・デバイスラグ・症例集約・術者数、**自分の施設で次にやること** | 全章の統合 |

---

## 3. エビデンス格付けスキーム（本プロジェクトの中核装置）

各技術に **E0〜E5** を付与し、章末表と第10章マトリクスで一覧する。「未来っぽさ」と「実際の成熟度」の乖離を可視化するのが狙い。

| 段階 | 定義 | 例（暫定） |
|---|---|---|
| **E0** | 概念・in vitro・動物のみ | 完全なex vivo組織工学弁 |
| **E1** | First-in-human / 症例集積（n<50、短期） | ポリマー僧帽弁（Tria）1年 |
| **E2** | 単施設の中期成績（n≧100 or 5年） | 経腋窩AVR 1,000例、HAART |
| **E3** | 多施設前向き/大規模レジストリ | ARISE、AVIATOR、脱細胞化20年 |
| **E4** | RCT または ガイドライン収載 | MIMVS、VSARR（GL収載） |
| **E5** | 標準治療として定着 | bileaflet機械弁、stented生体弁 |

**併記する3軸**：
- **普及の壁**（技術難度／施設症例数／学習曲線） … Goversの「年12例」のような閾値があれば数値で
- **日本での可用性**（薬事承認の有無・保険償還区分・実施施設）
- **反証の有無**（その技術に対する否定的データ。**必ず探しに行く**。HAART×Yokoyamaのような対が理想）

**🔮 私の見立て**は独立ブロックにし、HTMLでは色分けして「引用ではない」ことを一目で示す。

---

## 4. 実行フェーズ

### P0. シード分解（**完了済み** 2026-07-26）
- [x] PDF取り込み・`pdf_text/ezag185.txt` 抽出
- [x] 主張15項目の分解と検証ポイント列挙 → `md/seed_ezag185_notes.md`
- [x] 引用25本の必読リスト化
- [x] 図4点をPDFから抽出（300 dpi）
- [x] 本論文が扱っていない空白8項目の特定

### P1. 引用25本の一次文献確認（最優先・ここが土台）
- 25本すべてのDOI/PMIDを確定（CrossRef＋PubMed）→ `tables/seed_refs.csv`
- **フルテキスト入手**：OA→直接DL、非OA→OUP/Elsevierは **Playwright経由**（curlは403）、それでも不可なら抄録＋二次引用で扱い、**その旨を明記**
- PDFは `pdf/` に `YYYY_Author_Journal_Topic-Hyphenated.pdf` 命名で保存（[[reference_all_papers_library]] の規約に合わせる）
- **図はこの時点でまとめて抽出**（後述§図の方針）
- 各文献を `md/refs/` に1ファイル1本のノート（n・デザイン・追跡・主要数値・限界）

**優先順位**（時間が足りない場合はここから）：
1. ref[19] De Paulis, Eur Heart J 2025 AV形成の現況 ← 二次資料として最重要
2. ref[5] Sarikouch 脱細胞化20年（EJCTS 2026）
3. ref[12] AVIATOR VSARR PSM
4. ref[23] Tria ポリマー弁 JACC 2025
5. ref[11] 経腋窩AVR 1,000例
6. ref[6] ARISE 5年
7. ref[24][25] Ozaki
8. 残り

### P2. 系統検索による拡張（各章の穴埋め）
章ごとにPubMed/CrossRefで検索。**Editorialの引用が古い箇所（ref[7]2008, ref[8]2011, ref[18]2010）は必ず現代データで更新する**。

```
# 例
"minimally invasive mitral valve surgery"[tiab] AND (2021:2026[dp]) AND (registry OR "propensity" OR meta-analysis)
("decellularized" AND ("homograft" OR allograft) AND valve) AND 2020:2026[dp]
("polymeric" OR "polymer") AND ("heart valve" OR "valve prosthesis") AND 2020:2026[dp]
("Ozaki" OR "aortic valve neocuspidization" OR AVNeo) AND 2018:2026[dp]
"Ross procedure"[tiab] AND (2020:2026[dp]) AND (survival OR durability OR registry)
("valve-sparing" OR "valve sparing") AND ("root replacement") AND 2020:2026[dp]
("aortic valve repair") AND (annuloplasty OR HAART OR ring) AND 2018:2026[dp]
```
**忘れずに**：
- **ガイドライン**：2025 ESC/EACTS 弁膜症GL ＋ **2026年7月号の正誤表（ezag193）**、EACTS/STS 大動脈GL＋正誤表（ezag194）
- **登録/試験**：ClinicalTrials.gov で living valve / polymer valve / decellularized の進行中試験を拾う（＝「まだ結果が出ていない未来」の在庫確認）
- **日本**：JCVSD、PMDA承認状況、保険償還（Ozaki・脱細胞化・ロボットAVR）

### P3. エビデンス格付けと表の作成
- `tables/technology_evidence_matrix.csv`（技術 × E段階 × 反証 × 日本可用性 × 出典DOI）
- `tables/seed_claims_verification.csv`（Editorialの主張15項目 × 裏取り結果 × 判定：支持／条件付き／反証あり）
- `tables/ongoing_trials.csv`

### P4. 日本の文脈（この章が本ページの差別化点）
- 承認/償還されているか、実施可能か、症例数は足りるか
- 日本発の系譜（Ozaki、Kasaharaハイブリッド生地、根本慎太郎、須磨RGEA的な「着想→検証」の型）
- 症例集約の議論（Govers ≥12例/年 を日本の施設分布に当てはめると何が起きるか）

### P5. 執筆
- `md/FutureOfValveSurgery_integrated_review.md`
- 1章あたり 3,000〜6,000字目安、全体で 40,000〜60,000字（AF レビューの1/3規模）
- **必ず入れる**：各章冒頭に3行サマリ、章末にE段階表と🔮見立て、数値は必ず出典DOI付き

### P6. 図・HTML化・公開
- 図の配置（§図の方針）
- `python3 convert_to_html.py md/... output/future_valve_surgery_review.html`
  （検索機能が要るなら `robotic_cpb/build_html.py` パターンを流用）
- `index.html` の **大動脈弁セクション**に card 追加＋count更新。**MDとHTMLの両方をcommit**（片方だけだとPages 404）

### P7. 検証（`superpowers:verification-before-completion` 相当）
- **数値照合2段スクリプト**（AFレビューで確立した手法）：①本文の全数値トークンを抽出しソースと突合 ②同一行共起チェック
- 全DOIをCrossRefで個別検証 → `output/doi_verification_future_valve.md`
- 図のライセンス一覧表を作り、公開版に非OA図が混入していないことを機械チェック
- Playwrightでlocalhost配信してレンダリング確認（file://は不可）

---

## 5. 図の方針（2026-07-26 指示：**自作SVGは作らない**）

**原則：論文PDFから実図をそのまま切り出して使う。自作のSVG・模式図・「わかりやすい概念図」は一切作らない。**

### 使うツール：`guideline-figure-extraction` スキル（P6ではこれを使う）

このリポジトリには専用スキルがあり、**まさにこの用途（原典PDFから図表を切り出して .md と .html の対に埋め込む）** のために
作られている。**P6では自前スクリプトを書かず、必ずこのスキルを起動する**（`Skill: guideline-figure-extraction`）。

スキルの鉄則と手順（要点）：
- **鉄則**：原典に図が無いなら「無い」と書く。**穴埋めのための自作図は禁止**（本人指示と完全に一致）
- 手順：`inventory.py`（図表の棚卸し・密度スイープ）→ `render.py`（**分数グリッド付き**プレビュー）→ `figcrop.json` を書いて `crop.py` → `config_template.py` を写した `figconf.py` で `inject.py --check` → 本実行
- **矩形はピクセルではなく分数で読む**（プレビューは表示時に縮尺が変わるため、ピクセル指定は必ずズレる）。crop は **dpi=200**
- 段組・ページをまたぐ表は `parts` で上下連結し、その旨をキャプションに書く
- キャプションは「図が示すもの」ではなく「**読者がその画像で検証できる値**」を書く（閾値・クラス・原文の一文）
- `inject.py` が 図表一覧・著作権注記・ライトボックス・TOCまで生成する
- 検証は `python3 -m http.server` ＋ Playwright（`file:` はMCPでブロック）。**`loading="lazy"` のままだと `naturalWidth===0` で誤判定**するので `loading='eager'` にしてから確認

### 補助手段（スキルの前段として使ってよい）

シード論文のように**図が丸ごと埋め込み画像として入っている場合**は、`pdfimages` の方が速く高品位に取れる
（実際に ezag185 は 300 dpi・背景なしで4点とも抽出できた）。ベクタ描画の図はスキルの `render.py`＋`crop.py` を使う。

```bash
pdfimages -list paper.pdf                       # 図の点数と解像度を確認
pdfimages -j -p paper.pdf figures/<slug>        # 埋め込み画像をそのまま抽出
```

- 抽出後は **必ず目視**して、図番号・内容と一致する名前に改名（`<slug>_figN_<内容>.jpg`）
- **図だけ貼らない**。原文キャプション＋日本語の短い解説を必ず添える
- `tables/figure_credits.csv` に **図ごとに 出典DOI / ライセンス / 公開可否** を記録

### ライセンスの扱い（2系統ビルド）
`output/` はGitHub Pagesで**公開**される。したがって：

| 論文のライセンス | 扱い |
|---|---|
| **CC BY / CC BY-NC(-ND)** | 出典・ライセンス明記のうえ **公開HTMLに埋め込む**（AFレビューで確立した運用） |
| **非OA**（本シード論文 ezag185 を含む） | **公開版には入れない。** `figures_local/` に置き `.gitignore` して**ローカル閲覧用ビルド**にのみ埋め込む。公開版は「Fig.1（DOIリンク）参照」の形にする |

→ `.gitignore` に `future_cardiac_surgery/figures_local/` と `*/pdf/` を追加すること。
→ **代替探索**：非OA図の内容がどうしても必要な場合、同等の図をOA論文から探す（P6で実施）。

---

## 6. 成果物一覧

```
future_cardiac_surgery/
  RESEARCH_PLAN.md                    ← 本ファイル
  HANDOFF.md                          ← 次セッションの入口
  pdf/                                ← 原著PDF（.gitignore対象）
  pdf_text/                           ← pdftotext出力
  md/
    seed_ezag185_notes.md             ← 完了
    refs/<author>_<year>.md           ← P1で1本1ファイル
    FutureOfValveSurgery_integrated_review.md  ← 本体
  tables/
    seed_refs.csv
    seed_claims_verification.csv
    technology_evidence_matrix.csv
    ongoing_trials.csv
    figure_credits.csv
  figures/                            ← 公開可（OA）図
  figures_local/                      ← 非OA図（.gitignore）
  output/                             ← ビルド用一時（最終HTMLはリポジトリ直下 output/ へ）
```

最終HTML: `output/future_valve_surgery_review.html`
検証ログ: `output/doi_verification_future_valve.md`

---

## 7. 品質基準（ここを下回ったら未完成）

1. **Editorialの主張15項目すべてに裏取り判定**（支持／条件付き支持／反証あり／検証不能）が付いている
2. 本文の**すべての数値に出典DOI**があり、機械照合を通っている
3. 各技術に**E段階と反証の有無**が付いている（反証を探した形跡があること。「見つからなかった」も記録）
4. **🔮見立てと引用が視覚的に分離**されている
5. 図は**すべてPDF由来の実図**で、ライセンス表があり、公開版に非OA図が混入していない
6. 既存レビュー（small_annulus_avr / aae_technique_atlas / valve durability / robotic_cpb / cor_knot）と**重複せずリンクしている**
7. 第10章に**日本での実行戦略**が具体的に書かれている（「〜が期待される」で終わらせない）

---

## 8. 想定作業量

| フェーズ | 目安 |
|---|---|
| P1 引用25本の精読 | 1〜2セッション |
| P2 系統検索・拡張（＋30〜60本） | 1〜2セッション |
| P3/P4 格付け・日本の文脈 | 1セッション |
| P5 執筆 | 2〜3セッション |
| P6/P7 図・HTML・検証 | 1セッション |

**次セッションは P1 から。** 詳細は `HANDOFF.md`。
