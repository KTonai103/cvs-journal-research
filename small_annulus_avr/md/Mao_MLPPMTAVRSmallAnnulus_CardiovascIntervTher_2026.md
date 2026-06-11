---
title: "Clinical significance of machine learning algorithm in predicting PPM during TAVR in small annuli"
authors: "Mao Y, Liu Y, Zhai M, Jin P, Li W, Chen F, Yang Y, Zhang G, Liu J, Guo Y, Pan X, Wu Y, Yang J"
journal: "Cardiovascular Intervention and Therapeutics"
citation: "Cardiovasc Interv Ther 2026;41:402-413"
doi: "10.1007/s12928-025-01215-5"
pmid: "41491442"
pdf: "[[small_annulus_avr/Reference/CatC_AsianCohort/Mao_MLPPMTAVRSmallAnnulus_CardiovascIntervTher_2026.pdf]]"
tags:
  - small-annulus
  - tavi
  - chinese-cohort
  - asian-cohort
  - ppm
  - cohort
date: 2026-05-16
category: "アジア人コホート"
journal-abbr: "CardiovascIntervTher"
paper-type: "中国 multi-center 後ろ向き観察 + ML algorithm 開発"
annulus-size: "perimeter <72 mm or area <400 mm² (CT)"
patient-bsa: "1.68 m² (中央値; IQR 1.58-1.81)"
valve-type: "SE 82.8%, BE 17.2%"
enlargement-technique: "N/A (TAVR)"
asian-cohort: yes
ppm-rate: "Severe PPM (TTE-based, iEOA<0.65): cutoff PGAV 61.2 mmHg; XGBoost 補正後 cutoff 46.5 mmHg"
viv-discussion: no
sample-size: "n=273 (internal derivation) + n=118 (external validation)"
follow-up: "2 年"
---

> [!NOTE] Key Message
> 中国 5 施設 (Xijing/Fuwai/West China/GD People's 等) の小弁輪 TAVR **391 例** (273+118) で、TTE が LHC より PGAV を **9.8 mmHg 過大評価** することを定量化し、**XGBoost ML algorithm で TTE-PGAV を補正**。補正後 mean PGAV ≥68.6 mmHg が 2y composite endpoint を強く予測 (40.7% vs 16.6%, P<0.001)。**中国人 BSA 1.68 m² と「アジア人」中でも比較的大きめ cohort** で、TTE-based PPM 評価の限界を示し、ML による補正を提唱。

---

## 1. 背景・問題設定

- TAVR 後の PPM は EOAi で評価されるが、**小弁輪では TTE が PGAV を過大評価**することが知られる (modified Bernoulli equation の限界, severe annular calcification, LV systolic dysfunction)。
- LHC が gold standard だが侵襲。Hemodynamics 評価の精度向上が中国・アジア small annulus TAVR の喫緊課題。

## 2. 患者集団

- 5 high-volume 中国施設 (Xijing, Fuwai, West China, Guangdong People's etc.) 2020-2021
- Internal derivation: n=273; External validation: n=118
- 年齢 73 歳, 男性 52.0%
- BMI 25 kg/m², **BSA 1.68 m² (中央値, IQR 1.58-1.81)** — 日本/韓国より大きく中国人として典型
- Small annulus: CT perimeter <72 mm or area <400 mm²
- Mean annular area 345.5 mm² (IQR 325-367)
- EOAi 0.46 cm²/m², 重症 AS
- NYHA III以上 90.8%, STS 5.10%
- THV: SE 82.8% (主に supra-annular), BE 17.2%

## 3. 手技詳細

- 標準的 TAVR (transfemoral 主体)
- Predilation 78.4%, Postdilation 42.5%
- Oversizing (perimeter ≥15%) 61.2%
- 同手技で TTE と LHC を**同時計測**しトレーニングデータ取得
- XGBoost algorithm 入力変数: LVEF, LVESV, peak velocity, LV mass index, LA volume index, mean PGAV, EOAi, STJ diameter

## 4. アウトカム

| Outcome | Result |
|---|---|
| 30-day all-cause mortality | 1.5% (in-hospital) |
| Stroke (in-hospital) | 1.1% |
| New pacemaker | **8.7%** |
| AKI | 4.0% (acute kidney failure) |
| Major vascular complication | 2.9% |
| Severe PPM (TTE iEOA<0.65) — mean PGAV cutoff | 61.2 mmHg |
| Severe PPM (XGBoost-corrected) — mean PGAV cutoff | **46.5 mmHg** |
| Moderate PPM — XGBoost cutoff | 36.8 mmHg |
| Mean gradient postop (TTE) | 11.0 (IQR 6.0-18.5) mmHg |
| Mean gradient (LHC) | -2.0 mmHg (TTE 過大評価 9.8 mmHg) |
| EOAi postop | 0.90 (IQR 0.62-1.09) cm²/m² |
| 2y composite endpoint (death + HF rehosp) | 26.8% (95%CI 23.7-32.5) |
| Predicted mean PGAV ≥68.6 mmHg | 2y composite **40.7% vs 16.6% (P<0.001)** |
| 1y survival | NR |
| 5y survival | NR |
| 10y survival | NR |

## 5. 議論ポイント

- TTE は LHC より PGAV を 9.8 mmHg (中央値 11.3%) 過大評価
- 小弁輪では LVOT 計測精度が低く、severe annular calcification で誤差増大
- XGBoost (8 変数) は LHC との R=0.94 まで予測精度を改善
- Mean PGAV 68.6 mmHg を cutoff にすると 2y outcome を二分する識別性能を獲得
- 中国 Fuwai (national center) 含む multicenter で external validation も成功 (R=0.87)
- 注意: severe annular calcification + 中国人体格では Asian-specific のキャリブレーションが必要

## 6. 本研究RQへの含意（最重要）

- **Primary RQ**: TAVR後の hemodynamics 評価において **TTE が小弁輪では系統的に過大評価**する事実は、AAE-SAVR と TAVR の outcome 比較で TTE 単独データを使う研究の精度を疑わせる。Asian small annulus cohort の PPM rate は TTE-based ではすべて過大評価されている可能性。
- **Secondary RQ (19mm 許容性, initial sizing)**: 中国人 BSA 1.68 m² でも annulus 345.5 mm² (≈ 21mm) の小弁輪 cohort で PPM cutoff が変動。**XGBoost-corrected mean PGAV ≥68.6 mmHg = 真の severe PPM** という新規定義が提案された。Initial sizing で過剰恐怖を避けるための tool。
- **Tertiary RQ (Asian-specific 戦略)**: ★ **中国 cohort BSA 1.68 m²** は本研究 RQ の中で「アジアでも比較的大きめ」のスペクトラム端を提示。日本人 (Meguro J-TVT 1.34 m², Kamioka 1.38 m²) と韓国人 (Lee 1.5, Moon 1.5 m²) より大きい。「アジア人小体格」を一括りにできないことを示すデータ。中国 Fuwai を含む multicenter で SE 弁 82.8% 使用 → 中国 TAVR 慣行は SE 寄り。

## 7. 限界

- TTE/CTA 以外の変数 (annular calcification grade 等) を含めず精度上限
- 極度に低い PGAV (<20 mmHg) は除外 → 全 cohort 適用不可
- XGBoost cutoff 68.6 mmHg は探索的、prospective validation 未実施
- Asian/Chinese 特有データで他人種への generalizability 不明
- 観察研究で confounders 完全制御不能

## 8. 引用文献ハイライト

1. Okuno T et al. JACC Cardiovasc Interv 2019;12:2173-82. Supra vs intra-annular PPM (本研究の理論基盤)
2. Ternacle J et al. JACC Cardiovasc Interv 2021;14:1466-77. PARTNER 2 PPM
3. Herrmann HC et al. J Am Coll Cardiol 2018;72:2701-11. STS/ACC TVT PPM
4. Mohty D et al. Circulation 2006;113:420-6. PPM 長期生存 (本研究 RQ Cat D 関連)
5. Miyasaka M et al. JACC Cardiovasc Interv 2018;11:771-80. OCEAN-TAVI Asian PPM
