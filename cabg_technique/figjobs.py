#!/usr/bin/env python3
"""Batch-extract the embedded artwork for every figure the review cites.

Line art stored as an inverted 1-bit mask (the ATS papers) comes out white-on-black;
detect that by mean luminance and flip it back.
"""
import io, os
import fitz
from PIL import Image, ImageOps, ImageStat

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")

# (source pdf no, xref, output stem)
JOBS = [
    # -- ch1 overview -------------------------------------------------
    ("02", 19,  "magee_f1_pericardial_incision"),
    ("02", 32,  "magee_f2_apical_positioner"),
    ("02", 39,  "magee_f3_silastic_snare"),
    # -- ch2 exposure -------------------------------------------------
    ("06", 5,   "ricci_f1_single_suture"),
    ("06", 6,   "ricci_f2_lad"),
    ("06", 11,  "ricci_f3_diagonal"),
    ("06", 12,  "ricci_f4_om_lift"),
    ("06", 13,  "ricci_f5_om_compress"),
    ("06", 14,  "ricci_f6_rca"),
    ("06", 19,  "ricci_f7_pda_right"),
    ("06", 20,  "ricci_f8_pda_left"),
    ("07", 61,  "bergsland_f1_oblique_sinus"),
    ("07", 5,   "bergsland_f2_snare_tension"),
    ("07", 6,   "bergsland_f3_pack_elevation"),
    ("17", 11,  "albert_f1_outside_inside"),
    ("11", 27,  "grundeman04_f1_hemodynamics"),
    ("11", 28,  "grundeman04_f2_starfish_heart"),
    ("12", 9,   "nierich_f1_trendelenburg"),
    ("12", 10,  "nierich_f2_dopamine"),
    ("12", 19,  "nierich_f3_collapse_trace"),
    ("12", 24,  "nierich_f4_tee_rv"),
    ("16", 135, "shim_f1_pa_doppler"),
    # -- ch3 conduits -------------------------------------------------
    ("21", 3,   "laugesen_f2_three_harvest"),
    ("26", 16,  "tatoulis_f1_forearm_anatomy"),
    ("26", 32,  "tatoulis_f2_allen_plethysmography"),
    ("26", 56,  "tatoulis_f5_ita_vs_ra_histology"),
    ("26", 94,  "tatoulis_f6_incision"),
    ("26", 107, "tatoulis_f9_harmonic"),
    ("27", 82,  "gaudino_f4_radial_ygraft"),
    ("27", 90,  "gaudino_f5_melbourne_babyy"),
    ("27", 100, "gaudino_f6_extension_grafts"),
    ("29", 15,  "inaba_f1_notouch_harvest"),
    ("29", 17,  "inaba_f2_notouch_anastomosis"),
    ("31", 5,   "suma_f1_gea_anatomy"),
    ("31", 15,  "suma_f2_gea_detachment"),
    ("31", 16,  "suma_f3_gea_skeletonized"),
    ("31", 26,  "suma_f5_gea_targets"),
    ("25", 30,  "issa_f3_robot_docked"),
    # -- ch4 graft design ---------------------------------------------
    ("32", 8,   "kawajiri_f1_side_to_side"),
    ("32", 12,  "kawajiri_f2_seagull"),
    ("32", 20,  "kawajiri_f3_composite_types"),
    ("34", 27,  "glineur_f1_insitu_vs_y"),
    ("42", 77,  "gaudino20_f2_conduit_algorithm"),
    ("39", 17,  "wallgren_f1_snake_vs_separate"),
    ("36", 3,   "calafiore_f1_setpoint"),
    ("43", 17,  "hiraoka_f2_vr_rita"),
    ("35", 89,  "vervoort_f1_mag_selection"),
    # -- ch5 anastomosis / hostile targets -----------------------------
    ("46", 13,  "nishigawa_f1_endarterectomy_core"),
    ("46", 27,  "nishigawa_f2_instruments"),
    ("46", 39,  "nishigawa_f3_angiography"),
    ("04", 269, "osman_f2_vein_patch_a"),
    ("04", 270, "osman_f2_vein_patch_b"),
    ("04", 321, "osman_f3_rv_sandwich"),
    ("04", 345, "osman_f4_fmj_lad"),
    ("48", 11,  "wang_f1_foley_sketch"),
    ("48", 17,  "wang_f2_foley_steps"),
    ("49", 216, "sirin_f1_porcelain_ct"),
    # -- ch6 training --------------------------------------------------
    ("53", 8,   "fann_f2_task_station"),
    ("54", 10,  "anand_f1_simulator_kit"),
    ("55", 24,  "deraet_f2_valladolid_box"),
    ("55", 47,  "deraet_f5_vienna_beating"),
    ("56", 28,  "tozzi_f1_learning_pathways"),
    ("56", 63,  "tozzi_f4_om_exposure"),
    ("57", 46,  "naito_f1_training_model"),
    ("59", 25,  "han_f_animal_lab"),
]


def grab(pdf, xref, out):
    doc = fitz.open(pdf)
    info = doc.extract_image(xref)
    im = Image.open(io.BytesIO(info["image"]))
    doc.close()
    if im.mode in ("LA", "RGBA"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode in ("CMYK", "P"):
        im = im.convert("RGB")
    elif im.mode == "1":
        im = im.convert("L")
    if im.mode == "L" and ImageStat.Stat(im).mean[0] < 110:
        im = ImageOps.invert(im)            # inverted 1-bit line art
    im.save(out)
    return im.size


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    ok = fail = 0
    for n, xref, stem in JOBS:
        dst = os.path.join(OUT, f"{stem}.png")
        try:
            w, h = grab(f"p/{n}.pdf", xref, dst)
            ok += 1
            print(f"ok   {stem:<38} {w}x{h}")
        except Exception as e:
            fail += 1
            print(f"FAIL {stem:<38} {type(e).__name__}: {e}")
    print(f"\n{ok} extracted, {fail} failed")
