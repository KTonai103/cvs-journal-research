#!/usr/bin/env python3
"""Triage the harvested corpus: drop non-cardiac / non-robotic noise, then score
each record for how-to / pitfall / technique / training value and bucket it into
the review's chapters."""
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "corpus")

recs = json.load(open(os.path.join(OUT, "meta.json")))

# ---------------------------------------------------------------- exclusions
OTHER_SPECIALTY = re.compile(r"""
 prostat|hysterect|nephrect|partial\ nephr|colorect|rectal\ cancer|proctect|
 gastrect|esophagect|oesophagect|bariatric|sleeve\ gastrect|hernia|inguinal|
 cystect|bladder|kidney\ transplant|ureter|pyelopl|adrenalect|
 thyroid|parathyroid|tonsill|laryng|oropharyn|transoral|
 hepatect|pancreat|cholecystect|splenect|liver\ resect|
 endometri|myomect|oophor|sacrocolpopexy|ovarian|cervical\ cancer|vaginal|
 lobectomy|segmentectomy|lung\ cancer|pulmonary\ resect|thymect|mediastinal\ mass|
 pleural|chest\ wall\ tumor|
 spine|spinal|vertebr|arthroplast|knee|hip\ replace|orthop|
 exoskeleton|rehabilitat|gait|prosthetic\ limb|nanorobot|nanoparticle|
 dental|implantolog|ophthalm|retinal|cochlear|
 bronchoscop|colonoscop|capsule\ endoscop
""", re.I | re.X)

CARDIAC = re.compile(r"""
 cardiac|heart|mitral|aortic\ valve|tricuspid|pulmonic|coronary|CABG|TECAB|
 MIDCAB|internal\ mammary|internal\ thoracic|LIMA|RIMA|bypass\ graft|
 atrial\ septal|ventricular\ septal|patent\ foramen|myxoma|
 cardiopulmonary\ bypass|CPB|sternotomy|thoracotomy.*valve|
 atrial\ fibrillation|maze|left\ atrial\ appendage|epicardial\ lead|
 pacing\ lead|resynchron|left\ ventricular\ lead|
 annuloplasty|leaflet|chord|papillary|valvuloplast|valve\ repair|
 valve\ replacement|endocarditis|pericard|aorta|ascending\ aort|
 transplant.*heart|ventricular\ assist|LVAD
""", re.I | re.X)

ROBOTIC = re.compile(r"robot|da\ vinci|davinci|telemanipulat|telesurg|"
                     r"teleoperat|hugo|versius|dexter|senhance|hinotori|revo-i",
                     re.I)
ENDOSCOPIC = re.compile(r"totally\ endoscopic|endoscopic\ mitral|thoracoscopic\ mitral|"
                        r"minimally\ invasive\ mitral|endoscopic\ (cardiac|valve)|"
                        r"port-access|mini-?thoracotomy", re.I)

# ---------------------------------------------------------------- scoring
HOWTO_STRONG = [
    (r"how\ we\ do\ it|how\ to\ do|how\ i\ do", 6),
    (r"pitfall", 6),
    (r"tips\ and\ tricks|tips\b|tricks\b", 5),
    (r"step[-\ ]by[-\ ]step", 5),
    (r"surgical\ technique|operative\ technique|technical\ (aspect|consideration|note|detail)", 4),
    (r"lessons\ learned", 4),
    (r"troubleshoot", 4),
    (r"atlas|illustrat|schematic|video\ tutorial|multimedia", 4),
    (r"port\ placement|port\ position|trocar|docking|port\ site|port\ strateg", 6),
    (r"exposure|retract|insufflat|visuali[sz]ation", 3),
    (r"setup|set-up|patient\ position|room\ setup|bedside", 3),
    (r"training|curriculum|credential|proctor|simulat|proficiency|skills\ assessment", 5),
    (r"learning\ curve|CUSUM|initial\ experience|first\ \d+\ (case|patient)|program\ (development|build)", 4),
    (r"expert\ consensus|position\ (paper|statement)|guideline|recommendation", 5),
    (r"complication|conversion\ to\ sternotomy|conversion\ rate|adverse\ event|safety", 2),
    (r"patient\ selection|contraindicat|preoperative\ planning|CT\ (assessment|planning|criteria)", 4),
    (r"caveat|challenge|difficult|obstacle|limitation", 2),
    (r"review|state\ of\ the\ art|current\ status|contemporary|update|perspective|future", 2),
]
REVIEW_PT = {"Review", "Systematic Review", "Practice Guideline", "Guideline",
             "Consensus Development Conference", "Meta-Analysis"}

CHAPTERS = [
    ("mitral",   r"mitral|annuloplasty|Barlow|leaflet|chord|neochord|papillary"),
    ("avr",      r"aortic\ valve|aortotomy|AVR\b|aortic\ root"),
    ("tecab",    r"TECAB|coronary|CABG|MIDCAB|internal\ mammary|internal\ thoracic|"
                 r"LIMA|RIMA|anastomos|revasculari"),
    ("asd_tumor", r"atrial\ septal|septal\ defect|patent\ foramen|myxoma|"
                  r"cardiac\ tum|intracardiac\ mass"),
    ("arrhythmia", r"atrial\ fibrillation|maze|ablation|left\ atrial\ appendage|"
                   r"pacing\ lead|epicardial\ lead|resynchron|ventricular\ lead"),
    ("tricuspid_redo", r"tricuspid|reoperat|redo|repeat\ (cardiac|sternotomy)|"
                       r"previous\ sternotomy"),
    ("training", r"training|curriculum|credential|proctor|simulat|learning\ curve|"
                 r"proficiency|education|fellowship|CUSUM"),
    ("port_setup", r"port\ placement|port\ position|trocar|docking|exposure|"
                   r"retract|insufflat|patient\ position|setup|set-up"),
    ("future",    r"Hugo|Versius|Dexter|Senhance|Hinotori|Revo-i|single-port|"
                  r"telesurg|remote\ surgery|5G|artificial\ intelligence|"
                  r"machine\ learning|augmented\ reality|haptic|force\ feedback|"
                  r"autonomous|next-generation|future"),
]


def score(r):
    blob = f"{r['title']} {r['abstract']}"
    ti = r["title"]
    s = 0
    hits = []
    for pat, w in HOWTO_STRONG:
        if re.search(pat, ti, re.I):
            s += w * 2          # title hits weigh double
            hits.append(pat.split("|")[0].replace("\\ ", " "))
        elif re.search(pat, blob, re.I):
            s += w
    if set(r["ptypes"]) & REVIEW_PT:
        s += 4
    if r["pmc"]:
        s += 3                  # open access -> figures are extractable
    yr = int(r["year"]) if r["year"].isdigit() else 0
    if yr >= 2020:
        s += 3
    elif yr >= 2015:
        s += 1
    elif yr and yr < 2008:
        s -= 1
    if re.search(r"case report", " ".join(r["ptypes"]), re.I):
        s -= 3
    if r["n_authors"] <= 2 and not set(r["ptypes"]) & REVIEW_PT:
        s -= 1                  # editorials/letters without review value
    if re.search(r"^(letter|reply|comment|invited commentary|editorial)", ti, re.I):
        s -= 6
    if re.search(r"Editorial|Comment|Letter", " ".join(r["ptypes"])):
        s -= 5
    return s, hits


def chapters_of(r):
    blob = f"{r['title']} {r['abstract']}"
    out = [name for name, pat in CHAPTERS if re.search(pat, blob, re.I | re.X)]
    return out or ["general"]


# A paper only counts as cardiac-surgical if the *title* commits to it. Abstract-only
# mentions are how urology/thoracic/general-surgery papers leaked in (they cite
# "cardiac risk", "coronary disease", "aorta" incidentally).
CARDIAC_TITLE = re.compile(r"""
 cardiac\ surg|cardiac\ surgical|heart\ surg|cardiothoracic\ surg|
 mitral|tricuspid|aortic\ valve|valvular|valve\ (repair|replacement|surgery|disease)|
 coronary\ (artery\ bypass|bypass|revascular|surgery)|CABG|TECAB|MIDCAB|
 internal\ (mammary|thoracic)|LIMA|
 atrial\ septal|septal\ defect|patent\ foramen|myxoma|cardiac\ tum|
 atrial\ fibrillation|maze\ procedure|left\ atrial\ appendage|
 epicardial\ lead|pacing\ lead|ventricular\ lead|resynchroni|
 myectomy|endocarditis|pericardi|
 cardiopulmonary\ bypass|sternotomy|
 robotic\ cardiac|cardiac\ robotic|robotic\ heart|
 cardiac\ transplant|heart\ transplant|ventricular\ assist|LVAD|
 aortic\ (root|surgery|dissection|aneurysm)|ascending\ aorta
""", re.I | re.X)

kept, dropped = [], Counter()
for r in recs:
    blob = f"{r['title']} {r['abstract']}"
    ti = r["title"]
    if not blob.strip():
        dropped["empty"] += 1
        continue
    is_robo = bool(ROBOTIC.search(blob))
    is_endo = bool(ENDOSCOPIC.search(blob))
    is_card = bool(CARDIAC_TITLE.search(ti))
    if OTHER_SPECIALTY.search(ti):
        dropped["other_specialty_title"] += 1
        continue
    if not is_card:
        dropped["not_cardiac_title"] += 1
        continue
    if not (is_robo or is_endo):
        dropped["not_robotic"] += 1
        continue
    # catheter-based robotic navigation (EP labs) is a different discipline
    if re.search(r"catheter ablation|magnetic navigation|robotic magnetic|"
                 r"remote magnetic|Stereotaxis|Sensei|percutaneous coronary "
                 r"intervention|robotic PCI", ti, re.I):
        dropped["catheter_robotics"] += 1
        continue
    s, hits = score(r)
    r2 = dict(r)
    r2["score"] = s
    r2["hits"] = hits
    r2["chapters"] = chapters_of(r)
    r2["robotic"] = is_robo
    r2["endoscopic_only"] = is_endo and not is_robo
    kept.append(r2)

kept.sort(key=lambda x: -x["score"])
print("dropped:", dict(dropped))
print("kept:", len(kept))
print("chapter distribution:", Counter(c for k in kept for c in k["chapters"]))
print("robotic:", sum(1 for k in kept if k["robotic"]),
      " endoscopic-only:", sum(1 for k in kept if k["endoscopic_only"]))

with open(os.path.join(OUT, "triaged.json"), "w") as f:
    json.dump(kept, f, indent=1, ensure_ascii=False)

# human-readable shortlist of the top candidates
with open(os.path.join(OUT, "shortlist.txt"), "w") as f:
    for k in kept[:400]:
        f.write(f"[{k['score']:>3}] PMID {k['pmid']} ({k['year']}) "
                f"{'ROBO' if k['robotic'] else 'ENDO'} "
                f"{'PMC' if k['pmc'] else '---'} "
                f"{'/'.join(k['chapters'])}\n")
        f.write(f"      {k['title']}\n")
        f.write(f"      {k['journal']}  ptypes={','.join(k['ptypes'][:3])}\n\n")
print("wrote shortlist.txt")
