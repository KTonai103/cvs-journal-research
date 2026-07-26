#!/usr/bin/env python3
"""PubMed harvest: robotic cardiac surgery technique / pitfalls / tips / training.

Multi-angle sweep. Emphasis on how-to, port placement, exposure, training,
and procedure-specific technique (MV repair, AVR, TECAB, ASD/tumor, arrhythmia,
tricuspid/redo), plus future platforms.
"""
import json
import os
import time
import urllib.parse
import urllib.request

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")
os.makedirs(OUT, exist_ok=True)

ROBO = '("robotic"[tiab] OR "robot-assisted"[tiab] OR "robotically"[tiab] OR "da Vinci"[tiab] OR "robot"[tiab] OR "telemanipulat*"[tiab])'
CARDIAC = '("cardiac surgery"[tiab] OR "cardiac"[tiab] OR "heart surgery"[tiab] OR "mitral"[tiab] OR "aortic valve"[tiab] OR "coronary"[tiab] OR "tricuspid"[tiab] OR "atrial"[tiab])'
HOWTO = '("technique"[tiab] OR "techniques"[tiab] OR "how we do it"[tiab] OR "how to"[tiab] OR "tips"[tiab] OR "tricks"[tiab] OR "pitfall*"[tiab] OR "lessons learned"[tiab] OR "step-by-step"[tiab] OR "setup"[tiab] OR "set-up"[tiab] OR "approach"[tiab] OR "strategy"[tiab] OR "operative"[tiab] OR "surgical technique"[tiab] OR "video"[tiab] OR "atlas"[tiab])'

QUERIES = {
    # --- 1. Core how-to / pitfalls, cross-procedure ---
    "01_robo_cardiac_howto": f'{ROBO} AND {CARDIAC} AND {HOWTO} AND ("2005"[dp]:"2026"[dp])',
    "02_robo_pitfalls": f'{ROBO} AND {CARDIAC} AND ("pitfall*"[tiab] OR "complication*"[tiab] OR "adverse"[tiab] OR "conversion"[tiab] OR "sternotomy conversion"[tiab] OR "troubleshoot*"[tiab] OR "failure"[tiab] OR "safety"[tiab]) AND ("2005"[dp]:"2026"[dp])',
    "03_robo_review_state": f'{ROBO} AND {CARDIAC} AND (review[pt] OR "state of the art"[tiab] OR "current status"[tiab] OR "expert consensus"[tiab] OR "position statement"[tiab] OR guideline[pt]) AND ("2015"[dp]:"2026"[dp])',

    # --- 2. Port placement / docking / exposure / instrument setup ---
    "04_port_placement": f'{ROBO} AND ("port placement"[tiab] OR "port position*"[tiab] OR "port site"[tiab] OR "trocar"[tiab] OR "docking"[tiab] OR "arm placement"[tiab] OR "incision placement"[tiab] OR "working port"[tiab] OR "camera port"[tiab]) AND ({CARDIAC} OR "thoracic"[tiab]) AND ("2000"[dp]:"2026"[dp])',
    "05_exposure_retraction": f'{ROBO} AND ("exposure"[tiab] OR "retraction"[tiab] OR "atrial retractor"[tiab] OR "left atrial retractor"[tiab] OR "CO2 insufflation"[tiab] OR "carbon dioxide insufflation"[tiab] OR "visualization"[tiab] OR "field"[tiab]) AND {CARDIAC} AND ("2000"[dp]:"2026"[dp])',
    "06_ct_planning": f'{ROBO} AND ("computed tomography"[tiab] OR "CT"[tiab] OR "preoperative planning"[tiab] OR "patient selection"[tiab] OR "contraindication*"[tiab] OR "chest wall"[tiab] OR "thoracic anatomy"[tiab]) AND {CARDIAC} AND ("2005"[dp]:"2026"[dp])',

    # --- 3. Training / simulation / learning curve / credentialing ---
    "07_training_curriculum": f'{ROBO} AND {CARDIAC} AND ("training"[tiab] OR "curriculum"[tiab] OR "education"[tiab] OR "credential*"[tiab] OR "proctor*"[tiab] OR "mentor*"[tiab] OR "fellowship"[tiab] OR "residency"[tiab] OR "certification"[tiab]) AND ("2005"[dp]:"2026"[dp])',
    "08_simulation": f'{ROBO} AND ("simulation"[tiab] OR "simulator"[tiab] OR "dry lab"[tiab] OR "wet lab"[tiab] OR "3D printed"[tiab] OR "three-dimensional print*"[tiab] OR "virtual reality"[tiab] OR "skills assessment"[tiab] OR "proficiency"[tiab]) AND ({CARDIAC} OR "valve"[tiab] OR "anastomosis"[tiab]) AND ("2005"[dp]:"2026"[dp])',
    "09_learning_curve": f'{ROBO} AND {CARDIAC} AND ("learning curve"[tiab] OR "CUSUM"[tiab] OR "case volume"[tiab] OR "institutional experience"[tiab] OR "first 100"[tiab] OR "initial experience"[tiab] OR "program development"[tiab] OR "team"[tiab]) AND ("2005"[dp]:"2026"[dp])',

    # --- 4. Mitral valve repair ---
    "10_robo_mitral_technique": f'{ROBO} AND ("mitral"[tiab]) AND {HOWTO} AND ("2005"[dp]:"2026"[dp])',
    "11_robo_mitral_outcomes": f'{ROBO} AND ("mitral"[tiab]) AND ("repair"[tiab] OR "annuloplasty"[tiab] OR "leaflet"[tiab] OR "chordal"[tiab] OR "neochord*"[tiab] OR "resection"[tiab] OR "sliding"[tiab] OR "commissur*"[tiab] OR "Barlow"[tiab]) AND ("2010"[dp]:"2026"[dp])',
    "12_robo_mitral_knot_suture": f'{ROBO} AND ("mitral"[tiab] OR "valve"[tiab]) AND ("knot"[tiab] OR "suture"[tiab] OR "Cor-Knot"[tiab] OR "automated fastener"[tiab] OR "nitinol"[tiab] OR "running suture"[tiab] OR "needle"[tiab]) AND ("2010"[dp]:"2026"[dp])',

    # --- 5. Aortic valve ---
    "13_robo_avr": f'{ROBO} AND ("aortic valve"[tiab]) AND ("replacement"[tiab] OR "repair"[tiab] OR "aortotomy"[tiab] OR "technique"[tiab] OR "feasibility"[tiab] OR "first"[tiab] OR "series"[tiab]) AND ("2000"[dp]:"2026"[dp])',

    # --- 6. TECAB / coronary ---
    "14_tecab": '("TECAB"[tiab] OR "totally endoscopic coronary artery bypass"[tiab] OR "totally endoscopic coronary"[tiab] OR "robotic coronary artery bypass"[tiab] OR "robotic-assisted coronary"[tiab] OR "MIDCAB"[tiab] AND "robot"[tiab]) AND ("2000"[dp]:"2026"[dp])',
    "15_robo_lima_hybrid": f'{ROBO} AND ("internal mammary"[tiab] OR "internal thoracic"[tiab] OR "LIMA"[tiab] OR "hybrid coronary revascularization"[tiab] OR "anastomo*"[tiab] OR "graft"[tiab]) AND ("coronary"[tiab] OR "bypass"[tiab]) AND ("2000"[dp]:"2026"[dp])',

    # --- 7. Others: ASD / septal / tumor ---
    "16_robo_asd_tumor": f'{ROBO} AND ("atrial septal defect"[tiab] OR "ASD"[tiab] OR "patent foramen"[tiab] OR "myxoma"[tiab] OR "cardiac tumor"[tiab] OR "cardiac tumour"[tiab] OR "intracardiac mass"[tiab] OR "septal defect"[tiab]) AND ("2000"[dp]:"2026"[dp])',

    # --- 8. Others: arrhythmia / LAA / leads ---
    "17_robo_af_laa_lead": f'{ROBO} AND ("atrial fibrillation"[tiab] OR "maze"[tiab] OR "ablation"[tiab] OR "left atrial appendage"[tiab] OR "pacing lead"[tiab] OR "epicardial lead"[tiab] OR "resynchron*"[tiab] OR "left ventricular lead"[tiab]) AND ("2000"[dp]:"2026"[dp])',

    # --- 9. Others: tricuspid / redo ---
    "18_robo_tricuspid_redo": f'{ROBO} AND ("tricuspid"[tiab] OR "reoperation"[tiab] OR "redo"[tiab] OR "reoperative"[tiab] OR "repeat cardiac"[tiab] OR "previous sternotomy"[tiab]) AND {CARDIAC} AND ("2005"[dp]:"2026"[dp])',

    # --- 10. Future / next-gen platforms / telesurgery ---
    "19_next_gen_platform": '("Hugo RAS"[tiab] OR "Versius"[tiab] OR "Dexter"[tiab] OR "Senhance"[tiab] OR "Hinotori"[tiab] OR "Revo-i"[tiab] OR "single-port robot*"[tiab] OR "SP robot*"[tiab] OR "next-generation robotic"[tiab] OR "new robotic platform"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "20_telesurgery_ai": f'{ROBO} AND ("telesurgery"[tiab] OR "remote surgery"[tiab] OR "5G"[tiab] OR "telerobotic"[tiab] OR "artificial intelligence"[tiab] OR "machine learning"[tiab] OR "augmented reality"[tiab] OR "haptic"[tiab] OR "force feedback"[tiab] OR "autonomous"[tiab]) AND ({CARDIAC} OR "surgery"[tiab]) AND ("2015"[dp]:"2026"[dp])',

    # --- 11. Complementary endoscopic MICS technique (limited use) ---
    "21_endoscopic_mics_technique": '("totally endoscopic"[tiab] OR "endoscopic mitral"[tiab] OR "thoracoscopic mitral"[tiab] OR "minimally invasive mitral"[tiab]) AND ("technique"[tiab] OR "port"[tiab] OR "how we do it"[tiab] OR "pitfall*"[tiab] OR "tips"[tiab] OR "exposure"[tiab] OR "learning curve"[tiab] OR "training"[tiab]) AND ("2010"[dp]:"2026"[dp])',

    # --- 12. Robotic cardiac outcomes/benchmarks (for evidence framing) ---
    "22_robo_benchmark_meta": f'{ROBO} AND {CARDIAC} AND ("meta-analysis"[pt] OR "meta-analysis"[tiab] OR "propensity"[tiab] OR "national"[tiab] OR "database"[tiab] OR "STS"[tiab] OR "registry"[tiab] OR "randomized"[tiab]) AND ("2018"[dp]:"2026"[dp])',
}


def eutil(path, params):
    params = dict(params)
    params.setdefault("tool", "cvs_journal_research")
    params.setdefault("email", "ktonai.cs@gmail.com")
    url = f"{BASE}/{path}?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if attempt == 3:
                raise
            print(f"    retry {attempt+1}: {e}")
            time.sleep(3 * (attempt + 1))


def main():
    all_pmids = {}
    for key, q in QUERIES.items():
        txt = eutil("esearch.fcgi", {
            "db": "pubmed", "term": q, "retmax": "600", "retmode": "json",
        })
        data = json.loads(txt)
        ids = data["esearchresult"].get("idlist", [])
        count = data["esearchresult"].get("count")
        print(f"{key}: count={count} fetched={len(ids)}")
        all_pmids[key] = ids
        with open(os.path.join(OUT, f"pmids_{key}.json"), "w") as f:
            json.dump({"query": q, "count": count, "ids": ids}, f, indent=1)
        time.sleep(0.4)

    union = sorted({p for ids in all_pmids.values() for p in ids}, key=int)
    with open(os.path.join(OUT, "pmids_union.json"), "w") as f:
        json.dump({"n": len(union), "ids": union,
                   "by_query": {k: len(v) for k, v in all_pmids.items()}}, f, indent=1)
    print(f"\nUNION: {len(union)} unique PMIDs")


if __name__ == "__main__":
    main()
