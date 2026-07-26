# robotic_technique — 引き継ぎ

最終更新 2026-07-27

## 状態：**完成**

ロボット心臓手術の**術式手技**レビュー（Port配置・訓練・術式別Pitfall/Tips・展望）。

- [x] 文献サーベイ（PubMed 22クエリ → 4,894 → 1,652 → 選定）
- [x] **75本を手元に確保**（PDF 58 / MMCTS本文 9 / 抄録のみ 6）
- [x] 設計 → `docs/superpowers/specs/2026-07-26-robotic-cardiac-technique-review-design.md`
- [x] **本文 全9章＋付録A/B/C 執筆完了** → `md/robotic_technique_review.md`（約107,000字）
- [x] **原典 Figure 46点**を抽出・挿入（`figures/` → `output/figures/rt_*.png`）
- [x] HTML化 → `output/robotic_technique_review.html`（351 KB）
- [x] `index.html` の「体外循環・周術期」sectionにカード追加（3件→4件、ヘッダ統計12→13）
- [x] 検証：図46/46・404ゼロ・デッドアンカーゼロ・横スクロールゼロ（PC/モバイル）
- [x] 数値照合 stage1 **0件**・DOI/PubMed/MMCTS **159リンク**すべて到達確認

残っているのは **git push のみ**。

## 成果物

| ファイル | 内容 |
|---|---|
| `md/robotic_technique_review.md` | 本文（真実の源）。付録A動画一覧／B略語集／C図表一覧／引用文献75本を内包 |
| `output/robotic_technique_review.html` | 公開用。convert_to_html.py で生成（3階層サイドバー付き） |
| `output/figures/rt_*.png` | 掲載図46点（`rt_` 接頭辞で他レビューと衝突回避） |
| `figures/*.png` | 抽出した原図（`output/figures/` へのコピー元） |
| `inject_figs.py` | 図の配置・キャプション・出典・図表一覧の生成。**冪等**（再実行で置換） |
| `build_refs.py` | PubMed から引用文献表を生成 → `corpus/references.md` |
| `mmcts_fetch.py` | **MMCTS を curl だけで取得**（下記参照） |
| `verify_numbers.py` | 数値の2段照合 |
| `reading/*.txt` | 精読用コーパス（参考文献・所属を落として圧縮、約1.4MB） |

## 再生成の手順

```bash
python3 robotic_technique/inject_figs.py            # 図と図表一覧を再注入
python3 convert_to_html.py robotic_technique/md/robotic_technique_review.md
cd robotic_technique && python3 verify_numbers.py   # 数値照合
```

## 今回の技術的発見（次に効くもの）

### MMCTS は curl だけで取れる — Playwright 不要
mmcts.org は Laravel/Inertia の SPA で、curl では殻しか返らないように見えるが、
**記事本文（step-by-step の `video_sections` を含む）は `<div id="app">` の
`data-page` 属性に JSON で埋まっている**。`mmcts_fetch.py` がこれを展開する。
DOI からも引ける（`python3 mmcts_fetch.py 10.1510/mmcts.2025.065 out.md`）。

### NCBI ID converter は移転済み
`ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/` は **301**。
現行は `https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=…&format=json`。
（レスポンスの `pmid` が **int** な罠は従来どおり）

### Elsevier / SAGE は Playwright でも抜けない
ScienceDirect は headless Chrome でも captcha。**OA hybrid でも同じ**。
Europe PMC も "Subscription required" を返す。→ 購読誌は**抄録のみ引用**に切り替え、
本文に「※抄録のみ引用（本文未取得）」を明示する運用にした（6本）。

### PDF から図を取るときの落とし穴
- `extract_images.py list` の **xref 順は誌面の Figure 番号順とは限らない**。
  Wei RAVR は Fig 7 が A/B の2画像なので、以降が1つずつずれた。**必ず目視で確認**する。
- **Mick「steps to success」の "300dpi 図版11枚" は誤り** — 実体は
  Video 1–11 の1コマ目（da Vinci の器械バーUIが写り込んでいる）。
  設計方針「動画のコマ取りはしない」に反するので**本文には不採用**とし、付録Aの動画リンクに回した。
- **Algoet の Figure 5・6 は他誌からの転載**（"Cited from Cerny et al." / "Göbölös et al."）→ 使用不可。

### DOI は推測せず PubMed から取る
Arai の DOI を巻号から推測して `10.1016/j.xjtc.2025.11.021` と書いたが **404**。
正しくは `10.1016/j.xjtc.2025.102169`。**publisher の 403 と実在しない DOI の 404 は区別する**
（OUP/SAGE/MDPI/Cureus/Wolters Kluwer は HEAD を 403 で弾くので、
CrossRef API `api.crossref.org/works/<doi>` で実在確認する）。

### 数値照合スクリプトの注意
OUP（EJCTS/ICVTS）は**桁区切りが空白**（`13 731`）。
正規表現で拾う前に `(?<=\d) (?=\d{3}\b)` を潰さないと未一致が出る。

## 未回収文献（阪大ローカル等で要検討）

| PMID | 内容 | 現在の扱い |
|---|---|---|
| 39672523 | ロボット僧帽弁の同時手術 総説（Semin Thorac Cardiovasc Surg） | 7.6 で抄録引用 |
| 41690664 | ロボットMV形成 + on-pump CABG to LAD（国循） | 7.4(c) で抄録引用 |
| 40750037 | TAVR explant + ロボットAVR | 5.8 で抄録引用 |
| 40913323 | ポートサイト出血のバルーンtamponade | 4.6(b) で抄録引用（数値は抄録に全部ある） |
| 41622650 | hinotori 両側IMA採取（人屍体） | 9.2 でタイトルのみ |
| 37753828 | 安価なTECABシミュレータ | 9.3 で抄録引用 |

いずれも**抄録で本文の主張は成立している**。本文取得できれば手技の細部を足せる。

## 設計判断（再議不要）

- **ポート配置は独立章にせず術式別**（第2.4節に比較表、各術式章の冒頭に専用節）
- **図は原典 Figure のみ／自作SVG禁止／動画のコマ取り禁止／動画は▶リンクのみ**
- **既存 robotic_cpb レビューと分担** — 送脱血・endoballoon・灌流・麻酔は既存に委ね相互リンク
