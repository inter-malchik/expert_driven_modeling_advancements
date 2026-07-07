> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Gindullina et al.'s work (hereafter **Paper A**) frames Expert-Guided PINN as a human-in-the-loop system where an epidemiologist critiques a forecast and an LLM rewrites the PINN's composite loss. Chakraborti, Sreedharan, Zhang, and Kambhampati's *"Plan Explanations as Model Reconciliation: Moving Beyond Explanation as Soliloquy"* (hereafter **Paper B**) formalizes a different contract for such loops: when the human's model $\mathcal{M}^H$ diverges from the robot's $\mathcal{M}^R$, explanations must reconcile models—not monologue about the AI's internal correctness.

Paper A never represents $\mathcal{M}^H$. The PINN Customizer emits Python loss code; the expert infers intent only from the downstream curve. That is soliloquy in disguise: modification without a minimally complete explanation (MCE) bridging epidemic concepts ("peak too early") to PINN terms ($L_{IC}$, term2 penalties). Paper B's Model Reconciliation Problem (MRP) is a specification for the explanation layer Paper A's modification templates and semantic checker were meant to enable but not yet define.

---

## 1. Two models in the loop: Multi-Model Planning versus a single SIRD-PINN

Paper B analyzes plans optimal in $\mathcal{M}^R$ that fail in $\mathcal{M}^H$:

> **Quote (Chakraborti et al.):** *«Interaction between humans and AI systems is best analyzed in light of their differing models. The robot here generates an optimal plan $\pi_R^*$ with respect to its model $\mathcal{M}^R$, which is interpreted by the human with respect to his model $\mathcal{M}^H$. Explanations are needed when $\pi_R^*$ is not an optimal plan with respect to $\mathcal{M}^H$.»*

Paper A fixes one formal $\mathcal{M}^R$—SIRD ODEs embedded in a PINN loss—and returns only a replotted forecast:

> **Quote (Gindullina et al.):** *«A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle. The process begins with an expert's qualitative assessment of a forecast, which is translated into a structured specification for loss function modification... The loop is closed by presenting the refined forecast to the expert.»*

| Criterion | Paper A | Paper B | Takeaway |
|:--- |:--- |:--- |:--- |
| AI model ($\mathcal{M}^R$) | SIRD-PINN + composite loss | PDDL planning domain | Same loop shape, different formalism |
| Human model ($\mathcal{M}^H$) | Implicit (peak shape, interventions) | Explicit PDDL in experiments | A never stores or updates $\mathcal{M}^H$ |
| System output | Loss code + plot | Model patch (MCE/MME) | A acts without explaining the patch |
| Acceptance test | Visual "Compliance with the comment" | $C(\pi^*,\widehat{\mathcal{M}})=C^*_{\widehat{\mathcal{M}}}$ | Subjective curve match ≠ reconciled optimality |

---

## 2. Soliloquy: the PINN speaks only to itself

Paper B rejects planner monologues:

> **Quote (Chakraborti et al.):** *«Much of that work involved the planner explaining its decisions with respect to its own model (i.e. current state, actions and goals) and assuming that this "soliloquy" also helps the human in the loop. While such a sanguine assumption may well be requited when the human is an expert "debugger"... it is completely unrealistic in most human-AI interaction scenarios, where the humans may have a domain and task model that differs significantly from that used by the AI system.»*

Paper A targets epidemiologists without PINN expertise:

> **Quote (Gindullina et al.):** *«Our solution eliminates the need for rigorous a priori mathematical formalization and static architecture, offering epidemiologists an adaptive tool for calibrating forecasts without requiring a deep understanding of the model's internal parameterization.»*

Yet the only machine-readable artifact is loss source code—comprehensible only through the plot. Paper A's Future work names an "LLM-loss-semantic-checker" but not model reconciliation.

---

## 3. MRP as blueprint for "modification explanations"

> **Quote (Chakraborti et al.):** *«The Model Reconciliation Problem (MRP) is a tuple $\langle \pi^*, \langle \mathcal{M}^R, \mathcal{M}^H \rangle \rangle$ where $C(\pi^*, \mathcal{M}^R) = C^*_{\mathcal{M}^R}$... explanations should be seen as the robot's attempt to move the human's model to be in conformance with its own.»*

> **Quote (Chakraborti et al.):** *«A Multi-Model Explanation denoted by $\mathcal{E}$ is a solution to an MRP... such that $C(\pi^*, \widehat{\mathcal{M}}) - C^*_{\widehat{\mathcal{M}}} < C(\pi^*, \mathcal{M}^H) - C^*_{\mathcal{M}^H}$.»*

Mapped to Paper A: $\pi^*$ is the post-modification incidence trajectory; $\mathcal{M}^R$ is SIRD+PINN+loss; $\mathcal{M}^H$ is the expert's epidemic story. A reconciling explanation would state: *your mental model says post-peak decline is too slow; our model maps that to insufficient penalty on $I(t)$ in $(t_{peak},T)$—the minimal loss edit that makes our forecast optimal in your updated view.* Today only the edit exists.

---

## 4. Plan Patch Explanations versus Table A.2 templates

> **Quote (Chakraborti et al.):** *«A Plan Patch Explanation (PPE) is given by... focusing only on plan being explained. However, it may also contain information that need not have been revealed... Thus, it is incomplete.»*

> **Quote (Chakraborti et al.):** *«A Minimally Complete Explanation (MCE) is the shortest complete explanation... An explanation is complete iff $C(\pi^*, \widehat{\mathcal{M}}) = C^*_{\widehat{\mathcal{M}}}$.»*

Paper A's Table A.2 ("add penalty to term2; other components prohibited") is a PPE over the loss: it names *where* to edit, not *why* that edit makes the forecast optimal in the expert's model (R1 completeness fails). The 700-day outbreak remains compilable yet inexplicable in $\mathcal{M}^H$ terms.

---

## 5. R1–R4 requirements versus "Compliance with the comment"

> **Quote (Chakraborti et al.):** *«R1. Completeness... R2. Conciseness... R3. Monotonicity... R4. Computability... an explanation that is very easy to compute may be very hard to comprehend.»*

Paper A's primary metric:

> **Quote (Gindullina et al.):** *«Compliance with the comment. This is the primary criterion for assessing the technical success of the modification system. A comparative analysis is performed between the expert's text commentary and the visualization of the modified forecast.»*

> **Quote (Gindullina et al.):** *«The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion.»*

25–27% compliance measures instruction-following visuals, not whether an MCE would make the modified forecast optimal in an explicit $\widehat{\mathcal{M}}^H$. Monotonic templates (R3) align with Paper A's planned class-subclass modification templates but remain unimplemented.

---

## 6. Fetch-robot precondition parallel to boundary-condition edits

> **Quote (Chakraborti et al.):** *«This correction brings the human and the robot model closer, and is necessary and sufficient to make the robot's plan optimal in the resultant domain.»*

Paper A's ambiguous case: expert requests two more weeks of growth; Llama-8B quadruples the $I(T_{max})\to 0$ boundary weight:

> **Quote (Gindullina et al.):** *«In the modified loss function, the meta-llama/Meta-Llama-3.1-8B-Instruct model increased the weight of the zero boundary condition... by a factor of four, which is difficult to interpret in relation to the expert's request.»*

An MCE would reconcile: *long-horizon $I(t)$ decay is governed by $L_{IC}$ in our model; your growth request conflicts with strengthening that boundary term*—instead of silently showing a flat curve.

---

## 7. Negotiation, ε-optimality, and the Conversational Agent

> **Quote (Chakraborti et al.):** *«The human in the loop can either chose to use this explanation to update her own model or negotiate in course of further dialog (e.g. to update the robot's model).»*

Paper B's future work extends to humans with bounded planning capacity via ε-optimality and top-K plans. Paper A's Conversational Agent validates comment *format* (concreteness, certainty) but cannot negotiate model divergence—e.g., when Class 4 peak-shift language maps to the wrong loss term. Multi-model dialogue is the missing complement to one-shot codegen.

---

## 8. Comparative summary

| Criterion | Paper A | Paper B | Takeaway |
|:--- |:--- |:--- |:--- |
| Explanation object | Implicit in loss diff | Explicit $\mathcal{E}^{MCE}$ / $\mathcal{E}^{MME}$ | A needs a forward explanation channel |
| Search procedure | Single LLM sample | A* over model edits (Algorithm 1) | Template search could mirror MCE-SEARCH |
| Evaluator role | Expert plot judgment | Formal optimality in $\widehat{\mathcal{M}}$ | Redefine "LLM-expert-evaluator" as MRP solver |
| Failure at 25–27% | No $\mathcal{M}^H$ patch offered | MCE minimizes $|\Gamma(\widehat{\mathcal{M}})\Delta\Gamma(\mathcal{M}^H)|$ | Low compliance may reflect missing explanations, not only bad code |

---

## Proposed direction 1. Explicit $\mathcal{M}^H$ ontology alongside classifier labels

**Pipeline stage:** Hierarchical classifier + new explanation head.

**Mechanism:** Store expert-level fluents ("peak early", "decline too sharp", "missing intervention effect") parallel to class/subclass; after each loss edit, emit an MCE-style mapping from fluent to Table A.2 operation.

**Failure mode:** Expert cannot interpret why term2 was penalized.

---

## Proposed direction 2. MCE search over modification-template space

**Pipeline stage:** PINN Customizer (replace free-form codegen).

**Mechanism:** Search minimal template subset from Appendix A making the forecast optimal in $\widehat{\mathcal{M}}^H$, using Paper B's model-space A* (Algorithm 1) over admissible penalty operators.

**Failure mode:** Over-large PPE edits that compile but fail R1 completeness.

---

## Proposed direction 3. Conversational reconciliation dialogue

**Pipeline stage:** Conversational Agent.

**Mechanism:** When proposed $\mathcal{E}$ leaves residual suboptimality, elicit contrastive expert statements ("did you mean slower decline or later peak?") before PINN Customizer runs—implementing negotiate branch from Paper B.

**Failure mode:** Peak-shift comment routed to boundary-condition edit.

---

## Proposed direction 4. Top-K undominated forecasts (ε-optimality)

**Pipeline stage:** Retraining loop → expert UI.

**Mechanism:** Present 3–5 Pareto forecasts trading comment alignment vs. $L_{data}$ fit instead of one scalarized optimum—per Paper B's ε-optimality / top-K future work.

**Failure mode:** Ambiguous flat-curve outcomes from scalarized loss.

---

## Proposed direction 5. LLM-expert-evaluator as MRP solver

**Pipeline stage:** Evaluation (Future work agent).

**Mechanism:** Redefine evaluator to output $\mathcal{E}^{MCE}$ linking comment interpretation to loss change and predicted curve—not merely a compliance score on the plot.

**Failure mode:** Subjective compliance without inter-rater calibration.

---

## Conclusion

Paper B argues that human-in-the-loop AI must treat explanation as model reconciliation: minimally complete patches that make the system's plan optimal in the human's updated model, with optional monotonicity and dialogue. Paper A solves the *action* side—NL to loss edit—with a fixed $\mathcal{M}^R$ but leaves $\mathcal{M}^H$ implicit and shows only curves. Read together, Expert-Guided PINN is a prototype executor; MRP/MCE is the specification for the explanation and evaluation layer still missing between classifier output and expert trust—directly informing modification templates and the semantic checker Gindullina et al. already propose.
