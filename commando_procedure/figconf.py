# -*- coding: utf-8 -*-
"""Figure-injection config for the Commando Procedure integrated review.

Run:  python3 ~/.claude/skills/paper-figure-extraction/scripts/inject.py \
          commando_procedure/figconf.py --check
Then without --check. Regenerate the HTML from the clean MD first
(`python3 commando_procedure/build_html.py`) — inject.py refuses to run twice.

All figures are extracted from the PDFs in commando_procedure/pdfs/ — either as
native embedded raster artwork (extract_images.py, 150–300 dpi) or, for the
AATS recommendation tables, as 220-dpi page crops defined in figcrop.json.
"""

HTML_PATH = "../output/commando_procedure_review.html"
MD_PATH = "md/Commando_Procedure_IntegratedReview_2026.md"
FIG_DIR = "figures"

SOURCES = {
    "aats": ("paper", "📘 AATS 2016 IE 手術ガイドライン（Pettersson & Hussain 2019）",
             "Pettersson GB, Hussain ST. Ann Cardiothorac Surg 2019;8:630-44"
             "（図はいずれも 2016 AATS Consensus Guidelines, J Thorac Cardiovasc Surg "
             "2017;153:1241-1258.e29 からの転載）"),
    "yi": ("paper", "📄 Yi H, et al. Gen Thorac Cardiovasc Surg 2025（総説）",
           "Yi H, Li Y, Zhao Q, Wu X. Gen Thorac Cardiovasc Surg 2025;73:567-78"),
    "navia19": ("paper", "📄 Navia JL, et al. Ann Thorac Surg 2019（Cleveland Clinic n=138）",
                "Navia JL, Elgharably H, Hakim AH, et al. Ann Thorac Surg 2019;108:1314-24"),
    "navia23": ("paper", "📄 Navia JL, Aleman R. JTCVS Tech 2023（hemi-Commando 手技）",
                "Navia JL, Aleman R. JTCVS Tech 2023;22:88-9"),
    "navia10": ("paper", "📄 Navia JL, et al. J Thorac Cardiovasc Surg 2010（hemi-Commando 原型）",
                "Navia JL, Al-Ruzzeh S, Gordon S, Fraser T, Aguero O, Rodriguez L. "
                "J Thorac Cardiovasc Surg 2010;139:1077-81"),
    "elg": ("paper", "📄 Elgharably H, et al. Eur J Cardiothorac Surg 2018（hemi-Commando n=37）",
            "Elgharably H, Hakim AH, Unai S, et al. Eur J Cardiothorac Surg 2018;53:1055-61"),
    "marin": ("paper", "📄 Marin-Cuartas M, et al. Eur J Cardiothorac Surg 2023（Leipzig n=22）",
              "Marin-Cuartas M, De La Cuesta M, Davierwala PM, et al. "
              "Eur J Cardiothorac Surg 2023;64:ezad208"),
    "forteza": ("paper", "📄 Forteza-Gil A, et al. Eur J Cardiothorac Surg 2025（Barcelona n=78）",
                "Forteza-Gil A, Sandoval E, Martínez-López D, et al. "
                "Eur J Cardiothorac Surg 2025;67:ezaf047"),
    "aphram": ("paper", "📄 Aphram G, et al. JTCVS Tech 2021（Brussels en bloc 変法）",
               "Aphram G, Jahanyar J, de Kerchove L, El Khoury G. JTCVS Tech 2021;9:25-7"),
    "kim13": ("paper", "📄 Kim SW, et al. Ann Thorac Surg 2013（Samsung Seoul n=30）",
              "Kim SW, Park PW, Kim WS, Sung K, Lee YT, Jun TG, Jeong DS. "
              "Ann Thorac Surg 2013;95:635-41"),
    "matsu": ("paper", "📄 Matsuzaki K, et al. Interdiscip Cardiovasc Thorac Surg 2024（日本・変法）",
              "Matsuzaki K, Mitomi K, Imai A, Sato M, Watanabe Y. "
              "Interdiscip Cardiovasc Thorac Surg 2024;38:ivad213"),
    "yajima": ("paper", "📄 Yajima S, et al. Eur J Cardiothorac Surg 2022（patch-sparing 変法）",
               "Yajima S, Sakashita Y, Sekiya N, Sakaguchi T. "
               "Eur J Cardiothorac Surg 2022;62:ezac405"),
    "vz": ("paper", "📄 von Zeppelin M, et al. Medicina 2026（Frankfurt, CC BY）",
           "von Zeppelin M, Winter A, Emrich F, et al. Medicina 2026;62(1):33"),
    "vob": ("paper", "📄 Vobornik M, et al. Front Cardiovasc Med 2023（Hradec Králové, CC BY）",
            "Vobornik M, Timbilla S, Gofus J, et al. Front Cardiovasc Med 2023;10:1154129"),
    "iac": ("paper", "📄 Iaccarino A, et al. J Clin Med 2023（Humanitas, CC BY）",
            "Iaccarino A, Barbone A, Basciu A, et al. J Clin Med 2023;12:5891"),
    "jarral": ("paper", "📄 Jarral OA, et al. JTCVS Tech 2024（TAVR-IE → Commando）",
               "Jarral OA, Pupovac SS, Tseng JC, et al. JTCVS Tech 2024;27:72-5"),
    "rheault": ("paper", "📄 Rheault-Henry M, Chu MWA. JTCVS Tech 2025（緊急 hemi-Commando）",
                "Rheault-Henry M, Chu MWA. JTCVS Tech 2025;32:81-3"),
    "nosaka": ("paper", "📄 Nosaka Y, et al. Interdiscip Cardiovasc Thorac Surg 2024（石川・緊急）",
               "Nosaka Y, Kato H, No H. Interdiscip Cardiovasc Thorac Surg 2024;38:ivad207"),
    "simpson": ("paper", "📄 Simpson MT, et al. Eur J Cardiothorac Surg 2023（Commando 後の解剖）",
                "Simpson MT, Kachel M, Mirza F, et al. Eur J Cardiothorac Surg 2023;64:ezad155"),
    "bojko": ("paper", "📄 Bojko M, et al. Semin Thorac Cardiovasc Surg 2024（USC n=41）",
              "Bojko M, Hershenhouse KS, Elsayed RS, et al. "
              "Semin Thorac Cardiovasc Surg 2024;36:158-66"),
}

FIGS = [
    # ================= 2-1  AMC の構造 =================
    dict(name="vob_f02.jpg", src="vob", sec="2-1",
         ref="FIGURE 2 ／ p.4",
         alt="Manouguian-Guiraudon 併用アプローチでLVOTと左右心房を見下ろした術中写真。AML基部・RCA・LCA が標識され、緑矢印が aorto-mitral curtain の穿孔を示す",
         title="FIGURE 2 ／ p.4",
         body="<strong>AMC が「どこにあるか」を一枚で示す術中写真。</strong>"
              "Manouguian–Guiraudon 併用アプローチで LVOT と左右心房を見下ろした視野。"
              "<strong>AML</strong>（前尖）基部の直上、<strong>RCA</strong> と <strong>LCA</strong> 起始部に挟まれた領域が "
              "aortomitral curtain であり、緑矢印はその<mark>穿孔</mark>を指している。"
              "本文 2-1 の「IVF＝僧帽弁周径の前方 1/3」がどの範囲を指すか、この視野で確認できる。",
         cite="FIGURE 2, p.4"),

    dict(name="yi_f05.jpg", src="yi", sec="2-1",
         ref="Fig. 5 ／ p.572",
         alt="aorto-mitral continuity を開いた視野の術中写真。左房天蓋・大動脈弁・僧帽弁輪・前尖・後尖・中隔・右房が標識されている",
         title="Fig. 5 ／ p.572",
         body="<strong>AMC を縦切開して開いた視野。</strong>"
              "本文 6章 Step 1 の「非冠尖〜左冠尖交連付近で IVF を切開し僧帽弁へのアクセス路を形成」した状態にあたる。"
              "原著の説明では、AMC を開く際は<strong>ハサミの一方の刃を左房内、他方を左室内に入れる</strong>。"
              "大動脈弁（AOV）・前尖（AML）・後尖（PML）・左房天蓋が一続きの術野になることが読み取れる。",
         cite="Fig. 5, p.572"),

    dict(name="simpson_f03.jpg", src="simpson", sec="2-1",
         ref="Figure 3 ／ p.5",
         alt="CTで aortomitral angle と aortomitral curtain 長、僧帽弁輪面積を計測した画面",
         title="Figure 3 ／ p.5",
         body="<strong>AMC は「計測できる」構造である。</strong>"
              "(A) <strong>aortomitral angle（AMA）</strong>と<strong>AMC 長</strong>、(B) 僧帽弁輪面積の計測画面。"
              "同シリーズでは <mark>AMC が長いほど AMA は小さくなる（Spearman ρ = −0.929）</mark>という強い逆相関が示されており、"
              "Commando で AMC をどれだけの長さで再建したかが、将来の VIV-TAVI／TMVR の可否に直結する（→ 11-3）。",
         cite="Figure 3, p.5"),

    # ================= 2-2  IVF 破壊の病態 =================
    dict(name="iac_f04.jpg", src="iac", sec="2-2",
         ref="Figure 4 ／ p.11 of 16",
         alt="機械弁二弁IEにおける aortomitral curtain 離断。1,2 は経食道心エコーで上行大動脈から左房へのジェット、3 は大動脈切開創から見た離断部（黒い空洞）",
         title="Figure 4 ／ p.11 of 16",
         body="<strong>「AMC 離断」が画像と術野でどう見えるか。</strong>"
              "機械弁二弁置換後 IE の症例。(1)(2) の TEE では<strong>上行大動脈から左房への交通とジェット</strong>が描出され、"
              "(3) の大動脈切開創からは離断した AMC が<mark>黒い空洞（black hole）</mark>として見える。"
              "本文 2-2 の「傍弁輪漏（PVL）→ 空洞性欠損 → 両弁輪破壊」という進行の終末像にあたる。",
         cite="Figure 4, p.11 of 16"),

    dict(name="vob_f01.jpg", src="vob", sec="2-2",
         ref="FIGURE 1 ／ p.2",
         alt="二弁心内膜炎患者の経食道心エコー。緑矢印が aorto-mitral curtain の穿孔を示す",
         title="FIGURE 1 ／ p.2",
         body="<strong>術前 TEE での AMC 穿孔（緑矢印）。</strong>"
              "(A) 2D、(B) カラードプラ。本文 5-1 が TEE を「必須」に置く根拠がこの一枚で、"
              "左房と左室流出路の間に<strong>本来存在しないシャント</strong>が描出されている。",
         cite="FIGURE 1, p.2"),

    dict(name="vob_f03.jpg", src="vob", sec="2-2",
         ref="FIGURE 3 ／ p.4",
         alt="穿孔した aortomitral curtain を根治的に切除した後の術中写真。両線維三角にかけた縫合糸を緑矢印が示す",
         title="FIGURE 3 ／ p.4",
         body="<strong>デブリードマン後の「欠損の大きさ」。</strong>"
              "穿孔した AMC を根治的に切除した直後の視野で、AML はごく一部（residue）しか残っていない。"
              "緑矢印は<strong>両線維三角にかけた支持糸</strong>で、ここが再建パッチのアンカー点になる。"
              "本文 7-1 が「左線維三角の無張力再建」を最重要 Pitfall とする理由——"
              "<mark>この欠損を張力なく埋めるには generous なパッチが要る</mark>——が視覚的に理解できる。",
         cite="FIGURE 3, p.4"),

    dict(name="jarral_f01.jpg", src="jarral", sec="2-2",
         ref="FIGURE 1 ／ p.74",
         alt="TAVR後心内膜炎における aortomitral curtain の広範な破壊を示す術中写真",
         title="FIGURE 1 ／ p.74",
         body="<strong>AMC の広汎破壊（TAVR-IE 症例）。</strong>"
              "本文 3-1 が Commando の絶対適応とする「IVF/AMC 破壊」の実像。"
              "弁輪間の線維性骨格が消失し、大動脈弁輪と僧帽弁輪が連続性を失っているため、"
              "<mark>どちらか一方の弁だけを置換しても縫合する土台が残らない</mark>。",
         cite="FIGURE 1, p.74"),

    dict(name="yi_f04.jpg", src="yi", sec="2-2",
         ref="Fig. 4 ／ p.571",
         alt="部分的に破壊された aorto-mitral curtain の術中写真と、心膜パッチで補強した前僧帽弁輪",
         title="Fig. 4 ／ p.571",
         body="<strong>「全破壊」ではない AMC —— 菲薄・脆弱で再建を要する段階。</strong>"
              "(a) <strong>部分的に破壊された AMC</strong>（黄色破線）と左右冠動脈・大動脈弁輪の位置関係、"
              "(b) 前僧帽弁輪を<strong>心膜パッチで補強</strong>した状態。"
              "破壊が全周に及ばない症例では、Commando より侵襲の小さい "
              "<em>patch reconstruction without posterior extension</em> が選択肢になる"
              "（Zaki A, et al. JTCVS Tech 2023;22:181-4；本図は Yi 2025 が同論文から転載したもの）。",
         cite="Fig. 4, p.571"),

    # ================= 3-1  適応（AATS 推奨表） =================
    dict(name="aats_f02_indications.png", src="aats", sec="3-1",
         ref="Figure 2 ／ p.634（PDF p.5）",
         alt="AATS 2016 IEガイドラインの推奨表：手術適応と手術タイミングの COR / LOE 一覧",
         title="Figure 2 ／ p.634（PDF p.5）",
         body="<strong>本文 3-1 の適応表はこの原典から取り直した。</strong>"
              "上段が「手術適応」、下段が「手術時期」。<strong>Class I</strong> は "
              "①弁機能不全による心不全、②<em>S. aureus</em>・真菌・高度耐性菌による左心系 IE、"
              "③<mark>房室ブロック・弁輪部/大動脈膿瘍・破壊性穿通性病変</mark>、④持続感染 の 4 項目のみ。"
              "旧版の本文が Class I としていた「繰り返す塞栓」は実際には <strong>Class IIa</strong>、"
              "「可動性疣贅 >10 mm」は<strong>塞栓所見を伴って Class IIb</strong> である——"
              "この表の COR 列で直接照合できる。Commando の対象病変（③）は Class I に含まれる。",
         cite="Figure 2, p.634"),

    # ================= 4-1  術式分類 =================
    dict(name="forteza_f01.jpg", src="forteza", sec="4-1",
         ref="Figure 1 ／ p.3",
         alt="Commando 系術式の 2×2 分類図。縦軸が僧帽弁置換の有無、横軸が大動脈基部置換の有無で、hemi-Commando / Commando / Root-hemicommando / Root-Commando の4型に分かれる",
         title="Figure 1 ／ p.3",
         body="<strong>4 つの術式名を 2 軸で整理した分類図。</strong>"
              "縦軸＝<strong>僧帽弁置換の有無</strong>、横軸＝<strong>大動脈基部置換の有無</strong>。"
              "MVR なし × 基部置換なし＝<em>hemi-Commando</em>、MVR あり × 基部置換なし＝<em>Commando</em>、"
              "基部置換ありの 2 型がそれぞれ <em>Root-hemicommando</em> / <em>Root-Commando</em>。"
              "Barcelona の集計では下段（<mark>Root 群 30 例 vs Non-ROOT 群 48 例</mark>）で"
              "院内死亡・中期生存に有意差はなかった（→ 10-1）。本文 4-1 のアルゴリズムはこの 2 軸に対応する。",
         cite="Figure 1, p.3"),

    # ================= 5-1  術前評価 =================
    dict(name="rheault_f01.jpg", src="rheault", sec="5-1",
         alt="術前TEEとCT：大動脈弁疣贅（赤矢印）、大きな大動脈基部膿瘍（黄矢印）、AMCと中心線維三角の破壊、高度の大動脈弁・僧帽弁逆流",
         ref="FIGURE 1 ／ p.82",
         title="FIGURE 1 ／ p.82",
         body="<strong>本文 5-1 の必須検査（TEE＋心臓 CT）が実際に何を写すか。</strong>"
              "A：TEE で<strong>大動脈弁疣贅（赤矢印）</strong>と<mark>大きな大動脈基部膿瘍（黄矢印）</mark>、"
              "AMC と中心線維三角の破壊。B：高度の大動脈弁・僧帽弁逆流。"
              "C・D：CT で複数の疣贅と基部膿瘍の広がり、および<strong>実測径</strong>。"
              "膿瘍の位置・深さと His 束との距離は、この段階で完全 AVB リスク（→ 11-2）の予測に使う。",
         cite="FIGURE 1, p.82"),

    dict(name="aats_f03_workup.png", src="aats", sec="5-1",
         ref="Figure 3 ／ p.635（PDF p.6）",
         alt="AATS 2016 IEガイドラインの推奨表：神経学的合併症・術前脳画像・抗凝固管理の COR / LOE 一覧",
         title="Figure 3 ／ p.635（PDF p.6）",
         body="<strong>術前ワークアップ（とくに脳）の推奨。</strong>"
              "本文 5-1 が「脳 MRI/CT を必須」とする根拠が最上段で、"
              "<strong>神経症状のある IE 患者には脳画像を Class I</strong>、"
              "左心系 IE では無症状でもスクリーニングが Class IIa。"
              "タイミングについては<mark>頭蓋内出血の既往例で 3 週以上の待機が妥当（Class IIa）</mark>と明記されており、"
              "本文 5-2 の「脳卒中合併例」行はこの記載に合わせて改めた。"
              "ヘパリンは脳出血所見があれば一時中止（Class I）。",
         cite="Figure 3, p.635"),

    # ================= 6  手技：デブリードマンまで =================
    dict(name="yi_f01.png", src="yi", sec="6-3",
         ref="Fig. 1 ／ p.568",
         alt="Commando 手術の線画。斜方大動脈切開を僧帽弁輪と左房天蓋へ延長し、両弁を切除、僧帽弁人工弁を後方弁輪とパッチ上縁に固定する一連の図",
         title="Fig. 1 ／ p.568",
         body="<strong>Commando の全体像を示す古典的な線画（a→b→c）。</strong>"
              "a：<strong>斜方大動脈切開を僧帽弁輪および左房天蓋へ延長</strong>し、大動脈弁と僧帽弁を切除。"
              "b：僧帽弁人工弁を<mark>後方は弁輪へ、上方（前方 1/3）はパッチへ</mark>固定する——"
              "本文 6章 Step 5 の「前方 1/3 は IVF パッチ縫合糸が MVP 縫合輪を貫通」に対応。"
              "c：大動脈弁を再建 IVF パッチ前翼に縫合し、パッチ下葉で左房天蓋を閉じる。",
         cite="Fig. 1, p.568"),

    dict(name="navia19_f01.jpg", src="navia19", sec="6-3",
         ref="Figure 1（A–F）／ p.1315",
         alt="Commando 手術の術中写真6枚と対応する模式図：左房天蓋の開放、LVOT の観察、僧帽弁置換、心膜パッチによるIVF再建、左房天蓋閉鎖、大動脈基部再建",
         title="Figure 1（A–F）／ p.1315",
         body="<strong>本文 6章 Step 1–7 に一対一で対応する術中写真（Cleveland Clinic）。</strong>"
              "A 左房天蓋を大動脈基部へ向けて開放 → B 左房と LVOT を観察 → "
              "C <strong>僧帽弁置換</strong> → D <strong>心膜パッチによる IVF 再建</strong>"
              "（<mark>僧帽弁人工弁の一部が IVF パッチに縫合されている</mark>点に注目）→ "
              "E 大動脈弁置換後に<strong>ダイヤ型パッチの下半分</strong>で左房天蓋を閉鎖"
              "（大動脈人工弁の一部も IVF パッチに縫合）→ F <strong>上半分</strong>で大動脈基部を再建。"
              "本文 6章 Step 5 の「MVR → IVF 再建 → AVR」の順序と、"
              "「下葉＝左房天蓋／上葉＝大動脈基部」というダブルレイヤーパッチの使い分けが、この 6 枚で確認できる。",
         cite="Figure 1, p.1315"),

    # ================= 6-4  AMC / IVF 再建 =================
    dict(name="vz_f02.jpg", src="vz", sec="6-4",
         ref="Figure 2（A, B）／ p.3 of 14",
         alt="Commando 手技の模式図。A は左房と左室流出路の視野、B は生体弁を植え込んだ僧帽弁",
         title="Figure 2（A, B）／ p.3 of 14",
         body="<strong>切除範囲と「僧帽弁を先に置く」順序。</strong>"
              "A：感染大動脈弁・大動脈基部・左房天蓋・AML 基部を切除して<strong>IVF を完全に切除</strong>した視野。"
              "原著は<mark>健常組織まで 3〜5 mm の安全域をつけて切除</mark>し、"
              "同時に膿瘍腔を左室へドレナージさせると明記している。"
              "B：<strong>僧帽弁人工弁をまず後方弁輪に植え込む</strong>——本文 Step 5 の「MVR が先」に対応。",
         cite="Figure 2, p.3 of 14"),

    dict(name="vz_f03.jpg", src="vz", sec="6-4",
         ref="Figure 3（A–C）／ p.4 of 14",
         alt="Commando 手技の模式図。A はウシ心膜パッチによるIVF再建、B は大動脈弁置換後の左房天蓋再建、C は大動脈基部再建",
         title="Figure 3（A–C）／ p.4 of 14",
         body="<strong>再建の 3 ステップ（本文 Step 4→6→7）。</strong>"
              "A：<strong>ウシ心膜パッチで IVF を再建</strong>し、その<mark>前方部分を僧帽弁人工弁に縫い込む</mark>。"
              "B：大動脈弁置換を済ませてから<strong>左房天蓋を再建</strong>。C：<strong>大動脈基部を再建</strong>。"
              "本文が「下葉＝左房天蓋／上葉＝大動脈基部」と記述する使い分けが、A→B→C の順で図示されている。",
         cite="Figure 3, p.4 of 14"),

    dict(name="kim13_f02.png", src="kim13", sec="6-4",
         ref="Fig 2（A–E）／ p.638",
         alt="aortomitral fibrous body 再建の詳細模式図。ウシ心膜パッチの幅3〜3.5cm、上葉5〜6cm・下葉3cmへの分割、everting 縫合または3-0 polypropylene 連続縫合",
         title="Fig 2（A–E）／ p.638",
         body="<strong>パッチの実寸が書かれた唯一の図。</strong>"
              "僧帽弁人工弁を後方弁輪に固定したのち (B) <strong>Teflon プレジェット付き everting 縫合</strong>、"
              "または (B′) <strong>3-0 polypropylene 連続縫合</strong>で人工弁前方をパッチ中央に固定する。"
              "この縫合線がパッチを<mark>上葉 5〜6 cm・下葉 3 cm、幅 3〜3.5 cm</mark>に分割する。"
              "本文 Step 4 の「generous size で裁断」が具体的に何 cm を指すのか、ここで確認できる。",
         cite="Fig 2, p.638"),

    dict(name="kim13_f01.jpg", src="kim13", sec="6-4",
         ref="Fig 1（A–D）／ p.637",
         alt="ウシ心膜パッチによる僧帽弁輪再建・全周性大動脈弁輪再建・人工弁縫合・ダブルレイヤーの術中写真4枚",
         title="Fig 1（A–D）／ p.637",
         body="<strong>同じ手技の術中写真（Samsung Seoul, n=30）。</strong>"
              "A：人工弁抜去と aortomitral fibrous body 離断ののち<strong>ウシ心膜で僧帽弁輪を再建</strong>（矢印）。"
              "B：<strong>全周性の大動脈弁輪再建</strong>（矢印）。C：人工弁植込みのための僧帽弁縫合。D：ダブルレイヤー。"
              "本シリーズは<mark>院内死亡 6.7%</mark>と本文 10-1 の表中で最良の成績を示している（→ 10-1）。",
         cite="Fig 1, p.637"),

    # ================= 6-7  洗浄・閉鎖・術中管理 =================
    dict(name="aats_f06_intraop.png", src="aats", sec="6-7",
         ref="Figure 6 ／ p.639（PDF p.10）",
         alt="AATS 2016 IEガイドラインの推奨表：術中管理の具体的検討事項（人工物の除去、ペースメーカー抜去、機械弁の回避、生理食塩水洗浄、標本の取り扱い、術後抗菌薬）の COR / LOE 一覧",
         title="Figure 6 ／ p.639（PDF p.10）",
         body="<strong>Commando の術中判断のうち、ガイドラインが Class を与えている項目。</strong>"
              "本文の複数の節がこの 1 枚に集約されている——"
              "6章 Step 7 の洗浄＝<mark>「デブリードマン完了後の術野の generous な生理食塩水洗浄」Class I</mark>、"
              "8-1 の機械弁＝<strong>「頭蓋内出血・広範脳梗塞例、重症で術後経過遷延が予想される例では機械弁を避ける」Class I</strong>、"
              "11-1 の抗菌薬＝<strong>「活動性 IE 術後の静注は 6 週間、起算は手術日」Class IIa</strong>／真菌性 IE は生涯経口抑制（Class IIa）。"
              "感染が証明されていない人工物・血管グラフトも <em>S. aureus</em>／真菌なら摘出が妥当（Class IIa）。",
         cite="Figure 6, p.639"),

    # ================= 7  Pitfalls =================
    dict(name="iac_f03.jpg", src="iac", sec="7",
         ref="Figure 3 ／ p.11 of 16",
         alt="機械弁大動脈弁心内膜炎で人工弁を摘出した際に判明した大動脈弁輪の侵食と膿瘍の術中写真",
         title="Figure 3 ／ p.11 of 16",
         body="<strong>「人工弁を抜いて初めて分かる」弁輪破壊。</strong>"
              "機械弁 PVE で人工弁を摘出した瞬間に判明した<mark>弁輪の侵食と膿瘍</mark>。"
              "本文 4-1 が「最終判断は術中所見による」とする理由がこれで、"
              "術前 TEE/CT で hemi-Commando を計画していても、この所見が出れば Full Commando へ切り替える。"
              "原著は、こうした症例では<strong>人工弁を縫着する土台が残らず、左室−大動脈連続性が失われうる</strong>と述べている。",
         cite="Figure 3, p.11 of 16"),

    dict(name="rheault_f02.jpg", src="rheault", sec="7",
         ref="FIGURE 2（A–D）／ p.82",
         alt="術中写真：巨大な大動脈周囲膿瘍腔、膿瘍による左房天蓋と僧帽弁前尖の侵食、4-0 PROLENE 結節縫合による前尖・中心線維三角再建、3-0 PROLENE による大動脈基部再建",
         title="FIGURE 2（A–D）／ p.82",
         body="<strong>Pitfall #1「左線維三角の無張力再建」を、糸の号数まで含めて示す 4 枚。</strong>"
              "A：<strong>巨大な大動脈周囲膿瘍腔</strong>（白矢印）。B：膿瘍による<mark>左房天蓋（黄矢印）と AML（白矢印）の侵食</mark>。"
              "C：<strong>4-0 PROLENE 結節縫合</strong>で AML と<strong>中心線維三角</strong>を再建。"
              "D：<strong>3-0 PROLENE</strong> で大動脈基部を再建。"
              "本文 7-1 が「離脱後は修復不能」とする部位が、まさに C の縫合線である。",
         cite="FIGURE 2, p.82"),

    # ================= 8-1  弁選択 =================
    dict(name="navia19_f05.jpg", src="navia19", sec="8-1",
         ref="Figure 5（A, B）／ p.1322",
         alt="再発心内膜炎回避率のKaplan-Meier曲線。A は hemi-Commando と Commando の層別、B は allograft と non-allograft の層別",
         title="Figure 5（A, B）／ p.1322",
         body="<strong>「同種移植片は感染再発を減らすのか」への直接の答え。</strong>"
              "B が <strong>allograft 群 vs non-allograft 群</strong>の再発 IE 回避率で、"
              "<mark>両群の曲線はほぼ重なり、明らかな差は示されていない</mark>。"
              "本文 8-1 の「弁種による感染再発率・死亡率は同等」という記述は、この層別解析に裏打ちされている。"
              "A は hemi-Commando（赤・破線）と Commando（青・実線）の層別。"
              "同種移植片の優位性は<strong>不整形弁輪への適合性と止血の容易さ</strong>にあり、抗菌特性は決め手ではない。",
         cite="Figure 5, p.1322"),

    # ================= 9-1  hemi-Commando =================
    dict(name="navia23_f01.jpg", src="navia23", sec="9-1",
         ref="FIGURE 1（A–F）／ p.89",
         alt="hemi-Commando の模式図6枚：aortomitral continuity と IVF の切除、大動脈同種移植片の準備、デブリードマン、homograft 前尖の native 前尖への縫合、移植片の植込み、左房天蓋のパッチ閉鎖",
         title="FIGURE 1（A–F）／ p.89",
         body="<strong>hemi-Commando の 6 ステップ（Cleveland Clinic 公式図）。</strong>"
              "A–C：<strong>aortomitral membrane・上行大動脈・AML を含めて aortomitral continuity と IVF を一塊で切除</strong>し、"
              "大動脈同種移植片を準備。D–F：<mark>homograft の AML を native AML 遊離縁に縫合</mark>して IVF と AML を同時に再建、"
              "僧帽弁輪形成リングを置き、左房天蓋をパッチで閉じる。"
              "本文 9-1 の「AML 遊離縁（coaptation zone）＝腱索付着部は温存」がなぜ成立するか——"
              "<strong>切除するのは近位帯状ゾーンだけ</strong>——が D で確認できる。",
         cite="FIGURE 1, p.89"),

    dict(name="navia19_f02.jpg", src="navia19", sec="9-1",
         ref="Figure 2（A–F）／ p.1316",
         alt="hemi-Commando の術中写真6枚：感染機械弁の露出、デブリードマン後のLVOTとAML、僧帽弁輪形成リング留置、allograft AML の native AML への植込み、大動脈同種移植片残周の LVOT への植込み、心膜パッチによる左房天蓋閉鎖",
         title="Figure 2（A–F）／ p.1316",
         body="<strong>同じ 6 ステップの術中写真。</strong>"
              "A：感染した<strong>機械弁大動脈弁</strong>を露出。B：デブリードマン後の LVOT と AML。"
              "C：<mark>僧帽弁輪形成リングの留置</mark>——本文 9-1 の「不完全弁輪形成術リングで AML 過可動・SAM を防止（施行率 36%）」に対応。"
              "D：allograft AML を native AML に植込み。E：大動脈同種移植片の残周を LVOT へ。"
              "F：心膜パッチで左房天蓋を閉鎖し、同種移植片に縫着。",
         cite="Figure 2, p.1316"),

    dict(name="marin_f02.jpg", src="marin", sec="9-1",
         ref="Figure 2（A–D）／ p.4",
         alt="Leipzig 版 hemi-Commando の模式図4枚：大動脈基部・左房天蓋・大動脈僧帽弁接合部・前尖基部の en bloc 切除、折り返したウシ心膜パッチによる前僧帽弁輪・前尖再建、根部置換後のLVOT再建、単一心膜パッチによる左房天蓋閉鎖",
         title="Figure 2（A–D）／ p.4",
         body="<strong>同種移植片が手に入らない施設のための hemi-Commando。</strong>"
              "A：大動脈基部・左房天蓋・大動脈僧帽弁接合部・AML 基部の合流部を <strong>en bloc 切除</strong>し、"
              "<mark>AML 遊離縁のみ温存</strong>。B：<strong>ウシ心膜パッチを二つ折りにして</strong>前僧帽弁輪と前尖を再建"
              "（本文 8-1 の「グルタルアルデヒド固定ウシ心膜を折りたたんで二重層使用」）。"
              "C：根部置換後、人工弁/グラフトを大動脈弁輪・neo-LVOT・<strong>パッチ前肢</strong>の 3 点に固定。"
              "D：単一心膜パッチで左房天蓋を閉鎖。",
         cite="Figure 2, p.4"),

    dict(name="vob_f04.jpg", src="vob", sec="9-1",
         ref="FIGURE 4 ／ p.4",
         alt="僧帽弁前尖を付けたまま採取した大動脈同種移植片。緑矢印が前尖、両線維三角に糸がかかっている",
         title="FIGURE 4 ／ p.4",
         body="<strong>hemi-Commando の主役——AML 付き大動脈同種移植片。</strong>"
              "緑矢印が<strong>温存された僧帽弁前尖</strong>で、両線維三角に糸がかかった状態。"
              "この 1 枚の組織で<mark>大動脈弁・大動脈基部・IVF・AML を一括して置換できる</mark>ことが、"
              "本文 9-1 が hemi-Commando を「AML 限局浸潤の第 1 選択」とする理由である。",
         cite="FIGURE 4, p.4"),

    dict(name="navia10_c.png", src="navia10", sec="9-1",
         ref="FIGURE 1 ／ p.1078",
         alt="採取された aortomitral homograft の線画。大動脈基部に連続して僧帽弁前尖が付いている",
         title="FIGURE 1 ／ p.1078",
         body="<strong>hemi-Commando 原型（2010）の homograft。</strong>"
              "大動脈基部に僧帽弁前尖が連続したまま採取されている。"
              "原著は移植前に<strong>僧帽弁輪サイザーで三角間距離と前尖高を実測</strong>し、"
              "<mark>再建後も同じ距離・高さになるよう trimming する</mark>と述べている——"
              "過剰なら逸脱、不足なら牽引となるため。本文 7-2 Pitfall #6（SAM）#7（遅発性 MR）の根源にあたる手順。",
         cite="FIGURE 1, p.1078"),

    dict(name="navia10_b.png", src="navia10", sec="9-1",
         ref="FIGURE 3 ／ p.1078",
         alt="感染組織を完全に除去した後の術者視野の線画。大動脈弁輪と僧帽弁前尖基部が連続した欠損になっている",
         title="FIGURE 3 ／ p.1078",
         body="<strong>デブリードマン完了時の術者視野。</strong>"
              "本文 6章 Step 3 の「正常組織が露出するまで」を達成した状態で、"
              "大動脈弁輪から AML 基部までが<strong>一続きの欠損</strong>になっている。"
              "この欠損形状が、hemi-Commando で AML 付き homograft を選ぶ根拠そのものである。",
         cite="FIGURE 3, p.1078"),

    dict(name="navia10_d.png", src="navia10", sec="9-1",
         ref="FIGURE 4 ／ p.1079",
         alt="aortomitral homograft 植込みの線画その1。homograft 前尖を native 前尖に連続縫合している",
         title="FIGURE 4 ／ p.1079",
         body="<strong>植込み①——homograft AML を native AML へ。</strong>"
              "本文 9-1 の「trimmed した homograft AML を native AML 遊離縁に "
              "<strong>3-0 Prolene 連続縫合</strong>」に対応する縫合線。"
              "組織が脆弱な症例では、原著は<mark>ウシ心膜ストリップで近位縫合線を補強</mark>する。",
         cite="FIGURE 4, p.1079"),

    dict(name="navia10_e.png", src="navia10", sec="9-1",
         ref="FIGURE 5 ／ p.1079",
         alt="aortomitral homograft 植込みの線画その2。移植片を左室流出路の全周へ固定している",
         title="FIGURE 5 ／ p.1079",
         body="<strong>植込み②——LVOT 全周への固定。</strong>"
              "AML 側の縫合を終えたのち、移植片の残る円周を LVOT へ縫着する。"
              "本文 7-1 の無張力 3 条件のうち「再建 IVF＋左線維三角が心室側壁筋から大動脈弁輪まで無張力」は、"
              "この縫合線の張力配分で決まる。",
         cite="FIGURE 5, p.1079"),

    dict(name="navia10_f.png", src="navia10", sec="9-1",
         ref="FIGURE 6 ／ p.1079",
         alt="aortomitral homograft 植込みの線画その3。左房天蓋を閉鎖し、大動脈側の吻合を完成させた全体像",
         title="FIGURE 6 ／ p.1079",
         body="<strong>植込み③——左房天蓋の閉鎖と完成像。</strong>"
              "左房を閉じ、大動脈側の遠位吻合を完成させた全体像。"
              "本文 6章 Step 8 の「離脱前止血確認」が必要な部位——"
              "<mark>離脱後は lateral trigone 再建部に外科的アクセスができない</mark>——は、"
              "この状態でもう左房の背側に隠れている。",
         cite="FIGURE 6, p.1079"),

    dict(name="navia10_a.png", src="navia10", sec="9-1",
         ref="FIGURE 2 ／ p.1078",
         alt="術前経食道心エコー。僧帽弁前尖上の疣贅と肥厚を示す",
         title="FIGURE 2 ／ p.1078",
         body="術前 TEE。<strong>僧帽弁前尖上の疣贅と肥厚</strong>が描出されており、"
              "本文 9-1 の hemi-Commando 適応条件③「MR が AML 病変のみ」に合致する所見。"
              "後尖・腱索・後方弁輪に病変が及んでいないことの確認が、Full Commando との分岐点になる。",
         cite="FIGURE 2, p.1078"),

    dict(name="elg_f02.jpg", src="elg", sec="9-1",
         ref="Figure 2（A, B）／ p.1059",
         alt="術前後の経食道心エコー。A は大動脈基部膿瘍とIVF・前尖基部の肥厚、B は aortomitral homograft 植込み後で黄色矢印が native 前尖と homograft 前尖の縫合線を示す",
         title="Figure 2（A, B）／ p.1059",
         body="<strong>再建が「エコーでどう見えるか」。</strong>"
              "A：術前——<strong>大動脈基部膿瘍（Abs）</strong>と IVF・AML 基部の肥厚。"
              "B：術後——<mark>黄色矢印が native AML と homograft AML の縫合線</mark>。"
              "本文 11-3 の術後エコー評価項目「IVF 再建の完全性」を判定する際に探すべき所見がこれで、"
              "この縫合線に沿った異常交通がなければ再建は完全と判断できる。",
         cite="Figure 2, p.1059"),

    # ================= 9-3  En bloc（Brussels） =================
    dict(name="aphram_f01.jpg", src="aphram", sec="9-3",
         ref="FIGURE 1（A–D）／ p.26",
         alt="en bloc 大動脈基部切除の術中写真4枚。冠動脈の授動と保護、非/左冠尖交連からの反時計回りの切除、非/右冠尖交連背側の剥離、ハサミによる切除完了",
         title="FIGURE 1（A–D）／ p.26",
         body="<strong>Brussels 変法の核心——切除の順番。</strong>"
              "A：<mark>最初で最重要のステップは冠動脈（矢印：前方の RCA、後方の LCA）を授動して保護すること</mark>。"
              "B：切除は<strong>非/左冠尖交連から開始し反時計回りに</strong>進め、剥離は交連の外側で LVOT へ向かい、"
              "<strong>交連自体を標本に含める</strong>。C：非/右冠尖交連の背側へ剥離を続行。D：ハサミで切除完了。"
              "本文 7-2 Pitfall #11「冠動脈再吻合困難」の対策が「冠動脈ボタン先行移動」である理由が A で分かる。",
         cite="FIGURE 1, p.26"),

    # ================= 9-4  Patch-sparing（Yajima） =================
    dict(name="yajima_f01.jpg", src="yajima", sec="9-4",
         ref="Figure 1（A–F）／ p.2",
         alt="patch-sparing AMC 再建の模式図6枚：多発仮性動脈瘤を伴う感染大動脈基部、感染AMCと前僧帽弁輪、既存機械弁とAMCの摘出、supra-annular な新機械弁植込みと自己組織による走行縫合、新しいAMC、ウシ心膜ストリップで補強したコンポジットグラフトの縫着",
         title="Figure 1（A–F）／ p.2",
         body="<strong>人工パッチを一切使わない AMC 再建。</strong>"
              "A：<strong>多発仮性動脈瘤</strong>を伴う感染大動脈基部・弁輪。B：感染した AMC と前僧帽弁輪。"
              "C：既存機械弁と AMC の摘出。D：<mark>新しい機械弁を supra-annular に植え込み、縫合輪の 2/3 を後方弁輪に沿わせ、"
              "前方弁輪と AMC は自己組織の走行縫合のみで処理</mark>。E：こうしてできた「新しい AMC」。"
              "F：コンポジットグラフトを再建自己 AMC に縫着し、<strong>ウシ心膜ストリップで補強</strong>。"
              "本文 9-4 の「MVP をワンサイズ小さく」という注意は、D の supra-annular 配置に由来する。",
         cite="Figure 1, p.2"),

    # ================= 9-5  Aorto-annulo-septotomy（Matsuzaki） =================
    dict(name="matsu_f01.jpg", src="matsu", sec="9-5",
         ref="Figure 1 ／ p.2",
         alt="aorto-annulo-septotomy の大動脈・右房切開線を従来アプローチと対比した模式図。左が本法、右が従来法",
         title="Figure 1 ／ p.2",
         body="<strong>切開線が従来法とどう違うか。</strong>"
              "左が aorto-annulo-septotomy、右が従来アプローチ。"
              "本法は<mark>左房天蓋切開を省き、卵円窩から垂直に心房中隔を切開して右房側から到達</mark>する。"
              "原著は<strong>左房天蓋切開を最小化すると術中出血合併症が減る</strong>と述べており、"
              "本文 7-2 Pitfall #8（再手術時の出血）への一つの解になっている。禁忌は冠状静脈洞膿瘍。",
         cite="Figure 1, p.2"),

    dict(name="matsu_f02.jpg", src="matsu", sec="9-5",
         ref="Figure 2（A–C）／ p.3",
         alt="術中写真：非冠尖側大動脈弁輪における弁間線維体の穿孔（黄矢印）、aorto-annulo-septotomy と combined annulus の術者視野、2本のバルブサイザーによる combined annulus の計測",
         title="Figure 2（A–C）／ p.3",
         body="<strong>「combined annulus」という概念。</strong>"
              "A：非冠尖側大動脈弁輪における<strong>弁間線維体の穿孔</strong>（黄矢印）。"
              "B：中隔を切開した後の術者視野で、大動脈弁輪と僧帽弁輪が<mark>1 つの「combined annulus」として正面から見える</mark>。"
              "C：<strong>2 本のバルブサイザーで combined annulus を同時に計測</strong>——"
              "本文 9-5 の「複合パッチで同時弁置換・IVF 再建」を実現するための前提操作。",
         cite="Figure 2, p.3"),

    dict(name="matsu_f03.jpg", src="matsu", sec="9-5",
         ref="Figure 3（A, B）／ p.4",
         alt="double valve composite の作製と植込みの模式図、および4層パッチ翼による心房中隔・右房・大動脈の再建",
         title="Figure 3（A, B）／ p.4",
         body="<strong>4 層パッチ翼付き double valve composite。</strong>"
              "A：大動脈弁と僧帽弁を<mark>5 mm 間隔で IFB パッチにより連結し、体外で 1 つのコンポジットに組み上げてから植え込む</mark>。"
              "本文 9-5 の「複合パッチ（ポリエステル＋ウシ心膜）」がこの構造。"
              "B：<strong>4 層のパッチ翼</strong>（1st/2nd bovine pericardium）で心房中隔・右房・大動脈を順に閉鎖する。"
              "体外で組み立てるため、傍弁漏の発生を抑えられるというのが原著の主張。",
         cite="Figure 3, p.4"),

    # ================= 9-6  Chimney / 弁輪拡大への応用 =================
    dict(name="yi_f08.jpg", src="yi", sec="9-6",
         ref="Fig. 8（a–i）／ p.574",
         alt="Chimney Commando の模式図9枚。管状ポリエステル人工血管の内側に僧帽弁人工弁を端から5〜10mmの位置に縫着し、余剰を切除して弁付きコンジットを自作、僧帽弁輪の3/4をコンジットで固定し残り1/4をパッチで再建する",
         title="Fig. 8（a–i）／ p.574",
         body="<strong>本文 9-6「Chimney Commando」の作り方が、この 9 枚で完結する。</strong>"
              "a–c：長さ <strong>3〜4 cm</strong> の管状ポリエステル人工血管の内側に、"
              "<mark>一端から 5〜10 mm の位置に僧帽弁人工弁を縫着</strong>し、余剰を切除して弁付きコンジットを自作。"
              "d–i：<strong>コンジット円周の 3/4 を native 僧帽弁輪にアンカーし、残り 1/4 をパッチで IVF 再建</strong>する"
              "（d–f の “patch”）。人工弁が僧帽弁輪より上方（煙突状）に位置するため、"
              "弁輪を大きく拡大しても LVOT 閉塞を招きにくい——本文が「30 mm 超の弁輪拡大も可能」とする根拠。",
         cite="Fig. 8, p.574"),

    dict(name="yi_f06.jpg", src="yi", sec="9-6",
         ref="Fig. 6（A, B）／ p.573",
         alt="AMC パッチ拡大の模式図と術中写真。パッチによる annular enlargement、左房パッチ、大動脈弁縫合糸が native 弁輪からパッチへ同一水平面で連続する様子",
         title="Fig. 6（A, B）／ p.573",
         body="<strong>Commando の原理を「弁輪拡大」に転用する。</strong>"
              "A：模式図——<mark>大動脈弁の縫合糸が native 弁輪から心膜パッチへ、同一水平面で連続して後方へ延びる</mark>。"
              "この 1 本の縫合線で弁輪が解剖学的レベルで拡大される。B：対応する術中写真（Patch と Mitral Prosthesis）。"
              "本文 3-2 の非 IE 適応「PPM（人工弁患者不適合）——弁輪拡大目的での IVF 切開＋再建」が、この図の内容にあたる。",
         cite="Fig. 6, p.573"),

    dict(name="yi_f07.jpg", src="yi", sec="9-6",
         ref="Fig. 7 ／ p.573",
         alt="大動脈切開が左/非冠尖交連を越えて僧帽弁前尖へ、経中隔切開が上部心房中隔を越えて延び、左室の流入路と流出路が一つの開口になった模式図",
         title="Fig. 7 ／ p.573",
         body="<strong>Double annular enlargement（Marey & Said 法）。</strong>"
              "大動脈切開を<strong>左/非冠尖交連を越えて僧帽弁前尖へ</strong>延ばし、"
              "垂直の経中隔切開を <em>extended Guiraudon</em> アプローチへ移行させて上部心房中隔を越えさせる。"
              "両切開を連結すると<mark>左室の流入路と流出路が 1 つの開口になる</mark>——"
              "Commando の術野展開そのものを、弁輪拡大の手段として使う発想。",
         cite="Fig. 7, p.573"),

    # ================= 10  成績 =================
    dict(name="navia19_f03.jpg", src="navia19", sec="10",
         ref="Figure 3（A, B）／ p.1320",
         alt="術後生存曲線。A は全体、B は hemi-Commando（赤）と Commando（青）の層別。10年で hemi-Commando が上回る",
         title="Figure 3（A, B）／ p.1320",
         body="<strong>本文 10-2 の Key Numbers の出所。</strong>"
              "A：全体（n=138）の生存曲線。B：<mark>hemi-Commando（赤・破線）が Commando（青・実線）を一貫して上回る</mark>。"
              "ただし数字を読むときは注意——これは<strong>術式の優劣ではなく適応の違い</strong>を映している。"
              "hemi-Commando は「後尖・腱索・後方弁輪が温存できる＝破壊が限局した」症例に選ばれるためで、"
              "本文 10-3 が改善策の筆頭に「適応例での hemi-Commando 活用」を挙げるのはこの意味においてである。",
         cite="Figure 3, p.1320"),

    dict(name="navia19_f04.jpg", src="navia19", sec="10",
         ref="Figure 4 ／ p.1321",
         alt="再手術回避率のKaplan-Meier曲線。hemi-Commando（赤・破線）と Commando（青・実線）の層別",
         title="Figure 4 ／ p.1321",
         body="<strong>再手術回避率——生存とは逆の並び。</strong>"
              "生存では優位だった hemi-Commando（赤・破線）が、"
              "<mark>再手術回避では 6 年以降 Commando（青・実線）を下回る</mark>。"
              "本文 7-2 Pitfall #7「遅発性 MR（homograft AML の収縮・線維化）」と 13-1 の未解決課題④が、"
              "この曲線の乖離として現れている。hemi-Commando を選ぶ際に説明すべきトレードオフ。",
         cite="Figure 4, p.1321"),

    dict(name="elg_f03.jpg", src="elg", sec="10",
         ref="Figure 3 ／ p.1060",
         alt="hemi-Commando 37例の全生存Kaplan-Meier曲線と95%信頼区間",
         title="Figure 3 ／ p.1060",
         body="<strong>hemi-Commando 確立論文（n=37）の生存曲線。</strong>"
              "本文 10-1 の「Elgharably 2018／院内死亡 8%」に対応するシリーズ。"
              "<mark>95% 信頼区間（網掛け）が 7 年以降で急激に開く</mark>点に注意——"
              "at risk が 3 例まで減っており、長期成績はこの図からは結論できない。"
              "本文 13-1 が「長期データ」を未解決課題の筆頭に置く理由がここにある。",
         cite="Figure 3, p.1060"),

    dict(name="forteza_f02.jpg", src="forteza", sec="10",
         ref="Figure 2 ／ p.5",
         alt="Commando 系術式を受けた全78例のKaplan-Meier生存曲線。5年で約67%",
         title="Figure 2 ／ p.5",
         body="<strong>Barcelona 2 施設・全 Commando 系術式（n=78）の生存。</strong>"
              "曲線は<mark>術後最初の数か月で急峻に低下し、その後ほぼ平坦</mark>になる——"
              "本文 10-1 の「5 年 67.2%」という数字は、この early hazard を通過した後の水平部分である。"
              "つまり<strong>危険期は手術直後に集中しており、乗り切れば予後は安定する</strong>。"
              "同シリーズは根治的デブリードマンにより <strong>relapse 0%</strong> を達成している（本文 10-3）。",
         cite="Figure 2, p.5"),

    dict(name="forteza_f03.jpg", src="forteza", sec="10",
         ref="Figure 3 ／ p.5",
         alt="ROOT 置換群と Non-ROOT 群の生存曲線の比較。両群はほぼ重なる",
         title="Figure 3 ／ p.5",
         body="<strong>「根部置換を足すと成績は落ちるのか」——落ちない。</strong>"
              "ROOT 群（赤、n=30）と Non-ROOT 群（青、n=48）の生存曲線は<mark>5 年を通じてほぼ重なる</mark>。"
              "本文 9-2 の「ROOT vs non-ROOT で院内死亡・中期生存に有意差なし（共に 1 年 76%、5 年 67%）」が、"
              "この 2 本の曲線そのもの。根部感染があっても<strong>根部置換を追加することを躊躇する理由はない</strong>。",
         cite="Figure 3, p.5"),

    dict(name="kim13_f03.png", src="kim13", sec="10",
         ref="Fig 3 ／ p.639",
         alt="IE群（実線、n=22）と非IE群（点線、n=8）の累積生存曲線。5年で74.6% vs 87.5%、P=0.766",
         title="Fig 3 ／ p.639",
         body="<strong>IE 群と非 IE 群で生存に差はない（P = 0.766）。</strong>"
              "IE 群（実線, n=22）<mark>80.8% → 74.6%</mark>、非 IE 群（点線, n=8）<mark>87.5% → 87.5%</mark>。"
              "本文 10-1 の「Kim 2013／5 年 74.6%（IE 群）」の出所。"
              "ただし非 IE 群 n=8 で <em>P</em> 値は無差を証明しない——"
              "本文 3-2 の非 IE 適応（MAC など）の予後は、より大規模な Kakavand 2024（n=129）で評価すべき。",
         cite="Fig 3, p.639"),

    dict(name="bojko_f03.jpg", src="bojko", sec="10",
         ref="Figure 3（graphical abstract）／ p.165",
         alt="USC シリーズの研究デザインと主要結果のグラフィカルアブストラクト。41例を初回16例と再手術25例に分け、手術死亡34%、1年生存55.4%、再手術例のハザード比4.96",
         title="Figure 3（graphical abstract）／ p.165",
         body="<strong>本文 10-1 で最も高い手術死亡（34.1%）を報告したシリーズの内訳。</strong>"
              "41 例中<mark>25 例（61%）が再手術例</mark>であり、"
              "<strong>再手術例の中期死亡ハザード比は 4.96（95% CI 1.29–19.14, P = 0.013）</strong>。"
              "施設間の死亡率比較（本文 10-1 の表）を読む際は、この<strong>再手術比率の違い</strong>を必ず併せて見る必要がある。"
              "本文 12-2 が Redo での注意点を独立節にしている理由でもある。",
         cite="Figure 3, p.165"),

    # ================= 11-3  術後解剖と VIV 計画 =================
    dict(name="simpson_f01.jpg", src="simpson", sec="11-3",
         ref="Figure 1（A–D）／ p.3",
         alt="Commando 後の大動脈弁輪計測。A 弁輪径、B Valsalva洞径、C 大動脈基部の直交断面、D 弁−冠動脈間距離",
         title="Figure 1（A–D）／ p.3",
         body="<strong>Commando 後に記録しておくべき計測値。</strong>"
              "(A) 弁輪径、(B) Valsalva 洞径、(C) 大動脈基部の直交断面、(D) <strong>弁−冠動脈間距離</strong>。"
              "本文 11-3 の「使用パッチ長・弁の位置情報を記録しておくことが重要」を具体化した 4 項目で、"
              "将来 <mark>VIV-TAVI を行えるかどうかは (D) で決まる</mark>。",
         cite="Figure 1, p.3"),

    dict(name="simpson_f04.jpg", src="simpson", sec="11-3",
         ref="Figure 4（A–D）／ p.6",
         alt="好ましいaortomitral angle（A,B）と好ましくないaortomitral angle（C,D）のCT比較。C,Dでは AMC 長が長く AMA が90度に近い",
         title="Figure 4（A–D）／ p.6",
         body="<strong>「良い角度」と「悪い角度」。</strong>"
              "A・B が<strong>好ましい AMA</strong>、C・D が<strong>好ましくない AMA</strong>。"
              "C・D では<mark>AMC が長く、AMA が 90° に近づいている</mark>。"
              "AMC を長く再建するほど大動脈弁と僧帽弁が直交配置に近づき、"
              "将来の TMVR で人工弁が LVOT へ張り出しやすくなる。"
              "Commando の術中に「パッチをどこまで伸ばすか」を決める段階で、この帰結を織り込む必要がある。",
         cite="Figure 4, p.6"),

    dict(name="simpson_f06.jpg", src="simpson", sec="11-3",
         ref="Figure 6 ／ p.7",
         alt="neo-LVOT の解析画像。左パネルは仮想TMVR弁がLVOTへ張り出す様子、右パネルは黒く縁取られた neo-LVOT 面積",
         title="Figure 6 ／ p.7",
         body="<strong>neo-LVOT が Commando 後 TMVR の可否を決める。</strong>"
              "左：仮想 TMVR 弁が LVOT へ張り出す様子。右：黒く縁取られた <strong>neo-LVOT 面積</strong>。"
              "原著は<mark>neo-LVOT 面積 >200 mm² を十分なクリアランスの目安</mark>としている。"
              "本文 11-3 の「Commando 後の解剖的変化は将来の VIV-TAVI / TMVR 計画に影響する」が、"
              "この 1 つの数値に集約される。",
         cite="Figure 6, p.7"),

    # ================= 12-1  緊急 Commando =================
    dict(name="nosaka_f01.jpg", src="nosaka", sec="12-1",
         ref="Figure 1（A–C）／ p.2",
         alt="術前画像：胸部X線、心エコーの僧帽弁疣贅、Valsalva洞の慢性解離性動脈瘤のCTと3D再構成",
         title="Figure 1（A–C）／ p.2",
         body="<strong>緊急 Root-Commando に至った病態。</strong>"
              "(A) 術前胸部 X 線、(B) 心エコーの<strong>僧帽弁疣贅</strong>、"
              "(C-a/C-b) CT と 3D 再構成による <mark>Valsalva 洞の慢性解離性動脈瘤</mark>。"
              "本文 12-1 の「IE ＋ Valsalva 洞慢性解離性動脈瘤 → 緊急 Root-Commando で救命」（石川県立中央病院）の症例で、"
              "5-1 の「ECG gated CT で仮性動脈瘤の解剖学的詳細」を必須とする理由がここにある。",
         cite="Figure 1, p.2"),

    dict(name="nosaka_f02.png", src="nosaka", sec="12-1",
         ref="Figure 2（A, B）／ p.3",
         alt="左冠動脈ボタン下の仮性動脈瘤を示すCTと、術後胸部X線",
         title="Figure 2（A, B）／ p.3",
         body="<strong>緊急手術後に生じた合併症——冠動脈ボタン下の仮性動脈瘤。</strong>"
              "(A) <mark>左冠動脈ボタン直下の仮性動脈瘤</mark>（矢印）、(B) 再手術後の胸部 X 線。"
              "本文 7-2 Pitfall #11 が「冠動脈ボタン先行移動」を対策に挙げる一方、"
              "<strong>緊急下では吻合部の脆弱性が残りうる</strong>ことを示す実例。"
              "Root-Commando 後は冠動脈ボタン吻合部を CT でフォローする根拠になる。",
         cite="Figure 2, p.3"),

    # ================= 12-3  TAVR-IE =================
    dict(name="jarral_f02.jpg", src="jarral", sec="12-3",
         ref="FIGURE 2 ／ p.74",
         alt="僧帽弁人工弁を留置しaortomitral curtainをパッチ再建した術中写真。新しいneo-LVOTのための十分なスペースが確保されている",
         title="FIGURE 2 ／ p.74",
         body="<strong>TAVR-IE に対する Commando の完成像。</strong>"
              "僧帽弁人工弁を留置し、AMC をパッチで再建した状態で、"
              "<mark>新しい neo-left ventricular outflow tract のための十分なスペース</mark>が確保されている。"
              "本文 12-3 の技術的注意点「冠動脈入口部への影響」「術後の VIV 解剖計画への影響」は、"
              "この段階でパッチをどの高さ・どの角度に置くかで決まる（→ 11-3 の neo-LVOT >200 mm²）。",
         cite="FIGURE 2, p.74"),
]

ORDER = ["2-1", "2-2", "3-1", "4-1", "5-1", "6-3", "6-4", "6-7", "7", "8-1",
         "9-1", "9-3", "9-4", "9-5", "9-6", "10", "11-3", "12-1", "12-3"]

GROUPS = {
    "2-1": ("原典図：aortomitral curtain（AMC）の解剖",
            "本文の模式図が指す構造を、術中写真と CT 計測で確認する。"),
    "2-2": ("原典図：IVF/AMC 破壊の実像",
            "エコー所見から術野所見まで、破壊が進行した段階ごとの原典図。"),
    "3-1": ("原典表：AATS 2016 の手術適応と推奨クラス", None),
    "4-1": ("原典図：Commando 系術式の分類", None),
    "5-1": ("原典図表：術前画像と AATS のワークアップ推奨", None),
    "6-3": ("原典図：Commando の全体像と術中ステップ",
            "線画による全体像と、Cleveland Clinic の術中写真を並べる。"),
    "6-4": ("原典図：AMC/IVF 再建の実際とパッチ実寸",
            "本文が「generous size」とだけ述べる部分の、具体的な寸法と縫合法。"),
    "6-7": ("原典表：AATS 2016 の術中管理推奨", None),
    "7": ("原典図：Pitfall が現実に起きた術野", None),
    "8-1": ("原典図：弁種と感染再発——同種移植片は有利か", None),
    "9-1": ("原典図：hemi-Commando の手技",
            "模式図（Cleveland Clinic 公式）→ 術中写真 → 変法（Leipzig）→ "
            "原型論文（2010）の順に並べた。"),
    "9-3": ("原典図：En bloc 根部切除（Brussels 変法）", None),
    "9-4": ("原典図：Patch-sparing 変法（Yajima 2022）", None),
    "9-5": ("原典図：Aorto-annulo-septotomy 変法（Matsuzaki 2024）", None),
    "9-6": ("原典図：Chimney Commando と弁輪拡大への応用", None),
    "10": ("原典図：施設別シリーズの生存・再手術・再感染曲線",
           "本文 10-1 の表の各行が、原典ではどのような曲線だったか。"),
    "11-3": ("原典図：Commando 後の解剖と VIV/TMVR 計画", None),
    "12-1": ("原典図：緊急 Root-Commando の症例", None),
    "12-3": ("原典図：TAVR-IE に対する Commando", None),
}

SEC_LABEL = {
    "2-1": "2-1", "2-2": "2-2", "3-1": "3-1", "4-1": "4-1", "5-1": "5-1",
    "6-3": "6 Step3", "6-4": "6 Step4", "6-7": "6 Step7", "7": "7-2",
    "8-1": "8-1", "9-1": "9-1", "9-3": "9-3", "9-4": "9-4", "9-5": "9-5",
    "9-6": "9-6", "10": "10-2", "11-3": "11-3", "12-1": "12-1", "12-3": "12-3",
}

NEW_SECTIONS = {}

HTML_MARKERS = {
    "2-1": '<h3 id="2-2-ivf-破壊の病態メカニズム">',
    "2-2": '<h2 id="3-適応">',
    "3-1": '<h3 id="3-2-非ie適応">',
    "4-1": '<h3 id="4-2-術式の特徴比較">',
    "5-1": '<h3 id="5-2-手術タイミングaats-2016-推奨">',
    "6-3": '<h3 id="step-4amc--ivf-再建commando-の核心">',
    "6-4": '<h3 id="step-5僧帽弁置換mvr-avr-より先に施行">',
    "6-7": '<h3 id="step-8体外循環離脱前の止血確認">',
    "7": '<h3 id="7-3-cpb手術時間の管理">',
    "8-1": '<h3 id="8-2-僧帽弁の選択">',
    "9-1": '<h3 id="9-2-root-commando根部置換を伴う変法">',
    "9-3": '<h3 id="9-4-patch-sparing-変法yajima-2022">',
    "9-4": '<h3 id="9-5-aorto-annulo-septotomy-変法matsuzaki-2024-日本">',
    "9-5": '<h3 id="9-6-chimney-commandoyang-変法">',
    "9-6": '<h3 id="9-7-posterior-av-groove-再建追加変法pechenenko-2023">',
    "10": '<h3 id="10-3-成績改善のポイント">',
    "11-3": '<h2 id="12-特殊シナリオ">',
    "12-1": '<h3 id="12-2-再手術redoでの-commando">',
    "12-3": '<h3 id="12-4-機械双弁-ie--commando">',
}

MD_MARKERS = {
    "2-1": "### 2-2. IVF 破壊の病態メカニズム",
    "2-2": "## 3. 適応",
    "3-1": "### 3-2. 非IE適応",
    "4-1": "### 4-2. 術式の特徴比較",
    "5-1": "### 5-2. 手術タイミング（AATS 2016 推奨）",
    "6-3": "### Step 4：AMC / IVF 再建（Commando の核心）",
    "6-4": "### Step 5：僧帽弁置換（MVR）—— **AVR より先に施行**",
    "6-7": "### Step 8：体外循環離脱前の止血確認",
    "7": "### 7-3. CPB・手術時間の管理",
    "8-1": "### 8-2. 僧帽弁の選択",
    "9-1": "### 9-2. Root-Commando（根部置換を伴う変法）",
    "9-3": "### 9-4. Patch-Sparing 変法（Yajima 2022）",
    "9-4": "### 9-5. Aorto-Annulo-Septotomy 変法（Matsuzaki 2024, 日本）",
    "9-5": "### 9-6. Chimney Commando（Yang 変法）",
    "9-6": "### 9-7. Posterior AV Groove 再建追加変法（Pechenenko 2023）",
    "10": "### 10-3. 成績改善のポイント",
    "11-3": "## 12. 特殊シナリオ",
    "12-1": "### 12-2. 再手術（Redo）での Commando",
    "12-3": "### 12-4. 機械双弁 IE → Commando",
}

LINE_START_SECS = set()

LIGHTBOX_MARKER = "<script>\n(function () {\n  var sidebar"

INDEX = dict(
    heading="図表一覧（原典PDF出典）",
    anchor="図表一覧原典pdf出典",
    source_col="出典論文",
    html_marker='<h2 id="15-参照ノート">',
    md_marker="\n---\n\n## 15. 参照ノート",
    lead="本文書に挿入した図表 54 点はすべて <code>commando_procedure/pdfs/</code> の原典 PDF から"
         "抽出したもので、画像ファイルは <code>commando_procedure/figures/</code> に格納している。"
         "手技図・術中写真は PDF に埋め込まれた原画像を再サンプリングせずに取り出し、"
         "AATS の推奨表のみ 220 dpi のページ切り出しで作成した。図をクリックすると拡大表示される。",
    lead_md="本文書に挿入した図表 54 点はすべて `commando_procedure/pdfs/` の原典 PDF から"
            "抽出したもので、画像ファイルは `commando_procedure/figures/` に格納している。"
            "手技図・術中写真は PDF に埋め込まれた原画像を再サンプリングせずに取り出し、"
            "AATS の推奨表のみ 220 dpi のページ切り出しで作成した。",
    copyright="掲載した図表はいずれも各学会・出版社が著作権を有する出版物からの抜粋であり"
              "（von Zeppelin 2026 <em>Medicina</em>、Vobornik 2023 <em>Front Cardiovasc Med</em>、"
              "Iaccarino 2023 <em>J Clin Med</em> はオープンアクセス CC BY）、"
              "原典の推奨クラス・手技手順・成績を本文の記述と照合するための"
              "<strong>個人的な参照目的</strong>で引用している。"
              "再配布・二次利用は行わないこと。臨床判断にあたっては必ず原典を参照すること。",
)

TOC_HTML_INSERTS = []
TOC_MD_INSERTS = []
