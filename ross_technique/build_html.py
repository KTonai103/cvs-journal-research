#!/usr/bin/env python3
"""Build the Ross technique review HTML.

Reuses the house CSS/callout/pandoc pipeline from convert_to_html.py and the
search + TOC + glossary machinery from af_surgical_ablation/build_html.py, and
ADDS what a figure-heavy technique review needs:
  - figure cards (figure.gfig) with source/licence lines
  - video figures (figure.vfig) — thumbnail is a link to the original video, with a ▶ badge
  - a click-to-zoom lightbox for every figure
  - width/height stamped on every <img> from the actual file (avoids reflow with lazy loading)

Usage:
  python3 ross_technique/build_html.py [input.md] [output.html]
"""
import importlib.util
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, ROOT)

from convert_to_html import (  # noqa: E402
    CSS_TEMPLATE,
    strip_frontmatter,
    convert_wikilinks,
    convert_highlights,
    convert_callouts,
    pandoc_convert,
    wrap_tables,
)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# SEARCH_CSS / GLOSSARY_CSS / SCRIPT / GLOSS_SCRIPT are document-agnostic.
afb = _load(os.path.join(ROOT, "af_surgical_ablation", "build_html.py"), "afb")

# The AF review used <h2> for chapters; this one uses <h1> (第0章…第11章), so the
# TOC has to include H1 and give it the top-level `nav-chapter` styling.
TOC_SCRIPT = afb.SCRIPT.replace(
    "var headings = content.querySelectorAll('h2, h3, h4');",
    "var headings = Array.prototype.slice.call(\n"
    "    content.querySelectorAll('h1, h2, h3, h4'));\n"
    "  // the leading H1 is the document title, already shown in the page body\n"
    "  if (headings.length && headings[0].tagName === 'H1') headings.shift();\n"
    "  if (headings.some(function (h) { return h.tagName === 'H1'; })) {\n"
    "    nav.classList.add('has-chapters');\n"
    "    var sbHead = document.getElementById('sidebar-header');\n"
    "    if (sbHead) sbHead.textContent = '目次 — 章・節';\n"
    "  }"
).replace(
    "    if (h.tagName === 'H2') a.className = 'nav-journal';",
    "    if (h.tagName === 'H1') a.className = 'nav-chapter';\n"
    "    else if (h.tagName === 'H2') a.className = 'nav-journal';"
)
assert "nav-chapter" in TOC_SCRIPT and "h1, h2, h3, h4" in TOC_SCRIPT, \
    "af_surgical_ablation/build_html.py changed shape — re-check the TOC patch"

FIG_CSS = """
/* ---- figure cards ---- */
figure.gfig {
  margin: 20px 0 24px;
  padding: 10px 10px 4px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--light-bg);
}
figure.gfig img {
  display: block; max-width: 100%; height: auto; margin: 0 auto;
  border: 1px solid var(--border); border-radius: 4px; background: #fff;
  cursor: zoom-in;
}
figure.gfig figcaption {
  display: block; text-align: left; font-size: 0.8rem; color: var(--fg);
  line-height: 1.6; margin: 10px 2px 6px; padding: 0;
}
figure.gfig figcaption b { color: var(--accent); }
figure.gfig figcaption mark { font-weight: 600; }
figure.gfig .src {
  display: block; margin-top: 5px; font-size: 0.72rem; color: var(--muted);
}
/* video figures: thumbnail is a link, with a play badge */
figure.vfig { background: #eef1f5; }
figure.vfig a { position: relative; display: block; text-decoration: none; }
figure.vfig a img { cursor: pointer; }
figure.vfig .play {
  position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);
  width: 58px; height: 58px; border-radius: 50%;
  background: rgba(20,20,20,0.62); color: #fff;
  font-size: 1.5rem; line-height: 58px; text-align: center;
  box-shadow: 0 2px 12px rgba(0,0,0,0.35); transition: background 0.15s, transform 0.15s;
}
figure.vfig a:hover .play { background: rgba(21,101,192,0.92); transform: translate(-50%, -50%) scale(1.08); }
figure.vfig figcaption a { font-weight: 600; }

.videolist {
  border-left: 4px solid #1565c0; background: #e8f0fe;
  padding: 10px 16px; margin: 14px 0 20px; border-radius: 0 4px 4px 0; font-size: 0.85rem;
}
.videolist p { margin: 6px 0; font-size: 0.85rem; }

/* ---- lightbox ---- */
#lb {
  position: fixed; inset: 0; z-index: 400; display: none;
  background: rgba(0,0,0,0.88); align-items: center; justify-content: center;
  padding: 24px; cursor: zoom-out;
}
#lb.open { display: flex; }
#lb img { max-width: 96vw; max-height: 88vh; border-radius: 4px; background: #fff; }
#lb-cap {
  position: fixed; left: 0; right: 0; bottom: 0; padding: 10px 18px;
  background: rgba(0,0,0,0.72); color: #eee; font-size: 0.78rem; line-height: 1.5;
  text-align: center; max-height: 22vh; overflow-y: auto;
}
#lb-close {
  position: fixed; top: 14px; right: 18px; background: transparent; border: none;
  color: #fff; font-size: 2rem; line-height: 1; cursor: pointer;
}
@media print {
  figure.gfig { break-inside: avoid; background: #fff; }
  figure.vfig .play { display: none; }
  #lb { display: none !important; }
}
"""

LIGHTBOX = """
<div id="lb" role="dialog" aria-modal="true" aria-label="図の拡大表示">
  <button id="lb-close" aria-label="閉じる">&times;</button>
  <img id="lb-img" alt="">
  <div id="lb-cap"></div>
</div>
<script>
(function () {
  var lb = document.getElementById('lb'), im = document.getElementById('lb-img'),
      cap = document.getElementById('lb-cap');
  if (!lb || !im) return;
  function open(src, alt, text) {
    im.src = src; im.alt = alt || ''; cap.textContent = text || '';
    lb.classList.add('open');
  }
  function close() { lb.classList.remove('open'); im.src = ''; }
  document.querySelectorAll('figure.gfig').forEach(function (fig) {
    var img = fig.querySelector('img');
    if (!img) return;
    var isVideo = fig.classList.contains('vfig');
    img.addEventListener('click', function (e) {
      // on a video card the thumbnail is a link to the original video — let it through
      if (isVideo) return;
      e.preventDefault();
      var fc = fig.querySelector('figcaption');
      open(img.currentSrc || img.src, img.alt, fc ? fc.textContent.trim() : '');
    });
  });
  lb.addEventListener('click', function (e) { if (e.target !== im) close(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && lb.classList.contains('open')) close();
  });
})();
</script>
"""


def stamp_dimensions(html, md_dir):
    """Add width/height (and loading=lazy) to every <img> from the file on disk."""
    try:
        from PIL import Image
    except ImportError:
        return html
    roots = [os.path.join(ROOT, "output"), os.path.join(BASE)]
    cache = {}

    def size(src):
        if src in cache:
            return cache[src]
        for r in roots:
            p = os.path.join(r, src)
            if os.path.exists(p):
                with Image.open(p) as im:
                    cache[src] = im.size
                    return cache[src]
        cache[src] = None
        return None

    def fix(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        if not src:
            return tag
        wh = size(src.group(1))
        add = ' loading="lazy" decoding="async"' if "loading=" not in tag else ""
        if wh:
            add += f' width="{wh[0]}" height="{wh[1]}"'
        return tag[:-1] + add + ">"

    return re.sub(r"<img\b[^>]*>", fix, html)


def glossary_parts():
    path = os.path.join(BASE, "glossary.json")
    data = json.load(open(path, encoding="utf-8"))
    n = len(data["entries"])
    payload = json.dumps({"entries": data["entries"]}, ensure_ascii=False).replace("</", "<\\/")
    script_tag = '<script type="application/json" id="gloss-data">' + payload + "</script>"
    button = ('<button id="gloss-btn" aria-label="略語集を開く" title="略語集 (a)">'
              '略語 A–Z<span class="kbd">a</span></button>')
    modal = f"""<div id="gloss-overlay" role="dialog" aria-modal="true" aria-labelledby="gloss-title">
  <div id="gloss-panel">
    <div id="gloss-head">
      <div id="gloss-title-row">
        <span id="gloss-title">略語 A–Z</span>
        <span id="gloss-sub">全 {n} 項目 ／ 行をクリックすると本文を検索・Esc で閉じる</span>
        <button id="gloss-close" aria-label="閉じる">&times;</button>
      </div>
      <input id="gloss-filter" type="search" placeholder="略語・英語・日本語で絞り込み" autocomplete="off" aria-label="略語を絞り込み">
      <div id="gloss-az" aria-label="頭文字で移動"></div>
    </div>
    <div id="gloss-body"></div>
  </div>
</div>"""
    return script_tag, button, modal, n


DESC = ("Ross手術の術式バリエーション・Pitfall・ラーニングカーブを、"
        "文献60編（PDF 53＋MMCTS 7）から手技レベルで統合したレビュー")


def build(md_path, html_path):
    text = open(md_path, encoding="utf-8").read()
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
    body_html = stamp_dimensions(body_html, os.path.dirname(md_path))

    if not title:
        m = re.search(r"<h1[^>]*>(.*?)</h1>", body_html)
        title = re.sub(r"<[^>]+>", "", m.group(1)) if m else "Ross手術 手技レビュー"

    gloss_json, gloss_btn, gloss_modal, _ = glossary_parts()

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{DESC}">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS_TEMPLATE}{afb.SEARCH_CSS}{afb.GLOSSARY_CSS}{FIG_CSS}</style>
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
    <div id="sidebar-header">目次 — 章立て</div>
    <nav id="sidebar-nav"></nav>
  </aside>
  <main class="content">
{body_html}
  </main>
</div>
<div id="sidebar-backdrop"></div>
<button id="sidebar-toggle" aria-label="目次を開く">&#9776;</button>
{gloss_btn}
{gloss_modal}
{gloss_json}
{TOC_SCRIPT}
{afb.GLOSS_SCRIPT}
{LIGHTBOX}
</body>
</html>
"""
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    open(html_path, "w", encoding="utf-8").write(html)
    print(f"  HTML: {html_path} ({os.path.getsize(html_path)/1024:.1f} KB)")


def main():
    if len(sys.argv) == 3:
        build(sys.argv[1], sys.argv[2])
    else:
        build(os.path.join(BASE, "md", "Ross_Technique_Review.md"),
              os.path.join(ROOT, "output", "ross_technique_review.html"))


if __name__ == "__main__":
    main()
