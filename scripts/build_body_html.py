"""Generate article/body_html.py from legacy markdown content."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "assets" / "figures"

FIGURE_CAPTIONS = {
    "FIG1": (
        "fig1.png",
        "<strong>Fig. 1.</strong> Schematic of Expert-Guided PINN. The expert enters a comment "
        "that will help them correctly structure the conversational agent. Next, a class and "
        "subclass are defined for the comment, for which rules for generating modifications to "
        "the current loss function will be defined. After generating the loss function and "
        "checking its compilability, the PINN training process begins. The user then receives "
        "a new prediction, which they can then decide whether it satisfies their comment or not.",
    ),
    "FIG2": (
        "fig2.png",
        "<strong>Fig. 2.</strong> Workflow of the PINN Customizer: (a) a prompt containing a task, "
        "comment, and rules, (b) scheme of PINNs, (c) PINN Customizer, (d) Code tester, "
        "(e) User interface.",
    ),
    "FIG3": (
        "fig3.png",
        "<strong>Fig. 3.</strong> (a) Comparative Performance of LLMs in loss function generation "
        "tasks (temperature=1.0, 20 launches); (b) Comparison of TSED Score for LLMs.",
    ),
    "FIG4": (
        "fig4.png",
        "<strong>Fig. 4.</strong> (a) Example of a successful result: a sharper decline in the "
        "number of cases after the peak, as requested by the expert; (b) Example of an unsuccessful "
        "result: unrealistically long epidemic duration when the expert requests a 7–10 day shift "
        "of the peak; (c) Example of an ambiguous result: stabilization of case counts instead of "
        "continued growth for two additional weeks, and an atypically flat epidemic curve.",
    ),
    "FIG5": (
        "fig5.png",
        "<strong>Fig. 5.</strong> LLMs Performance Comparison (temperature=1.0). Evaluated on: "
        "(a) Matching training data, (b) Forecast has changed, (c) Compliance with the epidemic "
        "logic, (d) Compliance with the comment.",
    ),
    "FIGA6": (
        "figA6.png",
        "<strong>Fig. A.6.</strong> Hierarchical Structure of Expert Comment Classes and Subclasses.",
    ),
    "FIGA7": (
        "figA7.png",
        "<strong>Fig. A.7.</strong> User navigation pathway.",
    ),
}

HIGHLIGHTS_TABLE = """
<table class="paper-highlights">
<tr><td>Problem or issue</td><td>In epidemiological tasks, expert judgement is frequently employed. A framework is required to formally integrate domain expertise into computational forecasting models to enhance their predictive accuracy</td></tr>
<tr><td>What is already known</td><td>As a rule, expert knowledge is incorporated into the model either directly in a form of mathematical formulas, or through web interfaces, which makes it necessary for the epidemiologists to learn the model parameters and their influence on the output</td></tr>
<tr><td>What this paper adds</td><td>We introduce a novel software framework for the interactive adaptation of Physics-Informed Neural Network loss function, powered by a Large Language Model, which makes it possible to formalize the expert knowledge into the PINN optimization objective via expert’s interactions with the LLM using natural language</td></tr>
<tr><td>Who would benefit</td><td>Experts in the field of epidemiology who are in charge of epidemic surveillance, and domain specialists in general who employ predictive models</td></tr>
</table>
"""

TABLE1 = """
<div class="paper-table-wrap">
<p class="paper-table-title">Table 1</p>
<p class="paper-table-caption">Hierarchical text classification performance metrics.</p>
<table class="paper-table">
<thead><tr><th>Metric</th><th>Value</th></tr></thead>
<tbody>
<tr><td>Accuracy</td><td>0.811</td></tr>
<tr><td>Macro F1</td><td>0.837</td></tr>
<tr><td>Macro Precision</td><td>0.847</td></tr>
<tr><td>Macro Recall</td><td>0.832</td></tr>
</tbody>
</table>
</div>
"""

TABLE_A2 = """
<div class="paper-table-wrap">
<p class="paper-table-title">Table A.2</p>
<p class="paper-table-caption">Rules for modifying the loss function based on the class and subclass of the expert comment. Each term represents a specific compartment: term1 (susceptible), term2 (infectious), term3 (dead), term4 (recovered).</p>
<table class="paper-table">
<thead>
<tr><th>Class</th><th>Class Description</th><th>Permitted Modifications for the subclass</th><th>Constraints</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>The behavior of the epidemic curve does not match the expert’s expectations.</td><td>1 Add penalty to term2.<br>2 Add penalty to term1.<br>3 Add penalty to term4.<br>4 Add penalty to term3.</td><td>Modification of other function components is <strong>prohibited</strong>.</td></tr>
<tr><td>2</td><td>The error relates to accounting for epidemic countermeasures.</td><td>1 Add a time-based penalty.<br>2 Adjust/add parameters affecting implemented measures.<br>3 Add a penalty accounting for introduced measures.</td><td>Only term2 can be changed. Modification of other function components is <strong>prohibited</strong>.</td></tr>
<tr><td>3</td><td>The error is due to the fact that the forecast contains incorrect parameters or time dynamics of the epidemiological process.</td><td>1 Add time-based penalty to term2.<br>2 Add penalty to term2 considering quantitative characteristics.</td><td>Modification of other function components is <strong>prohibited</strong>.</td></tr>
<tr><td>4</td><td>The epidemic peak position does not match expert expectations.</td><td>1 Add offset to desired peak day in term2.<br>2 Add penalty for discrepancy in infected count during peak in term2.</td><td>Modification of other function components is <strong>prohibited</strong>.</td></tr>
</tbody>
</table>
</div>
"""


def figure_html(marker: str) -> str:
    return f"<!--{marker}-->"


def inline_format(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def convert_markdown_block(text: str) -> str:
    lines = text.strip().splitlines()
    html_parts: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_ordered = False
    in_blockquote = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            html_parts.append(f"<p>{inline_format(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items, list_ordered
        if list_items:
            tag = "ol" if list_ordered else "ul"
            items = "".join(f"<li>{inline_format(item)}</li>" for item in list_items)
            html_parts.append(f"<{tag}>{items}</{tag}>")
            list_items = []
            list_ordered = False

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            flush_list()
            in_blockquote = False
            i += 1
            continue

        if stripped.startswith("> "):
            in_blockquote = True
            i += 1
            continue

        if in_blockquote:
            i += 1
            continue

        if stripped == "---":
            flush_paragraph()
            flush_list()
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            flush_list()
            html_parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            flush_list()
            html_parts.append(f"<h3>{inline_format(stripped[4:])}</h3>")
            i += 1
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            flush_paragraph()
            flush_list()
            if stripped.startswith("| |"):
                html_parts.append(HIGHLIGHTS_TABLE)
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                i += 1
            continue

        if stripped == "**Table 1**":
            flush_paragraph()
            flush_list()
            html_parts.append(TABLE1)
            i += 1
            while i < len(lines) and (
                lines[i].strip().startswith("Hierarchical")
                or lines[i].strip().startswith("|")
            ):
                i += 1
            continue

        if stripped == "**Table A.2**":
            flush_paragraph()
            flush_list()
            html_parts.append(TABLE_A2)
            i += 1
            while i < len(lines) and (
                lines[i].strip().startswith("Rules for")
                or lines[i].strip().startswith("|")
            ):
                i += 1
            continue

        if stripped == "**Fig. 1.** Schematic of Expert-Guided PINN. The expert enters a comment that will help them correctly structure the conversational agent. Next, a class and subclass are defined for the comment, for which rules for generating modifications to the current loss function will be defined. After generating the loss function and checking its compilability, the PINN training process begins. The user then receives a new prediction, which they can then decide whether it satisfies their comment or not.":
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG1"))
            i += 1
            continue

        if stripped.startswith("**Fig. 2.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG2"))
            i += 1
            continue

        if stripped.startswith("**Fig. 3.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG3"))
            i += 1
            continue

        if stripped.startswith("**Fig. 4.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG4"))
            i += 1
            continue

        if stripped.startswith("**Fig. 5.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG5"))
            i += 1
            continue

        if stripped.startswith("**Fig. A.6.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIGA6"))
            i += 1
            continue

        if stripped.startswith("**Fig. A.7.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIGA7"))
            i += 1
            continue

        if stripped.startswith("**CRediT authorship contribution statement**"):
            flush_paragraph()
            flush_list()
            html_parts.append('<div class="paper-backmatter">')
            html_parts.append("<p><strong>CRediT authorship contribution statement</strong></p>")
            i += 1
            continue

        if stripped == "## Appendix A. Classification of expert comments":
            flush_paragraph()
            flush_list()
            html_parts.append("</div>")
            html_parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
            i += 1
            continue

        if stripped.startswith("## References"):
            flush_paragraph()
            flush_list()
            break

        ordered_match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        bullet_match = re.match(r"^[\*\-]\s+(.*)$", stripped)

        if ordered_match:
            flush_paragraph()
            if not list_ordered and list_items:
                flush_list()
            list_ordered = True
            list_items.append(ordered_match.group(2))
            i += 1
            continue

        if bullet_match:
            flush_paragraph()
            if list_ordered and list_items:
                flush_list()
            list_items.append(bullet_match.group(1))
            i += 1
            continue

        flush_list()
        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    flush_list()
    return "\n".join(html_parts)


def extract_article_content() -> str:
    source = ROOT / "article" / "source.md"
    if not source.exists():
        raise RuntimeError(
            "article/source.md not found. Restore the markdown source before rebuilding."
        )
    return source.read_text(encoding="utf-8")


def main() -> None:
    body_html = convert_markdown_block(extract_article_content())
    marker = "<h2>References</h2>"
    if marker in body_html:
        body_part, refs_part = body_html.split(marker, 1)
    else:
        body_part, refs_part = body_html, ""

    body_output = ROOT / "article" / "body_html.py"
    body_output.write_text(
        "# Auto-generated by scripts/build_body_html.py\n"
        f'BODY_HTML = """{body_part}"""\n',
        encoding="utf-8",
    )

    refs_output = ROOT / "article" / "references_html.py"
    refs_output.write_text(
        "# Auto-generated by scripts/build_body_html.py\n"
        f'REFERENCES_HTML = """{refs_part.strip()}"""\n',
        encoding="utf-8",
    )
    print(f"Wrote {body_output} ({len(body_part)} chars)")
    print(f"Wrote {refs_output} ({len(refs_part)} chars)")


if __name__ == "__main__":
    main()
