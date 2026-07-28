"""Static HTML snippets and figure markers used by the body builder."""

from __future__ import annotations

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
