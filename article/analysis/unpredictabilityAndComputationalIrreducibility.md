Paper A (Gindullina et al., Expert-Guided PINN) runs an expert-in-the-loop cycle where an LLM edits SIRD-PINN loss code and the system **must retrain** before anyone can judge the forecast. Paper B (Zwirn & Delahaye, *Unpredictability and Computational Irreducibility*) proves that for computationally irreducible (CIR) systems there is **no shortcut** to the $n^{\text{th}}$ state faster than stepwise simulation. The thesis: Gindullina’s architecture **institutionalises** CIR-style epistemology (macro epidemic curves knowable only after running the PINN) while still tempting users to believe NL edits compress that path—hence high compile rates beside 25–27% semantic compliance (Comparative inference).

---

## 1. CIR: no shortcut to the nth state

> **Quote (Zwirn & Delahaye):** *«Given a physical system whose behavior can be calculated by simulating explicitly each step in its evolution, is it always possible to predict the outcome without tracing each step? That means: is there always a shortcut to go directly to the nth step?»*

> **Quote (Zwirn & Delahaye):** *«A cellular automaton (CA) is computationally irreducible if in order to know the state of the system after n steps there is no other way than to evolve the system n times according to the equations of motion. That means that there is no short-cut, no way to compress the dynamic.»*

> **Quote (Zwirn & Delahaye):** *«For CIR automata, functions or processes, there is no short-cut allowing to predict the nth state faster than waiting till all the steps are done. In this sense, these objects are unpredictable.»*

Epidemic PINN training iterates gradient steps on coupled data, IC, and ODE residuals—numerical simulation of a hybrid dynamical system (Comparative inference). Zwirn formalises why **outcome preview without run** may be ill-posed for CIR-like objects.

---

## 2. Mandatory retraining as enforced simulation

> **Quote (Gindullina et al.):** *«After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN... The model is trained with the Adam optimizer... Upon completion of the training process, the system visualizes the resulting forecast... and presents it to an expert for comparative analysis.»* (§2.3)

> **Quote (Gindullina et al.):** *«The loop is closed by presenting the refined forecast to the expert, enabling continuous model alignment with domain knowledge.»* (Introduction)

Neither expert nor LLM receives the new incidence curve **before** optimization completes (Author-stated workflow). That matches CIR intuition: macrostate (curve shape) requires running microdynamic update (PINN epochs) (Comparative inference).

---

## 3. Expert comment as external condition, not a compression algorithm

> **Quote (Zwirn & Delahaye):** *«We prove that... if the behavior of an object is computationally irreducible, no computation of its nth state can be faster than the simulation itself.»*

> **Quote (Gindullina et al.):** *«Our solution eliminates the need for rigorous a priori mathematical formalization... offering epidemiologists an adaptive tool for calibrating forecasts without requiring a deep understanding of the model's internal parameterization.»*

Expert NL acts as **external condition** shifting loss weights—analogous to contingent inputs in CIR formalism—not as a proof that the $n^{\text{th}}$ forecast state is derivable in closed form (Comparative inference). Accessibility claim must not be read as computational shortcut (Speculative extension).

---

## 4. Compile-fix verifies syntax, not shortened prediction path

> **Quote (Gindullina et al.):** *«Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated.»*

> **Quote (Zwirn & Delahaye):** *«CIR is meaningful only regarding the way the different states are related each others... what CIR means implies that there exists no general program which can compute for every n the nth state from n faster than the ECA.»*

Compile loops repair **token-level** programs; they do not certify that the edited loss yields a predictable macro trajectory without full retrain (Comparative inference). 80–100% compile with 25–27% compliance separates syntax path from semantic epidemic path (Empirically shown).

---

## 5. Fig. 4b sensitivity: micro-rule perturbation, unexpected macrostate

> **Quote (Gindullina et al.):** *«Training with this modified loss produced a new forecast... that effectively ignores this boundary condition. As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days).»* (§3.3, Fig. 4b)

> **Quote (Zwirn & Delahaye):** *«It is now common knowledge that it is not because the behavior of a system is deterministic that it is possible to predict it.»* — common knowledge motivating CIR (Introduction).

Small boundary-condition edit → catastrophic macro change resembles sensitivity to microdynamic rules in complex systems (Comparative inference). Not proof that SIRD-PINN is CIR in Zwirn’s formal sense, but explains why **preview-free** interaction is risky (Author-stated ambiguous outcomes).

---

## 6. Evaluation at T=1.0 explores variance, not compressed decision

> **Quote (Gindullina et al.):** *«All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment.»*

> **Quote (Zwirn & Delahaye):** *«Predicting the behavior of a computation machine is to be able to find the result it computes faster than the machine itself.»*

High-temperature sampling multiplies distinct loss edits, each requiring full simulation to evaluate—**anti-compression** in practice (Comparative inference). Production T=0–0.2 would reduce variance but not remove retrain obligation (Author-stated).

> **Quote (Gindullina et al.):** *«For production deployment, a lower temperature setting (e.g., 0 or 0.2) will be applied to ensure result reproducibility and system stability.»* (§2.4)

> **Quote (Zwirn & Delahaye):** *«Considering the case of possibly CIR predicates shows that the real meaning of CIR is located inside the very succession of states not inside any single state.»*

---

## 7. Joint success and marginal metrics under simulation cost

> **Quote (Gindullina et al.):** *«Forecast has changed. A check is performed to ensure that the new forecast differs significantly from the original... MAE greater than 700»* (§2.4 criterion 2).

> **Quote (Gindullina et al.):** *«Matching training data... A value of 1100 was empirically chosen as the threshold»* (§2.4 criterion 1).

Marginal criteria can pass while primary compliance fails—each marginal check still requires a completed PINN run (Empirically shown Fig. 5). Under CIR logic, there is no cheaper filter that certifies semantic success without paying simulation cost for each candidate loss (Comparative inference).

---


## 8. Wolfram conjecture and epidemic simulation practice

> **Quote (Zwirn & Delahaye):** *«Wolfram conjectured that in most cases the answer is no. This "no" expresses the concept of computational irreducibility (CIR).»*

> **Quote (Gindullina et al.):** *«Compartmental models represent a standard and widely adopted approach... describe the dynamics of transitions between compartments using systems of ordinary differential equations.»* (§2 Methodology)

Epidemic ODE+PINN hybrids are not elementary cellular automata, yet public-health practice already treats **scenario simulation** as the honest path to intervention outcomes (Author-stated in both traditions). Paper A operationalises that norm while marketing NL accessibility (Comparative inference).

---

## 9. Comparison table

| Criterion | Paper A (Expert-Guided PINN) | Paper B (Zwirn & Delahaye) | Takeaway |
| :--- | :--- | :--- | :--- |
| Core question | Can NL steer epidemic PINN? | When is simulation unavoidable? | A embodies B’s answer operationally |
| Macro prediction | After PINN retrain | After n evolution steps | Both reject free lookahead |
| Shortcut claim | Implicit via LLM one-shot code | Formally rejected for CIR | A must not oversell NL |
| Verification | Python compile | Proof on automata/functions | Syntax ≠ semantic epidemic fit |
| Failure mode | 700-day curve | Unpredictable nth state | Micro edit, macro surprise |
| Human role | Expert judges post-sim | Theorist defines CIR | Expert is post-hoc observer |

---

## Direction 1. Pre-simulation macro hypothesis (no full retrain)

**Stage:** PINN Customizer. **Mechanism:** LLM outputs predicted qualitative curve change; expert approves before Adam loop. **Failure mode:** Expert cannot mentally simulate PINN (CIR epistemology) (Speculative extension).

## Direction 2. Report simulation cost per interaction round

**Stage:** Evaluation. **Mechanism:** Log epochs, wall time, LLM calls alongside compliance—make irreducibility **visible**. **Failure mode:** Hidden latency breaks «interactive» claim (Comparative inference).

## Direction 3. Conversational Agent flags shortcut-seeking comments

**Stage:** Conversational Agent. **Mechanism:** Reject comments implying closed-form peak shift without training. **Failure mode:** Expert expects instant curve edit (Speculative extension).

## Direction 4. Abstain on high sensitivity edits

**Stage:** Retraining loop. **Mechanism:** Detect large BC/weight perturbations; require confirmation or ensemble retrain. **Failure mode:** Fig. 4b boundary weakening (Empirically shown) (Speculative extension).

## Direction 5. Hold-out future macrostates for true forecast

**Stage:** Evaluation. **Mechanism:** Withhold post-peak days from loss fitting so macrostate is not interpolative. **Failure mode:** Expert comments on already-visible decline (dinara_comprehensive_review.md §A.3) (Speculative extension).

---

## Conclusion

Zwirn & Delahaye clarify that determinism does not grant **fast macro prediction** for CIR-like systems. Gindullina et al. build a practical loop that always pays the simulation price (PINN retrain) yet markets NL as easing formalization. The gap between 80%+ compile and 25–27% compliance is consistent with CIR-style epistemology: editing micro-rules (loss) cheaply does not compress deriving macro epidemic curves. Future work should make simulation cost and abstention explicit rather than implying LLM edits shortcut epidemiological dynamics.
