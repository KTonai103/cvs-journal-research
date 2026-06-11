---
title: "狭小弁輪 SAVR / AAE 文献検索クエリ集"
date: 2026-05-13
tags: [small-annulus-avr, search-queries, pubmed, crossref, j-stage]
category: 弁膜症外科
---

# 文献検索クエリ集（再現性確保のため）

**作成日**: 2026-05-13
**目的**: Phase 2 の並列 Research Agent ディスパッチで使用する PubMed / CrossRef / J-STAGE / Web 検索クエリを一元管理。実行ログとして検索日・ヒット数・採用本数も記録する。

---

## 1. Inclusion / Exclusion 基準

### Inclusion
- 成人（age ≥18）対象の SAVR または TAVR/TAVI 研究
- 大動脈弁輪径 ≤23mm（明記）または BSA <1.8 m²（機能的小弁輪）
- 出版年 ≥2010（古典 AAE 原著は historical reference として 1970–1979 も採用）
- 原著論文 / RCT / システマティックレビュー / メタアナリシス / レジストリ研究 / ガイドライン
- 英語 + 日本語（J-STAGE 経由）

### Exclusion
- 症例報告（n<5）
- 小児（age <18）
- Ross 手術主題
- 純粋に bicuspid valve のみ focus（小弁輪との関連がなければ除外）
- 動物実験・in vitro 研究

---

## 2. PubMed クエリ（カテゴリ別）

### Cat A: Y-incision / Roof technique
```
("Y-incision" OR "roof technique" OR "Yang technique") AND (aortic OR annulus OR annular) AND (enlargement OR enlarging)
Filter: 2020:2026[dp], Humans, English
```

### Cat B: 古典 AAE 長期成績
```
("aortic annular enlargement" OR "aortic root enlargement" OR Nicks[All Fields] OR Manouguian[All Fields] OR Konno[All Fields])
  AND (long-term OR outcomes OR survival OR mortality)
Filter: 2010:2026[dp], Humans, English
```

### Cat C: 狭小弁輪 + アジア人コホート
```
(("small annulus"[tiab] OR "narrow annulus"[tiab] OR "annulus ≤21"[tiab] OR "annulus 19mm"[tiab] OR "annulus 21mm"[tiab] OR "annulus 23mm"[tiab])
  AND (Asian[tiab] OR Japanese[tiab] OR Korean[tiab] OR Chinese[tiab] OR "body surface area"[tiab] OR "small body size"[tiab]))
  AND ("aortic valve replacement"[MeSH] OR SAVR OR TAVI OR TAVR)
Filter: 2010:2026[dp], Humans
```

### Cat D: PPM（Prosthesis-Patient Mismatch）
```
"prosthesis-patient mismatch"[MeSH Major Topic]
  AND (mortality OR survival OR gradient OR "effective orifice area")
Filter: 2010:2026[dp], Humans, English
+ Manual seminal: Pibarot 2000 JACC, Head 2012 EHJ, Mohty 2009 Circulation
```

### Cat E: TAVI vs SAVR in small annulus
```
(TAVI OR TAVR OR "transcatheter aortic valve")
  AND ("small annulus"[tiab] OR "small aortic" OR "narrow annulus")
  AND (SAVR OR "surgical aortic valve" OR surgical)
Filter: 2015:2026[dp], Humans, English, RCT[ptyp] OR Meta-Analysis[ptyp]
+ Manual: SMART trial (Herrmann 2024 NEJM)
```

### Cat F: ViV-TAVR / TAVI explant
```
("valve-in-valve"[tiab] OR ViV)
  AND TAVR AND (feasibility OR explant OR "valve size" OR "surgical valve size")
Filter: 2015:2026[dp], Humans, English
+ Manual: VIVID registry (Bleiziffer et al.)
```

### Cat G: Sutureless / Rapid deployment
```
(sutureless[tiab] OR "rapid deployment"[tiab] OR Perceval[tiab] OR Intuity[tiab])
  AND ("aortic valve replacement"[MeSH])
  AND ("small annulus" OR PPM OR "small body")
Filter: 2015:2026[dp], Humans, English
```

### Cat H: ガイドライン・コンセンサス
```
(guideline[ptyp] OR "consensus statement"[ptyp])
  AND ("aortic valve" OR SAVR OR TAVR OR AVR)
  AND (small OR mismatch OR enlargement)
Filter: 2018:2026[dp], English
+ Manual:
  - 2020 ACC/AHA Guideline (Circulation/JACC)
  - 2021 ESC/EACTS Guidelines (EHJ)
  - JCS 2020 弁膜症治療のガイドライン (Circ J + 学会公式 PDF)
  - STS expert consensus on AAE (2024 想定)
```

### Cat I: 機械弁 vs 生体弁 in small annulus
```
(mechanical[tiab] OR bioprosthetic[tiab] OR biological[tiab])
  AND "aortic valve replacement"[MeSH]
  AND ("small annulus" OR "19mm" OR "21mm" OR "small valve")
Filter: 2015:2026[dp], Humans, English
+ Seminal: Goldstone AB. NEJM 2017
```

---

## 3. CrossRef クエリ（ISSN 固定 + キーワード）

主要ジャーナル ISSN:

| 雑誌 | ISSN |
|---|---|
| JTCVS | 0022-5223 |
| EJCTS | 1010-7940 |
| Ann Thorac Surg | 0003-4975 |
| JACC | 0735-1097 |
| Circulation | 0009-7322 |
| NEJM | 0028-4793 |
| Circulation Journal (日本循環器学会) | 1346-9843 |
| Gen Thorac Cardiovasc Surg (日本胸部外科学会, English) | 1863-6705 |

### 検索パターン
1. `crossref.search(query="Y-incision aortic annular enlargement", filter={ISSN: "0022-5223", from-pub-date: "2020-01-01"})`
2. `crossref.search(query="annular enlargement small annulus", filter={ISSN: "1010-7940", from-pub-date: "2018-01-01"})`
3. `crossref.search(query="aortic valve replacement Japanese", filter={ISSN: "1346-9843", from-pub-date: "2015-01-01"})` ← Circulation Journal（日本人エビデンス）

---

## 4. J-STAGE 手動 harvest 戦略

J-STAGE には自動検索 API がないため、以下の手順で **手動 harvest**:

### 対象ジャーナル
- **日本心臓血管外科学会雑誌**（Japanese Journal of Cardiovascular Surgery）
- **日本胸部外科学会雑誌**（Japanese Journal of Thoracic and Cardiovascular Surgery → 現 Gen Thorac Cardiovasc Surg、英文化済み）
- **日本心臓病学会誌**
- **Circulation Journal**（日本循環器学会、英文）

### 手順
1. J-STAGE 検索画面（https://www.jstage.jst.go.jp/）で各誌を選択
2. キーワード: `狭小弁輪 OR 小弁輪 OR 弁輪拡大 OR Y-incision OR Manouguian OR Nicks OR Konno OR PPM`
3. 期間: 2010–2026
4. ヒット論文を `obsidian:defuddle` で取得 → MD 化
5. 抄録のみで full text 入手不可なものは「対象外」に分類

### 制限時間
Phase 2 内で **1 日上限** とし、5–8 本確保で打ち切り。残りは Phase 4 の統合レビュー執筆時に「日本のエビデンス空白」として明示。

---

## 5. Web 検索（mgrep --web）

PubMed / CrossRef で拾えない以下を補完:
- SMART trial の最新 follow-up（学会発表ベース、未論文化）
- TAVI 4-Center registry / OCEAN-TAVI registry など日本国内多施設研究
- 各学会の position statement / consensus

```
mgrep --web "SMART trial small annulus TAVR 2025 long-term follow-up"
mgrep --web "OCEAN-TAVI registry small annulus Japan"
mgrep --web "JCS 2020 弁膜症ガイドライン 大動脈弁置換 PPM"
```

---

## 6. obsidian:defuddle（雑誌サイト・J-STAGE Markdown 化）

- 雑誌オンラインの目次・abstract ページから論文情報を Markdown 抽出
- J-STAGE 個別論文ページ → 日本語論文の抄録抽出
- 学会公式サイト（JCS 等）→ ガイドライン PDF への直リンク取得

---

## 7. データ品質チェック（Phase 2 末尾）

1. **重複除去**: PMID / DOI で merge
2. **DOI 検証**: `get_crossref_paper_by_doi` で抜き打ち 5 件確認
3. **PMID 検証**: PubMed E-utilities `esummary.fcgi` で抜き打ち 5 件確認
4. **タイトル一致性**: CrossRef と PubMed のタイトルが一致するか

---

## 8. 実行ログ（Phase 2 で記入）

| 実行日 | 実行者 | クエリ ID | ツール | ヒット数 | 採用数 | 備考 |
|---|---|---|---|---|---|---|
| 2026-05-XX | Agent 1 | Cat A | PubMed | — | — | — |
| 2026-05-XX | Agent 1 | Cat B | PubMed | — | — | — |
| 2026-05-XX | Agent 2 | Cat C | PubMed + J-STAGE | — | — | — |
| 2026-05-XX | Agent 2 | Cat I | PubMed | — | — | — |
| 2026-05-XX | Agent 3 | Cat D | PubMed | — | — | — |
| 2026-05-XX | Agent 3 | Cat F | PubMed | — | — | — |
| 2026-05-XX | Agent 4 | Cat E | PubMed + Web | — | — | — |
| 2026-05-XX | Agent 4 | Cat G | PubMed | — | — | — |
| 2026-05-XX | Agent 4 | Cat H | Web + 手動 | — | — | — |

---

*作成: 2026-05-13 | 関連: [[paper_list]] | [[_index]] | [[HANDOFF]] | [[PLAN]]*
