#!/usr/bin/env python3
"""Slice the harvested corpus into per-topic digests for targeted agent reading."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
COR = os.path.join(HERE, "corpus")
recs = json.load(open(os.path.join(COR, "hemostat_pubmed.json"), encoding="utf-8"))

SLICES = {
    "hydrofit_polymer": r"hydrofit|hydrophilic (polymer|urethane)|urethane prepolymer|polyurethane.{0,30}(sealant|adhesive)|isocyanate",
    "bioglue_grf": r"bioglue|glutaraldehyde.{0,40}albumin|albumin.{0,20}glutaraldehyde|gelatin[- ]resorcin|GRF glue|resorcinol[- ]formal",
    "fibrin_sealant": r"fibrin (sealant|glue|adhesive)|bolheal|beriplast|tisseel|tissucol|evicel|artiss|vivostat|crosseal|quixil",
    "fibrin_patch": r"tachosil|tachocomb|tachotop|fibrin.{0,15}(patch|sponge|coated)|collagen.{0,20}fibrinogen.{0,20}thrombin|hemopatch|veriset",
    "flowable_gelatin": r"floseal|surgiflo|gelatin[- ]thrombin|flowable (gelatin|hemostat)|gelatin matrix",
    "orc_cellulose": r"surgicel|oxidi[sz]ed (regenerated )?cellulose|\bORC\b|tabotamp|gelita",
    "polysaccharide": r"arista|perclot|endoclot|polysaccharide (hemo|spheres)|starch.{0,20}hemostat|hemoblast",
    "collagen_gelatin_sponge": r"microfibrillar collagen|avitene|helistat|gelfoam|gelatin sponge|spongostan|surgifoam",
    "cyanoacrylate": r"cyanoacrylate|glubran|histoacryl|dermabond|aron alpha",
    "pga_felt": r"polyglycolic acid|neoveil|\bPGA (felt|sheet|mesh)|teflon felt|felt strip",
    "pegpolymer": r"coseal|progel|duraseal|adherus|polyethylene glycol.{0,20}(sealant|hydrogel)|PEG (sealant|hydrogel)",
    "complication_pseudoaneurysm": r"pseudoaneurysm|false aneurysm|anastomotic (rupture|dehiscence)|aortic wall (necrosis|damage|injury)|redissection|re-dissection",
    "complication_infection": r"mediastinitis|graft infection|prosthetic (valve )?infection|abscess|endocarditis|infected|infection|biofilm",
    "complication_other": r"foreign body|granuloma|embolism|emboli[sz]ation|anaphyla|antibod|coagulopathy|stenosis|compression|swelling|mass mimick|mimicking",
    "guideline_ce": r"guideline|consensus|systematic review|meta-analysis|cost-effectiveness|cost analysis|economic",
}

# Relevance gate: must plausibly be about a hemostatic/sealant product
RELEVANT = re.compile(
    r"hemostat|haemostat|sealant|glue|adhesive|fibrin|thrombin|cellulose|gelatin|gelatine|collagen|"
    r"hydrofit|bioglue|floseal|surgiflo|surgicel|tachosil|tachocomb|coseal|progel|arista|perclot|"
    r"cyanoacrylate|polyglycolic|neoveil|hemopatch|veriset|endoclot|bolheal|beriplast|tisseel|"
    r"resorcin|prepolymer", re.I)

os.makedirs(os.path.join(HERE, "corpus", "slices"), exist_ok=True)
index = {}
for name, pat in SLICES.items():
    rx = re.compile(pat, re.I)
    hits = []
    for r in recs:
        blob = f"{r['title']} {r['abstract']}"
        if not rx.search(blob):
            continue
        # complication slices additionally require product relevance
        if name.startswith("complication") or name == "guideline_ce":
            if not RELEVANT.search(blob):
                continue
        hits.append(r)
    hits.sort(key=lambda r: (r["year"] or "0"), reverse=True)
    index[name] = len(hits)
    path = os.path.join(COR, "slices", f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# SLICE: {name}  ({len(hits)} records)\n\n")
        for r in hits:
            f.write(f"### PMID {r['pmid']} ({r['year']}) — {r['journal']}\n")
            f.write(f"TITLE: {r['title']}\n")
            f.write(f"DOI: {r['doi']} | TYPE: {r['pubtype']}\n")
            f.write(f"ABSTRACT: {r['abstract'] or '(no abstract)'}\n\n")

for k, v in sorted(index.items(), key=lambda x: -x[1]):
    print(f"{v:>5}  {k}")
