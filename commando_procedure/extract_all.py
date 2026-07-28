#!/usr/bin/env python3
"""Batch raster extraction for the Commando integrated review figures."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.expanduser(
    "~/.claude/skills/paper-figure-extraction/scripts/extract_images.py")
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

# (pdf stem, page, xref, output name)
JOBS = [
    # ---- Yi 2025 narrative review: 11 intraoperative / schematic figures ----
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 2, 7, "yi_f01.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 4, 34, "yi_f02.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 5, 52, "yi_f03.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 5, 54, "yi_f04.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 6, 72, "yi_f05.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 7, 83, "yi_f06.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 7, 85, "yi_f07.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 8, 94, "yi_f08.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 9, 108, "yi_f09.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 9, 110, "yi_f10.png"),
    ("Yi_CommandoProcedureNarrativeReview_GenThoracCardiovascSurg_2025", 10, 121, "yi_f11.png"),
    # ---- von Zeppelin 2025 (Medicina, CC BY) technique figures ----
    ("vonZeppelin_SurgeryCardiacSkeletonDestruction_Medicina_2025", 3, 164, "vz_f02.png"),
    ("vonZeppelin_SurgeryCardiacSkeletonDestruction_Medicina_2025", 4, 171, "vz_f03.png"),
    # ---- Navia 2010: incorporated aortomitral homograft ----
    ("Navia_IncorporatedAortomitralHomograft_JTCVS_2010", 2, 4, "navia10_a.png"),
    ("Navia_IncorporatedAortomitralHomograft_JTCVS_2010", 2, 5, "navia10_b.png"),
    ("Navia_IncorporatedAortomitralHomograft_JTCVS_2010", 2, 6, "navia10_c.png"),
    ("Navia_IncorporatedAortomitralHomograft_JTCVS_2010", 3, 11, "navia10_d.png"),
    ("Navia_IncorporatedAortomitralHomograft_JTCVS_2010", 3, 12, "navia10_e.png"),
    ("Navia_IncorporatedAortomitralHomograft_JTCVS_2010", 3, 13, "navia10_f.png"),
    # ---- Navia 2023 hemi-Commando ----
    ("Navia_HemiCommandoProcedure_JTCVSTech_2023", 2, 13, "navia23_f01.png"),
    # ---- Elgharably 2018 hemi-Commando ----
    ("Elgharably_HemiCommandoHomograftDVE_EJCTS_2018", 2, 29, "elg_f01.png"),
    ("Elgharably_HemiCommandoHomograftDVE_EJCTS_2018", 5, 76, "elg_f02.png"),
    ("Elgharably_HemiCommandoHomograftDVE_EJCTS_2018", 6, 121, "elg_f03.png"),
    # ---- Aphram 2021 en bloc root Commando ----
    ("Aphram_EnBlocRootCommandoBrussels_JTCVSTech_2021", 2, 7, "aphram_f01.png"),
    # ---- Forteza-Gil 2025 Barcelona ----
    ("FortezaGil_CommandoVariantsIntervalvularFibrosa_EJCTS_2025", 3, 40, "forteza_f01.png"),
    ("FortezaGil_CommandoVariantsIntervalvularFibrosa_EJCTS_2025", 5, 77, "forteza_f02.png"),
    ("FortezaGil_CommandoVariantsIntervalvularFibrosa_EJCTS_2025", 5, 78, "forteza_f03.png"),
    # ---- Iaccarino 2023 intraoperative photographs ----
    ("Iaccarino_SurgicalChallengesIEStateOfArt_JClinMed_2023", 11, 167, "iac_f03.png"),
    ("Iaccarino_SurgicalChallengesIEStateOfArt_JClinMed_2023", 11, 168, "iac_f04.png"),
    # ---- Jarral 2024 TAVR-IE -> Commando ----
    ("Jarral_TAVREndocarditisCommandoProcedure_JTCVSTech_2024", 2, 6, "jarral_f01.png"),
    ("Jarral_TAVREndocarditisCommandoProcedure_JTCVSTech_2024", 2, 7, "jarral_f02.png"),
    # ---- Kim 2013 Samsung schematics ----
    ("Kim_AortomitralFibrousBodyDVR_AnnThoracSurg_2013", 3, 141, "kim13_f01.png"),
    ("Kim_AortomitralFibrousBodyDVR_AnnThoracSurg_2013", 4, 148, "kim13_f02.png"),
    ("Kim_AortomitralFibrousBodyDVR_AnnThoracSurg_2013", 5, 164, "kim13_f03.png"),
    # ---- Marin-Cuartas 2023 Leipzig ----
    ("MarinCuartas_HemiCommandoLeipzig_EJCTS_2023", 4, 47, "marin_f02.png"),
    # ---- Matsuzaki 2024 aorto-annulo-septotomy ----
    ("Matsuzaki_ModifiedCommandoAortoAnnuloSeptotomy_ICVTS_2024", 2, 22, "matsu_f01.png"),
    ("Matsuzaki_ModifiedCommandoAortoAnnuloSeptotomy_ICVTS_2024", 3, 46, "matsu_f02.png"),
    ("Matsuzaki_ModifiedCommandoAortoAnnuloSeptotomy_ICVTS_2024", 4, 60, "matsu_f03.png"),
    # ---- Navia 2019 largest series ----
    ("Navia_InvasiveValvularIEAortomitralFibrosa_AnnThoracSurg_2019", 2, 14, "navia19_f01.png"),
    ("Navia_InvasiveValvularIEAortomitralFibrosa_AnnThoracSurg_2019", 3, 24, "navia19_f02.png"),
    ("Navia_InvasiveValvularIEAortomitralFibrosa_AnnThoracSurg_2019", 7, 67, "navia19_f03.png"),
    ("Navia_InvasiveValvularIEAortomitralFibrosa_AnnThoracSurg_2019", 8, 79, "navia19_f04.png"),
    ("Navia_InvasiveValvularIEAortomitralFibrosa_AnnThoracSurg_2019", 9, 88, "navia19_f05.png"),
    # ---- Nosaka 2024 emergency root-Commando ----
    ("Nosaka_EmergencyRootCommando_ICVTS_2024", 2, 18, "nosaka_f01.png"),
    ("Nosaka_EmergencyRootCommando_ICVTS_2024", 3, 32, "nosaka_f02.png"),
    # ---- Rheault-Henry 2025 emergent hemi-Commando ----
    ("RheaultHenry_EmergentHemiCommando_JTCVSTech_2025", 2, 6, "rheault_f01.png"),
    ("RheaultHenry_EmergentHemiCommando_JTCVSTech_2025", 2, 7, "rheault_f02.png"),
    # ---- Simpson 2023 post-Commando anatomy for VIV ----
    ("Simpson_AnatomicConsiderationsPostCommando_EJCTS_2023", 3, 36, "simpson_f01.png"),
    ("Simpson_AnatomicConsiderationsPostCommando_EJCTS_2023", 5, 54, "simpson_f03.png"),
    ("Simpson_AnatomicConsiderationsPostCommando_EJCTS_2023", 6, 68, "simpson_f04.png"),
    ("Simpson_AnatomicConsiderationsPostCommando_EJCTS_2023", 7, 72, "simpson_f06.png"),
    # ---- Vobornik 2023 Hradec Kralove ----
    ("Vobornik_AortomitralCurtainReconstructionDVE_FrontCardiovascMed_2023", 2, 27, "vob_f01.png"),
    ("Vobornik_AortomitralCurtainReconstructionDVE_FrontCardiovascMed_2023", 4, 50, "vob_f02.png"),
    ("Vobornik_AortomitralCurtainReconstructionDVE_FrontCardiovascMed_2023", 4, 55, "vob_f03.png"),
    ("Vobornik_AortomitralCurtainReconstructionDVE_FrontCardiovascMed_2023", 4, 60, "vob_f04.png"),
    # ---- Yajima 2022 patch-sparing ----
    ("Yajima_PatchSparingAMCReconstruction_EJCTS_2022", 2, 18, "yajima_f01.png"),
    # ---- Bojko 2024 USC graphical abstract ----
    ("Bojko_AortomitralCurtainReconstructionOutcomes_SeminThorac_2024", 8, 60, "bojko_f03.png"),
]


def main():
    fails = []
    for stem, page, xref, name in JOBS:
        pdf = os.path.join(HERE, "pdfs", stem + ".pdf")
        dest = os.path.join(OUT, name)
        r = subprocess.run([sys.executable, SCRIPT, "get", pdf, str(page),
                            str(xref), dest], capture_output=True, text=True)
        if r.returncode != 0:
            fails.append((name, r.stderr.strip()[-200:]))
        else:
            print(r.stdout.strip() or f"ok {name}")
    print(f"\n{len(JOBS) - len(fails)}/{len(JOBS)} extracted")
    for n, e in fails:
        print(f"FAIL {n}: {e}")


if __name__ == "__main__":
    main()
