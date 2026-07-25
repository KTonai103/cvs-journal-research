#!/usr/bin/env python3
"""PubMed harvest for surgical AF ablation / Maze / hybrid / AFMR review."""
import json
import time
import urllib.parse
import urllib.request
import os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")
os.makedirs(OUT, exist_ok=True)

QUERIES = {
    # --- 1. Cox-Maze / concomitant surgical ablation core ---
    "01_coxmaze_outcomes": '("Cox-Maze"[tiab] OR "Cox maze"[tiab] OR "maze procedure"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "02_concomitant_ablation": '("surgical ablation"[tiab] OR "concomitant ablation"[tiab]) AND ("atrial fibrillation"[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "03_sts_guideline": '(("atrial fibrillation"[tiab]) AND (guideline[pt] OR "practice guideline"[pt] OR "expert consensus"[tiab] OR "clinical practice guidelines"[tiab])) AND (surgical[tiab] OR surgery[tiab] OR ablation[tiab]) AND ("2023"[dp]:"2026"[dp])',
    # --- 2. Lesion set ---
    "04_box_lesion_pwi": '("posterior wall isolation"[tiab] OR "box lesion"[tiab] OR "left atrial posterior wall"[tiab]) AND ("atrial fibrillation"[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "05_pvi_vs_biatrial": '("pulmonary vein isolation"[tiab] AND (surgical[tiab] OR "biatrial"[tiab] OR "left atrial lesion"[tiab])) AND ("atrial fibrillation"[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "06_cryo_vs_rf": '((cryoablation[tiab] OR cryothermy[tiab] OR "cryoenergy"[tiab]) AND (radiofrequency[tiab] OR bipolar[tiab])) AND ("atrial fibrillation"[tiab]) AND (surgical[tiab] OR surgery[tiab] OR maze[tiab]) AND ("2015"[dp]:"2026"[dp])',
    # --- 3. Hybrid / convergent ---
    "07_hybrid_ablation": '("hybrid ablation"[tiab] OR "hybrid atrial fibrillation"[tiab] OR "staged hybrid"[tiab] OR "epicardial-endocardial"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "08_convergent": '("convergent procedure"[tiab] OR "CONVERGE trial"[tiab] OR "EPi-Sense"[tiab] OR "epicardial ablation"[tiab] AND "atrial fibrillation"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "09_thoracoscopic": '("thoracoscopic"[tiab] OR "totally thoracoscopic"[tiab] OR "minimally invasive surgical ablation"[tiab] OR "Wolf mini-maze"[tiab] OR "mini-maze"[tiab]) AND ("atrial fibrillation"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "10_surg_vs_catheter": '(("surgical ablation"[tiab] OR "thoracoscopic"[tiab] OR "hybrid"[tiab]) AND ("catheter ablation"[tiab])) AND ("atrial fibrillation"[tiab]) AND (trial[tiab] OR "meta-analysis"[pt] OR randomized[tiab] OR "network meta-analysis"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    # --- 4. LAA ---
    "11_laaos3": '("LAAOS"[tiab] OR "left atrial appendage occlusion"[tiab] OR "left atrial appendage closure"[tiab] OR "left atrial appendage exclusion"[tiab]) AND (surgical[tiab] OR surgery[tiab] OR "cardiac surgery"[tiab]) AND ("2020"[dp]:"2026"[dp])',
    "12_atriclip": '("AtriClip"[tiab] OR "epicardial clip"[tiab] OR "appendage clip"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    # --- 5. AFMR / atrial functional valve disease ---
    "13_afmr": '("atrial functional mitral regurgitation"[tiab] OR "atrial secondary mitral regurgitation"[tiab] OR "atrial functional MR"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "14_aftr": '("atrial functional tricuspid regurgitation"[tiab] OR "atrial secondary tricuspid regurgitation"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "15_afmr_surgery": '(("atrial functional"[tiab] OR "atrial secondary"[tiab]) AND (mitral[tiab] OR tricuspid[tiab])) AND (surgery[tiab] OR surgical[tiab] OR repair[tiab] OR annuloplasty[tiab] OR ablation[tiab]) AND ("2018"[dp]:"2026"[dp])',
    # --- 6. PFA ---
    "16_pfa_core": '("pulsed field ablation"[tiab] OR "pulsed-field ablation"[tiab] OR "electroporation"[tiab]) AND ("atrial fibrillation"[tiab]) AND ("2022"[dp]:"2026"[dp])',
    "17_pfa_surgical": '("pulsed field"[tiab] OR "electroporation"[tiab]) AND (epicardial[tiab] OR surgical[tiab] OR thoracoscopic[tiab] OR intraoperative[tiab]) AND ("atrial fibrillation"[tiab] OR "cardiac"[tiab]) AND ("2021"[dp]:"2026"[dp])',
    "18_pfa_redo_recurrence": '("pulsed field ablation"[tiab]) AND (recurrence[tiab] OR redo[tiab] OR repeat[tiab] OR "reconnection"[tiab] OR gap*[tiab] OR failure[tiab]) AND ("2023"[dp]:"2026"[dp])',
    # --- 7. LA size / predictors ---
    "19_la_size": '(("left atrial size"[tiab] OR "left atrial volume"[tiab] OR "left atrial diameter"[tiab] OR "left atrial enlargement"[tiab] OR "giant left atrium"[tiab])) AND ("atrial fibrillation"[tiab]) AND (ablation[tiab] OR maze[tiab] OR surgery[tiab]) AND ("2016"[dp]:"2026"[dp])',
    "20_la_reduction": '("left atrial reduction"[tiab] OR "left atrial plication"[tiab] OR "atrial volume reduction"[tiab] OR "LA reduction plasty"[tiab]) AND ("2010"[dp]:"2026"[dp])',
    # --- 8. concomitant with valve surgery ---
    "21_mitral_af_ablation": '(mitral[tiab]) AND ("atrial fibrillation"[tiab]) AND (ablation[tiab] OR maze[tiab]) AND (outcome*[tiab] OR survival[tiab] OR recurrence[tiab] OR randomized[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "22_cabg_avr_af": '((CABG[tiab] OR "coronary artery bypass"[tiab] OR "aortic valve replacement"[tiab])) AND ("atrial fibrillation"[tiab]) AND ("surgical ablation"[tiab] OR maze[tiab]) AND ("2018"[dp]:"2026"[dp])',
    # --- 9. rhythm outcome / sinus rhythm benefit ---
    "23_sinus_benefit": '("sinus rhythm"[tiab]) AND ("atrial fibrillation"[tiab]) AND (survival[tiab] OR mortality[tiab] OR stroke[tiab]) AND (ablation[tiab] OR surgical[tiab] OR maze[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "24_early_rhythm_control": '("early rhythm control"[tiab] OR "EAST-AFNET"[tiab]) AND ("2020"[dp]:"2026"[dp])',
    # --- 10. new devices / technology ---
    "25_devices": '(("bipolar clamp"[tiab] OR "Isolator"[tiab] OR "Cardioblate"[tiab] OR "nContact"[tiab] OR "Cobra Fusion"[tiab] OR "Estech"[tiab] OR "AtriCure"[tiab])) AND ("2015"[dp]:"2026"[dp])',
    "26_novel_energy": '("high-intensity focused ultrasound"[tiab] OR "microwave ablation"[tiab] OR "laser ablation"[tiab] OR "novel energy source"[tiab]) AND ("atrial fibrillation"[tiab]) AND ("2010"[dp]:"2026"[dp])',
    # --- 11. ganglionated plexi / autonomic, Marshall ---
    "27_gp_marshall": '("ganglionated plexi"[tiab] OR "ligament of Marshall"[tiab] OR "vein of Marshall"[tiab]) AND ("atrial fibrillation"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    # --- 12. Japanese / Asian perspective ---
    "28_japan": '("atrial fibrillation"[tiab]) AND (maze[tiab] OR "surgical ablation"[tiab]) AND (Japan*[tiab] OR "Japanese"[tiab] OR Asian[tiab]) AND ("2015"[dp]:"2026"[dp])',
    # --- 13. complication / pacemaker ---
    "29_complications": '(maze[tiab] OR "surgical ablation"[tiab]) AND ("atrial fibrillation"[tiab]) AND (pacemaker[tiab] OR complication*[tiab] OR "sinus node"[tiab] OR "esophageal"[tiab]) AND ("2016"[dp]:"2026"[dp])',
    # --- 14. anticoagulation after ablation/LAA ---
    "30_oac_after": '("atrial fibrillation"[tiab]) AND (anticoagulation[tiab] OR "oral anticoagulant"[tiab]) AND (("after ablation"[tiab] OR "post-ablation"[tiab] OR "appendage"[tiab])) AND (discontinu*[tiab] OR withdraw*[tiab] OR cessation[tiab] OR OPTION[tiab]) AND ("2020"[dp]:"2026"[dp])',
}


def eutil(path, params):
    params.setdefault("tool", "cvs-journal-research")
    params.setdefault("email", "ktonai.cs@gmail.com")
    url = f"{BASE}/{path}?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))


def search(term, retmax=200):
    js = json.loads(eutil("esearch.fcgi", {
        "db": "pubmed", "term": term, "retmax": retmax, "retmode": "json"}))
    return js["esearchresult"].get("idlist", []), js["esearchresult"].get("count")


def summaries(pmids):
    out = {}
    for i in range(0, len(pmids), 150):
        chunk = pmids[i:i + 150]
        js = json.loads(eutil("esummary.fcgi", {
            "db": "pubmed", "id": ",".join(chunk), "retmode": "json"}))
        res = js.get("result", {})
        for pid in res.get("uids", []):
            r = res[pid]
            doi = ""
            for aid in r.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid.get("value", "")
            out[pid] = {
                "pmid": pid,
                "title": r.get("title", "").rstrip("."),
                "journal": r.get("source", ""),
                "year": (r.get("pubdate", "") or "")[:4],
                "pubdate": r.get("pubdate", ""),
                "doi": doi,
                "authors": ", ".join(a["name"] for a in r.get("authors", [])[:3]),
                "lastauthor": r.get("lastauthor", ""),
                "pubtype": r.get("pubtype", []),
                "volume": r.get("volume", ""),
                "pages": r.get("pages", ""),
            }
        time.sleep(0.4)
    return out


def main():
    allrecs = {}
    index = {}
    for key, term in QUERIES.items():
        ids, count = search(term)
        index[key] = {"term": term, "count": count, "pmids": ids}
        print(f"{key:28s} hits={count:>6}  fetched={len(ids)}")
        time.sleep(0.4)
        recs = summaries(ids)
        for pid, r in recs.items():
            if pid in allrecs:
                allrecs[pid]["queries"].append(key)
            else:
                r["queries"] = [key]
                allrecs[pid] = r
    with open(os.path.join(OUT, "search_index.json"), "w") as f:
        json.dump(index, f, indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, "records.json"), "w") as f:
        json.dump(allrecs, f, indent=1, ensure_ascii=False)
    print(f"\nTOTAL unique PMIDs: {len(allrecs)}")


if __name__ == "__main__":
    main()
