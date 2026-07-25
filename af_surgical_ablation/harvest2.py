#!/usr/bin/env python3
"""Targeted supplementary search: landmark trials + key surgical-AF authors."""
import json, os, time
from harvest import search, summaries, OUT

TARGETED = {
    "T01_LAAOS3_primary": '("LAAOS III"[tiab] OR "Left Atrial Appendage Occlusion Study"[tiab])',
    "T02_CTSN_gillinov": '("surgical ablation"[tiab] OR "ablation"[ti]) AND ("mitral"[tiab]) AND (Gillinov[au] OR "Cardiothoracic Surgical Trials Network"[tiab] OR CTSN[tiab])',
    "T03_damiano": '(Damiano RJ[au] OR "Damiano R"[au]) AND ("atrial fibrillation"[tiab] OR maze[tiab])',
    "T04_ad_niv": '(Ad N[au]) AND ("atrial fibrillation"[tiab] OR maze[tiab] OR ablation[tiab])',
    "T05_melby_schuessler": '(Melby SJ[au] OR Schuessler RB[au] OR "Khiabani AJ"[au] OR "MacGregor RM"[au]) AND ("atrial fibrillation"[tiab])',
    "T06_wolf_minimaze": '("Wolf mini-maze"[tiab] OR "Wolf minimaze"[tiab] OR "mini-maze"[tiab] OR "minimaze"[tiab])',
    "T07_sts_database_util": '("Society of Thoracic Surgeons"[tiab] OR "STS database"[tiab] OR "STS Adult Cardiac Surgery Database"[tiab]) AND ("atrial fibrillation"[tiab]) AND (ablation[tiab] OR "appendage"[tiab])',
    "T08_gap_conduction": '(("conduction gap"[tiab] OR "gaps"[tiab] OR "transmurality"[tiab] OR "transmural lesion"[tiab] OR "exit block"[tiab] OR "entrance block"[tiab])) AND ("surgical ablation"[tiab] OR maze[tiab] OR epicardial[tiab]) AND ("atrial fibrillation"[tiab])',
    "T09_af_after_maze_redo": '(("recurrent atrial"[tiab] OR "atrial tachycardia"[tiab] OR "redo"[tiab] OR "repeat ablation"[tiab])) AND (maze[tiab] OR "surgical ablation"[tiab]) AND ("mapping"[tiab] OR "catheter"[tiab]) AND ("2015"[dp]:"2026"[dp])',
    "T10_afmr_annuloplasty_recur": '(("mitral"[tiab] AND annuloplasty[tiab])) AND ("atrial fibrillation"[tiab] OR "atrial functional"[tiab]) AND (recurrent[tiab] OR recurrence[tiab] OR durability[tiab] OR "residual"[tiab]) AND ("2015"[dp]:"2026"[dp])',
    "T11_laa_electrical": '("left atrial appendage isolation"[tiab] OR "LAA isolation"[tiab] OR "BELIEF trial"[tiab]) AND ("atrial fibrillation"[tiab])',
    "T12_poaf_prevention": '("postoperative atrial fibrillation"[tiab]) AND (prevent*[tiab]) AND ("posterior pericardiotomy"[tiab] OR "botulinum"[tiab] OR "denervation"[tiab] OR "colchicine"[tiab] OR "amiodarone"[tiab]) AND ("2020"[dp]:"2026"[dp])',
    "T13_af_hf_ablation": '("atrial fibrillation"[tiab]) AND ("heart failure"[tiab]) AND (ablation[tiab]) AND ("CASTLE-AF"[tiab] OR "CASTLE-HTx"[tiab] OR "CABANA"[tiab] OR "randomized"[ti]) AND ("2018"[dp]:"2026"[dp])',
    "T14_screening_ai_ecg": '("atrial fibrillation"[tiab]) AND ("artificial intelligence"[tiab] OR "machine learning"[tiab] OR "deep learning"[tiab]) AND (predict*[tiab] OR ablation[tiab] OR "substrate"[tiab]) AND ("2023"[dp]:"2026"[dp])',
    "T15_atrial_cardiomyopathy": '("atrial cardiomyopathy"[tiab] OR "atrial myopathy"[tiab] OR "atrial fibrosis"[tiab]) AND ("2020"[dp]:"2026"[dp])',
    "T16_lge_mri_utah": '("late gadolinium"[tiab] OR "DECAAF"[tiab] OR "atrial fibrosis"[tiab]) AND (MRI[tiab] OR "magnetic resonance"[tiab]) AND ("atrial fibrillation"[tiab]) AND (ablation[tiab])',
    "T17_ep_devices_new": '("Hybrid AF"[tiab] OR "EPi-Sense"[tiab] OR "AtriCure"[tiab] OR "Isolator Synergy"[tiab] OR "EnCompass"[tiab] OR "cryoICE"[tiab] OR "CryoSphere"[tiab])',
    "T18_totally_thoracoscopic_jpn": '("thoracoscopic"[tiab] OR "video-assisted"[tiab]) AND ("atrial fibrillation"[tiab]) AND (ablation[tiab]) AND ("box lesion"[tiab] OR "left atrial appendage"[tiab] OR "ganglionated"[tiab])',
    "T19_af_after_tavr_savr": '("atrial fibrillation"[tiab]) AND (TAVR[tiab] OR TAVI[tiab] OR "transcatheter aortic valve"[tiab]) AND (ablation[tiab] OR "appendage"[tiab] OR outcome*[tiab]) AND ("2022"[dp]:"2026"[dp])',
    "T20_economics_cost": '("atrial fibrillation"[tiab]) AND (ablation[tiab]) AND ("cost-effectiveness"[tiab] OR "cost effectiveness"[tiab] OR "economic evaluation"[tiab] OR "health economic"[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "T21_afmr_la_reverse": '(("left atrial"[tiab] AND ("reverse remodeling"[tiab] OR "reverse remodelling"[tiab]))) AND ("atrial fibrillation"[tiab] OR "mitral regurgitation"[tiab]) AND ("2018"[dp]:"2026"[dp])',
    "T22_tricuspid_concomitant": '("tricuspid"[tiab]) AND ("atrial fibrillation"[tiab]) AND (("concomitant"[tiab] AND (repair[tiab] OR annuloplasty[tiab])) OR "maze"[tiab]) AND ("2019"[dp]:"2026"[dp])',
    "T23_pfa_surgical_clamp": '("pulsed field"[tiab] OR "nanosecond"[tiab] OR "electroporation"[tiab]) AND (clamp[tiab] OR "surgical"[tiab] OR "Cox-maze"[tiab] OR "beating heart"[tiab])',
    "T24_history_cox": '("Cox JL"[au] OR "Cox James"[au]) AND (maze[tiab] OR "atrial fibrillation"[tiab])',
    "T25_lesion_set_longterm": '("lesion set"[tiab]) AND ("atrial fibrillation"[tiab]) AND (surgical[tiab] OR maze[tiab] OR "cardiac surgery"[tiab])',
}


def main():
    path = os.path.join(OUT, "records.json")
    allrecs = json.load(open(path))
    index = json.load(open(os.path.join(OUT, "search_index.json")))
    for key, term in TARGETED.items():
        ids, count = search(term, retmax=120)
        index[key] = {"term": term, "count": count, "pmids": ids}
        print(f"{key:28s} hits={count:>6}  fetched={len(ids)}")
        time.sleep(0.4)
        for pid, r in summaries(ids).items():
            if pid in allrecs:
                allrecs[pid]["queries"].append(key)
            else:
                r["queries"] = [key]
                allrecs[pid] = r
    json.dump(index, open(os.path.join(OUT, "search_index.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(allrecs, open(path, "w"), indent=1, ensure_ascii=False)
    print(f"\nTOTAL unique PMIDs: {len(allrecs)}")


if __name__ == "__main__":
    main()
