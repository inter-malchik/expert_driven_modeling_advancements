> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., 2026) applies off-the-shelf instruct LLMs inside a PINN Customizer to translate epidemiologist comments into modified SIRD loss-function code. Paper B (Huang et al., 2024, *A Survey on Hallucination in Large Language Models*) systematizes why such pipelines fail: faithfulness hallucinations (instruction, context, and logical inconsistency), inference-time stochasticity, and mitigation via decoding constraints, multi-agent checking, and structured generation.

Paper A records symptoms — 6–27% *Compliance with the comment*, unused penalty terms, literal numeric insertion, 700-day outbreaks after boundary-condition edits — without a general LLM-hallucination vocabulary. Paper B supplies that vocabulary and catalogs evaluated countermeasures that map onto Paper A's own *Future work* (multi-agent evaluators, semantic checkers, modification templates). The pairing is strongest where Paper A's deterministic epidemiological target collides with Paper B's analysis of high-temperature, open-ended decoding.

---

## 1. Faithfulness hallucination taxonomy names Paper A's failure modes

Huang et al. redefine LLM hallucination for open-ended assistants:

> **Quote (Huang et al.):** *"faithfulness hallucination captures the divergence of generated content from user input or the lack of self-consistency within the generated content. This category is further subdivided into instruction inconsistency... context inconsistency... and logical inconsistency."*

Paper A's documented anomalies fit this grid. Literal insertion of numbers from comments is *instruction inconsistency* — the code follows tokens from the prompt without satisfying the epidemiological intent. The 700-day curve after weakening the zero boundary condition is *logical inconsistency*: compilable loss code whose implied dynamics contradict SIRD semantics.

> **Quote (Gindullina):** *"There is a systematic problem with interpreting numerical values in expert comments. In particular, the meta-llama/Llama-3.3-70B-Instruct model exhibits a tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

> **Quote (Gindullina):** *"the LLM meta-llama/Llama-3.3-70B-Instruct responded to this comment by reducing the influence of the zero boundary condition in the loss function... the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

Huang's survey does not replace epidemiological judgment; it classifies the LLM layer's error family.

---

## 2. Deterministic PINN targets vs. inference-time randomness

Paper A's mathematical core is a fixed ODE residual inside a composite loss. Yet prototyping used maximum decoding stochasticity:

> **Quote (Gindullina):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment. This setting was used exclusively during the testing and prototyping phase to explore the system's full behavioral range."*

Huang et al. tie high temperature directly to hallucination risk at inference:

> **Quote (Huang et al.):** *"An elevation in the sampling temperature results in a more uniform token probability distribution, increasing the likelihood of sampling tokens with lower frequencies from the tail of the distribution. Consequently, this heightened tendency to sample infrequently occurring tokens exacerbates the risk of hallucinations."*

Generating rigid Python that must preserve $L_{data} + L_{IC} + L_{ODE}$ structure while sampling tail tokens is structurally misaligned: Paper B predicts exactly the sporadic spurious variables and broken physics Paper A tables as systematic errors. Production plans (T=0–0.2) acknowledge the issue but are not evaluated in the reported compliance numbers.

---

## 3. Syntax-only checking cannot catch faithfulness hallucinations

Paper A's Code Tester stops at the interpreter:

> **Quote (Gindullina):** *"Syntactic analysis – checking the code's compilability using the Python interpreter. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated."*

Huang's scope is broader — hallucinations that pass surface checks:

> **Quote (Huang et al.):** *"faithfulness hallucination captures the divergence of generated content from user input or the lack of self-consistency within the generated content."*

A loss function can compile while violating modification rules in Appendix A or epidemiological logic — Paper A's *Compliance with the epidemic logic* and Fig. 4b document this gap. Huang's faithfulness detection families (fact-based, classifier-based, LLM-based judges) target precisely what compilation omits.

---

## 4. Temperature-driven multi-samples as latent self-consistency data

Paper A's T=1.0 setting yields multiple candidates per comment — the same design Huang cites for behavioral uncertainty estimation:

> **Quote (Huang et al.):** *"By sampling multiple responses from an LLM for the same prompt, Manakul et al. [205] detected hallucinations via evaluating the consistency among the factual statements."*

Paper A already elicits variation but uses one sample for training and expert review, discarding the rest:

> **Quote (Gindullina):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment."*

Expert verdicts (successful / unsuccessful / ambiguous) could rank candidates by cross-sample consistency before PINN retraining — Paper B's *Self-Consistency* branch applied to loss-code faithfulness rather than factual QA.

---

## 5. Multi-agent cross-examination as blueprint for Paper A's future evaluators

Paper A proposes specialized agents not yet implemented:

> **Quote (Gindullina):** *"A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment... An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations."*

Huang surveys an operational analogue:

> **Quote (Huang et al.):** *"Drawing inspiration from legal cross-examination practices, Cohen et al. [62] introduced the LMvLM approach. This strategy leverages an examiner LM to question an examinee LM, aiming to unveil inconsistencies of claims during multi-turn interaction."*

LMvLM is a **working instantiation** of the evaluator/checker split Paper A lists as future work. Inserting an examiner between codegen and PINN retraining would address the resource waste of training on faithfulness-hallucinated losses.

---

## 6. Context-aware decoding vs. ad hoc penalty prompting

Paper A constrains the LLM via prompt rules and plans class-specific *modification templates*. Huang reviews inference-time faithfulness decoding that reweights token distributions toward context — including context-aware decoding (CAD):

> **Quote (Huang et al.):** *"Shi et al. [275] proposed context-aware decoding (CAD), which modifies the model's original output distribution in a contrastive formulation. By amplifying the difference between output probabilities with and without context, CAD encourages the LLM to focus more on contextual information rather than over-rely on prior knowledge."*

In Paper A, "context" is the original loss code plus modification rules; CAD-style contrast could down-weight tokens that violate Table A.2 constraints before syntax check — a parametric alternative to longer prompt rule lists.

---

## 7. Plan-then-Generate for numerical expert cues

Paper A's future templates aim to map numbers to well-posed updates. Huang's attribution literature includes staged generation:

> **Quote (Huang et al.):** *"Fierro et al. [88] introduced the blueprint model for attribution, which conceptualizes text plans as a series of questions that serve as blueprints for generation process, dictating both the content and the sequence of the output."*

> **Quote (Gindullina):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

A mandatory plan step ("peak shift $\Delta t$ → penalty on $I(t)$ phase") before code emission directly targets literal *Constant Value*-style mis-binding documented in Paper A.

| Criterion | Paper A (Gindullina et al.) | Paper B (Huang et al.) | Takeaway |
|:--- |:--- |:--- |:--- |
| Error framing | Empirical symptom list | Faithfulness + factuality taxonomy | B names A's failures |
| Decoding | T=1.0 prototyping | Temperature ↔ hallucination risk | Stochastic codegen vs deterministic physics |
| Validation | Python compiler | Multi-method hallucination detection | Syntax ≠ epidemic faithfulness |
| Multi-agent | Proposed, not built | LMvLM, self-consistency surveyed | B blueprint for A's Future work |
| Numerics | Literal parameter insertion | Plan-then-Generate / attribution | Staged NL plan before code |

---

## 8. Subjective compliance and LLM-judge metrics

Paper A admits evaluator subjectivity on its primary metric:

> **Quote (Gindullina):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the 'Compliance with the comment' criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

Huang catalogs *LLM-Judge* evaluation on hallucination benchmarks. An automated judge comparing comment text to before/after incidence trajectories — with chain-of-thought justification — would scale testing beyond manual review while staying inside B's faithfulness-evaluation frame.

---

## Proposed direction 1. Context-aware decoding in PINN Customizer (inference)

**Pipeline stage:** PINN Customizer.

**Mechanism:** Contrastive decoding against modification-rule context; penalize tokens that break SIRD term constraints before compilation.

**Failure mode:** T=1.0 tail-token sampling producing spurious variables and unphysical penalties.

---

## Proposed direction 2. LMvLM semantic critic between codegen and retraining

**Pipeline stage:** After PINN Customizer, before PINN retraining loop.

**Mechanism:** Examiner LM cross-questions generator on conservation laws, boundary conditions, and rule-table compliance.

**Failure mode:** Compilable loss leading to 700-day outbreaks or epidemic-logic violations.

---

## Proposed direction 3. Plan-then-Generate for numeric comments

**Pipeline stage:** PINN Customizer (two-step).

**Mechanism:** Emit mathematical plan from comment + class; generate Python only from approved plan.

**Failure mode:** Literal numeric insertion without semantic adaptation.

---

## Proposed direction 4. Self-consistency selection at T=1.0

**Pipeline stage:** PINN Customizer execution.

**Mechanism:** Sample K loss functions; select cluster with highest inter-sample structural agreement (TSED) before expert review.

**Failure mode:** Single random sample from high-variance decoding.

---

## Proposed direction 5. LLM-judge for compliance scoring

**Pipeline stage:** Evaluation after retraining.

**Mechanism:** CoT judge scores comment–forecast alignment; low scores trigger regeneration.

**Failure mode:** Subjective *Compliance with the comment* limiting scale-up.

---

## Conclusion

Huang et al. do not alter Paper A's epidemiological conclusions; they supply the **missing LLM theory** for its empirical failure surface. Faithfulness hallucination (instruction and logical inconsistency), inference stochasticity at T=1.0, and surveyed mitigations (self-consistency, LMvLM, CAD, staged plans, LLM judges) align with problems and future directions Paper A already documents. Integrating these — especially semantic checking before PINN retraining — would move Expert-Guided PINN from symptom logging toward principled hallucination control.
