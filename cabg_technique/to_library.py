#!/usr/bin/env python3
"""Move the 50 obtained PDFs into ~/Documents/All Papers/Clinical/Coronary/ under the
library naming rule (LastName_Year_KeyWords.pdf, see All Papers/CLAUDE.md), and leave
symlinks behind in cabg_technique/pdf/ so the figure pipeline keeps working.
"""
import json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.expanduser("~/Documents/All Papers/Clinical/Coronary")

# PMID -> KeyWords part of the library filename (abbreviation-forward, 3-6 tokens)
KEY = {
 "39484768": "Coronary_Artery_Anatomy_CardiacSurgery_Review",
 "12813693": "BeatingHeart_CABG_OperativeStrategy_Technique",
 "41977076": "Complex_CABG_Intraoperative_Challenges_Strategies",
 "10875598": "OPCAB_Exposure_Stabilization_Techniques",
 "11093536": "OPCAB_Exposure_MechanicalStabilization_Sternotomy",
 "10543532": "OPCAB_SingleSuture_Circumflex_Exposure",
 "15561035": "OPCAB_PosteriorVessel_DeepPericardialSuture_vs_ApicalSuction",
 "15276546": "OPCAB_90deg_CardiacDisplacement_Starfish_Positioner",
 "10969664": "OPCAB_HeartDisplacement_Hemodynamic_Tolerance",
 "10800817": "BeatingHeart_VerticalDisplacement_RightHeartSupport",
 "9594865":  "BeatingHeart_VerticalDisplacement_CoronaryFlow_Octopus",
 "36824043": "OPCAB_Hemodynamic_Management_Targets_Review",
 "39156549": "MICS_CABG_Standardized_Lateral_Posterior_Exposure",
 "34961523": "ITA_Harvesting_Preparation_SystematicReview",
 "34787965": "StepByStep_Graft_Harvesting_CABG_MMCTS",
 "32979482": "LIMA_Skeletonized_vs_Pedicled_MetaAnalysis",
 "38775645": "LIMA_Harvest_Pedicled_Skeletonized_Thunderbeat_RCT",
 "33171172": "LIMA_Skeletonization_Reduces_Bleeding_RCT",
 "42025666": "ITA_Harvest_Open_vs_IntactPleura_MetaAnalysis",
 "30505758": "Robotic_BITA_Harvest_Technique",
 "40589185": "Robotic_BITA_Harvesting_10Commandments",
 "34318106": "RadialArtery_MultiarterialCABG_Optimal_Harvest",
 "30552888": "RadialArtery_CABG_TechnicalAspects",
 "41432491": "RadialArtery_Endoscopic_vs_Open_Harvest_RCT",
 "31376117": "NoTouch_SVG_Harvesting_Technique_CABG",
 "33155775": "Endoscopic_NoTouch_SVG_Harvesting_MMCTS",
 "27525230": "GEA_Graft_CABG_30YearExperience",
 "30505752": "BITA_InSitu_vs_Composite_Configuration",
 "32439394": "BITA_LAD_Optimal_Configuration_LITA_vs_RITA",
 "27406988": "BITA_InSitu_vs_Ygraft_RCT",
 "36983276": "TotalArterial_Revascularization_MAG_Reconstruction_Options",
 "39718243": "ArterialConduits_CABG_SetPoint_Concept",
 "24973924": "SV_vs_RITA_Ycomposite_SAVE_RITA_RCT",
 "31539513": "SVG_Sequential_vs_Individual_Grafting",
 "30838388": "SVG_SnakeGraft_vs_Separate_SWEDEHEART",
 "28651939": "CompetitiveFlow_CABG_FFR_GraftConfiguration",
 "36094465": "NonsevereStenoses_CABG_CompetitiveFlow_Perspective",
 "33247735": "MultiArterial_CABG_Programme_StepwiseApproach",
 "41779085": "BypassGraft_Design_VirtualReality_Simulation",
 "34705350": "Coronary_Anastomosis_TipsAndTricks_MMCTS",
 "39617372": "Coronary_Anastomosis_Methods_KyobuGeka_JP",
 "34977715": "Coronary_Endarterectomy_DiffuseDisease_Technique",
 "28315286": "Coronary_Endarterectomy_vs_PatchAngioplasty_LAD",
 "33689738": "Clampless_ProximalAnastomosis_CalcifiedAorta_Foley",
 "34589167": "PorcelainAorta_CABG_Surgical_Strategies",
 "31421104": "EpiaorticUltrasound_Stroke_Prevention_CABG",
 "27298393": "TTFM_Intraoperative_GraftVerification_Standards",
 "35242366": "TTFM_Outcome_CABG_Surgeon_Trainee",
 "19114195": "Coronary_Anastomosis_Simulation_Improvement",
 "32891660": "Coronary_Anastomosis_Simulation_DirectedInterventions",
 "23456683": "DIY_Coronary_Anastomosis_Simulator",
 "34647125": "Humanoid_Simulator_CABG_Training",
 "38307118": "SingleLIMA_LAD_OPCAB_Training_Model",
 "39820718": "Trainees_BITA_Tgraft_Safety_Efficiency_CUSUM",
 "37425436": "OPCAB_TrainingCourse_QualityControl_CUSUM",
 "14643813": "OPCAB_LearningCurve_SafeEvolution",
}


def lastname(a):
    a = (a or "").strip()
    parts = a.split()
    if len(parts) > 1 and len(parts[-1]) <= 3 and parts[-1].isupper():
        parts = parts[:-1]                       # drop the initials token
    name = " ".join(parts)
    return (name.replace("ü", "u").replace("ö", "o").replace("ä", "a")
                .replace("é", "e").replace("è", "e").replace("í", "i")
                .replace("á", "a").replace("ñ", "n").replace("ç", "c")
                .replace("-", "").replace(" ", ""))


def main(apply):
    os.makedirs(LIB, exist_ok=True)
    rows = json.load(open(os.path.join(HERE, "raw/download_status.json")))
    got = [r for r in rows if r["status"] == "ok"]
    missing = [r["pmid"] for r in got if r["pmid"] not in KEY]
    if missing:
        print("no KEY for:", missing)
        return 1
    for r in sorted(got, key=lambda r: r["file"]):
        src = os.path.join(HERE, "pdf", r["file"])
        dst = os.path.join(LIB, f"{lastname(r['first_author'])}_{r['year']}_{KEY[r['pmid']]}.pdf")
        mark = "exists" if os.path.exists(dst) else "move "
        print(f"{mark} {os.path.basename(dst)}")
        if apply and not os.path.islink(src):
            if not os.path.exists(dst):
                shutil.move(src, dst)
            elif os.path.exists(src):
                os.remove(src)
            os.symlink(dst, src)
    print(f"\n{len(got)} papers -> {LIB}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
