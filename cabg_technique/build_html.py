#!/usr/bin/env python3
"""Build the search-enabled, sidebar-navigated Commando Procedure review HTML.

Reuses the house CSS / callout / pandoc pipeline from convert_to_html.py and the
full-text search box + sidebar TOC from robotic_cpb/build_html.py, exactly as
aae_techniques/build_html.py does.

Usage:
  python3 commando_procedure/build_html.py           # defaults to the integrated review
  python3 commando_procedure/build_html.py in.md out.html
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "robotic_cpb"))

from convert_to_html import (  # noqa: E402
    CSS_TEMPLATE,
    strip_frontmatter,
    convert_wikilinks,
    convert_highlights,
    convert_callouts,
    pandoc_convert,
    wrap_tables,
)
import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "robotic_build", os.path.join(ROOT, "robotic_cpb", "build_html.py"))
robotic_build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(robotic_build)
SEARCH_CSS = robotic_build.SEARCH_CSS
SCRIPT = robotic_build.SCRIPT

DESCRIPTION = (
    "CABG手技アトラス — これから冠動脈外科をやる外科医のために。心臓の脱転・展開と血行動態、"
    "内胸動脈／橈骨動脈／no-touch大伏在静脈／右胃大網動脈の採取、多枝バイパスのグラフトデザイン、"
    "吻合と難標的（内膜摘除・porcelain aorta・TTFM）、トレーニングと学習曲線を一次文献50編から再構成し、"
    "原典PDFの手技図・術中写真34点を該当箇所に引用した術式リファレンス")

FIG_CSS = """
figure.gfig{margin:1.8rem 0;padding:0;background:var(--light-bg,#f8f9fb);
  border:1px solid var(--border,#dde1e8);border-radius:10px;overflow:hidden;}
figure.gfig img{display:block;width:100%;height:auto;background:#fff;cursor:zoom-in;}
figure.gfig figcaption{padding:.85rem 1.1rem;font-size:.92rem;line-height:1.75;text-align:left;
  color:var(--fg,#222);border-top:1px solid var(--border,#dde1e8);}
figure.gfig figcaption b{color:var(--accent,#0b5fa5);}
#gfig-lb{position:fixed;inset:0;background:rgba(0,0,0,.88);display:none;
  align-items:center;justify-content:center;z-index:9999;cursor:zoom-out;padding:2vh 2vw;}
#gfig-lb.on{display:flex;}
#gfig-lb img{max-width:96vw;max-height:96vh;object-fit:contain;}
@media print{figure.gfig{break-inside:avoid;}}
"""

FIG_JS = """
<div id="gfig-lb"><img alt=""></div>
<script>
(function(){var lb=document.getElementById('gfig-lb'),im=lb.querySelector('img');
document.querySelectorAll('figure.gfig img').forEach(function(t){
  t.addEventListener('click',function(){im.src=t.src;im.alt=t.alt;lb.classList.add('on');});});
lb.addEventListener('click',function(){lb.classList.remove('on');im.src='';});
document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on');});})();
</script>
"""


def build(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    text, title = strip_frontmatter(text)
    text = convert_wikilinks(text)
    text = convert_highlights(text)
    text = convert_callouts(text)

    parts = re.split(r'(<div class="callout".*?</div>\n?)', text, flags=re.DOTALL)
    converted = []
    for part in parts:
        if part.startswith('<div class="callout"'):
            converted.append(part)
        else:
            converted.append(pandoc_convert(part))
    body_html = wrap_tables("\n".join(converted))

    if not title:
        m = re.search(r"<h1[^>]*>(.*?)</h1>", body_html)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1))

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{DESCRIPTION}">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS_TEMPLATE}{SEARCH_CSS}{FIG_CSS}</style>
</head>
<body>
<div class="layout">
  <aside id="sidebar" aria-label="目次と検索">
    <div id="sidebar-search">
      <div style="position:relative;">
        <input id="search-input" type="search" placeholder="本文を検索 ( / でフォーカス )" autocomplete="off" aria-label="本文を検索">
        <button id="search-clear" aria-label="検索をクリア">&times;</button>
      </div>
      <div id="search-meta">
        <span id="search-count"></span>
        <button id="search-prev" aria-label="前の一致">&#8593;</button>
        <button id="search-next" aria-label="次の一致">&#8595;</button>
      </div>
    </div>
    <div id="sidebar-header">目次</div>
    <nav id="sidebar-nav"></nav>
  </aside>
  <main class="content">
{body_html}
  </main>
</div>
<div id="sidebar-backdrop"></div>
<button id="sidebar-toggle" aria-label="目次を開く">&#9776;</button>
{SCRIPT}
{FIG_JS}
</body>
</html>
"""
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {html_path} ({os.path.getsize(html_path)/1024:.1f} KB)")


def main():
    if len(sys.argv) == 3:
        build(sys.argv[1], sys.argv[2])
    else:
        md = os.path.join(BASE, "md", "CABG_technique_atlas.md")
        out = os.path.join(ROOT, "output", "cabg_technique_atlas.html")
        build(md, out)


if __name__ == "__main__":
    main()
