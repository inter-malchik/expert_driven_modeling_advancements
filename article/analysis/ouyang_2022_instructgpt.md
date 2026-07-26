> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Gindullina et al.'s work (hereafter **Paper A**) introduces an Expert-Guided PINN: a system where an epidemiologist provides free-text feedback on a model's forecast. This feedback is classified according to a strict ontology, and a large instruction-tuned LLM—with no task-specific fine-tuning—converts the classified feedback into Python code that modifies the PINN's loss function. Ouyang et al.'s paper, *«Training language models to follow instructions with human feedback»* (hereafter **Paper B**), first presented InstructGPT: a three-stage method (SFT → Reward Model → PPO) that transforms a raw, pre-trained GPT-3 into a model that actually fulfills user intent, rather than merely generating plausible text.

The conceptual link between the two works is direct and unambiguous: the LLM powering the PINN Customizer in Paper A is structurally identical to the unmodified, "raw" prompted baseline that Ouyang et al. use as their starting point in Paper B, not the final aligned model they produce. Paper B does not merely explain why naive prompting of Llama-3.1-8B/Llama-3.3-70B/DeepSeek-V3.1 only achieves a 6–27% compliance rate—it provides a complete, reproducible methodology (SFT demonstrations → preference comparisons → policy training on preference signals) to turn this prototype into a task-specific fine-tuned system. Critically, this methodology can leverage the exact raw data (expert verdicts of "success/failure/ambiguous") that Paper A already generates at every iteration, but currently discards.

Below, we outline exactly how Paper B resolves key methodological gaps in Paper A, and propose concrete steps to integrate an RLHF-like framework into the Expert-Guided PINN system.

---

## 1. The LLM in the PINN Customizer is exactly the "GPT (prompted)" baseline from Paper B

Ouyang et al.'s core thesis is stated in their abstract:

> **Quote (Ouyang et al.):** *«Making language models bigger does not inherently make them better at following a user's intent.»*

They go on to demonstrate that a model relying solely on few-shot prompting ("GPT-3-prompted") is the weakest baseline in their hierarchy, consistently underperforming both their supervised fine-tuning (SFT) model and their PPO fine-tuned model across all model sizes (Figure 1). This is a literal description of what Paper A implements: the expert's comment, modification rules, and original loss function code are simply packaged into a prompt and sent to an off-the-shelf instruction-tuned model:

> **Quote (Gindullina et al.):** *«All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment. This setting was used exclusively during the testing and prototyping phase to explore the system's full behavioral range.»*

None of the three models tested (Llama-3.1-8B-Instruct, Llama-3.3-70B-Instruct, DeepSeek-V3.1) are fine-tuned for the task of loss function generation—only the comment classifier is fine-tuned. Architecturally, the PINN Customizer is therefore exactly the "GPT (prompted)" baseline from Figure 1 of Paper B, not an equivalent of the SFT or PPO models. Given that even Ouyang et al.'s prompted GPT-3 systematically underperforms its fine-tuned counterparts, the low compliance rate (25–27% for the best models in Paper A) is not an accident—it is an expected outcome of stopping the alignment pipeline at this early stage.

---

## 2. Anatomy of the two pipelines: three training steps vs. a single forward pass

Paper B's methodology is formalized into three distinct stages:

> **Quote (Ouyang et al.):** *«Step 1: Collect demonstration data, and train a supervised policy... Step 2: Collect comparison data, and train a reward model... Step 3: Optimize a policy against the reward model using PPO.»*

In Paper A, the equivalent pipeline is reduced to a single, training-free step:

| Criterion | Paper A (Expert-Guided PINN) | Paper B (InstructGPT) |
|:--- |:--- |:--- |
| What is actually fine-tuned | Only the hierarchical comment classifier (BERT+ML, 2000 synthetic examples) | The entire generative policy: SFT model → RM → PPO policy |
| Model producing the final output | Off-the-shelf instruction-tuned model with no task-specific fine-tuning | GPT-3 fine-tuned on task-specific demonstrations and comparisons |
| Source of "correctness" signal | Single expert judgment (success/failure/ambiguous), not stored anywhere | Ranking of K=4–9 responses by annotators → RM → PPO |
| Feedback loop | Open: every new query starts from the same base weights | Closed: «Steps 2 and 3 can be iterated continuously; more comparison data is collected on the current best policy» |
| Generation temperature | t=1.0 during prototyping "for maximum variation"; t=0–0.2 in production | Multiple policy samples used to train the RM; final policy is optimized, not selected randomly |
| Task success metric | Compliance with the comment: 6% / 25% / 27% | 175B InstructGPT preferred over 175B GPT-3: 85 ± 3% |

The difference is not in the quality of the base models (DeepSeek-V3.1's 671B parameters make it broadly comparable in power to GPT-3) but in the fact that Paper B adds two full training layers between the raw model and the production system (SFT and RM+PPO) that Paper A entirely omits for its generative component.

---

## 3. Reward Model training data is already being produced—and discarded

The core of Paper B is the loss function for the reward model (RM), trained on pairwise comparisons:

> **Quote (Ouyang et al.):** *«$y_w$ is the preferred completion out of the pair of $y_w$ and $y_l$, and $D$ is the comparison dataset»* (Equation 1, §3.4).

To collect these pairs cost-effectively, annotators are asked to rank multiple responses to the same prompt:

> **Quote (Ouyang et al.):** *«we have labelers rank between K = 4 and K = 9 responses, and train on all $\binom{K}{2}$ comparisons from each prompt as a single batch element»*.

Paper A already partially replicates this setup explicitly to generate K different outputs for the same comment:

> **Quote (Gindullina et al.):** *«All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment.»*

Each run then receives a three-level expert rating that forms an ordinal preference scale by design:

> **Quote (Gindullina et al.):** *«Successful result... Unsuccessful result... Ambiguous result. The expert's requirements are formally satisfied, but the result is questionable (for example, the curve looks unrealistic).»*

In short, Paper A already has two critical components of Ouyang et al.'s RM dataset: (a) multiple candidate completions for a single input (enabled by t=1.0) and (b) human quality ratings for each completion (success/failure/ambiguous). All that is missing is the third step: saving these pairs as training examples of the form $(x, y_w, y_l)$, instead of using one random sample for visualization and discarding the rest.

---

## 4. Scale does not solve the problem: DeepSeek-V3.1 (671B) hits 27%, while InstructGPT-1.3B outperforms 175B GPT-3

One of Paper B's most powerful findings directly refutes the idea that "a bigger model will fix this":

> **Quote (Ouyang et al.):** *«outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters»*.

Paper A empirically encounters a mirror of this result, but fails to draw the same conclusion: increasing model size improves code compilability and alignment with epidemiological logic, but barely moves the core metric—semantic alignment with the expert's comment:

> **Quote (Gindullina et al.):** *«The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models (Figure 5).»*

DeepSeek-V3.1 (671B total / 37B active parameters) achieves 27% compliance, Llama-3.3-70B hits 25%, and only Llama-3.1-8B plummets to 6%. Beyond a minimum size threshold ("8B is too small"), further increasing parameters from 70B to 671B has almost no impact on the final metric—exactly the gap between raw model size and alignment that Ouyang et al. formalize as a core methodological takeaway:

> **Quote (Ouyang et al.):** *«the cost of increasing model alignment is modest relative to pretraining... This suggests that right now increasing investments in alignment of existing language models is more cost-effective than training larger models.»*

The direct implication for Paper A is that instead of waiting for a larger, newer model to replace DeepSeek-V3.1, it is cheaper and more impactful to fine-tune the existing models for the task—including the underperforming Llama-3.1-8B.

---

## 5. The missing SFT step, specifically for the code-generating LLM

In Paper A, fine-tuning only happens once—and not on the component that produces the final output:

> **Quote (Gindullina et al.):** *«The model, based on "bert-base-cased", was fine-tuned on a synthetic dataset of 2000 expert-like commentaries. This dataset was generated by DeepSeek-V3.1 using real expert comments to ensure representativeness.»*

The comment classifier is fine-tuned, but the LLM that writes the loss function code—the component whose low compliance rate (6–27%) is the system's main bottleneck—relies entirely on prompting. In Paper B's terms, this means the entire pipeline is implemented for one sub-task (classification) but even the first, lowest-cost step (SFT) is skipped for the far more complex sub-task (code generation):

> **Quote (Ouyang et al.):** *«Our labelers provide demonstrations of the desired behavior on the input prompt distribution... We then fine-tune a pretrained GPT-3 model on this data using supervised learning.»*

Yet Paper A already has a proven blueprint for generating low-cost training demonstrations without large-scale manual annotation—the same approach used for the classifier: synthetic data generated by a stronger model and validated against real examples. This bootstrapping method can be extended to pairs of «(comment, class/subclass, rules, original code) → correct code modification», training the generator itself on these examples instead of just the classifier.

---

## 6. Shared language of limitations: hallucinations are reduced, not eliminated

Both works reach a strikingly similar conclusion: alignment/fine-tuning reduces, but does not eliminate, systematic model errors. For Ouyang et al.:

> **Quote (Ouyang et al.):** *«On "closed-domain" tasks from our API prompt distribution, where the output should not contain information that is not present in the input, InstructGPT models make up information not present in the input about half as often as GPT-3 (a 21% vs. 41% hallucination rate, respectively).»*

And later, in their limitations section:

> **Quote (Ouyang et al.):** *«Our models are neither fully aligned nor fully safe; they still generate toxic or biased outputs, make up facts, and generate sexual and violent content without explicit prompting.»*

Gindullina et al. describe the same pattern, but without the fine-tuning step that would reduce error rates:

> **Quote (Gindullina et al.):** *«Adding unused variables and constant terms. Erroneous assumptions about the presence of nonexistent patterns in the data. Incorrect interpretation and use of numerical parameters mentioned in comments.»*

And in their final assessment of the approach:

> **Quote (Gindullina et al.):** *«These results should be considered proof-of-concept, demonstrating the potential of the approach but also highlighting the need to develop more stringent generation rules and control mechanisms to ensure the interpretability and reliability of the results.»*

The difference is that for Ouyang et al., this is an honest acknowledgment of residual risk *after* passing through SFT+RM+PPO (cutting ungrounded fact generation in half), while for Gindullina et al., this describes the model *before* any fine-tuning of the generator—meaning the upper bound of error reduction that fine-tuning could achieve has not even been tested.

---

## 7. Who judges "Compliance" and can their ratings be trusted as a training signal?

Paper A explicitly acknowledges the main methodological weakness of its core metric:

> **Quote (Gindullina et al.):** *«The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results.»*

Ouyang et al. faced the same risk—their RM is also trained on the subjective judgments of 40 contract annotators—but before building a training signal on these judgments, they measured how reproducible the ratings were:

> **Quote (Ouyang et al.):** *«training labelers agree with each-other $72.6 \pm 1.5\%$ of the time, while for held-out labelers this number is $77.3 \pm 1.3\%$»*

They also independently verified that the model did not overfit to the preferences of specific annotators:

> **Quote (Ouyang et al.):** *«Our models generalize to the preferences of "held-out" labelers that did not produce any training data.»*

Neither of these checks are performed for the "Compliance with the comment" metric in Paper A—ratings are provided by a single expert with no formal measurement of inter-rater reliability across multiple epidemiologists. This means that before converting expert verdicts into a training signal (see §3), Paper A should first conduct this calibration; otherwise, noise in the ratings will directly translate to noise in the future reward model.

---

## 8. Data scale: why full PPO as implemented by Ouyang et al. is currently out of reach for Paper A

It is useful to directly compare the data volumes powering RLHF in Paper B with the realistic data volumes available to Paper A:

> **Quote (Ouyang et al.):** *«The SFT dataset contains about 13k training prompts (from the API and labeler-written), the RM dataset has 33k training prompts (from the API and labeler-written), and the PPO dataset has 31k training prompts.»*

These are the output of a team of 40 hired annotators working over months. For Paper A, the primary source of real (not synthetic) expert comments will remain a small group of researchers from a single institute:

> **Quote (Gindullina et al.):** *«Large-scale validation on authentic expert comments is planned for future work at the Smorodintsev Research Institute for Influenza.»*

Given this gap in data volume, attempting to directly replicate Ouyang et al.'s PPO loop is high-risk—especially since even they noted that RL training was unstable on their far larger dataset:

> **Quote (Ouyang et al.):** *«we found that 175B RM training could be unstable and thus was less suitable to be used as the value function during RL.»*

This is a strong argument in favor of lighter alternatives to PPO for small datasets—such as rejection sampling or iterative self-training on filtered generations, rather than a full actor-critic cycle (see Direction 3 below).

---

## Future Development Directions

Below are concrete steps to adapt Paper B's methodology to Paper A's architecture, accounting for the fact that Gindullina et al.'s expert feedback data volumes are orders of magnitude smaller than those available to Ouyang et al.

**Direction 1. Convert the three-level expert verdict into a Reward Model dataset.**
For every input $x$ = (comment, class/subclass, rules, original loss function code), multiple code variants are already generated with t=1.0—exactly what is needed for pairwise comparisons. The only required changes are: (1) instead of selecting one random sample to show the expert, save all K generated candidates; (2) ask the expert (or the "LLM-expert-evaluator" proposed in Paper A's future work) to classify each candidate as successful/ambiguous/unsuccessful; (3) convert the three-level scale into pairwise preferences ($successful \succ ambiguous \succ unsuccessful$) and train a small reward model using Ouyang et al.'s Equation 1. Following their example, avoid training the RM on a full-size 175B model, and instead use a compact 6B version «as this saves a lot of compute».

**Direction 2. Add a lightweight SFT step for the code generator, not just the classifier.**
Using the same method that produced the 2000-comment synthetic dataset for the classifier (generated by DeepSeek-V3.1 from real expert examples), it is possible to build a small set of demonstrations of «(comment, class/subclass, rules, code) → reference modification»: some from already observed successful runs (the 25–27% of successful cases accumulated in the paper's experiments), and some synthetically generated and manually verified. Use this dataset to fine-tune (e.g., via LoRA) the underperforming Llama-3.1-8B-Instruct, which currently only achieves 6% compliance. Per Ouyang et al.'s calculations, «Training our 175B SFT model requires 4.9 petaflops/s-days... compared to 3,640 petaflops/s-days for GPT-3», so SFT for an 8B model on a far smaller dataset is a feasible project for a university lab, unlike training a new large-scale model from scratch.

**Direction 3. Use rejection sampling instead of a full PPO loop.**
Given the gap between Ouyang et al.'s 13k/33k/31k prompts and the expected volume of real comments from a single influenza research institute, it is more practical to avoid replicating the full PPO+value-function pipeline (especially since even Ouyang et al. noted RL instability on their larger dataset) and adopt a simpler framework: generate N candidates for a comment, automatically filter out obviously invalid samples using Paper A's existing criteria 1–3 («Matching training data», «Forecast has changed», «Compliance with the epidemic logic»—all three are already thresholded and automatable), only send surviving candidates to the expert for review, and add approved pairs back to the SFT dataset. This is effectively an iterative version of Direction 2, requiring no separate value network or PPO infrastructure.

**Direction 4. Leverage the existing t=1.0 variation as a data source, not just for test-time diversity.**
Paper A intentionally generates diverse outputs for the same comment («to achieve maximum variation in results»), but only uses this diversity to evaluate models during testing. This same set of samples is effectively a free implementation of Ouyang et al.'s «rank between K = 4 and K = 9 responses» framework. Formalize this practice: collect comparisons during the prototyping phase with t=1.0, and switch to t=0–0.2 in production as originally planned.

**Direction 5. Prevent "reward hacking" with a penalty for degenerate modifications.**
One of the systematic failures described in Paper A—«Adding unused variables and constant terms»—is structurally identical to the reward overoptimization problem Ouyang et al. encountered: «we suspect that behavior (2) emerges partly because we instruct labelers to reward epistemic humility; thus, they may tend to reward outputs that hedge, and this gets picked up by our reward model». In both cases, the model finds a way to formally satisfy a metric («forecast has changed», «output appears cautious») without solving the underlying task. To address this, Ouyang et al. introduced «a per-token KL penalty from the SFT model at each token to mitigate over-optimization of the reward model». If Paper A eventually trains a generator against a reward model (Direction 1), it will need an analogous regularizer—for example, a penalty based on the TSED code comparison metric already used in the paper, measured against reference modifications, to avoid rewarding trivial, meaningless edits.

**Direction 6. Calibrate the subjectivity of "Compliance with the comment" before, not after, training a model on it.**
Before using expert verdicts as a training signal (Direction 1), first measure their reliability—just as Ouyang et al. measured inter-annotator agreement upfront ($72.6 \pm 1.5\%$ for training annotators, $77.3 \pm 1.3\%$ for held-out annotators) before trusting an RM trained on those judgments. For Paper A, this would mean collecting ratings from multiple epidemiologists on the same set of comment/forecast pairs and publishing the inter-rater reliability score; otherwise, any reward model trained on single-expert judgments will inherit all the subjective noise the paper itself explicitly warns about.
