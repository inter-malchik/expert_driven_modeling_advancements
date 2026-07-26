> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


#### comparison with kreikemeyer_2025

Paper A (Gindullina et al., "Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models") is an applied study: it builds an Expert-Guided PINN agent pipeline in which an expert comment passes through a dialogue agent and a hierarchical classifier, then is handed to an LLM that is expected to complete the PINN loss-function code. To assess "how model scale affects the quality of interpretation," the authors compare three publicly available models that differ practically only in parameter count — meta-llama/Llama-3.1-8B-Instruct (8B), meta-llama/Llama-3.3-70B-Instruct (70B), and deepseek-ai/DeepSeek-V3.1 (671B/37B active) — using them out of the box, without any task-specific fine-tuning. The results are highly uneven: the smallest model fails on nearly every metric (50% non-compilable code, 6% "compliance with the comment"), and the experiment itself ("three models with different parameter sizes were selected") embeds an implicit hypothesis that parameter scale is the main (and essentially the only tested) lever for code-generation quality.

Paper B (Kreikemeyer et al., "Using (Not-so) Large Language Models to Generate Simulation Models in a Formal DSL: A Study on Reaction Networks") directly tests that hypothesis on a structurally similar task — translating an informal textual description into a formal DSL — except not "PINN loss penalties" but chemical (kinetic) reaction networks (CRN). The authors explicitly formulate a thesis that reads as a counterargument to Paper A's implicit assumption: *"We argue that a combination of fine-tuning, few-shot prompting, and other techniques allow the use of much smaller, open-weight LLMs for the translation task, requiring only a fraction of the resources and providing full control over reproducibility"*. The open 7-billion-parameter model Mistral-7B-Instruct-v0.3, fine-tuned via LoRA on a synthetic corpus and with optional grammar-constrained decoding, recovers the reference model in 84.5% of cases — "remarkably close" to 99% for GPT-4o, "given orders-of-magnitude parameter difference". That is almost the same parameter range as the failed Llama-3.1-8B in Paper A, but with a fundamentally different outcome.

Below we show that the three levers Paper B applies to a small model — task-specific fine-tuning (LoRA), few-shot examples from a curated corpus, and output constrained by a formal grammar (grammar-constrained decoding) — are not applied at all in Paper A: there the small model is used exactly as bluntly as the large one, differing only in parameter count. This does not overturn Paper A's finding (the large model still wins), but it reclassifies the Llama-3.1-8B catastrophe from a "fundamental limit of scale" into an "artifact of experimental design in which the small model was given none of the three compensating tools." It is also worth comparing the two synthetic-data generators (DeepSeek-generated expert comments in A and the reaction-description generator in B) and Paper B's small user study as a template for Paper A's announced but not yet implemented validation on real experts.

---

## 1. The same dependent variable, different independents

Both papers solve formally the same task: translating free text into code/structure governed by a narrow formal target language. In Paper A this is Python code that adds penalty terms to $L = L_{data} + L_{IC} + L_{ODE}$; in Paper B it is a CRN model in EBNF grammar. Both author groups also fix a model of roughly "7–8 billion parameters" as the lower bound of the experiment.

But in Paper A the only variable varied between runs is pure model scale:

> **Quote (Gindullina et al.):** *"To empirically evaluate the impact of model scale on the quality of expert comment interpretation and the generation of correct loss functions, three models with different parameter sizes were selected"*.

In Paper B, by contrast, scale is only one of eight tested method combinations (LoRA vs. no LoRA × few-shot vs. no few-shot × GCD vs. no GCD), and this fork is the paper's main contribution:

> **Quote (Kreikemeyer et al.):** *"Several papers already discuss using LLMs for the model translation task... However, they rely solely on the generalization capabilities of very large models... they leave the use of more advanced training, such as parameter-efficient fine-tuning and other techniques... unexplored"*.

In other words, Paper B was written as a direct response to the pattern Paper A reproduces: test a small model only as-is and infer its ceiling from that.

---

## 2. Soft rules versus hard grammar

In Paper A, constraints on generation are textual instructions inside the prompt, not a mechanism that physically prevents the model from exceeding them. Table A.2 states them in natural language: *"Add penalty to term2"*, *"Modification of other function components is prohibited"*. Checking happens only after the fact:

> **Quote (Gindullina et al.):** *"1. Syntactic analysis – checking the code's compilability using the Python interpreter. 2. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated"*.

This is an expensive loop: *"this mechanism requires additional queries to the LLMs, which significantly increases computational costs and time, especially for models with an initially low success rate"* — meaning correction costs the most precisely for the weak model (Llama-3.1-8B).

Paper B, instead of soft verbal rules, specifies a formal grammar of the target language (fragment, ISO EBNF):

```ebnf
root = "```\n" reaction, {reaction}, "```\n";
reaction = [species], " -> ", [species], " @ ", rate, ";\n";
```

and applies grammar-constrained decoding (GCD), which physically prunes the token probability distribution to those that continue a valid grammar string:

> **Quote (Kreikemeyer et al.):** *"Even when fine-tuned, the language model might not reliably produce syntactically valid models. This can be enforced by constraining the selection of tokens in the output sequence to conform to a specific format, e.g., a formal grammar"*.

The difference is fundamental: in A syntactic correctness is what is *checked after generation* and asked to be redone; in B it is what *cannot be violated during* generation.

---

## 3. Three levers absent for Llama-3.1-8B in Paper A

| Criterion | Paper A — Llama-3.1-8B-Instruct | Paper B — Mistral-7B-Instruct-v0.3 |
|:--- |:--- |:--- |
| Parameters | 8B | 7.3B |
| Task-specific fine-tuning | none — out-of-the-box only | LoRA ($r=8$, $\alpha=8$, dropout $=0.3$) on 800 synthetic pairs |
| Few-shot from target corpus | none — prompt contains only context, rules, and source code | 30 curated examples (few-shot variant); 0 for fine-tuned variant |
| Formal grammar output constraint | none — post-hoc compilation + iterative correction only | optional grammar-constrained decoding (`transformers-cfg`) |
| Final result for small model | 50% non-compilable code, 20% runs "terminated with error", 6% compliance with the comment | 84.5% ± 0% exact matches with reference model (temp = 0) |
| Larger-scale reference model | DeepSeek-V3.1 (671B/37B active): 27% compliance | GPT-4o: 99% ± 0% |

This is exactly the combination Paper B's thesis formulates: *"fine-tuning, few-shot prompting, and other techniques"* versus "just take a larger model." None of Paper B's three tools is applied to Llama-3.1-8B in Paper A — it receives the same prompt as the 70B and 671B models, differing only in weight count.

---

## 4. Kreikemeyer's own "raw" Llama-8B as a control point

Especially telling is that Paper B itself includes a model in the same size class as Gindullina's failed Llama-3.1-8B — Llama-8B-v3.1, also tested few-shot only, without LoRA. But with well-chosen 20 examples and a system prompt it achieves a completely different result:

> **Quote (Kreikemeyer et al.):** *"It is evident, that the orders-of-magnitude larger LLM can still outperform the specialized, smaller LLM by just providing examples. However, the 1B larger Llama8B_v3.1, with few-shot prompting, can not outperform the specialized Mistral7B_v0.3"*.

Per Table 1 its accuracy is 72.5% ± 0%, meaning that in its own test protocol an "8B"-class model is by no means hopeless — it trails the fine-tuned 7B model (84.5%) and GPT-4o (99%), but performs an order of magnitude better than Paper A's 6% failure. The difference is not model architecture (the Llama family appears in both papers) but that Paper B's prompt contains structured examples of "text → correct formal model," whereas Paper A's prompt contains only rules and source code without a single example of a correct transformation. This is direct empirical support for the assignment thesis: the 8B-model catastrophe in Paper A is less a limit of scale than the absence of structural supports.

---

## 5. Output constraint is not a universal recipe: Paper B's honest caveat

It is important not to oversimplify the conclusion: Paper B itself shows that GCD does not always help. On an already fine-tuned model, adding grammar-constrained decoding did not improve but slightly reduced accuracy:

> **Quote (Kreikemeyer et al.):** *"When using constrained decoding, the results are similar, but often this technique seems to slightly decrease the accuracy in our case. We attribute this to the fact that, already with the fine-tuning or LoRA, the LLM learns to accurately adhere to the grammar as implicitly defined by the training data"*.

But the authors themselves note that this follows from the simplicity of their CRN grammar, not a general property of GCD:

> **Quote (Kreikemeyer et al.):** *"This result might be different in cases where the grammar is more complex and not easily picked up from examples"* — and in the conclusion: *"We have seen that the simple DSL we defined is relatively easy to train for and GCD is not beneficial. Still, the latter could become more relevant for more expressive modeling languages"*.

Paper A's target language is not a string of a dozen terminals but arbitrary Python code with mathematical expressions, variables, and function calls — precisely the case of a "more complex grammar" for which, by Paper B authors' own forecast, GCD may yield greater benefit than in their own experiment.

---

## 6. Two synthetic-data generators, two degrees of caution

Both papers produce a synthetic text corpus to train a separate system component. In Paper A these are 2000 "expert" comments for fine-tuning the hierarchical BERT+ML classifier:

> **Quote (Gindullina et al.):** *"The model, based on "bert-base-cased", was fine-tuned on a synthetic dataset of 2000 expert-like commentaries. This dataset was generated by DeepSeek-V3.1 using real expert comments to ensure representativeness"*.

The mention of "real expert comments to ensure representativeness" is the only stated quality-control measure for the synthetic data; the paper reports no quantitative check of distributional alignment. Paper B's synthetic generator is built from explicitly listed "ingredients" (370 manually filtered sentence templates, species lists from UniProt/economics/epidemiological states, connectors) and, more importantly, training and test sets are separated by vocabulary, not only by random sampling:

> **Quote (Kreikemeyer et al.):** *"To avoid a model performing well when overfitting the training data, we base the training and testing samples on disjoint sets of ingredients (e.g., species names)"*.

Paper A reports nothing comparable (separating the training and test portions of the 2000 comments by non-overlapping "ingredients" rather than a simple random split). This is a concrete, cheaply transferable practice.

At the same time both author groups equally acknowledge the limit of such a strategy. Paper A — in Limitations:

> **Quote (Gindullina et al.):** *"The hierarchical classifier was trained and evaluated on synthetic data, which may not capture the full linguistic variability of real expert feedback. Large-scale validation on authentic expert comments is planned for future work at the Smorodintsev Research Institute for Influenza"*.

Paper B — in Discussion, regarding its validation set consisting literally of three manually written examples: *"The validation data consists of three manually written samples"*, — and in the conclusion: *"Most importantly, as evident from our user study, interaction needs to be included"*. Thus in both papers the weakest methodological link — the transition from synthetic data to real users — remains unresolved, but Paper B has already taken a small but real step toward closing it (see next section).

---

## 7. Five live experts as the step Paper A lacks

Paper B concludes evaluation with a small user study — exactly the type of validation Paper A only announces as future work:

> **Quote (Kreikemeyer et al.):** *"We concluded the evaluation with a small-scale user study by interviewing n = 5 scientists with varying experience in developing simulation models... Each supervised session lasted about an hour"*.

Notably, one identified failure occurred precisely in epidemiology — the same domain as Dinara Gindullina's work:

> **Quote (Kreikemeyer et al.):** *"This became particularly evident in the domain of epidemiology, where the basic SIR reactions ($S + I \to 2I; I \to R$) could not be derived from a natural language description"*.

This does not contradict the assignment thesis but refines it: even a successfully fine-tuned small model errs not from lack of parameters but from a gap in training concepts (the SIR pattern was simply not explicitly included in the synthetic generator) — a problem that is reproducible and fixable by adding the concept to the data, not by enlarging the model. The study format — before/after questionnaire, sessions on real rather than synthetic formulations, breakdown of specific failures by type — is a ready, already tested protocol Paper A could directly borrow for the promised validation at the Smorodintsev Research Institute for Influenza.

---

## 8. Reference-alignment metric: similarity to source versus match to ground truth

There is one more methodological divergence worth stating explicitly. Paper A, besides the subjective expert rating "Compliance with the comment," uses the automatic TSED metric:

> **Quote (Gindullina et al.):** *"To quantify the degree of correspondence between the original loss function and its modified versions generated by language models, the TSED (Tree Similarity of Edit Distance) metric Song et al. (2024) was applied"*.

But TSED measures not correctness of modification but its *structural closeness to the original, unmodified code* — essentially "how much the code changed at all," not "whether it changed as the expert requested." That is why Paper A's main success criterion ("Compliance with the comment") remains qualitative and subjective — as acknowledged directly in Limitations: *"The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results"*.

Paper B's metric is structured differently: it does not compare the output to the original (unmodified) text but compares it directly to a known reference:

> **Quote (Kreikemeyer et al.):** *"In our case, correct means aligning with the ground truth answer from our test data. We test this alignment by extracting the reactions from the model output and checking whether, for each reaction in the ground truth, there is a corresponding reaction in the model's answer"*.

This is possible only because Paper B has a single correct CRN model for each test example, produced by the same generator as the description text. Paper A has no analogous "gold standard": Table A.2 rules state *which* terms may be changed but do not specify the concrete numerical/structural form of the correct modification for a given comment. This is exactly the gap that formalization of modification templates, already sketched in Paper A's Future Work, would fill — and it would allow replacing subjective "Compliance with the comment" with automatic reference matching along the lines of Paper B Section 5.4.1.

---

## Directions for Paper A

**Direction 1. LoRA fine-tuning of Llama-3.1-8B on a synthetic corpus (comment → correct code).** By analogy with Paper B Sections 5.2 and 5.6, assemble a corpus of pairs "(comment class/subclass, original loss function, reference modification)" generated, for example, by DeepSeek-V3.1 or Llama-3.3-70B-Instruct (models with best baseline compliance), and run a grid search over LoRA hyperparameters ($r \in \{4,8,16\}$, $\alpha \in \{8,16\}$, dropout $\in \{0.3,0.5,0.7\}$, 3 repeats per seed) for Llama-3.1-8B — instead of using it only zero/few-shot as now.

**Direction 2. Formal EBNF/GBNF grammar for a loss-function "mini-DSL" + grammar-constrained decoding.** Formalize the admissible modification space from Table A.2 (term1…term4, allowed penalty-addition operations, ranges of numerical constants) as an explicit grammar and connect `transformers-cfg` (as in Paper B Section 4.5) instead of the "generate → compile → ask to fix" loop — this should reduce the share of non-compilable code for weak models without extra LLM calls, and by Paper B's own forecast (Sections 5.7/6) GCD gain grows with grammar complexity — and Python code is inherently more complex than Kreikemeyer's CRN grammar.

**Direction 3. Fully local pipeline instead of dependence on DeepSeek-V3.1.** Paper B trained and ran its models on a single consumer/semi-professional GPU (*"a single NVIDIA RTX A5000 graphics processing unit (GPU) with 24,564 MiB³ of graphics memory"*), positioning the result as a *"self-hostable, compute-efficient, and memory efficient alternative"* to commercial giants. For Gindullina's team, working on Smorodintsev Research Institute for Influenza data, this is a direct path to replace calls to 671B DeepSeek-V3.1 via an external API with a fine-tuned 7–8B model run entirely on the institute's local server — without sending medically sensitive expert comments outside.

**Direction 4. Rigorous statistics instead of point estimates on 20 runs.** Transfer to Paper A's Figure 3/5 data (20 runs per model at temperature = 1.0) the stochastic convergence methodology from Paper B Section 5.4.2 — repeat runs until the confidence interval of the mean metric converges to a specified half-width ($d_n = 0.02$ at confidence level 0.99) — and also separate training/test portions of the 2000-comment synthetic corpus by non-overlapping "ingredients" (class/subclass types, lexicon), as in Paper B Section 5.2, not only by random sampling.

**Direction 5. User study following the Kreikemeyer et al. protocol.** Use the structure of Paper B Section 5.10 (expectations questionnaire before/after, session "simple task first, then complex," ~one hour supervised, breakdown of specific failure types) as a ready template for Paper A's announced but not yet performed validation on authentic, not synthetic, expert comments at the Smorodintsev Research Institute — including explicit testing of whether the pattern "the model gets confused when wording deviates from the literal form of training examples," noted in Paper B Section 5.10, reproduces with real epidemiologists.

**Direction 6. Objective reference-alignment metric instead of subjective "Compliance with the comment".** Develop Paper A Future Work's "class-subclass-specific modification templates" into concrete parameterized templates (as Paper B Section 4.1 formalizes the target CRN as a checkable structure), generate for each pair (class/subclass, synthetic comment) a single correct loss-function modification, and replace qualitative "Compliance with the comment" with automatic matching to that reference using Paper B Section 5.4.1 methodology — instead of TSED, which measures only degree of deviation from the original, not correctness of the new code.

---

## Summary

Paper B does not overturn Paper A's main quantitative conclusion — the large model still wins (99% vs. 84.5%, "orders-of-magnitude parameter difference"). But it provides a controlled, measured counterexample to the implicit assumption around which Paper A's experimental design is built: that with a fixed usage mode (zero/few-shot, no fine-tuning, no output constraint) differences in results are differences in model scale alone. A model almost the same size as Paper A's failed Llama-3.1-8B (6% compliance, 50% non-compilable code), in Paper B, given exactly three compensating tools — LoRA fine-tuning on a curated synthetic corpus, few-shot examples, and optional grammar-constrained decoding — nearly closes the gap with a model two orders of magnitude larger. For Paper A this means the smallest model's failure is not necessarily a verdict on the architecture or a "fundamental PINN limitation," as the authors cautiously suggest, but likely in substantial part an artifact of giving the small model none of the three levers already tried and quantitatively assessed in Paper B. Together with this, Paper B offers a concrete, already implementable path toward what Paper A's institutional context requires (medical data, potential operational deployment at the influenza research institute) — a self-hostable, compute-cheap small model instead of dependence on an external 671B-model API.
