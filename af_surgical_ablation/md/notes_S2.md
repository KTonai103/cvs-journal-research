# 精読ノート S2 — 総論・歴史・現在地

> セッションA / 対象 2編 / 作成 2026-07-23
> 本ノートは統合レビュー執筆（セッションF）で**これだけを読めば足りる**ことを目指す。

## このセクションの結論（3-5行）

1. **Maze の lesion set は「マッピングに導かれない一律の術式」として意図的に設計された。** Cox 本人の一次証言によれば、AF は「2 個以上の大きな macroreentrant circuit が同時に存在する」ため個別マッピングに導かれ得ず、"fallback strategy" として **1 entrance (SAN) / 1 exit (AVN) / 1 true route / several blind alleys** という一律の幾何学が採用された。初回臨床例は **1987 年 9 月 25 日**、lesion set は **両心耳切除（both atrial appendages excised）＋肺静脈隔離＋ cut-and-sew の心房切開線**。この症例は **術後第 5 病日**に（endotracheal suction を誘因として）AF を発症したが、抗不整脈薬なしで **19 年 11 か月 1 週間**洞調律を維持し、20 周年の**ちょうど 3 週間前**に再発、β-blocker に即座に反応した（n=1、統計的効果量は原文に 0 件）。
2. **Cox は初回症例の術後 5 日目 AF を語る文脈で「当時我々は blanking period（少なくとも 90 日）が絶対に必要だと知らなかった」と述懐している。** Cox は 90 日の根拠を **(a) 心房切開線の治癒、(b) 心房電気生理学的特性の正常化**の 2 点に置く（※「この症例が blanking period 概念の起源である」とは原文は述べていない＝読み手の推論）。ただし当時のリズム判定は **Allessie による脈の触診＋心電図（ECG）** のレベルであり、19 年の「洞調律維持」は現代の連続モニタリング基準では検証されていない（＝歴史的成績と現代基準は非互換）。
3. **現在の同時外科的アブレーション（SA）は「やるべきだが、やられていない」。** 術前 AF 有病率は **6.1–61.8%**、SA 実施率は Kowalewski 本文で **22–38%**／同論文 Abstract で **22–48%**（★同一論文内で食い違い＝**要確認**）、STS database（2011–2014）では術前 AF **86 941 例**中 **42 066 例（48.3%）**、STS 2022 update では **年間 >20 000 件**で横ばい。術前 AF は CABG **>360 000 例**の解析で **adjusted 30 日死亡を 50% 増加**、**major morbidity を 32% 増加**させ（95%CI・P 値の記載なし）、CABG 既往 AF 例は **全死亡 40% 高値・心臓死 2.8 倍**（同、CI/P 値なし）。
4. **ハードアウトカムは「観察研究では有意、RCT では非有意」で分裂し、しかも生存曲線は交差する。** STS の PSM **28 739 patient-pairs** で 30 日死亡 **RR 0.92 (95%CI 0.85–0.99)**・脳卒中 **RR 0.84 (95%CI 0.74–0.94)**、Elbadawi（**約 48 000 例**）で院内死亡 **3.6% vs 4.2%, P<0.001**・脳血管イベント **2.0% vs 2.8%, P<0.001**、台湾全国 **11 459 例**で全死亡 **HR 0.75 (95%CI 0.69–0.81, P<0.001)**。しかし台湾データでは **SA 群の 2 年生存はむしろ不良**で中期に曲線が交差してから逆転し、**23 RCTs のメタアナリシスでは生存利益なし — RR 1.07 (95%CI 0.75–1.52, P=0.88)**。
5. **LAAO は SA と組み合わせてこそ意味がある（LAAO 単独は脳卒中を減らさず、拡張障害例では有害でありうる）。** Mehaffey の risk-adjusted 解析で **LAAO 単独 vs AF 無治療の院内脳卒中 OR 0.99 (95%CI 0.93–1.06, P=0.81)＝無効**、**SA+LAAO でようやく OR 0.89 (95%CI 0.83–0.94, P<0.001)**。ただし脳卒中抑制は入院中のみで **30 日以降 OR 1.09 (0.96–1.25, P=0.17)・3 年 OR 1.06 (0.84–1.34, P=0.62)** と消失する一方、**3 年死亡 OR 0.90 (0.88–0.93, P<0.001)** と生存では優る。KROK registry では **SA+LAAO > SA 単独 > LAAO 単独**の生存 gradient（log-rank P<0.001）で、**AVR + LAAO 単独（SA なし）は「AF 無治療」より長期生存が悪化**した。加えてリズム成績の数値（**44–94%**、**57–88%**、1 年 **約70% vs 30%**、hybrid 36 か月 FFA **AAD 許容 72.9±2.9% vs off AAD 59.0±2.5%**＝約 14 ポイント差）は blanking period・>30 秒閾値・AT/AFL の扱い・モニタリング法が全編を通じて未定義であり、**互いに比較不能**である。

---

## 論文別ノート

### [PMID 41176374] Cox JL. 2025. Heart Rhythm 22(11):2735–2736 — 試験名なし（"Iconic Figure" 欄の歴史的回顧エッセイ／単著コメンタリー、原著研究ではない）

> **⚠️ 文書種別に関する重要な注意**
> 本論文は依頼時に「研究論文」として指定されていたが、**原文は Heart Rhythm 誌の "Iconic Figure" 欄に掲載された 2 ページの単著回顧記事**であり、患者コホート・エンドポイント・統計解析を一切含まない。原文全体で本文は約 143 行（見出し・図説・所属・文献リスト含む）、参考文献は **5 件のみ**。したがって「デザイン」「対象」「追跡」「エンドポイント定義」「リズム判定」「主要結果（効果量）」に該当する定量データは **原文に存在しない**。以下、該当なしの項目はその旨を明記する。
> **原文に存在する数値のうち、初回症例の臨床経過に関わるものは次の 5 つ**: ① September 25, 1987、② fifth postoperative day、③ at least 90 days、④ 19 years, 11 months, and 1 week、⑤ exactly 3 weeks（20 周年の 3 週間前）。**ただしこれ以外にも年号・時期・個数の記述は原文に存在する**（By the early 1980s / in 1982 / In 1980 / 3 dimensions / 2 or more large macroreentrant circuits / 2 goals / At 1-month, 2-month, 3-month follow-up / only 3 months earlier / 20th "anniversary" / September 2022 / 35-year celebration / another 35 years / 35 years ago）。**「臨床成績・効果量に該当する定量値」は原文に一切存在しない、というのが正しい記述である。**

- **DOI**: https://doi.org/10.1016/j.hrthm.2025.07.024
- **著者所属**: 1) Feinberg School of Medicine, Northwestern University, Chicago, Illinois; 2) Division of Cardiac Surgery, Department of Surgery, Center for Heart Rhythm Disorders, Northwestern University; 3) Comprehensive Atrial Fibrillation Program, Bluhm Cardiovascular Institute, Northwestern University

- **デザイン**:
  - **該当なし（研究デザインなし）**。単施設/多施設・前向き/後ろ向き・RCT/PSM/IPTW いずれの記載もない。統計手法・使用ソフト・登録番号の記載は **いずれも原文になし**。
  - 学会発表歴: 研究としての発表歴の記載はない。ただし本文中に **"In September 2022, at a 35-year celebration of the first Maze procedure"** という記念行事への言及がある（研究発表ではない）。
  - 資金（原文逐語）: **"This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."**
  - COI（Disclosures、原文逐語）: **"Dr Cox serves on the Board of Directors of Adagio Medical Holdings, Lucid Diagnostics, and PAVmed and serves as a senior consultant for AtriCure."**
    - ※ エネルギー源・デバイスに関する議論を含むレビューで本稿を引用する際は、この COI を併記するのが妥当（＝読み手の判断であり、原文はこれ以上の記述をしていない）。
    - ※ **横断チェック**: 同じ Cox の COI は Kowalewski 2025（本 S2 のもう 1 編）では **"a financial relationship with Adagio Medical, AtriCure, PAVmed, Lucid Diagnostics and PotentiaMetrics"** と記載されており、**PotentiaMetrics は Cox 2025 の disclosure には現れない**。どちらも原文どおりで、記載範囲の違い（開示先の年次差・様式差）と考えられる。**どちらか一方の表記に統一して引用しないこと。**

- **対象**:
  - **N 数の記載なし（コホートなし）**。除外の流れ・背景因子・AF 病型内訳・同時手術の記載も **すべてなし**。
  - 唯一言及される患者は **初回 Maze 症例 1 例のみ**（原文 "The first patient, the cousin of a local cardiologist"）。年齢・性別・基礎疾患・AF 罹病期間の具体値は記載なし。AF 罹病期間については **"an operation for AF that had been present for many years"** とのみ記述（年数の数値なし）。
  - **lesion set（原文の記述、Figure 1 legend より逐語）**:
    > **"Both atrial appendages are excised, and the pulmonary veins are isolated. Appropriately placed atrial incisions not only interrupt the conduction routes of the most common reentrant circuits, but they also direct the sinus impulse from the SAN to the AVN along a specified route."**
    - すなわち **両心耳切除（both atrial appendages excised）＋肺静脈隔離＋外科的心房切開線（atrial incisions）**という、オリジナル Maze（後年 "cut-and-sew" と呼ばれる術式）の記述。※ **"cut-and-sew" という語は原文には一度も出現しない**（原文の表現は "atrial incisions" / "lesions of conduction block"）。引用時に本稿の逐語表現として扱わないこと。
    - なお本稿の Figure 1 は **Reproduced from Figure 9 in Cox et al.（= Cox JL, Schuessler RB, D'Agostino HJ Jr, et al. J Thorac Cardiovasc Surg 1991;101:569–583, p 577）** の再掲であり、**本稿オリジナルの新規図ではない**（＝図の一次資料は 1991 JTCVS）。
    - Figure 1 略語定義: AF = atrial fibrillation; AVN = atrioventricular node; LAA = left atrial appendage; RAA = right atrial appendage; SAN = sinoatrial node。
  - **エネルギー源**: 原文には **エネルギー源（cryo/RF/PFA 等）への言及が一切ない**。記述されるのは外科的切開（"atrial incisions" / "lesions of conduction block"）のみで、**"cut-and-sew" という語自体も原文には出現しない**。PFA・胸腔鏡下・ハイブリッド・concomitant ablation・AFMR に関する記述も **本稿には存在しない**。

- **追跡**:
  - **median (IQR) の記載なし**（コホート追跡が存在しないため）。
  - 記載されている唯一の時間経過は初回症例の個別経過:
    - 手術日 **September 25, 1987**（原文 "the first Maze procedure was performed clinically on September 25, 1987"）
    - **術後第 5 病日に AF 発症** — 原文 "on the fifth postoperative day, he suddenly developed AF while receiving endotracheal suction"。**誘因は endotracheal suction と明記**。
    - **1 か月フォロー**: 洞調律、**digoxin 中止**。
    - **2 か月フォロー**: 洞調律だが **severe lupus syndrome** を発症 → **procainamide 中止**。
    - **3 か月フォロー**: lupus syndrome 消失、**抗不整脈薬なしで洞調律**（原文 "he remained in sinus rhythm on no antiarrhythmic drugs"）。
    - その後 **"remained in sinus rhythm for 19 years, 11 months, and 1 week on no antiarrhythmic drugs"**、Maze 手術の 20 周年の**ちょうど 3 週間前**に AF 再発（原文 "exactly 3 weeks before the 20th 'anniversary' of his Maze procedure, he suddenly developed recurrent AF"）。再発 AF は **β-blockers に即座に反応**（"It responded immediately to β-blockers"）。

- **エンドポイント定義**:
  - **主要／副次エンドポイントの定義は原文に存在しない**（研究ではないため）。
  - **>30 秒閾値の記載なし。AT/AFL を失敗に含めるかの記載なし。AAD の扱いに関する正式な定義なし**（ただし初回症例の記述では "on no antiarrhythmic drugs" と、AAD off での洞調律であることが明示されている）。
  - **blanking period ★ — 本稿で最も引用価値の高い一次記述**: Cox 自身が、blanking period という概念が **初回症例の術後 5 日目 AF という「予期せぬ出来事」から事後的に学ばれたもの**であると述懐している。原文逐語:
    > **"We were unaware at that time that it was absolutely essential to allow at least 90 days (the 'blanking period') for the atrial incisions to heal and for the electrophysiological characteristics of the atria to return to normal before we could accurately determine the success or failure of the surgical procedure."**
    - すなわち本稿は **blanking period = at least 90 days** とし、その生物学的根拠を **(a) 心房切開線の治癒、(b) 心房電気生理学的特性の正常化**の 2 点に置いている。これは本稿が明示する**唯一の「方法論的定義」**である。
    - ※ 90 日以外の数値（例: 30 日、3 か月を超える延長 blanking 等）への言及は **原文になし**。

- **リズム判定 ★**:
  - **モニタリング手段のプロトコル記載なし。実施率の記載なし**（連続モニタ・7 日イベントレコーダ・ILR・24h Holter いずれも本稿には登場しない）。
  - 本稿で記述されているリズム確認手段は、初回症例に対する **触診（脈拍）と心電図**のみ。原文逐語:
    > **"It so happened that the eminent electrophysiologist from the Netherlands, Prof Maurits Allessie, was visiting our institution that day, and I asked him to feel the patient's pulse. He confirmed that it was regular with an appropriate rate and that the electrocardiogram showed a normal sinus rhythm."**
  - → **1987 年当時のリズム判定は「脈の規則性＋（単回の）心電図」レベル**であり、現代の連続モニタリング基準とは比較不能である。※ 原文は "the electrocardiogram" とのみ記し、"resting"（安静時）とは書いていない。この対比は本レビューで「歴史的成績と現代基準の非互換性」を論じる際の一次引用として使える（ただし **原文はその比較自体を主張していない**＝読み手の推論）。

- **主要結果**:
  - **統計的効果量・95%CI・P 値は原文に一切存在しない（0 件）。** 本稿には表も、%表記の成績も、生存曲線も含まれない。以下は原文が述べる**概念的・歴史的主張**である。
  1. **1980 年代初頭の到達点（原文逐語）**: "By the early 1980s, successful surgical procedures had been developed for Wolff-Parkinson-White syndrome, ischemic ventricular tachycardia, idiopathic ventricular tachycardia, arrhythmic right ventricular dysplasia, left and right atrial automatic tachycardias, and atrioventricular nodal reentry."（文献 1）— **AF だけが取り残されていた**。
  2. **AF に対する当時唯一の介入は His 束の外科的離断（原文逐語）**: "The only intervention for atrial fibrillation (AF) before that time was elective surgical interruption of the His bundle, but in 1982, Scheinman and Morady of the University of California, San Francisco, described a catheter fulguration technique for His bundle ablation that replaced the previous open-heart surgical approach."（文献 2 = J Am Med Assoc 1982;248:851–855）
  3. **マッピングの限界（Maze の設計思想の出発点）**: Duke の**アナログ式（analog）術中マッピングシステム**、1980 年の Duke 外科研究室での AF 動物モデル、その後 Washington University in St. Louis での 3 次元コンピュータマッピングを経て得られた知見として —
     > **"Our studies demonstrated that once established, AF is characterized by the simultaneous presence of 2 or more large macroreentrant circuits in one or both atria that sustain AF after it has been induced. We quickly learned that unlike surgery for other arrhythmias, AF surgery could not be guided by mapping."**
     - **結論**: AF 手術は個別マッピングに導かれ得ない → **"we adopted a 'fallback' strategy and developed a uniform surgical procedure"**（＝**患者ごとにテーラーメイドせず、一律の lesion set を全例に適用する**という設計思想の起源）。
  4. **Maze の 2 つの目標（原文逐語）**: **"(1) ablation of all types of AF and (2) preservation of the ability of a sinus-generated impulse to activate both atria and ventricles in a synchronous manner."**
     - ※ (1) の "all types of AF" は、**病型（paroxysmal/persistent/long-standing persistent）を問わない普遍的術式**を最初から志向していたことを示す一次記述。
  5. **"bread-loafing" の否定と lesion 間隔の理論（原文逐語）**:
     > **"Previous experimental studies had shown that AF could be ablated by 'bread-loafing' the atria, but this left the atria incapable of being activated afterward. We deduced that if we placed lesions of conduction block close enough together and if we left the myocardial regions between the lesions connected to one another, then large macroreentrant circuits could not form because of insufficient area; therefore, the atria could not fibrillate."**
     - **critical mass（面積不足で macroreentry が成立しない）という lesion set 設計原理**が明示されている。ただし **「何 mm 以内」といった具体的距離の数値は原文に一切なし**。
  6. **maze（迷路）というアナロジーの中身（lesion set の幾何学的定義、原文逐語）**:
     > **"the lesions were placed so that there was 1 'entrance' into the maze (the sinoatrial node), 1 'exit' from the maze (the atrioventricular node), 1 'true route' between them, and several 'blind alleys' that branched off from this 'true route' so that both atria would be activated—a Maze procedure"**
     - ＝ **1 entrance (SAN) / 1 exit (AVN) / 1 true route / several blind alleys**。この 4 要素が Maze の定義であり、**blind alleys の目的は「両心房を確実に興奮させ、術後の atrial transport function を温存すること」**（Figure 1 legend: "thereby preserving atrial transport function postoperatively"）。
  7. **動物実験→臨床導入（原文逐語）**: "After rather exhaustively testing its safety and efficacy in our animal model, the first Maze procedure was performed clinically on September 25, 1987."（文献 5 = Cox JL. The first Maze procedure. J Thorac Cardiovasc Surg 2011;141:1093–1097）
  8. **初回症例の早期 AF の治療**: **digoxin と procainamide**（原文 "Early postoperative AF was treated with digoxin and procainamide (remember, this was 1987!) and quickly converted back to sinus rhythm."）。procainamide は **severe lupus syndrome** のため 2 か月後に中止、中止後 lupus は消失。
  9. **長期転帰（n=1）**: 抗不整脈薬なしで **19 年 11 か月 1 週間**洞調律維持、その後 AF 再発、β-blockers に即座に反応。
  10. **総括的主張（エビデンスの提示は本稿にはない）**: **"The subsequent safety and effectiveness of the Maze procedure for the treatment of AF is now well established."** — この文には **引用文献番号が付されておらず、裏付けデータも本稿には示されていない**（＝著者の総括的言明）。
  11. **将来展望（著者自身の言葉）**: 2022 年の 35 周年記念で「Maze はあと 35 年続くと思うか」と問われ、**"Of course not!"** と答え、続けて **"But if you had asked me that same question 35 years ago, I would have given you the same answer!"** と述べた。
      - ＝ **術式の陳腐化を予想し続けながら、実際には 35 年生き延びた**という自己言及的アイロニー。カテーテル/PFA 時代における外科的 AF 治療の位置づけを論じる導入・締めの引用として使える。

- **限界**:
  - 【著者記載】: **限界に関する記述は原文に一切ない**（Limitations セクションなし）。
  - 【読み手として】:
    1. **本稿はエビデンス文献ではなく一次史料（回顧記事）である。** 有効性・安全性の数値的裏付けはゼロであり、"now well established" という記述をエビデンスとして引用してはならない。成績を引用する場合は 1991 JTCVS（文献 4）以降の原著を当たる必要がある。
    2. **記述されている転帰は n=1 の逸話**であり、19 年 11 か月 1 週間という数値は集団の耐久性を示すものではない。
    3. **リズム判定が触診＋単回の心電図（原文 "the electrocardiogram"）** であり、無症候性再発の把握は不可能。19 年の「洞調律維持」は現代の連続モニタリング基準では検証されていない。
    4. **現代的論点（concomitant ablation、lesion set の簡略化、LAA 閉鎖の塞栓予防効果、胸腔鏡下・ハイブリッド、PFA、AFMR、洞調律維持の予後的意義）には一切触れていない。** 本レビューにおける本稿の役割は「原理と歴史的出発点の一次引用」に限定すべき。
    5. **参考文献 5 件のうち 2 件（文献 1, 3）は "In press" の書籍章**（Cox JL, McCarthy PM, Malaisrie SC, eds. *Surgery for Atrial Fibrillation and Other Cardiac Arrhythmias*, Elsevier）であり、**本稿執筆時点で検証不能**。当該書籍が引用の裏付けとして機能しない点に注意。
    6. **COI**: 著者は Adagio Medical Holdings・Lucid Diagnostics・PAVmed の取締役、AtriCure のシニアコンサルタント。本稿自体はデバイス推奨を含まないため直接的バイアスは生じにくいが、同著者の他論文を引用する際は考慮が必要。

- **外科への含意**:
  1. **【原著の主張】lesion set は「マッピングに導かれない一律の術式」として設計された。** "AF surgery could not be guided by mapping" → "a uniform surgical procedure"。したがって Cox-Maze の lesion set は、個々の患者の trigger/driver 分布に最適化されたものではなく、**目標として明示的に "ablation of all types of AF"（あらゆる病型の AF の根治）を掲げた一律の術式**として作られている。**【読み手の推論】** これを「意図的に過剰包括的」と評価するのは読み手側の解釈であり、原文にその表現・評価はない。**【読み手の推論】** 現代の「lesion set 簡略化（PVI only 等）」の議論は、この設計思想を意図的に放棄する行為であることを認識すべき。
  2. **【原著の主張】lesion 密度の原理は "insufficient area for macroreentry"。** 個々の線が「どこを通るか」よりも、**分割された領域の面積が macroreentry を維持できない大きさであること**が本質。ただし具体的な距離・面積の閾値は本稿に示されていない。
  3. **【原著の主張】blind alleys は心房輸送能温存のための必須構成要素。** "bread-loafing" は AF を止めるが心房を興奮不能にする。**【読み手の敷衍】** すなわち **lesion を追加するほど良いわけではない**という、lesion set 拡大に対する原理的な歯止めが Maze には最初から組み込まれている。
  4. **【原著の主張】blanking period は "at least 90 days" で、根拠は切開線治癒＋心房電気生理の正常化であり、この期間を置くまでは「手術の成功／失敗を正確に判定できない」。** **【読み手の推論】** 術後 3 か月以内の AF を「失敗」と判定してはならないという臨床運用が、初回症例の**術後 5 日目 AF（endotracheal suction が誘因）**の経験に由来する、という因果関係は原文には明記されていない（原文は「当時は知らなかった」と述べるにとどまる）。なお **原文は AT（心房頻拍）／AFL には一切言及していない**。**現代の外科的アブレーション試験で blanking period を設定する際、その正当化の一次引用として本稿が使える。**
  5. **【原著の主張】両心耳切除（both atrial appendages excised）はオリジナル Maze の構成要素であって、後付けの追加手技ではない**（Figure 1 legend）。**【読み手の推論】** LAA 閉鎖の是非を論じる際、Cox-Maze では **LAA だけでなく RAA も切除**されていた点は、現代の「LAA occlusion only」との違いとして押さえるべき。
  6. **【読み手の推論】歴史的成績と現代基準の非互換性。** 本稿が明示するリズム判定手段（脈の触診＋ECG）を踏まえると、1990 年代の Cox-Maze 成功率と、連続モニタリング＋>30 秒閾値で評価される現代試験の成功率を直接比較することはできない。
  7. **【原著の主張】Maze は「あと 35 年は続かない」と著者自身が考えている。** 2022 年の 35 周年記念での問い（"Do you think the Maze procedure will be around for another 35 years?"）に対する "Of course not!" がその一次記述である。**【読み手の推論】** これを「原理（macroreentry の面積制限＋伝導路の温存）を保ちつつ手段（cut-and-sew → RF/cryo → PFA）を交換していく歴史の容認」と読むのは読み手側の敷衍であり、**原文は RF/cryo/PFA いずれにも一切言及していない**。レビューの序論／結論で PFA・ハイブリッドへの発展を位置づける際の引用として有用。

- **推奨クラス**: **該当なし。** 本稿は歴史的コメンタリーであり、**Class 表記・LOE 表記は原文に一切登場しない**。他ガイドラインからの二次引用も含まれない。

- **抽出上の注意（後段の統合作業者向け）**:
  - 原文テキストは 143 行・約 8.4 KB と短く、**表は 1 つも存在しない** → 表の列ズレ・行ズレのリスクは **なし**。ラベルと値の対応を検証すべき箇所は存在しなかった。
  - pdftotext のハイフネーション由来の分断（例: "electro-physiology", "macro-reentrant", "preser-vation", "inci-sions"）と、**"AF 5 atrial fibrillation" のように「=」が「5」に化けている**（Figure 1 の略語定義行）点に注意。フラグメント／本ノートでは正しい語形に復元して引用しているが、**逐語引用部分の語句自体は改変していない**（ハイフン分断の再結合のみ）。

---

### [PMID 40574669] Kowalewski M, Dąbrowski EJ, Kurasz A, Święczkowski M, Raffa GM, Kawczyński M, et al.（Thoracic Research Centre, endorsed by the European Society of Cardiology Cardiovascular Surgery Working Group）. 2025. Eur J Cardiothorac Surg 67(7):ezaf187 — 試験名なし（narrative "state-of-the-art review"）

> 原題: **"Surgical ablation of atrial fibrillation with concomitant cardiac surgery: a state-of-the-art review"**
> DOI: 10.1093/ejcts/ezaf187 / Advance Access publication 17 June 2025 / Received 29 November 2024; revised 11 April 2025; accepted 9 June 2025
> Open Access (CC BY-NC 4.0)。区分は EJCTS の "REVIEW"（GENERAL ADULT CARDIAC セクション）。

> **⚠️ 本論文は原著研究ではなく narrative review である。** 以下、S6 と同じ見出し構成に沿って書くが、「デザイン／対象／追跡／エンドポイント定義／リズム判定」の項目は
> **本論文自身が一次データを持たないため、原文に記載がない旨を明示する**。数値はすべて本総説が二次引用として提示したもので、
> 引用元の一次論文を確認せずに本ノートの数値を「その試験の結果」として断定してはならない（参照番号を各行に併記した）。

- **デザイン**:
  - 種別: narrative（叙述的）state-of-the-art review。**系統的レビューではない**。原文の自己記述:
    > "The goal of this narrative review is to summarize current evidence to aid physicians in decision making regarding AF management during cardiac surgery."
  - **検索式・データベース・検索期間・スクリーニングフロー・PRISMA 図・PROSPERO 登録番号・エビデンス評価法（GRADE 等）・統計手法・使用ソフトウェア: いずれも原文に記載なし。**
  - メタアナリシスは実施していない（引用しているメタアナリシスはすべて他者の既発表研究）。
  - 学会発表歴: 記載なし。資金: **"FUNDING — None declared."**
  - **エンドースメント**: European Society of Cardiology **Cardiovascular Surgery Working Group** による endorsement 付き。実施母体は Thoracic Research Centre（www.trc.org.pl）。
  - 著者構成が特徴的で、心臓外科側（Suwalski, Kowalewski＝KROK registry、Maesen/La Meir＝Maastricht/Brussels hybrid 系、Wash-U 系データを引用）と電気生理側（de Asmundis, Pannone, Merino, Pürerfellner, Lip）の合同執筆。
  - **COI（原文 Conflict of interest より逐語要約）**:
    - Bart Maesen: Medtronic grants と **AtriCure**・Medtronic からの consultant fee（施設宛）
    - Mark La Meir: "a consultant for AtriCure"
    - Piotr Suwalski: "a consultant for AtriCure"
    - Thorsten Hanke: "speakers' fees and travel expenses from AtriCure Europe"
    - James L. Cox: "a financial relationship with Adagio Medical, AtriCure, PAVmed, Lucid Diagnostics and PotentiaMetrics"
    - Carlo de Asmundis: AtriCure を含む多数からの research grant/teaching fee
    - Radosław Litwinowicz: Medtronic/Getinge/LivaNova consultant
    - Gregory Y.H. Lip: BMS/Pfizer, Boehringer Ingelheim, Daiichi Sankyo, Anthos の consultant/speaker（本人への報酬なし）
    - → **アブレーションデバイス企業（特に AtriCure）との関係が濃い執筆陣による、SA 推進方向の総説**であることは明記して読むべき。

- **対象**:
  - 本総説自体の N 数は存在しない（一次データなし）。
  - 扱う対象母集団は「preoperative AF を有し心臓手術を受ける患者」全般（CABG・AVR・MV surgery・combined）。
  - **術前 AF の有病率（原文逐語）**: "The prevalence of preoperative atrial fibrillation (AF) varies between **6.1% and 61.8%**, depending on the patient profile and the type of procedure [1–3]."
  - AF 病型内訳・同時手術・lesion set・エネルギー源については、**Table 1 に採録された 10 研究のみ数値が示される**（後述「§21 Table 1」）。
  - **エネルギー源（本総説の記述、原文逐語）**: "Several methods were used historically for SA, including microwaves and lasers; however, to date, **only 2 energy sources have been approved: radiofrequency and cryoablation**, both used during the CM IV procedure."
    PFA は "an emerging technology ... still under extensive investigation"。

- **追跡**:
  - **本総説としての追跡期間は該当なし（記載なし）。**
  - Table 1 の各研究の "Mean/median follow-up (years)" は原文に**「mean か median か」の区別なく単一の見出し**で示されており、**IQR・SD の記載は一切なし**（＝「median (IQR)」表記は原文に無い）。
  - 本文中で示される追跡期間の記述は以下（原文どおり）:
    - Pecha ら: **"with a mean follow-up of 5.9 years"**（[47, 49]）
    - Ad ら 2012: **"a mean 35-month observation"**（[41]）
    - mini-Maze vs PVI RCT: **"over a mean follow-up period of 14.4 months"**（[43]）
    - hybrid メタアナリシス: **"79.4% FFA observed at a mean 19-month follow-up"**（[80, S1]）
    - STAR mapping: **"80% FFA at 17 months"**（[S26]）

- **エンドポイント定義**:
  - **本総説は主要／副次エンドポイントを設定していない（narrative review のため該当なし）。**
  - ★**重大な限界**: 本総説は、引用している各研究の
    **blanking period の有無・長さ／AF 再発の「>30 秒」閾値／atrial tachycardia (AT)・atrial flutter (AFL) を失敗に含めるか／AAD 内服下の洞調律を成功とみなすか**
    について、**定義を一切統一・明示していない**。grep 照合の結果、原文中に "blanking" および ">30 s"（30 秒閾値）という語は **1 度も出現しない**。一方 **"off AAD" という語自体は本文に 1 回出現する**が（"in studies allowing AAD and in those with patients off AAD"）、その定義（どの薬剤クラスを、いつからいつまで off とするか）は示されていない。
  - AAD の扱いに触れている数少ない箇所は以下の 2 つのみ:
    - hybrid の実世界データ（原文逐語）: "**72.9% ± 2.9% and 59.0% ± 2.5% at 36 months of FFA in studies allowing AAD and in those with patients off AAD, respectively** [79]"
      → AAD 併用可 vs off AAD で **約 14 ポイント**の差が出ることを本総説自身が示している＝**定義次第で成績が大きく動くことの直接的証拠**。
    - Ad ら（CM III + AVR/CABG）: "94% achieved SR at the 1-year follow-up, **with 81% not requiring class I and III AADs**" [41]
  - Table 1 に "AAD" 列があるが、**列の意味（AAD 内服率なのか、AAD 非使用下の FFA なのか）が研究ごとに異なる**（§21 参照）。原文に列定義の脚注はない。
  - FFA（freedom from arrhythmia）という略語は Abbreviations に定義されているが、**「どの不整脈からの」「どの期間の」自由かは定義されていない**。

- **リズム判定 ★**:
  - **本総説は、モニタリング手段（ECG／24h Holter／7-day event recorder／連続モニタ／ILR）とその実施率について、系統的な記載を一切していない。**
    本文中に "Holter"、"implantable loop recorder"、"continuous monitoring"、"7-day" 等の記述は **本文には存在しない**。
  - 唯一の言及は **Figure 4 の凡例中の略語定義**のみ:
    > "Figure 4: Factors related to sinus rhythm conversion after surgical ablation [S30–S35]. AF: atrial fibrillation; ATA: atrial tachyarrhythmia; CABG: coronary artery bypass grafting; HLoS: hospital length of stay; ICU: intensive care unit; **ILR: implantable loop recorder**; LA: left atrium; MVS: mitral valve surgery; SR: sinus rhythm; y: year."
    → **Figure 4 の本体は画像であり pdftotext でテキスト抽出できない**（図中に ILR に関する具体的記述がある可能性はあるが、確認不能）。
  - 参考: 引用文献 [71] は "Cherniavsky A, Kareva Y, Pak I et al. Assessment of results of surgical treatment for persistent atrial fibrillation during coronary artery bypass grafting **using implantable loop recorders**. Interact CardioVasc Thorac Surg 2014;18:727–31." であり、ILR を用いた研究が引用リストに含まれることのみ確認できる（本文中で ILR の結果は論じられていない）。
  - **結論として、本総説を「リズム判定法のエビデンス源」として使うことはできない。** 統合レビューで「44–94%」「57–88%」「70% vs 30%」等の SR 成功率を引用する場合は、**モニタリング手段が不明であることを必ず付記する**必要がある。

#### 主要結果

##### §1. 術前 AF の疫学的インパクト（本総説の導入）
1. 術前 AF の有病率: **6.1%–61.8%**（患者背景・術式により変動）[1–3]。
2. Malaisrie ら（CABG **>360 000 例**）: 術前 AF は **adjusted 30-day mortality を 50% 増加**、**major morbidity rate を 32% 増加**させた [2]。
   → **95%CI・P 値は原文に記載なし**（"a 50% increase" "a 32% increase" のみ）。
3. 術後 AF（POAF）の予防（原文逐語）: "the odds of postoperative AF occurring may be decreased by **up to 58%** using posterior pericardiotomy [5, 6]."
   → **効果量のみ。95%CI・P 値は記載なし。**
4. 長期予後（原文逐語）: "patients with prior AF undergoing CABG have a **40% higher risk of all-cause mortality** and a **2.8-fold higher risk of cardiac-related mortality**" [9]。**95%CI・P 値の記載なし。**
5. 周術期 AF に関する **35 studies のメタアナリシス** [13]: "an elevated risk of stroke and death, both in the short and the long term" — **数値・CI・P 値いずれも記載なし**。
6. その他の機序として、AF 由来の graft flow 障害が early graft failure のリスク因子であること [8]、silent AF も症候性 AF と同様の合併症と関連すること [4] を挙げる。**数値なし。**

##### §2. CA（カテーテルアブレーション）との比較
7. RCT のメタアナリシス [17]: 外科的治療は CA と比較し **1 年時点でより高い有効性** — **odds ratio (OR) 0.37, 95% CI 0.20–0.69**（P 値の記載なし）。
   ただし **pneumothorax がより高頻度 — OR 0.09; 95% CI 0.01–0.74**（P 値記載なし）。
   ⚠️ **参照方向の注記（一次資料で解決済み）**: 本文は "greater efficacy ... (OR 0.37, 0.20–0.69)" かつ "a higher incidence of pneumothorax (OR 0.09; 0.01–0.74)" と、SA を主語にしたまま両方 OR<1 を並べているが、これは**原著 [17] の OR が一貫して「CA を分子・SA を分母」（CA relative to SA）で報告されている**ことに由来し、**原文内の論理的不整合ではない**。原著 Huang H et al. J Thorac Cardiovasc Surg 2022;163:980–93 は "the summary OR for CA relative to SA was 0.37 (95% CI, 0.20-0.69)"、"CA was associated with a greater incidence of femoral vascular complications (OR, 5.81) but a lower incidence of pneumothorax (OR, 0.09; 95% CI, 0.01-0.74) than SA" と明記している。すなわち **OR 0.37 ＝ CA の 1 年成功オッズが SA の 0.37 倍（SA 優位）**、**OR 0.09 ＝ CA の気胸オッズが SA の 0.09 倍（＝SA で気胸が多い）**。本総説は参照群（CA）を明示していないだけなので、引用時は「CA vs SA の OR」と参照群を補って記載すること。
8. persistent AF に限定した別メタアナリシス [18]: SA の方が有効性が高いが手技合併症は増加。**数値なし。**

##### §3. SA の実施率（underutilization）
9. 原文逐語: "Approximately **22–38%** of preoperative AF cases are treated with ablation [1–3]."
   ⚠️ **Abstract では "performance rates varying between 22% and 48%"** と書かれており、**本文（22–38%）と Abstract（22–48%）が食い違う＝★要確認**。48% は下記 STS の 48.3% を指すと思われるが、原文はそう明記していない。**両方をそのまま併記して扱うこと。**
10. **STS database**（全米 50 州＋カナダ 5 施設＋その他 6 国際施設、**2011–2014 年**）: 術前 AF **86 941 例**中 **42 066 例（48.3%）**が SA を受けた [19]。（分数そのまま。原文に % と分数の両方あり）
11. **STS 2022 update** [20]: isolated AVR と CABG 併用手術は減少、低侵襲・経カテーテル弁膜症治療は増加。しかし
    "the volume of AF SA procedures has remained relatively stable, with **over 20 000 procedures performed annually**."

##### §4. underutilization の理由（本総説の解釈）
12. かつては有効性のエビデンス不足が理由だったが、現在の障壁は **技術的問題と周術期リスク懸念** [4]。
13. Brancato ら [21]: 主要な障壁は術者の経験に関するもので、"SA is often marginalized in cardiothoracic training programs"。
    興味深いことに **より最近に卒業した外科医の方が SA 実施経験が多かった**。**数値・CI・P 値の記載なし。**
14. AF 患者は周術期リスクが高いという認識 [22]。KROK cohort の EuroSCORE II validation study [23] でも実際に高リスク。**数値なし。**
15. SA 追加は CPB 時間・大動脈遮断時間を延長する [24, 25]。ただし低侵襲手技（CABG では CPB 回避も可能）や、**LA を開けずに PVI + box lesion を行う手技**でリスク軽減しうる [26]。

##### §5. ガイドライン／コンセンサスの記載（**すべて二次引用**）
> ⚠️ **本総説はガイドライン文書ではない。以下の Class/LOE はすべて他文書からの二次引用であり、本論文自身は推奨クラスを提示していない。**

16. **STS Clinical Practice Guidelines [29]（＝STS 2017）**（原文逐語）:
    > "Recommendations include a **class I, level A** designation for SA during **MV procedures**, a **class I, level B** designation for **CABG, AVR or combined procedures** and a **class IIa, level B** recommendation for **stand-alone SA** in cases of symptomatic AF refractory to AADs or catheter-based therapies."
    本総説の評価（原文逐語）: "The most liberal characteristic of the STS guidelines may be related to the primarily surgical character, unlike the joint consensuses and statements of other major cardiac societies, led primarily by cardiologists."
17. **2024 EHRA/HRS/APHRS/LAHRS expert consensus statement on catheter and surgical ablation [30]**（原文逐語）:
    > "advises that **SA should be performed in all patients with AF undergoing LA open surgery, regardless of previous antiarrhythmic treatment** [30]. In patients undergoing **LA closed surgery who are intolerant or refractory to AADs, SA should be performed**, whereas in those with **no prior pharmacologic treatment, initial SA may be appropriate**. Importantly, the beneficial impact of left atrial appendage occlusion (LAAO) was underlined and is **now indicated in all patients undergoing SA, regardless of the type of operation performed** [30]."
    → **Class/LOE 表記は本総説には転記されていない**（推奨文の趣旨のみ）。
18. **2024 ESC/EACTS AF Guidelines [31]**（原文逐語）:
    > "the 2024 European Society of Cardiology/European Association for Cardio-Thoracic Surgery guidelines **upgraded to class I recommendations for concomitant SA in patients undergoing MV operations** and included a **new class IIa recommendation for concomitant ablation in patients undergoing non-mitral surgery** [31]."
    → **LOE の記載は本総説にはなし。**
19. 抗凝固に関する本総説の立場（原文逐語）:
    > "As current evidence suggests, **SA—even when combined with LAAO—does not provide sufficient grounds for discontinuing anticoagulation in surgical patients** [31]."
20. 周術期 OAC 管理は **2024 EACTS Guidelines on perioperative medication in adult cardiac surgery [40]** に依拠（原文逐語）:
    "OAC should be discontinued before the operation based on the specific drug used and **restarted early after the operation—regardless of the outcome of SA**—provided that the risk of postoperative bleeding is low [30]."
    → **同時 SA の周術期管理に特化した推奨は存在しない**と明記: "There are currently **no specific recommendations** regarding the perioperative management of patients undergoing concomitant SA."
21. **Figure 1**: "Summary or recommendations for ablation during cardiac surgery [30, 31, S28, S29]"（ESC/EACTS、EHRA/HRS/APHRS/SOLAECE、ECAS 等の推奨を横並び比較した図）。
    ⚠️ **図本体はラスタ画像であり pdftotext ではテキスト抽出不能。図中の Class/LOE の一覧は本ノートでは再現できない**（凡例のみ抽出可）。

##### §6. Cox-maze の発展と lesion set（術式論）
22. **CM の進化（原文の記述をそのまま）**:
    - 原法 CM（＝CM I）の 2 大問題: **"inability to produce appropriate sinus tachycardia"** と **"postoperative LA dysfunction"**。
    - **CM II**: 横切開（transverse atriotomy）を LA dome を越えて後方へ移動 → しかし LA 露出のため **上大静脈を完全離断**する必要が生じた。
    - **CM III** [35]: 中隔切開を SVC 開口部の後方に置くことで SVC 離断を回避。ただし原文逐語 "Due to its complexity, the CM III operation **did not become widely adopted**."
    - **CM IV** [36]: CM III の cut-and-sew パターンを **bipolar radiofrequency ablation and/or cryoablation** による ablative line に置換。現在の主流。
    - **Figure 3: "Evolution of the Cox-maze procedure."**（図本体は画像、テキスト抽出不能）
23. **PAF vs non-PAF の治療目標（原文逐語、術式選択の根拠）**:
    > "In the case of paroxysmal forms of AF (PAF), the primary aim of ablation is to **isolate the source of the triggers**. For effective and lasting therapy of **non-PAF, it is necessary to target the substrate** responsible for arrhythmia maintenance. This goal is attempted during the operation by performing ablation lines, according to the CM IV procedure, which **includes isolation of the posterior wall of the LA with additional lines in both atria** with the aim of interrupting and preventing the formation and circulation of **macro-re-entrant drivers** perpetuating AF."
24. 歴史: atrial transection、corridor operation、LA isolation は 1980 年代初頭に開発。Cox は commentary [32] で **bi-atrial lesion の重要性**を強調。
25. **Figure 2**: "Decision-making flowchart for choice of atrial fibrillation ablation technique. **Reproduced from McCarthy and Cox [33]**."
    凡例に列挙される要素（＝フローチャートの構成要素）: AF, AVR, **BA: bi-atrial**, CAB, LA, **LAA**, **LAAO**, **LSP: long-standing persistent**, NOAC, **PAF**, preop, **PVI**, **RH: right heart**。
    ⚠️ **図本体は画像でテキスト抽出不能。分岐条件（LA 径・AF 持続期間の閾値など）は本ノートでは復元できない。** 原著 [33] McCarthy PM, Cox JL. J Thorac Cardiovasc Surg 2025;169:907–15 を別途参照すべき。
26. **PVI 単独に対する本総説の立場**（原文逐語）:
    > "Even though **CM IV remains the gold standard** of surgical therapy, many surgeons forego this procedure mostly due to its level of complexity, its invasiveness and the amount of time it consumes. ... Although this approach might be reasonable in patients with PAF, given the anatomical background of non-PAF, it appears to be **less than optimal** in this group of patients."
    > "However, performing **PVI with box lesions instead of a full CM procedure is still highly beneficial compared to refraining from treating arrhythmia at all** [19]."
    → **「フル CM ができないなら PVI+box でもやらないよりは遥かに良い」**が本総説の実務的メッセージ。

##### §7. 手術時間の延長という懸念
27. 原文逐語: "Most studies investigating outcomes related to SA have found that, whereas **CPB and cross-clamp times may be significantly extended, there are no differences in complication rates** attributable to this issue [24, 25, 41]."
28. MV 手術併施 SA の RCT メタアナリシス [42]: CPB・遮断時間は延長するが **30 日死亡に差なし**。**数値・CI・P 値の記載なし。**
29. 本総説の結論: "concerns regarding operative time **should not deter** patients with AF from undergoing the ablation procedure."

##### §8. 洞調律（SR）回復・維持の成績
30. SA の有効性は **44% から 94%** の範囲 [44]。lesion set・エネルギー種・AF 病型により **57% から 88%** [45]。
    → **いずれも範囲のみ。CI・P 値なし。定義（AAD の扱い・モニタリング法）不明。**
31. Stand-alone ablation: 1 年・5 年・10 年で高い freedom from atrial tachyarrhythmias、AF 病型・術式によらず一貫 [46]。**数値なし。**
32. **RCT のメタアナリシス [48]**: 1 年時点で **約 70%** が AF free、対照群は **30%**。
    → 原文は "approximately 70% ... compared to 30%"。**CI・P 値の記載なし。**
33. 全心臓手術集団での SR 変換率 [47]: **3 か月 49.8%、6 か月 57.6%、12 か月 59.9%**。
34. **良好なリズム転帰と関連する因子**（原文逐語）:
    > "Identified factors associated with better rhythm outcomes included **left atrial diameter <6 cm**, **PAF rather than non-PAF**, **shorter duration of AF** and **immediate postoperative conversion to SR**."
    加えて本総説の提言（原文逐語）: "Evaluation of the LA diameter should be standardized, and the **left atrial volume index or left atrial reservoir strain** should be considered as **superior** for such evaluation, as supported by the most recent studies and summarized in guidelines [31]."
35. Pecha ら（**mean follow-up 5.9 years**）[47, 49]: SR 維持 **56.6%**、**PAF 67.3% vs persistent AF 54.8%**（"significantly better" と記載されるが **P 値・CI の記載なし**）。
36. Van Breugel ら [50]: SR 変換率 — **paroxysmal 69.8%、persistent 44.4%、permanent 28.2%**。**CI・P 値なし。**
37. MV 置換時の SA は CABG/AVR 併施より成功率が低い可能性（構造的変化と心房拡大のため）[27, 51, 52]。**数値なし。**
38. **CM III + AVR or CABG**（全 AF 病型）[41]: **1 年で 94% が SR**、**81% が class I/III AAD 不要**。
39. **persistent AF + MV surgery の RCT メタアナリシス [42]**: SR 率 — **退院時 65.1%、6 か月 63.5%、12 か月 67%**。
40. **MV 手術 8430 例のメタアナリシス [53]**: 5 年間の aggregate **freedom from arrhythmia (FFA)** — **90.2%、83.5%、79.5%、76.4%、73.2%**
    （1〜5 年に対応すると読めるが、**原文は "over 5 years of follow-up as ... respectively" とのみ記載し、各値がどの年に対応するかを明示していない**。行対応は推定であり断定不可）。
41. **年齢**: MacGregor [54] — **75 歳超**の CM IV では不整脈再発リスクが有意に上昇。**HR・CI・P 値の記載なし。**
42. **術者経験**: Ad ら [55] — 原文逐語 "surgeon experience (**at least 50 ablation cases**) predicted SR with **6% greater odds for every 10 SA cases** performed"。**CI・P 値の記載なし。**
43. **右房（RA）lesion の意義**（本総説が強調する論点。原文逐語）:
    > "Although studies are limited and meta-analyses are unavailable, emerging data underscore the need to address **right atrium (RA) pathology** to improve outcomes in SA. Data suggest that **RA lesions may be especially important in preventing macro-re-entrant arrhythmias**. This point may be relevant, especially in patients undergoing MV surgery, because studies have reported **increased rates of atrial tachycardia** in those patients [56]."
44. **Figure 4**: "Factors related to sinus rhythm conversion after surgical ablation [S30–S35]"（図本体は画像、テキスト抽出不能）。

##### §9. rate control vs rhythm control（洞調律維持の意義）
45. 最近のメタアナリシス [57]: rhythm control は rate control に対し **cerebrovascular death, stroke, hospitalization due to heart failure** で優越。
    著者らの強調点（原文逐語）: "studies with **increased numbers of ablation in the rhythm control arm** mostly influenced improved outcomes"。**数値・CI・P 値の記載なし。**
46. 効果は **早期 rhythm control** 導入例でより顕著 [58]。**数値なし。**
47. long-standing persistent AF に対する rhythm control では、rate control 比で **左室駆出率の改善**が観察された [59]。**数値なし。**
48. 本総説による SA の生存改善メカニズム仮説（原文逐語）: "the **cessation of AF-related detrimental cardiac remodelling leading to heart failure** and **potentially reduced risk of thromboembolic events**."

##### §10. 短期アウトカム
49. **STS database [19]**（全 AF 病型、**propensity score matching で 28 739 patient-pairs**）:
    - 30 日死亡: **8% 低下 — RR 0.92, 95% CI 0.85–0.99**（P 値の記載なし）
    - 脳卒中: **16% 低下 — RR 0.84, 95% CI 0.74–0.94**（P 値の記載なし）
50. **Elbadawi ら [68]**（全 AF 病型、**nearly 48 000 patients**）:
    - 院内死亡: **3.6% vs 4.2%, P < 0.001**（SA 群 vs 非 SA 群。**原文は % のみで分数なし。95%CI の記載なし**）
    - 脳血管イベント: **2.0% vs 2.8%, P < 0.001**（同上）
51. 一方で（原文逐語）"AF ablation procedures may also **increase the risk of adverse outcomes, particularly conduction disturbances** [27]."

##### §11. 恒久ペースメーカ（PPM）
52. PPM 植込みリスクは術式により変動 [60, 61]。**最大の関連因子は bi-atrial lesion set** [62–64]。
    解剖学的に **RA でのアブレーションは刺激伝導系損傷を来しやすい**。経験蓄積とともに PPM 率は漸減。
53. **RCT における PPM の最多理由は heart block であり sinoatrial node dysfunction ではない** [27] → 本総説はこれを **RA lesion の重要性**の傍証としている（原文逐語）:
    > "in RCTs regarding SA, the most common reason for a PPM implant was **heart block, not sinoatrial node dysfunction itself**, which underscores the importance of RA lesions [27]."
54. AF そのものが sick-sinus syndrome・房室ブロックのリスクを高める [65]。
    さらに **AAD 使用は PPM リスクを 5 倍に増加**（韓国の **770 977 例**の解析）[66]。**CI・P 値の記載なし。**
55. AF 病型と PPM 率の関係は限定的なデータ。Pecha ら・Kowalewski ら は **AF 病型を PPM の予測因子として報告していない** [4, 19, 63, 67]。
56. **KROK・HEIST registry、PRAGUE-12 その他**: SA 群と対照群で **PPM 率に有意差なし** [24, 67, 70, 71]。**数値・CI・P 値の記載なし。**

##### §12. 長期アウトカム（生存）
57. **台湾の全国 population-based スタディ（11 459 例）[72]**:
    - 全死亡: **HR 0.75, 95% CI 0.69–0.81, P < 0.001**（＝25% 低下）
    - サブグループ（背景因子・術式・Charlson Comorbidity Index・CHADS2-VA2Sc score）を問わず一貫（**原文表記は "CHADS2-VA2Sc"**。CHA₂DS₂-VASc の誤植と思われるが原文どおり記載）。
    - ★**重要な時間依存性（原文逐語）**: "patients undergoing SA exhibited **worse 2-year survival**; however, a better prognosis was observed in the long-term follow-up after a **midterm crossover of survival curves**."
      → **早期は SA 群が不利、中期でクロスし長期で逆転**。同時 SA の意思決定における最重要ニュアンス。**クロス時点の具体値は記載なし。**
58. **Musharbash ら**（本文中の綴りは **"Masherbash"**、Table 1 では "Musharbash F. [S37]"）: CM IV は無アブレーションと比べ **10 年生存を有意に改善 — adjusted HR 0.47, 95% CI 0.26–0.86, P = 0.014**。
    さらに **SA 群と no-AF controls の間に差なし（P = 0.85）** → 原文 "suggesting that ablation may effectively reduce the burden of arrhythmia"。
    ⚠️ 本文には HR 0.47 の出典番号が付いていない（直後の文で [73] が別研究を指す）。Table 1 の [S37] に対応すると読める。
59. **多施設研究（20 407 例）[73]**: SA 追加により **5 年生存が改善**。**効果量・CI・P 値の記載なし。**
60. KROK registry の複数のポーランド解析が死亡率低下を示す [24, 25, 74]。**数値なし。**
61. **否定的エビデンス**:
    - **23 RCTs のメタアナリシス [48]**: 生存利益なし — **RR 1.07, 95% CI 0.75–1.52, P = 0.88**。
    - Ad ら [41]（**mean 35-month** 観察、CABG or AVR ± SA）: 死亡率に差なし — **log-rank = 0.49, P = 0.48**
      （原文表記は "logrank ¼ 0.49, P ¼ 0.48"＝log-rank 統計量 0.49。**"¼" は pdftotext による "=" の文字化け**）。
62. 本総説による不一致の説明: RCT の観察期間が短くイベント数が少なく検出力不足であること、レジストリには選択バイアスがあること。
63. **選択バイアスへの反論**: HEIST registry の解析 [75] では **より高リスクの患者ほど SA を受けており**、**EuroSCORE II サブグループ間で長期生存利益の大きさは同程度**であった。ただし本総説自身も原文で "Certainly though, the improvement in prognosis might also reflect patient selection." と留保している。

##### §13. Hybrid／thoracoscopic アブレーション
64. **本総説の hybrid の定義・位置づけ（原文逐語）**: "Hybrid ablation **combines SA with CA** to shorten operative times while ensuring effective lesion sets. Although it is minimally invasive, it provides reduced operating time and allows for **staged procedures**. It also requires **close collaboration between cardiac surgeons and electrophysiologists**."
65. thoracoscopic 単独: 外傷少・入院短・回復早いが "technically demanding, and outcomes may be **highly dependent on surgical centre experience**."
66. staged/hybrid の位置づけは依然議論的 [76, 77]。
67. **メタアナリシス [78]（＝Aerts L, Europace 2024 の IPD メタアナリシス）**: **hybrid thoracoscopic は isolated thoracoscopic より FFA で優れる可能性、合併症に差なし**。**数値・CI・P 値の記載なし。**
68. thoracoscopic 単独が劣る理由（本総説の解釈、原文逐語）:
    > "Inferior outcomes with the thoracoscopic approach may be associated with its **limitations for achieving bi-atrial lesions** and using only **unipolar ablation devices** in some studies, which commonly creates **epicardial but non-transmural lesions**."
69. **実世界データ [79]**: 36 か月 FFA — **AAD 許容の研究で 72.9% ± 2.9%**、**off AAD の研究で 59.0% ± 2.5%**。（± が SE か SD か原文に記載なし。95%CI なし）
70. **メタアナリシス [80, S1]**: hybrid の FFA **79.4%（mean 19-month follow-up）**。
    persistent／long-standing AF で CA より **20% 以上高い FFA — 70.7% vs 49.9%, P < 0.001**（**95%CI の記載なし**）。
71. **hybrid vs CA の RCT は 2 件**: **HARTCAP-AF** と **CEASE-AF** [79, S2, S3]（原文逐語）:
    > "Both showed the **superiority of the hybrid approach over CA** in patients with **persistent or long-standing persistent AF**, with **no significant differences in terms of safety**."
    → **効果量・CI・P 値はいずれも本総説に記載なし。**
72. Future directions（原文逐語）: "**Hybrid ablation procedures concomitant with general cardiac surgery** are gaining more attention, especially in patients with **persistent or long-standing AF and high perioperative risk**. Although both hybrid and staged procedures provide good results, **their superiority over conventional AF surgery is still uncertain**."

##### §14. PVI と他手技の比較（lesion set 比較）
73. **PVI の位置づけ（原文逐語）**: "PVI is the **most frequently used surgical technique** for AF-related ablation, primarily due to its **simplicity and low complication rates** [S4]."
74. **ドイツの CABG/AVR 研究 [S5]**: **complete left-sided lesion set と PVI で 12 か月の freedom from AF に差なし**。**数値・CI・P 値の記載なし。**
75. **Hald ら [S6]**（後ろ向き、全心臓手術、PVI vs bi-atrial ablation）:
    - persistent AF での **freedom from AF: 45% vs 63%, P = 0.039**（bi-atrial が優れる。**95%CI なし**）
    - **PPM 植込み率: 6% vs 9%, P = 0.039**（bi-atrial で高い。**95%CI なし**）
    ⚠️ 原文の記述順は "PVI versus bi-atrial ablation ... **the latter approach** demonstrated greater effectiveness ... (freedom from AF: 45% vs 63%)" であり、**45%=PVI、63%=bi-atrial** と読むのが整合的。PPM も **6%=PVI、9%=bi-atrial** と読める。**ただし原文は各数値に群ラベルを付けていない**ので、断定するなら一次資料確認が必要。
76. **network meta-analysis（bi-atrial / left atrial / PVI、計 7207 例）[S7]**:
    - **PVI が SR 回復で最も有効性が低い**。
    - 著者らの結論（原文逐語）: "**left atrial ablation may be considered the most preferable technique**" — 理由は bi-atrial と比べ **同等の有効性・有意に低い PPM 必要率・低い再手術率・短い CPB 時間**。**数値・CI・P 値の記載なし。**
    → ★ **§43/§53 で本総説は「RA lesion が重要」と述べる一方、ここでは「LA ablation が最も好ましい」という NMA を紹介しており、総説内で立場が両論併記になっている。統合レビューではこの緊張関係を明示すべき。**
77. **Sef ら（systematic review & meta-analysis）[S4]**: MV 手術における **CM IV は PVI より中期 FFA が良好**、生存利益も示唆。**数値・CI・P 値の記載なし。**
78. **CABG での CM vs PVI（原文逐語）**: "**Only 1 small RCT (total of 95 patients)** compared outcomes between **'mini-Maze' procedures and PVI** in the context of coronary revascularization, whereby over a **mean follow-up period of 14.4 months**, comparable rates of FFA were observed (**80% vs 86% in PVI vs 'mini-Maze'**, respectively) [43]." **P 値・CI の記載なし。**
79. **AVR および/または CABG のサブセット [S8]**: CM は死亡率・複合エンドポイントの両方で有意に優越 —
    - 死亡: **adjusted HR 0.38, 95% CI 0.21–0.66, P = 0.001**
    - 複合エンドポイント: **adjusted HR 0.52, 95% CI 0.35–0.76, P = 0.001**
    （**複合エンドポイントの構成要素は原文に記載なし**）

##### §15. CM IV と他手技の比較
80. 原文逐語: "The **CM IV stands out as the sole operative technique approved by the U.S. Food and Drug Administration** for AF corrective operations and **remains the current gold standard** [S9]."
81. 原文逐語: "Due to the necessity of **opening both atria**, surgeons often hesitate to perform bi-atrial lesions, **particularly in CABG and AVR procedures**, opting instead for either **PVI or LA ablation**."
82. メタアナリシス群 [48, S10]: CM 手技の優越性を一貫して示すが、**他手技より PPM 植込みが多い**。**数値なし。**
83. 低侵襲手技の systematic review [26]: **CPB を用いた CM が最も有効**で、**SR 回復率 87%**（epicardial・hybrid SA との比較）。**CI・P 値なし。**
84. **Tampa 2 Maze procedure** [S11]（新規術式、原文逐語）:
    > "The recently described **Tampa 2 Maze procedure** uses **new isolation clamp and cryoablation lines** to perform a **novel left heart lesion set**. In a pilot study, surgeons **validated lesion transmurality with mapping** and concluded that their approach is **simpler than CM IV ablation and can create a comparable lesion set**."
    → **症例数・成績・追跡期間の記載なし。**

##### §16. その他の転帰（再入院・心不全・脳卒中）
85. **再入院** [S12]: 90 日・180 日では全体として差なし。ただし cause-specific 解析では **長期に AF と PPM 植込みによる再入院が SA 群で多い**。**数値なし。**
86. **心不全合併例の SA**: 症例集積と小規模非ランダム化研究が中心 [S9]。良好な転帰（**左室駆出率の正常化**と低合併症率）[S13, S14]。**数値なし。**
    CASTLE-AF・CASTLE-HTx は **CA** で複合一次エンドポイントと死亡を含む二次エンドポイントを有意に減少 [S15, S16]。
    原文逐語: "As for **SA**, the potential benefits in this heart failure subpopulation are **yet to be elucidated**."
87. **脳卒中**:
    - **PRAGUE-12 の 5 年フォロー [70]**: 不整脈治療を受けた群で脳卒中発生が有意に低い — **sub-hazard ratio 0.32, 95% CI 0.12–0.84, P = 0.02**
    - **Cheng ら（観察研究）[72]**: 長期の脳卒中リスク低下 — **sub-distribution hazard ratio 0.78, 95% CI 0.67–0.91**（**P 値の記載なし**）
    - しかし複数の大規模メタアナリシス [42, 48, 53] は有意差を示さず。理由として **観察期間が短いこと**と **大半で OAC が継続されていること**を挙げる。
    - **OPTION trial**（CA 後 90 日での OAC 中止と LAA 閉鎖）に言及。原文 "Data as of SA remain limited."

##### §17. LAAO（左心耳閉鎖）との併用 ★本総説の中心的主張のひとつ
88. **LAAOS III [S17]**: 心臓手術への LAAO 組込みで **stroke or systemic embolism が減少 — HR 0.67, 95% CI 0.53–0.85, P = 0.001**。
89. **Mehaffey ら [S18]**（本総説が **"the most compelling evidence to date"** と評価。LAAO 単独 / SA+LAAO / AF 治療なし の比較、risk-adjusted 解析）:

    | 比較 | アウトカム | 効果量 | 95% CI | P値 |
    |---|---|---|---|---|
    | SA + LAAO vs no AF treatment | in-hospital stroke | **OR 0.89** | 0.83–0.94 | **P < 0.001** |
    | LAAO alone vs no AF treatment | in-hospital stroke | **OR 0.99** | 0.93–1.06 | **P = 0.81** |
    | SA + LAAO vs LAAO alone | stroke（index hospitalization） | **OR 0.88** | 0.83–0.94 | **P < 0.001** |
    | SA + LAAO vs LAAO alone | stroke（after 30 days） | **OR 1.09** | 0.96–1.25 | **P = 0.17** |
    | SA + LAAO vs LAAO alone | stroke（after 3 years） | **OR 1.06** | 0.84–1.34 | **P = 0.62** |
    | LAAO alone vs no AF treatment | long-term prognosis | **OR 0.75** | 0.73–0.77 | **P < 0.001** |
    | SA + LAAO vs no AF treatment | long-term prognosis | **OR 0.68** | 0.66–0.70 | **P < 0.001** |
    | SA + LAAO vs LAAO alone | 3-year mortality | **OR 0.90** | 0.88–0.93 | **P < 0.001** |
    | SA + LAAO vs LAAO alone | composite end points | **OR 0.90** | 0.81–0.99 | **P = 0.035** |

    （上表はすべて原文本文からの逐語転記。**"long-term prognosis" と "composite end points" の具体的定義は原文に記載なし。**
    表は pdftotext の表ではなく本文散文からの抽出であるため行ズレの懸念はない。）
    → ★**解釈上の要点**: 脳卒中抑制効果は **入院中（index hospitalization）のみ有意**で、**30 日以降・3 年時点では消失**している（OR>1 に反転すらしている）。
      一方で **3 年死亡と複合エンドポイントでは SA+LAAO が LAAO 単独に優る**。**「LAAO 単独では脳卒中は減らない（OR 0.99）」**が本総説の強調点。
90. **KROK registry [S19]**: 生存利益に **gradient** — 原文逐語 "the greatest reduction in mortality was associated with **SA combined with LAAO**, followed by **SA alone** and **LAAO alone** (**log-rank P < 0.001**)"。**HR・CI の記載なし。**
91. ★**LAAO 単独の害の可能性（左室拡張障害例）** — 本総説の重要な警告（原文逐語）:
    > "specific considerations must be made for patients with **left ventricular diastolic dysfunction**. In these patients, **the left atrial appendage may serve as the primary capacitance chamber in the left heart, thereby maintaining cardiac output**, and its exclusion alone (e.g. without SA) **may exacerbate symptoms of heart failure due to reduced atrial compliance**. In the aforementioned KROK registry analysis, **addition of LAAO alone in patients undergoing AVR resulted in reduced long-term survival compared to the no-AF treatment** [S19]."
    → **AVR + LAAO 単独（SA なし）は長期生存が悪化しうる**という registry 所見。**効果量・CI・P 値の記載なし。**
    対策として原文は "preoperative haemodynamic assessments and multidisciplinary decision making" を推奨。

##### §18. 神経節叢（Ganglionated plexi, GP）アブレーション
92. GP は一部の患者で不整脈源かつ AF 維持基質と疑われる [S20]。
93. **メタアナリシス [S21]**: **PAF に対する PVI に GP 隔離を追加すると SR 維持が改善**。**数値・CI・P 値の記載なし。**
94. しかし **long-standing persistent AF では 2 年観察で SR 維持は 38.2% のみ**。
95. 本総説の結論: GP 隔離は **PAF では有用な追加**、それ以外では限定的。ただし原文逐語 "unless complemented by **wider cardio-neuroablation strategies** that showed promising effectiveness in a recent pilot study [S22]."

##### §19. PFA（pulsed field ablation）— ★外科領域での現状
96. カテーテル AF アブレーションにおける PFA は有望な結果 [S23, S24]。
97. ★**外科的アプローチについての本総説の結論（原文逐語）**:
    > "When considering the surgical approach, **currently available evidence considers the application of PFA in swine alone** [S25]. **All of the performed lesions were transmural**, confirming the superior efficacy of the technique in the **epicardial approach**. The **future applicability of PFA in humans undergoing cardiac surgery remains to be elucidated**."
    → **本総説（2025 年 6 月時点）は、外科的 PFA のヒトエビデンスはゼロ、ブタ試験のみ、と評価している。**
      これは 2024–2026 に出た外科 PFA のヒト研究を**採り上げていない**ことを意味する。**本総説の PFA 記述は既に陳腐化しているとみなすべき。**

##### §20. マッピングと今後の方向性
98. 原文逐語: "Future research should prioritize the **standardization of lesion sets, energy sources and surgeon training** to improve reproducibility and maximize patient outcomes."
99. 電気生理マッピングへの関心の高まり。カテーテル研究では **persistent AF でマッピングガイド下アブレーションの高い有効性**。
100. **STAR（stochastic trajectory analysis of ranked signals）-guided CA** [S26]: **80% FFA at 17 months**。**CI・P 値なし。**
101. **TAILOR-AF（NCT05169320）** [S27]: instantaneous amplitude and frequency modulation mapping → CA → 必要に応じ **胸腔鏡による低侵襲外科的アプローチ**、という順序を検証する試験。
102. **LeAAPS trial** [S28]: **AF 既往のない高リスク患者**に対する **prophylactic LAAO** の心臓手術時の効果を検証中。

##### §21. Table 1 の完全転記（pdftotext -layout で列構造を確認済み）
> ⚠️ **検証記録**: 素の pdftotext 出力ではこの表は列がすべて分断されており、値とラベルの対応が復元不能だった。
> **`pdftotext -layout -f 10 -l 10` で再抽出し、10 行 × 11 列すべてが 1 対 1 で対応していることを目視確認済み**（行ズレなし）。
> 以下は -layout 出力からの逐語転記。単位（%）が原文で省略されているセルはそのまま記載した。

**Table 1: Summary of selected studies reporting long-term outcomes of surgical ablation**

| Study | Number of patients | Type of primary surgery | AF type | Concomitant SA | Mean/median follow-up (years) | SR maintenance | AAD | LAAO | OAC | Deaths |
|---|---|---|---|---|---|---|---|---|---|---|
| Ad N. [S35] | 370 | CABG and valvular | Paroxysmal (42–51%), persistent (38–45%), long-standing persistent (11–13%) | 100% | 2 | 83–91% | 16–33% | N/D | 40% at 1 year | 6.1–8.5% |
| Musharbash F. [S37] | 10 859 | CABG and valvular | Paroxysmal (45% in ablation group) and non-paroxysmal (55% in ablation group) | **4%** | 4.2 | N/D | N/D | 100%ᵃ | N/D | 38% at 10 years (31% in paroxysmal, 39% in non-paroxysmal) |
| Henn M. [S32] | 576 | CABG and valvular | Paroxysmal (41%), persistent/long-standing persistent (58%) | 100% | 3.7 | 73% at 5 years (78% in both paroxysmal and non-paroxysmal after exclusion of patients with non-box lesion sets) | 69% freedom from ATA and AAD at 5 years (66% in both paroxysmal and non-paroxysmal after exclusion of patients with non-box lesion sets) | 100%ᵃ | 45% | N/D |
| Ad N. [S38] | 787 137 with 5-year follow-up | CABG and valvular | Paroxysmal (4%), persistent (36%), long-standing persistent (60%) | 100% | Complete 5-year follow-up | 85% at 5 years; atrial arrhythmia recurrence-free survival in 63.5% | 29 | 100% | 38% | N/D |
| Wu C. [S36] | 207 | MVR | Persistent (100%) | 100% | 8.4 | 74.4 | N/D | N/D | N/D | 8.2% |
| Hwang S. [S39] | 362 | MVR | Paroxysmal (23%), persistent/long-standing persistent (87%) | 100% | 5.4 | 82.6 at 5 years | 26.2 at >3 months | N/D | 14.9% | 5.8% |
| Pecha S. [47] | 503 | CABG and valvular | Paroxysmal (41%), persistent (59%) | 100% | 1 | 59.9% (67.3% in paroxysmal, 54.8% in persistent) | N/D | 0 | N/D | 5.1% at 1 year |
| Cheng Y. [72] | 2828 | CABG and valvular, aorta | N/D | 100% | 5.1 | N/D | N/D | N/D | N/D | 5.7% |
| Osmancik P. [70] | 108 | CABG and valvular | Paroxysmal (27%), persistent (23.2%), long-standing persistent (49.8%) | 100% | Complete 5-year follow-up | 26.9% | 17% | 0 | 79% | 25% CVD mortality |
| Kim H. [S40] | 1965 | CABG and valvular | Paroxysmal (11%), persistent (89%) | 100% | 4.1 | 77.1% at 5 years | 4.4% non-AF on AAD at 5 years | 0 | 65.3% at 5 years | 13.3% |

脚注（原文逐語）:
- 略語: "AAD: antiarrhythmic drugs; AF: atrial fibrillation; ATA: atrial tachyarrhythmia; CABG: coronary artery bypass grafting; CVD: cardiovascular diseases; LAAO: left atrial appendage occlusion; MVR: mitral valve replacement/repair; N/D: no data; OAC: oral anticoagulation; SA: surgical ablation; SR: sinus rhythm."
- ᵃ "All reported procedures were Cox-Maze maze IV, assuming concomitant left atrial appendage closure."（原文の "Cox-Maze maze IV" は誤植と思われるがそのまま転記）

**Table 1 についての注意点（読み手として必ず記録すべき整合性の問題）**:
- **AF 病型の合計が 100% にならない行がある**: Hwang S. [S39] は 23% + 87% = **110%**、Henn M. [S32] は 41% + 58% = **99%**。**原著の記載ミスまたは丸めの可能性。そのまま引用しない方が安全。**
- **単位（%）が欠落したセルがある**: Wu C. の SR maintenance "74.4"、Hwang S. の "82.6 at 5 years"、"26.2 at >3 months"、Ad N. [S38] の AAD "29"。**いずれも原文に % 記号がない**。文脈上 % と推定されるが原文どおり記載した。
- **本文と Table 1 の不一致**:
  - Cheng Y. [72] は**本文では "encompassing 11 459 patients"** だが **Table 1 では N = 2828**（アブレーション群のみの可能性が高いが原文に説明なし）。**★要確認**
  - Pecha S. [47] は**本文では "with a mean follow-up of 5.9 years ... SR was sustained in 56.6%"**（この 5.9 年/56.6% は [49] 由来と読める）だが、**Table 1 では follow-up 1 年・SR 59.9%**。**本文と表で数値が別物**なので、統合レビューでは必ずどちらを引いたか明示すること。**★要確認**
  - Musharbash は**本文では "Masherbash"** と綴られている（同一人物）。
- **Ad N. [S38] の "787 137 with 5-year follow-up"** は、Concomitant SA 100%・"Complete 5-year follow-up" と併記されており、**患者数なのか患者-年なのか、あるいは母集団全体なのかが原文から判別できない**。**この数値の単独引用は避けるべき。**
- **Musharbash F. [S37] の Concomitant SA = 4%** は「コホート中で SA を受けた割合」と読める（他行の 100%＝SA 施行例のみのコホート、とは意味が異なる）。**列の定義が行によって揺れている。**
- **Osmancik P. [70]（PRAGUE-12 5 年）の SR maintenance = 26.9%** は、他行（数値が示された 7 行のレンジは **59.9–91%**：Pecha 59.9%、Henn 73%、Wu 74.4、Kim 77.1%、Hwang 82.6、Ad N. [S38] 85%、Ad N. [S35] 83–91%）と比べ極端に低い。RCT・長期・厳格判定であることを反映している可能性が高く、**観察研究の高い成功率と単純比較してはならない。**
- **LAAO 列に "0"（Pecha, Osmancik, Kim）がある** ＝ LAAO 未施行コホート。SA 単独でも生存利益が示された研究群と、LAAO 100% の研究群が混在している。

- **限界**:
  - 【著者記載】（原文 "Limitations" セクションの逐語要約）
    1. "most available data on SA come from **observational studies and registries**, with **limited RCT data—particularly in non-mitral procedures or stand-alone ablation**."
    2. "the **follow-up periods in many RCTs are relatively short**, which may **underestimate the long-term efficacy and safety** of SA techniques."
    3. "**Selection bias** remains a concern in registry-based studies, because **patients selected for ablation are often younger and at lower operative risk**, potentially skewing outcomes."
       （※ ただし §63 の HEIST registry 解析 [75] では逆の所見が示されており、総説内で整合していない）
    4. エビデンスが限定的／未確定の領域として: "optimal strategies for **OAC discontinuation after SA and/or LAAO**"、"the **safety of LAAO in patients with diastolic dysfunction** or those undergoing **aortic procedures without concomitant SA**"
    5. "Ongoing trials, such as the **LeAAPS study**, are expected to clarify the role of **prophylactic LAAO in patients without prior AF** but with high-risk features."
    6. "the **long-term impact of LAAO alone on heart failure symptoms and on haemodynamics** in select subgroups remains to be determined."
  - 【読み手として】
    7. ★**narrative review であり、系統的検索・選択基準・バイアス評価が一切ない。** Table 1 の 10 研究がどう選ばれたかの基準は原文に無く（"selected studies" とのみ）、**選択自体にバイアスがある可能性を排除できない**。統合レビューでは本論文を「エビデンス源」ではなく **「論点の地図」**として使うのが適切。
    8. ★**リズム転帰の定義（blanking period、>30 秒、AT/AFL の扱い、AAD の扱い、モニタリング手段と実施率）が全編を通じて一切定義・統一されていない。** 「44–94%」「57–88%」「約 70% vs 30%」「87%」等の数値は**互いに比較不能**である。
    9. ★ **RA lesion の重要性を強調する記述（§43, §53）と、network meta-analysis を根拠に「LA ablation が最も好ましい」とする記述（§76）が並存し、本総説は bi-atrial vs LA-only の争点に決着をつけていない。** 本総説を根拠に lesion set を決めることはできない。
    10. ★**PFA の外科応用について「ブタのみ」と断じている（§97）**。本総説の文献検索は 2024 年 11 月投稿・2025 年 4 月改訂時点で止まっており、**外科的 PFA のヒトデータを扱う本レビューの他フラグメント（S8 等）とは記述が矛盾する**。**PFA については本論文を最新情報源として使ってはならない。**
    11. ★**AFMR（atrial functional MR）への言及がゼロ。** 本レビューのテーマの一角である AFMR／atrial secondary TR、および「AFMR に対する弁形成 + Maze」の議論は本総説には**まったく含まれていない**。この論点は他文献で埋める必要がある。
    12. ★**AFMR 同様、LAA 閉鎖の「デバイス／手技（clip vs 縫合 vs stapler）」「閉鎖成功率／残存フロー」の議論もない。** LAAO は「する／しない」の二値でしか扱われていない。
    13. 多くの引用数値に **95%CI と P 値のどちらか（または両方）が欠落**している（本ノートで逐一明示した）。特に「50% 増」「32% 増」「40% 高い」「2.8 倍」「58% 低下」「6% greater odds」等は **点推定のみ**で、有意性の裏付けが本総説からは確認できない。
    14. **企業（AtriCure 等）との COI が濃い執筆陣**であり、かつ ESC の **外科系** working group による endorsement である点は、「SA を推進する」方向のバイアスとして割り引いて読む必要がある。
    15. 本文の "¼" は pdftotext による "=" の文字化けである（例: "P ¼ 0.014" = "P = 0.014"）。本ノートでは "=" に直して転記した。また "CHADS2-VA2Sc" は原文表記であり CHA₂DS₂-VASc の誤植と思われる。

- **外科への含意**:
  > 【原著の主張】＝本総説が明示的に述べていること。【読み手の推論】＝本ノート作成者による解釈で、原文には書かれていないこと。

  1. **【原著の主張】同時 SA は「やるべきだが、やられていない」治療である。** 術前 AF 患者の SA 実施率は 22–38%（Abstract では 22–48%、STS 2011–2014 では 86 941 例中 42 066 例＝48.3%）にとどまり、STS ガイドラインは MV で class I/level A、CABG・AVR・combined で class I/level B を与えている（**二次引用**）。2024 ESC/EACTS は MV を class I にアップグレードし、非僧帽弁手術に class IIa を新設した（**二次引用**）。
  2. **【原著の主張】CM IV は依然として gold standard であり、FDA が承認した唯一の術式である。** 一方で複雑さ・侵襲・時間を理由に多くの外科医が回避しており、**「フル CM ができないなら PVI + box lesion でも、何もしないよりは遥かに良い」**（[19] を根拠）。
  3. **【原著の主張】手術時間の延長を理由に SA を避けるべきではない。** CPB・遮断時間は確かに延びるが、合併症率・30 日死亡に差はない（[24, 25, 41, 42]）。延長の多くは learning curve に起因する。
  4. **【原著の主張】lesion set は AF 病型で決める。** PAF ではトリガー隔離（PVI 中心）で足りうるが、non-PAF では **substrate（LA 後壁隔離 + 両心房の追加ライン）**を標的にしなければ持続効果は得られない。良好なリズム転帰の予測因子は **LA 径 <6 cm・PAF・AF 罹病期間が短い・術直後に SR へ復帰**（[47]）。LA 評価は **LA volume index または LA reservoir strain** の方が優れる（本総説の提言、[31]）。
  5. **【原著の主張】RA lesion を軽視すべきでない。** RCT での PPM の最多理由は **heart block であって洞結節機能不全ではない**（[27]）ため、「PPM が増えるから両心房はやめる」という論法は成立しない。MV 手術後の atrial tachycardia が多い（[56]）ことも RA lesion の必要性を示唆する。
     **【読み手の推論】** ただし本総説は同時に「LA ablation が最も好ましい」とする NMA（[S7]、7207 例）も紹介しており、**両心房 vs LA 単独の決着はついていない**。実務的には「MV 手術 + non-PAF + 心房性頻拍のリスクが高い症例で bi-atrial を検討し、CABG/AVR 単独では LA lesion に留める」という McCarthy–Cox 流のテーラリング（Fig. 2）が本総説の想定する落としどころと読める。
  6. **【原著の主張】LAAO は SA と組み合わせてこそ意味がある。** LAAOS III は LAAO の脳卒中抑制を示したが（HR 0.67, 95%CI 0.53–0.85, P=0.001）、Mehaffey [S18] では **LAAO 単独 vs AF 無治療の院内脳卒中は OR 0.99（0.93–1.06, P=0.81）で有意差なし**、**SA + LAAO で初めて OR 0.89（0.83–0.94, P<0.001）**となる。KROK でも **SA+LAAO > SA 単独 > LAAO 単独**の生存 gradient（log-rank P<0.001）。
  7. ★**【原著の主張】左室拡張障害例では LAAO 単独（SA なし）が有害になりうる。** LAA が left heart の capacitance chamber として心拍出を維持している可能性があり、**KROK では AVR + LAAO 単独が「AF 無治療」より長期生存が悪かった**（[S19]）。
     **【読み手の推論】** これは「LAAOS III の結果を根拠に、AF 手術をしないまま LAA だけ閉じる」という運用への明確な警告であり、実務上きわめて重要。HFpEF/拡張障害の強い AVR 症例では、SA なしの LAAO 単独は少なくとも慎重に。
  8. **【原著の主張】SA を行っても（LAAO を併施しても）抗凝固は中止できない。**（[31] に依拠）周術期は 2024 EACTS perioperative medication guideline に従い、**SA の成否によらず**出血リスクが低ければ早期再開。
  9. ★**【原著の主張】生存曲線は交差する。** 台湾の全国データ（n=11 459）では **SA 群の 2 年生存はむしろ悪く**、中期で曲線が交差した後に長期で逆転して HR 0.75（0.69–0.81, P<0.001）となる。
     **【読み手の推論】** 余命が 2〜3 年に満たないと見込まれる高齢・高リスク症例では、同時 SA の生存利益は回収できない可能性がある。逆に、長期予後が期待できる症例ほど適応は強い。この「時間軸」の説明はインフォームドコンセントで明示すべき。
  10. **【原著の主張】RCT では生存利益は示されていない**（23 RCTs メタアナリシス: RR 1.07, 95% CI 0.75–1.52, P=0.88）。生存利益はレジストリ・PSM 研究由来である。ただし HEIST 解析（[75]）は「健康な患者を選んでいるだけ」という単純な選択バイアス説を否定している。
      **【読み手の推論】** 「SA は生存を改善する」と断言する際は、必ず **エビデンスレベルが観察研究である**ことを併記すべき。
  11. **【原著の主張】術者経験は成績を規定する。** 50 例以上の経験が SR を予測し、10 例ごとに odds が 6% 上昇（[55]）。75 歳超では再発リスクが有意に高い（[54]）。
      **【読み手の推論】** 施設としては症例を集約し、術者を絞って経験を積ませる方が、全員が少数例ずつ行うより成績が良い可能性がある。
  12. **【原著の主張】Hybrid は persistent／long-standing persistent AF と高周術期リスク例で有望。** HARTCAP-AF・CEASE-AF の 2 RCT がいずれも CA に対する優越性を示し、安全性に差はなかった。thoracoscopic 単独が劣る理由は **両心房 lesion が作れないこと**と **unipolar デバイスによる非貫壁性病変**。ただし "their superiority over conventional AF surgery is still uncertain"。
  13. **【原著の主張】PFA の外科応用はまだブタ実験段階（本総説時点）。**
      **【読み手の推論】** 本総説の PFA 記述は 2025 年前半で情報が止まっている。**統合レビューの PFA パートは本論文に依拠してはならない。**
  14. **【読み手の推論】本総説の最大の実務的価値は、(a) LAAO 単独の限界と拡張障害例での害の可能性、(b) 生存曲線の交差という時間軸、(c) 「フル CM が無理なら PVI+box でもやれ」という現実的スタンス、(d) RA lesion と heart block の因果の整理、の 4 点にある。** リズム成功率の数値そのものは定義が不統一なので、統合レビューでは一次論文（CTSN、Damiano 系、Aerts IPD-MA 等）に置き換えるべき。

- **推奨クラス**:
  - **本論文自身は推奨クラス／LOE を一切提示していない。**（narrative review であり、ガイドライン文書ではない）
  - 本文中に現れる **"class I, level A"、"class I, level B"、"class IIa, level B"（STS 2017 [29]）**、**"class I"／"class IIa"（2024 ESC/EACTS [31]）**は **すべて二次引用**である。
  - 2024 EHRA/HRS/APHRS/LAHRS consensus [30] については **推奨文の趣旨のみが要約されており、Class/LOE 表記は本総説に転記されていない**。
  - Figure 1 に各学会推奨の一覧が図示されているが、**図はラスタ画像でテキスト抽出不能**のため、本ノートでは Class/LOE の網羅的転記ができない。推奨の一次確認は **S1 セクション（2024 ESC/EACTS = PMID 39210723、2024 EHRA/HRS = PMID 38597857）**で行うこと。**ただし本総説が "class I, level A / class I, level B / class IIa, level B" を引いている STS ガイドラインは STS 2023（PMID 38286206）ではなく STS 2017**（[29] Badhwar V, Rankin JS, Damiano RJ et al. The Society of Thoracic Surgeons 2017 clinical practice guidelines for the surgical treatment of atrial fibrillation. Ann Thorac Surg 2017;103:329–41）であり、STS 由来の Class/LOE を一次確認する際は **STS 2017 を当たること**（S1 の STS 2023 は別文書）。

- **参考: 本総説が引用している主要試験・レジストリ名（統合レビューの追跡用）**:
  - **RCT / trial**: PRAGUE-12（5 年フォロー [70]）、CTSN [27]、HARTCAP-AF [S2 or S3]、CEASE-AF [S2 or S3]、CASTLE-AF [S15]、CASTLE-HTx [S16]、LAAOS III [S17]、OPTION trial（本文中、参照番号なし）、PULSED AF Pivotal Trial [34]、PALACS（posterior left pericardiotomy [6]）、Pilot-CRAfT [59]、**TAILOR-AF（NCT05169320）[S27]**、**LeAAPS [S28]**（いずれも進行中）
  - **レジストリ**: **STS Adult Cardiac Surgery Database** [19, 20]、**KROK**（Polish National Registry of Cardiac Surgery Procedures）[23, 24, 25, 74, S19]、**HEIST registry** [75]、Northern New England Cardiovascular Disease Study Group [73]、台湾 nationwide [72]
  - **新規術式**: **Tampa 2 Maze procedure** [S11]
  - ⚠️ **参照番号 S1–S40 は supplementary material（オンライン補遺）にのみ収載されており、本 PDF 本文の参考文献リスト（[1]–[80]）には含まれない。** したがって **Table 1 の [S32], [S35]–[S40] の書誌情報は本 PDF からは特定できない**。特定が必要なら EJCTS のオンライン補遺を別途取得すること。

---

## 横断比較表

### 表A. S2 の 2 編は「何の文献か」がまったく違う

| 項目 | Cox 2025 (Heart Rhythm) | Kowalewski 2025 (EJCTS) |
|---|---|---|
| 文書種別 | **"Iconic Figure" 欄の 2 ページ回顧エッセイ**（単著コメンタリー） | **narrative state-of-the-art review**（ESC CV Surgery WG endorsed） |
| 一次データ | **なし**（患者は n=1 の逸話のみ） | **なし**（すべて他論文の二次引用） |
| 参考文献数 | **5 件**（うち 2 件は "In press" の書籍章＝検証不能） | 本文 [1]–[80] ＋補遺 [S1]–[S40]（**S 番号は本 PDF から書誌特定不能**） |
| 原文に存在する数値 | **臨床成績・効果量に該当する数値は 0 個**（初回症例の経過に関する数値が 1987/9/25、術後5日目、90日、19年11か月1週間、3週間の 5 個。ほかに 1980/1982/1980年代・1・2・3か月フォロー・2022年35周年などの年号・時期記述あり） | 多数（ただし大半で 95%CI か P 値、あるいは両方が欠落） |
| 統計的効果量 | **0 件** | 二次引用として多数（OR/RR/HR） |
| 扱う lesion set | **cut-and-sew オリジナル Maze のみ**（RF/cryo/PFA への言及ゼロ） | CM I→II→III→IV、PVI、box、bi-atrial、hybrid、thoracoscopic、GP、PFA |
| リズム判定 | **脈の触診 ＋ 心電図**（Allessie が触診。原文は "the electrocardiogram" とのみ記載＝「安静時」の語はなし） | **記載なし**（Holter/ILR/連続モニタの語が本文に不在。Fig.4 凡例に ILR の略語定義のみ） |
| blanking period | **"at least 90 days" を明示（根拠つき）** | **語そのものが原文に出現しない** |
| 推奨クラス | **該当なし**（Class/LOE 表記ゼロ、二次引用もなし） | **自身は提示せず。STS 2017・2024 ESC/EACTS の Class をすべて二次引用** |
| COI | Adagio Medical Holdings / Lucid Diagnostics / PAVmed の取締役、AtriCure のシニアコンサルタント | 執筆陣に AtriCure 関係が多数（Maesen, La Meir, Suwalski, Hanke, Cox, de Asmundis） |
| 本レビューでの役割 | **原理と歴史的出発点の一次引用に限定** | **「論点の地図」として使う。エビデンス源にはしない** |

### 表B. Kowalewski 2025 が提示するリズム成績の一覧（★すべて定義・モニタリング法が不明）

| 集団・文脈 | 数値 | 出典番号 | CI / P |
|---|---|---|---|
| SA 全般の有効性レンジ | **44–94%** | [44] | 記載なし |
| lesion set・エネルギー・病型別レンジ | **57–88%** | [45] | 記載なし |
| RCT メタ 1 年 AF free（SA vs 対照） | **約 70% vs 30%** | [48] | 記載なし |
| 全心臓手術での SR 変換 | **3 か月 49.8% / 6 か月 57.6% / 12 か月 59.9%** | [47] | 記載なし |
| Pecha（mean f/u 5.9 年）SR 維持 | **56.6%**（PAF 67.3% vs persistent 54.8%） | [47, 49] | "significantly better" のみ、**P 値・CI なし** |
| Van Breugel SR 変換 | **paroxysmal 69.8% / persistent 44.4% / permanent 28.2%** | [50] | 記載なし |
| CM III + AVR or CABG 1 年 | **94% SR、81% が class I/III AAD 不要** | [41] | 記載なし |
| persistent AF + MV の RCT メタ | **退院時 65.1% / 6 か月 63.5% / 12 か月 67%** | [42] | 記載なし |
| MV 手術 8430 例メタの 5 年 FFA | **90.2 / 83.5 / 79.5 / 76.4 / 73.2%**（年次対応は原文が明示せず） | [53] | 記載なし |
| CPB 使用 CM の SR 回復（低侵襲手技 SR） | **87%** | [26] | 記載なし |
| Hald: persistent AF の freedom from AF | **45%（PVI） vs 63%（bi-atrial）, P=0.039** | [S6] | 95%CI なし。**群ラベルは原文に付いていない** |
| mini-Maze vs PVI RCT（n=95, mean 14.4 か月） | **80%（PVI） vs 86%（mini-Maze）** | [43] | 記載なし |
| hybrid 実世界 36 か月 FFA | **AAD 許容 72.9±2.9% / off AAD 59.0±2.5%** | [79] | ± が SE か SD か不明、CI なし |
| hybrid メタ（mean 19 か月） | **79.4%**、persistent/LSP で **70.7% vs 49.9% (CA), P<0.001** | [80, S1] | 95%CI なし |
| STAR guided CA | **80% FFA at 17 months** | [S26] | 記載なし |
| GP 隔離（long-standing persistent, 2 年） | **38.2%** | — | 記載なし |

**読み方**: これらを横に並べて比較してはならない。**blanking period・>30 秒閾値・AT/AFL の扱い・AAD の扱い・モニタリング手段と実施率が、本総説では一つも定義されていない。** 本総説自身が示した「AAD 許容 72.9% vs off AAD 59.0%」という **約 14 ポイントの差**が、定義次第で成績がどれだけ動くかの直接証拠である。

### 表C. Kowalewski 2025 が提示するハードアウトカム（効果量が明示されているものだけ）

| アウトカム | 研究・集団 | 効果量 | 95% CI | P | 出典 |
|---|---|---|---|---|---|
| 30 日死亡（SA vs 非 SA） | STS PSM **28 739 pairs** | **RR 0.92** | 0.85–0.99 | 記載なし | [19] |
| 脳卒中（SA vs 非 SA） | 同上 | **RR 0.84** | 0.74–0.94 | 記載なし | [19] |
| 院内死亡 | Elbadawi **約 48 000 例** | **3.6% vs 4.2%** | 記載なし | **<0.001** | [68] |
| 脳血管イベント | 同上 | **2.0% vs 2.8%** | 記載なし | **<0.001** | [68] |
| 全死亡（長期） | 台湾 **11 459 例** | **HR 0.75** | 0.69–0.81 | **<0.001** | [72] |
| 脳卒中（長期） | 同上 | **sub-distribution HR 0.78** | 0.67–0.91 | 記載なし | [72] |
| 10 年生存（CM IV vs 無アブレーション） | Musharbash | **adjusted HR 0.47** | 0.26–0.86 | **0.014** | [S37]（本文に番号なし） |
| 同・SA 群 vs no-AF controls | 同上 | 差なし | — | **0.85** | 同上 |
| 死亡（AVR ± CABG サブセット、CM） | [S8] | **adjusted HR 0.38** | 0.21–0.66 | **0.001** | [S8] |
| 複合エンドポイント（同、構成不明） | [S8] | **adjusted HR 0.52** | 0.35–0.76 | **0.001** | [S8] |
| 生存（**否定的**） | **23 RCTs メタ** | **RR 1.07** | 0.75–1.52 | **0.88** | [48] |
| 死亡（**否定的**） | Ad, mean 35 か月 | **log-rank 統計量 0.49** | — | **0.48** | [41] |
| 脳卒中（PRAGUE-12 5 年） | 不整脈治療あり vs なし | **sub-hazard ratio 0.32** | 0.12–0.84 | **0.02** | [70] |
| stroke or systemic embolism（LAAO） | **LAAOS III** | **HR 0.67** | 0.53–0.85 | **0.001** | [S17] |
| SA vs CA の有効性（1 年） | RCT メタ | **OR 0.37** | 0.20–0.69 | 記載なし | [17]（**原著は "CA relative to SA" の OR＝SA 優位。参照群は CA**） |
| pneumothorax（同） | 同上 | **OR 0.09** | 0.01–0.74 | 記載なし | 同上 |

---

## セクション横断の論点

1. **「一律の lesion set」という設計思想と、現代の「簡略化」志向は正面から衝突している。**
   - **Cox 2025（一次証言）**: AF は個別マッピングに導かれ得ないため、"fallback strategy" として **全例に同じ lesion set** を当てる術式を作った。目標は明示的に **"ablation of all types of AF"**、すなわち病型を問わない普遍性である。
   - **Kowalewski 2025（現状）**: 実際には PVI が **"the most frequently used surgical technique"** であり、CM IV は「複雑・侵襲的・時間がかかる」ため回避されている。総説自身も "Although this approach might be reasonable in patients with PAF, given the anatomical background of non-PAF, it appears to be **less than optimal**" と認める。
   - → **統合レビューでは「PVI 単独への簡略化は、Maze の設計原理（面積不足で macroreentry を成立させない）を意図的に放棄する行為である」と明示すべき。** ただし Kowalewski の実務的スタンス「**フル CM が無理なら PVI + box でもやらないよりは遥かに良い**」（[19] 根拠）も同時に併記すること。両者は矛盾ではなく「原理」と「現実」の階層差である。

2. **bi-atrial か LA-only か — Kowalewski 総説の内部で決着していない（★最大の未解決点）。**
   - **RA lesion 支持側（§43, §53）**: "RA lesions may be especially important in preventing macro-re-entrant arrhythmias"。RCT における PPM の最多理由は **heart block であって sinoatrial node dysfunction ではない**（[27]）＝「PPM が増えるから両心房はやめる」という論法は成立しない。MV 手術後の atrial tachycardia 増加（[56]）も傍証。Hald [S6] では persistent AF の freedom from AF が **45%（PVI） vs 63%（bi-atrial）, P=0.039**。
   - **LA-only 支持側（§76）**: bi-atrial / left atrial / PVI を比較した **network meta-analysis（7207 例, [S7]）**は「**left atrial ablation may be considered the most preferable technique**」と結論。理由は bi-atrial と同等の有効性・有意に低い PPM 率・低い再手術率・短い CPB 時間。
   - **Cox 2025 側の一次原理**: blind alleys（＝両心房を確実に興奮させる分枝）は Maze の 4 要素の 1 つであり、**両心房を活性化させることが術式定義に組み込まれている**（Figure 1 legend: "thereby preserving atrial transport function postoperatively"）。ただし Cox 2025 は「RA lesion の要否」という現代的争点には**一切触れていない**。
   - → **どちらのフラグメントも決着をつけていない。統合レビューでは「Kowalewski 総説を根拠に lesion set を決めることはできない」と明記すべき。**

3. **成功率の数値は歴史的にも横断的にも比較不能である（判定手段の問題）。**
   - **Cox 2025**: 1987 年の判定は **Allessie の脈の触診＋心電図**（原文 "the electrocardiogram"、「安静時」の語はなし）。この基準で「19 年 11 か月 1 週間の洞調律維持」が語られている。
   - **Kowalewski 2025**: モニタリング手段の系統的記載が **本文に一切ない**（Holter/ILR/continuous monitoring/7-day の語が本文に不在。Figure 4 凡例に "ILR" の略語定義があるのみ）。
   - → **「Maze の成功率は 90% を超える」といった通説を、判定手段を明示せずに引用してはならない。** 本セクションの 2 編は、AF 外科の**出発点も現在地も、リズム判定という一点で同じ弱点を抱えている**ことを示している。統合レビューではこの点を導入部の問題設定に据えるのが有効。
   - 具体的な証拠として **Kowalewski §69 の「AAD 許容 72.9%±2.9% vs off AAD 59.0%±2.5%」（36 か月 FFA、[79]）** を使うと、定義の違いだけで約 14 ポイント動くことを一発で示せる。

4. **blanking period は「Cox の一次証言」で正当化できるが、現在の総説はそれを使っていない。**
   - **Cox 2025** は blanking period = **"at least 90 days"** を明示し、根拠を **(a) 心房切開線の治癒、(b) 心房電気生理学的特性の正常化**とする。起源は初回症例の**術後 5 日目 AF（誘因: endotracheal suction）**という具体的経験である。
   - 一方 **Kowalewski 2025 は "blanking period" という語を本文で一度も使っていない**。引用している全研究の blanking の有無・長さを統一も明示もしていない。
   - → **統合レビューで blanking period を論じる際は、正当化の一次引用として Cox 2025 を使い、「現代の総説レベルですらこの定義が統一されていない」という現状批判に Kowalewski 2025 を使う**という二段構えが最も強い。
   - ⚠️ **注意**: Cox 2025 には **30 日 blanking や延長 blanking への言及は一切ない**。90 日以外の数値を Cox に帰属させてはならない。

5. **LAA/LAAO の扱いが、原型と現代で断絶している。**
   - **Cox 2025（原型）**: オリジナル Maze では **both atrial appendages excised**（LAA だけでなく **RAA も切除**）。これは後付けの追加手技ではなく **lesion set の構成要素**である。
   - **Kowalewski 2025（現代）**: LAAO は「する／しない」の二値でしか扱われず、**デバイス／手技（clip vs 縫合 vs stapler）・閉鎖成功率・残存フローの議論はゼロ**。RAA については言及なし。
   - しかも現代データは **LAAO 単独では脳卒中は減らない（OR 0.99, 95%CI 0.93–1.06, P=0.81）** ことを示し、**SA と組み合わせて初めて OR 0.89（0.83–0.94, P<0.001）**となる。さらに脳卒中抑制は index hospitalization に限定され、**30 日以降 OR 1.09（0.96–1.25, P=0.17）・3 年 OR 1.06（0.84–1.34, P=0.62）で消失**する。
   - → **未解決**: 「Cox-Maze では RAA も切除していた」という原型の事実と、現代の LAAO-only 志向の乖離は誰も検証していない。統合レビューでは論点として提示するにとどめるべき（**両フラグメントとも RAA 切除の臨床的効果を検証したデータを提示していない**）。

6. **「SA は生存を改善するか」— 観察研究と RCT が正面から食い違い、しかも時間軸で符号が変わる。**
   - **肯定側（観察）**: 台湾 11 459 例 **HR 0.75 (0.69–0.81, P<0.001)**、Musharbash **adjusted HR 0.47 (0.26–0.86, P=0.014)**、[S8] **adjusted HR 0.38 (0.21–0.66, P=0.001)**、多施設 20 407 例で 5 年生存改善（効果量記載なし）、KROK 複数解析。
   - **否定側（RCT）**: **23 RCTs メタ RR 1.07 (0.75–1.52, P=0.88)**、Ad [41] **log-rank 0.49, P=0.48**。
   - **時間軸**: 台湾データでは **SA 群の 2 年生存はむしろ悪く**、**midterm crossover** を経て長期で逆転する（**クロス時点の具体値は原文に記載なし**）。
   - **選択バイアス論争**: 総説の Limitations は「アブレーションを受ける患者は若く低リスク」と述べるが、**§63 の HEIST 解析 [75] では逆に「より高リスクの患者ほど SA を受けており、EuroSCORE II サブグループ間で生存利益の大きさは同程度」**と報告されている。**総説内で整合していない（★要確認・一次資料 [75] の確認推奨）**。
   - → **統合レビューでの書き方**: 「SA は生存を改善する」は**観察研究由来**と明記し、**RCT では示されていない**ことと、**利益の回収に数年かかる（2 年時点ではむしろ不利）**ことを必ず併記する。

7. **PFA の記述は本総説の時点で既に古い（S8 との整合性に注意）。**
   - **Kowalewski 2025 §97**: 外科的 PFA について **"currently available evidence considers the application of PFA in swine alone" [S25]** — ブタ実験のみ、ヒトデータはゼロという評価。
   - しかし投稿 2024 年 11 月・改訂 2025 年 4 月で検索が止まっており、**外科的 PFA のヒトデータを扱う本レビューの他セクション（S8 等）とは記述が矛盾する**。
   - → **PFA については本論文を情報源として使ってはならない。** 統合レビューでは「2025 年半ばの総説時点でも外科 PFA はブタのみと評価されていた」という**時代記述**としてのみ引用可。
   - **Cox 2025** 側もエネルギー源（RF/cryo/PFA）に**一切言及していない**（原文の表現は "atrial incisions" / "lesions of conduction block" のみで、"cut-and-sew" の語すら出現しない）ため、PFA の議論は S2 の 2 編ではまったく支えられない。ただし Cox の "Of course not!"（Maze はいずれ置き換えられる）は、**PFA/ハイブリッドへの発展を位置づける序論の引用としては極めて有効**。

8. **本セクションで埋まらない穴（他セクションで補うべき論点）。**
   - **AFMR（atrial functional MR）／atrial secondary TR**: **両フラグメントともゼロ言及**。S2 では一切支えられない。
   - **LAA 閉鎖のデバイス・手技論**（clip vs 縫合 vs stapler、閉鎖成功率、残存フロー）: Kowalewski に議論なし、Cox は「切除」しか語らない。
   - **リズム判定プロトコルの具体**（何日モニタ、実施率）: 両者ともなし。
   - **Figure 1（各学会推奨の横並び）・Figure 2（McCarthy–Cox の decision flowchart）・Figure 3（CM の進化）・Figure 4（SR 変換の関連因子）はすべてラスタ画像で本文から復元不能**。特に **Figure 2 の分岐条件（LA 径や AF 持続期間の閾値）**は統合レビューで最も欲しい情報だが、**原著 [33] McCarthy PM, Cox JL. J Thorac Cardiovasc Surg 2025;169:907–15 を別途参照する必要がある**。
   - **推奨クラスの一次確認**: Kowalewski が引く Class/LOE はすべて二次引用。一次確認は **S1 セクション（2024 ESC/EACTS = PMID 39210723、2024 EHRA/HRS = PMID 38597857）**で行うこと。**なお Kowalewski の引く STS の Class/LOE は STS 2017（[29] Badhwar V et al. Ann Thorac Surg 2017;103:329–41）由来であり、S1 の STS 2023（PMID 38286206）とは別文書である。**

9. **数値の食い違い（★要確認リスト）。**
   - **Kowalewski 内部**: 本文 "**22–38%**" vs Abstract "**22% and 48%**"（SA 実施率）。→ **両方併記。48% は STS の 48.3% を指す可能性があるが原文はそう述べていない。**
   - **Kowalewski 内部**: Cheng Y. [72] は本文 **11 459 例**、Table 1 **2828 例**。→ **どちらを引用したか必ず明示。**
   - **Kowalewski 内部**: Pecha S. [47] は本文 **mean f/u 5.9 年・SR 56.6%**（[49] 由来と読める）、Table 1 **f/u 1 年・SR 59.9%**。→ **本文と表で別物。**
   - **Kowalewski 内部**: Table 1 の AF 病型合計が Hwang S. [S39] で **110%**、Henn M. [S32] で **99%**。→ **そのまま引用しない。**
   - **Kowalewski 内部**: 選択バイアスの方向が Limitations（若く低リスク）と §63 HEIST（より高リスク）で逆。
   - **Kowalewski 内部（★解決済み・食い違いではない）**: [17] の OR 0.37（有効性）と OR 0.09（気胸）は、いずれも**原著 Huang H et al. JTCVS 2022;163:980–93 が「CA relative to SA」として報告した OR**（0.37 ＝ CA の 1 年成功オッズが SA の 0.37 倍＝SA 優位、0.09 ＝ CA の気胸オッズが SA の 0.09 倍＝SA で気胸が多い）。本総説が参照群を明記していないだけで、**内部不整合ではない**（一次資料で確認済み）。
   - **2 編間の COI 記載差**: Cox の開示先が Cox 2025 では 4 社（Adagio Medical Holdings / Lucid Diagnostics / PAVmed 取締役、AtriCure シニアコンサルタント）、Kowalewski 2025 では 5 社（Adagio Medical, AtriCure, PAVmed, Lucid Diagnostics, **PotentiaMetrics**）。→ **どちらか一方に統一して引用しない。**
   - **なお、2 編の間で「同一の臨床数値が食い違っている」箇所は存在しない**（Cox 2025 に臨床成績数値が 0 件のため、そもそも突き合わせ可能な数値がない）。

---

## 統合レビューで使える一文（引用可能な形）

1. Cox 自身の回顧によれば、Maze 手術の lesion set は個別マッピングに基づいて設計されたものではない。「一度成立した AF は、片側または両側の心房に 2 個以上の大きな macroreentrant circuit が同時に存在することを特徴とし、他の不整脈の手術と違って AF 手術はマッピングに導かれ得ない」ことが判明したため、彼らは "fallback strategy" として **全例に同一の術式を適用する**方針を採った（Cox JL, Heart Rhythm 2025;22:2735–2736）。

2. Maze の設計原理は「lesion を密に置き、かつ lesion 間の心筋領域を互いに連結したまま残せば、面積不足のため大きな macroreentrant circuit が形成され得ない」という critical mass の考え方にある。この原理により、心房を興奮不能にしてしまう "bread-loafing" は明確に否定された。**具体的な lesion 間距離の数値は原著に示されていない。**

3. Maze という名称は lesion 配置の幾何学そのものを指す — **1 つの入口（洞結節）、1 つの出口（房室結節）、その間の 1 本の true route、そして両心房を興奮させるために true route から分岐する複数の blind alleys**。blind alleys は術後の心房輸送能を温存するための必須構成要素であり、lesion を追加すればするほど良いという発想は原理的に否定されている。

4. オリジナル Maze の lesion set は **「両心耳を切除し、肺静脈を隔離し、適切に配置した心房切開線で最も一般的な reentrant circuit の伝導路を遮断する」**ものであった（Cox 2025 Figure 1 legend、図自体は Cox JL et al. J Thorac Cardiovasc Surg 1991;101:569–583 の Figure 9 の再掲）。すなわち **左心耳のみならず右心耳の切除も原法の構成要素**であり、現代の「LAA 閉鎖のみ」との相違は認識しておく必要がある。

5. 初回の Maze 手術は **1987 年 9 月 25 日**に施行された。この患者は**術後第 5 病日に気管内吸引を契機として AF を発症**したが digoxin と procainamide で洞調律に復した。procainamide は術後 2 か月時点で severe lupus syndrome のため中止され（中止後に消失）、術後 3 か月には抗不整脈薬なしで洞調律であった。以後 **19 年 11 か月 1 週間**にわたり抗不整脈薬なしで洞調律を維持し、Maze 手術 20 周年の**ちょうど 3 週間前**に AF を再発、β遮断薬に即座に反応した。

6. Cox は初回症例（術後 5 日目 AF）を語る文脈で、当時 blanking period の必要性を認識していなかったと述懐している（※「この症例が概念の起源である」とまでは原文は述べていない）。Cox は「当時我々は、外科手術の成功/失敗を正確に判定できるようになるまでに、**心房切開線が治癒し心房の電気生理学的特性が正常に戻るための少なくとも 90 日（"blanking period"）を置くことが絶対に必要である**と知らなかった」と述べている。**外科的アブレーション試験で blanking period を設定する際の正当化として、この一次記述を引用できる。**

7. ただし 1987 年当時のリズム判定は、来訪していた Maurits Allessie 教授に患者の脈を触れてもらい規則的であることを確認し、心電図で洞調律を確認するというものであった。**歴史的な Maze の成績と、連続モニタリングと >30 秒閾値で評価される現代試験の成績は直接比較できない。**

8. Cox は 2022 年の初回 Maze 手術 35 周年記念の場で「Maze 手術はあと 35 年続くと思うか」と問われ「**もちろん続かない！ しかし 35 年前に同じ質問をされていたら、同じ答えをしていただろう**」と答えている。（※ ここから先は読み手の敷衍であり Cox の言明ではない）外科的 AF 治療を「原理（macroreentry の面積制限と伝導路の温存）を保ちながら手段を交換していく歴史」と位置づける読み方は成立しうるが、**原文は RF/cryo/PFA を含む後継技術に一切言及しておらず、Cox がその発展系列を容認したという記述は存在しない**。

9. 心臓手術患者における術前 AF の有病率は患者背景と術式により **6.1% から 61.8%** と幅があり、術前 AF は CABG **>360 000 例**の解析で **adjusted 30 日死亡を 50%、major morbidity を 32% 増加**させる（Kowalewski M et al., Eur J Cardiothorac Surg 2025;67:ezaf187。**95%CI・P 値は原著総説に記載されていない**）。

10. それにもかかわらず同時外科的アブレーションは十分に実施されていない。同総説は本文で「術前 AF 症例の **約 22–38%** がアブレーションを受けている」と述べる一方、**Abstract では 22–48% と記載しており記述が一致しない**。STS database（2011–2014）では術前 AF **86 941 例**中 **42 066 例（48.3%）**が外科的アブレーションを受け、STS 2022 update では **年間 20 000 件超**で横ばいと報告されている。

11. 短期アウトカムでは、STS database の傾向スコアマッチング（**28 739 patient-pairs**）で同時外科的アブレーションは 30 日死亡 **RR 0.92（95%CI 0.85–0.99）**、脳卒中 **RR 0.84（95%CI 0.74–0.94）**と関連し（**P 値は総説に記載なし**）、約 48 000 例の別解析では院内死亡 **3.6% vs 4.2%（P<0.001）**、脳血管イベント **2.0% vs 2.8%（P<0.001）**であった。

12. 長期生存については観察研究と RCT が食い違う。台湾の全国データ（**11 459 例**）では全死亡 **HR 0.75（95%CI 0.69–0.81, P<0.001）**であったが、**23 の RCT を統合したメタアナリシスでは生存利益は認められなかった（RR 1.07, 95%CI 0.75–1.52, P=0.88）**。総説はこの乖離を、RCT の観察期間が短くイベント数が不足していること、レジストリには選択バイアスがあることで説明している。

13. さらに重要なのは時間軸である。同じ台湾データでは **外科的アブレーション群の 2 年生存はむしろ不良**であり、**中期に生存曲線が交差した後**に長期で予後が逆転している（**交差時点の具体値は総説に記載なし**）。余命が短いと見込まれる症例では生存利益を回収できない可能性があり、インフォームドコンセントで説明すべき点である。

14. 手術時間の延長を理由に同時アブレーションを避けるべきではない。総説は「体外循環時間と大動脈遮断時間は有意に延長しうるが、それに帰属する合併症率の差は認められていない」とし、僧帽弁手術併施 RCT のメタアナリシスでも 30 日死亡に差はなかったと述べる（**数値・CI・P 値は総説に記載なし**）。

15. 良好なリズム転帰と関連する因子として総説が挙げるのは **左房径 <6 cm、非発作性ではなく発作性 AF、AF 罹病期間が短いこと、術直後に洞調律へ復帰すること**の 4 つである。加えて総説は、左房評価は標準化されるべきで **左房容積係数（LAVI）または左房リザーバーストレイン**の方が優れる、と提言している。

16. 術者経験も成績を規定する。**50 例以上のアブレーション経験**が洞調律を予測し、**10 例ごとに odds が 6% 上昇**したと報告されている（**CI・P 値は総説に記載なし**）。また **75 歳超**の Cox-Maze IV では不整脈再発リスクが有意に高い（**HR・CI・P 値の記載なし**）。

17. 右房 lesion を軽視すべきではない。総説は「RCT において恒久ペースメーカ植込みの最多の理由は **心ブロックであって洞結節機能不全そのものではなく**、このことは右房 lesion の重要性を強調する」と述べている。すなわち「ペースメーカが増えるから両心房 lesion をやめる」という論法は成立しない。

18. ただし総説は同時に、bi-atrial／left atrial／PVI を比較した **7207 例の network meta-analysis** を引用し「**左房アブレーションが最も好ましい術式と考えられうる**」（bi-atrial と同等の有効性、有意に低いペースメーカ必要率、低い再手術率、短い体外循環時間）とも紹介している。**同一の総説内で bi-atrial 支持と LA-only 支持が併存しており、この争点は決着していない。**

19. Cox-Maze IV は **米国 FDA が AF 矯正手術として承認した唯一の術式**であり現時点の gold standard であるが、複雑さ・侵襲・所要時間から多くの外科医が回避している。総説の実務的スタンスは「**フルの Cox-Maze の代わりに PVI + box lesion を行うことは、不整脈をまったく治療しないことに比べれば依然として極めて有益である**」というものである。

20. 左心耳閉鎖（LAAO）は外科的アブレーションと組み合わせてこそ意味がある。risk-adjusted 解析では **LAAO 単独 vs AF 無治療の院内脳卒中は OR 0.99（95%CI 0.93–1.06, P=0.81）で有意差がなく**、**SA + LAAO で初めて OR 0.89（95%CI 0.83–0.94, P<0.001）**となる。総説はこれを「現時点で最も説得力のあるエビデンス」と評価している。

21. ただしその脳卒中抑制効果は入院期間中に限定される。SA + LAAO vs LAAO 単独の脳卒中は index hospitalization で **OR 0.88（95%CI 0.83–0.94, P<0.001）**だが、**30 日以降は OR 1.09（95%CI 0.96–1.25, P=0.17）**、**3 年時点では OR 1.06（95%CI 0.84–1.34, P=0.62）**と消失する。一方で **3 年死亡は OR 0.90（95%CI 0.88–0.93, P<0.001）**、複合エンドポイントは **OR 0.90（95%CI 0.81–0.99, P=0.035）**と SA + LAAO が優る。

22. KROK registry でも生存利益に勾配があり、「死亡率低下が最も大きいのは **SA + LAAO**、次いで **SA 単独**、最後に **LAAO 単独**であった（log-rank P<0.001）」と報告されている（**HR・CI は総説に記載なし**）。

23. 左室拡張障害を有する患者では左心耳閉鎖単独が有害となりうる。総説は「これらの患者では左心耳が左心系の主要な capacitance chamber として心拍出を維持している可能性があり、（外科的アブレーションを伴わない）その閉鎖単独は心房コンプライアンス低下により心不全症状を増悪させうる」と警告し、**KROK registry の解析では AVR 施行患者に LAAO のみを追加した場合、AF 無治療と比べて長期生存が悪化した**と報告している（**効果量・CI・P 値の記載なし**）。

24. 外科的アブレーションを行っても、たとえ左心耳閉鎖を併施しても、**抗凝固を中止する十分な根拠にはならない**というのが総説の立場である（2024 ESC/EACTS ガイドラインに依拠）。周術期は使用薬剤に応じて術前中止し、**アブレーションの成否によらず**出血リスクが低ければ術後早期に再開する。なお総説は「**同時外科的アブレーション患者の周術期管理に特化した推奨は現時点で存在しない**」と明記している。

25. ハイブリッドアブレーションは persistent／long-standing persistent AF と周術期高リスク例で有望とされる。RCT は **HARTCAP-AF と CEASE-AF の 2 件**で、いずれもカテーテルアブレーションに対する優越性を示し安全性に差はなかった（**効果量・CI・P 値は総説に記載なし**）。胸腔鏡単独が劣る理由として総説は「**両心房 lesion を達成できないこと**」と「一部研究で **unipolar デバイスのみを使用し、心外膜側で非貫壁性の lesion しか作れなかったこと**」を挙げている。

26. 本総説が引用するリズム成績（SA 全般で **44–94%**、lesion set・エネルギー・病型により **57–88%**、RCT メタで 1 年 AF free **約 70% vs 対照 30%**、僧帽弁手術 8430 例メタの 5 年 FFA **90.2/83.5/79.5/76.4/73.2%**）は、**blanking period・>30 秒閾値・AT/AFL の扱い・AAD の扱い・モニタリング手段と実施率がいずれも定義されておらず、互いに比較できない**。総説自身が示した実世界ハイブリッドデータ — **36 か月 FFA が AAD 許容研究で 72.9%±2.9%、AAD 非使用研究で 59.0%±2.5%** — は、定義の違いだけで成績が約 14 ポイント動くことの直接的な証拠である。

27. 外科的 PFA について本総説（2025 年 6 月）は「**外科的アプローチを考えると、現在得られているエビデンスはブタでの適用のみである**。実施されたすべての lesion は貫壁性であり、心外膜アプローチにおける本手技の優れた有効性が確認された。心臓手術を受けるヒトにおける PFA の将来的な適用可能性は今後の解明を要する」と述べている。**この記述は本総説の文献検索時点（2024 年 11 月投稿・2025 年 4 月改訂）で止まっており、外科的 PFA の最新情報源として用いてはならない。**

28. なお本総説はガイドライン文書ではなく、本文中の Class/LOE は**すべて二次引用**である — STS ガイドラインの「**僧帽弁手術での SA に class I / level A**、**CABG・AVR・combined に class I / level B**、**AAD 抵抗性またはカテーテル治療抵抗性の症候性 AF に対する stand-alone SA に class IIa / level B**」、および 2024 ESC/EACTS の「**僧帽弁手術における同時 SA を class I にアップグレード**、**非僧帽弁手術における同時アブレーションに class IIa を新設**」（LOE の記載は総説になし）。**推奨の一次確認は原ガイドラインで行う必要がある。**
