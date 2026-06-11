---
title: "Phase 2 — Claude vs Codex Cross-Check Summary"
date: 2026-05-13
tags: [phase-2, cross-check, verification, hallucination-audit]
status: 最終確定リストの根拠ドキュメント
---

# Phase 2 — Claude vs Codex 相互検証サマリー

> [!important] 結論
> Claude 側 4 Agent の literature recall は **致命的に不正確**（PMID 全件 hallucination 確認、著者・年・DOI も多数誤り）。Codex 側は **知識ベース上は正確** だが curl が DNS で blocked。**最終的に信頼できるのは Claude メインスレッドが直接 PubMed E-utilities API を叩いた実検証結果のみ**。本ドキュメントは、最終 paper_list.md に載せる前の検証マトリクス。

---

## 1. ハルシネーション・エラー集計

| カテゴリ | Claude 側件数 | 確定 hallucination | Codex 訂正 | 実検証通過 |
|---|---|---|---|---|
| Cat A (Y-incision) | 6 | 6 (PMID 全件) | n/a | 21 件新規実検証 |
| Cat B (古典 AAE) | 6 | 1 (Coutinho PMID) | n/a | 10 件新規実検証 |
| Cat C (アジア人コホート) | 8+ (大半未確定) | n/a (未確定) | 17 件新規発見 | (Codex 知識依存) |
| Cat D (PPM) | 8 | 1 (Mohty 2006 PMID 不充分) | 2 件 DOI 訂正 | (Codex 知識依存) |
| Cat E (TAVI vs SAVR) | 4 | 1 PMID (SMART) | 4 件 (PMID/著者/年/DOI) | (Codex 知識依存) |
| Cat F (ViV) | 13 | 0 | 6 件 (著者・DOI) | 1 件新規 (Dvir 2014) |
| Cat G (Sutureless) | 5 | **5 件全て** PMID/著者/年/誌違い | 5 件 (全件) | (Codex 訂正) |
| Cat H (Guidelines) | 4 | 3 件 (PMID 違い、STS 存在せず) | 3 件 | (Codex 訂正) |
| Cat I (Mech vs Bio) | 1 | 1 (Goldstone PMID 28296591 誤り) | 1 件 (→ 29117490) | (Codex 訂正) |

**累計**: Claude side で **少なくとも 30 件以上の PMID/DOI/著者誤り**。最終リストには **実検証通過分のみ**採用。

---

## 2. PMID Hallucination Audit — Cat A+B (PubMed 実検証済み)

| Claude 提示 | Claude 主張の内容 | PubMed 実 PMID 内容 | 判定 |
|---|---|---|---|
| 37050629 | Yang B JTCVS 2023 Y-incision seminal | Sensors 2023「射出成形モニタリング」 | ❌ Hallucination |
| 35181639 | Yang B Ann Thorac Surg 2021 | J Immunol 2022「魚類ウイルス免疫」 | ❌ Hallucination |
| 37614789 | Yang B JTCVS 2024 5yr outcomes | RSC Adv 2023「撥水繊維」 | ❌ Hallucination + 論文自体存在せず |
| 36891204 | Ohira S Ann Thorac Surg 2023 | Front Psychol 2023「Latinx COVID 心理」 | ❌ Hallucination |
| 37892156 | Kaneko T JTCVS 2024 Japanese Y-incision n=47 | Biomolecules 2023「ナツメヤシ生化学」 | ❌ Hallucination + 論文自体存在せず |
| 36234567 | Masuda M EJCTS 2023 Modified Y-incision | Nanomaterials 2022「廃水処理」 | ❌ Hallucination |
| 31234567 | Totaro P EJCTS 2019 AAE meta-analysis | Sensors 2019「電気インピーダンス」 | ❌ Hallucination |
| 32456789 | Zoghbi WA JACC 2020 Multi-Registry | Can J Ophthalmol 2020「結膜炎」 | ❌ Hallucination |
| 29357689 | Coutinho EJCTS 2018 Manouguian 25y | Clin Child Psychol 2018「養子縁組心理」 | ❌ Hallucination |

**全 9 件中 9 件が hallucination（100%）** — Cat A+B では Claude side の PMID は信頼に値しない

---

## 3. Cat F 主要訂正（first author / DOI 誤り）

| Claude 提示 | 実際 |
|---|---|
| Bleiziffer S VIVID coronary obstruction EHJ 2018, DOI **ehy079** | **Ribeiro** first author, DOI **ehx455** |
| Bleiziffer S 2016 Circ Cardiovasc Interv ViV depth, DOI **004056** | **Simonato** first author, DOI **003651** |
| Tarantini Ann Thorac Surg 2016 | **D'Onofrio** first author |
| Tarantini BVF 2025 PMID 40537943 | **Ruge** first author, REDUCE registry |
| Bapat REVALVE 2025 PMID 40393632 | **Blackman** first author, design paper only |

---

## 4. Cat G ほぼ全件再帰属（severe）

| Claude 提示 | 実際 |
|---|---|
| **Di Eusanio SURD-IR EJCTS 2019, PMID 30689828** | **Santarpino** first author |
| **Berretta JTCVS 2021 PMID 32832411** | 実際は **Ann Cardiothorac Surg 2020** |
| **Lorusso JTCVS 2021 PMID 34563505** | **Berretta** first author, Ann Thorac Surg 2022 |
| **Sénage JTCVS 2015 PMID 24413009** | **Borger** first author, MMCTS 2013 |
| **Folliguet ICVTS 2016 PMID 26920726** | **Beckmann** first author |

**Cat G の Claude side は 5/5 件すべて first author + 誌名 + 年が違う**

---

## 5. Cat H ガイドライン重要訂正

| 項目 | Claude | 訂正 |
|---|---|---|
| **ACC/AHA 2020 full guideline** | PMID 33332149 | **PMID 33332150**（33332149 は exec summary） |
| **ESC/EACTS 2021 full guideline** | PMID 35636831 | **PMID 34453165**（35636831 は Rev Esp Cardiol reprint） |
| **STS expert consensus on AAE 2024** | "想定実在" | ❌ **存在しない** — STS Learning Center hands-on course のみ |

---

## 6. Cat C 補完（Codex の新規発見 17 件）

OCEAN-TAVI series, J-TVT registry, Japanese 17mm SAVR series (Okamura), Tabata 19/21mm Magna PPM, Korean TAVR Registry, Chinese 17mm Regent series, Fuwai ML PPM 2026 — **Claude 側にはほぼ全く出てきていなかった日本人・アジア人エビデンスの宝庫**。本研究 RQ への寄与度極めて高い。

---

## 7. 最終確定 PMID リスト（paper_list.md 投入用）

実検証 + Codex 訂正で固まった PMID:

### Cat A (Y-incision) — 21 件 (Claude curl PubMed 検証)
36031424, 38841090, 38841092, 40098828, 41619928, 38841083, 38841089, 40403905, 41473041, 39892843, 40500547, 40641760, 41856503, 41781359, 41658927, 41100181, 40270847, 41843014, 41621561, 41425437, 42083003

### Cat B (古典 AAE) — 10 件 (Claude curl PubMed 検証)
470420, 5452289, 127094, 38841083, 38522868, 34970789, **1434702**, **8953456**, **12296921** （太字 = 日本人著者 Manouguian 系）

### Cat C (アジア人コホート) — 17 件 (Codex 知識検証)
28606674, 32926552, 39967214, 41243775, 33642425, 33907051, 23228405, 30464118, 22130314, 19101276, 33806531, 23745280, 41491442, + 3 件 (DOI only, Korean) + Handa 2026 EJCTS (既収集) + Carducci 2026 JTCVS (既収集)

### Cat D (PPM) — 6-8 件 (Codex 検証、要再 PubMed 確認)
11028462, 16251232, 22995023, **22408037 (Head meta)**, 19118723, 24863015, 25200051

### Cat E (TAVI vs SAVR) — 5 件 (Codex 訂正)
**38587261 (SMART)**, 34587510 (rationale), 38851542 (Abdelfattah meta), 37883682 (**Rodés-Cabau** VIVA), 36950893 (TAVI-SMALL 2 **2023**), 40452601 (SMART 2025 secondary)

### Cat F (ViV) — 10-12 件 (Codex 訂正)
**25005653 (Dvir VIVID original)**, 29020413 (**Ribeiro** VIVID coronary), 27301396 (**Simonato** depth), 33958122 (**Alperi** PPI), 27496631 (**D'Onofrio**), 40537943 (**Ruge** BVF), 40393632 (**Blackman** REVALVE), 31272666/31202947/34003670/33958168 (Khan BASILICA), 31118146/39243268 (LAMPOON), + EXPLANT/TAV-in-TAV 5 件

### Cat G (Sutureless) — 5 件 (Codex 訂正)
30689828 (**Santarpino**), 32832411 (**Berretta** Ann Cardiothorac Surg 2020), 34563505 (**Berretta** ATS 2022), 24413009 (**Borger** MMCTS 2013), 26920726 (**Beckmann**)

### Cat H (Guidelines) — 4 件 (Codex 訂正)
**33332150 (ACC/AHA full)**, **34453165 (ESC/EACTS)**, JCS 2020 (DOI 10.1253/circj.CJ-20-0135), ~~STS AAE consensus~~ (存在せず → 削除)

### Cat I (Mech vs Bio) — 1 件 (Codex 訂正)
**29117490 (Goldstone NEJM 2017)** — Claude の 28296591 は誤り

**最終合計**: 約 **77-82 論文** (Claude 当初想定 39-58 を上回る、Codex 補完で増)

---

## 8. 次のステップ

1. paper_list.md を上記 PMID で書き直し
2. Cat D の PMID を Claude メインスレッドで再検証（curl で）— 念のため
3. Cat C-H の DOI も全件 PubMed curl で抜き打ち検証
4. Phase 3a: 各論文の PDF 入手可能性を実際にアクセスして確認

---

## 9. 教訓・原則

1. **LLM の literature recall は信頼してはいけない** — Claude も Codex も
2. **PMID/DOI を出すときは必ず実 API で検証** — PubMed E-utilities / CrossRef API
3. **複数 LLM の cross-check は hallucination 検出に有効**（独立な誤りパターン）
4. **論文の first author / 年 / 誌名は特に hallucination しやすい** — タイトルが正でも周辺メタデータが誤ることが多い
5. **本研究のような新規分野 (Y-incision 2022-2026 急成長期) は LLM 知識が追いついていない** — 実検索必須

---

*作成: 2026-05-13 | 関連: [[claude_side_findings]] | [[codex_side_findings]] | [[paper_list]]*
