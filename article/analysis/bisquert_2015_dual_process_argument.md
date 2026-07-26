> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_20](https://doi.org/10.1007/978-3-319-23540-0_20)  
> **Source in `src/`:** [`../src/2015 Towards a Dual Process Cognitive Model for Argument Evaluation.md`](../src/2015%20Towards%20a%20Dual%20Process%20Cognitive%20Model%20for%20Argument%20Evaluation.md)

Gindullina et al. (hereafter **Paper A**) treat “Compliance with the comment” as a binary, author-judged primary success metric (25%/27%/6% for Llama-70B / DeepSeek / Llama-8B) and plan a future LLM-expert-evaluator without modeling *who* accepts an edit or *how deeply* they check it. Limitations already flag subjectivity; Future work still averages success as if all expert judgments were interchangeable.

Bisquert, Croitoru & Dupin de Saint-Cyr (2015; hereafter **Paper B**) formalize Kahneman/ELM dual-process argument evaluation: System 1 (association table \(AT\)) vs System 2 (KB + contextual entailment), with four engagement profiles—unconcerned, enthusiastic, quiescent, engaged—selected by interest \(i(\varphi)\) and awareness threshold \(\lambda\). The same argument can be accepted under S1 and rejected under S2 (DUR-DUR example). Thesis: **Paper A’s subjective compliance and planned Smorodintsev user studies mix S1 cue-matching with S2 warrant checks; stratifying experts by engagement profile is the missing design control for interpreting acceptance of LLM loss edits.**

---

## 1. Subjective compliance is an untyped acceptance event

Paper A’s primary criterion is a visual match between comment and forecast; authors themselves call it subjective and lack formal semantic metrics.

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

> **Quote (Gindullina et al.):** *"4. Compliance with the comment. This is the primary criterion for assessing the technical success of the modification system. A comparative analysis is performed between the expert’s text commentary and the visualization of the modified forecast."*

Paper B shows that “acceptance” is not one cognitive act: quiescent agents use shallow associations and speaker cues; engaged agents check warrants and premises via S2. Averaging 20 launches into a single compliance % conflates those acts. (Author-stated in A; Author-stated in B) (Comparative inference)

---

## 2. Four profiles: who is scoring the green curve?

Paper B’s profile function maps interest and stack size to cognitive route.

> **Quote (Bisquert et al.):** *"we define four levels of engagement: unconcerned, enthusiastic, quiescent or engaged with increasing involved level of cognition"*

> **Quote (Bisquert et al.):** *"profile(\(\varphi,\kappa\))= unc if \(i(\varphi)=0\); qui if \(i(\varphi)=1\) and \(|AT(\varphi)|<\lambda\); eng if \(i(\varphi)=1\) and \(|AT(\varphi)|\geq\lambda\); ent if \(i(\varphi)=2\)"*

> **Quote (Gindullina et al.):** *"Upon completion of the training process, the system visualizes the resulting forecast, calculates metrics, and presents it to an expert for comparative analysis… At this stage, the expert evaluates the relevance of the modified forecast to the original comment"*

A Smorodintsev epidemiologist who glances at Fig. 4a and says “sharper decline—OK” may be quiescent (S1 shape match); one who asks whether term2 penalty was the right warrant is engaged. Paper A’s protocol records neither \(i\) nor \(\lambda\). (Comparative inference)

---

## 3. S1 accepts what S2 rejects: the DUR-DUR lesson

Paper B’s running example is exactly the failure mode of shallow compliance: S1 accepts an argument that S2 later rejects after warrant/premise check.

> **Quote (Bisquert et al.):** *"While he would not have agreed with a deeper analysis, he instead relied on his S1, where post harvest separation is associated with something he rejects… and therefore accepted the argument."*

> **Quote (Bisquert et al.):** *"Then, he checks if the premise holds: as seen in Ex. 3, \(phs \mid\!\sim_2 \neg exp\), and thus \(phs \not\mid\!\sim_2 exp\). Hence, he rejects the argument."*

> **Quote (Gindullina et al.):** *"An example of an ambiguous result is shown in Figure 4… the new forecast shows a stabilization in the number of cases (although growth was requested)… modifications to the loss function may be effectively random rather than logically justified by epidemiological reasoning."*

Fig. 4c is an S1-accept / S2-reject candidate: the curve “changed somehow,” so a quiescent judge may mark success; an engaged judge checking warrant (comment → loss edit → forecast) should fail it. (Empirically illustrated in A; Formally shown in B) (Comparative inference)

---

## 4. Enthusiastic vs engaged: confirming prior vs checking warrant

Paper B distinguishes already-convinced flag matching from rational warrant validation.

> **Quote (Bisquert et al.):** *"evalarg(a,ent)= \(\oplus\) iff \(eval_1(c)=f\) else \(-\)"*

> **Quote (Bisquert et al.):** *"An engaged agent has to pass three steps before validating an argument: validity of the warrant… syntactic validity of the use of the warrant… rational validation of applicability"*

> **Quote (Gindullina et al.):** *"It is crucial to note that the successful model modification via external input does not mean the quality or correctness of the expert’s suggestion itself"*

Paper A already separates instruction-following from comment quality—but not judge profile. An enthusiastic author who “wanted a sharper decline” and sees one may accept without checking whether BC weights were the wrong edit class (Fig. 4b). Engaged evaluation would require the warrant (class/subclass rule) to unify with the actual code change. (Comparative inference)

---

## 5. Response axiom: why pooled compliance is fragile

Paper B’s public-opinion axioms clarify when survey-like averaging is valid.

> **Quote (Bisquert et al.):** *"Response Axiom: Individuals answer survey questions by averaging across the considerations that are immediately salient or accessible to them. It holds for quiescent and enthusiastic… However, it does not hold for unconcerned and engaged agents"*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility… with a success rate of 25-27% for the best models (Figure 5)."*

If planned Institute experts include both quiescent plot-scanners and engaged warrant-checkers, a single compliance rate mixes Response-axiom-valid and -invalid judges. Stratify first; then report per-profile rates. (Author-stated in B; Comparative inference for A)

---

## 6. Comparison table: acceptance as profile-conditioned

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Unit of success | Binary “Compliance with the comment” | \(evalarg(a,p)\in\{\oplus,-,.\}\) by profile \(p\) | Untyped yes/no vs typed acceptance (Comparative inference) |
| Cognitive route | Implicit author visual judgment | S1 (\(AT\)) vs S2 (KB + contextual entailment) | Same edit can flip by route (Author-stated in B) |
| Engagement | Not measured | unc / ent / qui / eng from \(i,\lambda\) | Stratify Smorodintsev studies (Speculative extension) |
| Ambiguous outcomes | Formal vs questionable reshape (Fig. 4c) | S1 accept / S2 reject (DUR-DUR) | Ambiguity ≈ profile mismatch (Comparative inference) |
| Future evaluator | LLM-expert-evaluator, confidence scores | Warrant check + premise \(\mid\!\sim_2\) | Evaluator needs engaged criteria, not S1 cues (Comparative inference) |
| Aggregation | Pooled % over ~20 launches | Response axiom only for qui/ent | Do not average across profiles (Author-stated in B) |

---

## 7. LLM-expert-evaluator needs an engagement mode

Paper A’s Future work proposes an automated compliance judge without specifying shallow vs deep checking.

> **Quote (Gindullina et al.):** *"An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement."*

> **Quote (Bisquert et al.):** *"a more engaged agent will use a deeper reasoning (S2) while a quiescent agent will only use associations (S1)."*

If the evaluator only matches comment keywords to curve shape (S1), it will inflate success on Fig. 4c-type cases. An engaged-mode evaluator must check: (i) classified subclass warrant exists in the rule base; (ii) generated loss unifies with that warrant; (iii) forecast change is a consequence of the warrant, not a side effect of BC weight edits. (Speculative extension)

---

## 8. Conversational Agent as engagement probe

Paper A’s Agent already filters concreteness/certainty/objectivity—but does not elicit interest or knowledge depth.

> **Quote (Gindullina et al.):** *"The conversational agent’s functionality includes validating expert comments for compliance with the following criteria: concreteness… certainty… and objectivity"*

> **Quote (Bisquert et al.):** *"In the ELM model… the determination of the \"route\" for persuasion is made thanks to two main factors: the interest in processing the message and the ability… to process it."*

A cheap extension: after comment approval, ask two Likert items (interest in this subclass; self-rated familiarity with the loss terms involved) as proxies for \(i\) and \(|AT|\) vs \(\lambda\). That yields profile strata without implementing full \(AT\)/KB. (Speculative extension)

---

## 9. Incorporation depth: what sticks after acceptance

Paper B’s update table shows persuasion depth depends on profile: engaged agents add rules; quiescent/enthusiastic mostly push associations and flags.

> **Quote (Bisquert et al.):** *"Accordingly to public opinion axioms, the more cognition was involved in its evaluation, the more persuasive content will take root in the mind of the agent."*

> **Quote (Bisquert et al.):** *"for eng … addrule(\(\kappa,K_h\)) … setflag(\(\kappa,c,f\))"* (Table 1, accepted case)

> **Quote (Gindullina et al.):** *"The expert analyses the updated forecast and judges its quality."* / *"Successful result… Unsuccessful… Ambiguous"*

If Institute experts only mark binary success, Paper A learns nothing about whether the *warrant* entered their KB (reusable expertise) or only a transient S1 association with the plot. Logging post-acceptance “would you reuse this edit class?” separates shallow compliance from engaged incorporation. (Comparative inference)

---

## Direction 1. Stratify Institute user studies by engagement profile

**Pipeline stage:** evaluation / planned Smorodintsev validation.  
**Mechanism:** Pre-register unconcerned / enthusiastic / quiescent / engaged proxies (interest + familiarity); report compliance, ambiguous-rate, and “warrant-check pass” separately per stratum; do not publish a single pooled 25–27%-style headline.  
**Failure modes addressed:** subjective primary metric; S1-accept / S2-reject ambiguity (Fig. 4c); Response-axiom violations when pooling.  
**Measurable acceptance:** intra-profile agreement (κ) higher than cross-profile; engaged stratum correlates better with independent warrant audit. (Speculative extension)

---

## Direction 2. Dual-mode LLM-expert-evaluator (qui vs eng)

**Pipeline stage:** Future work multi-agent evaluator.  
**Mechanism:** Quiescent mode = shape/timing cue match; engaged mode = subclass warrant unification + premise consistency with Table A.2 + contrastive foil. Trigger regeneration only when engaged mode fails, even if quiescent mode passes.  
**Failure modes addressed:** random BC edits that “look changed”; ambiguous formal satisfaction; evaluator that merely echoes author S1. (Speculative extension)

---

Paper B is not about PINNs; it is about *whose* acceptance counts. Dual-process profiles explain why Expert-Guided PINN’s compliance metric is unstable across judges and why a future evaluator without engagement modes will reproduce the same subjectivity under automation.

---

## Manuscript placement

- **§2.4 + Smorodintsev validation plan:** stratify judges by engagement profile (cluster **8**).
- **Future work LLM-evaluator:** dual-mode qui vs eng (cluster **3**).
- **Limitations:** pooled 25–27% mixes Response-axiom regimes.

## What not to transfer

Paper B’s formal S1/S2 machinery and DUR-DUR toy arguments need not ship. Transfer **engagement strata + dual acceptance modes**—not a full cognitive architecture. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Intra-profile κ on compliance exceeds cross-profile κ; engaged stratum aligns better with independent warrant audit.

**Protocol.** Pre-register four profile proxies (interest × familiarity); same 20 forecasts rated by stratified Institute annotators; warrant checklist separate.

**Metric.** κ within/between; correlation(engaged, warrant-pass). Expect pooled headline unstable. (Speculative extension)

## Related essays in this series

- [`03_tonda_2013_bnsl_interaction.md`](03_tonda_2013_bnsl_interaction.md) — real-expert study design.
- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — warrant = contrastive cause.
- [`07_walton_2010_dialogue_explanation.md`](07_walton_2010_dialogue_explanation.md) — exam as S2 probe.
- Bridge: [`../dinara_analysis/15_ouyang_2022_instructgpt.md`](../dinara_analysis/15_ouyang_2022_instructgpt.md) — preference by profile.


## Conclusion

Paper B supplies the missing cognitive typing for Paper A’s subjective primary metric: acceptance of an LLM loss edit depends on S1 vs S2 and on engagement profile. Quiescent judges can ratify Fig. 4c-style ambiguities that engaged warrant checks should reject; pooled compliance rates therefore mix incompatible Response-axiom regimes. Expert-Guided PINN should stratify Smorodintsev user studies by profile and build dual-mode evaluators—S1 cue match is not a substitute for S2 warrant validation. Until then, “25–27% compliance” remains an untyped average over cognitively distinct acceptance events.

