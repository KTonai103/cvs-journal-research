# ロボット心臓手術 手技/Pitfall/Tips レビュー — 設計

作成 2026-07-26 / 対象ディレクトリ `robotic_technique/`

## 目的

ロボット心臓手術を「これから始める / 症例を増やす」術者が、**術式ごとに**
ポートをどこに置き、どう訓練し、どこで失敗するかを引ける図表中心の HTML。

## 成果物

| ファイル | 内容 |
|---|---|
| `robotic_technique/md/robotic_technique_review.md` | 本文（真実の源） |
| `output/robotic_technique_review.html` | 公開用（GitHub Pages） |
| `robotic_technique/figures/*.png` | 原典から切り出した図 |
| `robotic_technique/figconf.py`, `figcrop.json` | 図の再切り出し用設定 |
| `index.html` | 体外循環セクションにカード追記 |

## ソース

手元 59 本（PDF 48 / MMCTS 本文 8 / 抄録のみ 3）。`corpus/download_list.json`
と `corpus/link_inventory.json` に PMID・DOI・PMC・動画URLを保持。

第7章（複合弁）を追加したため 10 本を追加取得（`md/download_list_combined.md`）。

### 今後の課題 — 未回収文献

阪大のローカルアクセスで取得可否を検討する。取れなくても各章は成立する。

| PMID | 内容 | 効く節 |
|---|---|---|
| 39434978 | Cx領域の展開技法（PMC無料・単純な取り逃し） | 6.3 |
| 40547428 | RAVR 側方アプローチの視野最適化（PMC無料・同） | 5.2 |
| 39672523 | ロボット僧帽弁の同時手術 総説 | 7章全体 |
| 40799111 | MMCTS rapid deployment AVR + MV の step-by-step | 7.2 |
| 41690664 | ロボットMV形成 + on-pump CABG to LAD（国循） | 7.4 |
| 40750037 | TAVR explant + ロボットAVR | 5.5 / 9.4 |
| 40913323 | ポートサイト出血のバルーンtamponade（抄録+ビジュアルアブストラクトのみ手元） | 4.6 |

## 決定事項

### D1. ポート配置は独立章にしない — 術式別に置く

初期案では「ポート配置」を1章にまとめていたが、実データで術式ごとに
**胸腔の左右・肋間・ドッキング方向がすべて違う**ことが確認された。
共通するのは「前腋窩線を基準にマーキングする」「Veress針でCO2を入れてから
最初のトロカールを置く」という手順の型だけ。よって:

- 第2章に**共通の型のみ**（患者選択の解剖閾値、術前CTで見る項目、体位とマーキング、CO2）
- ポート配置図・表は**第4〜7章の各術式の冒頭**に置く

### D2. 図は原典 Figure のみ。動画は ▶ リンクのみ（ユーザー承認済み）

動画からのコマ取りはしない。`paper-figure-extraction` スキルの鉄則に従い
自作 SVG も作らない。図がない論文は動画リンクとテキストで構成する。

**図0本と実測確認済みの15本**（`corpus/fig_availability.json`）:
Bonatti(末梢吻合)/Kitahara(RAVR)/Algoet(トロカール流派)/Loulmet(MAC×2)/
Gillinov/Pickering/Darehzereshki/Jonsson/Bonatti(単孔式)/Balkhy(TECAB)/
DeLay/Podgorsek/Dorsey/Badhwar — ACS・JTCVS Tech の本文＋動画記事。

Mick「steps to success」はキャプションが "Video 1–11" だが**300dpi の誌面図版を
11枚保持**しているため図として使用可。

図の在庫: 図 123 / 表 82 / 動画 26（32論文）。章立て確定後に必要分のみ切り出す。

### D3. 動画リンクの解決順

1. MMCTS → md frontmatter の `mmcts.org/tutorial/NNNN`（動画ページ直リンク）
2. それ以外 → DOI（動画が埋め込まれた論文ページ）
3. PMC 無料のものは PMC リンクも併記（supplementary の保険）

59本中 48本が動画付き見込み。付録に術式別の動画一覧を置く。

### D4. 既存 robotic_cpb レビューとの分担

送脱血・endoballoon・カニュレーション・麻酔・灌流は既存レビューに委ね、
本レビューは術式手技に集中。第1章から相互リンクする。

## 章立て

```
1 総論
  1.1 プラットフォームと現況（国内含む）
  1.2 エビデンスの現在地 — MV / CABG / AVR で成熟度が違う
  1.3 本レビューの範囲と robotic_cpb への導線

2 共通の土台（術式に依らない部分だけ）
  2.1 患者選択の解剖学的閾値
  2.2 術前CTで何を見るか
  2.3 体位・マーキング・CO2 の型
  2.4 ポート配置は術式別 → 4〜7章への導線

3 訓練とプログラム構築
  3.1 STS training pathway（Phase I–III）
  3.2 シミュレーション（wet lab / 自作シミュレータ / 運針マップ）
  3.3 ラーニングカーブの実数 — 術式別の必要症例数
  3.4 プログラム立ち上げの実務
  3.5 胸骨正中切開への転換 — guardrails

4 僧帽弁形成
  4.1 ★ポート配置（標準 / 極端に薄い / 女性）
  4.2 展開 — 左房切開と LA retractor
  4.3 弁形成手技
  4.4 弁輪縫縮
  4.5 難症例（MAC / Barlow / TEER後 / redo）
  4.6 Pitfall（Cx損傷 / ポート出血 / 左房縫合線 / 心筋保護）

5 大動脈弁（RAVR）
  5.1 ★ポート配置と右側方アクセス
  5.2 大動脈切開・弁の出し方・視野最適化
  5.3 弁選択（rapid deployment / sutured）と縫合器
  5.4 併施（弁輪拡大 / 心室中隔心筋切除）
  5.5 現況と限界

6 冠動脈（TECAB / MIDCAB）
  6.1 ★ポート配置 — RA-MIDCAB と TECAB の違い
  6.2 IMA採取（skeletonized / clipless / ランドマーク / BITA）
  6.3 標的血管の展開（LAD / Cx領域 / 後壁枝）
  6.4 吻合
  6.5 on-pump か off-pump か
  6.6 Pitfall（正中転換のリスク因子とタイミング）

7 複合弁・同時手術
  7.1 ★ポート配置 — 1つの胸腔で2弁を扱う（dual-camera 戦略）
  7.2 AVR + MV（経大動脈的 vs 経左房、順序、遮断時間）
  7.3 MV + TV（三尖弁を足すコスト）
  7.4 弁 + 冠動脈（TECAB併施 / on-pump CABG併施 / 単一切開）
  7.5 弁 + 不整脈手術（CryoMAZE・LAA）
  7.6 どこまで足せるか — 適応の線引き

8 Others
  8.1 ★ASD・心房中隔
  8.2 心房腫瘍
  8.3 ★不整脈・左心耳（右胸 vs 左胸epicardial、閉鎖不完全の評価）
  8.4 三尖弁・房室弁（単独）
  8.5 再手術（癒着剥離の入り方）

9 展望
  9.1 単孔式（da Vinci SP）
  9.2 国産機 hinotori
  9.3 AR/MR・AI
  9.4 何が足りないか

付録  動画一覧（術式別） / 図表一覧 / 引用59本 / 略語集
```

## HTML 実装

`convert_to_html.py` を再利用（`fix_cjk_emphasis` 依存）。追加要素:

- 3階層サイドバー目次（章→節→図表）— `feature_html_sidebar` の実装
- 図カード: 図全体が原典リンク、右下に ▶ 動画バッジ、下部に出典クレジット
- lightbox（`paper-figure-extraction` の assets）
- 全文検索（`robotic_cpb/build_html.py` の実装を流用）
- 略語ポップアップ（AF レビューの `glossary.json` 方式）
- 図表一覧と著作権注記（個人参照用）

## 検証

`python3 -m http.server` で配信して Playwright で確認（`file:` は不可）:
図の枚数、404ゼロ、lightbox 開閉、横スクロールなし、動画リンクの到達、
サイドバーのアンカー解決。画像は `loading='eager'` にしてから
`naturalWidth` を assert する。

## やらないこと

- 自作 SVG / 概念図
- 動画からのコマ取り
- CPB・麻酔・灌流の詳述（robotic_cpb に委ねる）
- カテーテル系ロボット（magnetic navigation 等）
