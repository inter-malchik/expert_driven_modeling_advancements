> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., Expert-Guided PINN) presents an interactive calibration loop for epidemiological forecasts and reports that experiments «confirm the fundamental feasibility» of the approach at 25–27% «Compliance with the comment». Paper B (Oreskes, Shrader-Frechette & Belitz, 1994, *Verification, Validation, and Confirmation of Numerical Models in the Earth Sciences*) argues that for models of open natural systems **verification and validation are impossible**, confirmation is always partial, and the primary value of a model is heuristic.

The connection is tight for public health: SIRD-PINN models an open biological system with incomplete data, auxiliary hypotheses, and repeated calibration. Paper A uses the language of «confirming success» and four evaluation criteria that Paper B would classify as partial corroboration—not validation. The comparative thesis: Expert-Guided PINN is methodologically closer to Oreskes's honest heuristic framing than its abstract lexicon suggests, but its evaluation vocabulary risks overstating what 25–27% compliance can establish for policy.

---

## 1. Impossibility thesis vs. the language of «confirmation» in the abstract

The central thesis of Paper B:

> **Quote (Oreskes et al.):** *«Verification and validation of numerical models of natural systems is impossible. This is because natural systems are never closed and because model results are always non-unique. Models can be confirmed by the demonstration of agreement between observation and prediction, but confirmation is inherently partial.»*

> **Quote (Oreskes et al.):** *«The primary value of models is heuristic.»*

Paper A in the abstract:

> **Quote (Gindullina et al.):** *«Experimental results confirm the fundamental feasibility of this approach, demonstrating a success rate of 25-27% for the best models and providing a compelling proof-of-concept.»*

«Confirm feasibility» in Paper A is more correctly read in Paper B's sense—*partial* confirmation of the idea's usefulness, not verification of forecast reliability for policy. Paper A's own «proof-of-concept» label is closer to Oreskes's heuristic value.

---

## 2. Open systems: epidemic modeling as hydrogeology

Natural systems are not closed:

> **Quote (Oreskes et al.):** *«Numerical models may contain closed mathematical components that may be verifiable... However, the models that use these components are never closed systems.»*

> **Quote (Oreskes et al.):** *«What we call data are inference-laden signifiers of natural phenomena to which we have incomplete access.»*

The epidemiological PINN on 359 days of ARVI data (July 2020 – June 2021) inherits the same problems: incomplete parameters, epidemic control measures outside SIRD, virus mutations—«auxiliary hypotheses» in Paper B's terminology. Paper A acknowledges PINN optimization complexity:

> **Quote (Gindullina et al.):** *«The use of physics-informed neural networks inherits their systemic limitations... including the complexity of optimization, sensitivity to hyperparameters, and the lack of guarantees that physical constraints will be satisfied in the final solution.»*

These are symptoms of an open, underdetermined system—not failures a closed-system verification pass could eliminate.

---

## 3. Non-uniqueness and multiple loss functions yielding the same plot

> **Quote (Oreskes et al.):** *«More than one model construction can produce the same output. This situation is referred to by scientists as nonuniqueness and by philosophers as underdetermination.»*

> **Quote (Oreskes et al.):** *«A faulty model may appear to be correct.»*

> **Quote (Gindullina et al.):** *«All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment.»*

Paper A: the LLM generates different loss functions at temperature=1.0; 15–28% of runs barely change the forecast; «Compliance with the comment» is 25–27% while 73–80% show «forecast has changed». Different penalty sets can yield visually similar curves with different physics—a 700-day epidemic with «plausible shape». Oreskes warns: agreement between the plot and the comment does not select a unique model.

---

## 4. Affirming the consequent: instruction-following success ≠ model truth

> **Quote (Oreskes et al.):** *«To claim that a proposition (or model) is verified because empirical data match a predicted outcome is to commit the fallacy of affirming the consequent.»*

> **Quote (Oreskes et al.):** *«If a model fails to reproduce observed data, then we know that the model is faulty in some way, but the reverse is never the case.»*

Paper A deliberately separates instruction-following from the quality of the expert's advice:

> **Quote (Gindullina et al.):** *«It is crucial to note that the successful model modification via external input does not mean the quality or correctness of the expert's suggestion itself... This study, therefore, assesses the capability for instruction-following, not the impact of the comment on forecast accuracy.»*

This aligns with Paper B. But the phrasing «confirm feasibility» in the abstract risks being read as affirming the consequent at the level of the whole system—especially for regulators, whom Oreskes cites as interpreting «validated» as «true».

---

## 5. Calibration vs. the «verification phase»: expert-in-the-loop as forced empirical adequacy

> **Quote (Oreskes et al.):** *«The process of tuning the model... is known as calibration.»*

> **Quote (Oreskes et al.):** *«Models almost invariably need additional tuning during the so-called verification phase... This limitation indicates that the so-called verification is a failure. The second step is merely a part of the calibration.»*

Paper A's cycle is a series of loss calibrations driven by comments:

> **Quote (Gindullina et al.):** *«The expert analyses the updated forecast and judges its quality.»*

> **Quote (Gindullina et al.):** *«Matching training data... A value of 1100 was empirically chosen as the threshold... using the MAE metric.»*

MAE thresholds of 1100/700 are empirical «forced empirical adequacy» (Paper B's term via van Fraassen), not independent validation on a hold-out future. Oreskes: post-audit shows that models with good history match often fail going forward.

---

## 6. Neutral evaluation language vs. «Successful / Unsuccessful / Ambiguous»

> **Quote (Oreskes et al.):** *«A neutral language is needed for the evaluation of model performance... Judgmental terms such as excellent, good, fair, and poor are useful because they invite, rather than discourage, contextual definition.»*

> **Quote (Oreskes et al.):** *«Verify and validate are affirmative terms: They encourage the modeler to claim a positive result.»*

Paper A introduces three outcome groups:

> **Quote (Gindullina et al.):** *«Successful result. The curve is reshaped in accordance with the expert's request, and its form does not contradict the laws of epidemic dynamics.... Unsuccessful result. The curve is reshaped incorrectly.... Ambiguous result. The expert's requirements are formally satisfied, but the result is questionable (for example, the curve looks unrealistic).»*

«Ambiguous» is a step toward Oreskes's neutrality. But «Compliance with epidemic logic» at 90–100% alongside 25–27% comment compliance creates a false sense of physics «validation» when semantics fail—a conflation of levels that Paper B cautions against using DOE/IAEA definitions of validation as an example.

---

## 7. Heuristics and sensitivity: what the model *can* do for policy

> **Quote (Oreskes et al.):** *«Models can be also be used for sensitivity analysis—for exploring "what if" questions—thereby illuminating which aspects of the system are most in need of further study.»*

> **Quote (Oreskes et al.):** *«Models are most useful when they are used to challenge existing formulations, rather than to validate or verify them.»*

Paper A is closer to this position in its discussion of limitations:

> **Quote (Gindullina et al.):** *«These results should be considered proof-of-concept, demonstrating the potential of the approach but also highlighting the need to develop more stringent generation rules and control mechanisms.»*

Expert-Guided PINN heuristically explores the space of «what if the expert is right about the curve shape»—it does not prove that SIRD-PINN is true. Oreskes provides language for honest positioning before the Smorodintsev Institute.

---

## 8. Comparison table

| Criterion | Paper A (Gindullina et al.) | Paper B (Oreskes et al.) | Takeaway |
|:--- |:--- |:--- |:--- |
| Epistemic claim | «Confirm fundamental feasibility» at 25–27% | Confirmation is always partial; V&V impossible for open systems | A's headline overstates what partial corroboration allows |
| System type | Open epidemic process (SIRD-PINN) | Open natural systems (hydrogeology) | Same epistemic constraints apply |
| «Verification» in practice | Python compile check | Only closed mathematical subcomponents verifiable | A conflates syntax with truth |
| Model uniqueness | Many loss edits → similar plots (T=1.0) | Non-uniqueness / underdetermination | Visual fit does not identify one true model |
| Calibration | Expert-driven loss tuning + MAE thresholds | Calibration ≠ validation; «verification phase» is tuning | A's loop is calibration, not independent validation |
| Primary value | Proof-of-concept / instruction-following | Heuristic exploration and sensitivity | Honest framing aligns when caveats are explicit |

Paper A's subjective compliance metric is itself a form of partial corroboration—expert judgment, not independent test data:

> **Quote (Gindullina et al.):** *«The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion.»*

Oreskes would classify this as contextual, judgmental evaluation—acceptable if labeled as such, misleading if called validation.

---

## Proposed direction 1. Replace «validation» in the UI with «corroboration / relative fit»

**Stage:** Evaluation / expert-facing reports (§2.4). **Mechanism:** Label outcomes as «partial agreement with the comment» or «relative fit to expert intent», not «successful model validation». **Failure mode:** Regulators or clinicians interpret 25–27% compliance as a validated forecast oracle.

## Proposed direction 2. Hold-out temporal split as weak confirmation

**Stage:** Evaluation setup (§2.4, 359-day dataset). **Mechanism:** Split July 2020 – June 2021 into calibration / confirmation windows; tune loss only on the first half, report partial confirmation on the second—mirroring hydrologists in Paper B. **Failure mode:** MAE thresholds 1100/700 calibrated on the same data used for scoring.

## Proposed direction 3. Explicit non-uniqueness block for the expert

**Stage:** PINN Customizer output + retraining loop. **Mechanism:** When compliance succeeds, display a warning that alternative loss functions may yield similar plots; optionally show one rejected candidate from T=1.0 diversity. **Failure mode:** Expert accepts a 700-day «plausible» curve as uniquely correct.

## Proposed direction 4. Sensitivity instead of a single forecast

**Stage:** Retraining loop after loss edit. **Mechanism:** Perturb penalty weights ±ε and plot forecast bands; report curve stability as robustness, not truth—Oreskes's sensitivity analysis for «what if». **Failure mode:** Single deterministic retrain masks fragile edits that pass one visual check.

## Proposed direction 5. Documenting auxiliary hypotheses per class/subclass

**Stage:** Hierarchical classifier + PINN Customizer (§2.2–2.3). **Mechanism:** For each confirmed class/subclass, log implicit assumptions (e.g., Class 2: measures enter only through term2; fixed population $N$)—an audit trail of system openness per Oreskes. **Failure mode:** Hidden auxiliary hypotheses make failed forecasts look like LLM errors rather than model misspecification.

---

## Conclusion

Paper B rules out claims of verification/validation for models of open natural systems and proposes confirmation (partial), relative evaluation, and heuristic value. Paper A is methodologically closer to the latter—proof-of-concept, separating instruction-following from forecast accuracy—but the lexicon of «confirm feasibility» and high «epidemic logic» marginals without underdetermination caveats create an epistemic gap. For epidemiological decision support, Oreskes's honest framing fits Expert-Guided PINN as a tool for aligning expert judgment with a formal model and exploring «what if», not as a verified forecast oracle.
