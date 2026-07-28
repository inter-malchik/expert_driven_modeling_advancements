"""Figure configuration and rendering for the paper view."""

from __future__ import annotations

import base64
import html
import re
from pathlib import Path

FIGURES_DIR = Path(__file__).resolve().parent.parent / "assets" / "figures"

HALF_WIDTH_FIGURES = {"FIG1", "FIG3"}

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


def figure_data_uri(filename: str) -> str:
    encoded = base64.b64encode((FIGURES_DIR / filename).read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def figure_label(caption: str) -> str:
    match = re.search(r"<strong>Fig\.\s*([^<]+)</strong>", caption)
    if match:
        return f"Fig. {match.group(1).strip().rstrip('.')}"
    return "Figure"


def figure_html(marker: str) -> str:
    filename, caption = FIGURE_CAPTIONS[marker]
    label = html.escape(figure_label(caption))
    figure_id = marker.lower().replace("fig", "figure-")
    show_label = label.replace("Fig.", "fig.", 1)
    width_class = " paper-figure--half-width" if marker in HALF_WIDTH_FIGURES else ""
    return (
        f'<figure class="paper-figure{width_class}" id="{figure_id}">'
        f'<details class="paper-figure-details">'
        f'<summary class="paper-figure-summary">'
        f'<span class="paper-figure-show-label">Show {show_label}</span>'
        f'<span class="paper-figure-caption">{caption}</span>'
        f"</summary>"
        f'<div class="paper-figure-image">'
        f'<img src="{figure_data_uri(filename)}" alt="{html.escape(filename)}" />'
        f"</div>"
        f"</details>"
        f"</figure>"
    )


def inject_figures(html_text: str) -> str:
    for marker in FIGURE_CAPTIONS:
        html_text = html_text.replace(f"<!--{marker}-->", figure_html(marker))
    return html_text
