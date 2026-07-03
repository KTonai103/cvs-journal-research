#!/usr/bin/env python3
"""Build the search-enabled, sidebar-navigated Cor-Knot pitfalls HTML report.

Reuses the house CSS / callout / pandoc pipeline from convert_to_html.py and the
full-text search box + sidebar TOC from robotic_cpb/build_html.py.

Usage:
  python3 cor_knot/build_html.py            # defaults to the Cor-Knot review
  python3 cor_knot/build_html.py in.md out.html
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
# reuse the search CSS + nav/search JS verbatim from the robotic build
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location(
    "robotic_build", os.path.join(ROOT, "robotic_cpb", "build_html.py"))
robotic_build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(robotic_build)
SEARCH_CSS = robotic_build.SEARCH_CSS
SCRIPT = robotic_build.SCRIPT

DESCRIPTION = ("Cor-Knot（自動チタンファスナー）の合併症とPitfall — 弁尖穿孔・大動脈基部損傷・"
               "冠動脈干渉・遅発性塞栓の機序と、どう打つべきかのテクニカルガイド（PubMed 61本の統合レビュー）")


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
<style>{CSS_TEMPLATE}{SEARCH_CSS}</style>
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
        md = os.path.join(BASE, "md", "cor_knot_pitfalls_review.md")
        out = os.path.join(ROOT, "output", "cor_knot_pitfalls_review.html")
        build(md, out)


if __name__ == "__main__":
    main()
