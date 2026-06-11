---
title: "狭小弁輪 SAVR / 弁輪拡大術 リサーチコレクション — 引継ぎ資料"
date: 2026-05-13
tags: [handoff, small-annulus-avr, status]
---

# 狭小弁輪 SAVR / 弁輪拡大術 リサーチコレクション 引継ぎ資料

**作成日**: 2026-05-13
**更新日**: 2026-05-13
**現フェーズ**: **Phase 1（スケルトン構築）完了 → Phase 2（並列文献収集）待機**

---

## 研究テーマ

「大動脈弁置換における狭小弁輪症例の扱い — Y-incision を含む弁輪拡大術 (AAE: Aortic Annulus Enlargement) は、小体格・狭小弁輪患者（特にアジア人・日本人）にも本当に正当化されるか？」

### Research Question
- **Primary**: 狭小大動脈弁輪（≤23mm）かつ小体格（BSA <1.6–1.8 m²）の患者で、弁輪拡大付き SAVR は弁輪拡大なし SAVR / TAVI と比較してアウトカムを改善するか
- **Secondary**: 将来の ViV-TAVR 実現可能性を確保するために、initial SAVR で何 mm の弁が必要か。19mm 弁植込みは long-term で許容されるか
- **Tertiary**: 日本人・アジア人特有の解剖（small annulus, small aorta, low BMI）を反映した手術戦略はどうあるべきか

### 確定済の意思決定（2026-05-13）
| 項目 | 選択 |
|---|---|
| ディレクトリ名 | `small_annulus_avr/` |
| 狭小弁輪 operational definition | **annulus ≤23mm（広義）** — 21mm 主軸、21–23mm も Asian cohort 重視で取り込む |
| 最終成果物 | **日本語の統合レビュー** + Obsidian ノート群（論文タイトル・引用は英語のまま） |
| 日本語文献（J-STAGE 等） | **含める** — Cat C で日本人小体格コホート重視、手動 harvest |

---

## 現在の状態

```
small_annulus_avr/
├── HANDOFF.md              ← この資料
├── PLAN.md                 ✅ 計画書（Phase 0 で確定）
├── _index.md               ✅ skeleton（Phase 4 で完成予定）
├── paper_list.md           ✅ skeleton（Phase 2 で埋める）
├── search_queries.md       ✅ 完成（再現性のための検索クエリ集）
├── md/                     ⏸  空（Phase 3 で 39–58 本作成予定）
├── pdfs/                   ⏸  空（Phase 3a で収集予定）
└── tables/                 ✅ outcomes_master.csv ヘッダのみ
```

### フェーズ進捗

| フェーズ | 内容 | 状態 |
|---|---|---|
| **Phase 0** | 調査計画策定（Plan mode） | ✅ 完了 (2026-05-13) |
| **Phase 1** | スケルトン構築（本セット） | ✅ 完了 (2026-05-13) |
| **Phase 2** | 並列 4 Agent で文献収集 → `paper_list.md` 完成 | ⏸ 未着手 |
| **Phase 3a** | PDF 収集（pdfs/） | ⏸ 未着手 |
| **Phase 3b** | 個別論文 MD（軽量 + 詳細）作成 | ⏸ 未着手 |
| **Phase 4** | `outcomes_master.csv` 抽出 + `_index.md` 統合 + 日本語統合レビュー執筆 | ⏸ 未着手 |
| **Phase 5** | （任意）HTML レポート化・GitHub Pages 公開 | ⏸ 未着手 |

---

## YAML Frontmatter テンプレート（small_annulus_avr 専用）

```yaml
---
title: "論文英語タイトル"
authors: "First Author et al."
journal: "雑誌フルネーム"
citation: "Journal YEAR;VOL:PAGES"
doi: "10.xxxx/xxxxx"
pmid: "XXXXXXXX"
pdf: "[[small_annulus_avr/pdfs/FileName.pdf]]"
tags:
  - small-annulus
  - savr
  - [固有タグ: e.g., y-incision, manouguian, ppm, viv-tavr, japanese-cohort]
date: YYYY-MM-DD
category: "弁輪拡大術 | TAVI比較 | PPM | ViV | ガイドライン | アジア人コホート"
journal-abbr: "JTCVS / EJCTS / AnnThoracSurg / JACC / NEJM / Circulation / JCS / ..."
paper-type: "technique | rct | cohort | meta-analysis | guideline | review | registry"
# --- 本テーマ固有フィールド ---
annulus-size: "≤21mm | 21-23mm | mixed | not specified"
patient-bsa: "<1.6 | 1.6-1.8 | >1.8 | mixed"
valve-type: "bioprosthetic | mechanical | TAVI | mixed"
enlargement-technique: "Y-incision | Manouguian | Nicks | Konno | none | combined"
asian-cohort: yes | no | partial
ppm-rate: "severe X% / moderate Y%"
viv-discussion: yes | no
sample-size: "n=XXX"
follow-up: "median X yr"
---
```

### タグ命名規則（kebab-case）

| グループ | タグ例 |
|---|---|
| 患者集団 | `small-annulus`, `bsa-low`, `japanese-cohort`, `asian-cohort`, `korean-cohort` |
| 手技 | `y-incision`, `manouguian`, `nicks`, `konno`, `aae`, `root-replacement` |
| 弁 | `bioprosthetic`, `mechanical`, `sutureless`, `perceval`, `intuity`, `inspiris`, `magna` |
| 介入比較 | `tavi-savr`, `viv-tavr`, `tavr-explant` |
| アウトカム | `ppm`, `severe-ppm`, `pacemaker`, `mortality`, `gradient` |
| エビデンス階層 | `rct`, `meta-analysis`, `registry`, `single-center`, `guideline`, `jcs-guideline`, `sts-consensus` |
| 雑誌系統 | `jtcvs`, `ejcts`, `nejm`, `jacc`, `circulation` |

---

## ファイル命名規則

PDF / MD のファイル名は **commando_procedure と統一**:

```
[LastName]_[CamelCaseDescriptor]_[JournalAbbr]_[Year].{md,pdf}
```

例:
- `Yang_YIncisionAorticAnnularEnlargement_JTCVS_2023.pdf`
- `Herrmann_SMARTtrialSmallAnnulusTAVR_NEJM_2024.pdf`
- `Hayashida_JapaneseTAVIRegistrySmallAnnulus_CircJ_2018.pdf`
- `Manouguian_AnnularEnlargementOriginal_JTCVS_1979.pdf`

---

## 次のステップ（Phase 2 開始時のチェックリスト）

1. [ ] `search_queries.md` を読み返して、Cat A–I のクエリを最新版に refine
2. [ ] **並列 4 Agent ディスパッチ**（[[PLAN]] §4 参照）
   - Agent 1: Cat A + B（Y-incision / 古典 AAE）
   - Agent 2: Cat C + I（アジア人コホート + 弁選択） — J-STAGE 含む
   - Agent 3: Cat D + F（PPM + ViV）
   - Agent 4: Cat E + G + H（TAVI 比較 + sutureless + ガイドライン）
3. [ ] 各 Agent 出力（PMID/著者/雑誌/年/DOI/一行抄録/優先度★ の表）を `paper_list.md` のカテゴリ別テーブルに集約
4. [ ] **重複除去**: PMID/DOI で merge
5. [ ] **DOI 検証**: 抜き打ち 5 件を `get_crossref_paper_by_doi` で確認
6. [ ] `paper_list.md` の「PDF入手状況サマリー」テーブルを更新

---

## 関連ファイル（read-only 参照）

- [[commando_procedure/HANDOFF]] — テンプレ原本
- [[commando_procedure/_index]] — 統括ハブ構成の参考
- [[commando_procedure/md/Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025]] — Manouguian 歴史参照
- [[commando_procedure/md/Kakavand_CommandoMitralAnnularCalcification_JTCVSOpen_2024]] — PPM 7.8% データ
- [[MD/cardiac_surgery_journals_2026_03]] — Handa et al. 日本人 LAVI×SAVR
- [[MD/cardiac_surgery_journals_2026_05]] — Carducci TAVR vs SAVR
- `/Users/k.tonai/.claude/plans/research-y-incision-bigger-the-better-1-foamy-breeze.md` — 計画書原本

---

*作成: 2026-05-13 | 関連: [[_index]] | [[paper_list]] | [[search_queries]] | [[PLAN]]*
