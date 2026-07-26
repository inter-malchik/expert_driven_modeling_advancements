> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., 2026) combines **frequentist-style** PINN fitting ($L_{data}$, MAE gates, ODE residuals) with **Bayesian-flavored** expert priors encoded as LLM-generated penalties. Paper B (Hanti Lin, 2024, *To Be a Frequentist or Bayesian?*) maps five positions on a spectrum — from radical frequentism to radical Bayesianism — and argues for **contextualist centrism**: likelihoodist / frequentist-Bayes hybrids depending on problem structure.

Paper B names what Paper A does implicitly and explains **bad-prior** failures in infinite-dimensional PINN weight spaces.

---

## 1. Centrism: expert penalty as prior, data term as likelihood

Lin's spectrum includes **Centrism (Frequentist Bayesianism)** — subjective priors disciplined by frequentist error control (Sect. on nonparametric Bayes).

Paper A's decomposition:

$$L = L_{data} + L_{IC} + L_{ODE} + L_{expert}$$

Paper A on semantic adaptation:

> **Quote (Gindullina):** *"To bridge this gap, we present an Expert-Guided PINN framework that enables the semantic adaptation of a Physics-Informed Neural Network's loss function based on unstructured expert comments."*

- $L_{data}$: fit observations — **likelihood / frequentist** pressure.
- $L_{expert}$: encodes comment — **subjective structural prior** on trajectories.
- Epidemic-logic checks + MAE thresholds: **frequentist filters** on posteriors-that-are-not-Bayesian.

| Component | Statistical role (Paper B lens) | Paper A |
|:--- |:--- |:--- |
| $L_{data}$ | Likelihood pressure | MAE on incidence |
| $L_{expert}$ | Prior / regularizer | LLM penalties |
| Compile + logic checks | Frequentist model check | Code Tester + criteria 3–4 |
| Comment compliance | Subjective success | 25–27% |

---

## 2. Bad priors in nonparametric PINN space

Lin (Freedman, Diaconis):

> **Quote (Lin):** *"a careless choice can easily lead to a bad prior Pr(·), bad in the frequentist sense that, even with an arbitrarily large sample size, the prior might still fail to have this frequentist desideratum: a high frequentist probability of only producing a small-to-zero posterior error."*

Paper A:

> **Quote (Gindullina):** *"modifications to the loss function may be effectively random rather than logically justified by epidemiological reasoning."*

LLM edits navigate **high-dimensional weight space**; a careless $L_{expert}$ is Lin's bad prior — Fig. 4b unbounded growth. Paper B predicts this without pinning blame only on “hallucination”. Template-bounded penalties = frequentist guard on prior family.

---

## 3. Contextualism and regime-specific modeling

Lin:

> **Quote (Lin):** *"I self-identify as a contextualist. And I believe that, although the right position varies systematically (rather than arbitrarily) with problem contexts, it is restricted to be moderate frequentism or centrism—that is, likelihoodist frequentism or frequentist Bayesianism."*

Paper A adapts loss per epidemic wave via local expert opinion instead of one static national model — **contextualist** statistical practice. Lin legitimizes mixing paradigms; Paper A is a case study, not a category error.

---

## 4. Bayesian model checking vs. ad hoc MAE thresholds

Lin discusses Rubin-style **Bayesian p-values** for checking whether the model fits data given posterior uncertainty.

Paper A uses MAE < 1100, MAE > 700 for change detection — crude frequentist heuristics. Paper B suggests replacing or augmenting with simulation-based checks on epidemic summaries (peak day, growth rate) when evaluating LLM-proposed $L_{expert}$.

---

## 5. Law of likelihood: separate data edits from prior edits

Lin decomposes evidential support vs. prior degree of belief (Law of Likelihood section).

Paper A's LLM often touches multiple loss terms at once. Lin's prescription: **Class 4** (peak/data shape) comments → $L_{data}$ weights only; **Class 2** (measures) → $L_{expert}$ / mechanism priors — reduces compensatory cancellation between likelihood and prior parts.

---

## 6. Moderate Bayesianism and Paper A's split-responsibility protocol

Lin on moderate Bayesians:

> **Quote (Lin):** *"Some (And Probably Most) Bayesians Also Recognize Frequentist Probabilities."*

Paper A's split protocol — conversational validation, expert class confirmation, expert accept/reject on plot — mirrors Lin's **dual standards**: subjective expert judgment disciplined by frequentist compile checks and MAE screens. Neither pure Bayes (full posterior on $L$) nor pure frequentism (fixed $L$) — contextualist centrism in Lin's terms.

---

## 7. Hallucination as prior pathology; templates as admissible prior class

Paper A:

> **Quote (Gindullina):** *"However, direct use of LLM is associated with the risk of hallucinations Cossio (2025) – the generation of incorrect or physically unjustified code, which requires the development of strict control mechanisms."*

Lin would classify hallucinated loss terms as **incoherent priors** — high posterior error even at infinite data. Paper A's planned class-subclass templates define an admissible prior family, analogous to objective Bayesians' search for uninformative yet coherent priors.

Paper A on numerical literalism:

> **Quote (Gindullina):** *"There is a systematic problem with interpreting numerical values in expert comments. In particular, the meta-llama/Llama-3.3-70B-Instruct model exhibits a tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

Literal numbers in $L_{expert}$ are priors without epidemiological likelihood support — Lin's bad-prior pathology in comment space.

| Criterion | Paper A | Paper B (Lin) | Takeaway |
|:--- |:--- |:--- |:--- |
| Paradigm | Expert prior + data fit + checks | Contextualist centrism | A is hybrid by design |
| Failure mode | Bad LLM prior (Fig. 4b) | Bad prior in nonparametric space | Same diagnosis |
| Mitigation | Templates, semantic checker | Frequentist guard on priors | Convergent roadmap |
| Evaluation | MAE + subjective compliance | Frequentist + Bayesian standards | A under-specifies checks |

---

## Proposed direction 1. Template-constrained prior family (PINN Customizer)

**Mechanism:** LLM picks from bounded kernel family; Lin's frequentist consistency on priors.

**Failure mode:** Bad priors in weight space (Fig. 4b).

---

## Proposed direction 2. Simulation-based check on epidemic functionals (evaluation)

**Mechanism:** Posterior/predictive checks on peak timing, not only MAE.

**Failure mode:** Ad hoc 700/1100 thresholds.

---

## Proposed direction 3. Split likelihood vs. prior edit tracks (classifier routing)

**Mechanism:** Route comment class to $L_{data}$ vs. $L_{expert}$ per Law of Likelihood.

**Failure mode:** Boundary penalty overriding ODE (Fig. 4c).

---

## Proposed direction 4. Two-agent frequentist–Bayesian dialogue (future multi-agent)

**Pipeline stage:** PINN Customizer + evaluation loop.

**Mechanism:** Agent A maximizes comment fit; Agent B enforces frequentist plausibility — Lin's centrism as architecture.

**Failure mode:** Single LLM optimizing both without guard.

---

## Conclusion

Lin's spectrum places Expert-Guided PINN in **frequentist Bayesian centrism under contextualism**: expert text supplies priors, PINN optimization supplies likelihood pressure, and epidemic sanity checks supply frequentist discipline. Paper B explains why unconstrained LLM priors fail in PINN's nonparametric landscape — and why Paper A's template and checker roadmap is statistically principled, not mere engineering caution. The next step is not choosing Bayes over frequentism but **routing each comment class** to the statistically appropriate update operator.
