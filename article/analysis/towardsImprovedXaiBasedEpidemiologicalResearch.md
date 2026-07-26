> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., 2026) implements Expert-Guided PINN: expert comment → LLM loss edit → SIRD PINN retrain → qualitative success judgment. Paper B (Khalili & Wimmer, 2024, *Towards Improved XAI-Based Epidemiological Research into the Next Potential Pandemic*) is a PRISMA-based review (1,285 papers screened; 26 epidemiological+XAI studies deep-analyzed) that proposes a **six-stage ML pipeline** and five gap clusters: data, modeling, explanation, uncertainty, generation.

Paper B does not cite Paper A (expected: parallel publication streams). It nonetheless **diagnoses architectural narrowness** in systems that jump straight to training-time edits without preprocessing, feature engineering, uncertainty, or model-specific XAI — exactly Paper A's profile.

---

## 1. Pipeline scope: pointwise loss edit vs. end-to-end epidemiological ML

Paper B's reference framework:

> **Quote (Khalili & Wimmer):** *"Data preprocessing, feature engineering, parameter tuning, model training, model evaluation, and model explanation (XAI). This more detailed pipeline is extracted from the literature analysis."*

Paper A's visible pipeline:

> **Quote (Gindullina):** *"The architecture of the proposed solution includes four main components (Figure 1):... 4. LLM that translates a comment into executable code for a loss function satisfying given constraints."*

Expert intervention occurs almost entirely at **model training** via $\mathcal{L}_{total} = \mathcal{L}_{data} + \mathcal{L}_{IC} + \mathcal{L}_{ODE} + \text{Penalty}_{LLM}$. Paper B predicts that NPI timing, missing data, and feature selection errors upstream will not be fixed by loss penalties alone — consistent with flat or runaway curves when only $L_{ODE}$ weights change.

| Stage | Paper A coverage | Paper B emphasis | Takeaway |
|:--- |:--- |:--- |:--- |
| Data preprocessing | Fixed SPb incidence series | Imputation, imbalance, sparsity | A does not let experts fix input anomalies |
| Feature engineering | Implicit in SIRD states | NPIs, mobility, variants | A lacks explicit NPI feature channel |
| Parameter tuning | Ad hoc MAE thresholds | Bayesian / evolutionary search | A's gates are not full hyperparameter protocol |
| Model training | PINN + LLM loss | Hybrid SEIR-DL, ensembles | A is PINN-centric |
| Evaluation | 4 qualitative criteria | Continuous + classification metrics | A weak on formal semantic metrics |
| XAI | Post-hoc plot inspection | SHAP, IG, CBR, rule-based | A lacks model-specific explanation |

---

## 2. Hybrid dynamics: time-varying $\beta(t)$ vs. penalty hacking

Paper B on hybrid models:

> **Quote (Khalili & Wimmer):** *"SEIR-based ML models combine compartmental models with machine learning models to replace the fixed parameters of the former with time-varying parameters that are fitted using machine learning methods... Hybrid CNN-LSTM architectures as well as novel GNN approaches are archetypal alternative approaches that can represent the time-varying character of SEIR model parameters in a robust and explainable manner."*

Paper A keeps fixed SIRD structure; LLM adds penalties:

> **Quote (Gindullina):** *"The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process."*

When experts describe delayed peaks from late restrictions, Paper B's prescription is to learn **$\beta(t)$ or measure-aware inputs**. Paper A's boundary-condition weight change is a penalty hack Paper B's hybrid framing would treat as structurally misaligned — explaining catastrophic dynamics without blaming LLM syntax alone.

Paper B notes PINNs were **absent** in their reviewed COVID corpus but flags them for future XAI epidemiology:

> **Quote (Khalili & Wimmer):** *"Physics-informed neural networks (PINNs) [145] and neural ordinary differential equations (Neural ODEs) [146] are further noticeable modeling approaches that are not identified within the searched scope... but need to be considered more in future XAI-based epidemiologic research."*

Paper A is an early PINN+expert datapoint Paper B's gap analysis called for.

---

## 3. Case-based reasoning vs. scratch codegen

Paper B:

> **Quote (Khalili & Wimmer):** *"Case-based reasoning (CBR) techniques are another decent technique... In the evidence-based medical domain, cases are the most specialized form of knowledge representation... However, this area of research has not yet been explored in an XAI-based epidemiological context."*

Paper A's failures:

> **Quote (Gindullina):** *"The Meta-Llama-3.1-8B-Instruct model performed poorly, as half of the generated loss functions were uncompilable."*

> **Quote (Gindullina):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates."*

Paper B's CBR recommendation **converges** with Paper A's stated template future work: retrieve analogous past epidemic corrections instead of zero-shot codegen. DeepSeek-generated synthetic comments for BERT training are a weak form of case synthesis; they do not ground loss edits in verified epidemiological precedents.

---

## 4. Model-agnostic vs. model-specific XAI for the LLM–PINN stack

Paper B critiques agnostic explainers:

> **Quote (Khalili & Wimmer):** *"Model-agnostic methods are indeed surrogates, which first presume an ML model as a black box, then derive their interpretations... from a different modeling perspective with priors that are not necessarily in line with the internal procedures of the original model."*

Paper A's interpretability gap:

> **Quote (Gindullina):** *"A significant limitation is the lack of mechanisms to control the interpretability of the generated loss functions."*

Paper B recommends Integrated Gradients, attention weights, EBM/rule-based models for epidemiology (survey Sections 3.6, 5.3). Applied to Paper A: explain **PINN sensitivities** and **LLM-chosen penalty terms** with model-specific tools, not only final plots. Paper A's future “LLM-loss-semantic-checker” parallels Paper B's developer-level XAI for catching semantic/syntax errors at build time:

> **Quote (Khalili & Wimmer):** *"XAI enables system developers to take a look at the internal workings of AI-based algorithms and helps them eliminate potential pitfalls (e.g., misunderstandings of semantics and syntax errors)."*

---

## 5. Uncertainty: deterministic curves under scarce data

Paper B:

> **Quote (Khalili & Wimmer):** *"At the onset of pandemic phases, where the available data are scarce, not only the task of forecasting but also the task of explaining and generating suitable epidemiological policies are required to be inherently of a non-deterministic nature... Bayesian neural networks (to infer distributions over the models' weights and outputs), can enhance future epidemiological pipelines."*

Paper A outputs a single retrained forecast; expert comments shift a point estimate. Early-pandemic sparse windows are exactly when Paper B demands **uncertainty bands** so loss edits move distributions rather than collapsing optimization. Paper A's subjective compliance criterion is incompatible with Paper B's policy-facing trust model unless intervals are shown.

---

## 6. Generative counterfactuals and policy support

Paper B:

> **Quote (Khalili & Wimmer):** *"Generative epidemiological pipelines can create government policies along with different counter-factual scenarios as the pandemic spreads beyond the forecasting models."*

Paper A uses LLMs narrowly for loss code and synthetic classifier data. Expert comments are **implicit counterfactuals** (“peak should be later”) but the system does not branch scenarios — it commits to one retrain. Paper B would extend Paper A with generative what-if panels per comment class.

---

## 7. Evaluation gaps: 25–27% success in Paper B's lens

Paper A:

> **Quote (Gindullina):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models."*

Paper B laments missing global XAI evaluation schemas for epidemiology (Section 5.3). Paper A's MAE 700/1100 thresholds and n=20, T=1.0 are not bootstrap-stable protocol — unlike Paper B's PRISMA-inspired rigor for literature, not for single-system eval. Low comment compliance aligns with Paper B's thesis that **pipeline-stage omissions** (no feature-stage expert fix, no uncertainty, agnostic eval) compound.

---

## Proposed direction 1. CBR template library for PINN Customizer (model training)

**Pipeline stage:** PINN Customizer (replaces free codegen).

**Mechanism:** Retrieve k nearest historical (comment class, loss patch, outcome) cases; adapt template coefficients.

**Failure mode addressed:** 50% Llama-8B compile failure; 25–27% semantic success.

---

## Proposed direction 2. Expert-in-the-loop feature engineering for NPIs (preprocessing / features)

**Pipeline stage:** New upstream module before PINN.

**Mechanism:** Let experts flag missing NPI or reporting anomalies; adjust inputs per Paper B's Stage 1–2.

**Failure mode addressed:** Penalty-only edits that cannot fix data/feature mismatch.

---

## Proposed direction 3. Bayesian PINN forecast bands (evaluation / training)

**Pipeline stage:** PINN training + display.

**Mechanism:** Ensemble or B-PINN; expert comment shifts interval, not single curve.

**Failure mode addressed:** Deterministic failures under scarce data (Paper B Section 5.4).

---

## Proposed direction 4. Integrated Gradients on compartment losses (model explanation)

**Pipeline stage:** Post-retrain XAI module.

**Mechanism:** Attribute forecast change to $L_{data}$, $L_{IC}$, $L_{ODE}$, LLM penalty terms.

**Failure mode addressed:** Loss interpretability gap.

---

## Proposed direction 5. Multi-agent semantic checker at developer XAI layer (PINN Customizer)

**Pipeline stage:** Pre-retrain validation.

**Mechanism:** Implement Paper A's proposed checker using Paper B's developer-facing XAI role.

**Failure mode addressed:** Semantically random loss modifications.

---

## Conclusion

Paper A is a pioneering **Stage 4–5 prototype** (training + informal evaluation) with expert steering. Paper B's systematic review explains why such prototypes stall at 25–27%: epidemiological AI needs the full six-stage pipeline, CBR/template grounding, model-specific XAI, and explicit uncertainty for policy trust. Paper A's own future-work agenda (templates, multi-agent checkers) is already enumerated in Paper B's gap figure — the comparison turns both papers into a joint roadmap from proof-of-concept to industrial decision support.
