#!/usr/bin/env python3
"""Build a search-enabled, sidebar-navigated HTML report from a Markdown summary.

Reuses the house CSS / callout / pandoc pipeline from the project-root
convert_to_html.py, and ADDS:
  - a full-text search box in the sidebar (highlight + hit count + prev/next jump)
  - sidebar nav filtering by query
  - the existing heading-based TOC + scroll-spy + mobile drawer

Usage:
  python3 robotic_cpb/build_html.py [input.md] [output.html]
  python3 robotic_cpb/build_html.py   # defaults to the robotic CPB review
"""
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

SEARCH_CSS = """
/* ---- search box + results ---- */
#sidebar-search { padding: 0 8px 12px; position: sticky; top: 0; background: var(--sidebar-bg); z-index: 5; }
#search-input {
  width: 100%; padding: 8px 30px 8px 10px; font-size: 0.82rem;
  border: 1px solid var(--border); border-radius: 6px; background: #fff; color: var(--fg);
  font-family: inherit;
}
#search-input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 2px rgba(44,62,80,0.12); }
#search-clear {
  position: absolute; right: 16px; top: 7px; border: none; background: transparent;
  font-size: 1rem; color: var(--muted); cursor: pointer; line-height: 1; display: none;
}
#search-meta {
  display: none; align-items: center; gap: 6px; margin-top: 6px; font-size: 0.72rem; color: var(--muted);
}
#search-meta.show { display: flex; }
#search-count { flex: 1; }
#search-meta button {
  border: 1px solid var(--border); background: #fff; border-radius: 4px; cursor: pointer;
  width: 22px; height: 22px; font-size: 0.8rem; color: var(--accent); line-height: 1;
}
#search-meta button:hover { background: var(--sidebar-active); }
#sidebar-nav a.filtered-out { display: none; }
mark.search-hit { background: #ffe08a; color: inherit; padding: 0 1px; border-radius: 2px; }
mark.search-hit.current { background: #ff9100; color: #fff; box-shadow: 0 0 0 2px rgba(255,145,0,0.35); }

/* lead / meta blocks */
.doc-meta { font-size: 0.8rem; color: var(--muted); margin: -8px 0 18px; }
"""

# TOC (from headings) + search behaviour. Pure DOM, no innerHTML with content.
SCRIPT = r"""
<script>
(function () {
  var sidebar = document.getElementById('sidebar');
  var nav = document.getElementById('sidebar-nav');
  var btn = document.getElementById('sidebar-toggle');
  var backdrop = document.getElementById('sidebar-backdrop');
  var content = document.querySelector('main.content');
  if (!sidebar || !nav || !content) return;

  // ---------- build TOC ----------
  var headings = content.querySelectorAll('h2, h3, h4');
  var navLinks = [];
  headings.forEach(function (h, idx) {
    if (!h.id) h.id = 'heading-' + idx;
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent.replace(/\s+/g, ' ').trim();
    if (h.tagName === 'H2') a.className = 'nav-journal';
    else if (h.tagName === 'H3') a.className = 'nav-category';
    else a.className = 'nav-paper';
    a.dataset.target = h.id;
    nav.appendChild(a);
    navLinks.push(a);
  });

  function setOpen(open) {
    sidebar.classList.toggle('open', open);
    if (backdrop) backdrop.classList.toggle('open', open);
  }
  if (btn) btn.addEventListener('click', function () { setOpen(!sidebar.classList.contains('open')); });
  if (backdrop) backdrop.addEventListener('click', function () { setOpen(false); });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A' && window.matchMedia('(max-width: 960px)').matches) setOpen(false);
  });

  // ---------- scroll spy ----------
  if ('IntersectionObserver' in window) {
    var current = null, visible = new Set();
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) visible.add(en.target.id); else visible.delete(en.target.id);
      });
      var firstId = null;
      for (var i = 0; i < headings.length; i++) {
        if (visible.has(headings[i].id)) { firstId = headings[i].id; break; }
      }
      if (firstId && firstId !== current) {
        current = firstId;
        navLinks.forEach(function (l) { l.classList.toggle('active', l.dataset.target === firstId); });
        var act = nav.querySelector('a.active');
        if (act) {
          var r = act.getBoundingClientRect(), s = sidebar.getBoundingClientRect();
          if (r.top < s.top || r.bottom > s.bottom) act.scrollIntoView({ block: 'nearest' });
        }
      }
    }, { rootMargin: '-10% 0px -70% 0px', threshold: 0 });
    headings.forEach(function (h) { obs.observe(h); });
  }

  // ---------- full-text search ----------
  var input = document.getElementById('search-input');
  var clearBtn = document.getElementById('search-clear');
  var meta = document.getElementById('search-meta');
  var countEl = document.getElementById('search-count');
  var prevBtn = document.getElementById('search-prev');
  var nextBtn = document.getElementById('search-next');
  if (!input) return;

  var hits = [], curHit = -1, timer = null;

  function clearHits() {
    var marks = content.querySelectorAll('mark.search-hit');
    marks.forEach(function (m) {
      var p = m.parentNode;
      p.replaceChild(document.createTextNode(m.textContent), m);
      p.normalize();
    });
    hits = []; curHit = -1;
  }

  function highlight(q) {
    var lc = q.toLowerCase();
    var walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var t = node.parentNode && node.parentNode.tagName;
        if (t === 'SCRIPT' || t === 'STYLE') return NodeFilter.FILTER_REJECT;
        return node.nodeValue.toLowerCase().indexOf(lc) !== -1
          ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var text = node.nodeValue, lower = text.toLowerCase();
      var frag = document.createDocumentFragment(), idx = 0, pos;
      while ((pos = lower.indexOf(lc, idx)) !== -1) {
        if (pos > idx) frag.appendChild(document.createTextNode(text.slice(idx, pos)));
        var mk = document.createElement('mark');
        mk.className = 'search-hit';
        mk.textContent = text.slice(pos, pos + q.length);
        frag.appendChild(mk);
        hits.push(mk);
        idx = pos + q.length;
      }
      if (idx < text.length) frag.appendChild(document.createTextNode(text.slice(idx)));
      node.parentNode.replaceChild(frag, node);
    });
  }

  function filterNav(q) {
    var lc = q.toLowerCase();
    navLinks.forEach(function (l) {
      var match = !q || l.textContent.toLowerCase().indexOf(lc) !== -1;
      l.classList.toggle('filtered-out', !match);
    });
  }

  function gotoHit(i) {
    if (!hits.length) return;
    if (curHit >= 0 && hits[curHit]) hits[curHit].classList.remove('current');
    curHit = (i + hits.length) % hits.length;
    var m = hits[curHit];
    m.classList.add('current');
    m.scrollIntoView({ block: 'center', behavior: 'smooth' });
    countEl.textContent = (curHit + 1) + ' / ' + hits.length + ' 件';
  }

  function run(q) {
    clearHits();
    filterNav(q);
    if (!q || q.length < 2) {
      meta.classList.remove('show');
      clearBtn.style.display = q ? 'block' : 'none';
      return;
    }
    highlight(q);
    clearBtn.style.display = 'block';
    meta.classList.add('show');
    if (hits.length) { gotoHit(0); }
    else { countEl.textContent = '該当なし'; }
  }

  input.addEventListener('input', function () {
    clearTimeout(timer);
    var q = input.value.trim();
    timer = setTimeout(function () { run(q); }, 180);
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); gotoHit(curHit + (e.shiftKey ? -1 : 1)); }
    if (e.key === 'Escape') { input.value = ''; run(''); input.blur(); }
  });
  if (nextBtn) nextBtn.addEventListener('click', function () { gotoHit(curHit + 1); });
  if (prevBtn) prevBtn.addEventListener('click', function () { gotoHit(curHit - 1); });
  if (clearBtn) clearBtn.addEventListener('click', function () { input.value = ''; run(''); input.focus(); });

  // keyboard shortcut: "/" focuses search
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
})();
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
<meta name="description" content="ロボット支援下心臓手術における人工心肺管理の注意点・Pitfall — 心臓外科医・臨床工学技士・麻酔科医の視点別まとめ">
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
    <div id="sidebar-header">目次 — 視点・トピック</div>
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
        md = os.path.join(BASE, "md", "robotic_cpb_pitfalls_review.md")
        out = os.path.join(ROOT, "output", "robotic_cpb_pitfalls_review.html")
        build(md, out)


if __name__ == "__main__":
    main()
