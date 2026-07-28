# lin_2024.md

Harvard Data Science Review • Issue 6.3, Summer 2024

# To Be a Frequentist or Bayesian? Five Positions in a Spectrum

**Hanti Lin**  
1

1University of California Davis, Davis, California, United States of America

**The MIT Press**  
Published on: Aug 01, 2024  
DOI: https://doi.org/10.1162/99608f92.9a53b923  
License: Creative Commons Attribution 4.0 International License (CC-BY 4.0)

---

**Column Editors’ Note:** The new column, *Meta Data Science*, presents short articles that discuss philosophical issues around the practice and theory of data science, ranging from ethical to epistemological and metaphysical questions. It aims to promote philosophy-minded data science and data-science-minded philosophy, and we welcome proposals for future columns on these issues. In this inaugural article, one of this column’s editors, Hanti Lin (University of California, Davis), revisits a traditional debate: frequentism versus Bayesianism in the foundations of statistics. Instead of two dichotomized views, he proposes a spectrum with five positions—from radical frequentism to radical Bayesianism with intermediate views in between—on the basis of the existing practice of statistical science.

**Keywords:** philosophy of statistics, frequentism, Bayesianism

## Introduction

I once received a simple test for whether I am a frequentist or Bayesian. A coin has just been tossed, but the outcome is hidden. What is the probability that it landed heads just now? According to the test, you are a Bayesian if your answer is “50%, because I am 50% sure that it landed heads, and equally sure that it didn’t.” And you are a frequentist if your answer is “the probability is unknown but equals either 1 or 0, depending on whether the coin actually landed heads or tails, because probabilities are frequencies of events.”

Unfortunately, this test is too simplistic to reveal the complexity underlying the seemingly binary question: “To be a frequentist or Bayesian?” There is actually a spectrum of potential answers, extending from radical frequentism to radical Bayesianism, with nuanced positions in between. Let me build up the spectrum one step at a time.

## The Ontological Question

It is misleading to ask what is the probability of a certain event, as it presupposes that there exists exactly one kind of probability. We should first ask an ontological question: What kinds of probabilities exist?

Radical Bayesians hold that there exists only one kind of probability, which is one’s degrees of belief—it resides in one’s mind (de Finetti, 1972, 1989/1931).

On the other hand, radical frequentists believe that there exists only one kind of probability, which is frequentist probability (Neyman & Pearson, 1933; Neyman, 1977). There is disagreement on what frequentist probability is supposed to be. One possibility is limiting frequency, such as the frequency of heads in a hypothetical population of infinitely many coin tosses (von Mises, 1957). Another possibility is propensity (Popper, 1959). For example, the propensity for a coin to land heads in a repeatable setup is measured by the real number that the frequency of heads would be disposed to approach were that setup repeated infinitely many times—even if that setup is actually repeated only once before the universe ends. It has been debated whether Popper (1959) is right in thinking that propensity serves the purposes of science better than limiting frequency does; for this controversy, see Gillies (2000, Chapters 5–7). Anyway, I will simply use “frequentist probability” as an umbrella term to set aside that controversy and to focus on its contrast with degrees of belief.

Some Bayesians actually allow both kinds of probabilities to coexist. Consider Bayes’ rule, a normative principle stating that, in light of new data \(D\), one’s posterior or updated degree of belief in a hypothesis \(H\) ought to be proportional to two factors:

### Bayes’ Rule

\[
(\text{posterior degree of belief in } H)
\propto
(\text{probability of observing data } D \text{ if } H \text{ is true})
\cdot
(\text{prior degree of belief in } H)
\]

*likelihood*

The factor labeled as likelihood is a probability—but what kind of probability? Radical Bayesians would say that the likelihood term is a (conditional) degree of belief, period. Moderate Bayesians would agree, but add that the value of this term is, or should be, equal to a frequentist probability: the frequentist probability of observing data \(D\) if hypothesis \(H\) is true. Therefore, moderate Bayesians think that frequentist probabilities coexist alongside degrees of belief.

So it is misleading to simply categorize Bayesians as those who equate probabilities with degrees of belief. Instead:

> *Some (And Probably Most) Bayesians Also Recognize Frequentist Probabilities.*

For example, Edwards et al. (1963) argued that the objectivity of Bayesian inference is rooted at least in likelihoods, maintaining that likelihoods reflect frequentist probabilities.

Now we have three positions aligned along an axis in Figure 1. There will be another axis, which introduces a second question.

### Figure 1. The first dimension.

- **Radical Frequentism**
- **Moderate Bayesianism**  
  *(Likelihoods Reflecting Frequentist Probabilities)*
- **Radical Bayesianism**

Axis labels:

- **Only Frequentist Probabilities**
- **Both**
- **Only Degrees of Belief**

**Ontological Question:** *What Kinds of Probabilities Exist?*

## The Epistemological Question

What standards should be used to assess inference procedures, or to evaluate anything on which inference procedures rely (such as models and experimental designs)? This is an epistemological question.

> *Distinguish between Ontological and Epistemological Questions.*

Frequentist standards are the evaluative standards that value avoidance of error (Neyman & Pearson, 1933; Neyman, 1977). Errors manifest in various forms. Some errors are all-or-nothing, such as rejecting a true hypothesis, or producing an interval that fails to cover the true value. Other errors are quantifiable, such as in a point estimate that deviates more or less from the true value. Sometimes our concern lies not in the error of choosing a false model, but specifically in the predictive error: the error in predictions under a curve-fitting model. Given these diverse types of errors, different standards may need to be considered when we transition between contexts. This diversity underscores why there exist numerous frequentist standards, tailored to specific problem contexts. Despite these variations, frequentist standards share the common goal of error avoidance: ideally, a good inference procedure has a low frequentist probability of error, or a high frequentist probability of only a small-to-zero error, or related metrics like small mean squared error (a weighted average of squared errors, with weights being frequentist probabilities).

Bayesians generally agree on a distinctive standard to assess inference procedures: an inference procedure should output degrees of belief, and do it in conformity or in good approximation to Bayes’ rule. Once this standard is in place, an inference procedure essentially begins with a prior distribution, which is then updated using Bayes’ rule to produce posterior beliefs. Prior distributions themselves can be assessed, too, which leads to a traditional divide within the Bayesian camp: subjectivists vs. objectivists. Subjective Bayesians advocate for a somewhat slack constraint on priors: “Be coherent” (such as satisfying the axioms of probability). In contrast, objective Bayesians advocate for a more stringent standard: “Be coherent and as uninformative as possible.” The quest for uninformative priors has led to several definitions; see Yang & Berger (1996) and Robert (2007, Section 3.5). These standards are distinctively Bayesian, governing degrees of belief without reference to frequentist probabilities of error, which distinguishes them from frequentist standards.

Radical frequentists insist that only frequentist standards be applied for assessment of inferential matters. In contrast, radical Bayesians champion Bayesian standards exclusively. Moderate Bayesians align with radical Bayesians on this epistemological issue, but adopt a more flexible ontological view: they allow the likelihoods in Bayes’ rule to reflect frequentist probabilities, as discussed earlier. So now we have three positions arranged in a two-dimensional space, as depicted in Figure 2.

### Figure 2. Adding a second dimension.

Horizontal axis: **Ontological Question — What Kinds of Probabilities Exist?**

- Only Frequentist Probabilities
- Both
- Only Degrees of Belief

Vertical axis: **Epistemological Question — How to Assess Inference Procedures and Related Things?**

- By Frequentist Standards Only
- Mixture?
- By Bayesian Standards Only

Positions shown:

- **Radical Frequentism**
- **Moderate Bayesianism** *(Likelihoods Reflecting Frequentist Probabilities)*
- **Radical Bayesianism**

## Centrism: Frequentist Bayes

A synthesis of frequentism and Bayesianism is possible. As will be detailed shortly, Bayesians can integrate frequentist standards to evaluate inference procedures as well as the models underlying those procedures. This centrist stance is embodied by *frequentist Bayesianism*, as depicted in Figure 3. Let me illustrate the idea with some examples.

### Figure 3. Centrism identified.

Horizontal axis: **Ontological Question — What Kinds of Probabilities Exist?**

- Only Frequentist Probabilities
- Both
- Only Degrees of Belief

Vertical axis: **Epistemological Question — How to Assess Inference Procedures and Related Things?**

- By Frequentist Standards Only
- ?
- By Frequentist and Bayesian Standards
- By Bayesian Standards Only

Positions shown:

- **Radical Frequentism**
- **Centrism** *(Frequentist Bayesianism)*
- **Moderate Bayesianism** *(Likelihoods Reflecting Frequentist Probabilities)*
- **Radical Bayesianism**

### Example 1: Nonparametric Bayes

Even Bayesians can value avoidance of error, much like frequentists. A Bayesian inference procedure is essentially a prior updated via Bayes’ rule, incorporating data to generate posterior beliefs. Like any inference method, Bayesian procedures can lead to errors. A small posterior error is manifest in a high posterior degree of belief concentrated around the (unknown) truth among considered hypotheses. So, to assess a Bayesian inference procedure, we can check its frequentist probability of producing a small-to-zero posterior error.

Imagine, for instance, that we wonder what is the true regression curve on the \(XY\)-plane and assume just that it is a smooth function, without requiring a specific parametric form. In such a case, we engage in nonparametric statistics, and a careless choice can easily lead to a bad prior \(\Pr(\cdot)\), bad in the frequentist sense that, even with an arbitrarily large sample size, the prior might still fail to have this frequentist desideratum: a high frequentist probability of only producing a small-to-zero posterior error (Freedman, 1963; Diaconis & Freedman, 1986). To rule out such a bad prior is to apply a frequentist standard. For more on how this idea is pursued in nonparametric statistics, see the review by Rousseau (2016).

The above is just one example showing that

> *Some Bayesians Make Assessments by Incorporating Frequentist Standards.*

Let me give two more examples.

### Example 2: Empirical Bayes

Another approach to assessing and selecting priors from a frequentist perspective is called *empirical Bayes*, pioneered by Robbins (1956). In certain problem contexts, some data are already available before a prior is chosen. If candidate priors are parametrized, say by \(\beta\), then choosing a prior becomes a matter of selecting a value for \(\beta\). Empirical Bayes utilizes the available data to pick a value for \(\beta\): data are fed into an inference procedure to yield a point estimate for \(\beta\)—using a procedure often recommended by frequentists (such as maximum likelihood or cross-validation), adhering to some frequentist standards. Once a value of \(\beta\) is thus determined, a prior is automatically chosen and ready to be updated by Bayes’ rule upon acquiring new data. For a textbook presentation of empirical Bayes as frequentist Bayes, see Gelman et al. (2014, Section 5.1).

### Example 3: Bayesian Model Checking

Inference procedures are typically based on models, which can themselves be subject to assessment. From a frequentist perspective, a model is often regarded as a space of hypotheses or parameter values, such as the set of all quadratic (regression) curves on the \(XY\)-plane. Such a model can be assessed in terms of how well it fits the available data; the crux is to have a measure of goodness-of-fit. A common approach involves using the available data to compute the so-called \(p\)-value of each hypothesis in the model. If the maximum \(p\)-value among those hypotheses is low, it indicates a poor fit of this model with the data—prompting concerns about this model’s adequacy. Disregarding the details and variations in the exact definition of \(p\)-values, suffice it to know that \(p\)-values are defined to have a tight connection to the frequentist probability of error (Fisher, 1925). Here is the idea:

> Consider any procedure that recommends rejecting an assessed model \(M\) when the maximum of the \(p\)-values from \(M\) is lower than a (small) threshold \(\alpha\). Then, whenever \(M\) is true, this procedure must have a (small) less-than-\(\alpha\) frequentist probability of erroneously rejecting \(M\).

You can freely replace “rejecting” by “worrying about” or any other con-attitudes; the tight connection remains.

This \(p\)-value assessment of models extends to the Bayesian setting, where a model consists of

1. a hypothesis space,
2. a prior distribution over that space.

Given data, we can calculate the \(p\)-value of each hypothesis in (i), as in the previous case. However, instead of taking the maximum, this time we compute a weighted average of those \(p\)-values—with the weights being posterior beliefs, obtained by updating the prior (ii) on the available data. This weighted average is known as a Bayesian \(p\)-value. If this value is low, it indicates a poor fit with data and we should start to worry about the assessed model. This is the main idea of Bayesian model checking (Rubin, 1984). In addition to using \(p\)-values, there is another frequentist method commonly used to assess Bayesian models: cross-validation. For a textbook presentation, see Gelman et al. (2014, Chapters 6 & 7).

The above presents only three of the many possible approaches to what may be called the centrist position: frequentist Bayesianism. Several more approaches are reviewed by Bayarri and Berger (2004). Frequentist Bayesians might disagree on the right approaches to adopt, though.

## A Not-So-Bayesian Component of Bayes’ Rule

Even when frequentists resist any synthesis with Bayesianism, they can still find something acceptable in Bayes’ rule. Here is the idea. Bayes’ rule can be formulated in an intuitively appealing form, asserting that the posterior probability of a hypothesis should be propositional to the evidential support that the hypothesis receives from data:

### Bayes Rule, in the Form of Evidential Support

\[
(\text{posterior degree of belief in } H)
\propto
(\text{degree to which data } D \text{ supports } H)
\cdot
(\text{prior degree of belief in } H)
\]

*evidential support*

As appealing as this rule may be, its practical application hinges on our ability to measure the strength of evidential support. Fortunately, this rule transforms into the familiar Bayes’ rule if evidential support is proportional to the likelihood, as asserted by the following principle (Hacking, 2016/1965; Royall, 1997):

### The Law of Likelihood

\[
(\text{degree to which data } D \text{ supports } H)
\propto
(\text{probability of observing data } D \text{ if } H \text{ is true})
\]

Therefore, Bayes’ rule in its usual form can be decomposed into two more fundamental principles: the evidential support form of Bayes’ rule and the law of likelihood.

This decomposition is crucial because the law of likelihood, as the second part, does not even refer to degrees of belief if likelihoods are construed as frequentist probabilities. Hence:

> *Some Frequentists Can Agree with Bayesians on Using Likelihood to Measure Evidential Support.*

While frequentists generally employ frequentist standards to assess inference procedures, some of them also incorporate additional standards based on the law of likelihood—they are *likelihoodist frequentists*. Let me give two examples below; more examples are detailed in Pawitan’s (2001) textbook.

### Example 1: Confidence-Likelihood Interval

Imagine a problem of interval estimation. A radical frequentist would only impose a frequentist standard, such as a 95% confidence level, which requires an at-least-95% frequentist probability of producing an interval that covers the true value. In contrast, a likelihoodist frequentist would impose an additional standard: any interval that excludes certain values should also exclude the values less supported by the data, that is, the values with lower likelihoods, assuming the law of likelihood (Barnard, 1967). This is a likelihoodist standard, which does not refer to frequentist error probability, but is based on the law of likelihood.

### Example 2: Later Pearson vs. Neyman-Pearson

Later Pearson (1947, 1962) is also a likelihoodist frequentist, who rejected the radical frequentist view inherent in the Neyman-Pearson school (1933) that he cofounded. In hypothesis testing, later Pearson would start by applying a likelihoodist standard: considering a candidate pool that comprises only the likelihood ratio tests. These tests are defined to reject the null hypothesis when the evidential support for the null hypothesis is too low compared with the evidential support for the alternative hypothesis—which means, under the law of likelihood, that the ratio of their likelihoods is too low. Later Pearson would then narrow down the candidate pool by appeal to frequentist standards (such as a low frequentist probability of type I or II error). Thus, frequentist and likelihoodist standards are both employed—they serve fundamental roles that complement each other in likelihoodist frequentism.

By way of contrast, radical frequentists in the Neyman-Pearson school would only employ frequentist standards—irrespective of whether those standards turn out to pick out likelihood ratio tests. So, even when radical and likelihoodist frequentists agree on using the same inference procedure in a specific problem context (such as a likelihood ratio test for hypothesis testing or the maximum likelihood method for point estimation), their reasons remain distinct.

Likelihoodist frequentism can be referred to as *moderate frequentism*, as portrayed in Figure 4. It departs from the radical frequentist end and moves toward the center by incorporating the law of likelihood, a principle shared with some Bayesians. To be sure, there is an ontological difference: as suggested by the first axis, moderate frequentists can only take likelihoods to be frequentist probabilities, whereas some Bayesians allow for both kinds of probabilities, viewing likelihoods as conditional degrees of belief that reflect frequentist probabilities (as discussed in the section entitled “The Ontological Question”). Despite that difference, there remains significant common ground. Those occupying the three intermediate positions (from moderate frequentism through centrism to moderate Bayesianism) all endorse the law of likelihood: that the strength of evidential support is objectively measured by likelihoods, which are, or at least reflect, frequentist probabilities.

### Figure 4. A little spectrum finished.

Horizontal axis: **Ontological Question — What Kinds of Probabilities Exist?**

- Only Frequentist Probabilities
- Both
- Only Degrees of Belief

Vertical axis: **Epistemological Question — How to Assess Inference Procedures and Related Things?**

- By Frequentist Standards Only
- By Frequentist and Likelihoodist Standards
- By Frequentist and Bayesian Standards
- By Bayesian Standards Only

Positions shown along the spectrum:

- **Radical Frequentism**
- **Moderate Frequentism** *(Likelihoodist Frequentism)*
- **Centrism** *(Frequentist Bayesianism)*
- **Moderate Bayesianism** *(Likelihoods Reflecting Frequentist Probabilities)*
- **Radical Bayesianism**

## Closing

The question “To be a frequentist or Bayesian?” is deceptively simple. I have tried to develop a little spectrum (Figure 4) to give a hint of the underlying complexity. Some elements actually involve deeper intricacies, inviting further exploration.

Firstly, the two questions asked, ontological and epistemological, have more potential answers than mentioned above. Additional candidates for types of probabilities include fiducial probability (Fisher, 1935; Zabell, 1992; Hannig et al., 2016) and logical probability (Carnap, 1945; Zabell, 2011); for more, see the survey by Hájek (2023). There are other pertinent questions to ask, such as: How should we quantify uncertainty? (Using frequentist confidence intervals, or Bayesian credible intervals, or simply degrees of belief, or something else?) A richer set of questions can reveal more nuanced positions in a higher dimensional spectrum.

The possibility of reinterpretation introduces another layer of complexity. Consider the empirical Bayes procedure discussed earlier, presented as an approach to frequentist Bayesianism. Interestingly, one does not need to adopt frequentist Bayesianism to employ the empirical Bayes procedure. For this procedure has two more possible interpretations. It can be reinterpreted as a formal procedure (for shrinkage estimation) in a way acceptable to radical frequentists. It can also be reinterpreted as a mere approximation to a purely Bayesian procedure, acceptable to moderate-to-radical Bayesians (for a comparison, see Petrone et al., 2014). More generally, a statistical method, theorem, or idea initially associated with one position might be reinterpreted to align with an alternative position.

There is one more layer of complexity. Given a spectrum of five or more positions, one might respond with an invariantist stance, asserting the universal validity of a single position. Alternatively, one might adopt a contextualist stance, maintaining that the right position depends on the problem context. Contextualists may further disagree on how the right position varies from one context to another.

The present article is only meant to paint a richer picture of possible views for our consideration. Important tasks lie ahead: discussing arguments for or against those views. But do you have to pick a view immediately? The division of labor can benefit everyone. Some people may excel at identifying important real-world inference problems, which others can study in order to refine existing inference procedures or develop new ones. These advancements can then inspire philosophical reflections, hopefully aiding in the design of better procedures and solving more inference problems. You may pick any role in this virtuous circle, and perhaps switch between them as you see fit. Here is the point: this virtuous circle can thrive only when there are active conversations among diverse groups of people: working scientists, statisticians, machine learning researchers, and hopefully philosophers as well.

In case this might help you estimate the bias of this article: I self-identify as a contextualist. And I believe that, although the right position varies systematically (rather than arbitrarily) with problem contexts, it is restricted to be moderate frequentism or centrism—that is, likelihoodist frequentism or frequentist Bayesianism.

## Acknowledgments

I extend my gratitude to the four anonymous referees and the editor-in-chief, Xiao-Li Meng, for their exceptionally thoughtful comments and encouraging words.

## Disclosure Statement

Hanti Lin has no financial or non-financial disclosures to share for this article.

## References

Barnard, G. A. (1967). The use of the likelihood function in statistical practice. In L. LeCam & J. Neyman (Eds.), *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability* (Vol. 1, pp. 27–40). University of California Press.

Bayarri, M. J., & Berger, J. O. (2004). The interplay of Bayesian and frequentist analysis. *Statistical Science, 19*(1), 58–80. https://doi.org/10.1214/088342304000000116

Carnap, R. (1945). The two concepts of probability: The problem of probability. *Philosophy and Phenomenological Research, 5*(4), 513–532. https://doi.org/10.2307/2102817

de Finetti, B. (1972). *Probability, induction, and statistics: The art of guessing.* John Wiley & Sons.

de Finetti, B. (1989). Probabilism: A critical essay on the theory of probability and on the value of science (M. C. Di Maio, M. C. Galavotti, & R. C. Jeffrey, Trans.). *Erkenntnis, 31*(2–3), 169–223. https://doi.org/10.1007/bf01236563. (Original work published 1931).

Diaconis, P., & Freedman, D. (1986). On the consistency of Bayes estimates. *Annals of Statistics, 14*(1), 1–26. https://doi.org/10.1214/aos/1176349830

Edwards, W., Lindman, H., & Savage, L. J. (1963). Bayesian statistical inference for psychological research. *Psychological Review, 70*(3), 193–242. https://psycnet.apa.org/doi/10.1037/h0044139

Fisher, R. A. (1925). *Statistical methods for research workers.* Oliver & Boyd.

Fisher, R. A. (1935). The Fiducial argument in statistical inference. *Annals of Eugenics, 5*(4), 391–398. https://doi.org/10.1111/j.1469-1809.1935.tb02120.x

Freedman, D. (1963). On the asymptotic behavior of Bayes’ estimates in the discrete case. *Annals of Mathematical Statistics, 34*(4), 1386–1403. https://doi.org/10.1214/aoms/1177703871

Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2014). *Bayesian data analysis.* CRC Press.

Gillies, D. (2000). *Philosophical theories of probability.* Routledge.

Hacking, I. (2016). *Logic of statistical inference.* Cambridge University Press. Original work published (1965).

Hájek, A. (2023). Interpretations of probability. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford Encyclopedia of Philosophy* (Winter ed.). Stanford Center for the Study of Language and Information. https://plato.stanford.edu/archives/win2023/entries/probability-interpret/

Hannig, J., Iyer, H., Lai, R. C. S., & Lee, T. C. M. (2016). Generalized fiducial inference: A review and new results. *Journal of the American Statistical Association, 111*(515), 1346–1361. https://doi.org/10.1080/01621459.2016.1165102

Neyman, J. (1977). Frequentist probability and frequentist statistics. *Synthese, 36*(1), 97–131. https://doi.org/10.1007/BF00485695

Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society of London, Series A, Containing Papers of a Mathematical or Physical Character, 231*(694-706), 289–337. https://doi.org/10.1098/rsta.1933.0009

Pawitan, Y. (2001). *In all likelihood: Statistical modelling and inference using likelihood.* Oxford University Press.

Pearson, E. S. (1947). The choice of statistical tests illustrated on the interpretation of data classed in a 2 x 2 table. *Biometrika, 34*(1–2), 139–167. https://doi.org/10.1093/biomet/34.1-2.139

Pearson, E. S. (1962). Some thoughts on statistical inference. *Annals of Mathematical Statistics, 33*(2), 394–403. https://doi.org/10.1214/aoms/1177704566

Petrone, S., Rizzelli, S., Rousseau, J., & Scricciolo, C. (2014). Empirical Bayes methods in classical and Bayesian inference. *Metron, 72*(2), 201–215. https://doi.org/10.1007/s40300-014-0044-1

Popper, C. (1959). The propensity interpretation of probability. *The British Journal for the Philosophy of Science, 10*(37), 25–42. https://doi.org/10.1093/bjps/x.37.25

Robbins, H. (1956). An empirical Bayes approach to statistics. In J. Neyman (Ed.), *Proceedings of the Third Berkeley Symposium Mathematical Statistics and Probability* (Vol. 1, pp. 157–163). University of California Press.

Robert, C. P. (2007). *The Bayesian choice: From decision-theoretic foundations to computational implementation* (2nd ed.). Springer.

Rousseau, J. (2016). On the frequentist properties of Bayesian nonparametric methods. *Annual Review of Statistics and Its Application, 3*, 211–231. https://doi.org/10.1146/annurev-statistics-041715-033523

Royall, R. (2017). *Statistical evidence: A likelihood paradigm.* Routledge.

Rubin, D. B. (1984). Bayesianly justifiable and relevant frequency calculations for the applied statistician. *Annals of Statistics, 12*(4), 1151–1172. https://doi.org/10.1214/aos/1176346785

von Mises, R. (1957). *Probability, statistics and truth* (Rev. English Ed.). Macmillan.

Yang, R., & Berger, J. O. (1996). *A catalog of noninformative priors.* Institute of Statistics and Decision Sciences, Duke University.

Zabell, S. L. (1992). “R. A. Fisher and Fiducial Argument,” *Statistical Science, 7*(3), 369–387. https://doi.org/10.1214/ss/1177011233

Zabell, S. L. (2011). Carnap and the logic of inductive inference. In D. M. Gabbay, S. Hartmann, & J. Woods (Eds.), *Handbook of the history of logic: Vol. 10. Inductive Logic* (pp. 265–310). Elsevier. https://doi.org/10.1016/B978-0-444-52936-7.50008-2

---

©2024 Hanti Lin. This article is licensed under a Creative Commons Attribution (CC BY 4.0) International license, except where otherwise indicated with respect to particular material included in the article.
