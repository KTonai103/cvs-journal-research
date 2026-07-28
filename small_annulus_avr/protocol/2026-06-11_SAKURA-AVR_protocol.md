---
title: "SAKURA-AVR 研究プロトコル — 日韓多施設 狭小弁輪 SAVR 戦略比較コホート"
subtitle: "Small Annulus aortic valve replacement: Korea–japan United Research Analysis"
acronym: SAKURA-AVR
version: 0.2 (draft for collaborator review)
date: 2026-06-11
revised: 2026-07-25
status: draft
design: retrospective multicenter comparative cohort (ambispective-extensible)
sites: ["Osaka University", "NCVC (国立循環器病研究センター)", "Korean center #1", "Korean center #2"]
corpus: "small_annulus_avr/ (69 papers + 統合レビュー)"
related:
  - "[[../md/_IntegratedReview_SmallAnnulusAVR_2026]]"
  - "[[../_index]]"
tags: [protocol, small-annulus, savr, aortic-annulus-enlargement, ppm, asian-cohort, multicenter]
---

# SAKURA-AVR 研究プロトコル（草案 v0.1）

> **Small Annulus aortic valve replacement: Korea–japan United Research Analysis**
> 日韓多施設・後ろ向き比較コホート研究プロトコル
> 作成: 2026-06-11 / **改訂 v0.2: 2026-07-25** / ステータス: **共同研究者レビュー用 draft**
>
> **v0.2 の変更点**（すべて原典 PDF の再確認に基づく）:
> ① §1.1 のガイドライン記述を訂正（ESC/EACTS は PPM を **TAVI** 支持因子としている）
> ② §1.2.1 を新設 — 先行研究の AAE 生存優位が **BSA をそろえると消失**することを同定し、本研究の存在理由として明示
> ③ §1.5 を新設 — AM curtain「8mm」の出自（未発表 n=40）と計測法未標準の問題
> ④ §4.4・§7.1・§7.5-6 に **BSA の統制と交互作用検定**を設計として組み込み
> ⑤ §12 に open item ⑧（BSA 閾値）・⑨（curtain 計測法）を追加

本プロトコルは `small_annulus_avr/` 統合レビュー（69本精読）が同定したエビデンス・ギャップ §10.2 のうち、**「Asian小体格における AAE-SAVR vs no-AAE SAVR の直接比較が存在しない」**（ギャップ①③④）を、当コンソーシアムが保有する臨床データで埋めることを目的とする原著研究の設計書である。

---

## 1. 背景と研究の根拠（Rationale）

### 1.1 臨床的問題

Yang ら（Univ Michigan）の **Y-incision aortic annular enlargement (AAE)**（JTCVS 2024）を契機に、欧米では「狭小弁輪に 3–4 弁サイズ大の人工弁を植え込み、severe PPM を回避し将来の ViV-TAVR margin を確保する」"Bigger is better" パラダイムが急速に標準化しつつある。

**しかしガイドラインはこのパラダイムを支持していない**（2026-07 に一次資料で再確認）。狭小弁輪＋予想 severe PPM の扱いは 3 文書で次のように分かれる:

| ガイドライン | 該当箇所 | 方向 |
|---|---|---|
| ACC/AHA 2020 | Table 14 "Prosthetic valve preference" | **Favors SAVR** — "Concern for patient–prosthesis mismatch (annular enlargement might be considered)"。ただし同一行の TAVI 列に "TAVI provides larger valve area than same size SAVR" を併記 |
| ESC/EACTS 2021 | Table 6 | **Favours TAVI** — "High likelihood of severe patient–prosthesis mismatch (AVA <0.65 cm²/m² BSA)" が ＋TAVI ／ −SAVR |
| JCS 2020 | Table 33 | **TAVI should be considered** — "Small annulus highly expected patient-prosthesis mismatch" |

すなわち **弁輪拡大を明示的に指しているのは ACC/AHA のみで、3 文書中 2 つは同じ患者を TAVI へ送る**。なお ESC・JCS とも「PPM が予想される」と「TAVI デバイスが入らない弁輪」を別項目として区別しており、後者のみを SAVR 支持因子としている。

年齢軸では評価が逆転する。ESC/EACTS は **<75 歳かつ低リスクで SAVR（Class I, B）**、ACC/AHA は **<65 歳で SAVR（Class 1, A）・65–80 歳は shared decision** であり、**ESC のほうが SAVR の守備範囲が広い**。JCS には SAVR vs TAVI を年齢で振り分ける格付け推奨自体が存在せず、本文で「明確な cutoff は設けず、≥80 歳で TAVI・<75 歳で SAVR を優先順位の目安とする」と述べるにとどまる。狭小弁輪の日本人・韓国人女性は 65–75 歳に多く、**ESC 基準では「外科の患者」でありながら、その ESC が PPM を理由に TAVI へ送る**という捻れが生じる。

さらに ESC/EACTS Figure 4（重症 AS の管理アルゴリズム）の分岐は年齢・手術リスク・経大腿アクセス可否のみで、**弁輪サイズも PPM も登場しない**。ガイドラインのアルゴリズム本体は、本研究の対象患者について実質的に何も述べていない。

この乖離の背景には、欧米コホート（BSA ≥1.8 m²、annulus mean 21mm）と Asian 小体格（BSA 1.3–1.5 m²、annulus 17–20mm）の前提の差があると考えられる。

> **訂正記録（2026-07-25）**: 本項は当初「ACC/AHA 2020・ESC/EACTS 2021 は root enlargement を narrative で支持する／JCS のみ TAVI を推奨」と記述していた。原典 PDF を画像で確認した結果 **ESC/EACTS Table 6 は PPM を TAVI 支持因子としており、当初記述は誤り**であった。原因は `pdftotext` が Table 6 の ＋/− 記号を「1」「2」という数字として出力し、これを rating と誤読したことによる。記号を含む表は必ずページ画像で確認すること。

### 1.2 何が未解決か（統合レビューが同定したギャップ）

- **Y-incision/AAE vs no-AAE SAVR の直接比較 RCT が存在しない**（観察研究 PSM のみ、いずれも単施設・欧米）。
- **Asian 小体格における AAE の中期成績データがない**（Wang Fuwai n=53 が最大、早期のみ）。
- **AAE 後の僧帽弁機能/MR の系統的データがない**（Özçelik による severe central MR 初報告のみ）。なお同報告の症例の aortomitral curtain は TTE 実測 **17–18mm** であり、本邦で流布する「8mm」より長い。**「curtain が短いから MR が起きる」という単純な因果は現時点で成立せず、計測法の標準化自体が未解決である**（§1.5 参照）。
- **【2026-07 追加・本研究の設計を規定する最重要ギャップ】既存の AAE 生存優位シグナルは、体格交絡と分離されていない。**

#### 1.2.1 Makkinejad 2025 の生存優位は BSA をそろえると再現しない

本テーマに最も近い先行研究 Makkinejad ら（Ann Thorac Surg 2025）は、弁輪径をマッチさせた ≤23mm コホート（PSM 112 pair）で **6 年生存 98% vs 74%（P=.016）**、Cox で **AAE が独立保護因子（HR 0.19, 95%CI 0.06–0.62, P=.006）** と報告し、AAE 支持の最強エビデンスとされている。

しかし原典を精読すると、次の 4 点が判明する（いずれも同論文の記載に基づく）:

1. **傾向スコアマッチングに BSA が含まれていない。** マッチ変数は弁輪径（術中実測）・年齢・性別・糖尿病・慢性肺疾患・透析・EF・再手術歴・適応・高血圧・脂質異常症・弁種・脳卒中既往・心筋梗塞既往・緊急度であり、**BSA は入っていない**。結果として両群の BSA は **2.1 vs 1.9 m²（P<.001）** と有意に異なる。
2. **著者自身の感度解析で、BSA をマッチ変数に加えると 6 年生存 98% vs 73%、P=.067 となり有意差が消失する**（Supplemental Figure）。著者は "due to decreased sample size" と説明している。
3. **BSA の共変量推定値自体がきわめて不安定**（HR 5.77, 95%CI **1.02–32.8**）。CI が 30 倍の幅を持ち、体格の予後への寄与を精度よく推定できていない。
4. **6 年時点の at-risk は 35 例と 14 例**まで減少しており、生存曲線の右端は少数例に依存する。

**解釈にあたっての注意（重要）**: BSA 不均衡の向きは AAE 群のほうが大きく、BSA の点推定（HR 5.77）を額面どおり取れば AAE 群は不利を背負っていたことになる。したがって「体格交絡が AAE の見かけの効果を作り出した」と**単純に断ずることはできない**。しかし同時に、**著者自身の BSA マッチ解析が非有意に転じている**以上、体格を含む適応バイアスの影響を**否定することもできない**。

到達可能な結論は次の一点に尽きる —— **この生存優位は解析仕様の変更に対して頑健でなく、体格を揃えたコホートでは示されていない。** AAE の生存への寄与が (a) 拡大術そのものの効果なのか、(b) 患者選択に伴う適応バイアスなのかは、**現存する最良の先行研究をもってしても分離できていない**。

**これが本研究の存在理由である。** 判定には「体格が設計段階で揃っており、かつ十分な検出力を持つコホート」が要る。Makkinejad の BSA マッチ解析が失敗したのは主として **N の不足**であり、これは**体格分布が均質な集団を母集団とすれば構造的に回避できる**。小体格に偏った母集団を保有しているのは Asian コホートだけである。本研究は §7.1 で BSA を必須マッチ変数とし、§7.5-6 で BSA 制限感度解析と **BSA × AAE 交互作用の事前規定検定**を置くことで、このギャップに正面から答える設計とする。

### 1.3 新規性の確認（2026-06 時点）

最新文献検索の結果、Asian 多施設で外科的 **AAE vs no-AAE SAVR** を血行動態・中期予後で直接比較した研究は**存在しない**。近接研究はいずれも対象が異なる:

- East Asian の TAVI device 選択（self vs balloon、supra vs intra-annular）— JACC: Asia 2024 ほか。
- Sutureless SAVR vs TAVI（multi-institutional, 2024）。
- BE-TAVI small vs large annulus（2026, n=3,182; small で mean PG ≥20mmHg 14.1% vs 2.9%、severe PPM 9.8% vs 5.2%）。

→ **外科戦略（AAE か否か）を Asian 小体格で比較する空白は開いたまま**であり、本研究が初となる。

### 1.4 必須追加文献（**取得・要約済み 2026-06**）

以下は corpus 未収載だった必須文献で、**2026-06 に取得・精読 MD 化して corpus に統合済み**（[[../_index]] §5「2026-06 追加」）:

1. **Sá MP et al. JAHA 2024**（[[../md/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024]]）— SAVR 後 PPM の reconstructed time-to-event meta（**122,989例・592,952 patient-years**）。Head 2012 を更新。severe 20yr 全死亡 HR 1.29・心臓死 HR 2.04。**primary outcome（severe PPM 回避）の臨床的正当化**。
2. **VARC-3 2021**（[[../md/Genereux_VARC3EndpointDefinitions_EHJ_2021]]）— エンドポイント標準化（PPM・HVD/SVD・出血）。
3. **Makkinejad AnnThoracSurg 2025**（[[../md/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025]]）— **本研究に最も近い先行研究**：matched ≤23mm 弁輪で AAE vs isolated AVR を PSM 112 pair 比較、6yr 生存 98% vs 74%・AAE 中期死亡 HR 0.19。SAKURA が補完すべき gap（measured-EOA PPM co-primary・Asian small-body・TAVI reference・postop echo 完備）を明確化。
4. **Tanaka AnnCardiothoracSurg 2024**（[[../md/Tanaka_AorticAnnularEnlargementOutcomesMetaAnalysis_AnnCardiothoracSurg_2024]]）— AAE メタ解析：マッチ後死亡差なし・**severe PPM RR 0.61**。AAE アームの morbidity/mortality ベンチマーク。
5. **Abushouk JACC CI 2023**（[[../md/Abushouk_MeasuredVsPredictedPPM_JACCCardiovascInterv_2023]]）— measured vs predicted iEOA：予測は PPM を系統的過小評価。**co-primary を measured iEOA とする設計の citable authority**。
6. **RHEIA / Tchétché EHJ 2025**（[[../md/Tchetche_RHEIAtrialTAVIvsSAVRWomen_EHJ_2025]]）— 女性限定 TAVI vs SAVR RCT。外科群は AAE ゼロ＝実質 no-AAE 対照。TAVI 参照アームの最良級 RCT ベンチマーク。
7. 比較考察用: [[../md/Suruga_SmallVsLargeAnnulusBalloonExpandableTAVR_JAHA_2026]]（BE-TAVR small vs large）、[[../md/DiBacco_SuturelessVsTAVISmallAnnulusMultiInstitutional_BrazJCardiovascSurg_2024]]（sutureless vs TAVI）、[[../md/Chen_EastAsianTAVRdeviceSelectionSmallAnnulus_JACCAsia_2025]]（East Asian device 選択）。
8. 統計方法論（CatJ_Methods）: E-value（[[../md/VanderWeele_EValueSensitivityAnalysis_AnnInternMed_2017]]）、PSM バランス診断 SMD<0.1（[[../md/Austin_PSMbalanceDiagnostics_StatMed_2009]]）、STROBE（[[../md/vonElm_STROBEStatement_PLoSMed_2007]]）。

**未取得（DL困難・後日）**: Yamamoto EuroIntervention 2025（PCRログイン／PMC OA 2026-11-14解除）、Do-Nguyen ACTA 2026（SAGE）。

### 1.5 aortomitral curtain「8mm」の出自と、計測法が未標準であること（2026-07 追加）

本研究の解剖学的前提として繰り返し引用される「日本人の aorto-mitral (AM) continuity は約 8mm、Caucasian は 12–15mm」という対比には、**原典に遡ると重大な留保が必要**である。

**「8mm」の出所**は Maekawa ら（Artif Organs 2002）の本文一文であり、原文は次のとおり:

> "the distance between the 2 valves before operation is equal to the length of the AM continuity which is about 8 mm in Japanese patients (**unpublished data on 40 adult healthy cases in our institution by means of transthoracic echocardiography**)"

すなわち **①未発表データ ②健常成人 40 例 ③経胸壁エコー ④2002 年**の値であり、査読を経た計測研究の結果ではない。**本プロトコルおよび関連発表において、この値を確立した解剖学的定数として扱ってはならない。**

さらに **Özçelik 2026（Y-incision 後 severe central MR の初報告）の症例では、TTE 実測の aortomitral curtain が 17–18mm** と報告されている（同論文 Figure 3）。同論文は機序として "short native aortomitral curtain" を挙げるが、**実測値は「8mm」の 2 倍以上**である。両者が同一の指標を測っているのか（計測断面・収縮期/拡張期・モダリティが異なる可能性）は原典からは判定できない。

**結論として、現時点で言えるのは次の 2 点にとどまる。**

1. AAE 後に僧帽弁機能障害は起こりうる。機序は curtain とパッチの幾何に関係する（Özçelik Figure 4 の模式図）。
2. **AM curtain の計測法は標準化されておらず、アジア人集団での多施設実測データは存在しない。**

したがって本研究では、「curtain が短いから危険」という因果を前提とせず、**AM curtain 長を統一プロトコルで実測する変数として eCRF に組み込む**（§8）。4 施設で計測法を合意し実測すること自体が、**現在世界に存在しないデータの創出**であり、独立した副次的成果となる。計測法の定義は §12 open item ⑨で確定する。

---

## 2. 研究目的と仮説

### 2.1 Primary objective

狭小弁輪（measured annulus diameter ≤23mm、≤21mm を主要層）かつ小体格の AS 患者で、**AAE-SAVR は no-AAE SAVR と比較して severe PPM を減らし術後 mean gradient を低下させるか**を、日韓多施設データの傾向スコア調整下で定量する。

### 2.2 Primary hypothesis（co-primary、階層的検定）

- **H1（血行動態）**: AAE-SAVR は no-AAE SAVR と比較して **severe PPM 率が低い**（measured iEOA ≤0.65 cm²/m²、術後退院前/30日 echo）。
- **H2（血行動態）**: AAE-SAVR は no-AAE SAVR と比較して **1年 mean transvalvular gradient が低い**。
- 検定順序: H1 → H2 の階層的（gatekeeping）。H1 有意でなければ H2 は探索的扱い。

### 2.3 Secondary / safety objectives

- **主要副次（臨床）**: 中期（最長5年）全死亡・MACE を Cox/Kaplan–Meier で比較。
- **安全性副次（事前規定・Özçelik signal）**: AAE 群における **新規 ≥moderate MR 発生率・僧帽弁再介入率・僧帽弁幾何（available なら echo 指標）**。AM continuity が短い Asian 解剖での AAE 安全域を検証する本研究固有の論点。
- **参照比較（TAVI arm）**: self-expanding TAVI を事前規定の参照群とし、血行動態（severe PPM、mean gradient）を no-AAE / AAE 各群と記述的＋IPTW 補正下で比較（因果結論ではなく landscape 提示）。
- **探索的**: ViV feasibility surrogate（植込み弁 internal diameter ≥21mm 達成割合、D'Onofrio 2016 閾値）、PPI 率、AAE 群の術式別（Nicks/Manouguian/Y-incision/Y-and-I）サブ解析。

---

## 3. 研究デザイン

- **デザイン**: 後ろ向き多施設比較コホート（第1弾）。将来の前向き registry 拡張を見据えた ambispective-extensible 設計。
- **施設**: 阪大、NCVC、韓国2施設（計4施設、日韓）。lead/coordinating center は別途決定。
- **観察期間（症例登録対象）**: **2015-01-01 〜 2024-12-31（10年）**。理由＝modern bioprosthesis（Inspiris 2017–、Avalus）、Evolut/Sapien 3、および Y-incision（2021–）の時代を包含。
  - 注意: Y-incision は 2021 年以降に偏るため、**暦年を共変量＋感度解析で調整**（§7.5）。
- **追跡**: 各施設の最終 echo・生存情報まで。最低 1 年 echo を血行動態 co-primary の窓とする。

---

## 4. 対象集団

### 4.1 包含基準

1. 成人（≥18歳）。
2. **狭小弁輪**に対する初回 AVR（SAVR または TAVI）。狭小弁輪の定義（harmonized、§4.3）:
   - SAVR: 術中サイザー実測 or 術前 CT/TTE で **aortic annulus diameter ≤23mm**（**≤21mm を事前規定の主要層**）。
   - TAVI: CT 計測 **annulus area ≤430mm²**（SMART 基準）または derived diameter ≤23mm。
3. 主病態が **大動脈弁狭窄（AS 優位、AS/AR mixed 含む）**。

### 4.2 除外基準

- 活動性感染性心内膜炎、急性大動脈解離。
- **大動脈基部置換（Bentall/root replacement）**、David/Yacoub。
- **同時施行の他弁手術（僧帽弁・三尖弁置換/形成）**（※ CABG 同時は許容、共変量化）。
  - 例外検討: AAE + concomitant MV は corpus の重要トピック（Cangut/Gan）だが、主要解析の arm 純度を保つため**主要解析から除外し、別途記述**。
- 純粋 AR（AS 要素なし）、先天性/小児、redo（既存人工弁に対する手術＝ViV/explant は別解析）。

### 4.3 狭小弁輪定義の調和（方法論的論点）

SAVR（術中サイザー/外科弁ラベルサイズ）と TAVI（CT annulus area）で計測モダリティが異なる。**各症例の生データ（measured annulus diameter, area, 計測法）を eCRF に記録**し、解析時に diameter ベースで統一。主要解析は SAVR 2 群間（同一モダリティ）で行うため、この調和問題は TAVI 参照比較に限局する。

### 4.4 なぜ BSA を包含基準にしないのか（設計判断・2026-07）

本研究は「小体格」を主題としながら、**包含基準は弁輪径のみで定義し、BSA による患者選択は行わない**。この非対称は意図的であり、根拠は次の 3 点である。

1. **症例数の律速は AAE 群である**（§7.6）。BSA 上限を包含基準に加えると、ただでさえ少ない AAE 群がさらに減り、研究自体が成立しなくなるリスクが高い。**制限は解析段階で行うほうが、情報を捨てずに済む**。
2. **本研究の対象母集団は、そもそも BSA 分布が欧米より大きく左に寄っている。** 日韓 4 施設の狭小弁輪 AVR という設定自体が、Makkinejad コホート（BSA が AAE 群で有意に大きい米国集団）とは異なる分布を与える。すなわち**対象設定自体が体格交絡を部分的に縮小している**。
3. **BSA を連続量として保持するほうが、交互作用を検定できる。** BSA で切って対象を絞ると「AAE の効果が体格でどう変わるか」（§7.5-6b）という最も価値のある問いに答えられなくなる。**BSA は「除外するための基準」ではなく「解析するための変数」として扱う。**

ただし本判断には副作用がある。**「small-bodied Asian patients を対象とした」と論文で述べる際、その根拠は包含基準ではなく実際に集まったコホートの BSA 分布に依存する**。したがって主要論文では **Table 1 に BSA の分布（平均±SD、四分位、ヒストグラム）を必ず提示し、欧米先行研究の BSA と並べて示す**。P0 census（§9）では **各施設の狭小弁輪症例の BSA 分布を必ず集計項目に含める**こと。census の結果 BSA 分布が想定より大きい場合は、§12 open item ⑧に立ち返って包含基準の再検討を行う。

---

## 5. 曝露（アーム）定義

| Arm | 定義 | 主要解析での位置づけ |
|---|---|---|
| **Arm 1: no-AAE SAVR** | 弁輪拡大を伴わない外科的 AVR。supra-annular 生体弁、interrupted suturing、機械弁、**sutureless/rapid-deployment** を含む | **主要対比（対照）** |
| **Arm 2: AAE-SAVR** | Nicks / Manouguian / Konno / **Y-incision / Y-and-I** を伴う外科的 AVR | **主要対比（曝露）** |
| **Arm 3: TAVI（参照）** | self-expanding TAVI を主参照（BE-TAVI はサブ） | **事前規定の参照群（副次・記述）** |

**事前規定の感度解析**（§7.5）:
- 生体弁限定（機械弁除外）— 血行動態 primary を弁種で純化。
- sutureless 除外（Arm 1 を従来縫着生体弁に限定）。
- Y-incision 限定 vs 古典 AAE（Arm 2 内サブ）。

---

## 6. エンドポイント定義

### 6.1 Co-primary（血行動態）

1. **Severe PPM**: **measured iEOA ≤0.65 cm²/m²**（退院前/30日 echo）。
   - **重要な方法論的選択**: corpus の Pibarot 2020（EHJ-CI）が示す通り、**reference-chart projected EOA は約30%を誤分類**する。本研究は **doppler 実測 EOA / BSA（measured iEOA）を一次採用**し、projected iEOA は感度解析でのみ用いる。これは本研究の方法論的強みであり、査読対応の核。
2. **1年 mean transvalvular gradient**（TTE)。

### 6.2 主要副次（臨床、VARC-3 準拠）

- 全死亡（30日、1年、中期最長5年）、心臓関連死。
- MACE（死亡・脳卒中・弁関連再入院の複合）。
- SVD（VARC-HBV/VARC-3 hemodynamic valve deterioration）、弁再介入。

### 6.3 安全性副次（事前規定）

- **新規 ≥moderate MR 発生**（退院前・1年）、**僧帽弁再介入**。AAE 群で重点評価（Özçelik signal）。
- PPI（恒久ペースメーカー）、術後 AKI、脳卒中、出血（VARC-3）。

### 6.4 探索的

- 植込み弁 internal diameter ≥21mm 達成割合（ViV margin surrogate）。
- 術式別（AAE 4 法）血行動態・MR。
- CPB/遮断時間（AAE の侵襲コスト）。

---

## 7. 統計解析計画

### 7.1 主要対比と交絡調整

- **主要対比**: Arm 2 (AAE) vs Arm 1 (no-AAE)、**1:1 傾向スコアマッチング（caliper 0.2×SD of logit PS）**を主、**IPTW を感度解析**。
- バランス評価: 標準化平均差（SMD）<0.10 を目標。
- PS モデル共変量（Asian 特異性を重視）: 年齢、**性別**、**BSA**、**measured annulus diameter**、LVEF、NYHA、STS-PROM/EuroSCORE II、AF、CKD/透析、糖尿病、COPD、冠動脈疾患/同時 CABG、**暦年**、**施設**、弁種（生体/機械）。

> **BSA の扱い（§1.2.1 を受けた必須要件）**
>
> 先行研究の生存優位が BSA をそろえると消失する以上、BSA の扱いは本研究の妥当性の中核である。以下を必須とする。
>
> 1. **BSA は必ず PS モデルに入れる**（除外・事後追加を認めない）。
> 2. **マッチ後の BSA バランスを独立に報告する。** BSA の SMD、および両群の平均±SD・分布（できれば density plot）を主要論文の Table 1 に明示する。SMD <0.10 を満たさない場合はマッチング仕様を見直す。
> 3. **弁輪径と BSA は別の変数として扱う。** 両者は相関するが同一ではなく、「弁輪径をマッチしたから体格もそろっている」という仮定は Makkinejad の反例により明確に否定されている。
> 4. 本研究の対象は弁輪径で定義され（§4.1）、BSA では制限していない。これは症例数を確保するための意図的な選択である（§4.4）。したがって **BSA の統制はマッチングと §7.5 の感度解析が全面的に担う**。

### 7.2 Co-primary の検定

- 階層的 gatekeeping（H1: severe PPM → H2: 1年 gradient）で多重性を制御、両側 α=0.05。
- severe PPM: マッチ後 conditional logistic / クラスタ頑健 GEE。1年 gradient: 線形混合モデル（施設変量効果）。

### 7.3 生存・時間依存アウトカム

- Kaplan–Meier ＋ マッチ層別 Cox。competing risk（弁関連 vs 非弁関連死）には Fine–Gray。

### 7.4 欠測

- echo 欠測・追跡欠測は **multiple imputation（MICE）**。1年 echo 欠測率を記述し、complete-case を感度解析。

### 7.5 事前規定の感度・サブ解析

1. 生体弁限定 / sutureless 除外 / Y-incision 限定。
2. annulus ≤21mm 主要層に限定。
3. 暦年調整（2021 以降の Y-incision 偏りを補正）、施設別ランダム効果。
4. projected iEOA による severe PPM 再分類（measured との一致度＝Pibarot 2020 検証）。
5. TAVI 参照群 vs 各外科 arm（IPTW、記述）。
6. **【新規・§1.2.1 に対応】体格に関する 3 つの事前規定解析。** 本研究固有の貢献であり、探索的ではなく事前規定として実施・報告する。
   - **6a. BSA 制限解析**: **BSA <1.6 m²** に限定して主要対比を再実行する（閾値は §12 open item ⑧で確定。1.5 / 1.6 / 1.7 m² が候補）。これは Makkinejad の BSA マッチ感度解析を、体格の小さい集団で追試するものに相当する。
   - **6b. BSA × AAE 交互作用検定**: 主要対比のモデルに **BSA を連続量とした交互作用項**を投入し、**AAE の効果が体格によって修飾されるか**を検定する。**これが本研究の最も独自性の高い問いである** — 「AAE は誰に効くのか」に対し、体格という軸で初めて答える。有意水準は探索的多重性を考慮し交互作用 P<0.10 を signal とみなす（確証的判定はしない）。
   - **6c. BSA 三分位別のサブグループ提示**: forest plot で BSA 三分位ごとの効果推定値を示す。有意性判定ではなく効果の方向と一貫性を見るための記述。

   これら 3 解析は **co-primary の階層的検定の外側**に置き、主要結論を左右させない。ただし 6b が強い交互作用を示した場合、それ自体が独立した知見として報告に値する。

### 7.6 サンプルサイズ／検出力（暫定・要 feasibility census）

corpus 由来の効果量で暫定設計（最終値は §9 の census 後に確定）:

- severe PPM: no-AAE ≈ **15–25%**（Asian 小弁輪 SAVR; Tabata の moderate-severe 29–56% 等から保守的推定）vs AAE ≈ **5–7%**（Makkinejad PSM: 5.5%）。
  - 差 15% vs 5% を α=0.05・power 0.80 で検出 → 各群 **≈130例（計260）**。差 20% vs 6% なら 各群 ≈70。
- **制約は AAE 群の症例数**（Y-incision は 2021–）。4 施設 ×（AAE 年間例数）が律速。**§9 feasibility census で AAE 実数を最優先確認**。
- 1年 gradient（連続量）は同 N で十分な検出力（Makkinejad 7 vs 10mmHg, SD≈4）。

---

## 8. データ管理・ガバナンス

- **eCRF**: REDCap 等で共通項目を統一（annulus 生計測、弁種/サイズ/モデル、術式詳細、全 echo 時系列、追跡）。
- **匿名化**: 各施設で de-identify 後にプール。患者識別子は施設内に留置。
- **倫理**: 各施設 IRB 承認（後ろ向き・オプトアウト想定）、**日韓間データ共有契約（DTA）** と各国個人情報法（日本: 次世代医療基盤法/個情法、韓国: PIPA）遵守。
- **echo 標準化**: 可能なら **core-lab 中央判定** または標準化 re-read プロトコル（iEOA・gradient 計測の施設間ばらつきが co-primary の最大バイアス源）。
- **登録**: UMIN-CTR / ClinicalTrials.gov 事前登録。報告は **STROBE** 準拠。

---

## 9. 実行計画（マイルストン）

| Phase | 内容 | 主目的 |
|---|---|---|
| **P0: Feasibility census（最優先）** | 4施設で 2015–2024 の小弁輪 AVR 概数・**特に AAE 実例数**・echo 追跡可用性を集計 | サンプルサイズ確定・実現可能性判定 |
| P1: プロトコル確定・SAP | 本草案を共同研究者レビュー→統計解析計画（SAP）固定 | 事前登録 |
| P2: IRB / DTA | 各施設 IRB、日韓 DTA、事前登録 | 法的整備 |
| P3: eCRF 構築・データ収集 | REDCap・echo 収集（core-lab 検討） | データセット構築 |
| P4: 解析 | PSM/IPTW・co-primary・感度解析 | 結果 |
| P5: 論文化 | 原著（target: JTCVS / EJCTS / Circ J / Semin TCVS / JACC: Asia） | 出版 |

---

## 10. 限界・想定バイアスと対策

- **残存交絡**（非無作為）→ PSM＋IPTW、E-value による頑健性評価。
- **時代効果**（Y-incision 2021–）→ 暦年共変量・感度解析。
- **echo 計測の施設間異質性** → core-lab/標準化 re-read。
- **適応バイアス**（誰に AAE/TAVI を選ぶか）→ PS モデルに術前重症度・解剖を厚く投入、適応情報を eCRF 化。
- **AAE 群の N 不足リスク** → P0 census で早期判定、不足時は Arm 2 を「AAE 全法プール」で運用、または前向き拡張へ移行。
- **measured vs projected EOA** → measured を一次、両者一致度を報告（corpus Pibarot 2020 を直接活用）。
- **【最重要】体格交絡** → 先行研究（Makkinejad 2025）では BSA をマッチすると AAE の生存優位が消失した（§1.2.1）。本研究では BSA を必須マッチ変数とし（§7.1）、マッチ後 BSA バランスを独立に報告し、BSA 制限解析・BSA×AAE 交互作用検定を事前規定する（§7.5-6）。**それでも観察研究である以上、体格以外の適応バイアスは残りうる** — E-value で頑健性を定量する。
- **BSA を包含基準にしていないこと自体の限界** → 「小体格集団を対象とした」という主張の根拠が、包含基準ではなく結果として集まったコホートの BSA 分布に依存する（§4.4）。Table 1 で分布を明示し、欧米先行研究と並置して読者が判断できるようにする。

---

## 11. 期待されるインパクト

1. **ガイドライン乖離に Asian 実データで一次エビデンスを提供**。弁輪拡大を指すのは ACC/AHA のみで、ESC/EACTS・JCS は同じ患者を TAVI へ送る（§1.1）。3 文書とも根拠は narrative ないし低エビデンスレベルであり、**比較データでこの空白を埋めるのは我々しかいない**。
2. Asian 小体格における **AAE の真の上乗せ効果と安全域（MR signal 含む）** を世界で初めて多施設比較。
3. **既存の AAE 生存優位が体格交絡と分離できていない問題（§1.2.1）に、直接答える。** 先行研究で最強とされる HR 0.19 は BSA をそろえると P=.067 まで後退する。**「AAE が効くのか、体格の大きい患者が選ばれていたのか」を切り分けられるのは小体格コホートだけであり、それは我々が保有している。** 本研究の独自性の核はここにある。
4. corpus 統合レビューの中心命題（「一律 AAE は正当化されない」）を、当該集団そのもので検証する確証研究。

---

## 12. 共同研究者レビューで決めるべき open items

1. **狭小弁輪の閾値**: 主要層 ≤21mm で確定か、≤23mm 主軸に広げるか。
2. **機械弁の扱い**: 主要解析に含めるか（Asian 若年女性で 17–19mm Regent が一定数）、生体弁限定を主にするか。
3. **sutureless の配置**: Arm 1 内か、独立 arm か。
4. **TAVI 参照群**: self-expanding 限定か BE 含むか。
5. **追跡窓**: co-primary を「退院前 severe PPM」のみにして N を最大化するか、「1年 echo 必須」を堅持するか。
6. **lead center / 著者順 / オーサーシップ規約**。
7. **echo core-lab** を置くか（コスト vs バイアス低減）。
8. **【新規】BSA 制限感度解析の閾値**（§7.5-6a）: **<1.5 / <1.6 / <1.7 m²** のいずれを事前規定するか。臨床的意味（日韓の狭小弁輪症例の実分布）と統計的実行可能性（各群の残存 N）の両面から、**P0 census の BSA 分布を見て確定**する。あわせて、census の結果によっては BSA を包含基準に格上げするか（§4.4）も再検討する。
9. **【新規】aortomitral curtain の計測法**: 本邦で流布する「8mm」の原典は未発表データ・健常成人 40 例・TTE であり（§1.5）、Özçelik 症例の実測は 17–18mm と乖離する。**計測断面・タイミング（収縮期/拡張期）・モダリティ（TTE/TEE/CT）を 4 施設で統一するか**、統一するならその定義。標準化した計測の合意はそれ自体が独立した成果になりうる。

---

## 付録 A: corpus 由来ベンチマーク（設計根拠）

| 指標 | 値 | 出典（corpus） |
|---|---|---|
| Y-incision vs Nicks/Manouguian severe PPM（PSM 103 pair） | 5.5% vs 23.0% (P=0.039) | Makkinejad AnnCardiothoracSurg 2024 |
| Y-incision vs traditional AAE severe PPM（n=202） | 6.9% vs 26% (P=0.005) | Makkinejad AnnThoracSurg 2025 |
| Y-incision postop mean gradient | 6–7 mmHg | Yang JTCVS 2024 / Chen 2025 |
| Nicks ARE vs sutureless severe PPM | 11% vs 6% (n.s.) | Beckmann ICVTS 2016 |
| 日本人 interrupted suturing moderate-severe PPM | 29.4% vs mattress 56.0% (P=.002)<br>**⚠ 同表の severe PPM は 3.9% vs 6.0%、P=.684 で有意差なし。本研究の co-primary は severe PPM であり、「interrupted suturing で severe PPM も減る」とは言えない** | Tabata JTCVS 2014 |
| severe PPM 長期全死亡 HR | 1.84 (1.38–2.45)；**Sá 2024: severe 20yr HR 1.29・心臓死 HR 2.04** | Head EHJ 2012 / [[../md/Sa_PPMimpactAfterSAVRMetaAnalysis_JAHA_2024]] |
| **AAE vs isolated AVR（matched ≤23mm, PSM 112pair）6yr 生存** | **98% vs 74%**（AAE 中期死亡 HR 0.19, 0.06–0.62, P=.006）<br>**⚠ ただし PSM に BSA が含まれず、BSA をマッチすると 98% vs 73%・P=.067 で有意差消失（著者の Supplemental Figure）。効果量として採用する際は §1.2.1 の留保を必ず付すこと** | [[../md/Makkinejad_AAEvsIsolatedAVRMatchedAnnulus_AnnThoracSurg_2025]] |
| **AAE メタ severe PPM（iEOA≤0.65）** | **RR 0.61 (0.40–0.93)** | [[../md/Tanaka_AorticAnnularEnlargementOutcomesMetaAnalysis_AnnCardiothoracSurg_2024]] |
| AAE 後 severe central MR | 初報告（POD50 で MVR）。症例の AM curtain は TTE 実測 **17–18mm** | Özçelik 2026 |
| 日本人 AM continuity | 「約 8mm」— **未発表データ・健常成人 40 例・TTE**（§1.5）。確立した定数として扱わない | Maekawa ArtifOrgans 2002 |
| 予測 iEOA の severe PPM 検出力 | 予測 **1%** vs 実測 **17%**（Ternacle 2021, n=1,088, P<.001）。予測チャート感度 35%（House 2009）、severe PPM 予測感度 13%（Vriesendorp 2020） | [[../md/Abushouk_MeasuredVsPredictedPPM_JACCCardiovascInterv_2023]] Table 1 |

## 付録 B: 関連内部資料

- 統合レビュー: [[../md/_IntegratedReview_SmallAnnulusAVR_2026]]（§10.2 ギャップ、§9 アルゴリズム）
- ハブ: [[../_index]]（§6 Key Numbers, §4 参照マップ）
- 抽出データ: `../tables/outcomes_master.csv` / `ppm_landscape.csv` / `asian_cohort_subset.csv`

---

*草案 v0.1 / 2026-06-11 / SAKURA-AVR / 次段階: feasibility census（P0）と共同研究者レビュー*
