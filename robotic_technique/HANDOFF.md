# robotic_technique — 引き継ぎ

最終更新 2026-07-26

## いまどこ

ロボット心臓手術の**術式手技**レビュー（Port配置・訓練・術式別Pitfall/Tips・展望）。
最終成果物は図豊富なHTML。

- [x] 文献サーベイ（PubMed 22クエリ → 4,894 → 1,652 → 選定）
- [x] **69本を手元に確保**：PDF 58 / MMCTS本文 8 / 抄録のみ 3
- [x] 設計確定 → `docs/superpowers/specs/2026-07-26-robotic-cardiac-technique-review-design.md`
- [x] 図の在庫棚卸し（`corpus/fig_inventory.txt`、図0本の論文は `corpus/fig_availability.json`）
- [x] **本文 第1〜3章を執筆済み** → `md/robotic_technique_review.md`
- [ ] 第4〜9章の執筆 ← **次はここ**
- [ ] 図の切り出し（`figcrop.json` / `figconf.py` → `inject.py`）
- [ ] HTML化・index.html 追記・検証
- [ ] commit / push

## 次セッションの最短の入り方

1. `md/robotic_technique_review.md` を読む（第1〜3章が完成、4章以降は見出しのみ）
2. `docs/superpowers/specs/2026-07-26-*-design.md` の章立てに従って続ける
3. 精読は `reading/*.txt`（参考文献・所属を機械的に落として圧縮済み。全部で約1.2MB）
   - 圧縮スクリプトは `strip.py`。PDF追加時は `pdftotext` → `python3 strip.py`
4. 図は**章立てに沿って必要分だけ**切り出す（在庫123枚超あるが40〜45枚に絞る方針）

## 確定した設計判断（再議不要）

### ポート配置は独立章にせず、術式別に置く
実データで胸腔の左右・肋間・ドッキング方向がすべて違うことを確認済み。
共通なのは「前腋窩線基準でマーキング」「Veress針でCO2を入れてから最初のトロカール」の2点だけ。
→ 第2.4節に比較表、各術式章の冒頭に専用ポート節。

### 図は原典 Figure のみ／動画は ▶ リンクのみ（ユーザー承認済み）
動画のコマ取りはしない。自作SVGも禁止（`paper-figure-extraction` スキルの鉄則）。
リンク解決順：MMCTS は md frontmatter の `mmcts.org/tutorial/NNNN` → それ以外は DOI → PMC も併記。

### 既存 robotic_cpb レビューと分担
送脱血・endoballoon・灌流・麻酔は既存に委ね、本編は術式手技のみ。相互リンク。

## 図のあり所（重要）

**図0本と実測確認済みの15本**（`corpus/fig_availability.json`）は ACS/JTCVS Tech の
本文＋動画記事。動画リンクとテキストのみで構成する。
含まれるもの: Bonatti(末梢吻合) / Kitahara(RAVR) / **Algoet(トロカール流派)** /
Loulmet(MAC×2) / Gillinov / Pickering / Darehzereshki / Jonsson / Bonatti(単孔式) /
Balkhy(TECAB) / DeLay / Podgorsek / Dorsey / Badhwar

**逆に図が主軸になるもの**:

| 章 | 図の主軸 | 枚数 |
|---|---|---|
| 4 僧帽弁 | Hage(標準vs薄い患者のポート図＋Table 1) / Mick(300dpi図版11枚、キャプションは"Video N") / Czesla(Fig 3-4 = Cx–弁輪距離) | |
| 5 **AVR** | **Wei_2025_RAVR_Beyond_Isolated_Multivalve_Platform_ACS = 11枚の連続手技図**（体位→ポート/ドッキング→大動脈切開→弁切除→弁輪脱灰→人工弁→閉鎖→弁輪拡大） | 11 |
| 6 冠動脈 | Wertan(step-by-step 10枚) / Algoet_MIDCAB_to_TECAB(Fig 3-4 = 術式別切開線) | |
| 7 複合弁 | **Arai(Fig1=TECAB用ポート, Fig2=MV用ポート／同一患者)** / Goto(dual-camera port setup) / Wei_NTUH(Fig1 set-up, Fig2 弁の展開) | |
| 8 Others | Agnino(AFアブレーション9枚) / Kim(ASD 6枚) / Nakamura(心筋腫) | |

Algoet_MIDCAB_to_TECAB の **Figure 5・6 は他誌からの転載**（"Cited from Cerny et al."
"Cited from Göbölös et al."）なので**使用不可**。

## 本文で使う主要数値（第4章以降で再利用）

**Gillinov 患者選択**: 胸骨後面〜脊椎 ≥10cm 理想 / 7–10cm はカメラで実測 / <7cm 正中切開。
大腿動脈 ≥7mm、6mm前後は8mmグラフト縫着、<6mm 正中。最初の1,000例 死亡0・形成率99%。

**STS Phase 0**: 冠動脈=CABG通算250例（うちOPCAB 10）/ 心内=僧帽弁75例（うち40例は直近2年）
＋小開胸末梢CPB 15例、形成率≥80%。施設=年250例×3年、OR 70m²、ロボット枠 週1–2日（最低月2回）。
**Phase II**=最初10例を6ヶ月以内にO/E≤1 / **Phase III**=50例 / **Phase IV**=50例以上でTECAB・多弁・RAVRへ拡大。
工程別目標時間は本文 3.5 に表で記載済み（「目標の半分を目指せ」という但し書きも）。

**争点3つ**（第2.5節に表で記載済み）: 中等度AR / 重症MAC / 弁＋冠動脈の同時手術。
加えて endoaortic balloon（Czesla は解離2例で放棄、STS は Phase IV まで待てと明記）。

## 未回収文献 — 阪大ローカルで検討

| PMID | 内容 | 効く節 |
|---|---|---|
| 39434978 | Cx領域の展開技法（**PMC無料**・単純な取り逃し） | 6.3 |
| 40547428 | RAVR側方アプローチの視野最適化（**PMC無料**・同） | 5.2 |
| 39672523 | ロボット僧帽弁の同時手術 総説 | 7章 |
| 40799111 | MMCTS rapid deployment AVR+MV の step-by-step | 7.2 |
| 41690664 | ロボットMV形成+on-pump CABG to LAD（国循） | 7.4 |
| 40750037 | TAVR explant + ロボットAVR | 5.5 / 9.4 |

40913323（ポートサイト出血のバルーンtamponade）は抄録＋ビジュアルアブストラクトのみ手元。
ビジュアルアブストラクトに実数（再開胸率 0% vs 4.7%, P=0.004）があるので 4.6 節は書ける。

Innovations は権利上ほぼ取得不可（ユーザー確認済み）。代替:
ポート出血→Patel/Czesla、シミュレータ→Atroshchenko、hinotori→Bonatti単孔式。

## 落とし穴（踏んだもの）

- **triage の心臓判定は title 限定にする**。abstract 許容だと他科のロボット論文が
  「abstractに cardiac risk と書いてある」だけで大量混入（2,993→title限定で1,652）
- **NCBI ID converter のレスポンスの `pmid` は int**。文字列キーで引くと全件ミスする
- PDF本文中のURLは行折り返しで壊れており機械抽出できない → 動画リンクはDOIを使う
- ACS の "Masters of Cardiothoracic Surgery" は図を持たない記事が多い。
  `extract_images.py list` で**実測してから**図の主軸を決める（キャプション棚卸しだけでは
  Mick のように300dpi図版があるのに0と出る場合がある）
