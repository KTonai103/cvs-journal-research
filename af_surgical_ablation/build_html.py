#!/usr/bin/env python3
"""Build the AF surgical ablation review HTML (search-enabled, sidebar TOC).

Reuses the house CSS / callout / pandoc pipeline from the project-root
convert_to_html.py, and ADDS:
  - a full-text search box in the sidebar (highlight + hit count + prev/next jump)
  - sidebar nav filtering by query
  - the existing heading-based TOC + scroll-spy + mobile drawer
  - an always-available A-Z abbreviation glossary popup (top-right button, "a" shortcut)
    built from glossary.json; clicking an entry searches that abbreviation in the text

Usage:
  python3 af_surgical_ablation/build_html.py [input.md] [output.html]
  python3 af_surgical_ablation/build_html.py   # defaults to the AF surgical ablation review
"""
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

GLOSSARY_CSS = """
/* ---- abbreviation glossary (always-available popup) ---- */
#gloss-btn {
  position: fixed; top: 12px; right: 14px; z-index: 60;
  display: inline-flex; align-items: center; gap: 6px;
  padding: 7px 13px; border: 1px solid var(--border); border-radius: 999px;
  background: rgba(255,255,255,0.94); color: var(--accent);
  font-family: inherit; font-size: 0.78rem; font-weight: 700; cursor: pointer;
  box-shadow: 0 2px 10px rgba(0,0,0,0.10); backdrop-filter: blur(4px);
}
#gloss-btn:hover { background: #fff; box-shadow: 0 3px 14px rgba(0,0,0,0.16); }
#gloss-btn .kbd {
  font-weight: 400; font-size: 0.68rem; color: var(--muted);
  border: 1px solid var(--border); border-radius: 3px; padding: 0 4px;
}
#gloss-overlay {
  position: fixed; inset: 0; z-index: 70; display: none;
  background: rgba(20,26,32,0.46); padding: 24px 16px;
}
#gloss-overlay.open { display: block; }
#gloss-panel {
  max-width: 900px; margin: 0 auto; background: #fff; border-radius: 12px;
  box-shadow: 0 18px 50px rgba(0,0,0,0.30); display: flex; flex-direction: column;
  max-height: calc(100vh - 48px); overflow: hidden;
}
#gloss-head { padding: 14px 18px 10px; border-bottom: 1px solid var(--border); }
#gloss-title-row { display: flex; align-items: baseline; gap: 10px; }
#gloss-title { font-size: 0.98rem; font-weight: 700; color: var(--accent); }
#gloss-sub { font-size: 0.72rem; color: var(--muted); flex: 1; }
#gloss-close {
  border: none; background: transparent; font-size: 1.3rem; line-height: 1;
  color: var(--muted); cursor: pointer; padding: 0 2px;
}
#gloss-filter {
  width: 100%; margin-top: 10px; padding: 7px 10px; font-family: inherit; font-size: 0.82rem;
  border: 1px solid var(--border); border-radius: 6px; color: var(--fg);
}
#gloss-filter:focus { outline: none; border-color: var(--accent); }
#gloss-az { display: flex; flex-wrap: wrap; gap: 3px; margin-top: 9px; }
#gloss-az button {
  min-width: 22px; padding: 2px 5px; font-family: inherit; font-size: 0.72rem;
  border: 1px solid var(--border); border-radius: 4px; background: #fff;
  color: var(--accent); cursor: pointer;
}
#gloss-az button:hover { background: var(--sidebar-active); }
#gloss-az button:disabled { color: #c7ccd1; cursor: default; background: #fafbfc; }
#gloss-body { overflow-y: auto; padding: 6px 18px 18px; }
.gloss-group { margin-top: 14px; }
.gloss-letter {
  font-size: 0.8rem; font-weight: 700; color: var(--accent);
  border-bottom: 2px solid var(--sidebar-active); padding-bottom: 2px; margin-bottom: 6px;
}
.gloss-item {
  display: grid; grid-template-columns: 152px 1fr; gap: 10px;
  padding: 7px 6px; border-bottom: 1px solid #f0f2f4; cursor: pointer; border-radius: 4px;
}
.gloss-item:hover { background: var(--sidebar-active); }
.gloss-abbr { font-weight: 700; font-size: 0.84rem; color: var(--fg); word-break: break-word; }
.gloss-cat {
  display: inline-block; margin-top: 3px; font-size: 0.64rem; font-weight: 400;
  color: var(--muted); border: 1px solid var(--border); border-radius: 3px; padding: 0 4px;
}
.gloss-en { font-size: 0.76rem; color: var(--muted); font-style: italic; }
.gloss-ja { font-size: 0.82rem; line-height: 1.65; margin-top: 2px; }
.gloss-empty { padding: 18px 6px; font-size: 0.82rem; color: var(--muted); }
@media (max-width: 640px) {
  #gloss-btn { top: 8px; right: 8px; padding: 6px 10px; font-size: 0.72rem; }
  #gloss-btn .kbd { display: none; }
  #gloss-overlay { padding: 10px 8px; }
  .gloss-item { grid-template-columns: 1fr; gap: 2px; }
}
"""

GLOSS_SCRIPT = r"""
<script>
(function () {
  var btn = document.getElementById('gloss-btn');
  var overlay = document.getElementById('gloss-overlay');
  var bodyEl = document.getElementById('gloss-body');
  var azEl = document.getElementById('gloss-az');
  var filter = document.getElementById('gloss-filter');
  var closeBtn = document.getElementById('gloss-close');
  var dataEl = document.getElementById('gloss-data');
  if (!btn || !overlay || !bodyEl || !dataEl) return;

  var entries = [];
  try { entries = (JSON.parse(dataEl.textContent) || {}).entries || []; } catch (e) { return; }

  function letterOf(a) {
    var m = a.replace(/[^A-Za-z0-9]/g, '');
    var c = m.charAt(0).toUpperCase();
    return /[A-Z]/.test(c) ? c : '#';
  }
  entries.sort(function (x, y) {
    var a = x.a.replace(/[^A-Za-z0-9]/g, '').toUpperCase();
    var b = y.a.replace(/[^A-Za-z0-9]/g, '').toUpperCase();
    return a < b ? -1 : a > b ? 1 : 0;
  });

  var groups = {}, order = [];
  entries.forEach(function (e) {
    var L = letterOf(e.a);
    if (!groups[L]) { groups[L] = []; order.push(L); }
    groups[L].push(e);
  });
  order.sort();

  var itemNodes = [];
  order.forEach(function (L) {
    var g = document.createElement('section');
    g.className = 'gloss-group';
    g.id = 'gloss-g-' + L;
    var h = document.createElement('div');
    h.className = 'gloss-letter';
    h.textContent = L;
    g.appendChild(h);
    groups[L].forEach(function (e) {
      var row = document.createElement('div');
      row.className = 'gloss-item';
      row.tabIndex = 0;
      var left = document.createElement('div');
      var ab = document.createElement('div');
      ab.className = 'gloss-abbr';
      ab.textContent = e.a;
      left.appendChild(ab);
      if (e.cat) {
        var cat = document.createElement('span');
        cat.className = 'gloss-cat';
        cat.textContent = e.cat;
        left.appendChild(cat);
      }
      var right = document.createElement('div');
      if (e.en && e.en !== '—') {
        var en = document.createElement('div');
        en.className = 'gloss-en';
        en.textContent = e.en;
        right.appendChild(en);
      }
      var ja = document.createElement('div');
      ja.className = 'gloss-ja';
      ja.textContent = e.ja || '';
      right.appendChild(ja);
      row.appendChild(left);
      row.appendChild(right);
      row.dataset.hay = (e.a + ' ' + (e.en || '') + ' ' + (e.ja || '')).toLowerCase();
      function jump() {
        var q = e.a.split(/[\s/（(]/)[0].replace(/[^A-Za-z0-9²₂–\-]/g, '');
        close();
        if (q.length >= 2 && window.__afSearch) window.__afSearch(q);
      }
      row.addEventListener('click', jump);
      row.addEventListener('keydown', function (ev) { if (ev.key === 'Enter') jump(); });
      g.appendChild(row);
      itemNodes.push({ node: row, group: g, hay: row.dataset.hay });
    });
    bodyEl.appendChild(g);
  });

  var empty = document.createElement('div');
  empty.className = 'gloss-empty';
  empty.textContent = '該当する略語がありません。';
  empty.style.display = 'none';
  bodyEl.appendChild(empty);

  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').concat('#').forEach(function (L) {
    var b = document.createElement('button');
    b.textContent = L;
    if (!groups[L]) { b.disabled = true; }
    else {
      b.addEventListener('click', function () {
        var t = document.getElementById('gloss-g-' + L);
        if (t) bodyEl.scrollTop = t.offsetTop - bodyEl.offsetTop - 4;
      });
    }
    azEl.appendChild(b);
  });

  function applyFilter() {
    var q = (filter.value || '').trim().toLowerCase();
    var shown = 0;
    var perGroup = {};
    itemNodes.forEach(function (it) {
      var hit = !q || it.hay.indexOf(q) !== -1;
      it.node.style.display = hit ? '' : 'none';
      if (hit) { shown++; perGroup[it.group.id] = true; }
    });
    order.forEach(function (L) {
      var g = document.getElementById('gloss-g-' + L);
      if (g) g.style.display = perGroup[g.id] ? '' : 'none';
    });
    empty.style.display = shown ? 'none' : '';
  }
  filter.addEventListener('input', applyFilter);
  filter.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { filter.value = ''; applyFilter(); }
  });

  function open() {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    filter.focus();
  }
  function close() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }
  btn.addEventListener('click', open);
  if (closeBtn) closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', function (e) { if (e.target === overlay) close(); });
  document.addEventListener('keydown', function (e) {
    var t = document.activeElement, tag = t && t.tagName;
    var typing = tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT';
    if (e.key === 'Escape' && overlay.classList.contains('open')) { close(); return; }
    if (!typing && (e.key === 'a' || e.key === 'A') && !e.metaKey && !e.ctrlKey && !e.altKey) {
      e.preventDefault();
      overlay.classList.contains('open') ? close() : open();
    }
  });

  // deep link: .../af_surgical_ablation_review.html#gloss opens the glossary directly
  function fromHash() { if (location.hash === '#gloss') open(); }
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
</script>
"""


def glossary_parts():
    """Return (json_script_tag, button_html, modal_html, n_entries) from glossary.json."""
    path = os.path.join(BASE, "glossary.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    n = len(data.get("entries", []))
    payload = json.dumps({"entries": data["entries"]}, ensure_ascii=False)
    payload = payload.replace("</", "<\\/")  # never terminate the script element early
    script_tag = ('<script type="application/json" id="gloss-data">' + payload + "</script>")
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

  // exposed so the glossary popup can search an abbreviation in the text
  window.__afSearch = function (q) {
    input.value = q;
    run(q);
    if (window.matchMedia('(min-width: 961px)').matches) input.focus();
  };

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

    gloss_json, gloss_btn, gloss_modal, gloss_n = glossary_parts()

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="外科的心房細動治療の統合レビュー — Maze・lesion set・左心耳閉鎖・胸腔鏡下/ハイブリッド・PFA・AFMR/AFTR を177論文（71編フルテキスト精読）から統合">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS_TEMPLATE}{SEARCH_CSS}{GLOSSARY_CSS}</style>
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
{SCRIPT}
{GLOSS_SCRIPT}
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
        md = os.path.join(BASE, "md", "AF_surgical_ablation_review.md")
        out = os.path.join(ROOT, "output", "af_surgical_ablation_review.html")
        build(md, out)


if __name__ == "__main__":
    main()
