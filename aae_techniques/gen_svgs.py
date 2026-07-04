#!/usr/bin/env python3
"""Generate original schematic SVG diagrams for the AAE technique atlas.

All diagrams are ORIGINAL work (no copyrighted figure is traced), so they are
free to publish. Output: figures/aae_*.svg
Style: clean surgical schematic, Noto Sans JP labels, light background.
"""
import math, os

BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "figures")

FONT = "'Noto Sans JP','Hiragino Sans',sans-serif"
INK = "#1f2933"       # primary ink
MUT = "#5b6673"       # muted label
FIB = "#f0d9b5"       # fibrous tissue (curtain/trigone) warm tan
FIBED = "#c9a978"
MYO = "#d98b8b"       # myocardium / aortic wall pink
MYOED = "#b45c5c"
LUM = "#fbf4ef"       # lumen
BLUE = "#2f6db5"      # Nicks
GREEN = "#2e8b57"     # Manouguian
PURPLE = "#7a4fb5"    # Y-incision
ORANGE = "#d9772f"    # Konno

def wrap(inner, w, h, label):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="{label}" style="width:100%;height:auto;max-width:{w}px;display:block;'
            f'margin:0 auto;border:1px solid #e3e3e3;border-radius:10px;background:#fff;'
            f'font-family:{FONT};">\n{inner}\n</svg>\n')

# ---- shared top-down aortic root geometry ----
CX, CY, R = 310, 250, 140
# cusp centres (deg, y-down): NCC bottom, LCC upper-left, RCC upper-right
A = {"NCC": 90, "LCC": 210, "RCC": 330}
# commissures
COM = {"LN": 150, "NR": 30, "RL": 270}  # LCC-NCC, NCC-RCC, RCC-LCC

def pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r*math.cos(a), cy + r*math.sin(a)

def cusp_arc(deg, r=R, depth=52):
    """scalloped cusp belly centred at angle deg."""
    x0, y0 = pol(CX, CY, r, deg-58)
    x1, y1 = pol(CX, CY, r, deg+58)
    bx, by = pol(CX, CY, r-depth, deg)
    return f'M {x0:.0f} {y0:.0f} Q {bx:.0f} {by:.0f} {x1:.0f} {y1:.0f}'

def base_root(show_labels=True):
    s = []
    # aortic wall ring
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R+16}" fill="{MYO}" stroke="{MYOED}" stroke-width="2"/>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="{LUM}" stroke="{MYOED}" stroke-width="1.5"/>')
    # cusps
    for name, deg in A.items():
        s.append(f'<path d="{cusp_arc(deg)}" fill="none" stroke="{MUT}" stroke-width="2.2"/>')
    # commissure ticks
    for k, deg in COM.items():
        x1, y1 = pol(CX, CY, R-6, deg); x2, y2 = pol(CX, CY, R+16, deg)
        s.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{MYOED}" stroke-width="3"/>')
    # coronary ostia
    lox, loy = pol(CX, CY, R-70, A["LCC"])
    rox, roy = pol(CX, CY, R-70, A["RCC"])
    s.append(f'<circle cx="{lox:.0f}" cy="{loy:.0f}" r="9" fill="#7a1f1f"/><circle cx="{lox:.0f}" cy="{loy:.0f}" r="9" fill="none" stroke="#fff" stroke-width="2"/>')
    s.append(f'<circle cx="{rox:.0f}" cy="{roy:.0f}" r="9" fill="#7a1f1f"/><circle cx="{rox:.0f}" cy="{roy:.0f}" r="9" fill="none" stroke="#fff" stroke-width="2"/>')
    # aorto-mitral curtain (fibrous) below LCC-NCC commissure, plus trigones + AML
    cx_ln, cy_ln = pol(CX, CY, R+14, COM["LN"])   # lower-left commissure
    # curtain fan downward-left to mitral
    ltx, lty = pol(CX, CY, R+70, 175)   # left trigone
    rtx, rty = pol(CX, CY, R+70, 118)   # right trigone
    mvx, mvy = pol(CX, CY, R+150, 148)  # mitral centre
    s.append(f'<path d="M {ltx:.0f} {lty:.0f} Q {cx_ln-30:.0f} {cy_ln+40:.0f} {mvx-60:.0f} {mvy:.0f} '
             f'Q {mvx:.0f} {mvy+34:.0f} {mvx+60:.0f} {mvy-6:.0f} Q {cx_ln+50:.0f} {cy_ln+40:.0f} {rtx:.0f} {rty:.0f} Z" '
             f'fill="{FIB}" stroke="{FIBED}" stroke-width="1.5"/>')
    # anterior mitral leaflet arc
    s.append(f'<path d="M {mvx-58:.0f} {mvy+2:.0f} Q {mvx:.0f} {mvy+40:.0f} {mvx+58:.0f} {mvy-4:.0f}" fill="none" stroke="{MYOED}" stroke-width="2" stroke-dasharray="2 4"/>')
    # trigones (small triangles)
    for (tx, ty) in [(ltx, lty), (rtx, rty)]:
        s.append(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="8" fill="{FIBED}" stroke="{INK}" stroke-width="1"/>')
    # membranous septum near NCC-RCC commissure
    msx, msy = pol(CX, CY, R+30, COM["NR"])
    s.append(f'<rect x="{msx-14:.0f}" y="{msy-10:.0f}" width="28" height="20" rx="5" fill="#e7d27a" stroke="#a68a2a" stroke-width="1.2" transform="rotate(30 {msx:.0f} {msy:.0f})"/>')
    if show_labels:
        def lab(x, y, t, anchor="middle", col=INK, size=15, weight="600"):
            return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{col}">{t}</text>'
        nx, ny = pol(CX, CY, R-88, A["NCC"])
        s.append(lab(nx, ny+4, "NCC"))
        lx, ly = pol(CX, CY, R-92, A["LCC"])
        s.append(lab(lx, ly, "LCC"))
        rx, ry = pol(CX, CY, R-92, A["RCC"])
        s.append(lab(rx, ry, "RCC"))
        s.append(lab(lox-14, loy-14, "LCA", "end", "#7a1f1f", 12, "700"))
        s.append(lab(rox+14, roy-14, "RCA", "start", "#7a1f1f", 12, "700"))
        s.append(lab(mvx+2, mvy+18, "前尖(AML)", "middle", MYOED, 12, "700"))
        s.append(lab(ltx-14, lty+2, "左trigone", "end", FIBED, 11, "700"))
        s.append(lab(rtx+16, rty+2, "右trigone", "start", FIBED, 11, "700"))
        s.append(lab(mvx-4, mvy-14, "大動脈-僧帽弁curtain", "middle", "#9a7b3a", 11, "700"))
        s.append(lab(msx+34, msy+4, "膜性中隔", "start", "#8a7020", 11, "700"))
    return "\n".join(s)

# === SVG 1: base anatomy ===
title = ('<text x="310" y="34" text-anchor="middle" font-size="18" font-weight="700" fill="'+INK+'">大動脈基部（術者視・弁を除いた見下ろし図）</text>')
sub = ('<text x="310" y="54" text-anchor="middle" font-size="12" fill="'+MUT+'">弁輪拡大術を理解する解剖ランドマーク</text>')
inner = title + sub + '<g transform="translate(0,20)">' + base_root() + '</g>'
open(os.path.join(FIG, "aae_anatomy.svg"), "w").write(wrap(inner, 620, 560, "大動脈基部の解剖ランドマーク"))

# === SVG 2: incision map (4 techniques overlaid) ===
def arrow(x1, y1, x2, y2, col, w=5):
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}" '
            f'stroke-linecap="round" marker-end="url(#ah_{col.strip("#")})"/>')
defs = ""
for col in [BLUE, GREEN, PURPLE, ORANGE]:
    cid = col.strip("#")
    defs += (f'<marker id="ah_{cid}" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">'
             f'<path d="M0,0 L7,3 L0,6 Z" fill="{col}"/></marker>')
paths = []
# Nicks: NCC nadir straight down to mitral (posterior, short)
nx, ny = pol(CX, CY, R-6, A["NCC"])
paths.append(arrow(nx, ny, nx, ny+92, BLUE))
# Manouguian: LCC-NCC commissure into curtain toward AML
cln_x, cln_y = pol(CX, CY, R+2, COM["LN"])
mvx, mvy = pol(CX, CY, R+120, 150)
paths.append(arrow(cln_x, cln_y, mvx, mvy, GREEN))
# Y-incision: from LCC-NCC commissure a Y to both trigones (into, not through)
ltx, lty = pol(CX, CY, R+58, 176); rtx, rty = pol(CX, CY, R+58, 120)
paths.append(arrow(cln_x, cln_y, ltx, lty, PURPLE, 4))
paths.append(arrow(cln_x, cln_y, rtx, rty, PURPLE, 4))
# Konno: RCC-LCC commissure anteriorly up into RVOT/septum (opposite direction)
crl_x, crl_y = pol(CX, CY, R+2, COM["RL"])
paths.append(arrow(crl_x, crl_y, crl_x, crl_y-92, ORANGE))
legend = [
    (BLUE, "Nicks", "NCC → 僧帽弁輪（後方限局）＝1弁サイズ"),
    (GREEN, "Manouguian", "LCC-NCC交連 → curtain → 前尖起始（1〜2サイズ）"),
    (PURPLE, "Y-incision", "交連 → 両trigoneへY字（curtainは貫かない・3〜5サイズ）"),
    (ORANGE, "Konno", "前方・心室中隔 → RVOT（原径の約2倍・両心室形成）"),
]
lg = []
ly0 = 470
for i, (col, name, desc) in enumerate(legend):
    y = ly0 + i*26
    lg.append(f'<line x1="40" y1="{y-4}" x2="72" y2="{y-4}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
    lg.append(f'<text x="80" y="{y}" font-size="13" font-weight="700" fill="{col}">{name}</text>')
    lg.append(f'<text x="176" y="{y}" font-size="12" fill="{MUT}">{desc}</text>')
title2 = '<text x="310" y="34" text-anchor="middle" font-size="18" font-weight="700" fill="'+INK+'">4術式が切り込む方向 — 一望比較</text>'
inner2 = ('<defs>'+defs+'</defs>' + title2 + '<g transform="translate(0,16)">' + base_root(show_labels=True) + "".join(paths) + '</g>' + "".join(lg))
open(os.path.join(FIG, "aae_incision_map.svg"), "w").write(wrap(inner2, 620, 600, "4術式の切開方向の比較"))

# === SVG 3: enlargement ladder ===
rows = [
    ("Nicks (1970)", 1, BLUE, "後方 / 低侵襲"),
    ("Manouguian (1979)", 2, GREEN, "trigone / 中侵襲・MRリスク"),
    ("Konno (1975)", 3, ORANGE, "両心室 / 高侵襲・伝導障害"),
    ("Y-incision (2023-)", 5, PURPLE, "curtain温存 / 3-5サイズ"),
]
W3, H3 = 820, 330
s3 = ['<text x="410" y="34" text-anchor="middle" font-size="18" font-weight="700" fill="'+INK+'">術式別の弁サイズ up 能力（目安）</text>']
x0, unit, barh = 210, 78, 30
for i, (name, n, col, note) in enumerate(rows):
    y = 78 + i*58
    s3.append(f'<text x="196" y="{y+barh-8}" text-anchor="end" font-size="14" font-weight="700" fill="{INK}">{name}</text>')
    for k in range(n):
        s3.append(f'<rect x="{x0+k*unit}" y="{y}" width="{unit-8}" height="{barh}" rx="4" fill="{col}" opacity="{0.55+0.45*(k+1)/n:.2f}"/>')
        s3.append(f'<text x="{x0+k*unit+(unit-8)/2}" y="{y+barh-8}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">+{k+1}</text>')
    s3.append(f'<text x="{x0+n*unit+6}" y="{y+barh-9}" font-size="11" fill="{MUT}">{note}</text>')
s3.append(f'<text x="210" y="314" font-size="11" fill="{MUT}">※ 1目盛 = 人工弁1サイズ（≈2mm）up。実際の到達量は弁輪径・体格・解剖により変動。Y-incisionの実臨床中央値は3サイズ。</text>')
open(os.path.join(FIG, "aae_enlargement_ladder.svg"), "w").write(wrap("\n".join(s3), W3, H3, "術式別の弁サイズアップ能力"))

# === technique cross-section side views (coronal schematic) ===
def coronal_base():
    """aorta (top) - annulus - LV (bottom) coronal schematic; returns svg fragment."""
    s = []
    # ascending aorta
    s.append(f'<path d="M 150 60 L 150 150 Q 150 190 200 195 L 300 195 Q 350 190 350 150 L 350 60" fill="{LUM}" stroke="{MYOED}" stroke-width="3"/>')
    s.append(f'<path d="M 135 60 L 135 150 Q 135 205 200 210 L 300 210 Q 365 205 365 150 L 365 60" fill="none" stroke="{MYOED}" stroke-width="3"/>')
    # annulus line
    s.append(f'<line x1="150" y1="195" x2="350" y2="195" stroke="{INK}" stroke-width="2" stroke-dasharray="4 3"/>')
    # LV walls
    s.append(f'<path d="M 200 210 Q 175 320 250 360 Q 325 320 300 210" fill="{MYO}" opacity="0.35" stroke="{MYOED}" stroke-width="2"/>')
    # mitral (posterior/left) + septum (right)
    s.append(f'<text x="250" y="52" text-anchor="middle" font-size="12" fill="'+MUT+'">上行大動脈</text>')
    s.append(f'<text x="250" y="188" text-anchor="middle" font-size="11" font-weight="700" fill="'+INK+'">大動脈弁輪</text>')
    return "\n".join(s)

# SVG 4: Nicks coronal
s4 = ['<text x="250" y="30" text-anchor="middle" font-size="17" font-weight="700" fill="'+INK+'">Nicks法（後方パッチ）</text>', coronal_base()]
# incision extends from aortotomy down through NCC into mitral annulus (posterior=left side)
s4.append(f'<path d="M 200 70 L 200 205" stroke="{BLUE}" stroke-width="3" fill="none" stroke-dasharray="6 4"/>')
s4.append(f'<path d="M 185 205 Q 178 235 195 250" stroke="{BLUE}" stroke-width="3" fill="none" stroke-dasharray="6 4"/>')
# teardrop patch
s4.append(f'<path d="M 200 90 Q 165 150 175 250 Q 200 265 220 205 L 220 90 Z" fill="{BLUE}" opacity="0.20" stroke="{BLUE}" stroke-width="2"/>')
s4.append(f'<text x="150" y="150" text-anchor="end" font-size="12" font-weight="700" fill="{BLUE}">涙滴型パッチ</text>')
s4.append(f'<text x="150" y="166" text-anchor="end" font-size="11" fill="{MUT}">NCC→僧帽弁輪</text>')
s4.append(f'<text x="330" y="255" text-anchor="middle" font-size="11" fill="{MUT}">中隔側</text>')
s4.append(f'<text x="250" y="392" text-anchor="middle" font-size="11" fill="{MUT}">拡大量 ≈ 1弁サイズ・僧帽弁前尖に及ばず低リスク</text>')
open(os.path.join(FIG, "aae_nicks.svg"), "w").write(wrap("\n".join(s4), 500, 410, "Nicks法の模式図"))

# SVG 5: Manouguian coronal
s5 = ['<text x="250" y="30" text-anchor="middle" font-size="17" font-weight="700" fill="'+INK+'">Manouguian法（trigone〜前尖パッチ）</text>', coronal_base()]
s5.append(f'<path d="M 195 70 L 195 205 Q 190 250 200 290" stroke="{GREEN}" stroke-width="3" fill="none" stroke-dasharray="6 4"/>')
# AML top depiction
s5.append(f'<path d="M 175 250 Q 200 300 230 255" fill="none" stroke="{MYOED}" stroke-width="2.5"/>')
s5.append(f'<text x="235" y="285" font-size="11" font-weight="700" fill="{MYOED}">前尖(AML)</text>')
s5.append(f'<path d="M 195 90 Q 160 180 185 295 Q 205 305 218 205 L 218 90 Z" fill="{GREEN}" opacity="0.18" stroke="{GREEN}" stroke-width="2"/>')
s5.append(f'<text x="150" y="150" text-anchor="end" font-size="12" font-weight="700" fill="{GREEN}">紡錘型パッチ</text>')
s5.append(f'<text x="150" y="166" text-anchor="end" font-size="11" fill="{MUT}">交連→trigone貫通</text>')
s5.append(f'<circle cx="200" cy="292" r="7" fill="none" stroke="#c00" stroke-width="2"/>')
s5.append(f'<text x="250" y="392" text-anchor="middle" font-size="11" fill="#b45c5c">前尖への過延長・パッチ破断＝術後MRの機序（Case 4, 1979）</text>')
open(os.path.join(FIG, "aae_manouguian.svg"), "w").write(wrap("\n".join(s5), 500, 410, "Manouguian法の模式図"))

# SVG 6: Konno coronal (anterior aortoventriculoplasty, two patches)
s6 = ['<text x="250" y="30" text-anchor="middle" font-size="17" font-weight="700" fill="'+INK+'">Konno法（大動脈-心室形成 / 2パッチ）</text>', coronal_base()]
# anterior incision down the septum (right side here = anterior/septum)
s6.append(f'<path d="M 305 70 L 305 205 L 300 300 L 285 345" stroke="{ORANGE}" stroke-width="3" fill="none" stroke-dasharray="6 4"/>')
# septal patch (inside LV, on septum) + aortic patch
s6.append(f'<path d="M 305 205 L 305 340 Q 320 355 335 330 L 335 205 Z" fill="{ORANGE}" opacity="0.20" stroke="{ORANGE}" stroke-width="2"/>')
s6.append(f'<path d="M 300 80 L 300 200 L 340 200 L 340 80 Z" fill="{ORANGE}" opacity="0.30" stroke="{ORANGE}" stroke-width="2"/>')
# RVOT patch (outer, on the anterior/RV side)
s6.append(f'<path d="M 340 90 Q 380 160 360 300 Q 345 320 340 300 L 340 90 Z" fill="#c9a", opacity="0.18" stroke="#8a6" stroke-width="2"/>'.replace('"#c9a",','"#cbb285"'))
s6.append(f'<text x="392" y="150" text-anchor="start" font-size="11" font-weight="700" fill="#8a6b2a">RVOTパッチ</text>')
s6.append(f'<text x="392" y="166" text-anchor="start" font-size="11" fill="{MUT}">（右室流出路再建）</text>')
s6.append(f'<text x="360" y="255" text-anchor="start" font-size="12" font-weight="700" fill="{ORANGE}">中隔パッチ</text>')
s6.append(f'<text x="120" y="150" text-anchor="start" font-size="11" fill="{MUT}">僧帽弁側</text>')
s6.append(f'<text x="250" y="392" text-anchor="middle" font-size="11" fill="{MUT}">原径の約2倍まで拡大可・房室ブロック/伝導障害・高侵襲（先天性超狭小弁輪向け）</text>')
open(os.path.join(FIG, "aae_konno.svg"), "w").write(wrap("\n".join(s6), 500, 410, "Konno法の模式図"))

print("generated:")
for f in sorted(os.listdir(FIG)):
    if f.endswith(".svg"):
        print("  ", f, os.path.getsize(os.path.join(FIG, f)), "bytes")
