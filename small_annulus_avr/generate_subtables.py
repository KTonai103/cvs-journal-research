#!/usr/bin/env python3
"""Generate ppm_landscape.csv and asian_cohort_subset.csv from outcomes_master.csv."""

import csv
from pathlib import Path

PROJECT = Path("/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr")
MASTER = PROJECT / "tables" / "outcomes_master.csv"
PPM_CSV = PROJECT / "tables" / "ppm_landscape.csv"
ASIAN_CSV = PROJECT / "tables" / "asian_cohort_subset.csv"


def main():
    with MASTER.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # PPM landscape: any paper with at least one PPM rate reported (or PPM in title)
    ppm_cols = [
        "paper_id", "first_author", "year", "journal", "n", "ethnicity",
        "valve_type", "enlargement_technique",
        "ppm_severe_pct", "ppm_moderate_pct", "mean_gradient_postop_mmHg",
        "mean_annulus_mm", "mean_bsa", "notes",
    ]
    ppm_rows = [r for r in rows
                if r["ppm_severe_pct"] != "NR"
                or r["ppm_moderate_pct"] != "NR"
                or "PPM" in r["paper_id"]
                or "ppm" in r["paper_id"].lower()]
    with PPM_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ppm_cols, quoting=csv.QUOTE_MINIMAL,
                           extrasaction="ignore")
        w.writeheader()
        for r in ppm_rows:
            w.writerow(r)
    print(f"ppm_landscape.csv: {len(ppm_rows)} rows")

    # Asian cohort subset: ethnicity=yes or partial
    asian_cols = [
        "paper_id", "first_author", "year", "journal", "n", "ethnicity",
        "mean_bsa", "mean_annulus_mm", "valve_type", "enlargement_technique",
        "mortality_30d_pct", "ppm_severe_pct", "ppm_moderate_pct",
        "mean_gradient_postop_mmHg",
        "survival_1y_pct", "survival_5y_pct", "survival_10y_pct",
        "viv_feasibility_assessed", "notes",
    ]
    asian_rows = [r for r in rows
                  if r["ethnicity"].startswith(("yes", "partial"))
                  or any(kw in r["paper_id"].lower()
                         for kw in ["japan", "korea", "asian", "chinese",
                                    "ocean", "jcs", "okamura", "tabata",
                                    "shishido", "hase", "okuno", "meguro",
                                    "moon", "kamioka", "wang_yincision",
                                    "kim_two", "hu_17mm", "zhao_regent",
                                    "kitamura", "maekawa", "yashima", "mao",
                                    "lee_selfvsballoon", "izumi",
                                    "donguyen", "masaki_nicks", "gan_yincision"])]
    with ASIAN_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=asian_cols, quoting=csv.QUOTE_MINIMAL,
                           extrasaction="ignore")
        w.writeheader()
        for r in asian_rows:
            w.writerow(r)
    print(f"asian_cohort_subset.csv: {len(asian_rows)} rows")


if __name__ == "__main__":
    main()
