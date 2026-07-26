#!/usr/bin/env python3
"""Fetch an MMCTS tutorial as Markdown.

mmcts.org is a Laravel/Inertia SPA: curl gets a shell, but the whole article
(including the step-by-step `video_sections`) sits in the `data-page` JSON
attribute of `<div id="app">`.  No browser needed.

  python3 mmcts_fetch.py 2059 md/Kitahara_2025_..._MMCTS.md
  python3 mmcts_fetch.py 10.1510/mmcts.2025.065 out.md     # DOI also works
"""
import html
import json
import re
import subprocess
import sys

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def get(url):
    return subprocess.run(["curl", "-sL", "-A", UA, url],
                          capture_output=True, text=True).stdout


def resolve(ident):
    """tutorial number, mmcts.org URL or DOI -> tutorial URL"""
    if ident.startswith("http"):
        return ident
    if ident.startswith("10."):
        r = subprocess.run(["curl", "-sIL", "-A", UA, f"https://doi.org/{ident}"],
                           capture_output=True, text=True).stdout
        loc = re.findall(r"(?i)^location:\s*(\S+)", r, re.M)
        return loc[-1] if loc else ""
    return f"https://mmcts.org/tutorial/{ident}"


def unhtml(s):
    if not s:
        return ""
    s = re.sub(r"</(p|div|h[1-6]|li|tr)>", "\n\n", s)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<li[^>]*>", "- ", s)
    s = re.sub(r"</?(strong|b)>", "**", s)
    s = re.sub(r"</?(em|i)>", "*", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def fetch(ident):
    url = resolve(ident)
    page = get(url)
    m = re.search(r'data-page="([^"]+)"', page)
    if not m:
        raise SystemExit(f"no Inertia payload at {url}")
    post = json.loads(html.unescape(m.group(1)))["props"]["post"]

    out = ["---",
           f'title: "{post["title"]}"',
           f'source: "{url}"',
           f'doi: "{post.get("doi","")}"',
           f'published: "{(post.get("published_at") or "")[:10]}"',
           "---", ""]
    if post.get("video_link"):
        out += [f'Video: {post["video_link"]}  ({post.get("duration","?")} s)', ""]
    out += [f'Level: {post.get("expertise_level","")}', ""]

    for label, key in [("Abstract", "abstract"),
                       ("Introduction", "introduction"),
                       ("Patient presentation", "patient_presentation")]:
        if post.get(key):
            out += [f"## {label}", "", unhtml(post[key]), ""]

    if post.get("surgical_technique_prefix"):
        out += ["## Surgical technique", "", unhtml(post["surgical_technique_prefix"]), ""]
    else:
        out += ["## Surgical technique", ""]
    for i, sec in enumerate(post.get("video_sections") or [], 1):
        ttl = sec.get("title") or sec.get("name") or f"Step {i}"
        ts = sec.get("start_time") or sec.get("time") or ""
        out += [f"### {i}. {ttl}" + (f"  [{ts}]" if ts else ""), "",
                unhtml(sec.get("description") or sec.get("body") or ""), ""]
    if post.get("surgical_technique_suffix"):
        out += [unhtml(post["surgical_technique_suffix"]), ""]

    for label, key in [("Outcome and discussion", "outcome_and_discussion"),
                       ("Summary", "summary"),
                       ("Editorial commentary", "editorial_commentary"),
                       ("Authors", "author_and_post_information"),
                       ("References", "references")]:
        if post.get(key):
            out += [f"## {label}", "", unhtml(post[key]), ""]
    return "\n".join(out)


if __name__ == "__main__":
    text = fetch(sys.argv[1])
    if len(sys.argv) > 2:
        open(sys.argv[2], "w").write(text)
        print(f"{sys.argv[2]}: {len(text)} chars")
    else:
        print(text)
