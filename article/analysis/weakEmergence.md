Paper A (Gindullina et al., Expert-Guided PINN) lets experts state macroscopic epidemic goals in natural language while an LLM rewrites **micro-level** loss code; the PINN must then be **simulated** (retrained) to reveal the curve. Paper B (Bedau, 1997, *Weak Emergence*) defines macrostates that are derivable from microdynamics **only by simulation**, and warns against illicit «downward causation.» Gindullina’s loop is a worked example of weak-emergence epistemology with an engineered top-down control attempt—explaining why experts and LLMs cannot reliably predict compliance before training and why reverse macro→micro mapping succeeds only ~25–27% (Comparative inference).

---

## 1. Weak emergence: macrostate P only by simulation

> **Quote (Bedau):** *«Macrostate P of S with microdynamic D is weakly emergent iff P can be derived from D and S's external conditions but only by simulation.»*

> **Quote (Bedau):** *«To simulate the system one iterates its microdynamic, given a contingent stream of external conditions as input. Since the macrostate P is a structural property constituted out of the system's microstates, the external conditions and the microdynamic completely determine whether P materializes at any stage in the simulation.»*

Epidemic **curve shape** (peak, decline) is macrostate **P**; SIRD residuals and loss weights are microdynamic **D** with expert comments as external conditions (Comparative inference).

---

## 2. SIRD-PINN microdynamic and incidence macrostate

> **Quote (Gindullina et al.):** *«The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process.»* (§2, Methodology)

> **Quote (Gindullina et al.):** *«Four basic classes... 1. Behavior of the epidemiological curve (visual characteristics)... 4. Position of the epidemic peak on the time axis.»* (§2.2, Appendix A)

Classes 1 and 4 explicitly tag **macrostates** experts observe; LLM edits operate on ODE/loss microstructure (Author-stated). Bedau’s ontology maps cleanly (Comparative inference).

---

## 3. Mandatory PINN training as simulation step

> **Quote (Bedau):** *«What distinguishes a weakly emergent macrostate is that this sort of simulation is required to derive the macrostate's behavior from the system's microdynamic.»*

> **Quote (Gindullina et al.):** *«Upon completion of the training process, the system visualizes the resulting forecast, calculates metrics, and presents it to an expert for comparative analysis.»* (§2.3)

> **Quote (Gindullina et al.):** *«The user then receives a new prediction, which they can then decide whether it satisfies their comment or not.»* (Fig. 1 caption)

Without retrain, link penalty→curve is unknowable—Bedau’s simulation requirement in production code (Comparative inference).

---

## 4. Expert as macro-observer; Game of Life parallel

> **Quote (Bedau):** *«In general, though, it is impossible without simulation to derive the behavior of any macrostate in a Life configuration even given complete knowledge of the configuration.»*

> **Quote (Gindullina et al.):** *«The expert evaluates the relevance of the modified forecast to the original comment and decides whether to retain it or re-modify it.»* (§2.3)

Experts classify visual curve behavior (Classes 1–4) like Life observers classifying gliders—post-simulation macro labeling (Comparative inference). Accuracy 81% on synthetic comment classes does not replace simulating PINN outcomes (Empirically shown, Table 1).

---

## 5. Micro perturbation, macro surprise: Fig. 4b

> **Quote (Gindullina et al.):** *«The LLM responded to this comment by reducing the influence of the zero boundary condition in the loss function... the epidemic curve... exhibits an unrealistically long outbreak duration (more than 700 days).»*

> **Quote (Bedau):** *«Conway's Game of Life abounds with weakly emergent properties»* where macro behavior cannot be derived without running the micro rule.

Boundary-weight tweak ↔ micro rule change; 700-day curve ↔ unexpected macro property (Comparative inference). Bedau predicts such sensitivity for nonlinear micro→macro maps (Author-stated failure taxonomy).

---

## 6. Strong emergence rejected; engineered top-down control in A

> **Quote (Bedau):** *«Property P is an emergent property of a (mereologically-complex) object O iff P supervenes on properties of the parts of O, P is not had by any of the object's parts, P is distinct from any structural property of O, and P has a direct ("downward") determinative influence on the pattern of behavior involving O's parts.»* (O'Connor's strong emergence, discussed critically)

> **Quote (Gindullina et al.):** *«An LLM synthesizes this specification into executable code, which, after passing sanity checks, guides the PINN's training.»* (Introduction)

Expert macro intent → rewritten micro loss mimics **downward control** Bedau limits to weak, agent-mediated form (Comparative inference). 25–27% compliance measures failed reverse engineering of emergent curves (Empirically shown).

---

## 7. 25–27% as cost of non-compressible macro→micro map

> **Quote (Gindullina et al.):** *«The key result is confirmation of the fundamental feasibility... with a success rate of 25-27% for the best models. These results should be considered proof-of-concept»* (§3.4).

> **Quote (Bedau):** *«Underivability without simulation is a purely formal notion concerning the existence and nonexistence of certain kinds of derivations of macrostates from a system's underlying dynamic.»*

Low compliance is consistent with macro specification not compressing to a unique micro edit without search/simulation—not merely weak LLM scale (Comparative inference).

> **Quote (Bedau):** *«Empirical observation is generally the only way to discover these laws. With few exceptions, it is impossible without simulation to derive the behavior of any macrostate in a Life configuration even given complete knowledge of the configuration.»*

> **Quote (Gindullina et al.):** *«Modifications to the loss function may be effectively random rather than logically justified by epidemiological reasoning.»* (§3.3, ambiguous result discussion)

---


## 8. Chaotic sensitivity and PINN nonlinearity

> **Quote (Bedau):** *«Weak emergence has a special source in this kind of chaos: exponential divergence of trajectories, also known as sensitive dependence on initial conditions or "the butterfly effect". This particular mechanism does not underlie all forms of weak emergence, though.»*

> **Quote (Gindullina et al.):** *«After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN (we used a PINN's architecture based on the SIRD model equations from Abramova and Leonenko (2024))»* (§2.3)

SIRD compartmental dynamics can exhibit sensitive dependence on parameters and loss weighting even when the governing ODEs are low-dimensional (Comparative inference). Fig. 4b's 700-day tail is consistent with weak emergence under nonlinear coupling between data fit, boundary penalties, and ODE residuals—not a random compile artefact (Empirically shown).

---

## 9. Comparison table

| Criterion | Paper A (Expert-Guided PINN) | Paper B (Bedau) | Takeaway |
| :--- | :--- | :--- | :--- |
| System S | SIRD-PINN epidemic model | Cellular automata / agent models | Both micro→macro |
| Microdynamic D | Loss + ODE residuals | Birth-death / local rules | Editable in A via LLM |
| Macrostates P | Curve shape, peak | Gliders, growth patterns | Expert comments target P |
| Derivation method | PINN training | CA iteration | Both simulation-only |
| Top-down control | NL→loss (engineered) | Discouraged (strong emergence) | A tests weak limits |
| Empirical outcome | 25–27% compliance | Simulation laws in Life | Failure = emergent difficulty |

---

## Direction 1. Show predicted macro functional before full retrain

**Stage:** PINN Customizer. **Mechanism:** LLM outputs scalar targets (e.g., post-peak slope sign) checkable without full epochs. **Failure mode:** Expert cannot preview curve (Bedau simulation requirement) (Speculative extension).

## Direction 2. Hold-out future macrostates in evaluation

**Stage:** Evaluation / retraining loop. **Mechanism:** Train only on pre-peak data; macro goals must predict unseen tail. **Failure mode:** Comment on already-observed decline (Comparative inference).

## Direction 3. Split classifier: macro-visual vs micro-parameter classes

**Stage:** Hierarchical classifier. **Mechanism:** Route Class 1/4 (macro) through template library; restrict free code on latent compartments. **Failure mode:** Penalties on unobserved S/R (dinara_comprehensive_review.md §A.4) (Speculative extension).

## Direction 4. Ensemble loss edits with macro voting

**Stage:** PINN Customizer + retraining. **Mechanism:** Sample k loss edits; expert picks macrostate closest to intent after cheap partial trains. **Failure mode:** Single-shot 25% success (Empirically shown) (Speculative extension).

## Direction 5. Document simulation-only disclaimer in UI

**Stage:** Conversational Agent / user pathway (Appendix A.7). **Mechanism:** State that curve outcome requires training—align expectations with weak emergence. **Failure mode:** Automation bias from plausible curves (Comparative inference).

---

## Conclusion

Bedau’s weak emergence formalises why epidemic curve outcomes cannot be read off from loss edits without running PINN optimization. Gindullina et al. implement that loop for public health, adding NL-mediated micro rewrites that attempt top-down steering Bedau treats cautiously. The architecture is scientifically coherent with weak emergence; the low primary success rate is the empirical signature of non-compressible macro→micro maps, not an incidental LLM hyperparameter issue alone.
