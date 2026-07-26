> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_21](https://doi.org/10.1007/978-3-319-23540-0_21)  
> **Source in `src/`:** [`../src/2015 Change in Abstract Bipolar Argumentation Systems.md`](../src/2015%20Change%20in%20Abstract%20Bipolar%20Argumentation%20Systems.md)

Gindullina et al. (hereafter **Paper A**) evaluate Expert-Guided PINN largely as single-shot comment → classify → rewrite → retrain loops (~20 launches, Fig. 5). The Conversational Agent gates concreteness/certainty/objectivity but does not log how successive expert moves *attack* or *support* prior warrants, nor how those moves change the set of acceptable loss edits. Multi-comment sessions—and Future work’s multi-agent evaluator/checker—therefore lack a dynamics vocabulary: each new comment is concatenated or restarted, not characterized as an update.

Cayrol and Lagasquie-Schiex (2015; hereafter **Paper B**) study **change in abstract bipolar argumentation systems (BAS)**: arguments linked by attacks *and* supports, with change operations that add an argument plus attack/support edges, then characterize whether the update is extensive, restrictive, or constant (including c-conservative, c-expansive, c-narrowing, c-altering) relative to preferred/stable/grounded extensions. Thesis: **log multi-turn Expert-Guided PINN dialogue as BAS updates (attack vs support), and score protocol fidelity by change class + unresolved commitments—not by flat prompt concatenation.**

---

## 1. Dialogues are dynamic BAS, not static prompts

Paper B’s editorial-board example is a multi-agent dialogue where each turn adds an argument and an interaction—exactly the structure Paper A’s Conversational Agent never records.

> **Quote (Cayrol & Lagasquie-Schiex):** *"in the course of a discussion or due to the acquisition of new pieces of information, an AS can undergo changes such as the addition of a new argument or the removal of an argument considered as illegal. This is of particular interest for dialogs in a multiagent system since it is unrealistic to consider that the argumentation system reflecting the dialog can be statically defined."*

> **Quote (Cayrol & Lagasquie-Schiex):** *"at each step of the dialog, the global argumentation system evolves (here, by the addition of an argument and an interaction)."*

> **Quote (Gindullina et al.):** *"The conversational agent’s functionality includes validating expert comments for compliance with the following criteria: concreteness (a single specific point), certainty (lack of vagueness), and objectivity (lack of emotional overtones)."*

Paper A validates *local form*; Paper B characterizes *global dynamics*. For Institute studies with revision turns (“also make the decline steeper”), the missing artifact is the evolving graph, not another concreteness check. (Comparative inference)

---

## 2. Support is not the absence of attack

Paper B’s BAS distinguishes \(R_{\mathrm{att}}\) and \(R_{\mathrm{sup}}\); deductive support generates mediated and supported attacks when flattened to a Dung AS.

> **Quote (Cayrol & Lagasquie-Schiex):** *"A bipolar argumentation system (BAS, for short) is a tuple \(\langle A, R_{\mathrm{att}}, R_{\mathrm{sup}}\rangle\) where \(A\) is a finite and non-empty set of arguments, \(R_{\mathrm{att}}\) is a binary relation over \(A\) called the attack relation and \(R_{\mathrm{sup}}\) is a binary relation over \(A\) called the support relation."*

> **Quote (Cayrol & Lagasquie-Schiex):** *"If \(bR_{\mathrm{sup}}c\) then the acceptance of \(b\) implies the acceptance of \(c\), and as a consequence the non-acceptance of \(c\) implies the non-acceptance of \(b\)."*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates."*

In Expert-Guided PINN terms: a second comment that *reinforces* the same subclass warrant (e.g., “yes, later peak *and* steeper post-peak drop”) should be logged as support between warrants—not as a second independent free rewrite that may invent a new illegal BC edit. Flattening support into complex attacks is the formal reason “helpful” follow-ups can still destabilize the accepted edit set. (Comparative inference)

---

## 3. Change characterizations as protocol metrics

Paper B’s Definition 8 taxonomy (extensive / restrictive / constant, with c-conservative through c-altering) is a ready-made label set for Agent ablations.

> **Quote (Cayrol & Lagasquie-Schiex):** *"The change from \(G\) to \(G'\) is extensive (resp. restrictive, constant) iff \(|\mathcal{E}| < |\mathcal{E}'|\) (resp. \(|\mathcal{E}| > |\mathcal{E}'|\), \(|\mathcal{E}| = |\mathcal{E}'|\)."*

> **Quote (Cayrol & Lagasquie-Schiex):** *"All agents always propose constant changes, since they want to take a decision without ambiguity."* … *"\(J_2\) chooses a c-altering change because she totally disagrees with this extension."*

> **Quote (Gindullina et al.):** *"Compliance with the comment… is the primary criterion… only 25% (Llama-70B) / 27% (DeepSeek) / 6% (Llama-8B)."*

Map “acceptable extension” to the current set of admissible named templates / warrants. A follow-up that should refine without abandoning the first successful edit is c-expansive or c-conservative; a contradiction that discards the first warrant is restrictive or c-altering. Flat concatenation cannot tell these apart—so protocol fidelity stays unmeasured beside the 25–27% headline. (Comparative inference)

---

## 4. Addition \(\oplus^z\) as the Conversational Agent write API

Paper B’s Definition 10 is the operation Expert-Guided PINN lacks: add argument \(z\) with attack and support incident edges.

> **Quote (Cayrol & Lagasquie-Schiex):** *"Adding \(z\) and \(I_z\) is a change operation, denoted by \(\oplus^z_{(I_a,I_s)}\), providing a new BAS…"*

> **Quote (Gindullina et al.):** *"Our future work will focus on… a multi-agent architecture with an “LLM-expert-evaluator” and an “LLM-loss-semantic-checker.”"*

Evaluator/checker agents should not only score a static rewrite; they should propose \(\oplus^z\) updates (new warrant + attack/support links) and refuse updates that are unexpectedly extensive when the expert intended a constant refinement. (Speculative extension grounded in Author-stated Future work)

---

## Directions for Expert-Guided PINN

**Direction 1. Log each accepted comment as an argument node** with edges: attack (conflicts prior warrant / IC) or support (reinforces prior warrant). (Speculative extension)

**Direction 2. Label each turn’s change class** (c-conservative / c-altering / …) before retrain; abort or depth-cap on unintended extensive jumps. (Speculative extension)

**Direction 3. Agent ablation metric:** unresolved-support count + change-class agreement with expert intent, beside Arioua-style \(NUS_X\) emptying. (Speculative extension)

**Failure modes addressed:** silent multi-comment concatenation; “helpful” follow-ups that rewrite BC illegally; unevaluated Conversational Agent dynamics. (Speculative extension)

---

## Manuscript placement

- **§2.1 Conversational Agent / Future work multi-agent:** BAS update log + change characterizations (cluster **8**).
- **§2.4 Evaluation:** protocol fidelity metric beside compliance 25–27%.
- **Limitations:** single-shot Fig. 5 design understates multi-turn dynamics.

## What not to transfer

Do not require full mediated/supported-attack closure solvers, preferred-extension enumeration, or journalistic toy dialogues as epidemic UX. Paper B has no LLM/PINN. Transfer **attack/support logging + extensive/restrictive/constant labels for multi-comment turns**—not a claim that SIRD forecasts are Dung extensions. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Logging multi-comment sessions as BAS updates and enforcing intended constant/c-expansive changes reduces unresolved warrants and illegal BC edits versus flat concatenation of comments into one Customizer prompt.

**Protocol.** Collect 15–20 two-turn comment pairs (reinforce vs contradict). Arms: (A) concatenate both into one prompt; (B) \(\oplus^z\) log with attack/support tags + refuse unintended extensive change before retrain. Cap dialogue depth (e.g., 3).

**Metric.** Change-class agreement with pre-registered intent; unused-term / Criterion-3 fails; NUS-style unresolved count; compliance vs Paper A 25–27% on turn-2 forecasts. Expect arm B fewer logic fails and higher protocol fidelity. (Speculative extension)

## Related essays in this series

- [`08_arioua_2015_explanatory_dialogues.md`](08_arioua_2015_explanatory_dialogues.md) — \(NUS_X\)/\(CS_E\) stores as measurable dialogue state.
- [`07_walton_2010_dialogue_explanation.md`](07_walton_2010_dialogue_explanation.md) — examination probes after each \(\oplus^z\).
- [`17_amgoud_2015_undercutting.md`](17_amgoud_2015_undercutting.md) — attack edges that block named rules.
- Bridge: [`../dinara_analysis/15_ouyang_2022_instructgpt.md`](../dinara_analysis/15_ouyang_2022_instructgpt.md) — preference/feedback as iterative updates.

## Conclusion

Cayrol and Lagasquie-Schiex supply what Expert-Guided PINN’s Conversational Agent lacks: a bipolar dynamics language in which each expert move adds an argument with attack or support, and each update is labeled extensive, restrictive, or constant. Paper A still scores mostly single-shot compliance and gates comment form. Until multi-turn sessions are logged as BAS updates and judged by change class and unresolved commitments, the unevaluated Agent and Future work’s multi-agent stack remain prompt plumbing rather than a characterized dialogue protocol.
