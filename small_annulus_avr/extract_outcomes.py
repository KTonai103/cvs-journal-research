#!/usr/bin/env python3
"""Extract YAML frontmatter + outcomes table from each MD file → tables/outcomes_master.csv."""

import csv
import re
from pathlib import Path

PROJECT = Path("/Users/k.tonai/Documents/CVS_Journal_Research/small_annulus_avr")
MD_DIR = PROJECT / "md"
OUT_CSV = PROJECT / "tables" / "outcomes_master.csv"

CSV_COLUMNS = [
    "paper_id", "first_author", "year", "journal", "n", "ethnicity",
    "mean_bsa", "mean_annulus_mm", "valve_type", "enlargement_technique",
    "label_valve_size_mm",
    "mortality_30d_pct", "stroke_pct", "pacemaker_pct", "aki_pct",
    "ppm_severe_pct", "ppm_moderate_pct", "mean_gradient_postop_mmHg",
    "survival_1y_pct", "survival_5y_pct", "survival_10y_pct",
    "viv_feasibility_assessed", "notes",
]

# Outcome row patterns: match "| Outcome name | result |"
OUTCOME_PATTERNS = {
    "mortality_30d_pct":      [r"30[- ]?day\s+mortality", r"operative\s+mortality", r"in[- ]?hospital\s+mortality"],
    "stroke_pct":             [r"^Stroke\b", r"\bstroke\b(?!.*free)"],
    "pacemaker_pct":          [r"pacemaker", r"\bPPI\b", r"PPM\s+implant"],
    "aki_pct":                [r"\bAKI\b", r"acute\s+kidney"],
    "ppm_severe_pct":         [r"severe\s+PPM"],
    "ppm_moderate_pct":       [r"moderate\s+PPM"],
    "mean_gradient_postop_mmHg": [r"mean\s+gradient", r"mean\s+PG", r"postop.*gradient"],
    "survival_1y_pct":        [r"1[- ]?y(ea)?r?\s+survival", r"1y\s+survival"],
    "survival_5y_pct":        [r"5[- ]?y(ea)?r?\s+survival", r"5y\s+survival"],
    "survival_10y_pct":       [r"10[- ]?y(ea)?r?\s+survival", r"10y\s+survival"],
}


def parse_yaml(text):
    """Return dict of YAML frontmatter."""
    m = re.match(r"---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    yaml_text = m.group(1)
    fm = {}
    current_key = None
    for line in yaml_text.split("\n"):
        if not line.strip():
            continue
        if re.match(r"^[a-zA-Z][\w-]*\s*:", line):
            k, _, v = line.partition(":")
            current_key = k.strip()
            fm[current_key] = v.strip().strip('"\'')
        elif line.startswith("  - ") and current_key:
            tag = line[4:].strip().strip('"\'')
            if not isinstance(fm.get(current_key), list):
                fm[current_key] = []
            fm[current_key].append(tag)
    return fm


def parse_outcomes_table(text):
    """Find the '## 4. アウトカム' table and return {outcome_label: value} dict."""
    section = re.search(
        r"##\s*4\.?\s*アウトカム[^\n]*\n(.*?)(?=\n##\s|\Z)",
        text, re.DOTALL
    )
    if not section:
        return {}
    rows = {}
    for line in section.group(1).split("\n"):
        line = line.strip()
        if not line.startswith("|") or "---" in line or line.startswith("| Outcome") or line.startswith("| 推奨"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        label = cells[0].strip("* ")
        # join remaining cells as value
        value = " / ".join(c for c in cells[1:] if c)
        rows[label] = value
    return rows


def match_outcome(rows, patterns):
    """Find a row matching any of the given regex patterns. Return its value or NR."""
    for label, value in rows.items():
        for pat in patterns:
            if re.search(pat, label, re.IGNORECASE):
                return value
        # Also check if value mentions HR/OR (meta-analysis) - keep as-is
    return "NR"


def clean_pct(val):
    """Strip surrounding text, keep first percentage / number."""
    if not val or val == "NR":
        return "NR"
    # If contains HR / OR / CI, keep raw
    if re.search(r"\bHR\b|\bOR\b|95%", val):
        return val.replace(",", ";").replace('"', "'")
    # Strip leading "**" etc
    val = re.sub(r"\*\*", "", val)
    return val.replace(",", ";").replace('"', "'").strip()


def extract_first_author(authors_field):
    if not authors_field:
        return ""
    s = authors_field.split(",")[0].strip()
    s = re.sub(r"\bet\s+al\.?\b", "", s, flags=re.IGNORECASE).strip()
    return s


def extract_year(citation, filename):
    m = re.search(r"\b(19|20)\d{2}\b", citation or "")
    if m:
        return m.group(0)
    m = re.search(r"_(\d{4})\.md$", filename)
    return m.group(1) if m else ""


def extract_n(sample_size):
    if not sample_size:
        return "NR"
    m = re.search(r"n\s*=\s*([\d,]+)", sample_size, re.IGNORECASE)
    return m.group(1).replace(",", "") if m else sample_size.replace(",", ";")


def main():
    md_files = sorted(MD_DIR.glob("*.md"))
    rows_out = []
    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8")
        fm = parse_yaml(text)
        outcomes = parse_outcomes_table(text)
        paper_id = md_path.stem
        row = {
            "paper_id": paper_id,
            "first_author": extract_first_author(fm.get("authors", "")),
            "year": extract_year(fm.get("citation", ""), md_path.name),
            "journal": fm.get("journal-abbr", "") or fm.get("journal", "").split(",")[0][:30],
            "n": extract_n(fm.get("sample-size", "")),
            "ethnicity": fm.get("asian-cohort", ""),
            "mean_bsa": fm.get("patient-bsa", ""),
            "mean_annulus_mm": fm.get("annulus-size", ""),
            "valve_type": fm.get("valve-type", ""),
            "enlargement_technique": fm.get("enlargement-technique", ""),
            "label_valve_size_mm": "NR",
            "mortality_30d_pct":       clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["mortality_30d_pct"])),
            "stroke_pct":              clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["stroke_pct"])),
            "pacemaker_pct":           clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["pacemaker_pct"])),
            "aki_pct":                 clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["aki_pct"])),
            "ppm_severe_pct":          clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["ppm_severe_pct"])),
            "ppm_moderate_pct":        clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["ppm_moderate_pct"])),
            "mean_gradient_postop_mmHg": clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["mean_gradient_postop_mmHg"])),
            "survival_1y_pct":         clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["survival_1y_pct"])),
            "survival_5y_pct":         clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["survival_5y_pct"])),
            "survival_10y_pct":        clean_pct(match_outcome(outcomes, OUTCOME_PATTERNS["survival_10y_pct"])),
            "viv_feasibility_assessed": fm.get("viv-discussion", ""),
            "notes":                   (fm.get("follow-up", "")[:80] if fm.get("follow-up") else ""),
        }
        rows_out.append(row)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in rows_out:
            writer.writerow(row)
    print(f"Wrote {len(rows_out)} rows to {OUT_CSV}")
    # Coverage report
    nr_counts = {col: sum(1 for r in rows_out if r[col] in ("NR", "")) for col in CSV_COLUMNS if col != "paper_id"}
    print("NR/empty count per column:")
    for col, n in sorted(nr_counts.items(), key=lambda x: -x[1]):
        print(f"  {col:32s}  {n}/{len(rows_out)}")


if __name__ == "__main__":
    main()
