"""Extract draft data for new commentary cards from the analysis files.

For each .md in article/analysis/ that is NOT in the original 15 filenote set,
extract:
  - slug (filename without .md)
  - paper_b_url (from `> **Paper B — live link:**` line, if present)
  - paper_b_label (from parenthetical `(Author, YYYY, "Title"` or similar)
  - first_gindullina_quote (first `> **Quote (Gindullina et al.):** *"..."*` payload)
  - thesis (first non-blockquote paragraph after the header block)
  - anchor_match (whether the extracted quote is a substring of body_html.py after
    apostrophe/quote normalization)
  - inferred_section (nearest preceding <h2>/<h3> heading in body_html.py, if match)

Prints a JSON list to stdout so the calling code can inspect and curate.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = ROOT / "article" / "analysis"
BODY_HTML_PATH = ROOT / "article" / "body_html.py"

ORIGINAL_15 = {
    "alansari_survey_hallucination",
    "towardsImprovedXaiBasedEpidemiologicalResearch",
    "moeltner_lab_in_the_loop",
    "lin_frequentist_or_bayesian",
    "yu_2025_spec2rtl_agent",
    "explanationInArtificialIntelligence",
    "gruber_ontolingua_portable_ontology",
    "wang_code_generation_errors",
    "oreskes_verification_validation",
    "chakraborti_model_reconciliation",
    "kreikemeyer_2025_llm_reaction_networks",
    "huang_survey_hallucination",
    "ouyang_2022_instructgpt",
    "burke_heuristic_combination_structure",
    "bewareOfInmates_doYouGetIt_howFutureDepends",
}


def normalize(text: str) -> str:
    return (
        text.replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("«", '"')
        .replace("»", '"')
    )


QUOTE_RX = re.compile(
    r">\s*\*\*Quote\s*\(Gindullina[^)]*\):\*\*\s*\*[\"«“](.+?)[\"»”]\*",
    re.DOTALL,
)
QUOTE_RX_ALL = re.compile(
    r">\s*\*\*Quote\s*\(Gindullina[^)]*\):\*\*\s*\*[\"«“](.+?)[\"»”]\*",
    re.DOTALL,
)
LIVE_LINK_RX = re.compile(
    r">\s*\*\*Paper B\s*[—-]\s*live link:\*\*\s*\[([^\]]+)\]\(([^)]+)\)",
    re.IGNORECASE,
)
PAPER_B_PAREN_RX = re.compile(
    r"Paper B\s*\(([^)]+)\)",
    re.IGNORECASE,
)
HEADING_RX = re.compile(r"<(h[23])>([^<]+)</\1>")


def load_body_html() -> tuple[str, str, list[tuple[int, str]]]:
    raw = BODY_HTML_PATH.read_text(encoding="utf-8")
    # Extract the BODY_HTML string literal (everything between the first triple-quote pair).
    match = re.search(r'BODY_HTML\s*=\s*"""(.*?)"""', raw, re.DOTALL)
    if not match:
        raise RuntimeError("Could not locate BODY_HTML literal in body_html.py")
    body = match.group(1)
    body_norm = normalize(body)
    headings: list[tuple[int, str]] = []
    for m in HEADING_RX.finditer(body_norm):
        headings.append((m.start(), m.group(2).strip()))
    return body, body_norm, headings


def section_for_position(headings: list[tuple[int, str]], pos: int) -> str:
    current = ""
    for start, heading in headings:
        if start <= pos:
            current = heading
        else:
            break
    return current


def extract(md_text: str) -> dict:
    live_link = LIVE_LINK_RX.search(md_text)
    paper_b_paren = PAPER_B_PAREN_RX.search(md_text)
    first_quote = QUOTE_RX.search(md_text)

    lines = md_text.splitlines()
    thesis = ""
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(">"):
            continue
        if stripped.startswith("#"):
            continue
        thesis = stripped
        break

    return {
        "paper_b_url": live_link.group(2) if live_link else None,
        "paper_b_label": live_link.group(1) if live_link else None,
        "paper_b_paren": paper_b_paren.group(1).strip() if paper_b_paren else None,
        "first_gindullina_quote": first_quote.group(1).strip() if first_quote else None,
        "thesis": thesis,
    }


def main() -> None:
    body, body_norm, headings = load_body_html()

    entries = []
    for path in sorted(ANALYSIS_DIR.glob("*.md")):
        slug = path.stem
        if slug in ORIGINAL_15:
            continue

        md_text = path.read_text(encoding="utf-8")
        data = extract(md_text)

        anchor_match_text = None
        inferred_section = ""
        # Try ALL Gindullina quotes in the file — pick the first that verbatim matches
        # (after apostrophe/quote normalization) the HTML body.
        all_quotes = [m.group(1).strip() for m in QUOTE_RX_ALL.finditer(md_text)]
        matched_index = -1
        for idx, q in enumerate(all_quotes):
            q_norm = normalize(q)
            pos = body_norm.find(q_norm)
            if pos >= 0:
                anchor_match_text = q
                inferred_section = section_for_position(headings, pos)
                matched_index = idx
                break

        # Fallback: whitespace-relaxed match, still trying every quote in order.
        if not anchor_match_text:
            body_collapsed = re.sub(r"\s+", " ", body_norm)
            for idx, q in enumerate(all_quotes):
                q_norm = re.sub(r"\s+", " ", normalize(q))
                pos = body_collapsed.find(q_norm)
                if pos >= 0:
                    anchor_match_text = q + "  [ws-relaxed]"
                    inferred_section = section_for_position(headings, pos)
                    matched_index = idx
                    break

        data["all_quote_count"] = len(all_quotes)
        data["matched_quote_index"] = matched_index
        data["anchor_text"] = anchor_match_text

        entries.append(
            {
                "slug": slug,
                **data,
                "anchor_match": bool(anchor_match_text),
                "inferred_section": inferred_section,
            }
        )

    print(json.dumps(entries, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
