#!/usr/bin/env python3
"""Convert Obsidian-flavored Markdown to styled HTML for CVS Journal Research reports.

Usage: python3 convert_to_html.py [input.md] [output.html]
       python3 convert_to_html.py  # converts 2026_05 by default
"""

import re
import subprocess
import sys
import os

CALLOUT_STYLES = {
    "note":      ("#448aff", "#e8f0fe", "Note"),
    "info":      ("#448aff", "#e8f0fe", "Info"),
    "tip":       ("#00bfa5", "#e0f7f4", "Tip"),
    "success":   ("#00c853", "#e8f5e9", ""),
    "warning":   ("#ff9100", "#fff3e0", ""),
    "danger":    ("#ff5252", "#ffebee", ""),
    "important": ("#ff5252", "#ffebee", ""),
    "abstract":  ("#00b0ff", "#e1f5fe", "Abstract"),
    "question":  ("#64dd17", "#f1f8e9", "?"),
    "example":   ("#7c4dff", "#ede7f6", ""),
    "quote":     ("#9e9e9e", "#f5f5f5", ""),
    "bug":       ("#ff1744", "#fce4ec", "Bug"),
    "failure":   ("#ff5252", "#ffebee", ""),
    "todo":      ("#448aff", "#e8f0fe", "TODO"),
}

CSS_TEMPLATE = """
:root {
  --bg: #ffffff;
  --fg: #1a1a1a;
  --muted: #5c5c5c;
  --border: #d4d4d4;
  --accent: #2c3e50;
  --light-bg: #f7f8fa;
  --header-bg: #2c3e50;
  --header-fg: #ffffff;
  --link: #1565c0;
  --link-hover: #0d47a1;
  --sidebar-width: 288px;
  --sidebar-bg: #f7f8fa;
  --sidebar-active: #eef1f5;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
  font-family: "Noto Sans JP", -apple-system, BlinkMacSystemFont, "Hiragino Sans",
               "Helvetica Neue", Arial, sans-serif;
  font-size: 15px;
  line-height: 1.75;
  color: var(--fg);
  background: var(--bg);
}

.layout {
  display: flex;
  align-items: flex-start;
  min-height: 100vh;
}

main.content {
  flex: 1;
  min-width: 0;
  max-width: 900px;
  margin: 0 auto;
  padding: 32px 32px 80px;
}

/* Sidebar */
aside#sidebar {
  width: var(--sidebar-width);
  flex-shrink: 0;
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border);
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  padding: 22px 14px 28px;
  font-size: 0.82rem;
  z-index: 50;
  -webkit-overflow-scrolling: touch;
}

#sidebar-header {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--muted);
  text-transform: uppercase;
  padding: 0 8px 12px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 12px;
}

#sidebar-nav { display: flex; flex-direction: column; }

#sidebar-nav a {
  display: block;
  text-decoration: none;
  border-radius: 4px;
  transition: background 0.12s, color 0.12s;
  color: var(--fg);
}

#sidebar-nav a.nav-journal {
  font-weight: 700;
  color: var(--accent);
  padding: 8px 10px;
  font-size: 0.86rem;
  margin-top: 14px;
  border-left: 3px solid var(--accent);
  background: #eaeef3;
  border-radius: 0 4px 4px 0;
  line-height: 1.35;
}
#sidebar-nav a.nav-journal:first-child { margin-top: 0; }
#sidebar-nav a.nav-journal:hover { background: #dde3ea; }

#sidebar-nav a.nav-category {
  font-weight: 600;
  color: var(--muted);
  padding: 6px 10px 4px 16px;
  font-size: 0.74rem;
  text-transform: none;
  letter-spacing: 0.02em;
  margin-top: 6px;
  line-height: 1.4;
}
#sidebar-nav a.nav-category:hover { color: var(--accent); background: var(--sidebar-active); }

#sidebar-nav a.nav-paper {
  padding: 4px 10px 4px 26px;
  font-size: 0.76rem;
  line-height: 1.45;
  color: #444;
  border-left: 2px solid transparent;
  margin: 1px 0 1px 8px;
}
#sidebar-nav a.nav-paper:hover {
  background: var(--sidebar-active);
  color: var(--link);
}
#sidebar-nav a.nav-paper.active {
  background: var(--sidebar-active);
  color: var(--accent);
  font-weight: 600;
  border-left-color: var(--accent);
}
#sidebar-nav a.nav-journal.active,
#sidebar-nav a.nav-category.active { color: var(--accent); }

h1 {
  font-size: clamp(1.3rem, 4vw, 1.7rem);
  font-weight: 700;
  color: var(--accent);
  border-bottom: 3px solid var(--accent);
  padding-bottom: 14px;
  margin-bottom: 20px;
  line-height: 1.4;
}

h2 {
  font-size: clamp(1rem, 3vw, 1.18rem);
  font-weight: 700;
  color: var(--accent);
  border-left: 4px solid var(--accent);
  padding-left: 12px;
  margin: 44px 0 10px;
  line-height: 1.4;
}

h3 {
  font-size: clamp(0.92rem, 2.5vw, 1rem);
  font-weight: 600;
  color: var(--fg);
  margin: 28px 0 8px;
  line-height: 1.5;
}

h4 {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--muted);
  margin: 18px 0 6px;
}

p { margin: 8px 0; font-size: 0.9rem; }
strong { color: var(--fg); }

a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; color: var(--link-hover); }

hr { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 14px auto 4px;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: #fff;
}
img + em, p > img + em, figcaption {
  display: block;
  text-align: center;
  font-size: 0.78rem;
  color: var(--muted);
  margin: 4px auto 18px;
}

ul, ol { padding-left: 22px; margin: 8px 0; font-size: 0.9rem; }
li { margin-bottom: 5px; line-height: 1.6; }

/* Tables — horizontal scroll on mobile */
.table-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 12px 0 20px;
  border-radius: 6px;
  border: 1px solid var(--border);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.83rem;
  min-width: 400px;
}

thead th {
  background: var(--header-bg);
  color: var(--header-fg);
  font-weight: 600;
  padding: 10px 12px;
  text-align: left;
  font-size: 0.8rem;
  letter-spacing: 0.02em;
  white-space: nowrap;
}

tbody td {
  padding: 8px 12px;
  border-bottom: 1px solid #e8e8e8;
  vertical-align: top;
}

tbody td:first-child {
  font-weight: 600;
  color: var(--accent);
  background: var(--light-bg);
  white-space: nowrap;
}

tbody tr:last-child td { border-bottom: none; }
tbody tr:nth-child(even) td { background-color: #fafbfc; }
tbody tr:nth-child(even) td:first-child { background-color: #f0f1f3; }
tbody tr:hover td { background-color: #eef1f5; }
tbody tr:hover td:first-child { background-color: #e4e8ed; }

blockquote {
  background: var(--light-bg);
  border-left: 3px solid var(--border);
  padding: 10px 16px;
  margin: 12px 0 20px;
  font-size: 0.87rem;
  color: var(--muted);
  line-height: 1.65;
  border-radius: 0 4px 4px 0;
}
blockquote strong { color: var(--fg); }

mark {
  background: #fff3cd;
  padding: 1px 4px;
  border-radius: 2px;
  font-weight: 600;
}

.callout p { margin: 4px 0; }
.callout ul, .callout ol { margin: 4px 0 4px 18px; }
.callout table { font-size: 0.8rem; }

/* Sidebar toggle (mobile only) */
#sidebar-toggle {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 52px;
  height: 52px;
  font-size: 1.4rem;
  cursor: pointer;
  box-shadow: 0 3px 12px rgba(0,0,0,0.25);
  z-index: 200;
  align-items: center;
  justify-content: center;
}

#sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.42);
  z-index: 150;
}

@media print {
  .layout { display: block; }
  aside#sidebar, #sidebar-toggle, #sidebar-backdrop { display: none !important; }
  main.content { max-width: 100%; padding: 16px; font-size: 11px; margin: 0; }
  table { font-size: 9px; }
  h2 { break-after: avoid; }
}

@media (max-width: 960px) {
  main.content { padding: 24px 22px 80px; }
  aside#sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    width: 84vw;
    max-width: 320px;
    transform: translateX(-100%);
    transition: transform 0.22s ease;
    box-shadow: 2px 0 14px rgba(0,0,0,0.18);
    border-right: 1px solid var(--border);
  }
  aside#sidebar.open { transform: translateX(0); }
  #sidebar-backdrop.open { display: block; }
  #sidebar-toggle { display: flex; }
}

@media (max-width: 640px) {
  main.content { padding: 16px 14px 76px; font-size: 14px; }
  h2 { margin-top: 36px; }
  h3 { margin-top: 22px; }
  ul, ol { padding-left: 18px; }
  li, p { font-size: 0.88rem; }
  .callout { padding: 10px 12px !important; }
  blockquote { padding: 8px 12px; }
}

@media (max-width: 380px) {
  main.content { padding: 12px 10px 76px; font-size: 13px; }
  thead th { font-size: 0.72rem; padding: 8px; }
  tbody td { padding: 6px 8px; font-size: 0.8rem; }
}
"""

# DOM-based sidebar nav — no innerHTML with untrusted content
TOC_SCRIPT = """
<script>
(function() {
  var sidebar = document.getElementById('sidebar');
  var nav = document.getElementById('sidebar-nav');
  var btn = document.getElementById('sidebar-toggle');
  var backdrop = document.getElementById('sidebar-backdrop');
  if (!sidebar || !nav) return;

  var content = document.querySelector('main.content');
  var headings = (content || document).querySelectorAll('h2, h3, h4');
  var navLinks = [];

  headings.forEach(function(h, idx) {
    if (!h.id) h.id = 'heading-' + idx;
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent.replace(/\\s+/g, ' ').trim();
    if (h.tagName === 'H2') a.className = 'nav-journal';
    else if (h.tagName === 'H3') a.className = 'nav-category';
    else a.className = 'nav-paper';
    a.dataset.target = h.id;
    nav.appendChild(a);
    navLinks.push(a);
  });

  function setOpen(open) {
    if (!sidebar) return;
    sidebar.classList.toggle('open', open);
    if (backdrop) backdrop.classList.toggle('open', open);
  }

  if (btn) btn.addEventListener('click', function() {
    setOpen(!sidebar.classList.contains('open'));
  });
  if (backdrop) backdrop.addEventListener('click', function() { setOpen(false); });

  nav.addEventListener('click', function(e) {
    if (e.target.tagName === 'A' && window.matchMedia('(max-width: 960px)').matches) {
      setOpen(false);
    }
  });

  // Scroll spy via IntersectionObserver
  if ('IntersectionObserver' in window) {
    var current = null;
    var visibleIds = new Set();
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) visibleIds.add(entry.target.id);
        else visibleIds.delete(entry.target.id);
      });
      // Pick the first heading still in the viewport, in document order
      var firstId = null;
      for (var i = 0; i < headings.length; i++) {
        if (visibleIds.has(headings[i].id)) { firstId = headings[i].id; break; }
      }
      if (firstId && firstId !== current) {
        current = firstId;
        navLinks.forEach(function(l) {
          l.classList.toggle('active', l.dataset.target === firstId);
        });
        var active = nav.querySelector('a.active');
        if (active && typeof active.scrollIntoView === 'function') {
          var rect = active.getBoundingClientRect();
          var sbRect = sidebar.getBoundingClientRect();
          if (rect.top < sbRect.top || rect.bottom > sbRect.bottom) {
            active.scrollIntoView({ block: 'nearest' });
          }
        }
      }
    }, { rootMargin: '-10% 0px -70% 0px', threshold: 0 });
    headings.forEach(function(h) { observer.observe(h); });
  }
})();
</script>
"""


def strip_frontmatter(text):
    title = ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end]
            for line in fm.split("\n"):
                if line.startswith("title:"):
                    title = line[6:].strip().strip('"').strip("'")
            text = text[end+4:].lstrip("\n")
    return text, title


def convert_wikilinks(text):
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text


def convert_highlights(text):
    return re.sub(r'==(.*?)==', r'<mark>\1</mark>', text)


def pandoc_convert(md_text):
    try:
        proc = subprocess.run(
            ['pandoc', '-f', 'gfm', '-t', 'html5', '--wrap=none'],
            input=md_text, capture_output=True, text=True, check=True
        )
        return proc.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"pandoc error: {e}", file=sys.stderr)
        return md_text


def wrap_tables(html):
    """Wrap tables in .table-wrap for horizontal scroll on mobile."""
    return re.sub(r'(<table\b)', r'<div class="table-wrap">\1', html).replace(
        '</table>', '</table></div>'
    )


def convert_callouts(text):
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^> \[!(\w+)\]\s*(.*)$', lines[i])
        if m:
            ctype = m.group(1).lower()
            title_text = m.group(2).strip()
            style = CALLOUT_STYLES.get(ctype, CALLOUT_STYLES["note"])
            border_color, bg_color, default_label = style

            body_lines = []
            if title_text:
                if i + 1 < len(lines) and lines[i+1].startswith('> '):
                    pass
                else:
                    body_lines.append(title_text)
                    title_text = ""

            i += 1
            while i < len(lines) and lines[i].startswith('> '):
                body_lines.append(lines[i][2:])
                i += 1

            display_title = title_text if title_text else default_label
            if not body_lines and title_text:
                body_lines.append(title_text)
                display_title = default_label

            body_html = pandoc_convert('\n'.join(body_lines))

            title_html = (
                f'<div class="callout-title" style="color:{border_color};'
                f'font-weight:700;margin-bottom:4px;font-size:0.82rem;">'
                f'{display_title}</div>'
            ) if display_title else ''

            callout_html = (
                f'<div class="callout" style="background:{bg_color};'
                f'border-left:4px solid {border_color};padding:12px 16px;'
                f'margin:10px 0 18px;border-radius:4px;font-size:0.86rem;'
                f'line-height:1.65;">{title_html}{body_html}</div>'
            )
            result.append(callout_html)
        else:
            result.append(lines[i])
            i += 1

    return '\n'.join(result)


def convert_file(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    text, title = strip_frontmatter(text)
    text = convert_wikilinks(text)
    text = convert_highlights(text)
    text = convert_callouts(text)

    parts = re.split(r'(<div class="callout".*?</div>\n?)', text, flags=re.DOTALL)
    converted_parts = []
    for part in parts:
        if part.startswith('<div class="callout"'):
            converted_parts.append(part)
        else:
            converted_parts.append(pandoc_convert(part))
    body_html = '\n'.join(converted_parts)
    body_html = wrap_tables(body_html)

    if not title:
        m = re.search(r'<h1[^>]*>(.*?)</h1>', body_html)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1))

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="心臓外科・MCS・LVAD関連ジャーナル最新号 注目論文まとめ">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS_TEMPLATE}</style>
</head>
<body>
<div class="layout">
  <aside id="sidebar" aria-label="目次">
    <div id="sidebar-header">目次 — 雑誌・論文</div>
    <nav id="sidebar-nav"></nav>
  </aside>
  <main class="content">
{body_html}
  </main>
</div>
<div id="sidebar-backdrop"></div>
<button id="sidebar-toggle" aria-label="目次を開く">&#9776;</button>
{TOC_SCRIPT}
</body>
</html>
"""

    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = os.path.getsize(html_path) / 1024
    print(f"  Created: {os.path.basename(html_path)} ({size_kb:.1f} KB)")


def main():
    base = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) == 3:
        convert_file(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        md_path = sys.argv[1]
        name = os.path.splitext(os.path.basename(md_path))[0]
        html_path = os.path.join(base, "output", f"{name}.html")
        convert_file(md_path, html_path)
    else:
        md_dir = os.path.join(base, "MD")
        out_dir = os.path.join(base, "output")
        pairs = [
            ("cardiac_surgery_journals_2026_03.md", "journal_report_2026_03.html"),
            ("cardiac_surgery_journals_2026_04.md", "cardiac_surgery_journals_2026_04.html"),
            ("cardiac_surgery_journals_2026_05.md", "journal_report_2026_05.html"),
            ("cardiac_surgery_journals_2026_06.md", "journal_report_2026_06.html"),
        ]
        print("Converting Obsidian MD → styled HTML:")
        for md_name, html_name in pairs:
            md_path = os.path.join(md_dir, md_name)
            html_path = os.path.join(out_dir, html_name)
            if os.path.exists(md_path):
                convert_file(md_path, html_path)
            else:
                print(f"  SKIP: {md_name} not found")
        print("Done.")


if __name__ == "__main__":
    main()
