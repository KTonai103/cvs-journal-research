# HANDOFF — 心臓弁膜症外科の未来（future_cardiac_surgery）

> 最終更新: 2026-07-26 ｜ 状態: **P0〜P7 完了（レビュー本体・図・HTML・検証まで一巡）／git commit は未実施**
> **次にやること: ①commit & push ②残された問い6件の解消（下記§未解決）**

---

## 30秒サマリ

EACTS Innovation Committee の Editorial **「Heart Valve of the Future」**（EJCTS 2026;68(6):ezag185）を
シードに、**その主張15項目を一次文献で裏取りし E0〜E5 で格付け直した包括レビュー**を作った。

- 本体: `md/FutureOfValveSurgery_integrated_review.md`（**全10章・約77,000字・OA図17点**）
- 公開HTML: `../output/future_valve_surgery_review.html`（index.html 大動脈弁セクションに card 追加済・count 6→7）
- 検証ログ: `../output/doi_verification_future_valve.md`（**DOI 88/88 解決・数値照合2段**）

### 結論の骨格（3行）

1. Editorial の15主張のうち**無条件に支持できたのは5項目**。7項目が条件付き、2項目に重要な反証、
   1項目（**AIによる耐久性予測**）は**一次文献が0件**。
2. 最大の論点は **HAART（内側幾何学的リング）**。同じ著者群が2025年 *Eur Heart J* 総説では
   「早期失敗は cusp 組織の摩耗またはリング dehiscence に関連」と書きながら、Editorial では推奨側に置いている。
   そこへ **Yokoyama/Fukuhara 2026（JTCVS）の 44%再介入・5年40.8%** が出た。決着は **CONTOUR trial（NCT06869954, 2027年）**。
3. 日本では**順序が欧州と逆**。ロボット弁置換は2024年度改定で保険適用、Ozaki は保険適用・指定70施設超。
   Ross は**制度上は2016年から保険適用済み**（K939-6）だが**ホモグラフトの国内提供が年間約10例**で律速され、
   脱細胞化homograft は**国内未承認**でその手前にある。

---

## 成果物

| ファイル | 内容 |
|---|---|
| `md/FutureOfValveSurgery_integrated_review.md` | **本体**。全10章。各章末にエビデンス格付け表＋🔮私の見立て |
| `md/seed_ezag185_notes.md` | シード論文の分解（主張15・引用25・空白8） |
| `md/refs/_ACQUISITION_STATUS.md` | 文献入手状況（何をどこから取ったか） |
| `tables/seed_refs.csv` | 引用25本のDOI/PMID/PMCID/OA状況/ライセンス |
| `tables/seed_claims_verification.csv` | **主張15項目 × 裏取り結果 × 判定**（支持/条件付き/反証あり/検証不能） |
| `tables/technology_evidence_matrix.csv` | **技術24件 × E段階 × 反証 × 日本での可用性 × 出典DOI** |
| `tables/ongoing_trials.csv` | 進行中/完了の関連試験21件 |
| `tables/figure_credits.csv` | 図21件（公開17＋非公開4）のDOI/ライセンス/公開可否 |
| `figures/fv_*.jpg` | **公開可のOA図17点**（CC BY / CC BY-NC / CC BY-NC-ND） |
| `figures_local/ezag185_*.jpg` | **非OAのシード論文図4点**（`.gitignore`済・公開しない） |
| `harvest_figs.py` | PMCからOA図を取得（cdn blob URL・magic bytes検証・reCAPTCHA回避のキャッシュ） |
| `inject_figs.py` | 図をMDへhouse style（inline `<figure>`）で挿入 |
| `pdf/` `pdf_text/` | 原著PDF（.gitignore）と `pdftotext -layout` 出力 |

---

## 確定している前提（本人確認済み・勝手に変えない）

| 項目 | 決定 |
|---|---|
| スコープ | **弁膜症フォーカス**。冠動脈・大動脈・移植/MCS・不整脈は深追いしない |
| 用途 | 自分の知識整理・戦略立案。**数字と一次文献リンクを厚く、批判的評価を明示** |
| 未来予測 | エビデンス準拠＋**明示ラベル（🔮私の見立て）付きの自分の見立て** |
| 図 | **論文PDF/OA原図から実図のみ。自作SVG・模式図は作らない** |
| 図の公開範囲 | **CC BY / CC BY-NC / CC BY-NC-ND のみ公開HTMLへ。非OA（シード ezag185）は `figures_local/` 限定** |
| **JACC系・BMJ系** | **図は使用しない**（AFレビューで確立した方針）。→ Ozaki原典 *JACC Adv* 2025、TEHV石灰化メタ *JACC Basic Transl Sci* の図は不掲載。第8章にその旨を明記 |
| 分量 | 40,000〜60,000字の想定に対し**約77,000字**（一次文献の数値を落とさなかった結果） |

---

## 検証の実施内容（P7）

1. **DOI 88件を CrossRef `/works/{doi}` で個別照会 → 88/88 解決**。ログは `output/doi_verification_future_valve.md`
2. **数値照合2段**
   - stage 1: 本文の数値トークン599件から自明な数と西暦を除いた全件を原文テキスト群と突合 → **未確認0件**
     （桁区切りのカンマ/thin space、先頭ゼロを正規化。派生値だった「3,109」は内訳表記に修正）
   - stage 2: 主要な数値主張**62項目**を（数値, キーワード）の同一文脈共起で機械照合 → **62/62 確認**
3. **図のライセンス機械チェック** → 公開HTMLの図参照17件すべてCC系、非OA図の混入0、
   `figures_local/` と `output/figures/` にバイト同一ファイルなし
4. **描画確認** → Playwright MCP は**ブラウザプロファイルが他インスタンスに占有されて使えなかった**ため、
   `python3 -m http.server 8778` ＋ **Chrome headless `--screenshot`** で代替。
   全図のHTTP 200、17点の描画・キャプション・DOI/PubMedリンク・ライセンス表記、
   サイドバー目次、表組み、CJK太字、横スクロールなしを目視確認

### 検証で見つかった原著側の不整合（本文に明記済）

**AVIATOR（10.1093/ejcts/ezac514）は同一論文内で数値が食い違う**：
VSRR vs CVG-ARR の5年生存が**抄録 85.4%・本文 84.4%**、p値が**抄録/本文 P=0.002・Figure 2A で p=0.01**。
→ 第3章の図2キャプションに明記した（図を貼った目的そのもの）。

---

## 未解決／次にやること

1. **git commit & push**（未実施）。**MDとHTMLの両方**＋`index.html`＋`tables/`＋`figures/`＋`output/figures/` を含めること。
   `output/figures/` を入れ忘れると Pages で図が404になる。
2. **経腋窩AVR（ezae427）の新規ペースメーカ率**。1,000例の原著に記載がない（術前保有3.8%のみ）。著者照会が必要。
3. **日本の VSARR 実施数**。JATS集計は「大動脈弁形成173例」と「基部置換」を分けており、VSARR単独の全国数が特定できない。JCVSD詳細集計が必要。
4. ~~ホモグラフトの制度情報の一次確認~~ → **2026-07-26 解決。ただし当初の記述が誤りだったので下記§訂正を参照。**
   残る未確認点は**点数引き上げ時期**のみ（創設時9,960点→平成30年時点81,610点、どの改定で変わったか）。
5. **CONTOUR trial（NCT06869954）の結果**（2027年 primary completion）。第4章の結論はここで更新する。
6. **Ozaki の20年成績**。原典コホートの追跡は10%が9年超で、20年の曲線は存在しない。
7. **低強度抗凝固の日欧差**（日本30年観察研究は良好、欧米RCTは失敗）の原因が未解決。

---

## 環境・ツールの申し送り（今回得た知見）

- **OUP（EJCTS/EHJ）は curl 403 だが、Claude の `WebFetch` は通る**。ページ全体の要約になるので
  「Table Xの数値を抜き出せ」のように具体的に聞くと有効。ただし**要約モデルが数値を落とす**ので、
  決定的な数値は必ず原文PDFで確認する（今回 De Paulis 総説の耐久性データは WebFetch では取れず、PDFで取得できた）
- **PMCのOA図は `ftp.ncbi.nlm.nih.gov` に到達できない**（DNS/サンドボックス）。
  代わりに **PMC記事HTMLから `https://cdn.ncbi.nlm.nih.gov/pmc/blobs/...` を正規表現で拾う**
  （`harvest_figs.py`。`.../articles/PMCxxxx/bin/*.jpg` は404 HTMLを返すので magic bytes 検証が必須）
- **ライセンス確認は `https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMCxxxx`** が最速（`license="CC BY-NC"` が返る）
- **Playwright MCP がブラウザ占有で使えない場合**、`/Applications/Google Chrome.app/.../Google Chrome --headless=new --screenshot`
  で代替できる。日本語のURLフラグメントは効かないので、**QA用の contact sheet HTML を別に作って撮る**のが確実
- **PDF**: Readツールで直接開かず `pdftotext -layout` で先にテキスト化（フックで弾かれる）
- **HTML化**: `python3 convert_to_html.py <md> <html>`（リポジトリ直下で実行。CJK太字修正が入っている）
- **図はMDに inline `<figure>` で書く**（AFレビューと同じhouse style）。convert_to_html.py がそのまま通す
- **.gitignore に追加済**: `future_cardiac_surgery/figures_local/`（非OA図）、`future_cardiac_surgery/pdf_text/pmc_html/`（PMCキャッシュ2.5MB）

---

## 既存資産との接続（重複を作らない）

| 使うもの | 本レビューでの扱い |
|---|---|
| `output/small_annulus_avr_integrated_review_2026-06.html` | 適応論・PPM・AAE適応は委譲。第8章 lifetime management からリンク |
| `output/aae_technique_atlas.html` | how-to は委譲。第2章（ロボットAVRで弁輪拡大10.8%併施）・第8章からリンク |
| `output/topic_valve_durability_by_valve_2026_06.html` | **第9章「失敗した未来」の一次資料**（Mitroflow/Soprano の反面教師枠を再利用） |
| `output/robotic_cpb_pitfalls.html` `output/cor_knot_pitfalls.html` | 第2章「低侵襲の現実の落とし穴」からリンク |
| `MD/cardiac_surgery_journals_2026_07.md` | Yokoyama HAART 44%再介入（JTCVS #1）→ 第4章の中核 |
| `MD/cardiac_surgery_journals_2026_06.md` | Govers 年12例（#6）→ 第3章／須磨RGEA（#8）→ 第10章の「日本発術式の型」 |

---

## 訂正記録：ホモグラフトの保険収載（2026-07-26）

**当初の記述が誤っていた。** 「ホモグラフトは保険未収載＝先進医療、東大/NCVCのみ、患者自費約60万円」と
本文8か所＋technology_evidence_matrix.csv 3か所に書いていたが、これは
[日本心臓財団のQ&A（**質問日 2012年2月2日**）](https://www.jhf.or.jp/check/opinion/5-7/post_31.html)に基づき、
**2014年3月以前の制度を現状として記述**したものだった。国循で臨床していた本人の指摘（患者に実費請求した記憶がない・
むしろ病院の収益になると部長が言っていた）を受けて一次資料で確認し、全箇所を訂正済み。

### 一次資料で確定した事実

| 事項 | 内容 | 出典 |
|---|---|---|
| 保険収載 | **2016年4月（平成28年度改定）**。これに伴い先進医療「凍結保存同種組織を用いた外科治療」は**終了** | [東大組織バンク 2016-04-08告知](http://uttb.umin.ac.jp/info/) |
| 点数 | **K939-6 凍結保存同種組織加算 81,610点**（令和8年＝現行。平成30/令和2/4/6年も同額） | [令和8年医科点数表](https://shirobon.net/medicalfee/latest/ika/r08_ika/r08i_ch2/r08i2_pa10/r08i2a_sec3/r08i2a3_K939_6.html) |
| 患者負担 | **なし**。通知(3)「組織適合性試験及び同種組織を採取及び保存するために要する全ての費用は、所定点数に含まれ**別に算定できない**」 | 同（通知本文） |
| 実施施設 | 東大/NCVC限定では**ない**。施設基準(8)＝認定組織バンク保有、**または**バンク保有医療機関との事前契約 | 同（施設基準） |
| 算定対象手術 | K555・K555-3・K557・K557-4・K558・K560・K566・K567・**K570**・**K580〜K587**・K614・K623 ほか → **肺動脈弁ホモグラフト（Ross右心系・RVOT再建）は算定対象** | 同（通知(1)） |
| 「病院が儲かる」の構造 | バンクへの支払いは**1組織あたり約80万円**＝加算とほぼ相殺。ただし**自前バンクを持つ国循・東大は外部支払いが発生しない**。さらに通知(4)「請求は移植を行った保険医療機関で行い、**分配は相互の合議に委ねる**」→ 採取〜移植を自院完結なら81,610点を丸取りできる | [福嶌ら Organ Biology 2017;24(1):29-36](https://doi.org/10.11378/organbio.24.29)（OA）＋通知(4) |
| 真の律速 | **国内のホモグラフト提供数は年間約10例**。東大バンク実績264例（1998〜2024年末） | NCVC 2026-06-23発表／東大バンク |
| 現行の先進医療（別物） | 「**心臓移植レシピエント由来**凍結保存同種組織を用いた外科治療」2026-06-23承認・国循・日本初唯一＝**ドナー源拡大** | NCVC |

### 教訓（次回に効く）

- **日本心臓財団など患者向けQ&Aサイトは質問日を必ず見る。** 10年以上前の回答が現在形で残っている。
- **制度の裏取りは点数表本文（告示＋通知＋施設基準）を読む**のが最短。`shirobon.net/medicalfee/latest/...`
  は令和8年版が読める（`saka1029.github.io/tensuhyo/data/web/{28,30,02,04}/i/K939-6.html` で過去版も引ける＝改定履歴の追跡に使える）。
- **制度は「保険適用の有無」だけでなく「加算が実費を賄うか」「自前バンクの有無」で施設の損得が逆転する。**
  同じ制度で赤字の施設と黒字の施設がある。
- 日本語のOA総説（J-STAGE）が制度史の一次資料として強い。今回は福嶌ら2017が決定打だった。

---

## 完了：凍結保存 vs 脱細胞化ホモグラフトの比較節（§6.1、2026-07-26）

第6章に「普通の凍結保存ホモグラフトと脱細胞化ホモグラフトはどう違うのか」の解説節を追加する（本人依頼 2026-07-26）。

**手元にある材料**（`pdf_text/pmc_html/`）:
- ARISE (PMC11009017)：corlife oHG での**約30工程・界面活性剤ベース・非凍結**、histology＋残存dsDNA測定、14日間隔離、
  **4°Cで保存し採取後180日まで植込み可** ← 凍結保存（-196°C・年単位）との決定的な対比
- Sarikouch 20年 (PMC13017825)：室温振盪、2002年 Trypsin/EDTA＋EPC pre-seeding → 2005年以降 non-seeded 界面活性剤へ。
  **CryoLife SynerGraft（脱細胞化＋凍結保存）は小児で劇的に失敗し市場撤退**の記述あり
- Sarikouch 2016 (PMC4951634)：DPH vs 凍結保存CH vs BJV のマッチ比較
- 福嶌ら2017（`/private/tmp/.../fukushima2017.pdf`）：**日本の凍結保存法**（プログラムフリーザー・液体窒素）

**自分で取得可（OA）**: Ebken 2021 EJCTS PMC8083949 (CC BY-NC)／Oripov 2022 Front Cardiovasc Med PMC9395941 (CC BY)

**本人がDL済・`pdf/`へrename+move完了**:
| PMID | 論文 | 役割 |
|---|---|---|
| 21911800 | Cebotari, Circulation 2011;124(11 Suppl):S115-23 | Hannover脱細胞化プロトコルの原典 |
| 10649208 | Hawkins, JTCVS 2000;119(2):324-30 | **凍結保存後の抗HLA抗体**＝凍結側の免疫機序 |
| 12829079 | Simon, EJCTS 2003;23(6):1002-6 | SynerGraft小児早期破綻＝脱細胞化は万能でない |
| 22340029 | Brown, JTCVS 2012;143(3):543-9 | **同一施設での脱細胞化 vs 標準凍結保存 直接比較** |
| 29759737 | JTCVS 2018;156(4):1357-1365.e6 | 凍結保存allograft AVR長期成績（大動脈位の対照） |
| 30476047 | ICVTS 2019;28(4):503-509 | 凍結保存肺homograftの耐久性とドナー要因 |

**成果**: `## 6.1 用語の整理 — 「ホモグラフト」は4種類ある`（6.1.1〜6.1.6＋🔮見立て）を新設し、
旧6.1〜6.5を6.2〜6.6へ繰り下げ。内部参照（6.5／6.6）と第9章チェックリスト参照を修正済。
**新節の数値147トークンを原文と機械照合＝未確認0**（`.264`は原文が先頭ゼロなし表記、`70188`はDOIの一部）。
新規DOI 8件すべてCrossRefで解決確認。

**核心の4分類**（この区別がないと文献が読めない）:
①標準凍結保存（細胞が残る／−196°C／日本のバンク供給品）②脱細胞化＋凍結の同種弁（CryoValve SG）
③脱細胞化ブタ弁（SynerGraft Model 500/700＝小児で死亡例・撤退）④脱細胞化＋非凍結（corlife DPH/DAH＝本章の主題）。
**決めているのは脱細胞化の有無ではなく由来（ヒトかブタか）**。そして**④ vs ② の直接比較は存在しない**
＝「非凍結であること」の追加寄与は未分離＝E3に留める理由。

**まだやれること（任意）**: Ebken 2021 (PMC8083949, CC BY-NC) と Oripov 2022 (PMC9395941, CC BY) の
dot blot 図はOAなので §6.1.3 に挿入可能。ただし図番号1〜17の中間に入るため**全図の再ナンバリングが必要**
（前回ハマった箇所。`inject_figs.py` の renumber ロジックを再利用すること）。

## サイドバー改修（2026-07-26）

`convert_to_html.py` のTOCが `h2, h3, h4` しか拾っておらず、**`# 第N章` (h1) がサイドバーに出ていなかった**
（「どの章か分からない」との指摘）。修正内容:
- セレクタを `h1, h2, h3, h4` にし、**先頭のh1（文書タイトル）のみ除外**
  → 他の全ドキュメントはh1が1個（タイトル）だけなので**影響ゼロ**。確認済
- h1に `nav-chapter` クラス（accent背景の白抜き）を付与。h1が存在する文書では
  `#sidebar-nav.has-chapters` で h2 を従属レベルの見た目に落とす
- 章立て文書ではサイドバー見出しを「目次 — 雑誌・論文」→「**目次 — 章・節**」に自動変更
- 他レポートに反映するには各HTMLを再ビルドするだけ（MDは変更不要）
