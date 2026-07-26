# Ross手術 手技レビュー — HANDOFF

**目的**: Ross手術の**術式バリエーション・Pitfall/Tips・ラーニングカーブ**に絞った、図表が豊富な How-to まとめHTML。
**姉妹プロジェクト**: `/Users/k.tonai/Documents/Cardiac_Surgery_Guidelines/Ross_Procedure/`（EACTS 2025 Ross Consensus を中核としたガイドライン比較。適応・患者選択はそちらが担当）

**最終更新**: 2026-07-27（**P4完了＝レビュー完成**）

---

## 現在の状態 — 全フェーズ完了

- [x] P0: 文献ピックアップ（PubMed候補1,558本 → 67本）→ `md/paper_pick_list.md`
- [x] P1: 全67本の入手・rename・格納
- [x] P2: 精読・章立てドラフト → `md/00_outline_draft.md` v0.2
- [x] P3: 図・動画の収集（**CCライセンス図 76点をPMCから取得・全図目視確認**）
- [x] P4: 本文執筆＋HTML生成（**124,949字・全12章＋付録5本**）

### 成果物

| 種別 | パス |
|---|---|
| **公開HTML** | `output/ross_technique_review.html`（289 KB） |
| 統合MD（ビルド生成物） | `md/Ross_Technique_Review.md` |
| 章ごとのソース | `md/parts/00_front.md` … `13_back.md`（**編集はここ。統合MDは触らない**） |
| 図（76点） | `figures/ross_*.jpg` → ビルド時に `output/figures/` へコピー |
| 略語集（73項目） | `glossary.json` |
| indexカード | `index.html` の `#aortic` セクション先頭（大動脈弁 8件・トピック計12） |

### ビルド

```bash
python3 ross_technique/build.py       # parts結合 → 図表一覧/文献リスト生成 → HTML
```

- `build.py`: `md/parts/*.md` をファイル名順に結合。`<!--FIGINDEX-->` を図表一覧テーブルに、`<!--REFLIST-->` を `paper_pick_list.md` から生成した文献リスト（PubMed/PMC/DOIリンク付き）に置換。`<span id="figcount">` / `<span id="vidcount">` も実数に置換。最後に画像の存在チェック
- `build_html.py`: ルートの `convert_to_html.py`（CSS・callout・pandoc）＋ `af_surgical_ablation/build_html.py`（全文検索・TOC・略語集ポップアップ）を再利用し、図カード（`figure.gfig`）・動画カード（`figure.vfig`＋▶バッジ）・ライトボックス・`<img>` への width/height 自動付与を追加
  - ⚠️ **AF側の `SCRIPT` は h2/h3/h4 しか拾わない**ため、本レビュー（章＝h1）向けに `TOC_SCRIPT` で h1 を追加する差分パッチを当てている。AF側を書き換えると `assert` で落ちるので、その時はパッチを見直す

### 検証済み（2026-07-27）

localhost配信＋Playwright/Chrome headlessで確認（`file://` はPlaywright MCPで不可）:
- 画像76点すべて読み込み成功（`loading="lazy"` のため **eager に変えてから** naturalWidth を見る）
- 内部アンカー切れ 0／横スクロール 0（テーブルは `.table-wrap` 内で個別スクロール）／モバイル390px幅も破綻なし
- ライトボックス開閉・略語集73項目・全文検索（ヒット数＋前後移動）が動作
- 外部リンク177本を `curl` で確認。403はOUP/Elsevier/AHA/MDPIのbot遮断（ブラウザでは開く）。**Nappi 2024の `10.52198/...` は真の404**なので `build.py` の `DEAD_DOI` でリンクを外している

---

## 図・動画の方針（実装済み）

### 図は「PMCのCCライセンス論文」からのみ

`harvest_figs.py meta` → `figure_index.json`（各図のラベル・キャプション・ライセンス・cdn blob URL）→ `figs_selected.json` で採用図を宣言 → `harvest_figs.py get` でダウンロード。

**ハマりどころ**
- **urllib は「Checking your browser - reCAPTCHA」のスタブを返す。curl＋ブラウザUAなら通る**（`harvest_figs.py` は全fetchをcurl経由にしている）
- 画像バイトは `cdn.ncbi.nlm.nih.gov/pmc/blobs/...` にしか無い。記事HTMLから拾う（`/articles/PMCxxx/bin/...` は404 HTMLを掴む）
- **キャプションはEurope PMCの `fullTextXML` が確実**（`https://www.ebi.ac.uk/europepmc/webservices/rest/PMCxxx/fullTextXML`）。ただし **Ann Cardiothorac Surg はEurope PMCにXMLが無い**ので、PMC記事HTMLの `<figure class="fig...">` を直接パースする（`index_html_figs.py`）
- PMC OA subset（`oa.fcgi` → oa_package tar.gz）は **ACSも著者原稿も対象外**で使えなかった。かつhttps経路が404（ftpも550）。この道は捨てた

**除外したもの**（`付録C` に理由を明記済み）: Zhu JTCVS 2023 Fig 1（NIH author manuscriptでCCライセンス無し）、Skillington JTCVS 2015 Fig 1-3／Mazine ATS 2018／Matsushima ATS 2019／Myjavec EJCTS 2024／Basmadjian JTCVS 2016／Caldaroni JTCVS 2025（いずれも非OA）、EACTS Consensus Figure 2-10（ガイドライン側と重複するため）。
**Sievers 2010 JTCVS の online E-Appendix（subcoronary 全工程 Figure E1-E9）は依然未入手** — 第2章の図が薄い唯一の原因。入手できれば最優先で追加する。

### 動画は「サムネイル画像＋原典へのハイパーリンク」

Ann Cardiothorac Surg の動画はPMCに**サムネイル（タイトルスライド）画像が置かれている**ので、それを図として貼り、画像自体をDOIリンクにして▶バッジを重ねた（13点）。MMCTS 7本は購読制でサムネイルが取れないため、`.videolist` のテキストリンクにしている。JTCVS系の動画リンクは **PII（`S2666-2507(25)00138-5` 等）を記事HTMLから実測して確認済み**（推測すると間違える）。

---

## 内容面のメモ（次に手を入れるとき）

- **数値の齟齬は本文で明示的に処理した**: Liebrichの生存率（Abstract 20年92% は誤記。Results本文の 5年97%/15年92%/20年86% を採用）、Sievers subcoronary 除外基準（同一論文内に >31mm と >32mm）、Skillington 目標径（JTCVS 2015: 男24-26 / ACS 2021: 男24-25）
- **原著と照合済みの主要数値**: Starnes SHR 0.28、Sievers 2018（20年生存73.1%・再手術回避85.9%・VPC）、Tagliafierro（9.46/6.73/1.8%, P=0.003・Early=各術者の最初69例）、Réa（15年再手術 1.2% vs 6.8%）、Chauvette（HR 3.1）、Caldaroni（25年 85.3%/89.5%、AR 78.0%）、Stephens（105例・84%他施設・25%が4回目以上・早期死亡5%・同時手技の内訳）、Zhu ACP（開閉速度・力）、Shih（186 vs 48）、Skillington 2015（62.4%/49.4%・34.0→34.7mm）、Charitos（HR 2.4 と術前純AR HR 2.3）、Scorsese（米国2022年の導管83%超がhomograft）
- **本文で立てた軸**: ①失敗は術式選択でなく実装精度 ②補強の必要性は決着・方法は未決着 ③失敗は弁輪/洞/STJの3レベルで別々に起こる ④ラーニングカーブ75-100例。第11章に**11の対立点**＋決着済み10項目＋未解決6項目
- **まだ書けていない**: EACTS Consensus本文（ガイドライン側担当）、抄録のみ6編の手技記載、本邦データ（Kawamura 2026以外）

---

## 資料の置き場所

| 種別 | 場所 | 本数 |
|---|---|---|
| PDF | `~/Documents/All Papers/Clinical/Valve/` | 53 |
| 精読用テキスト | `pdf_text_clean/`（.gitignore済み） | 57 |
| MMCTS本文クリップ | `md/mmcts/` | 7 |
| 抄録のみ | `md/abstracts/` | 6 |
| PMC記事HTML／Europe PMC XML キャッシュ | `corpus/pmc_html/`, `corpus/epmc_xml/` | 34 / 20 |
| 文献リスト | `md/paper_pick_list.md`（67本・章別・PMID付き） | — |
