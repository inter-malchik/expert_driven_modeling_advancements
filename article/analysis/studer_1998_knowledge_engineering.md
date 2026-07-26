> **Paper B — live link:** [https://doi.org/10.1016/S0169-023X(97)00056-6](https://doi.org/10.1016/S0169-023X(97)00056-6)  
> **Source in `src/`:** [`../src/1998 Knowledge Engineering.md`](../src/1998%20Knowledge%20Engineering.md)

Gindullina et al. (hereafter **Paper A**) present Expert-Guided PINN as an interactive NL→loss pipeline: Conversational Agent → hierarchical class/subclass ontology → PINN Customizer → LLM rewrite of a SIRD PINN objective → compile check → retrain. Best “Compliance with the comment” reaches only 25–27% (DeepSeek / Llama-70B) versus 6% (Llama-8B). The manuscript’s “What this paper adds” box frames novelty as formalizing expert knowledge into the PINN objective *via natural language*, against a backdrop of static mathematical constraints or parameter-tuning UIs. Future work still calls for deeper class–subclass *modification templates* and multi-agent checkers—admitting that Appendix A rules “lack sufficient detail.”

Studer, Benjamins, and Fensel (1998; hereafter **Paper B**) survey Knowledge Engineering’s decisive shift from a *transfer* view (interview expert → dump rules into an interpreter) to a *modeling* view (build approximate, cyclic, evaluable models of expertise), crystallizing CommonKADS (domain / inference / task layers), MIKE, PROTÉGÉ-II, Problem-Solving Method (PSM) libraries, and ontology design principles (modularity, minimal encoding bias, minimal ontological commitment).

The transferable thesis is sharp: **Paper A’s contribution is domain-specific knowledge modeling over a PINN—not “first NL→objective.” Reposition novelty inside KE’s modeling paradigm; deepen the thin class/subclass ontology into a reusable method/task ontology of loss modifications.**

---

## 1. Transfer vs modeling: where Paper A still sounds first-generation

Paper B’s diagnosis of early expert systems—mixed knowledge types, tacit knowledge ignored, transfer only scaling to prototypes—maps uncomfortably onto free NL→full loss rewrite with prose Table A.2 rules.

> **Quote (Studer et al.):** *"In the early 1980s the development of a KBS was seen as a transfer process of human knowledge into an implemented knowledge base. This transfer was based on the assumption that the knowledge which is required by the KBS already exists and just has to be collected and implemented."*

> **Quote (Studer et al.):** *"Nowadays there exists an overall consensus that the process of building a KBS may be seen as a modeling activity. Building a KBS means building a computer model with the aim of realizing problem-solving capabilities comparable to a domain expert."*

> **Quote (Gindullina et al.):** *"What this paper adds… a novel software framework for the interactive adaptation of Physics-Informed Neural Network loss function, powered by a Large Language Model, which makes it possible to formalize the expert knowledge into the PINN optimization objective via expert’s interactions with the LLM using natural language"*

NL chat is a *channel*, not a modeling architecture. KE already rejected “collect knowledge → encode” as sufficient; Paper A should claim a *model* of epidemic-expert interventions on PINN losses, with LLM as a compiler into that model—not transfer of prose into code. (Comparative inference)

---

## 2. Cyclic evaluation and approximation—already Paper A’s practice, under-theorized

Paper B lists three modeling consequences: models approximate reality; modeling is cyclic; evaluation against reality is indispensable. Paper A’s expert accept/reject loop and Future work on institute validation already instantiate that—without citing the KE framing.

> **Quote (Studer et al.):** *"Like every model, such a model is only an approximation of the reality. In principle, the modeling process is infinite. … The modeling process is a cyclic process. New observations may lead to refinement, modification or completion of the already built-up model. … evaluation of the model with respect to reality is indispensable."*

> **Quote (Gindullina et al.):** *"Upon completion of the training process, the system visualizes the resulting forecast… At this stage, the expert evaluates the relevance of the modified forecast to the original comment and decides whether to retain it or re-modify it."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility… with a success rate of 25-27% for the best models… proof-of-concept… highlighting the need to develop more stringent generation rules and control mechanisms."*

25–27% is not a failed “NL magic” claim; it is expected under cyclic model refinement. Introduction should say so in KE vocabulary. (Author-stated) (Comparative inference)

---

## 3. CommonKADS layers: comment ontology ≠ expertise model

Paper A’s hierarchy (curve behavior / countermeasures / numeric dynamics / peak) is a *domain* vocabulary for comments. CommonKADS separates domain, inference (PSM), and task layers—Paper A collapses inference (how to edit the loss) into prompt prose.

> **Quote (Studer et al.):** *"A major contribution of KADS is its proposal for structuring the Expertise Model, which distinguishes three different types of knowledge… Domain layer… Inference layer… Task layer…"*

> **Quote (Gindullina et al.):** *"To ensure that LLM-generated modifications adhere to PINN principles, we restrict the space of possible loss functions via a rule-based system… we structure comments using a hierarchical ontology. It is based on four basic classes…"*

> **Quote (Gindullina et al.):** *"The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made."*

Deepening class/subclass without an inference-layer PSM (“Propose-penalty,” “Shift-peak,” “Revise-BC-weight”) recreates Paper B’s first-generation mixture: domain labels glued to opaque generation steps. (Comparative inference)

---

## 4. PSMs and Propose-and-Revise: templates as method roles, not English rows

Role-limiting methods and Propose-and-Revise already typed knowledge roles—*design-extensions*, *constraints*, *fixes*—analogous to typed loss-edit operators Paper A only plans.

> **Quote (Studer et al.):** *"A Problem-Solving Method (PSM) may be characterized as follows: A PSM specifies which inference actions have to be carried out for solving a given task. … Knowledge roles determine which role the domain knowledge plays in each inference action."*

> **Quote (Studer et al.):** *"In essence three generic roles may be identified for Propose-and-Revise… \"design-extensions\"… \"constraints\"… \"fixes\"…"*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

Templates should be published as a small PSM library over PINN losses (competence + assumptions on available terms), not as longer Appendix A sentences. That is KE reuse, not prompt craft. (Comparative inference) (Speculative extension)

---

## 5. Ontologies: deepen class/subclass with KE design principles

Paper B’s ontology criteria diagnose why four classes × thin subclasses under-constrain the LLM: encoding bias (rules as English), weak modularity (one global rewrite), and over-commitment (prohibit “other components” without defining admissible operators).

> **Quote (Studer et al.):** *"An ontology is a formal, explicit specification of a shared conceptualisation."*

> **Quote (Studer et al.):** *"Design principles include modularity, internal coherence, extensibility, minimal encoding bias, natural categories, minimal theory inclusions and minimal ontological commitment."*

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

> **Quote (Gindullina et al.):** *"There is a systematic problem with interpreting numerical values in expert comments… tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

Literal numeric insertion is an encoding-bias failure: numbers enter as surface tokens rather than as ontology-mapped roles (peak-offset ∈ range, weight multiplier ∈ bounds). Deepening the hierarchy should add *method/task* concepts (edit type, admissible AST fragment, numeric map), not only more visual subclasses. (Comparative inference)

---

## 6. Comparison table: KE framing vs Paper A claims

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Stated novelty | NL formalization into PINN objective | KE paradigm: transfer → modeling | Reposition as PINN-domain modeling (Comparative inference) |
| Knowledge structure | 4 classes / subclasses + Table A.2 | Domain / inference / task (CommonKADS) | Need PSM layer for edits (Comparative inference) |
| Reuse unit | Planned modification templates | PSM libraries; method/task ontologies | Templates = PSMs, not prose (Comparative inference) |
| Ontology maturity | Synthetic BERT tags + expert confirm | Formal shared conceptualization + design principles | Deepen with modularity / minimal encoding bias (Author-stated) |
| Evaluation stance | Subjective compliance 25–27%; proof-of-concept | Cyclic evaluation indispensable; models approximate | Frame 25–27% as early modeling cycle (Comparative inference) |
| Failure of transfer | Free rewrite + compile gate; Fig. 4b disasters | Transfer fails maintainability / mixed knowledge types | Compile ≠ expertise model (Empirically shown in A; Author-stated in B) |

---

## 7. PROTÉGÉ-II mappings: NL → method terms without full free codegen

PROTÉGÉ-II maps domain terms into method ontologies (rename, filter, class maps) and can generate KA tools from ontologies—closer to constrained Customizer design than to unrestricted LLM AST rewrite.

> **Quote (Studer et al.):** *"PROTÉGÉ-II offers different types of mapping relations: Renaming mappings… Filtering mappings… Class mappings…"*

> **Quote (Studer et al.):** *"A feature of PROTÉGÉ-II is that it can generate knowledge-acquisition tools from domain or application ontologies."*

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed… Syntactic analysis – checking the code’s compilability using the Python interpreter."*

A mapping layer (comment subclass → method concept → admissible loss fragment) would make the LLM fill *slots* in a method ontology, while compile checks stay necessary but secondary. (Speculative extension)

---

## 8. Reusability–usability and “more stringent rules”

Paper B warns that more general PSMs need refinement; Paper A’s instinct—“more stringent generation rules”—can recreate Role-Limiting rigidity unless templates are *configurable* methods with explicit assumptions.

> **Quote (Studer et al.):** *"The more general PSMs are, the more reusable they are, but applying them requires considerable refinement and adaptation. This phenomenon is known as the reusability-usability trade-off."*

> **Quote (Gindullina et al.):** *"These results should be considered proof-of-concept… highlighting the need to develop more stringent generation rules and control mechanisms to ensure the interpretability and reliability of the results."*

Stringency without a method library is transfer-era patching. Configurable PSMs (CRLMs in Paper B) are the KE name for class–subclass templates that still allow alternative fixes per task. (Comparative inference)

---

## 9. Mixed knowledge types: MYCIN lesson → Table A.2 + free codegen

Paper B’s MYCIN/maintenance critique—strategic knowledge mixed with domain rules—prefigures Paper A’s failure mode where comment intent, loss-component permissions, and optimizer side-effects are entangled inside one LLM rewrite.

> **Quote (Studer et al.):** *"e.g. in the MYCIN knowledge base strategic knowledge about the order in which goals should be achieved is mixed up with domain specific knowledge. This mixture of knowledge types, together with the lack of adequate justifications of the different rules, makes the maintenance of such knowledge bases very difficult and time consuming."*

> **Quote (Gindullina et al.):** *"An example of an ambiguous result is shown in Figure 4… the model increased the weight of the zero boundary condition… by a factor of four, which is difficult to interpret in relation to the expert’s request."*

Separating domain comment labels from inference-role justifications (why this operator, which assumption) is exactly what CommonKADS was invented to force. (Comparative inference)

---

## Direction 1. Introduction rewrite: novelty as KE modeling on PINN

**Pipeline stage:** manuscript framing (Introduction / “What this paper adds”).  
**Mechanism:** Cite transfer→modeling; claim a CommonKADS-style expertise model for *epidemiological forecast revision* whose inference layer is loss-PSMs and whose compiler is an LLM—not “first NL→objective.”  
**Failure modes addressed:** overclaim vs KE history; reviewer “what’s new vs expert systems?”  
**Evidence base:** Paper B §§2.1–3.1; Paper A box + 25–27% PoC. (Speculative extension — framing)

---

## Direction 2. Deepen ontology into domain + method/task layers

**Pipeline stage:** hierarchical classifier knowledge base + Future work templates.  
**Mechanism:** Keep four comment classes as domain ontology; add method ontology (penalty / offset / time-window / BC-fix) with numeric maps and assumptions; generate Customizer prompts from method slots (PROTÉGÉ-style), not free rewrite.  
**Failure modes addressed:** Table A.2 under-detail; literal numeric insertion; semantic opacity of edits.  
**Acceptance:** each accepted run cites method role + filled slots, auditable without reading raw loss AST. (Speculative extension)

---

## Manuscript placement

- **Introduction / “What this paper adds”:** reframe novelty as KE *modeling* on PINN+epidemiology (clusters **1**, **8**, **11** framing)—not “first NL→objective.”
- **§2.2 ontology + Future work templates:** CommonKADS-style domain vs method layers (cluster **9**).
- **Discussion of Fig. 4c:** MYCIN-style mixture of strategic and domain knowledge in one rewrite.

## What not to transfer

Do not rebuild full CommonKADS tooling, KARL, or 1990s PSM libraries as a product requirement. Paper B is a survey. Transfer **transfer→modeling vocabulary**, **layered ontologies**, and **PSM-as-template** thinking—not institutional KE process theater. (Comparative inference)

## Concrete next experiment

**Hypothesis.** A one-page novelty comparison table (Eureka / OPRO / Sahatova GUI / Expert-Guided PINN) changes reviewer-facing claims more than adding another LLM backbone.

| Dimension | Eureka/OPRO | Sahatova 2023 GUI | Expert-Guided PINN |
| :--- | :--- | :--- | :--- |
| Knowledge source | NL→reward/loss code | Sliders / params | NL→PINN loss |
| Fitness | Env / auto metric | Deterministic control | Subjective compliance |
| Verification | Rollout / score | Instant | Compile only |
| HITL | Optional | Direct | Comment + confirm class |
| Domain | RL / robotics | Epi forecasting | Epi PINN |

**Protocol.** Rewrite Introduction paragraph using this table; internal review for overclaim. (Speculative extension — framing experiment)

## Related essays in this series

- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — method ontology as grammar.
- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — reusable soft methods.
- [`02_steiner_2024_steering_wheel_crn.md`](02_steiner_2024_steering_wheel_crn.md) — inference protocol as PSM.
- Bridge: [`../dinara_analysis/15_ouyang_2022_instructgpt.md`](../dinara_analysis/15_ouyang_2022_instructgpt.md) — alignment as missing inference layer.

## Conclusion

Studer et al. supply the vocabulary Paper A needs for Q1 positioning: Expert-Guided PINN is knowledge *modeling* for epidemic forecast revision on a PINN substrate, not a first transfer of natural language into an objective. CommonKADS layers, PSM libraries, and ontology design principles explain why a thin class/subclass tree plus English prohibitions cannot control an LLM rewriter—and why Future work templates should be published as reusable loss-modification methods with explicit roles and assumptions. Deepen the ontology along those lines; reserve novelty for the PINN+epidemiology application, not for NL as such.
