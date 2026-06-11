# Research Plan — 狭小弁輪 SAVR と弁輪拡大術の正当性

新規プロジェクト `small_annulus_avr/` の文献調査・統合レビュー計画。

---

## Context（背景・問題意識）

### なぜ今この研究が必要か
- 欧米では Yang らによる Y-incision（Roof technique, JTCVS 2023）を契機に、**大動脈弁輪拡大術 (Aortic Annulus Enlargement: AAE)** が大流行している
- 風潮は **"Bigger the better"**：将来の Valve-in-Valve TAVR を見据え、初回 SAVR で 23–25mm 弁を入れるべきとされる
- 一方で **小体格・狭小弁輪患者（特に日本人・アジア人）** に対して、その追加侵襲が本当に正当化されるかは検証不足
- 19mm 弁しか入らない症例で、Y-incision/Manouguian/Nicks を加えることは、合併症増加とのトレードオフが妥当か

### Research Question
- **Primary RQ**: 狭小大動脈弁輪（annulus ≤23mm）かつ小体格（BSA <1.6–1.8 m²）の患者で、**弁輪拡大付き SAVR は弁輪拡大なし SAVR / TAVI と比較して**短期・長期アウトカム（mortality, stroke, PPM, gradient, survival）を改善するか
- **Secondary RQ**: 将来の ViV-TAVR 実現可能性を確保するために、initial SAVR で何 mm の弁が必要か。19mm 弁植込みは long-term で許容されるか
- **Tertiary RQ**: 日本人・アジア人特有の解剖（small annulus, small aorta, low BMI）を反映した手術戦略はどうあるべきか

### ユーザー意思決定（確定済）
| 項目 | 選択 |
|---|---|
| ディレクトリ名 | `small_annulus_avr/` |
| 狭小弁輪 operational definition | **annulus ≤23mm（広義）** — 21mm 主軸、21–23mm も Asian cohort 重視で取り込む |
| 最終成果物 | 日本語の統合レビュー + Obsidian ノート群（論文タイトル・引用は英語のまま） |
| 日本語文献（J-STAGE 等） | **含める** — Cat C で日本人小体格コホート重視、手動 harvest |

---

## 1. ディレクトリ構造

```
small_annulus_avr/
├── PLAN.md                     本計画書のプロジェクト内コピー
├── HANDOFF.md                  Frontmatter テンプレ + 引継ぎ資料
├── _index.md                   統括ハブ（参照マップ・Key Numbers・PDF index）
├── paper_list.md               カテゴリ別文献リスト（PMID/DOI/PDF status）
├── search_queries.md           PubMed/CrossRef/J-STAGE クエリ集（再現性確保）
├── md/                         個別論文 MD サマリー
│   ├── _IntegratedReview_SmallAnnulusAVR_2026.md   日本語統合レビュー（最終成果物）
│   └── [Author]_[Title]_[Journal]_[Year].md ...
├── pdfs/                       PDF 保存
└── tables/                     アウトカム抽出 CSV
    ├── outcomes_master.csv     横断比較用（短期・長期アウトカム）
    ├── ppm_landscape.csv       PPM rate / mean gradient 集計
    └── asian_cohort_subset.csv 日本人・アジア人コホート抽出ビュー
```

ファイル命名規則（`commando_procedure/` と統一）: `AuthorLastName_PaperTitleAbbrev_JournalAbbrev_YYYY.{md,pdf}`

---

## 2. 文献検索カテゴリ（9 分類）

| Cat | 内容 | 優先度 | 想定本数 | 代表 seminal paper |
|---|---|---|---|---|
| **A** | Y-incision / Roof technique 原著・技術 | ★★★★★ | 6–8 | Yang B et al. JTCVS 2023 (DOI: 10.1016/j.jtcvs.2022.07.006); Yang B. Ann Thorac Surg 2021 |
| **B** | 古典 AAE（Nicks 1970 / Manouguian 1979 / Konno 1975）長期成績 | ★★★★ | 4–6 | Manouguian S. JTCVS 1979;78:402; Nicks R. Thorax 1970;25:339; Coutinho GF. EJCTS 2018 |
| **C** | 狭小弁輪 + 小体格コホート（特に **日本人・アジア人**） | ★★★★★ | 8–12 | Hayashida K (TAVI registry); Tabata M (Japanese SAVR); Handa K 2026 EJCTS; Asan Med Center series; **J-STAGE harvest** |
| **D** | PPM 臨床的意義・閾値（severe iEOA ≤0.65, moderate ≤0.85） | ★★★★ | 5–7 | Pibarot P. JACC 2000; Head SJ. EHJ 2012 meta; Mohty D Circulation 2009 |
| **E** | TAVI vs SAVR in small annulus（**SMART trial 等**） | ★★★★★ | 4–6 | Herrmann HC. *SMART trial.* NEJM 2024; Abdelfattah OM 2023 meta; Carducci 2026（既収集） |
| **F** | ViV-TAVR / TAVI explant — 初回弁サイズの影響 | ★★★★ | 4–6 | Bleiziffer S et al. VIVID registry; Bapat V; Tarantini G EuroIntervention 2021 |
| **G** | Sutureless / Rapid deployment（Perceval, Intuity）— AAE 代替 | ★★★ | 3–5 | Berretta P (Perceval IRCCS); Lorusso R (SURE-AVR) |
| **H** | ガイドライン・コンセンサス（STS/AATS, EACTS/ESC, **JCS 2020 弁膜症**） | ★★★★ | 3–5 | 2020 ACC/AHA; 2021 ESC/EACTS; **JCS 2020 弁膜症ガイドライン**; STS expert consensus 2024 |
| **I** | 機械弁 vs 生体弁 in small annulus（補助） | ★★ | 2–3 | Goldstone AB NEJM 2017 |

**想定総数: 39–58 本**（J-STAGE 追加で commando より一回り大きい）

---

## 3. 検索クエリ設計

### Inclusion / Exclusion
- **Inclusion**: adult (≥18 yo) SAVR/TAVR; annulus ≤23mm（明記または BSA <1.8 m² で機能的に狭小）; ≥2010 publication; original article OR systematic review; English + Japanese
- **Exclusion**: case report (n<5); pediatric; Ross 手術; 純粋 bicuspid 主題（small annulus と関連する場合のみ採用）

### カテゴリ別クエリ（核）
| Cat | PubMed クエリ |
|---|---|
| A | `("Y-incision" OR "roof technique") AND (aortic OR annulus) AND enlargement` + filter 2020–2026 |
| B | `("aortic annular enlargement" OR "aortic root enlargement" OR Nicks OR Manouguian OR Konno) AND (long-term OR outcomes OR survival)` |
| C | `(small annulus OR narrow annulus OR "annulus 21mm" OR "annulus 23mm") AND (Asian OR Japanese OR Korean OR "body surface area")` + **J-STAGE 手動 harvest（日本心臓血管外科学会雑誌・日本胸部外科学会雑誌・Circulation Journal）** |
| D | `"prosthesis-patient mismatch"[MeSH] AND (mortality OR survival OR gradient)` + filter meta-analysis |
| E | `(TAVI OR TAVR OR "transcatheter") AND (small annulus) AND (SAVR OR surgical)` + RCT/meta filter |
| F | `("valve-in-valve" OR ViV) AND TAVR AND (feasibility OR explant OR size)` |
| G | `(sutureless OR "rapid deployment") AND (Perceval OR Intuity) AND (small annulus OR PPM)` |
| H | `(guideline OR consensus) AND ("aortic valve" OR SAVR) AND (2020:2026[dp])` + **JCS 2020 弁膜症ガイドライン（手動）** |
| I | `(mechanical OR bioprosthetic) AND ("aortic valve replacement") AND ("small annulus" OR "19mm" OR "21mm")` |

### データソース優先度
1. **MCP CrossRef**（ISSN 固定で JTCVS 0022-5223 / EJCTS 1010-7940 / Ann Thorac Surg / JACC 系）
2. **MCP PubMed**（curl ベース、E-utilities、MeSH）
3. **mgrep --web**（Web 検索代替 — SMART trial の最新 follow-up 等）
4. **obsidian:defuddle**（J-STAGE ページの Markdown 化）
5. **手動収集** — JCS 2020 弁膜症ガイドライン、日本語学会誌

---

## 4. 並列 Research Agent ディスパッチ戦略

### 第一波（並列 4 Agent）
| Agent | 担当 Cat | 出力 |
|---|---|---|
| **Agent 1** | A + B（手技：Y-incision + 古典 AAE） | paper list（表形式: PMID/著者/雑誌/年/DOI/一行抄録/優先度★） |
| **Agent 2** | **C + I（アジア人コホート + 弁選択） — J-STAGE 含む** | 同上 + 日本語論文サブセクション |
| **Agent 3** | D + F（PPM + ViV — 概念的連続） | 同上 + PPM 閾値の数値抽出 |
| **Agent 4** | E + G + H（TAVI 比較 + sutureless + ガイドライン） | 同上 + ガイドライン推奨文の抽出 |

### 統合手順（メインスレッド）
1. 重複除去（PMID/DOI 一致でマージ）
2. 優先度ランク付け（★★★★★ → ★）
3. `paper_list.md` 集約（commando 形式の表）
4. **PDF 入手可能性タグ付け**（open access / institution / handsearch）

### 第二波（個別 deep dive）
- ★★★★ 以上の論文 15–20 本を個別 Agent でフル MD 化
- 残りは軽量 MD（Key Message + 数値表のみ）

---

## 5. 個別論文 MD フォーマット

### YAML Frontmatter（commando スキーマ + 本テーマ固有フィールド）
```yaml
---
title: "..."
authors: "..."
journal: "..."
citation: "..."
doi: "..."
pmid: "..."
pdf: "[[small_annulus_avr/pdfs/...]]"
tags: [small-annulus, savr, ...]
date: YYYY-MM-DD
category: "弁輪拡大術 | TAVI比較 | PPM | ViV | ガイドライン | アジア人コホート"
journal-abbr: "JTCVS"
paper-type: "technique | rct | cohort | meta-analysis | guideline | review | registry"
# --- 本テーマ固有フィールド ---
annulus-size: "≤21mm | 21-23mm | mixed | not specified"
patient-bsa: "<1.6 | 1.6-1.8 | >1.8 | mixed"
valve-type: "bioprosthetic | mechanical | TAVI | mixed"
enlargement-technique: "Y-incision | Manouguian | Nicks | Konno | none | combined"
asian-cohort: yes | no | partial
ppm-rate: "severe X% / moderate Y%"
viv-discussion: yes | no
sample-size: n=XXX
follow-up: "median X yr"
---
```

### タグ命名（kebab-case）
`small-annulus`, `y-incision`, `manouguian`, `nicks`, `konno`, `tavi-savr`, `ppm`, `viv-tavr`, `sutureless`, `japanese-cohort`, `asian-cohort`, `bsa-low`, `guideline`, `meta-analysis`, `jcs-guideline`

### 本文セクション（commando 9 セクション + 1 新規）
1. Key Message (`> [!NOTE]` callout)
2. 背景・課題設定
3. 患者集団（**annulus size / BSA / 民族を必ず明示**）
4. 手技詳細
5. アウトカム表（30 日死亡・PPM・勾配・1y/5y 生存）
6. 議論ポイント（PPM/ViV 戦略への寄与）
7. 限界
8. **本研究 RQ への含意**（新規 — 統合レビューへの引用しやすさ確保）
9. 引用文献ハイライト

---

## 6. アウトカム抽出マスター表

### `tables/outcomes_master.csv` 列構成
```
paper_id, first_author, year, journal, n, ethnicity, mean_bsa, mean_annulus_mm,
valve_type, enlargement_technique, label_valve_size_mm,
mortality_30d_pct, stroke_pct, pacemaker_pct, aki_pct,
ppm_severe_pct, ppm_moderate_pct, mean_gradient_postop_mmHg,
survival_1y_pct, survival_5y_pct, survival_10y_pct,
viv_feasibility_assessed (Y/N), notes
```

### サブテーブル
- `ppm_landscape.csv` — Cat D 用 PPM 閾値別 forest plot 用データ
- `asian_cohort_subset.csv` — Cat C 集中ビュー（日本人・韓国人・中国人別）

---

## 7. 最終成果物（優先度順）

1. **`md/_IntegratedReview_SmallAnnulusAVR_2026.md`** — **日本語の統合レビュー**（5,000–8,000 語）
   - 論文タイトル・著者名・雑誌は英語のまま
   - 構成: 背景 → 各 AAE 手技の解剖学的レビュー → 国内外アウトカム比較 → アジア人コホートの特殊性 → PPM/ViV 戦略 → 推奨アルゴリズム → 限界・将来課題
2. **`_index.md`** — 参照マップ・Key Numbers・PDF index（commando 同形式）
3. **`tables/outcomes_master.csv`** — meta-analysis 風集計表
4. （任意 Phase 5）HTML レポート — 既存 obsidian-to-html スクリプトを流用して `output/small_annulus_avr_report.html` を生成、GitHub Pages 公開

---

## 8. フェーズ分け

| Phase | 内容 | 推定 | 完了基準 |
|---|---|---|---|
| **1** | PLAN.md / HANDOFF.md / _index.md skeleton / search_queries.md / 空ディレクトリ整備 | 1 日 | テンプレ全 placeholder 完成 |
| **2** | 並列 4 Agent で文献収集 → `paper_list.md` 完成 | 2–3 日 | 39–58 本確定、PMID/DOI 全件検証済み |
| **3a** | PDF 収集（pdfs/） | 2 日 | 90% 以上取得 |
| **3b** | 個別論文 MD（軽量 + 詳細）作成 | 3–5 日 | 全論文に MD 作成 |
| **4** | `tables/outcomes_master.csv` 抽出 + `_index.md` 統合 + **日本語統合レビュー執筆** | 3–4 日 | 統合レビュー draft 完成 |
| **5** | （任意）HTML レポート化 / GitHub Pages 公開 | 1 日 | `output/` に HTML 配置 |

---

## 9. 既存資源との連携（read-only）

- **commando_procedure からの再利用**: Manouguian 系の歴史的記述は `commando_procedure/md/Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025.md` を **wikilink で参照のみ**（重複ノートを作らない）。Cat B の Manouguian 項目に `> 関連: [[commando_procedure/md/Yi_...]]` の callout を入れる。Matsuzaki 2024 ICVTS の **aorto-annulo-septotomy** も参照リンクのみ。
- **既存月別ジャーナル MD への wikilink**: `[[MD/cardiac_surgery_journals_2026_03#Handa]]`（LAVI×SAVR 日本人）, `[[MD/cardiac_surgery_journals_2026_05#Carducci]]`（TAVR vs SAVR）を `_index.md` の Cat C/E に embed。
- **逆方向 wikilink は今回作らない**（既存月別 MD は read-only）。Phase 1 で「将来追加する逆リンク候補」を `_index.md` の Appendix に列挙のみ。
- **CLAUDE.md・ルート README は今回触らない**。

---

## 10. 重要ファイル一覧

### Phase 1 で新規作成（skeleton）
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/PLAN.md`
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/HANDOFF.md`
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/_index.md`
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/paper_list.md`
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/search_queries.md`
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/tables/outcomes_master.csv`（ヘッダのみ）
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/md/.gitkeep`
- `/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr/pdfs/.gitkeep`

### Phase 3 以降で順次作成
- `small_annulus_avr/md/[Author]_[Title]_[Journal]_[Year].md` × 39–58 本
- `small_annulus_avr/md/_IntegratedReview_SmallAnnulusAVR_2026.md`（日本語統合レビュー）
- `small_annulus_avr/tables/ppm_landscape.csv`
- `small_annulus_avr/tables/asian_cohort_subset.csv`

### 修正する既存ファイル
**なし**（既存 `commando_procedure/`, `MD/`, `CLAUDE.md` には触れない）

---

## 11. 参照すべき既存ファイル（read-only）

実装時に頻繁に参照するテンプレ・既収集資料:
- [commando_procedure/HANDOFF.md](../../Documents/CVS_Journal_Research/commando_procedure/HANDOFF.md) — Frontmatter テンプレ原本
- [commando_procedure/_index.md](../../Documents/CVS_Journal_Research/commando_procedure/_index.md) — 統括ハブ構成の参考
- [commando_procedure/paper_list.md](../../Documents/CVS_Journal_Research/commando_procedure/paper_list.md) — 分類リストの記法参考
- [commando_procedure/md/Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025.md](../../Documents/CVS_Journal_Research/commando_procedure/md/Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025.md) — Manouguian 歴史参照
- [commando_procedure/md/Kakavand_CommandoMitralAnnularCalcification_JTCVSOpen_2024.md](../../Documents/CVS_Journal_Research/commando_procedure/md/Kakavand_CommandoMitralAnnularCalcification_JTCVSOpen_2024.md) — PPM 7.8% データ
- [MD/cardiac_surgery_journals_2026_03.md](../../Documents/CVS_Journal_Research/MD/cardiac_surgery_journals_2026_03.md) — Handa et al. 日本人 LAVI×SAVR
- [MD/cardiac_surgery_journals_2026_05.md](../../Documents/CVS_Journal_Research/MD/cardiac_surgery_journals_2026_05.md) — Carducci TAVR vs SAVR
- [.claude/commands/journal-update.md](../../Documents/CVS_Journal_Research/.claude/commands/journal-update.md) — 6 フェーズ並列ディスパッチ workflow

---

## 12. Verification（検証手順）

### Phase 1 完了の検証
1. `small_annulus_avr/` 配下の 8 ファイル（+ tables/, md/, pdfs/ 空ディレクトリ）が全て生成されている → `ls -la small_annulus_avr/` で確認
2. `_index.md`, `HANDOFF.md`, `paper_list.md` が Obsidian で開ける（YAML エラーなし）→ Obsidian で各ファイルを開く
3. `PLAN.md` がプロジェクト内にコピーされている → `diff` で plan ファイルと一致確認

### Phase 2 完了の検証
1. `paper_list.md` に 39 本以上の論文がカテゴリ別に分類されている
2. 各論文の DOI/PMID が CrossRef または PubMed で検証可能 → `get_crossref_paper_by_doi` で抜き打ち 5 件確認
3. 重複（同一 DOI/PMID）が存在しない → 簡易 grep で重複確認

### Phase 3–4 完了の検証
1. ★★★★ 以上の論文すべてに個別 MD ノートが存在 → `ls md/ | wc -l` で 15+ 本
2. `outcomes_master.csv` に各 MD のデータが転記されている → 行数 = MD 数
3. 統合レビュー本文中の引用が `paper_list.md` の論文と一致 → 引用 ID の手動チェック

### Phase 5（任意）の検証
1. `output/small_annulus_avr_report.html` が生成され、ブラウザで開ける
2. wikilink・callout が正しくレンダリングされている
3. GitHub Pages 公開後、モバイルでも閲覧可能

---

## 13. リスク・前提

- **PDF 入手率**: 90% を目標とするが、古い Manouguian 1979 等は handsearch / institutional access 必須。10% 程度の欠落は許容。
- **J-STAGE 手動 harvest** は時間が読みにくい。Phase 2 で 1 日上限を設けて切り上げる。
- **「19mm 弁植込み許容性」の結論** は文献量不足の可能性が高い。その場合、統合レビューでは「エビデンス不足 = 今後の課題」として明示する（これ自体が本研究の貢献）。
- **MCP paper-search の停止リスク**: バックアップとして mgrep --web + curl ベース PubMed E-utilities を併用。
