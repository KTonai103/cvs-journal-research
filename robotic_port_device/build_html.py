#!/usr/bin/env python3
"""Build the robotic-port-device review HTML.

Reuses hemostatic_agents/build_html.py (house CSS + sidebar TOC + full-text search),
overriding only the meta description.

Usage:
  python3 robotic_port_device/build_html.py
  python3 robotic_port_device/build_html.py in.md out.html
"""
import importlib.util
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, ROOT)

spec = importlib.util.spec_from_file_location(
    "hemo_build", os.path.join(ROOT, "hemostatic_agents", "build_html.py"))
hemo_build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hemo_build)

hemo_build.DESCRIPTION = (
    "ロボット心臓手術用「先端バルーン＋外周止血材つき胸壁ポート」構想の背景・先行技術・新規性検討。"
    "ポート創面出血の疫学、バルーントロカールと止血材一体型アクセスデバイスの先行技術、"
    "Applied Medical / Intuitive の特許ランドスケープ、hinotori を含む事業戦略")


def main():
    if len(sys.argv) == 3:
        hemo_build.build(sys.argv[1], sys.argv[2])
    else:
        md = os.path.join(BASE, "md", "robotic_port_device_review.md")
        out = os.path.join(ROOT, "output", "robotic_port_device_review.html")
        hemo_build.build(md, out)


if __name__ == "__main__":
    main()
