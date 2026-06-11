---
title: "Modeling the Hemodynamic Impact of Y-incision Aortic Annular Enlargements on Aortic Valve Replacement and Valve-in-Valve Procedures"
authors: "Mia Bonini, Surya Sanjay, Maximilian Balmus, Alexander Makkinejad, Katelyn Monaghan, Marc Hirschvogel, Nicholas Burris, Bo Yang, David Nordsletten"
journal: "Journal of Cardiovascular Translational Research"
citation: "J Cardiovasc Transl Res 2025;18:876-887"
doi: "10.1007/s12265-025-10634-x"
pmid: "40500547"
pdf: "[[small_annulus_avr/Reference/CatA_YIncision/Bonini_HemodynamicModelingYIncisionAAE_JCardiovascTranslRes_2025.pdf]]"
tags:
  - small-annulus
  - savr
  - y-incision
  - aae
  - viv-tavr
  - modeling
date: 2026-05-16
category: "弁輪拡大術"
journal-abbr: "JCardiovascTranslRes"
paper-type: "modeling"
annulus-size: "19-25mm"
patient-bsa: "1.9-2.3 m²"
valve-type: "bioprosthetic"
enlargement-technique: "Y-incision"
asian-cohort: no
ppm-rate: "NR (modeling study)"
viv-discussion: yes
sample-size: "n=15 patient-specific CFD models (12 SAVR + 3 ViV)"
follow-up: "NA"
---

> [!NOTE] Key Message
> Y-AAE+SAVR の patient-specific CFD modeling (n=15)。Y-AAE で peak velocity -39.3%、mean TPG -87.2%、ViV-TAVR 設定で peak velocity -55%、TPG -92% と劇的改善。**blood residence time (thrombosis proxy) は増加せず**、large root + large valve の懸念を bioengineering で否定。

---

## 1. 背景・問題設定
SAVR では 54-65% で PPM が発生し TPG 上昇・LVH・拡張機能不全につながる。ViV-TAVR は alternative だが PPM 残存が問題。Y-AAE は initial SAVR で大型弁を留置可能だが、large sinus → 流速低下 → blood stasis/thrombosis 増加の懸念。本研究は CFD modeling で Y-AAE の hemodynamic 効果と thrombosis risk を定量化。

## 2. 患者集団
- 15 patient-specific 3D model: 12 SAVR + 3 ViV
- 4 matched groups: (1) Y-AAE+SAVR n=4 (2) virtualSAVR n=4 (3) matchedSAVR n=4 (4) TAVR-in-SAVR variants n=3
- Y-AAE 群: median 66 歳、女性 75%、BSA 2.2 m²、BMI 38、native annulus 23mm、implanted size 29
- matchedSAVR 群: median 64 歳、女性 75%、BSA 2.0 m²、BMI 32、native annulus 22mm、implanted size 23
- BAV 50% (両群)、prior cardiac surgery 0%、severe AS

## 3. 手技詳細
- Pre/postop CT angiography で 3D root anatomy reconstruction、tetrahedral volume mesh (1mm)
- Magna Ease bioprosthetic valve, virtual implantation で virtualSAVR control 構築
- CoreValve virtual deployment で TAVR-in-SAV scenario 構築 (commissures aligned, 4mm below SAVR bottom)
- CFD: Navier-Stokes (CHeart finite-element solver)、blood ρ=1.026 g/ml、μ=0.004 Pa·s
- Boundary conditions identical: HR 70 bpm、stroke volume 73.5 ml
- 3 cardiac cycles で convergence、residence time は 14 cycles 計算

## 4. アウトカム

| Outcome | Y-AAE+SAVR vs SAVR controls |
|---|---|
| 30-day mortality | NA (modeling) |
| Peak velocity reduction | -39.3% (vs virtualSAVR -41.1%, vs matchedSAVR -37.5%) |
| Mean TPG reduction | -87.2% (-86.5 to -87.9%) |
| Mean residence time | -10.3% reduction (vs matchedSAVR -15.1%) |
| Maximum RT | No consistent difference |
| Volume with RT>0.2 | Group-dependent (some higher, some lower) |
| **TAVR-in-SAV peak velocity** | **-55%** (Y-AAE post-ViV vs control pre-ViV) |
| **TAVR-in-SAV mean TPG** | **-92%** |
| Post-TAVR sinus RT increase | Y-AAE 0.0001%→3.4%, virtualSAVR 0.02%→4.6%, matchedSAVR 0.06%→5.4% |
| Mean RT increase post-TAVR | +31% all models |
| GOA reduction post-TAVR | -17.2% (Y-AAE), -23.3% (vSAVR), -20.7% (mSAVR) |

## 5. 議論ポイント
- Y-AAE+SAVR は systole に lower jet velocity と wider jet → shear stress 低、blood damage 減
- TPG 大幅減 → 心負担軽減、SVD risk 低下 (Johnston 2015 連動)
- 「large sinus で stasis 増」懸念は CFD で**否定**: mean RT は Y-AAE で寧ろ低、max RT 差なし、80% volume は 3 cycles で washout
- TAVR-in-SAV: Y-AAE 群でも post-TAVR は sinus RT 増加するが、絶対値は Y-AAE 群が control より低
- 3 年 echo follow-up と一致 (Yang JTCVS 2024 で thrombosis なし)

## 6. 本研究RQへの含意（最重要）
- **Primary RQ**: Y-AAE+SAVR の **hemodynamic 優位性 (TPG -87%, peak velocity -39%) を mechanism level で実証**。「Y-AAE は thrombosis risk を増やす」批判への bioengineering 反証。狭小弁輪 SAVR の最適化戦略として Y-AAE を支持する mechanistic evidence。
- **Secondary RQ (ViV用 initial sizing)**: **ViV-TAVR 設定で Y-AAE 群が peak velocity -55%, TPG -92%** という劇的優位性を示し、initial SAVR で Y-AAE 実施が **future ViV 成績を mechanism として改善**することを定量化。Kherallah 2023 の「ViV 後高 gradient は 1y mortality・stroke・MI・reintervention 増」基準を踏まえ、Y-AAE が long-term lifetime management で優位と結論。
- **Tertiary RQ (Asian-specific)**: BSA 1.9-2.3 m² は Western 集団。Asian (BSA <1.6) では sinus geometry/flow がさらに critical で本 modeling の外挿は要検証。ただし mechanism-based finding は普遍的。

## 7. 限界
- N=15 (4 quartets) と小規模、static anatomy (脈動なし)、boundary conditions 固定
- Valve leaflet dynamics 単純化 (orifice plane)、wall rigid 仮定
- RT = thrombosis surrogate、shear stress は未評価
- Aortic root wall mechanics・internal stress は未検討
- Bo Yang 自身が著者 → potential confirmation bias

## 8. 引用文献ハイライト
- Yang B, JTCVS 2024 (seminal Y-AAE n=50)
- Makkinejad A, Ann Cardiothorac Surg 2024 (Y-incision vs traditional AAE)
- Dvir D, Circ Cardiovasc Interv 2015 (ViV coronary obstruction risk)
- Rodés-Cabau J, Circ Cardiovasc Interv 2014 (PARTNER annulus size & hemodynamics)
- Hatoum H, JTCVS 2017/2019 (TAVR sinus flow stasis)
- Kherallah RY, Circ Cardiovasc Interv 2023 (post-ViV high gradient & 1y outcome)
- Johnston DR, ATS 2015 (12,569 implants long-term durability)
