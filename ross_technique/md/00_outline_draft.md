# Ross手術 手技レビュー — 章立てドラフト（v0.2）

**作成**: 2026-07-26（v0.1）／**改訂**: 2026-07-26（v0.2：未読20編＋MMCTS 4編を精読して穴を埋めた）
**位置づけ**: 精読済み文献から抽出した骨子。本文はこれを膨らませて執筆する。
**図の方針**: `[FIG-x.y]` = 挿入予定図のプレースホルダ（出典と必要な内容を明記）。`[VIDEO-x.y]` = スクショ＋原典動画へのハイパーリンク。
**姉妹ドキュメント**: `Cardiac_Surgery_Guidelines/Ross_Procedure/`（適応・患者選択・EACTS 2025 Consensus の図表22点は既に切り出し済み。**本レビューでは重複させない**）

**精読状況**: 収集した53編＋MMCTS 7編のうち、**Ross手技に関わる全編を精読済み**。未精読は Chen（生体弁耐久性・本題と無関係）と Vojacek EACTS Consensus 全文（ガイドライン側で精読済み）のみ。

---

## 全体を貫く4つの主張（Central Message）

1. **Ross手術の遠隔成績は「術式の選択」ではなく「術式の実装精度」で決まる。** Skillingtonの11例の再手術のうち10例に同定可能な技術的失敗があり、7例は最初の84例に集中。Caldaroniでは最初の4例（root replacement）のうち2例が基部拡大で再手術になり、inclusionに切り替えて以降ゼロ。Stelzerの702例では**complex症例の比率が34%→48%に上がる一方で死亡率は下がった**。**失敗は「遅発性の生物学的劣化」ではなく「初回手術の幾何学的エラー」として現れる**。

2. **「補強するか否か」には答えが出たが、「何で補強するか」には出ていない。** Mylonasの患者レベルメタ解析（補強2,514例 vs 無補強595例）は、補強群の15年生存 98.8% vs 82.6%（HR 11.9）、autograft再手術回避 86.6% vs 77.7%（HR 2.06）を示した。しかし**サブグループ解析では補強法の違いによる差はなかった**。Starnesの二尖弁成人の直接比較でも10年再介入率 4.0%（wrapped）vs 26.8%（unwrapped）と同方向。→ **本レビューは「補強は必須、方法は流派」という立場を取る**。

3. **autograftの失敗は3つのレベル（弁輪／Valsalva洞／STJ）で別々に起こる。** どの術式もこの3点を全部押さえて初めて成立する。単一の対策（例：subcommissural plicationだけ）は無効。**David の指摘が本質**：肺動脈基部のsubcommissural triangleの右室筋は移植後に壊死して線維化するため、**この三角形を外部から支えることが全術式に共通する必須条件**である。

4. **ラーニングカーブは測定可能（75-100例）で、mentorshipによって短縮できる。** Montreal 673例（CUSUM）、Baylor 234例（primary vs mentored で成績差なし）、Tirone David の「最初の5-10例には経験ある術者のmentorが必要」が一致する。

---

## 第0章　総論 — 術式の変遷と現在の3系統

### 0-1. なぜ術式が分岐したのか
- 1967年 Donald Ross、**subcoronary**（原法）。再現性が低く、術者依存が大きい
- → **free-standing full root replacement**：手技が単純化（modified Bentall様）し早期の弁閉鎖不全は減ったが、**術後7-9年で予想外の再手術増加**（無支持のPAが体循環圧に耐えられない）
- → 現在の3系統：**tailored free-standing RR＋補強** / **autologous inclusion（native大動脈基部内）** / **prosthetic inclusion（Dacron内）**、＋新興の **Ross-PEARS**

### 0-2. 3系統の設計思想の対比（本レビューの背骨となる表）

| | Tailored free-standing RR＋補強 | Autologous inclusion | Prosthetic inclusion |
|---|---|---|---|
| 代表 | El-Hamamsy (Mount Sinai) / Liebrich (Stuttgart) / Schäfers (Homburg) / Stelzer (Mount Sinai) | Skillington (Melbourne) / Afifi–Yacoub (Aswan) | de Kerchove (Brussels) / Starnes (USC) / Emani (Boston) / Schneider–Hazekamp (Leiden) |
| 支持する構造 | 弁輪＝深いLVOT留置＋外部リング、STJ＝interposition graft、洞＝native残存壁のtack | 大動脈基部全体を縮小して「鞘」にする | Dacron管が全長を支える |
| 人工物 | 最小限（リング＋短いgraft） | ほぼゼロ（部分ポリエステルバンドのみ） | 最大（Valsalva/straight graft） |
| 長所 | dynamismを保つ | 人工物ゼロ＋root-within-root | 弁輪拡大・AR例でも確実に安定 |
| 短所 | 補強箇所が分散し手数が多い | STJ>32-34mmでは適用不能、type 0 BAVに不向き | mechanotransduction喪失の懸念、幾何学的歪みでcusp prolapse、**小児では成長能を失う** |
| 最長データ | 25年（Liebrich 832例） | 25年（Caldaroni 516例） | 10年（Starnes 58例の比較コホート）〜15年（Jahanyar 102例） |

> `[FIG-0.1]` 3系統の断面模式図の並置。**出典: Mazine & El-Hamamsy, Ann Cardiothorac Surg 2021;10(4):463-475, Figure 1（A: autologous inclusion / B: Dacron inclusion / C: tailored + extra-aortic annuloplasty + interposition graft）**。CC BY-NC-ND、PMC全文あり。この1枚で本レビューの骨格が説明できる — **最優先で取得**
> `[FIG-0.2]` subcoronary vs root replacement の対比模式図（後方視、左右心房を除去した図）。**出典: Berdajs DA, Eur J Cardiothorac Surg 2014;46:944-51, Figure 1**

### 0-3. 補強の有無で何が変わるか（本レビューの前提となるエビデンス）

| 出典 | デザイン | 補強あり | 補強なし |
|---|---|---|---|
| **Mylonas 2026**（16研究、患者レベルIPDメタ解析） | RR 2,514例 vs NR 595例 | 生存 5/10/15年 **100% / 98.8% / 98.8%**、autograft再手術回避 96.4% / 94.2% / **86.6%** | 95.0% / 93.7% / **82.6%**（HR 11.9, P=.016）、95.8% / 87.6% / **77.7%**（HR 2.06, P<.001） |
| **Starnes 2023**（単一術者、成人BAV 129例） | wrapped 58 vs unwrapped 71、中央値10.3年 | autograft失敗 **3例（5.2%）**、10年再介入累積発生率 **4.0%** | 25例（**35.2%**）、**26.8%**（SHR 0.28, P=.035） |
| **Charitos**（German-Dutch Ross Registry 2,023例） | 多変量 | — | **無補強のroot replacement は再手術までの時間を短縮する独立予測因子（HR 2.4, 95%CI 1.4-4.1）** |

**ただし Mylonas のサブグループ解析では補強法の違いによる差はなかった。** → 「何で補強するか」は現時点で優劣がつかず、流派の問題である。

---

## 第1章　解剖とautograft採取 — 最初の30分で遠隔成績が決まる

### 1-1. 肺動脈弁には「線維性弁輪」がない
Mazineの教育論文が最も明快: 大動脈弁と異なり、**肺動脈弁尖は漏斗部筋（infundibular muscle）に囲まれているだけで、真の線維性弁輪を持たない**。採取後この筋は脱血管化し、**構造的支持を一切提供しない**。ここから2つの帰結が出る:
1. **筋を残さない**（trim to 2-4mm）
2. **LVOT内に深く留置し、native大動脈弁輪に支持させる**

**Davidはこれをさらに一歩進める**: 「肺動脈基部の**subcommissural triangleの右室筋は切除すべきである。壊死して線維組織に置換されるからだ**。したがって、治癒過程での肺動脈弁輪の拡大を防ぐために、**subcommissural areaがnativeの大動脈弁輪・基部組織で外部から支持されていることが極めて重要**である。」
→ これが全術式に共通する「なぜ外部支持が要るのか」の生物学的根拠であり、本レビュー全体の理論的支柱になる。

### 1-2. 幾何学の原則（David）
- 健常な小児・若年成人では**肺動脈弁STJは大動脈弁STJより2-3mm大きい**。半月弁の弁輪はそのSTJよりわずかに大きい。大動脈弁疾患ではこの関係が崩れている
- 大動脈位に移す際、**横径だけでなく各cuspの三日月形の付着形状も保たねばならない**
- **可能な限り、肺動脈弁輪はLVOT周の大部分でnative大動脈弁輪より低い位置に置く**
- **正常な大動脈弁輪は大柄な人でも25mmを超えることは稀**。弁輪径とBSAの関係は**BSA 2 m²を超えると頭打ちになる**

### 1-3. 採取のランドマーク（各流派の記載を統合）

| 手順 | Mount Sinai (Mazine) | Melbourne (Skillington) | Leiden (Schneider) | Boston (Dafflisio) | Dallas (Chandra) |
|---|---|---|---|---|---|
| PA離断位置 | 右PA起始の5mm近位（**右PAは常に左PAより近位＝ランドマーク**） | 肺動脈弁STJの5-8mm上 | 左右PA合流部の直下 | — | — |
| RVOT切開 | 右角鉗子を弁を通して挿入 →「poke a hole」非対面尖の5mm下 | 右角鉗子で作った圧痕上に、弁の5mm近位で横切開 | 右角鉗子を弁尖基部の5mm下に置いてガイド | hinge pointの3-4mm下。**最初は浅く切って、そこからskive up** | 右角鉗子を弁輪の6-8mm下に |
| 残す筋 | cusp insertionから3-5mm以内 | — | 過剰筋は全て切除（**残すとLVOTに膨隆する**） | 2-3mm | — |
| 第1中隔枝 | **左対面尖のnadirの約1cm下に出る。RVOT筋内に白い線として見えることが多い** → cusp insertion lineの2-3mm下に留まれば回避できる | 左後方、心内膜面から深さ可変 → 見えたら避ける | **心室中隔レベルで右室壁と左室壁の筋線維の走行方向の違いが必ず観察される。その層間が剥離面であり、そこを辿れば第1中隔枝は容易に同定・温存できる** | 浅く切ってskive upで回避 | #15刀で漏斗部中隔上部の後方筋束を部分的に分割 |

> **Schneiderの「筋線維の走行の違いを見て層を選ぶ」は、他のどの論文にもない最も具体的な記載**。本レビューで前面に出す価値がある。

**補強法別の例外**: Urganci（Vienna, root-reinforced Ross）は「**Valsalva人工血管への再植込みを容易にするため、弁輪下に最低5mmの筋組織を採取する**」としており、trimの原則と真逆。Dacron内に固定する術式では縫い代が要るという事情による。

> `[FIG-1.1]` **第1中隔枝の位置**。出典: **Mazine A, Ann Thorac Surg 2018;105:1294-8, Figure 1**（赤アスタリスクで第1中隔枝、RVOT筋内の白い線を図示）
> `[FIG-1.2]` **autograftへの針の通し方**。出典: **同 Figure 2**（内→外、肺動脈弁尖のhinge lineに正確に入れ、垂直でなく接線方向にhinge lineの1-2mm上へ抜く＝漏斗部筋を完全に除外する）
> `[FIG-1.3]` **筋線維の層間に見える2本の中隔枝**。出典: **Schneider A, MMCTS 2017, Figure 2** → https://mmcts.org/tutorial/828
> `[VIDEO-1.1]` autograft採取（Skillington, JTCVS Tech 2021, Video 1）→ https://www.jtcvs.org/article/S2666-2507(21)00698-2/fulltext
> `[VIDEO-1.2]` autograft採取床の止血（同 Video 2：左右冠動脈口から順行性心筋保護液を流しながらdiathermy）

### 1-4. 冠動脈のpitfall
- **「冠動脈ボタンを大動脈から剥がす」のではなく「大動脈を冠動脈から剥がす」**（Mazine）。直接損傷リスクが激減する。低出力電気メスで大動脈壁に平行な層を左房天蓋まで。右冠も「大動脈を右室から剥がす」
- **ボタン下縁の大動脈カフを2mm超残さない** → 拡張期に冠動脈の動的閉塞を起こしうる（Mazine）
- **inclusion系では左冠動脈のkinkingが最大の落とし穴**。Skillingtonは左冠周囲の窓を内外側にやや広く切除。Caldaroni 516例の唯一の早期死亡が**左主幹kinkingによる前壁梗塞**
- 遮断解除後、**両冠動脈が屈曲なく基部から出ていることを必ず目視確認**（Skillington、複数論文で繰り返し強調）
- **Saidのtip**: 右冠動脈ボタンは**遠位大動脈吻合の後壁縫合線を完成させてから**植えてもよい。基部の回旋を防ぎ、特に肥満患者で右室上の心外膜脂肪により近位RCAが圧迫されるのを回避できる
- **Schneiderのtip**: 右冠は術後に元より高い位置に来るため、**遠位吻合を済ませてから最後に再建する**

**症例で見る帰結（Koliastasis, JACC Case Rep 2025）**: 26歳男性、二尖弁の高度ARにRoss。術後ICUで一旦は正常心電図だったが、夜間の定期心電図で前壁ST上昇。**大動脈造影では両冠動脈口の植込みは正常に見えたが、冠動脈造影でLADの起始部完全閉塞**。PCIで再開通させたが穿孔を来し、被覆ステントとImpella 5.5を要した。→ **「造影で冠動脈口が正常に見えても、その先の屈曲・閉塞は否定できない」**

> `[FIG-1.4]` 冠動脈奇形unroofing後のRoss。出典: **Verdi KG, JTCVS Tech 2024;28:35-8, Figure 2（A-E: 前回修復のpledget糸と unroofed ARCA のtunnel／左右尖の交連からの剥離と線維性肥厚／弁尖切除と冠動脈ボタン授動／modified inclusionでのautograft準備／右冠のtranslocation）**

### 1-5. 刺激伝導系・不整脈
- Bockoven（小児42例）: **周術期心室頻拍 29%**、一過性完全房室ブロック3例（**全例が弁下部の同時手技＝Konno等を併施**）、永久ペースメーカー0
- 成人単独Rossではペースメーカー植込みは稀（Sievers 501例で5例、Tagliafierro 673例で1.2%、Sievers 630例では記載なし）
- 膜性中隔基部は温存する（脚ブロック回避）
- **外部リング留置時の具体的回避法**: 膜性中隔部の糸だけ他より1-2mm高く置く（Basmadjian）／右-無冠交連の6本目だけ**大動脈の外側から**かける（Côté）／Homburg式ePTFEでは膜性中隔領域では**縫合糸を大動脈の外に出したまま通す**（Matsushima）

### 1-6. 採取床からの出血
Liebrichのtip: **冠静脈洞からの逆行性灌流で小血管を可視化**してから低出力電気メスで止血。この段階なら容易だが、手術終盤には到達困難になる。
**Schneiderはさらに強い言い方をする**: 「心拍動下でRVOTの止血を丁寧に行う。**必要なだけ時間をかけることが重要である。homograft近位吻合の後に残った出血への対処は極めて困難で、縫合線を作り直さねばならないこともある**」。Skillington・Said・Conciも同旨。

---

## 第2章　術式① Subcoronary（原法）— なぜ生き残っているのか

### 2-1. 手技の核心（Misfeld/Sievers, Leipzig-Lübeck）
- 大動脈をhockey-stick様に非冠尖中央まで斜切開
- **弁輪径26-28mm → 左-無冠trigoneを心膜補強3-0モノフィラメントで狭める（3-4mm縮小）。>32mm（別記載では>31mm）ならRossを行わない**
- 近位縫合は**単結節4-0 polyfiberで「U字1針＋単結節3針」の反復パターン**。左-無冠trigoneから時計回り、次いで同じ点から反時計回りに右-無冠trigoneへ
- **最大の肺動脈洞を（最大であることが多い）無冠洞に置く**（特にSievers type I L/R BAV）
- 平面的な近位縫合線を目指す。針はcusp attachment lineの極近傍を通す
- **心膜ストリップを近位縫合線に織り込む**（止血＋弁輪狭小化＋補強。結紮時にストリップを軽く引くことで縮小できる）
- autograftの交連はnative交連より**十分高く**留置（ただし幾何学的歪みを作らない）
- 左右洞は切除しsubcoronaryで縫着（5-0）、**無冠洞のみautograft側を温存**し、native無冠洞を直接閉鎖 or 部分切除 or 心膜パッチで**autograft無冠洞のサイズに合わせる**。5-0 U字縫合で両無冠洞を固定
- 洞の縫合は5-0連続、さらに**5-0 U字縫合で交連を患者の大動脈壁に固定**（Sievers 2018）
- **type 0 BAV への対応（Sievers 2018）**: 180°に位置する冠動脈口の**間に、通常は大動脈基部の左外側に、autograftのための新しい交連を作る**。他の交連は基部の右側と冠動脈口に固定し、autograftの幾何学を可能な限り保つ ← **Melbourneがtype 0を禁忌としているのと対照的**

### 2-2. 成績
| | Sievers 2010（501例、平均5.9年） | Sievers 2018（630例、中央値12.5年・最長22.3年） |
|---|---|---|
| 病院死亡 | 0.4% | **0.3%** |
| 生存 | 一般集団と同等 | 20年 **73.1%**（年齢性別マッチ一般集団と有意差なし） |
| 再手術回避 | autograft＋homograft 10年 91.9% | 20年 **85.9%（0.6%/患者年）**、autograft **89.8%**、homograft **91.0%** |
| ペースメーカー | 5例 | — |

**Sievers 2018 の Valve Performance Classification（VPC）**: 20年時点で class I 5% / II 74% / III 19% / IV 1% → **79%が良好なclass I-II**。血行動態・症状・管理方針を統合した分類で、術式間比較の共通言語として提案されている。

### 2-3. ⚠️ subcoronaryだけリスク因子のプロファイルが違う
**Sievers 2018 の最も重要な所見**:
> **術前弁輪径、術前AR、弁輪補強、STJ補強、二尖弁の型のいずれも再手術の有意なリスク因子ではなかった。二尖弁と三尖弁で再手術までの時間に差はなかった。**

これは full root 文献（術前ARと弁輪拡大が支配的なリスク因子）と**真正面から食い違う**。著者らの解釈は「**subcoronary法ではnative大動脈基部そのものが自然な動的外部補強として働き、基部拡大を防ぎautograft機能を保つ**」というもの。

→ **本レビューではこれを「補強＝人工物 vs 補強＝native基部温存」という対立軸の一方の極として扱う**。

### 2-4. subcoronary vs root replacement — 直接比較の解釈に注意
Berdajs 2014のsystematic review（24研究）:

| | 10年生存 | 10年 再手術回避 |
|---|---|---|
| **成人** | SC 94% vs **RR 95.3%** | **SC 98%** vs RR 91.2% |
| 混合集団 | SC 87.3% vs **RR 89.1%** | SC 83.3% vs **RR 93.3%** |
| 小児 | SC 90% vs **RR 92.7%** | **SC 93.3%** vs RR 92.0% |

著者らの結論は「**結果はsubcoronaryのroot replacementに対する優位性を支持しない**」だが、**成人だけを見ると再手術回避はsubcoronaryが98% vs 91.2%と逆転している**。混合集団のプールが小児例に引きずられている可能性があり、**「集団を分けると結論が反転する」ことを本レビューで明示する**。

### 2-5. subcoronaryの位置づけ
- Misfeld の明言: 「**すべてのAS・混合病変でsubcoronaryを選ぶ。autograftがnative大動脈基部に守られるから**」
- **David の評価**: 「両基部の幾何が似ていればsubcoronaryが最良のアプローチ。**しかし私の経験では、それは例外であって原則ではない**」
- **Scorsese（麻酔科視点の総説）の評価**: subcoronaryは技術的複雑さとautograft本来の形状を歪めるリスクから使用頻度が低く、**大動脈基部の非対称（Sievers type 0、二尖弁、一尖弁、基部瘤）では適用が制限される**
- **除外基準（Lübeck）**: 弁輪>31-32mm、洞が2つしかない"true" BAV。加えてLVEF高度低下、多枝冠動脈疾患、結合組織疾患・活動性リウマチ、基部の高度変形、肺動脈弁異常、コントロール不能の高血圧

> `[FIG-2.1]` subcoronary留置の全工程。**出典: Sievers HH, J Thorac Cardiovasc Surg 2010;140:816-22 の online E-Appendix（Figure E1-E9の9図＋動画）** — 9図構成でsubcoronaryの全工程が図解されている唯一の資料。**未入手（supplement）。取得優先度 高**
> `[VIDEO-2.1]` Sievers HH, JTCVS 2018;156:79-86, Video 1（subcoronary Ross procedure）
> `[VIDEO-2.2]` Misfeld M, Ann Cardiothorac Surg 2021;10(4):538-540（annalscts.com）

### 2-6. subcoronary特有の術後管理
Lübeck: **クロピドグレル 75 mg/日を3ヶ月＋イブプロフェン 400 mg/日を5週間＋生涯の血圧管理**。
→ 他施設の「NSAID 3-6ヶ月」「アスピリン3ヶ月」と異なる。**抗血小板薬・抗炎症薬の期間は施設ごとにばらばらで、根拠は乏しい**ことを明示する。

---

## 第3章　術式② Free-standing full root ＋ 補強（RR+R）

### 3-1. Mount Sinai式 tailored total root（Williams & El-Hamamsy）
1. 大動脈をSTJの5mm遠位で切開
2. **無冠洞と左-右交連のnative組織は温存**（後で外部支持に使う）→ **露出のために無冠洞を切り開かない**
3. autograftはtop-down採取、右PA起始の3-5mm近位から
4. 漏斗部筋を2-3mm残してトリム
5. **結節4-0 prolene**で**弁輪下（subannular）に深く**留置。針は大動脈弁輪の1mm上から入れ2-3mm下に出す。autograft側は肺動脈弁尖のhinge pointから上向きに通し、薄い漏斗部筋を除外する
6. **neo-commissureを大動脈弁輪レベルで120°対称に**
7. 冠動脈ボタンは各洞の中央、STJより下に
8. 大動脈吻合を完成させる前に**≥28mmの大型肺動脈homograft**を植込む（遠位5-0、近位4-0で心室中隔は部分層で刺して中隔枝を避ける）
9. **交連上のPA余剰を切除、交連の2-3mm上まで**
10. **上行大動脈≥38mm または autograft STJ-上行大動脈mismatch → 26 or 28mm Dacron interposition graft**
11. **CPB離脱・プロタミン後**に、温存した無冠洞と左-右交連のnative組織をinterposition graftにtackし、**非拘束的な外部支持**とする

**成績**: 2010年以降>500例、手術死亡2例（0.4%）で**両方とも最初の100例内**。退院時平均圧較差4mmHg。10年まで基部径・弁機能安定。

> `[FIG-3.1]` 上記10-11のstep。出典: **Williams EE & El-Hamamsy I, Ann Cardiothorac Surg 2021;10(4):546-548**（PMC OA、動画あり）

### 3-2. Mount Sinai式のもう一つの系譜（Stelzer, 702例・1987-2019）
同じ施設でも Stelzer の補強の考え方は異なり、**フェルトを使う**:
- 当初から**測ったフェルトストリップでneo-aortic弁輪を拘束**
- 中期以降**2本目のフェルトストリップをSTJ安定化に追加**
- 洞部は可能な限り残存native大動脈壁で支持
- homograftは**10%オーバーサイズ**。2008年以降 >99%が脱細胞化
- **上行大動脈は>5cmで置換、それ未満の拡大はaortoplastyで縮小。目標は<3.5cm**
- 全縫合線が連続縫合。心膜上部を大血管の上で可能な限り閉鎖
- 抗線溶薬ルーチン、**acute normovolemic hemodilution**をルーチン化
- **SBP<110 mmHgを、特に最初の24-48時間、厳格に**

**成績（702例）**: 手術死亡 **7例（1%）**、合併症 6.6%。
- **simple群**（既往開胸なし＋軽微な同時手技のみ、419例, 59.7%）: 死亡 0.7%、合併症 4.8%
- **complex群**（既往開胸あり and/or 上行置換・僧帽弁形成等、283例, 40.3%）: 死亡 1.4%、合併症 9.2%
- **時系列で simple症例は減り、complex比率は34%→48%に増えたが、死亡率は下がった**

→ **「適応拡大と成績向上は両立しうる」ことを示す最良のデータ**。

### 3-3. Stuttgart式 reinforced FRT（Liebrich, 832例・25年）
- 漏斗部筋3-4mm残し、Hegarでサイズ計測
- 3本のprolineを大動脈弁輪の各nadirとautograftの対応nadirに置いて固定 → 近位吻合は**nadir間の連続縫合**
- **FRT+AR群では近位縫合線にDacronストリップを織り込み、さらに大動脈壁remnantからautograftへ2本目の縫合線を作って弁輪を安定化**
- CPB 172分、遮断137分。30日死亡0.96%。補強あり73%／なし27%

**明示された4つのpitfall（Liebrich, そのまま引用価値あり）**
1. 左主幹・第1中隔枝の損傷 → #15刀で後方RVOT心内膜を弁輪の5-8mm下に切開
2. **近位「補強」縫合線、特に弁輪安定化のための2本目の縫合線での深すぎる刺入によるautograft弁尖損傷**
3. RV-PA connectionのkinking（autograftに対して導管を長く残しすぎると、心臓が血液で満たされた時に遠位吻合部が折れる）

**明示された3つのcaution**
1. autograft拡大の回避＝近位吻合の補強＋autograftを短く保つ＋遠位（neo-STJ）安定化のための上行大動脈のDacron置換
2. autograft逆流の回避＝malalignment/distortionなしの縫着、解剖学的にやむを得ない場合は冠尖のcommissural plicationによる2-3mmの「軽度oversizing」
3. autograft床からの出血＝冠静脈洞逆行性灌流で出血点を可視化してから低出力電気メス

> ⚠️ **数値の齟齬（要確認）**: Liebrich論文のAbstractは「20年生存率92%」、Results本文は「5年97%／15年92%／20年86%」。**Results本文の値を採用し、齟齬を注記する**。

### 3-4. Aswan式 loose jacket（Afifi & Yacoub）
- 上行大動脈を中央（交連の約2cm上）で完全離断 → 近位大動脈を**無冠洞のnadir直上まで縦切開**
- 採取: 筋カフ2-4mm、遠位は交連の2-3mm上
- 縫着: **すべての針を（大動脈側で）弁輪の直下に、（肺動脈側で）肺動脈弁輪を含めて通し、肺動脈基部を大動脈弁輪の中に「埋める」**
- 冠動脈ボタンは**大動脈壁に残した孔を通してautograft洞に到達**。**十字切開で孔を広げてkinkを防ぐ**
- 「loose jacket」: **涙滴型の新鮮心膜**で無冠洞切開を閉鎖・やや拡大 → autograft周囲にnative大動脈壁の筒。**ジャケット上端を頭側に持ち上げて遠位大動脈吻合部を覆い、4-5本の結節縫合で固定**（＝autograft上方のnative大動脈の遅発性拡大を防ぐ必須手順）

> `[FIG-3.2]` **ガイドライン側に EACTS Consensus Figure 3 として既に切り出し済み** → 再利用
> `[VIDEO-3.1]` Afifi A, Ann Cardiothorac Surg 2021;10(4):544-545

### 3-5. Homburg式 suture annuloplasty＋simplified root wrapping（Matsushima & Schäfers）
- **弁輪径>25mm で外部suture annuloplastyを発動**
- autograftを左室内に反転させて弁輪内（intra-annular）に連続4-0で縫着 → 引き戻して縫合線を目視確認・追加縫合
- **ePTFE（Gore-Tex CV-0）**: 一方の針は右-左尖間交連の外側の中隔筋から入れ、基部弁輪の後方周をまわってautomitral continuityへ。他方の針は右尖nadir外側の右室心筋を前方に通し、**膜性中隔の領域では大動脈の外側に出したまま**、無冠尖nadir外側の大動脈外膜を接線方向に通す
- **BSAでHegarを選んで結紮（BSA<1.8 m²→21mm、≥1.8 m²→23mm）**
- 上行大動脈>30mmならDacron置換（BSA<1.8→24mm、≥1.8→26mm）
- **simplified root wrapping**: autograft遠位吻合に**大動脈基部組織のtongue（交連部）を巻き込む** → 10-15mm幅のnative基部壁がautograftの3交連の外側に残る
- 15例、再手術・拡大・AIなし

> `[FIG-3.3]` **出典: Matsushima S, Ann Thorac Surg 2019;107:e361-3, Fig 1（反転縫着）・Fig 2（ePTFE外部suture annuloplasty）・Fig 3（3本のtongueによるwrapping）**

### 3-6. Nam & Bloom（MGH）式 — 「測って印をつける」full root
- autograftを反転させてHegar/graduated cone上に載せ、**3尖の交連とnadirを全てマーキングして対称性をconeで評価**
- autograftを戻して長さを測る（通常約4cm）＝**そのまま planned homograft length になる**
- **coneでLVOT内に60°間隔の基準マーキング**を作る
- annuloplastyを要する場合は、**60°マーキング全点に6本のpledgeted糸**を置き、**目標弁輪径より5-6mm大きいDacron graftのsewing ringに通して、実測autograft径のHegar上で結紮**
- 右尖nadirから開始し、autograft側は外→内、LVOT側は内→外で深く。右/左交連へ向かい、次に左洞、autograftを術者の反対側に移して右洞の残り、最後に無冠洞
- **原則: crown状の外科的弁輪ではなく、basal ring レベルの平面的な留置**

> `[FIG-3.4]` **出典: Nam L & Bloom JP, JTCVS Tech 2026;36:102256, Central Illustration（60°マーキングを施した反転autograft）** — 「柔らかいautograftをどう幾何学的に扱うか」の到達点
> `[VIDEO-3.2]` 同論文 Video 1

### 3-7. Florida sleeve Ross（Spindel, Ochsner）— 「簡便な補強」
- 3洞すべてを切除し弁輪上5mmの大動脈壁を残す
- **同一水平面に6本のpledgeted subannular縫合**（各nadir下と各交連下に1本ずつ）
- **bulged root graftのサイズ = Mosaic valve sizerで測ったautograft弁輪径 ＋3mm（PA壁厚分）**
- graftを1/6ずつマーキングし**縦に二分**
- autograft近位吻合を先に完成 → **6本中5本をgraftに通してparachute・結紮**
- 冠動脈用のスリットを作りボタン再建 → 上行大動脈置換
- **遮断解除後、無冠尖nadirの6本目をTEEガイド下に結紮**（＝これがannuloplastyのきつさを決める）
- 二分したgraftを緩く結節縫合で寄せ、遠位を上行graftにtack。**この緩さが早期の拍動ごとの血行動態変化へのcompliancyになる**

> `[FIG-3.5]` **出典: Spindel SM, JTCVS Tech 2024;25:24-7, Figure 1（A-Hのstepwiseシェーマ）＋Figure 2（同じA-Hの術中写真）** — シェーマと術中写真が1対1対応する稀な図。**教育的価値が最も高い**
> `[VIDEO-3.3]` 同論文 Video 1

### 3-8. Ross-PEARS（Vienna / London）
**手技（Conci, MMCTS 2023 / Redondo, JTCVS Tech 2024）**
- 術前CTから患者個別の3Dプリント鋳型で**メッシュ製の外部支持prosthesis**を作製。**サイズは肺動脈径の115%**（Vienna）。製作に約3週間
- prosthesisの**近位hemを3本の等間隔prolene糸でマーク**（＝3つの弁交連に対応）、軸方向の縫い目を開く
- **autograftをinvagination techniqueで大動脈弁輪に縫着。連続4-0で、autograftとPEARS graftのhemを同時に取り込む** → これで弁輪が完全に補強される
- 冠動脈ボタンはPEARS graftの後方と前方左寄りの洞に開けた2つの窓を通して再建
- **上行大動脈とautograftの径差が大きい場合はreduction aortoplasty**（Redondoの50例中 **44%** が必要だった）
- CPB離脱・止血後に**PEARSを大動脈の周りに巻いて、非冠動脈側で縦の軸縫い目を結節Ti-Cron糸で閉じる**。**autograftと上行大動脈の全長を覆うことが望ましく、reduction aortoplasty後は特にそう**
- Viennaでは**腕頭動脈まで**包む

**他の補強との差別化（3点）**: ①患者個別で幾何学を保つ ②基部だけでなく上行大動脈全体を安定化 ③**しなやかなメッシュでautograftを隔離しないため滲出を許容する**

**成績（Redondo, London 50例, 2015-）**: 平均29.8歳（最年少9歳、14%が18歳以下）、**38%が既往開胸（11例は既往AVR）**、72%が二尖弁、平均上行径3.83cm。CPB 200.7分／遮断151.1分、在院中央値6日、平均FU 16.9ヶ月。**死亡ゼロ**、2例が後にAVR（1例はリウマチ性、1例はautograft弁尖の医原性損傷）。上行大動脈径は術直後から安定。

> `[VIDEO-3.4]` Conci L, MMCTS 2023 → https://mmcts.org/tutorial/1844 （10ステップ、13分半）
> `[FIG-3.6]` Ross-PEARS完成写真。出典: **Redondo A & Austin C, JTCVS Tech 2024;24:121-7, Central Illustration**（PMC / **CC BY**）

---

## 第4章　術式③ Inclusion（autologous＝Skillington法 / prosthetic＝Dacron）

### 4-1. Autologous inclusion（Melbourne, 516例・25年）— 「root-within-root」

**設計思想**: autograftの実測径に大動脈基部を合わせるのではなく、**患者の体格から決めた目標径に大動脈基部を作り替え、その中にroot replacementを行う**。

- CPB前に**左前肺動脈洞をナイロン糸でマーク**（後で右冠洞に向ける）
- STJの5-6mm上で横切開・離断
- **無冠洞に縦切開**を横切開から弁輪の4mm手前まで下ろす（弁輪の最大露出）
- **目標径: 男性 24-26mm、女性 22-24mm（身長等で微調整）**
  - 縮小1-3mm → plicationのみ＋外部ポリエステルバンド補強
  - 縮小4-8mm → **無冠洞組織を弁輪レベルで最大幅10mm切除し、左冠動脈口をボタンとして外し、外側から弁輪レベルまで剥離して、左洞・無冠洞が張る範囲に60%周のポリエステルバンド（partial ring）**
- **autograft洞に孔（fenestration）を開けておき、冠動脈ボタンを大動脈基部の内側に引き込んでautograft洞に吻合（6-0）**。左冠は左右両側で大動脈洞組織をやや多めに切除してkinkを避ける
- 無冠洞の縦切開を5-0で閉鎖 → **autograftが大動脈基部に完全に内包される**
- autograftの高さを患者の大動脈基部と同じに調整
- 遠位吻合4-0。**左冠吻合部より頭側では遠位大動脈基部も縫合線に含める（円周の15%＝1cm以上）**
- 遮断解除後、**下方の大動脈remnantを前方でfigure-of-eightナイロン糸により遠位autograft吻合線に吊り上げ**、ずり落ちて右冠動脈を塞ぐのを防ぐ
- **autograftをできる限り頻繁に血液に浸す**（採取後の待機中は右心膜腔で、植込み中は左室ベントを時々止めて）— 弁尖の生存性・細胞完全性の維持のため

**適用限界**
- **STJが32-34mmを超えると幾何学的mismatchが大きすぎて本法は不可**。弁輪は38mmまで修復可能（STJ ≤32mmが条件）
- **type 0（前後交連）BAV・一尖弁には不向き**
- 大動脈-肺動脈弁輪径比 >1.5 は拡大・失敗のリスク
- Caldaroniの相対禁忌表: 肺動脈弁異常／**STJまたは弁輪 >34mm**／type 0 BAV／Marfan等結合組織疾患／急性破壊性心内膜炎／SLE／リウマチ性／複数の同時手技／大動脈からの冠動脈起始異常／高度末梢血管疾患／**65歳超**／高度左室肥大／BMI>45／腎不全

**成績**
- Skillington 2015（322例）: 弁輪縮小62.4%、洞/STJ縮小49.4%、拡大7.1%、**何も操作しないのは21%のみ**。最大基部径 5/10/15年で 34.0/34.6/34.7mm。**基部拡大による再手術ゼロ**、再手術回避率96%（15年・18年）
- Caldaroni 2025（516例・25年）: 25年生存85.3%、**autograft再手術回避 89.5%（AS 95.0% / mixed 94.3% / AR 78.0%, p=.01）**、homograft再手術回避92.7%、総再手術8.3%、早期死亡0.2%。大動脈洞径 31.6→35.6mm（25年）、25年時の平均圧較差5.0mmHg、全生存者NYHA I

**Caldaroniが挙げるpitfall**
- autograftは**交連の2-3mm上**で切る／大動脈の切開は**STJの5mm上**
- 交連対称性の維持、LVOT内への留置、**3つのneo-commissureへの結節prolene糸の均等配置**。**単結節縫合こそが正確で均一な留置を可能にする**
- 弁輪縮小はBMIと性別に応じて、多くは最も拡大した非対称な洞（Sievers type I BAVなら無冠洞）のpartial annuloplastyで
- **上行大動脈は38-40mmを超えたら先手を打ってtailoring**し、基部弁輪と1:1比を目指す
- 冠動脈は**native基部に2つのporthole**を作り、autograftに直接吻合

> `[FIG-4.1]` **出典: Skillington PD, J Thorac Cardiovasc Surg 2015;149:S46-52, Figure 1（BAV＋拡大基部：無冠洞の四角形切除→弁輪plication）／Figure 2（A:内側からの直接縫合閉鎖、B:内→外の水平マットレス糸を4mm幅ポリエステルバンドに通す、C:外部リングによる完成形）／Figure 3（弁輪・STJ実測値に応じた3通りの基部切除パターン）** — **この3図で「大動脈基部をどう作り替えるか」が完結する。最優先で取得**
> `[FIG-4.2]` inclusion cylinderの完成模式図。出典: Caldaroni F, JTCVS 2025;170:1017-24 の Central Illustration
> `[VIDEO-4.1]` Skillington PD, Ann Cardiothorac Surg 2021;10(4):541-543（annalscts.com）

### 4-2. Prosthetic inclusion — 4つの流派

#### ① Brussels式（de Kerchove/Jahanyar）— Cardioroot、交連高でサイズ決定
- **Cardioroot（Getinge）を選好**（Valsalva graftより硬く、円錐状の流入部で調整しやすい）
- **サイズは肺動脈弁交連の高さ（基部リング→交連先端）で決める。通常28mm、稀に30mm**
- Valsalva部より下のskirtを除去、管状部を遠位大動脈吻合の高さに合わせて切る
- autograftをgraft内に入れ、**3本の交連縫合をValsalva部遠位端に仮置き** → 近位autograftを4-0連続で固定
- Dacron包埋したautograftを**3本の連続4-0で交連間ごとに大動脈弁輪へparachute**
- **交連は常にまずneo-STJレベルに置き、遠位の交連付着位置を後から調整して最適な弁形態を得る**
- **El Khoury "tongue" technique**: graftを電気メスで切開し、同じ高さでautograftを新冠動脈開口部の上縁で切開して、**PA組織の下側のtongueをDacronの開口部から引き出す**。→ 露出が良くなり吻合下面が滑らかになる。**むき出しのDacronは左冠尖を傷つけるため重要**
- **形態評価を3段階で行う**（back tableでgraftに縫着した時／弁輪に縫着した後／冠動脈再建後）。前2段階なら交連を調整可能
- 102例（2005-2020）、院内死亡ゼロ、早期再手術1例、5年以内3例（全例neo-AV修復）
- **明言**: 「**この手技にはラーニングカーブがある。Dacron-autograft inclusionはneo-AVの幾何学を歪め弁尖prolapseを起こしうる。大動脈を再遮断してprolapseを修復する必要が生じうる**」

#### ② USC式（Starnes）— straight PET、+2mm、小弁輪では包まない
- 2001年に導入。**straight vascular conduit（PET）、autograft径 +2mm**
- **弁尖のすぐ下でautograftをgraft内に固定** → 遠位autograftをgraftに固定 → wrapped autograftをLVOTに連続縫合 → 冠動脈ボタン再建 → 近位吻合
- **成人二尖弁にRossを断ったことは一度もない**（大動脈弁形態・病態・上行瘤の有無を問わない）。除外は肺動脈弁異常と複雑な結合組織疾患のみ
- **⚠️ 例外: 小さい（19-21mm）大動脈弁輪の場合はwrapしない**
- **成績（成人BAV 129例、中央値10.3年）**: autograft失敗 wrapped 3例（5.2%）vs unwrapped 25例（35.2%）。**10年再介入累積発生率 4.0% vs 26.8%（SHR 0.28, P=.035）**。10年生存 100% vs 95.6%（P=.15）

#### ③ Leiden式（Schneider & Hazekamp）— Valsalva graft、+2mm、「scalloped」
- autograft近位径を計測（例 26mm）→ **2mm大きい（28mm）Valsalva graft**。近位を1リング残してトリム
- 交連の下で3本の5-0でautograftをgraftに近位固定 → その3本で連続縫合
- **遠位は交連の高さと正確な位置を慎重に評価し、各交連を別々の5-0でgraftに固定。ここは非常に慎重に。歪みは後のautograft閉鎖不全を招く**
- **3つのValsalva洞をすべて切除（"scalloped"）** → 遠位縫合線を3本の別々の5-0連続で。**各縫合は2交連の間の最深点から開始**（misalignmentと歪みを避けるため）
- **再植込み後にwater testで配置を確認**
- LVOT側は3本の4-0を冠動脈再建がしやすい位置に置き、連続縫合。**針が弁組織に届かないよう注意**
- 電気メスでgraftに孔を開けて左冠を再建 → 遠位吻合 → **右冠は最後（元より高い位置に来るため）**
- **明言**: 「**この再植込み法は全例に可能ではない。graft径が身体成長を妨げてはならないので、autograft wrappingと再植込みは（ほぼ）成長の完了した患者にのみ適用できる**」

#### ④ Wroclaw式（Jasinski）— cylinder-within-a-cylinder（冠動脈を剥離しない）
- **弁輪内に18本の単結節・非pledgeted 2-0 Ethibondを心室大動脈接合部の水平面に**。無-左交連の線維性subcommissural triangleの底部から開始 → 左洞を時計回り → 左右交連間で深く → **右洞は心室中隔で水平面を保つため上部心室大動脈接合部の5mm下に** → 無-右交連。**糸を引き離して膜性中隔を同定してから刺入**。無冠洞は基部の非対称と軽度の傾きを補正するためやや高く
- 冠動脈洞をトリムしてmini-rootを作り、垂直牽引下に引き下ろして結紮
- **cylinder-within-a-cylinder が形成される**
- 第2の流出路縫合線を5-0連続で内側から一貫して操作
- **利点として明示: 「冠動脈を剥離する必要がなく、早期リスクが有意に減る」**

> `[FIG-4.3]` **ガイドライン側に EACTS Consensus Figure 8/9/10 として既に切り出し済み** → 再利用
> `[VIDEO-4.2]` Jahanyar J, ACS 2021;10(4):549-551, Video 1（cusp plication）・Video 2（小児の成長）
> `[VIDEO-4.3]` Starnes VA, JTCVS 2023;165:43-52, Video 1
> `[VIDEO-4.4]` Schneider A, MMCTS 2017 → https://mmcts.org/tutorial/828（図6点付き）
> `[VIDEO-4.5]` Jasinski M, MMCTS 2022 → https://mmcts.org/tutorial/1773

### 4-3. inclusionの「幾何学を測る」バリエーション

**Eversion for stabilization（El Arid, Tours）**
- autograftを**「en doigt de gant」＝手袋の指のように完全に反転**させ、Hegar dilator上で安定化
- **反転して内腔から見るとSTJが「わずかに隆起した肥厚したautograft壁のridge」として明瞭に同定でき**、マーカーで描ける。virtual basal ringも描く
- **clipレベルでのSTJ↔basal ring距離＝選ぶValsalva graftの直径**
- 近位縫合線は**結節3-0 coated polyester**（連続縫合はneo-aortic逆流と有意に関連しうるため）
- 冠動脈ボタンは5-0で**3層すべて**を含めて
- 15例、CPB 223±17分、遮断181±15分、術後AR全例mild未満

**Root pressurization before implantation（Emani, Boston）— 植込み前に「動く弁」を見る**
- autograft遠位（交連の3-4mm上）に**上行用Dacron graftを5-0連続で延長**
- **心筋保護液ラインに1/4インチチューブと三方活栓を追加し、灌流技師が全血で圧規定灌流**
- **まず40-60mmHgで加圧 → 心室側から弁尖の接合を直視**。中心性のごく軽度逆流は正常。**交連部に逆流ジェットが出たら、減圧した状態でsubcommissural plication糸**
- root補強graft（Valsalva選好）の**サイズ＝術前CTの肺動脈STJ径＋4mm**（PA壁厚1-2mm＋心周期中の基部拡張1-2mm分）
- **root graftを被せた状態で60-80mmHgに再加圧** → autograftがgraft内でどの平面・高さに座るかを調整。必要なら弁輪plication糸
- **最適配置が決まったら、加圧したまま**autograft近位端をroot graftに結節5-0で固定 → 交連位置をマーカーで記入して減圧
- **加圧のメディアは生理食塩水でなく全血**（食塩水では遠位縫合線から漏れる／全血なら出血評価もできる／弁尖内皮への酸素供給）
- 血腫予防のため**root graft遠位端は結節縫合で間隔を空けて固定**
- 4例、術後neo-AR なし/trivial、合併症ゼロ

**Reversed graft interposition（Kawamura, 川崎幸病院）— 柔らかいautograftを「張る」**
- **別テーブルで、autograftのSTJ直上に人工血管をあらかじめ連続吻合**（各洞に3本の別々の糸、5-0モノフィラメント）
- **人工血管の遠位端を内側に折り込む** → **弁輪が拡張されて丸い形状を保ち、視野が広がり、均等な縫合糸配置と正確な交連整列が可能になる。止血の評価もできる**
- 弁輪に22本の単結節縫合。基部リング円周をautograft洞比で正確に三分割してマーキング
- **テスト後に人工血管を引き抜いて、実際の使用位置に置き直す**（遠位吻合に使う。high takeoffの右冠は人工血管に吻合）
- **注意: 引き抜く際に弁尖を傷つけないよう最大限の注意。ただしwoven Dacronは柔軟で順応性が高く、挿入・抜去時の外傷リスクは小さい**
- CPB 253分、遮断208分、術後trivial AR

**2F technique（Farhat, Lyon）— David I＋3F stentlessのハイブリッド**
- PA壁を**3mm残して切除**（Davidと同じ発想）→ **冠動脈ostiaをDacronに直接再建できる**
- **straight Dacronを2mmオーバーサイズ**（bulge内での位置決め問題を避けるため）
- 3本の5/0を3つの弁交連下三角の中央に置き、連続縫合でautograftの筋をDacronに固定
- 各交連をTeflon felt付き4/0 U字縫合でDacronに固定（＝3F stentless弁の植込み法）
- **autograftが短くて上行大動脈全体を置換できない問題**も同時に解決
- 6例、遮断102分

**Beating-heart harvest ＋ anti-commissural plication（Zhu & Woo, Stanford）— 遮断時間短縮＋弁尖にやさしい幾何学**
- **心拍動下・CPB下**で肺動脈弁下の漏斗部を切開、PVから3mmの距離を保ちながら曲線状に切離。**第1中隔枝のすぐ上の層を保つ**
- 26mm straight PET graft内にautograft、subannular縫合線を5-0連続、交連を吊り上げてgraftに固定
- **ACP（anti-commissural plication）を交連レベルで行いneo-STJ径を縮小**。graftを交連間で交連の高さに**約2mmの水平マットレス縫合**でplicate
- **合計30-60分の遮断時間短縮**

**ACPの生体力学的根拠（Zhu, JTCVS 2023 — 3Dプリント左心シミュレータ）**
- ブタautograft 7例＋ヒトautograft 5例（心移植のレシピエント心・不使用ドナー心から採取）＋無補強ブタ5例（対照）
- **inclusion法は対照に比べてautograft逆流が有意に低下（P<.01）**
- **ACPあり vs なしで、弁尖の rapid opening velocity（3.9 vs 5.9 cm/s, P=.03）、rapid closing velocity（1.9 vs 3.1 cm/s, P=.01）、relative rapid opening force（4.6 vs 7.7, P=.03）がいずれも低下** → **弁尖への機械的負荷が減る**
- ex vivo条件では**PET graftはautograft径より6-7mm大きいものを選択**（ACP後の最終径がautograftの交連レベル径とほぼ一致）
- 採取時、**各肺動脈弁尖付着部のnadirより近位に最低2mmの右室組織を残す**

> `[FIG-4.4]` **出典: El Arid JM, Ann Thorac Surg 2022;114:e217-8, Figure 1（A: eversion / B: STJの同定 / C: 解剖学的ランドマークの同定）**
> `[FIG-4.5]` **出典: Dafflisio G, JTCVS Tech 2025;31:108-14, Figure 1-8** — PMC / **CC BY**。図の質・量ともに本章で最良
> `[FIG-4.6]` **出典: Kawamura T, ATS Short Rep 2026;4:642-4, Figure 2（A: back tableで予め吻合した人工血管 / B: 折り込みによる視野拡大）＋Figure 3（模式図）**
> `[FIG-4.7]` **出典: Zhu Y, JTCVS 2023;165:e103-16, Figure 1（A-L: 術中写真4点＋ヒトautograft準備6段階＋シミュレータ搭載2点）** — ACPの手技が写真で追える
> `[VIDEO-4.6]` Dafflisio, JTCVS Tech 2025, Video 1（加圧の実演）／`[VIDEO-4.7]` Zhu, JTCVS 2023, Video 1（ACP付きinclusionの手技）／`[VIDEO-4.8]` Kawamura, ATS Short Rep 2026, Video

---

## 第5章　弁輪形成・STJ・geometric mismatch

### 5-1. まず押さえるべき陰性所見: subcommissural plicationは効かない
Mazine & El-Hamamsyの指摘:
> **ARにおける問題は弁輪の「線維性」部分ではなく「筋性」部分の拡大にあり、subcommissural縫合はそこに届かない。だからAV修復でも無効であったのと同様に、Rossでも遅発性autograft失敗を防げない。**

Davidらが「弁輪拡大は外科的に対処できない、早期autograft変性のマーカーだ」と結論したのは、**対処法がsubcommissural plication＋部分Dacronリングだったから**である可能性がある。

### 5-2. 現在の弁輪安定化の選択肢とサイジング

| 方法 | サイジングのルール | 出典 |
|---|---|---|
| **外部リング（CORONEO Extra-Aortic）** | **リング径 = 肺動脈弁輪径 ＋8mm −2mm**（＋8mm＝術後長期のPA弁輪径との実測差の中央値、−2mm＝弁尖接合を増やすため）。5本のpledgeted mattress糸をLVOT内から外へ。CORONEOは31mmまで、それ以上は管状Dacronからリングを切り出す | Myjavec, EJCTS 2024 |
| **円形Dacronリング（Mount Sinai/Montreal）** | 6本のpledgeted 2-0 Ethibondを基部リングの水平面（**cuspのnadirの約2mm下**）に内→外。**膜性中隔部の糸だけ1-2mm高く**して刺激伝導系を避ける。**肺動脈弁輪径に一致するHegarをLVOTに入れ、5-6mm大きいDacronリングをHegarの周りで結紮**。目標径は性別とBSAから「正常な大動脈弁輪径（20-25mm）」を狙う | Mazine ATS 2018 / Basmadjian JTCVS 2016 |
| **ePTFE suture annuloplasty（Homburg）** | **患者BSAでHegarを選ぶ（BSA<1.8 m²→21mm、≥1.8 m²→23mm）**。autograft実測径によらない | Matsushima, ATS 2019 |
| **部分ポリエステルバンド（Melbourne）** | **目標径を性別と体格で決める（男24-26mm、女22-24mm）** | Skillington, JTCVS 2015 |
| **Florida sleeve式subannular縫合** | bulged root graft径 = autograft弁輪径（Mosaic sizer）＋3mm | Spindel, JTCVS Tech 2024 |
| **double expansible ring（Paris/Halifax）** | Hegar実測から表で決定（**弁輪25-27→リング29mm、28-30→31mm、≥31→33mm**）。**Hegar実測より約2サイズ（2mm）大きくして狭窄を避ける**。STJリングは**25-27 / 27-29 / 29-31mm**（autograftのneo-STJ径による） | Côté, JTCVS Tech 2025 |
| **フェルトストリップ（Stelzer）** | 実測したフェルトストリップでneo-aortic弁輪を拘束、中期以降は2本目をSTJに | Stelzer, JTCVS 2021 |

### 5-3. 外部リングは本当に効いているのか（Basmadjian 2016）
50例（うちRoss 18例、Dacronリング39・ExAoリング11、リング径中央値28mm）:
- **収縮期 27.9→23.6mm、拡張期 24.8→20.3mm（いずれもP<.001）**、**2年まで安定**
- **収縮期弁輪拡張（16%）が術後早期に保たれ、2年後も保存されていた** → 「動きを殺していない」ことの実証
- 懸念だった **Dacronリングの経時的拡大は起こらなかった**（上行大動脈導管としてのDacronは18ヶ月以内に最大20%拡大することが知られている）

**Myjavecが記載する経時変化**: 術直後に劇的に縮小 → 最初の3ヶ月でやや拡大（**近位吻合に取り込んだPA筋rimが萎縮するため**）→ 以後安定。**この生理を知らないと3ヶ月後のエコーで慌てる**。

> `[FIG-5.1]` **出典: Myjavec A, EJCTS 2024;65:ezae118, Figure 2（リングサイジングの模式図）＋Figure 1（PA径の経時変化グラフ）**
> `[FIG-5.2]` **出典: Basmadjian L, JTCVS 2016;151:1280-5, Figure 1（膜性中隔部の糸を1-2mm高く置く図）＋Central Illustration（収縮期・拡張期の弁輪径変化）**
> `[FIG-5.3]` **ガイドライン側に EACTS Consensus Figure 4（extra-aortic ring annuloplasty）が既にある** → 再利用
> `[VIDEO-5.1]` Myjavec, EJCTS 2024, Video 1

### 5-4. STJと上行大動脈
- **autograft側**: 交連上のPA組織を2-3mmまで切除（Mount Sinai / Melbourne / Boston 共通）
- **大動脈側の閾値は施設で30mmから50mmまで開いている**:

| 施設 | 上行大動脈への介入閾値 |
|---|---|
| Homburg（Schäfers） | **>30mm** でDacron置換（BSA<1.8→24mm、≥1.8→26mm） |
| Montreal（Abeln内） | >38-40mm |
| Mount Sinai（El-Hamamsy） | ≥38mm で26-28mm interposition graft |
| Melbourne（Skillington） | >38-40mmでtailoring、置換は男性>45mm・女性>40mm。**術前STJ 26-32mmなら上行の縦切除＋直接閉鎖（tailoring aortoplasty）で人工物を使わない** |
| Mount Sinai（Stelzer） | **>5cmで置換、それ未満はaortoplastyで縮小。目標<3.5cm** |

- **Côtéの提案する第3の道**: 「**拡大していない上行大動脈をSTJ安定化のためだけに置換する代わりに、STJリングを使う**。Dacron管が不要になり、大動脈のコンプライアンスを保ち、遠位吻合をなくし、基部と上行の内皮の連続性＝内皮機能を保てる」。STJリングは5本のpledgeted 2-0を**各交連に1本と各冠動脈の上に1本**。native無冠洞と左-右交連をリングにtackする
- Skillington 2015の失敗例2例は「**上行大動脈を28mmのオーバーサイズのポリエステルgraftで置換した**」ことが原因

### 5-5. 幾何学的mismatchへの古典的対応
Klena（J Heart Valve Dis 2000）の "annuloplasty and aortoplasty" が最初期の体系的記載。**現在の全ての弁輪形成・STJ調整の原型**として位置づける（抄録のみ入手）。

---

## 第6章　RVOT再建 — 「アキレス腱」

### 6-1. 凍結保存肺動脈homograftがなぜgold standardか
Skillingtonの整理:
- **肺動脈中膜は大動脈homograftより組織あたりカルシウム量が有意に少なく、弾性組織も少ない** → 長期の石灰化回避に有利
- 筋skirtがあるため**autograft採取後の空間に解剖学的に完璧にフィットし、採取床の止血にも寄与する**
- Melbourneの方針: 「**適切な肺動脈allograftが得られないならRossを提供しない**」
- 米国では2022年のRoss用肺動脈導管の**83%超がhomograft**（Scorsese）

### 6-2. 手技の細部（Skillington）
- **筋skirtを3-4mm幅にトリム**（筋を少なくすると免疫反応が減り、導管圧較差が下がると推定）
  - ※ Réa（Curitiba）は**0.5-1cmのrim**を残す。Saidは記載なし → **トリム量にコンセンサスはない**
- 遠位吻合: 5-0連続、**orthotopicに植える**
- 近位吻合: 4-0連続、**allograftの後尖に隣接するscallopのnadirをRVの後方吻合縁の中央に合わせる**。完成前に右心系をdeair
- **導管の捻れ（twisting/torsion）は何としても避ける**
- タイミング: **遮断下**に、autograft近位吻合の後・冠動脈再建と遠位吻合の前
  - ※ Schneiderは**近位吻合を遮断解除後の心拍動下**に行い、心膜ストリップで補強（後方は筋組織が脆弱なので特に重要）
- 抗菌薬: allograft筋・保存液・洗浄液を細菌培養に提出、**培養陰性確認まで or 48時間**。**筋の培養陽性なら4週間の静注**。洗浄液の陽性は汚染とみなす

### 6-3. 脱細胞化homograft — 2つの大規模データ

**Curitiba（Réa 2025, 414例, 単一術者 1995-2024）** — 最長のフォロー
- 脱細胞化 253例（中央値9.1年）vs 凍結保存 161例（中央値**20.4年**）
- プロトコル: **新鮮homograftを滅菌直後に0.1% SDS溶液で37℃・24時間振盪、PBS中4℃で最大90日保存**（ブラジル特許 PI0800603-2）
- **15年時点の機能不全の累積発生率は同等（12.4% vs 11.2%）**
- **しかし** 経時的な最大圧較差は脱細胞化群で低い（β=−2.99, P<.001）
- **15年時点の再手術の累積発生率は 1.2%（脱細胞化）vs 6.8%（凍結保存）**
- 凍結保存群では**年齢とhomograftサイズ**が狭窄のリスク因子だが、脱細胞化群では**年齢のみ**
- **さらに: 脱細胞化ヒト心膜による近位「conical extension」（39例）で late peak gradient がさらに低下**（直接吻合比 β=−6.37、anterior hood比 β=−7.44）

**Canadian Ross Registry（Chauvette 2022, 466例, 6施設）** — 早期の risk profile
- 全例に脱細胞化凍結保存homograft（SynerGraft, CryoLife）、中央値2.2年（最長8.5年）、99%完遂
- **6年での機能不全累積発生率 11±2%**、そのうち**狭窄が93%**（形態学的には**導管に沿った狭窄が59%**）
- **6年での再介入累積発生率 3±1%**
- **瞬間リスクは術後1年目が最大（3.5%/年）で、以後<1%/年に低下**
- **年齢<45歳が唯一の独立リスク因子（HR 3.1, 95%CI 1.1-8.6, P=.03）**
- homograftは（入手可能な範囲で）**系統的にオーバーサイズ**

**⚠️ 立場の対立**: Skillingtonは「中期成績を比較しても脱細胞化に明確な優位性はなく、コスト・入手性の問題もあるため従来の凍結保存を継続する」と明言。一方 El-Hamamsy / Stelzer（2008年以降>99%）/ Réa は脱細胞化を標準としている。**Réaのデータ（15年再手術 1.2% vs 6.8%）が現時点で最も強い反論材料**。

### 6-4. homograftが手に入らない世界への解（Said, MMCTS 2025）
4つの選択肢を同一tutorialで提示:
1. 標準的肺動脈homograft
2. **hand-made valved conduit**（Dacron graft内に標準的大動脈生体弁を4-0連続で固定。**生体弁のsewing ringを吻合線に含める必要はない**。近位端をbevelしてRVへ）
3. **Freestyle xenograft**（やや短いので短いDacronで橋渡し。**相対的に硬いので心停止中に近位吻合ができる**）
4. **pulmonary Ozaki**（前胸壁心膜シートを0.6%グルタルアルデヒド10分処理→生食で6分×3回洗浄。Ozaki AV sizerでneo-PV弁尖のサイズ決定、症例では3尖とも29mm。RVOT Dacron graft内側にneo-commissureをマークして4/0連続で縫着）

同tutorialの**tips**:
- 補強Dacronは**autograft近位径＋4mm**
- **近位端を固定した後にDacron graftを反転させると、遠位端を固定でき、加圧下で弁機能を確認でき、上行置換を伴う場合に遠位縫合線を1本節約できる**
- 冠動脈ボタンは**3層すべて**を含めて5/0連続
- **右冠動脈ボタンは遠位大動脈吻合の後壁縫合線を完成させてから**（基部の回旋を防ぐ）

> `[VIDEO-6.1]` Said SM, MMCTS 2025 → https://mmcts.org/tutorial/2005 （4手技を1本で対比、14分）
> `[FIG-6.1]` 完成したRVOT再建。**出典: Skillington P, JTCVS Tech 2021;10:403-7, Figure 1（artist's impression）＋Figure 2（二尖肺動脈弁の術中写真）**
> `[FIG-6.2]` 脱細胞化 vs 凍結保存の再手術累積発生率曲線＋conical extensionの模式図。**出典: Réa ABBADC, JTCVS Open 2025;25:25-38**（PMC / CC BY-NC-ND）
> `[VIDEO-6.2]` Skillington, JTCVS Tech 2021, Video 3（allograft作製と吻合）／`[VIDEO-6.3]` Chauvette, JTCVS 2022, Video 1（homograft植込みの標準化手技）

### 6-5. 再介入の閾値と方法
| | Melbourne（Skillington） | Curitiba（Réa） |
|---|---|---|
| 機能不全の定義 | — | 最大圧較差 ≥40mmHg または 中等度以上のPR |
| 再介入の適応 | 平均収縮期圧較差 **≥36 mmHg**、または重症PR＋（症状 / RV機能低下 / RVEDVI >140 mL/m² / MRIでRV:LV容積比 >1.8） | 症状・**最大圧較差 ≥50mmHg**・重症PR・RVサイズと機能・活動性心内膜炎の組合せで個別化 |

- **経皮的（バルーン・TPVI・遠位吻合部狭窄へのステント）が第一選択**
- **外科的再介入を選ぶのは**: 導管の収縮、**左主幹-allograft間距離 <3mm**、高度石灰化、心内膜炎
- 再手術では**stentless porcine root**を選好（心内膜炎を除く）。初回手術で心膜を閉じるか人工膜で覆っておくと再開胸が速い

---

## 第7章　特殊状況

### 7-1. 二尖・四尖肺動脈弁 — 最大の実務的対立
| | Montreal（Filippa/Demers） | Melbourne（Skillington） | Stony Brook（Scorsese, 総説） |
|---|---|---|---|
| 方針 | **個別判断で使用可** | **使用しない** | 「autograftとしての使用を妨げうる」 |
| 頻度 | 640例中11例（1.7%）、二尖8・四尖3 | 「cuspal asymmetryを含め最大5%」 | 記載なし |
| 結果 | 7例で使用（4例は断念）。1例が術後6日目にcusp prolapseでAR → 修復し8年再発なし。他は退院時AR≤1、中央値5年でAR≤1・全生存 | — | — |
| 手技上の要点 | **元の交連対称性を保つ（形態に応じて90°または180°に配置）**、LVOT内に深く留置、ボタンに緊張をかけない | — | — |

**重要な実務的所見（Filippa）**: **11例すべてが術中診断であり、術前CMRを含む包括的画像でも1例も指摘できなかった** → 「肺動脈弁は開けてみるまで分からない」ことを前提に、**術中に方針転換できる備え（代替弁の準備・患者への事前説明）が必須**。

**Davidの数値的な線引き**: 「**肺動脈STJが30mmを超える患者では、BSAによらずRossに消極的である**」

> `[FIG-7.1]` **出典: Filippa P, JTCVS Tech 2023;20:30-3, Figure 1（二尖肺動脈弁のTEEと術中像）**
> `[VIDEO-7.1]` 同 Video 1

### 7-2. 大動脈弁形成術の失敗後のRoss（Abeln, Homburg＋Montreal 80例）
- 初回修復から中央値6.6年後にRoss。元の形態は**一尖弁53%・二尖弁39%**
- CPB 144分・遮断98分（**初回Rossより短い**）、**周術期死亡・心筋梗塞・神経学的合併症ゼロ**
- 10年生存99%（年齢性別マッチ集団と同等）、**autograft再介入の累積発生率 8年で5.1%、しかも全例が弁温存手技**
- 弁輪>26mm（23例）で外部annuloplasty（Montreal=円形Dacronリング、Homburg 2010-2019=ePTFE、Homburg 1997-2011=心膜ストリップ）
- **結論: 「まず修復、ダメならRoss」という段階戦略は成立する**
- **Sievers（German Ross Registry）も同じ発想を提示**: 「修復あるいはOzakiを先に行い、失敗したらRossというのは興味深いが未証明の戦略」

### 7-3. 冠動脈奇形unroofing後のRoss（Verdi, Stanford）
17歳男性、右冠動脈左冠尖起始（ARCA）に対する**unroofing＋左右交連の切離・再懸垂＋pulmonary arteriopexy** → 直後からAI、2回の弁形成を経て高度AI再発。
- **なぜ難しいか**: ①unroofingで交連を切離・再懸垂するのでAIが起こる ②intramural coureの同定のため**大動脈肺動脈間を広範に剥離**してある ③**pulmonary arteriopexyで肺動脈が移動されている** ④長いunroofed RCAの再建
- 実際の対処: 胸骨再開時に**移動された肺動脈を胸骨から慎重に剥離**。大動脈と右房に送脱血 → **CPBを開始してから大動脈基部と肺動脈基部の間の剥離を進める**（前回の2回の大動脈切開と剥離で高度に癒着）→ 心停止後に肺動脈autograft内側面の剥離を完了
- autograftは**modified inclusion technique**で作製。左冠は正所性、**右冠はtunnelを分割してtranslocation**
- POD 0抜管、POD 5退院、TEEでtrivial ARのみ

### 7-4. その他（次パスで執筆）
- Ross-Konno（Said, ACS 2021;10(4):527-537 ＝ 手元に所蔵）
- 再三失敗した大動脈弁手術後のRoss（Loshusan, MMCTS 2024 → https://mmcts.org/case-report/1962）
- L字ministernotomy（Tsaroev, JTCVS Tech 2024 ＝ 手元に所蔵）

---

## 第8章　Autograft failure と再手術

### 8-1. 失敗の様式
- **弁尖は薄く柔軟なまま保たれることが多い**（Skillington: 摘出した全autograft弁尖に肉眼的変性なし）→ **failureは「弁の劣化」ではなく「基部の幾何学の破綻」**
- Skillingtonの11例の再手術: **10例に同定可能な技術的失敗**。4例は弁輪拡大を修正しなかった（1992-96年）、2例はオーバーサイズ28mm graft、4例は植込み時の歪みによるcusp prolapse
- **全再手術が7年以内（平均4.1年）に発生し、それ以降の失敗はゼロ**
- Caldaroni: 最初の4例（root replacement）のうち2例（50%）が基部拡大で戻ってきた。inclusionに切り替えて以降ゼロ

### 8-2. 稀だが致死的: autograft破裂・解離（Ramkaran, 11例のsystematic review）
- 発症年齢中央値39歳（20-56）、**Rossから中央値10年（6-18年）**
- **11例中9例がnative二尖弁**、Rossの適応は**8例が優位AR**
- **基部径中央値55mm（50-90mm）だが、60%は≤55mmで発症**
- 8/11が症候性、3/11は監視画像で偶発発見。初回検査はTTEが45%、確定はCT 55%・MRI 27%
- **9/11がautograft基部に限局**（冠動脈ボタン縫合線と遠位autograft縫合線が解離の進展を止める。ただし破裂のリスクは残る）
- 10例が手術（機械弁Bentall 4／生体弁Bentall 1／David-Yacoub 2／modified root remodeling 2／stentless porcine root 1）、**院内生存100%**。1例は術前に破裂して死亡
- **含意: 生涯監視の必須性と、より早期の待機的介入の検討**

### 8-3. 再手術の実際 — 3つの大規模シリーズ

| | Mayo（Stephens, 105例） | Mount Sinai（Stelzer, 83例89回） | Brussels（Jahanyar, 63例） |
|---|---|---|---|
| 期間 | 1991-2021 | 1996-2020 | 2001-2022 |
| 初回Rossの施設 | **84%が他施設**、大多数が無補強 | 75%が同一術者 | 76%がfree root技法 |
| Ross→再手術 | 平均10年前後 | **12.6±6.9年** | — |
| 4回目以上の胸骨切開 | **25%** | 3%（3-4回目） | — |
| 主な適応 | autograft逆流64% | autograft機能不全 68例 | 瘤のみ27%／瘤+AR 43%／AR単独30% |
| **手術死亡** | **5%** | **2.2%** | — |
| 遠隔成績 | 中央値6.3年で遠隔死亡13% | 再手術後生存 1/5/10/15年 = 94.6/87.4/82.3/**77.5%** | 生存 10年 **92.4%**、AV再手術回避 10年 **79.7%** |
| 遮断/CPB | 110±83 / 163±90分 | — | — |
| 輸血 | — | **28%のみ** | — |

**同時手技の多さが特徴**: Mayo（三尖弁17%・僧帽弁11%・CABG 8%）、Mount Sinai（**僧帽弁24件・三尖弁20件・心房細動アブレーション14件**・冠動脈5件）。→ **「Ross後の再手術はautograftだけの手術ではない」**

**Mayoの判断指針（Stephens）**
- autograft → **弁尖が構造的に正常・可動性良好・収縮能正常なら弁温存を検討。危険な再開胸で早期にCPBを回さねばならず長いCPB時間になる場合は避ける**
- **原則は機械弁Bentall**、生体弁は妊娠希望女性と抗凝固禁忌に限る
- RVOT → 原則カテーテル。ただし冠動脈解剖が許さないことがある
- autograft機能不全＋中等度以上のRV-PA導管機能不全 → **twin-root手技**
- RVOTには**将来のvalve-in-valveを見据えて大型のstented生体弁**。多数回胸骨切開歴や生体弁耐久性不良例では**機械弁PVR**（圧較差は安定するが出血 2.2%/年 vs 0.1%/年）
- **三尖弁の温存が決定的に重要**（人工肺動脈弁の機能不全は三尖弁が保たれていれば耐えられる）。弁輪>4cm or ≥中等度TRで修復
- twin-rootでは**左主幹がhomograftに癒着していることが多い**

**Brusselsの弁温存の技術（Jahanyar）**
- VBRまで周囲剥離 → 無冠洞を3-4mm残して切除 → 右冠ボタン → 左冠ボタン
- **⚠️ 最重要の教訓: 「初期のRossでは外科的弁輪レベルに心膜ストリップや人工物を用いていたが、これが後に高度石灰化を来しうる。現在は近位Ross縫合線にいかなる材料も用いない。既存の人工物による石灰化に遭遇したらValsalva graftを座らせる前に積極的にdebrideする」**
- VBRレベルにpledgeted 2-0 Ethibondを12本（膜性中隔部のみ大動脈尖の付着に沿う）。graftは非/左交連の高さでサイズ決定
- prolapseは中央cusp plication（5-0/6-0、他の2尖を基準尖にする）

**Homburg式のredo David（Liebrich, MMCTS 2024）— 初回Davidとの違い**
- **初回Davidとの最大の違いは、neo-aortic基部を neo-aortic弁輪よりはるかに下のレベルまで広範に全周性に授動すること**
- もう一つの要は**右室流出路と大動脈基部の丁寧な分離**
- **「full-root Ross後ならこれらは大きな労力なく安全に行えるが、jacket法やwrapped Ross後の剥離は、より密な癒着のためはるかに困難になりうる」** ← **補強法の選択が「10年後の再手術のしやすさ」を左右するという、他にない指摘**
- 基部周囲の組織量が多いため、**曲率の大きい針**を使ってneo-aortic弁尖の歪み・retractionを防ぐ

**Mayo/Westchester式の redo VSRR 2戦略（Marey）**
- graftサイズは**①autograftの左/無冠交連の高さ**、または**②弁の閉鎖が保たれるSTJ径に5-6mmを足す** — **「この状況では複数の方法を併用して最終決定するのがよい」**
- Case I（David V）: **2本のgraftを使用**。1本目（30mm）の基部と底部に4/0を複数かけて3つのpseudosinusを作り、subannular縫合線で固定 → autograft弁を交連縫合で吊り上げ → 3本の連続4/0で止血線 → 左冠 → **肺動脈分岐部の露出が後で困難になることを見越して先に肺動脈homograft遠位吻合** → 2本目（26mm）で大動脈再建 → 右冠
- Case II（David VI）: 26mm Valsalva graft単独。RVOTは25mm Inspiris Resilia生体弁付き導管
- **caveat: 石灰化したhomograftがautograftに癒着している場合、autograft弁の損傷を避けるため、癒着したautograft洞壁ごと一塊に切除する必要がある**
- **方針: 「Ross後に再手術を要する患者は、適応が拡大autograftであれhomograft不全であれ、大動脈側と肺動脈側の両方に対処する」**

> `[FIG-8.1]` **出典: Stephens EH, JTCVS Struct Endovasc 2026;9:100098, Figure 1（twin-root手術の完成図）** — CC BY
> `[VIDEO-8.1]` Liebrich M, MMCTS 2024 → https://mmcts.org/tutorial/1956 （redo David、13ステップ）
> `[VIDEO-8.2]` Marey GM, ACS 2023;12(3):282-4（annalscts.com）

---

## 第9章　ラーニングカーブ・volume-outcome・教育

### 9-1. 数字で見るラーニングカーブ（Tagliafierro, Montreal 673例）
- 5人の術者。**術者ごとに Early=1-69例、Middle=70-180例、Late=>180例**
- **主要合併症: 9.46% → 6.73% → 1.8%（p=0.003）**。主な駆動因子は長時間人工呼吸（5.8%→1.8%→0.9%）
- **CPB 203.5 → 169 → 163.5分**、**遮断 180 → 153 → 148分**、手術室使用時間 309 → 266 → 242分
- ICU在室 2 → 2 → 1日、在院 6 → 5 → 5日、輸血 43.6% → 33.2% → 22.8%
- **周術期死亡は3例（0.45%）のみで期間差なし**、退院時AR>1/4はわずか2例（0.3%）
- **CUSUM: 観察された主要合併症率がSTS予測を有意に下回るのは75-100例以降**
- **新規術者の参入はCUSUM曲線に有意な影響を与えなかった**

**なぜ悪化しなかったのかの著者の分析**
1. 5人全員が**大動脈基部手術の経験者**（大動脈外科医3・先天性外科医2）
2. **全員が同一の標準化手技を使用**
3. 術者だけでなく**チーム全体（看護師・麻酔科医・体外循環技士・集中治療医）の経験**が同時に蓄積
4. **周術期ケアの標準化**（早期離床、厳格な血圧管理、系統的な抗炎症薬処方）
5. 平均**>50例/年**

### 9-2. mentorshipの直接検証（Shih, Baylor Scott & White 234例）
経験あるRoss術者が**執刀した186例（1994-2021）vs メンターとして指導した48例（2001-2021）**:

| | 執刀 | 指導 | P |
|---|---|---|---|
| 手術死亡 | 3（2%） | 2（4%） | .28 |
| 院内再手術 | 6（3%） | 2（4%） | .75 |
| 10年生存 | 94.4% | 95.8% | .85 |

**条件**: 指導を受けた術者は**大動脈基部と大動脈弁reimplantationの経験者**であった。
**結論**: 「Ross手術は技術的に複雑だが、**経験ある大動脈基部外科医には、短期・長期成績を損なうことなく教えられる**」

### 9-3. 教え方の設計

**Mazine "How I Teach It"（Montreal）**
- **前提**: 研修者は**執刀者としてcomposite大動脈基部置換を複数回経験済み**であり、大動脈基部解剖に習熟していること
- **6ステップへの分解**: ①大動脈基部準備と冠動脈授動 ②autograft採取と準備 ③autograft植込み（近位吻合）④冠動脈再建 ⑤肺動脈homograft植込み ⑥autograft遠位吻合
- **ブタ心臓を用いたwet lab**
- **研修者が自分で患者ごとのtailored operative planを立て、術前に指導医に提示して議論する**
- **助手をしながら各ステップのtips and pitfallsを声に出して「narrate」させる**
- ステップごとに段階的に責任を移譲

**Chandra "How I Teach It"（UT Southwestern）— 心移植の摘出心を使う**
- 心移植のレシピエント心臓摘出後、**病理検査に出す前に手術室でそのままRossのシミュレーションに使う**
- **OHTに直接参加していない研修者**が、専任の指導医（多くは臓器採取担当医）のもとで実施 → **患者へのリスクゼロの高忠実度モデル**
- 手順: 肺動脈と大動脈の分離 → 大動脈基部と冠動脈ボタンの剥離（**弁輪から2-3mm、大動脈壁に平行に右房レベルまで**）→ 大動脈弁尖切除と基部解剖の観察（弁輪径・交連対称性・高さ）→ **この機会にKonno、Nicks-Nunez、Manouguianの解剖と手技も復習できる** → 漏斗部靱帯の切離 → autograft採取（**右角鉗子を肺動脈弁を通して弁輪の6-8mm下に**、Metzenbaum剪刀と#15刀で漏斗部中隔上部の後方筋束を部分的に分割、第1中隔枝に注意）→ 漏斗部筋のトリム → LVOTへの吻合 → 左冠・右冠の再建
- **遠位吻合は本質的にシミュレートできない**。homograftは高価なので使わず、原理の議論に留める
- 6心臓で実施、研修者の満足度は高い

**Davidの助言**: 「どんな複雑な手術にもラーニングカーブがあり、その急峻さは術者の技術、半月弁の機能解剖の知識、施行頻度に依存する。加えて、**最初の5-10例には経験ある術者がメンターとして必要である**」

### 9-4. 施設要件・標準化の提言
- ガイドライン側に記載済み: 年間1-2例の施設は10例超の施設より院内死亡が高い（OR 4.5）、術者レベルOR 3.8、学習曲線約75例、新規プログラムは年間10-15例（理想20-25例）
- **STSデータベースにはRoss専用のリスクスコアが存在しない**ため、Ross手術は「標準AVR」として評価されている。それでもCUSUMではSTS予測を下回る成績が達成できている（Tagliafierro）
- Reese論文（STS）でRossの死亡が3倍とされた背景: **施設あたり平均0.2-9.2例、95%の施設が年間<16件の大動脈基部手術**
- **Sievers & Ensminger（German Ross Registry）の提言**: さらなる質の向上には**高度の標準化（専用サイザーなど）**が望ましい。手技の簡略化、**標準化された研修カリキュラムの確立**、**認定を伴うproctoringの制度化**、in-vitroシミュレーションのための術前画像の精緻化、そして「完璧な手術に導くAIソフトウェア」の活用によって達成しうる

### 9-5. German Ross Registry（Sievers & Ensminger）の総括
- 2002年開始（1988-2001は後ろ向き）、**現在3ヶ国10施設・2,500例超**で3期目に入る
- **最も際立った結果は、若年〜中年患者の長期生存が少なくとも25年間、一般集団と変わらないこと**
- ただし**2期目（第2の10年）から生存にわずかな（有意でない）低下があり、autograft/homograft機能にもわずかな劣化がある**
- 未発表データ: **術前LVEF低下例は遠隔生存が悪い** → 不可逆的心筋障害の前に手術する意義
- autograft機能低下は**術前AR**と関連
- **再介入率は生体弁より低く機械弁より高い**。ただし直近10年で再手術リスクがやや上昇
- **術式そのものはもはやautograft再手術の独立予測因子ではなくなった**
- 外科的には**BSAに応じて弁輪を24-28mmに縮小・固定することが優れたautograft機能の重要因子**
- **水平面での無歪みの植込みが難しいのは、特にSievers Type 1 L-R（左右冠尖間にraphe）の二尖弁**
- 感染時のより積極的な抗菌薬投与がhomograft心内膜炎を防ぐ

---

## 第10章　周術期管理・術中評価

### 10-1. 麻酔・体外循環の設計（Scorsese, JCDD 2025 — 唯一のRoss麻酔総説）
- **送血は腕頭動脈起始より遠位の弓部にSeldinger法で** → **遮断を腕頭動脈直近位に置け、PA分岐部より遠位で遮断できるのでautograft採取と遠位肺動脈吻合が容易になる**。**TEEで術者のガイドワイヤーが近位下行大動脈の内腔にあることを確認する必要があり、外科・麻酔の連携ポイント**
- 脱血は両大静脈（単段カニューレ2本）。PFOや心内同時手技があれば右房単独も
- **LVベントは右上肺静脈から僧帽弁を越えてLVへ。TEEで先端が僧帽弁・大動脈弁に当たっていないことを確認**
- 心筋保護: 遮断時間が長いので順行性＋逆行性の併用。**逆行性を使う場合は冠静脈洞カテーテル位置をTEEでガイドして損傷を防ぐ**。del Nidoが多いが術者依存
- **血液温存: acute normovolemic hemodilution と retrograde autologous priming**（Stelzerもroutine化）

### 10-2. 術前画像で見るべきもの（Ross特異的）
- **CTCA**: 冠動脈の走行、**短い左主幹**、右冠動脈起始異常 → autograft採取・再建を難しくする
- **cMRI**: 弁の流体力学、心室機能、灌流、冠動脈奇形
- **CTA**: 大動脈基部と上行大動脈。**38-40mm超で同時手術を検討**
- **肺動脈弁複合体の集中評価**: 弁尖形態・弁輪径・組織の質・**漏斗部筋（厚さ・強度・周囲構造との関係）**。四尖/二尖はautograft使用を妨げうる
- **肺動脈基部と左主幹・左心耳の位置関係**を精査して採取時損傷を避ける

### 10-3. 術中TEE
- **術前**: 大動脈弁輪・Valsalva洞・STJ・上行大動脈の計測、弁形態と交連配置、**肺動脈弁機能と弁輪径**
- **Namの判定基準**: **中心性の軽微な逆流は許容。偏在性ジェットは弁尖prolapseや交連機能不全を示唆し、体循環圧では有意になりうる**
- Skillingtonの方針: 三尖で弁尖サイズが均等、trivial〜mildの逆流までが許容。**二尖・四尖・cuspal asymmetryならRossを行わない**
- **離脱後**: mildを超える残存ARは技術的問題を示唆し再遮断の対象
- **Florida sleeve法では、TEEガイド下で最後のsubannular縫合を結紮して annuloplastyのきつさを決める**（Spindel）

### 10-4. 血圧管理 — 施設間で目標が違う
| 施設 | 目標収縮期血圧 | 期間 | 第一選択薬 |
|---|---|---|---|
| Mount Sinai（El-Hamamsy） | <110 mmHg | 6-12ヶ月 | β遮断薬（dP/dt低下） |
| Mount Sinai（Stelzer） | <110 mmHg | **特に最初の24-48時間を厳格に** | — |
| Melbourne | <120 mmHg | β遮断薬3ヶ月 | β遮断薬 |
| Boston（円周補強） | 入院中<110、**退院後<120**（円周補強しているので在宅では厳格でなくてよい） | — | amlodipine/labetalol/lisinopril/metoprolol/valsartan |
| Lübeck | 「生涯の血圧管理」 | 生涯 | — |
| EACTS Consensus | <110-115 mmHg | 1年 | β遮断薬 |

→ **「補強の程度に応じて血圧管理の厳格さを変えてよいのか」は未解決の論点**（Bostonが明示的に主張、他は追随していない）

### 10-5. 抗炎症薬・抗血小板薬 — 根拠が最も薄い領域
| 施設 | レジメン |
|---|---|
| Melbourne / Mount Sinai / Montreal | NSAID 6ヶ月 |
| EACTS Consensus | イブプロフェン 5 mg/kg×3回/日を3-6ヶ月 |
| **Lübeck** | **クロピドグレル 75 mg/日×3ヶ月 ＋ イブプロフェン 400 mg/日×5週間** |
| Vienna（Ross-PEARS） | 低分子ヘパリン 6000 IU を3週間 |

→ **期間も薬剤も施設ごとにばらばらで、比較試験はない**ことを明示する。

### 10-6. 生涯フォロー
- 退院時 → 3-6ヶ月 → 以後年1回のエコー（EACTS）／Melbourneは年1回の診察＋隔年エコー／London（PEARS）は退院6週の外科診察 → 3ヶ月で循環器診察＋エコー → **1年でMRI** → 以後年1回エコー・2年ごとMRI
- Ramkaranの示唆: **二尖弁・術前AR例では、55mm未満でも破裂・解離が起こるため、監視間隔と介入閾値を個別化すべき**
- Chauvetteの示唆: **homograft機能不全の瞬間リスクは術後1年目が最大（3.5%/年）** → 早期のフォロー間隔を密にする根拠

---

## 補遺A　本レビューで明示する「対立点」一覧（v0.2で3項目追加）

| # | 論点 | A の立場 | B の立場 |
|---|---|---|---|
| 1 | **近位縫合線への人工物** | Liebrich（Stuttgart）: Dacronストリップを織り込む／Stelzer（Mount Sinai）: フェルトストリップで弁輪を拘束 | **Jahanyar（Brussels）: 初期に使った心膜/人工物が後年の高度石灰化の原因になった。現在は近位Ross縫合線に一切材料を使わない**／**David: 「近位吻合をTeflon feltで補強すべきでない。肺動脈弁輪が大動脈弁輪と同じかそれより低ければ不要であり、autograftの長期耐久性に悪影響を及ぼしうる」** |
| 2 | **autograftをDacronで包むか** | de Kerchove / Starnes / Emani / Schneider: 円周補強が全長の拡大を防ぐ（Starnesの10年再介入 4.0% vs 26.8%が最強の実証） | Mazine & El-Hamamsy: **形状を変えdynamismを損なう。mechanotransduction喪失で細胞外基質・平滑筋が乱れ弾性を失う**／**David: 「懐疑的。時の試練を経るまで古典的手技を捨てるべきでない」** |
| 3 | **弁輪サイジングの基準** | Melbourne/Homburg/German Registry: **患者体格**（性別・BSA）で目標径を決める | Mount Sinai/Hradec Kralove: **肺動脈弁輪径に合わせる**。Mazineは前者を「径の異なるautograftを歪めうる」と批判 |
| 4 | **二尖・四尖肺動脈弁** | Montreal: 個別判断で使用可（中期成績良好、640例中11例） | Melbourne: 使用しない（最大5%に遭遇）／David: **肺動脈STJ>30mmならBSAによらず消極的** |
| 5 | **脱細胞化homograft** | El-Hamamsy / Stelzer（2008年以降>99%）/ Réa: **15年再手術 1.2% vs 6.8%** | Skillington: 中期成績に明確な優位性なし、コスト・入手性から従来の凍結保存を継続 |
| 6 | **上行大動脈置換の閾値** | Homburg >30mm | Montreal/Mount Sinai(El-H) ≥38mm、Melbourne >38-40mm、**Mount Sinai(Stelzer) >50mm（それ未満はaortoplastyで<35mmへ）** |
| 7 | **subcoronary vs full root** | Sievers/Misfeld: ASと混合病変では常にsubcoronary。**630例でAR・弁輪径・BAV型のいずれも再手術リスク因子でなかった** | 大多数: full root＋補強（再現性）／Berdajs SR: 全体では優位性を支持しない（**ただし成人だけ見ると再手術回避はSCが98% vs 91.2%**）／David: 「両基部の幾何が似ていれば最良だが、それは例外」 |
| 8 | **術後血圧管理の厳格さ** | 大多数: <110-115を6-12ヶ月 | Boston（円周補強）: 在宅では<120で十分 |
| 9 | **STJの安定化に上行大動脈置換は要るか** ★新規 | Mount Sinai/Melbourne/Homburg: interposition graft または reduction aortoplasty | **Côté/Lansac: 拡大していない上行大動脈を置換する代わりにSTJリングを。Dacron管が不要になり、コンプライアンス・遠位吻合の省略・内皮連続性の保存という利点** |
| 10 | **筋skirtをどれだけ残すか（homograft側）** ★新規 | Skillington: **3-4mm**（免疫反応を減らし圧較差を下げる） | Réa: **0.5-1cm** ／ Urganci: autograft側は**5mm以上**残す（Valsalva graftへの縫い代のため） |
| 11 | **補強法の選択が「再手術のしやすさ」に及ぼす影響** ★新規 | — | **Liebrich（MMCTS 2024）: 「full-root Ross後の再David手術は大きな労力なく安全に行えるが、jacket法やwrapped Ross後の剥離は、より密な癒着のためはるかに困難になりうる」** ← 初回手術の選択が10年後の再手術リスクを決めるという、他にない指摘 |

---

## 補遺B　数値の要確認事項

1. **Liebrich 2021（ACS 10(4):485-490）の20年生存率**: Abstract「92%」 vs Results本文「15年92%／20年86%」 → 本文の値を採用し注記
2. **Skillington の弁輪目標径**: JTCVS 2015「男24-26mm、女22-24mm」 vs ACS 2021「男24-25mm、女22-24mm」 → 両方併記か新しい方
3. **Caldaroni の弁輪縮小の閾値**: 「native弁輪が女性>23mm、男性>25mmで積極的縮小」← Skillingtonの目標径と整合するか要確認
4. **Sievers のsubcoronary除外基準**: 2021年ACS論文「弁輪>31mm」 vs 同論文内「>32mm」 → 原典で再確認
5. **Mylonas メタ解析の生存HR 11.9** は信頼区間が 1.59-88.9 と極端に広い。**症例数の少ない比較研究のIPD再構築であることを注記して、点推定値を強調しすぎない**

---

## 補遺C　図・動画の取得タスク（P3で実施）

### 最優先（本レビューの骨格を担う図）
| ID | 出典 | 内容 | ライセンス |
|---|---|---|---|
| FIG-0.1 | Mazine, ACS 2021;10(4), Figure 1 | 3術式の並置模式図 | PMC / CC BY-NC-ND |
| FIG-4.1 | Skillington, JTCVS 2015, Fig 1-3 | 大動脈基部の作り替え3パターン | 非OA → PDF切り出し |
| FIG-4.5 | Dafflisio, JTCVS Tech 2025, Fig 1-8 | 加圧下でのautograft最適化8図 | PMC / **CC BY** |
| FIG-3.5 | Spindel, JTCVS Tech 2024, Fig 1+2 | Florida sleeve のシェーマ＋術中写真の1対1対応 | PMC / CC BY-NC-ND |
| FIG-1.1/1.2 | Mazine, ATS 2018, Fig 1-2 | 第1中隔枝の位置／針の通し方 | 非OA → PDF切り出し |
| FIG-4.7 | Zhu, JTCVS 2023, Figure 1 (A-L) | ACP付きinclusionの12コマ | 非OA → PDF切り出し |
| FIG-2.1 | Sievers, JTCVS 2010, E-Appendix Fig E1-E9 | subcoronaryの全工程9図 | **未入手（online supplement）** |

### 動画リンク（スクショ＋ハイパーリンク）
MMCTS 7本（URL確定済み、HANDOFF.md 参照）＋ Ann Cardiothorac Surg Masters 6本（annalscts.com）＋ JTCVS Tech/Open/JTCVS の本文中Video（**Sievers 2018・Starnes 2023・Chauvette 2022・Zhu 2023 の動画を新たに確認**）→ P3で1本ずつ実URLを確認

### ガイドライン側から再利用する図（重複作業を避ける）
EACTS Consensus Figure 2（深く対称な留置）・Figure 3（loose jacket）・Figure 4（extra-aortic ring）・Figure 5-7（autologous inclusion）・Figure 8-10（prosthetic inclusion）

### 未入手で追加取得を検討するもの
- **Sievers 2010 JTCVS の online E-Appendix**（subcoronary 9図＋動画）— 第2章の中核
- Klena 2000 J Heart Valve Dis 全文（現在は抄録のみ、廃刊誌）
- Herrmann 2019 WJPCHS 全文（現在のmdはメタデータのみで本文が空）
