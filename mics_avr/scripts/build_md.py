#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build md/MICS_AVR_figure_atlas.md from figsel.SEL + figs_index.json.

All figures come from PMC Open Access articles whose CC licence was verified via
the PMC OA web service (oa.fcgi). No figure is authored here.
"""
import json, os, sys, textwrap

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'scripts'))
from figsel import SEL

IDX = json.load(open(os.path.join(BASE, 'figs_index.json')))
SELMAP = {s[0]: s for s in SEL}

SECTIONS = [
 ("1", "術前評価とアプローチ選択", """
MICS AVR の成否の大半は **CT による上行大動脈の位置評価**で決まる。右前開胸（RAT / RAMT）が成立する条件は、
おおむね「軸位断で上行大動脈の**半周以上が胸骨傍線より右**にあり、左方偏位していないこと」。
大動脈が正中〜左方にある症例は部分胸骨切開（J字・逆V字）へ振り分ける。

AR 症例に固有の追加チェックは以下。

- **上行大動脈径**：AR の背景に annuloaortic ectasia / BAV があると上行大動脈が拡大している。上行置換や基部手術を要するなら MICS の適応判断が変わる（完全内視鏡下に Bentall まで行う施設報告もある → 図 inc14 の出典）。
- **弁輪径と STJ**：AR では弁輪が拡大しており AS より大きいサイズが入りやすい。逆に STJ 拡大例では弁尖の接合が失われている（§7 の El Khoury 分類）。
- **RCA の起始高位・石灰化分布**：横切開（transverse aortotomy）か縦切開（longitudinal / TATEGIRI）かの分岐点になる。
""", ["ct01","ct02","ct03","ct04","ct05","ct06","ct07"]),

 ("2", "体位", """
右前開胸・腋窩アプローチとも、右背部にロールを入れて**右胸を 20–30° 挙上**し、右上肢を頭側または下垂させて右前胸〜腋窩を展開する。
腋窩アプローチでは「**槍投げ（spear-throwing / javelin thrower's）体位**」と呼ばれる、右上肢を挙上して前腋窩線を露出する体位が用いられる。
体外式除細動パッドの貼付位置（右前胸を避け、左側胸部＋背部）と、鼠径部（大腿動静脈）を必ず消毒野に含めることを作図時に忘れないこと。
""", ["pos01","pos02","pos03","pos04"]),

 ("3", "皮切・ポート配置", """
オペレコの「創」の図で最も使われる部分。代表的な選択肢は以下の 4 つ。

| アプローチ | 主創の位置 | 備考 |
|---|---|---|
| **右前開胸（RAT / RAMT）** | 第 2 または第 3 肋間、胸骨右縁外側 5–6 cm | MICS AVR の主流。第 3 肋間は基部・上行まで届きやすい |
| **部分胸骨切開（J字）** | 胸骨柄〜第 3/4 肋間で右へ J 字に離断 | 上行大動脈が正中〜左方でも可。中枢送脱血が容易 |
| **部分胸骨切開（逆V字）** | 胸骨上部を逆V字に離断 | 胸骨体を温存 |
| **腋窩（transaxillary / MICLAT-S）** | 前腋窩線・第 3 肋間 | 創が腋窩に隠れ整容性に優れる |

完全内視鏡下（TE-AVR）では主創に加えて **working port・3D カメラポート・Chitwood クランプ刺入部**の 3 つを別に置く。
ポート数は施設により 2〜4 で、代表的な組み合わせは
「主創＝第 2〜3 肋間 / カメラ＝前腋窩線第 2〜3 肋間 / working port＝第 4 肋間 / Chitwood＝中腋窩線第 3 肋間」。
""", ["inc01","inc02","inc03","inc04","inc05","inc06","inc07","inc08","inc09","inc10","inc11","inc12","inc13","inc14","inc15","inc16","inc17","inc18","inc19","inc20"]),

 ("4", "送脱血・心筋保護（AR で最重要）", """
**AR 症例の MICS AVR で最大の技術的問題は心筋保護である。** 大動脈基部からの順行性心筋保護は逆流によって左室へ流れ込むため機能しない。
選択肢は 3 つで、いずれも作図が必要になる。

1. **大動脈切開後の冠動脈口への直接注入（selective ostial cardioplegia）** — 最も広く使われる。
   東京ベイ浦安市川医療センター/順天堂の 104 例（moderate 以上の AI）の報告では、遮断前に **KCl とランジオロールを全身投与**して細動・停止させたうえで大動脈を切開し、内視鏡ガイド下に左右冠動脈口へ選択的に冷晶質液を注入。
   完全胸骨切開への転換 0 例、手術死亡 0 例、平均遮断時間 72.5 ± 21.8 分（Ito J, et al. *JTCVS Tech* 2023;18:28-36. doi:10.1016/j.xjtc.2023.01.002）。
2. **逆行性（冠静脈洞）心筋保護** — 右房を開いて冠静脈洞にカニューレを purse-string で留置し、持続冷血逆行性心筋保護（700 mL/h）を行う方法（Sato S, et al. *Ann Thorac Cardiovasc Surg* 2022;28:36-40. doi:10.5761/atcs.nm.20-00293）。均一な心筋冷却が得られる。
3. **経皮的冠静脈洞カニューレ** — 内頸静脈から留置。MICS 用だが施設限定。

送脱血は、上行大動脈への**中枢送血**（右前開胸でも purse-string を直視下にかけられる）と**大腿動脈送血**の二択。
中枢送血は逆行性灌流による脳塞栓リスクを避けられるため、可能なら第一選択とする施設が多い。
遮断は **Chitwood-DeBakey 型の経胸壁クランプ**を別刺入孔から入れるのが標準。

AR ではさらに、遮断までの間に逆流で左室が膨満するため **左室ベント（右上肺静脈経由）を早期に確保**することが重要。
""", ["cp01","cp02","cp03","cp04","cp05","cp06","cp07","cp08","cp09","cp10","cp11","cp12","cp13"]),

 ("5", "大動脈切開・弁露出・弁縫着", """
**大動脈切開**は、従来の**横切開（hockey-stick）**と、内視鏡下で普及した**縦切開（longitudinal / TATEGIRI）**がある。
縦切開は無冠尖に向けて縦に延長するもので、270° の弁輪露出が得られ、RCA 高位起始例でも安全域が広い。閉鎖は 2 層縫合。

AR では弁尖に石灰化がないため**弁切除自体は容易**で、AS のようなデブリードマンや弁輪石灰化の処理はほぼ不要。
一方で**弁輪が軟らかく拡大している**ため、
- サイジングは慎重に（過大サイズは弁輪破裂・冠動脈口閉塞のリスク）
- 縫合は everting mattress（pledget を左室側）か non-everting mattress か連続縫合か、施設方針を明示

を作図で示すとよい。自動結紮（Cor-Knot）を使う場合は、**ファスナーの向きを Valsalva 洞と反対側に向ける**こと。逆向きで洞穿孔をきたした報告がある（図 av13/av14）。
""", ["av01","av02","av03","av04","av05","av06","av07","av08","av09","av10","av11","av12","av13","av14"]),

 ("6", "人工弁（Avalus ほか）", """
**Avalus™（Medtronic）** はウシ心膜弁で、支持フレームが **PEEK（ポリエーテルエーテルケトン）製＝金属フリー**、
硫酸バリウム含浸により X 線不透過性を確保している。弁尖は内側マウント（interior mounting）で、将来の valve-in-valve での冠動脈閉塞リスクを下げる設計。
縫合輪には**弁尖の中点／nadir にマーカー**があり、縫合間隔を等分しやすい。抗石灰化処理は AOA（alpha-amino oleic acid）。
金属アレルギー症例で選択される（PMC13245353）。
""", ["v01","v02","v03"]),

 ("7", "大動脈弁・大動脈基部の解剖（3尖弁）", """
オペレコの「A弁 3 尖」のシェーマに使える図。用語を正確に区別しておくと図が締まる。

- **VBR（virtual basal ring）** — 3 弁尖の nadir を結ぶ仮想平面。臨床で「弁輪径」と呼ぶのはこれ。
- **VAJ（ventriculo-arterial junction）** — 心室筋と大動脈壁の解剖学的境界。線維性部では VBR と一致するが、筋性部（左・右冠尖側）では乖離し、**myocardial crescent（筋性三日月）**をつくる。
- **FAA（functional aortic annulus）** — VBR から STJ までの、弁を支える機能単位。
- **交連下三角（interleaflet triangle）**
- **接合面** — 各弁尖の lunule（Arantius 結節から交連まで）が重なる領域。effective height (eH) が 9 mm を下回ると prolapse が生じうる。

**AR の機序は El Khoury 分類**で整理する（図 an06）。
Type I＝弁尖運動正常で FAA 拡大または穿孔（Ia: STJ+上行拡大、Ib: 基部拡大、Ic: VBR 拡大、Id: 穿孔）、Type II＝弁尖逸脱、Type III＝弁尖制限。
弁置換のオペレコでも「どの機序の AR だったか」を図示できると術式選択の根拠が明確になる。
""", ["an01","an02","an03","an04","an05","an06","an07","an08","an09","an10","an11","an12"]),
]


def cite(pmc, fidx):
    a = IDX[pmc]
    au = a['authors'][0].split(',')[0] if a['authors'] else ''
    jr = a['journal']
    yr = a['year']
    doi = a['doi']
    en = a['figs'][fidx]['caption']
    en = (en[:120] + '…') if len(en) > 120 else en
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/"
    doipart = f" doi:{doi}" if doi else ""
    return (f"出典: {au} et al. *{jr}* {yr}.{doipart} "
            f"[{pmc}]({url})（{a['license']}）／原図: \"{en}\"")


def figblock(fid, n):
    _, pmc, i, jcap = SELMAP[fid]
    import glob
    files = glob.glob(os.path.join(BASE, 'figures', f'mics_{fid}_{pmc}.*'))
    if not files:
        raise SystemExit(f'missing image for {fid}')
    fn = os.path.basename(files[0])
    return (f"![図{n}](../figures/{fn})\n"
            f"*図{n}｜{jcap}｜{cite(pmc, i)}*\n")


def main():
    out = []
    A = out.append
    A("# MICS AVR（大動脈弁閉鎖不全症）— オペレコ作図用 図譜\n")
    A("> 右小開胸／部分胸骨切開／完全内視鏡下 AVR の**手術記録（オペレコ）の作図に使える図**を、")
    A("> **PMC のオープンアクセス（CC ライセンス）論文からのみ**集めたもの。")
    A("> 体位・ポート配置・main 創の位置・人工弁（Avalus）・大動脈弁 3 尖の解剖を中心に、")
    A("> 大動脈弁閉鎖不全（AR / AI）症例に固有の論点（**心筋保護**・弁輪拡大・上行大動脈）を軸に構成した。\n")
    A(f"- 収載図: **{len(SEL)} 点** / 出典論文: **{len({s[1] for s in SEL})} 編**（すべて CC BY / CC BY-NC / CC BY-NC-ND）")
    A("- ライセンスは PMC OA Web Service（`oa.fcgi`）で 1 編ずつ機械照合し、CC ライセンスが確認できた論文のみを採用した")
    A("- 図は**すべて原著のもの**。本図譜で新たに作図したイラストは 1 点も含まない")
    A("- 作成日: 2026-07-26\n")
    A("---\n")

    A("## 0. AR に対する MICS AVR — 押さえるべき 5 点\n")
    A("1. **心筋保護が最大の論点。** 順行性大動脈基部投与は逆流のため無効。"
      "大動脈切開後の**冠動脈口への選択的注入**か、**冠静脈洞からの逆行性**を選ぶ。→ §4\n")
    A("2. **左室ベントを早期に。** AR で左室が拡大・膨満するため、右上肺静脈からのベントを遮断前後で確実に確保する。\n")
    A("3. **弁輪は軟らかく拡大している。** 石灰化がないので弁切除は容易だが、"
      "過大サイジングによる弁輪損傷に注意。縫合様式（everting / non-everting mattress / 連続）を図に明示する。\n")
    A("4. **上行大動脈を必ず評価する。** AR の背景に BAV / annuloaortic ectasia があると上行拡大を伴い、"
      "上行置換や基部手術の要否で術式・アプローチが変わる。\n")
    A("5. **AR 単独例の MICS AVR の報告は少ないが成績は良好。** "
      "慢性重症 AR に対する RAT-AVR 8 例の連続報告では院内死亡 0、一過性 AF 3 例（37.5%）、"
      "術後に LVDd 63→51 mm（p=0.012）、LVDs 42→35.5 mm（p=0.018）と有意に縮小した"
      "（Jung EY, et al. *J Yeungnam Med Sci* 2024;41:213-219. doi:10.12701/jyms.2024.00290, "
      "[PMC11294798](https://pmc.ncbi.nlm.nih.gov/articles/PMC11294798/)）。"
      "moderate 以上の AI 104 例に対する内視鏡補助下 selective ostial cardioplegia の報告でも、"
      "完全胸骨切開への転換 0 例・手術死亡 0 例（Ito J, et al. *JTCVS Tech* 2023;18:28-36）。\n")
    A("---\n")

    n = 0
    for num, title, intro, ids in SECTIONS:
        A(f"## {num}. {title}\n")
        A(textwrap.dedent(intro).strip() + "\n")
        for fid in ids:
            n += 1
            A(figblock(fid, n))
    A("---\n")

    # ---- 図表一覧 ----
    A("## 8. 図表一覧\n")
    A("| # | 図ID | 内容 | 出典 (PMCID) | ライセンス |")
    A("|---|---|---|---|---|")
    n = 0
    for num, title, intro, ids in SECTIONS:
        for fid in ids:
            n += 1
            _, pmc, i, jcap = SELMAP[fid]
            plain = jcap.replace('**', '').replace('==', '')
            plain = plain[:62] + ('…' if len(plain) > 62 else '')
            A(f"| 図{n} | `{fid}` | {plain} | [{pmc}](https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/) | {IDX[pmc]['license']} |")
    A("")

    # ---- 出典文献 ----
    A("## 9. 出典文献（図を採用した論文）\n")
    used = sorted({s[1] for s in SEL}, key=lambda p: (IDX[p]['year'], IDX[p]['journal']))
    for k, pmc in enumerate(used, 1):
        a = IDX[pmc]
        au = ', '.join(x.split(',')[0] for x in a['authors'][:2])
        if len(a['authors']) > 2:
            au += ', et al'
        doi = f" doi:{a['doi']}." if a['doi'] else ""
        A(f"{k}. {au}. **{a['title']}** *{a['journal']}* {a['year']}.{doi} "
          f"[{pmc}](https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/) — {a['license']}")
    A("")

    A("## 10. 図は無いが AR × MICS AVR で必読の文献\n")
    A("PMC で全文は読めるが CC ライセンスが確認できず、図を転載していないもの。リンク先で図を確認できる。\n")
    for r in [
      ("Ito J, Nakanaga H, Fujii H, Tabata M.", "Endoscopically assisted selective antegrade cardioplegia in minimally invasive aortic valve replacement for patients with aortic insufficiency.", "JTCVS Tech", "2023;18:28-36", "10.1016/j.xjtc.2023.01.002", "PMC10122126", "AR に対する MICS AVR の心筋保護の決定版。104 例。内視鏡下 selective ostial cardioplegia の手順が step-by-step で図示されている"),
      ("Sato S, Azami T, Kawamoto T, et al.", "Safety and Applicability of Continuous Retrograde Cardioplegia in Minimally Invasive Aortic Valve Replacement: New Approaches.", "Ann Thorac Cardiovasc Surg", "2022;28:36-40", "10.5761/atcs.nm.20-00293", "PMC8915936", "持続冷血逆行性心筋保護（700 mL/h）による MICS-AVR 9 例"),
      ("Jung EY, Im JE, Min HK, Lee SS.", "Aortic valve replacement through right anterior mini-thoracotomy in patients with chronic severe aortic regurgitation.", "J Yeungnam Med Sci", "2024;41:213-219", "10.12701/jyms.2024.00290", "PMC11294798", "慢性重症 AR に限定した RAT-AVR の連続 8 例。AR 単独を扱った数少ない報告"),
      ("Lamelas J.", "Minimally invasive aortic valve replacement: the \"Miami Method\".", "Ann Cardiothorac Surg", "2015;4:71-77", "10.3978/j.issn.2225-319X.2014.12.10", "PMC4311159", "MICS AVR の古典的手技論文。術野写真 12 点（PMC で全文閲覧可）"),
      ("Glauber M, Ferrarini M, Miceli A.", "Minimally invasive aortic valve surgery: state of the art and future directions.", "Ann Cardiothorac Surg", "2015;4:26-32", "10.3978/j.issn.2225-319X.2014.06.03", "PMC4384243", "MIAVR 総説"),
      ("Vola M, Fuzellier JF, Campisi S, et al.", "Technical points for aortic valve replacement through right anterior minithoracotomy.", "Eur J Cardiothorac Surg", "2018;54:194", "10.1093/ejcts/ezy105", "", "RAT-AVR の technical points"),
      ("Malvindi PG, et al.", "Minimally invasive aortic valve replacement through a right anterior thoracotomy.", "Multimed Man Cardiothorac Surg", "2024", "10.1510/mmcts.2024.041", "", "MMCTS の手技動画（非 OA）"),
    ]:
        au, ti, jr, vol, doi, pmc, note = r
        link = f" [{pmc}](https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/)" if pmc else ""
        A(f"- {au} **{ti}** *{jr}* {vol}. doi:{doi}.{link}  \n  → {note}")
    A("")

    A("---\n")
    A("## 著作権について\n")
    A("収載した図はすべて各出版社・著者が保持する著作権物であり、"
      "PMC Open Access Subset において CC BY / CC BY-NC / CC BY-NC-ND のいずれかで公開されているものに限って引用している。"
      "各図のキャプションに原典・DOI・PMCID・ライセンスを明示した。"
      "**個人の学習・診療の参考目的での利用に限る。** 再配布・商用利用・改変は各ライセンスの条件に従うこと"
      "（NC 付きは商用不可、ND 付きは改変版の配布不可）。\n")

    p = os.path.join(BASE, 'md', 'MICS_AVR_figure_atlas.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print('wrote', p, len('\n'.join(out)), 'chars,', n, 'figures')


if __name__ == '__main__':
    main()
