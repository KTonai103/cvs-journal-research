# -*- coding: utf-8 -*-
import io, sys
P="md/CABG_integrated_review_2026-07.md"
s=open(P,encoding="utf-8").read()

FIGS=[
("### 1-4. オフポンプの隆盛と幻滅",
 "f01_timeline_revasc.png","図1",
 "冠動脈血行再建の主要マイルストーン年表（上段=外科／下段=PCI）。**1985年に off-pump CABG** が置かれ、1967年 CABG臨床導入、1970年 心筋保護液導入、1971年 橈骨動脈導入が読み取れる。§1-2 で述べた「起点は拍動下手術」という順序は、1960年の First CABG in a human と1970年の cardioplegia の位置関係に対応する。",
 "Gaudino M, et al. *Lancet* 2023;401:1611–28（PMID 37121245, CC BY 4.0）Figure 1"),

("### 3-4. 高リスク患者では逆に利益が出る",
 "f02_crossover_subgroup.png","図2",
 "**クロスオーバー率（術者経験の代理指標）で層別した長期死亡**。≤3% 群 IRR 0.96（0.60–1.42）、>3–10% 群 IRR 1.07（0.94–1.21）はいずれも有意でなく、**>10% 群のみ IRR 1.30（95%CI 1.04–1.62）**。最下段の全体推定は IRR 1.11（1.00–1.23）。ROOBY Trial は最上段（>10%）に、CORONARY と GOPCABE は中段（>3–10%）に置かれている——この配置が §2-6 の表と対応する。",
 "Gaudino M, et al. *J Am Heart Assoc* 2018;7:e010034（PMID 30373421, CC BY-NC-ND 4.0）Figure 3"),

("## §9. 術中グラフト評価 — 到達度を手術室で確認する",
 "f03_incomplete_revasc_subgroup.png","図3",
 "不完全血行再建の相対頻度で層別した長期死亡。IR差 ≤2 群 IRR 0.81（0.44–1.48）、IR差 >2 群 IRR 1.16（0.91–1.48）、全体 1.10（0.93–1.30）で、**いずれも有意ではない**。すなわち「不完全性が死亡差を生む」という機序は、この層別だけでは確定していない。§8 の結論が Thakur の再介入解析（再バイパス OR 2.57）に依拠しているのはこのためである。",
 "Gaudino M, et al. *J Am Heart Assoc* 2018;7:e010034（PMID 30373421, CC BY-NC-ND 4.0）Figure 4"),

("### 4-2. Squiers の Medicare 123万例 — 逆向きの最大データ",
 "f04_raja_25yr_km.png","図4",
 "上＝傾向スコアマッチ後の25年 Kaplan–Meier 生存曲線（logrank P<0.0001）。**OPCAB 57.5% vs ONCAB 42.7%**、リスク集合は各5,666/5,681例から始まり、20年時点で 1,172/551 例が残存する。下＝30日以降の累積死亡（早期死亡を競合リスクとして処理、P<0.001）。**両群の乖離が10年を超えてから拡大する**ことが視覚的に確認できる——これが §4-1 で述べた「10年以降 subdistribution HR 0.53」に対応する。",
 "Raja SG, et al. *Ann Thorac Surg Short Rep* 2026;4:556–60（PMID 42266971, CC BY-NC-ND 4.0）Figures 1・2"),

("### 5-4. 3本目の動脈グラフト",
 "f05_conduit_patency.png","図5",
 "上＝導管別の統合開存率と平均造影追跡年数。**橈骨動脈 93.2%（5.5年）、右内胸動脈 90.9%（6.9年）、no-touch 伏在静脈 89.3%（4.7年）、従来伏在静脈 81.8%（4.5年）、右胃動脈 61.2%（2.8年）**。下＝従来伏在静脈を基準としたグラフト閉塞のフォレストプロット。**有意に優れるのは RA（IRR 0.54）と NT-SV（IRR 0.55）のみで、GEA 0.98・RITA 1.02 は基準と差がない**。§15-4 の RITA 論争はこの2行が火種である。",
 "Gaudino M, et al. *J Am Heart Assoc* 2021;10:e019206（PMID 33686866, CC BY-NC-ND 4.0）Table 2・Figure 1"),

("### 7-2. Vallely の定量化と、メモの「脳卒中0.4%」",
 "f06_notouch_aorta_cva.png","図6",
 "30日脳血管イベントを近位吻合の戦略別に層別したフォレストプロット。**大動脈 no-touch 群は RR 0.41（95%CI 0.27–0.61）、I²=0%**（イベント 30/8,291 vs 172/13,442）。対して**近位吻合デバイス群は RR 0.71（0.33–1.55）で有意差なし**（32/3,192 vs 106/7,495）。サブグループ間差の検定は P=0.20。**「クランプを外す」だけでは足りず「触らない」ことが要件である**という §7-1 の結論が、この2つのサブトータルの対比で読み取れる。",
 "Pawliszak W, et al. *J Am Heart Assoc* 2016;5:e002802（PMID 26892526, CC BY-NC 4.0）Figure 3"),

("### 7-3. ガイドラインの位置づけ",
 "f07_anaortic_grafting_strategies.png","図7",
 "anaortic OPCAB を維持するための多枝動脈グラフト構成4通り。**A**＝in situ LITA–LAD ＋ in situ RITA を橈骨動脈で延長し横隔洞経由で側壁/下壁へ。**B**＝LITA–LAD ＋ LITA–RITA（図示）または LITA–橈骨の「T」グラフトで側壁/下壁。**C**＝in situ RITA–LAD ＋ in situ LITA–側壁。**D**＝LITA–LAD ＋ LITA–橈骨「Y」グラフトで対角枝、RITA で側壁。**4通りいずれも上行大動脈への吻合を含まない**ことが、§7 の要件を満たす具体形である。",
 "Vallely MP, et al. *JTCVS Tech* 2021;10:140–8（PMID 34977717）Figure 4。原図は CC BY-NC-ND 4.0 として再掲されたもの"),

("### 11-3. 公式の訓練パスウェイ — ロボット領域で先行",
 "f08_simulation_performance.png","図8",
 "シミュレーション訓練前後の技術パフォーマンス（標準化平均差）。**全体 SMD 2.18（95%CI 1.73–2.63）、Z=9.44、P<0.00001**。組織/ハイブリッドシミュレータ 2.55（1.96–3.14）、合成シミュレータ 1.86（1.22–2.51）で、サブグループ間差は有意でない（P=0.12）。異質性は I²=81% と高い。**総被験者は423名分の対応データであり、これが §11-2 で述べた効果量の根拠である。**",
 "Sidik AI, et al. *J Surg Educ* 2026（PMID 42236427, CC BY 4.0）Figure 5"),
]

for anchor,fn,label,body,cite in FIGS:
    assert s.count(anchor)==1, f"anchor not unique: {anchor} ({s.count(anchor)})"
    block = (f"\n![{label} {fn}](../figures/{fn})\n\n"
             f"***{label}.*** {body}\n\n"
             f"*出典: {cite}*\n\n")
    s = s.replace(anchor, block + anchor, 1)

# 図表一覧 + copyright, inserted before the references section
idx_anchor = "## 引用文献（本文で参照した52編）"
assert s.count(idx_anchor)==1
index = """## 図表一覧（原典PDFからの切り出し）

本文に挿入した図表8点はすべて **`cabg_evidence/pdf/` の原典PDFから該当領域を切り出したもの**で、画像は `cabg_evidence/figures/` に格納している。**掲載対象は Creative Commons ライセンスで公開された論文に限定し**、「Reprinted with permission」と明記された転載図（例: Vallely Figure 2・3）は権利がCC範囲に及ばないため除外した。

| 図 | 内容 | 掲載節 | 出典（ライセンス） |
|---|---|---|---|
| 図1 | 冠動脈血行再建の年表（外科／PCI） | §1-4 | Gaudino, Lancet 2023（CC BY 4.0） |
| 図2 | クロスオーバー率で層別した長期死亡 | §3-4 | Gaudino, JAHA 2018（CC BY-NC-ND 4.0） |
| 図3 | 不完全血行再建で層別した長期死亡 | §9 冒頭 | Gaudino, JAHA 2018（CC BY-NC-ND 4.0） |
| 図4 | 25年 Kaplan–Meier 生存＋競合リスク累積死亡 | §4-2 | Raja, ATS Short Rep 2026（CC BY-NC-ND 4.0） |
| 図5 | 導管別 統合開存率＋閉塞フォレストプロット | §5-4 | Gaudino, JAHA 2021（CC BY-NC-ND 4.0） |
| 図6 | 30日脳血管イベント（no-touch／デバイス／クランプ） | §7-2 | Pawliszak, JAHA 2016（CC BY-NC 4.0） |
| 図7 | anaortic 多枝動脈グラフト構成 A–D | §7-3 | Vallely, JTCVS Tech 2021（CC BY-NC-ND 4.0） |
| 図8 | シミュレーション訓練の技術パフォーマンス | §11-3 | Sidik, J Surg Educ 2026（CC BY 4.0） |

> **著作権について** — 掲載図表はいずれも上記ライセンスの条件下で引用しており、著作権は各原著者・出版社に帰属する。CC BY-NC / BY-NC-ND のものは**非営利かつ改変なし**の条件で、原典の数値を本文の要約と照合するために引用している。臨床判断にあたっては必ず原典を参照すること。

---

"""
s = s.replace(idx_anchor, index + idx_anchor, 1)
open(P,"w",encoding="utf-8").write(s)
print("inserted 8 figures + index. bytes:", len(s.encode()))
