#!/usr/bin/env python3
"""Build a hyperlinked, easy-to-reference HTML for the Small-Annulus-AVR integrated review.

- Reuses convert_to_html.py (CSS, scroll-spy sidebar TOC, callouts, tables, pandoc).
- Converts [[md-basename]] wikilink citations into numbered superscripts [N] that link to
  a generated 参考文献 (references) section, where each entry carries clickable PubMed (PMID)
  and DOI hyperlinks. Citation keys are resolved against the YAML frontmatter of md/*.md.
- Non-paper wikilinks (e.g. [[_index]], [[tables/x]], [[protocol/y]]) render as plain text.

Usage: python3 build_review_html.py <review.md> <output.html>
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import convert_to_html as cth  # noqa: E402

MD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "md")

EXTRA_CSS = """
/* citation superscripts */
sup.cite { font-size: 0.7em; line-height: 0; white-space: nowrap; }
sup.cite a {
  color: var(--link); font-weight: 600; text-decoration: none;
  padding: 0 1px;
}
sup.cite a:hover { text-decoration: underline; }
/* reference list */
ol.ref-list { padding-left: 0; list-style: none; counter-reset: ref; font-size: 0.82rem; }
ol.ref-list > li {
  counter-increment: ref;
  position: relative;
  padding: 7px 8px 7px 40px;
  border-bottom: 1px solid #eee;
  line-height: 1.5;
}
ol.ref-list > li::before {
  content: counter(ref);
  position: absolute; left: 0; top: 7px;
  width: 30px; text-align: right;
  font-weight: 700; color: var(--accent);
}
ol.ref-list > li:target { background: #fff8e1; border-radius: 4px; }
.ref-title { font-weight: 600; color: var(--fg); }
.ref-meta { color: var(--muted); }
.ref-links a {
  display: inline-block; margin-right: 8px; margin-top: 2px;
  font-size: 0.78rem; font-weight: 600;
  padding: 1px 7px; border-radius: 3px; border: 1px solid var(--border);
  background: var(--light-bg);
}
.ref-links a.pmid { color: #0b6e4f; }
.ref-links a.doi { color: #8a4b08; }
.ref-links a:hover { text-decoration: none; background: #eef1f5; }
.review-meta { color: var(--muted); font-size: 0.82rem; margin: -8px 0 18px; }
"""


def parse_frontmatter(text):
    """Return dict of simple key:value frontmatter fields."""
    out = {}
    if not text.startswith("---"):
        return out
    end = text.find("\n---", 3)
    if end == -1:
        return out
    for line in text[3:end].split("\n"):
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
        if m:
            k, v = m.group(1), m.group(2).strip().strip('"').strip("'")
            if k not in out:
                out[k] = v
    return out


def load_citemap():
    """key (md basename) -> dict(title, authors, journal, citation, doi, pmid)."""
    cmap = {}
    for fn in os.listdir(MD_DIR):
        if not fn.endswith(".md") or fn.startswith("_Integrated"):
            continue
        key = fn[:-3]
        with open(os.path.join(MD_DIR, fn), encoding="utf-8") as f:
            fm = parse_frontmatter(f.read())
        cmap[key] = {
            "title": fm.get("title", key),
            "authors": fm.get("authors", ""),
            "journal": fm.get("journal", ""),
            "citation": fm.get("citation", ""),
            "doi": fm.get("doi", ""),
            "pmid": fm.get("pmid", ""),
        }
    return cmap


def short_authors(authors):
    if not authors:
        return ""
    # first author up to first comma/ampersand + et al.
    first = re.split(r',| and |&|;', authors)[0].strip()
    multi = bool(re.search(r',| and |&|;', authors))
    return f"{first}, et al." if multi else first


def convert_citations(text, cmap):
    """Replace [[key]] / [[key|alias]] / [[key#anchor]] (and md/ prefix).
    Paper keys -> numbered superscripts; others -> plain text. Returns (text, ordered_keys)."""
    order = []  # keys in order of first appearance

    def resolve(raw):
        raw = raw.strip()
        # split alias
        alias = None
        if "|" in raw:
            raw, alias = raw.split("|", 1)
            alias = alias.strip()
        raw = raw.strip()
        anchor = None
        if "#" in raw:
            raw, anchor = raw.split("#", 1)
        key = raw.strip()
        if key.startswith("md/"):
            key = key[3:]
        return key, alias, anchor

    def repl(m):
        key, alias, anchor = resolve(m.group(1))
        if key in cmap:
            if key not in order:
                order.append(key)
            n = order.index(key) + 1
            cite = cmap[key]
            tip = f'{short_authors(cite["authors"])} {cite["citation"]}'.strip()
            return (f'<sup class="cite"><a href="#ref-{n}" title="{_esc_attr(tip)}">'
                    f'[{n}]</a></sup>')
        # non-paper link -> plain text (alias, else last path segment, else key)
        disp = alias if alias else key.split("/")[-1]
        return disp

    text = re.sub(r'\[\[([^\]]+)\]\]', repl, text)
    return text, order


def _esc_attr(s):
    return s.replace('"', '&quot;').replace("<", "&lt;").replace(">", "&gt;")


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_reference_html(order, cmap):
    rows = []
    for key in order:
        c = cmap[key]
        n = order.index(key) + 1
        authors = _esc(c["authors"]) if c["authors"] else ""
        title = _esc(c["title"])
        meta = _esc(c["citation"] or c["journal"])
        links = []
        if c["pmid"] and c["pmid"] not in ("NR", ""):
            links.append(
                f'<a class="pmid" href="https://pubmed.ncbi.nlm.nih.gov/{c["pmid"]}/" '
                f'target="_blank" rel="noopener">PMID {c["pmid"]}</a>')
        if c["doi"] and c["doi"] not in ("NR", ""):
            links.append(
                f'<a class="doi" href="https://doi.org/{c["doi"]}" '
                f'target="_blank" rel="noopener">DOI</a>')
        links_html = f'<div class="ref-links">{"".join(links)}</div>' if links else ""
        rows.append(
            f'<li id="ref-{n}">'
            f'<span class="ref-meta">{authors} </span>'
            f'<span class="ref-title">{title}.</span> '
            f'<span class="ref-meta">{meta}.</span>'
            f'{links_html}</li>'
        )
    return ('<h2 id="references">参考文献 (References)</h2>\n'
            '<p class="review-meta">各文献の PMID は PubMed、DOI は出版社ページにリンクします。'
            '本文中の上付き番号 [N] をクリックすると該当文献へ移動します。</p>\n'
            '<ol class="ref-list">\n' + "\n".join(rows) + "\n</ol>")


def build(md_path, html_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    cmap = load_citemap()
    text, title = cth.strip_frontmatter(text)
    text, order = convert_citations(text, cmap)
    text = cth.convert_highlights(text)
    text = cth.convert_callouts(text)

    parts = re.split(r'(<div class="callout".*?</div>\n?)', text, flags=re.DOTALL)
    converted = []
    for part in parts:
        if part.startswith('<div class="callout"'):
            converted.append(part)
        else:
            converted.append(cth.pandoc_convert(part))
    body_html = "\n".join(converted)
    body_html = cth.wrap_tables(body_html)

    # append references
    body_html += "\n<hr>\n" + build_reference_html(order, cmap)

    if not title:
        m = re.search(r'<h1[^>]*>(.*?)</h1>', body_html)
        title = re.sub(r'<[^>]+>', '', m.group(1)) if m else "Small Annulus AVR Integrated Review"

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="狭小弁輪 SAVR と弁輪拡大術の統合レビュー（PMID/DOI ハイパーリンク付き）">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet">
<style>{cth.CSS_TEMPLATE}{EXTRA_CSS}</style>
</head>
<body>
<div class="layout">
  <aside id="sidebar" aria-label="目次">
    <div id="sidebar-header">目次</div>
    <nav id="sidebar-nav"></nav>
  </aside>
  <main class="content">
{body_html}
  </main>
</div>
<div id="sidebar-backdrop"></div>
<button id="sidebar-toggle" aria-label="目次を開く">&#9776;</button>
{cth.TOC_SCRIPT}
</body>
</html>
"""
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {html_path} ({os.path.getsize(html_path)/1024:.1f} KB)")
    print(f"  References hyperlinked: {len(order)} papers")
    # report any citations the review used that were unresolved is handled in convert (plain text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 build_review_html.py <review.md> <output.html>")
        sys.exit(1)
    build(sys.argv[1], sys.argv[2])
