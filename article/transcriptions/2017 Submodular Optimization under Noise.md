# Submodular Optimization under Noise

**Avinatan Hassidim**\*
Bar Ilan University
avinatan@cs.biu.ac.il

**Yaron Singer**†
Harvard University
yaron@seas.harvard.edu

### Abstract
We consider the problem of maximizing a monotone submodular function under noise. There has been a great deal of work on optimization of submodular functions under various constraints, resulting in algorithms that provide desirable approximation guarantees. In many applications, however, we do not have access to the submodular function we aim to optimize, but rather to some erroneous or noisy version of it. This raises the question of whether provable guarantees are obtainable in presence of error and noise. We provide initial answers, by focusing on the question of maximizing a monotone submodular function under a cardinality constraint when given access to a noisy oracle of the function. We show that:
*   For a cardinality constraint $k \ge 2$, there is an approximation algorithm whose approximation ratio is arbitrarily close to $1 - 1/e$;
*   For $k = 1$ there is an algorithm whose approximation ratio is arbitrarily close to $1/2$. No randomized algorithm can obtain an approximation ratio better than $1/2 + o(1)$;
*   If the noise is adversarial, no non-trivial approximation guarantee can be obtained.

---
\*Supported by ISF 1241/12;
†Supported by NSF grant CCF-1301976, CAREER CCF-1452961, Google Faculty Research Award, Facebook Faculty Award.

---

## Contents

**1 Introduction**
1.1 Main result
1.2 Extensions
1.3 Applications
1.4 Paper organization

**2 Optimization for Large $k$**
2.1 The Smooth Greedy Algorithm
&nbsp;&nbsp;&nbsp;&nbsp;2.1.1 The algorithm
&nbsp;&nbsp;&nbsp;&nbsp;2.1.2 Smoothing guarantees
&nbsp;&nbsp;&nbsp;&nbsp;2.1.3 Approximation guarantee
2.2 Slick Greedy: Optimal Approximation for Sufficiently Large $k$
&nbsp;&nbsp;&nbsp;&nbsp;2.2.1 The algorithm
&nbsp;&nbsp;&nbsp;&nbsp;2.2.2 Generalizing guarantees of smooth greedy
&nbsp;&nbsp;&nbsp;&nbsp;2.2.3 The smooth comparison procedure
&nbsp;&nbsp;&nbsp;&nbsp;2.2.4 Approximation guarantee of SLICK GREEDY

**3 Optimization for Small $k$**
3.1 Combinatorial averaging
3.2 The Sampled Mean Greedy Algorithm
3.3 Smoothing Guarantees
3.4 Approximation Guarantee in Expectation
3.5 From Expectation to High Probability

**4 Optimization for Very Small $k$**
4.1 Smoothing Guarantees
4.2 An Approximation Algorithm for Very Small $k$
4.3 Information Theoretic Lower Bounds for Constant $k$

**5 Extensions**
5.1 Additive Noise
5.2 Marginal Noise
5.3 Correlated Noise
5.4 Information Degradation
5.5 Approximate Submodularity

**6 Impossibility for Adversarial Noise**

**7 More related work**

**8 Acknowledgements**

---

## 1 Introduction

In this paper we study the effects of error and noise on submodular optimization. A function $f : 2^N \to \mathbb{R}$ defined on a ground set $N$ of size $n$ is submodular if for any $S, T \subseteq N$:
$$f(S \cup T) \le f(S) + f(T) - f(S \cap T)$$

Equivalently, submodularity can be defined in terms of a natural diminishing returns property. For any $A, B \subseteq N$ let $f_A(B) = f(A \cup B) - f(A)$, then $f$ is submodular if $\forall S \subseteq T \subseteq N, a \in N \setminus T$:
$$f_S(a) \ge f_T(a).$$

In general, submodular functions may require a representation that is exponential in the size of the ground set and the assumption is that we are given access to a *value oracle* which given a set $S$ returns $f(S)$. It is well known that submodular functions admit desirable approximation guarantees and are heavily used in applications such as market design, data mining, and machine learning (see related work). For the classic problem of maximizing a monotone (i.e. $S \subseteq T \implies f(S) \le f(T)$) submodular function under a cardinality constraint, the greedy algorithm which iteratively adds the element with largest marginal contribution into the solution obtains a $1 - 1/e$ approximation [82] which is optimal unless using exponentially-many queries [81] or P=NP [35].

Since submodular functions can be exponentially representative, it may be reasonable to assume that there are cases where one faces some error in their evaluation. In market design where submodular functions often model agents' valuations for goods, it seems reasonable to assume that agents do not precisely know their valuations. Even with compact representation, evaluation of a submodular function may be prone to error. In learning and sketching submodular functions, the algorithms produce an approximate version of the function [48, 8, 7, 4, 42, 43, 30, 31, 41, 44, 6].

*Can we retain desirable approximation guarantees in the presence of error?*

For $f : 2^N \to \mathbb{R}$ and $\epsilon > 0$ we say that $\tilde{f} : 2^N \to \mathbb{R}$ is $\epsilon$-erroneous if for every set $S \subseteq N$, it respects:
$$(1 - \epsilon)f(S) \le \tilde{f}(S) \le (1 + \epsilon)f(S)$$

For the canonical problem of $\max_{S:|S|\le k} f(S)$, one can trivially approximate the solution within a factor of $\frac{1-\epsilon}{1+\epsilon}$ using $\binom{n}{k}$ queries with an $\epsilon$-erroneous oracle by simply evaluating all possible subsets and returning the best solution (according to the erroneous oracle). Is there a polynomial-time algorithm that can obtain desirable approximation guarantees for maximizing a monotone submodular function under a cardinality constraint given access to $\epsilon$-erroneous oracles? In Appendix F we sketch an example showing that the celebrated greedy algorithm fails to obtain an approximation strictly better than $O(1/k)$ for any constant $\epsilon > 0$ when given access to an $\epsilon$-erroneous oracle $\tilde{f}$ instead of $f$. It turns out that this is not intrinsic to greedy. No algorithm is robust to small errors.

**Theorem (6.1).** *No randomized algorithm can obtain an approximation strictly better than $O(n^{-1/2+\delta})$ to maximizing monotone submodular functions under a cardinality constraint using $e^{n^\delta}/n$ queries to an $\epsilon$-erroneous oracle, for any fixed $\epsilon, \delta < 1/2$, with high probability.*

Since desirable guarantees are generally impossible with erroneous oracles, we seek natural relaxations of the problem. The first could be to consider stricter classes of functions. It is trivial to show for example, that additive functions (i.e. $f(S) = \sum_{a \in S} f(a)$) allow us to obtain a $\frac{1-\epsilon}{1+\epsilon}$ approximation when given access to $\epsilon$-erroneous oracles. Unfortunately, it seems like there are not many interesting classes of submodular functions that enjoy these properties. In fact, our impossibility result applies to very simple affine functions, and even coverage functions like the example in Appendix F. An alternative relaxation is to consider error models that are not necessarily adversarial.

**Noisy oracles.** We can equivalently say that $\tilde{f} : 2^N \to \mathbb{R}$ is $\epsilon$-erroneous if for every $S \subseteq N$ we have that $\tilde{f}(S) = \xi_S f(S)$ for some $\xi_S \in [1 - \epsilon, 1 + \epsilon]$. The lower bound stated above applies to the case in which the error multipliers $\xi_S$ are adversarially chosen. A natural question is whether some relaxation of the adversarial error model can lead to possibility results.

**Definition.** *For a function $f : 2^N \to \mathbb{R}$ we say that $\tilde{f} : 2^N \to \mathbb{R}$ is a **noisy** oracle if there exists some distribution $\mathcal{D}$ s.t. $\tilde{f}(S) = \xi_S f(S)$ where $\xi_S$ is independently drawn from $\mathcal{D}$ for every $S \subseteq N$.*

Note that the noisy oracle defined above is *consistent*: for any $S \subseteq N$ the noisy oracle returns the same answer regardless of how many times it is queried. When the noisy oracle is inconsistent, mild conditions on the noise distribution allow the noise to essentially vanish after logarithmically-many queries, reducing the problem to standard submodular maximization (see e.g. [59, 91]). Consistency implies that the noise is arbitrarily correlated for a given set in different time steps, but i.i.d between different sets. In fact, we will later generalize the model to the case in which $\xi_S$ and $\xi_T$ are i.i.d only when $S$ and $T$ are sufficiently far, and arbitrarily correlated otherwise (see Section 1.3). At this point, we are interested in identifying a natural non worst-case model of corrupted or approximately submodular functions that is amendable to optimization.

We will be interested in a class of distributions that avoids trivialities like $\mathcal{D} \subseteq \{0\}$ and is yet general enough to contain natural distributions. In this paper we define a class which we call *generalized exponential tail* distributions that contains Gaussian, Exponential, and distributions with bounded support which are independent of $n$ (o.w. optimization is impossible, see Appendix E). Note that optimization in this setting always requires that $n$ is sufficiently large. For example, if for every $S$ the noise is s.t. $\xi_S = 2^{100}$ with probability $1/2^{100}$ and $0$ otherwise, but $n = 50$, it is likely that the noisy oracle will always return $0$, in which case we cannot do better than selecting an element at random. Throughout the paper we assume that $n$ is sufficiently large.

**Definition.** *A noise distribution $\mathcal{D}$ has a **generalized exponential tail** if there exists some $x_0$ such that for $x > x0$ the probability density function $\rho(x) = e^{-g(x)}$, where $g(x) = \sum_i a_i x^{\alpha_i}$. We do not assume that all the $\alpha_i$'s are integers, but only that $\alpha_0 \ge \alpha_1 \ge \dots$, and that $\alpha_0 \ge 1$. If $\mathcal{D}$ has bounded support we only require that either it has an atom at its supremum, or that $\rho$ is continuous and non zero at the supremum.*

For simplicity, one can always consider the special case where $\mathcal{D} \subseteq [1 - \epsilon, 1 + \epsilon]$, which implies that two sets whose true values are close will remain close in the noisy evaluation. Even when the noise distribution is uniform in $[1 - \epsilon, 1 + \epsilon]$ it is easy to show that the greedy algorithm fails (see Appendix F). The question is whether provable guarantees are achievable in this model.

### 1.1 Main result

Our main result is that for the problem of optimizing a monotone submodular function under a cardinality constraint, near-optimal approximations are achievable under noise.

**Theorem.** *For any monotone submodular function there is a polynomial-time algorithm which optimizes the function under a cardinality constraint $k > 2$ and obtains an approximation ratio that is w.h.p arbitrarily close to $1 - 1/e$ using access to a generalized exponential tail noisy oracle of the function.*

This proof is a summary of three results, each for a different regime of $k$. For any $\epsilon > 0$ we show:

*   **$1 - 1/e - \epsilon$ guarantee for large $k$:** we say that $k$ is large when $k \in \Omega(\log \log n / \epsilon^2)$. For $k$ that is sufficiently larger than $\log \log n / \epsilon^2$ we give a deterministic algorithm which obtains a $(1 - 1/e - \epsilon)$ approximation guarantee w.h.p over the noise distribution;
*   **$1 - 1/e - \epsilon$ guarantee for small $k$:** we say that $k$ is small when $k \in O(\log \log n) \cap \Omega(1/\epsilon)$. In this regime the problem is surprisingly harder. We give a different deterministic algorithm which achieves the coveted $(1 - 1/e - \epsilon)$ guarantee, w.h.p. over the noise distribution;
*   **Guarantees for very small $k$:** We say that $k$ is very small when it is an arbitrarily small constant. For this case we give a randomized algorithm whose approximation ratio is $1 - 1/k - \epsilon$ w.h.p. over the randomization of the algorithm and the noise distribution. Note that this gives $1 - 1/e - \epsilon$ for any $k > 2$, and $1/2 - \epsilon$ for $k = 2$. We also give a $k/(k + 1)$ approximation which holds in expectation over the randomization of the algorithm. This achieves $1 - 1/e$ for $k = 2$ and $1/2$ for $k = 1$. For $k = 1$ no randomized algorithm can obtain an approximation ratio better than $1/2 + O(1/\sqrt{n})$ and $(2k - 1)/2k + O(1/\sqrt{n})$ for general $k$.

At their core, the algorithms are variants of the classic greedy algorithm. In the presence of noise, greedy fails since it cannot identify the set whose value is maximal in each iteration. To handle noise, we apply a natural approach we call *smoothing*. In general, by selecting a family of sets $\mathcal{H}$ we can define a surrogate function $F(S) = \sum_{H' \in \mathcal{H}} f(S \cup H')$ and its noisy analogue $\tilde{F}(S) = \sum_{H' \in \mathcal{H}} \tilde{f}(S \cup H')$ which we can evaluate. Intuitively, when $\mathcal{H}$ is sufficiently large and chosen appropriately, submodularity and monotonicity can be used to argue that $\tilde{F}(S) \approx F(S)$. Thus, smoothing essentially makes the noise disappear and instead leaves us to deal with the implications of optimizing with the surrogate $F$ rather than $f$. In that sense, a large part of the challenge is in using optimization over the surrogate $F$ to approximate the optimum over $f$, i.e.:

*   **Large $k$.** In this regime, we first define SMOOTH-GREEDY which takes an arbitrary set $H$ of size $\log \log n$ and runs the greedy algorithm with the surrogate $F = \sum_{H' \subseteq H} f(T \cup H')$ on $N \setminus H$. In the analysis we show that its output together with $H$ is arbitrarily close to $1 - 1/e$ of the optimal solution evaluated on $f_H$ (not $f$). The SLICK-GREEDY algorithm runs multiple instantiations of a slightly modified version of SMOOTH-GREEDY with different smoothing sets, and obtains a guarantee arbitrarily close to $1 - 1/e$ of the true optimum;
*   **Small $k$.** In this regime, we use a modified version of greedy which adds a bundle of $O(1/\epsilon)$ elements in each iteration. For each such bundle $B$ we define a surrogate $\tilde{F}$ with a smoothing neighborhood of elements which are at distance $2$ on the $\{0, 1\}^n$ hypercube from $B$. In each iteration SM-GREEDY identifies the bundle $A$ which maximizes $\tilde{F}$, but doesn't take it. Taking a random bundle $\hat{A}$ from the smoothing neighborhood of $A$ gives the $1 - 1/e$ guarantee but *in expectation*. To obtain the result w.h.p. SM-GREEDY takes the bundle $\hat{A}$ which maximizes $\tilde{f}(B)$, over all bundles $B$ in the smoothing neighborhood of $A$. The analysis is then quite technical and strongly leverages the properties of the noise distribution and that $k \in O(\log \log n)$. It is for this reason it is crucial that SLICK-GREEDY applies to $k \in \Omega(\log \log n)$;
*   **Very small $k$.** In this case we consider bundles of size $k$ and smoothing with singletons.

### 1.2 Extensions

One of the appealing aspects of the noise model and the algorithms, is that they can easily be extended to a rich variety of related models. In Section 5 we discuss application to additive noise, marginal noise, correlated noise, information degradation, and approximate submodularity.

### 1.3 Applications

*   **Optimization under noise.** When considering optimization under noise, queries can be independent or correlated in *time* and in *space*. For $f : 2^N \to \mathbb{R}$ the noisy oracle is defined as $\tilde{f}(S) = \xi_S(t)f(S)$ where $\xi_S(t) \sim \mathcal{D}$, for every step the oracle is queried $t \in \mathbb{N}$ and $S \subseteq N$.

    **Definition.** *Noise is **i.i.d in time** if $\xi_S(t)$ and $\xi_S(t')$ are independent for any $t \neq t' \in \mathbb{N}$ and $S \subseteq N$. Similarly, we can say that noise is **i.i.d in in space** if $\xi_S(t)$ and $\xi_T(t')$ for any $S \neq T$ and $t, t' \in \mathbb{N}$. The noise distribution is **correlated in time (space)** if it is not independent in time (space).*

    The case in which the oracle is inconsistent is one where the noise is i.i.d in time and in space. From an algorithmic perspective this problem is largely solved, as discussed above. From Theorem 6.1 we know that there is no poly-time approximation algorithm for the case in which the errors are arbitrarily correlated in time and in space, even when the support of the noise distribution is arbitrarily small. The model we describe assumes the noise is arbitrarily correlated in time, but i.i.d in space. In Section 5 we show how one can relax this assumption. In particular, we show how to generalize the algorithms to obtain approximation ratios arbitrarily close to $1 - 1/e$ in a noise model where $\xi_S(t)$ and $\xi_T(t')$ are arbitrarily correlated in time and in space for any $t, t' \in \mathbb{N}$ and $S, T$ for which $|S \Delta T| \in O(\sqrt{k})$ when $k \in \Omega(\log \log n)$ and $|S \Delta T| \in O(1)$ when $k \in O(\log \log n)$. To the best of our knowledge, this is the first step towards studying submodular optimization under any correlation.

*   **Maximizing approximately submodular functions.** There are cases where one may wish to optimize an *approximately* submodular function. Theorem 6.1 implies that being arbitrarily close to a submodular function is not sufficient. In statistics and learning theory, to model the fact that data is generated by a function that is approximately in a class of well behaved functions, the function generating the data $\tilde{f}$ is typically assumed to be a noisy version of a function $f$ from a well-behaved class of functions [53, 97, 88]:
    $$\tilde{f}(\mathbf{x}) = f(\mathbf{x}) + \xi_\mathbf{x},$$
    where $\xi_\mathbf{x}$ is an i.i.d sample drawn from some distribution $\mathcal{D}$. In regression problems for instance, one assumes that the data is generated by $\tilde{f}(\mathbf{x}) = \mathbf{w}^\intercal \mathbf{x} + \xi_\mathbf{x}$. This model captures the idea that some phenomena may not exactly behave in a linear manner, but can be approximated by such a model. Making a good prediction then involves optimizing the noisy model. This therefore seems like a natural model to study approximate submodularity, especially in light of Theorem 6.1. Notice that in this case we would be interested in the optimization problem: $\max_{S:|S|\le k} \tilde{f}(S)$. In Section 5 we describe a black-box reduction which allows one to use the algorithms described here to get optimal guarantees.

*   **Active learning.** In *active learning* one assumes a membership oracle that can be queried to obtain labeled data [3]. In noise-robust learning, the task is to get good approximations to the noise-free target $f$ when the examples are corrupted by some noise. In this model the assumption is that noise is *consistent and i.i.d*, exactly as in our model. That is, we observe $\tilde{f}(\mathbf{x}) + \xi_\mathbf{x}$ where $\mathbf{x}$ is drawn i.i.d from $\mathcal{D}$ and multiple queries return the same answer (see e.g. [49, 55, 89, 56, 13, 40]). Our results apply to additive noise, and thus apply to active learning with noisy membership queries of submodular functions. One example application of active learning where the function is submodular is experimental design [70, 69, 54].

*   **Learning and sketching.** In learning and sketching the goal is to generate a surrogate function which approximates the submodular function well (see e.g. [48, 8, 7, 4, 42, 43, 30, 31, 41, 44, 6]). Theorem 6.1 implies that a surrogate which approximates a submodular function arbitrarily well may be inapproximable. Our main result shows that if when sets are sufficiently far the surrogate approximates the function via independent noise, then one can use the surrogate for optimization. This can therefore be used as a stricter benchmark for learning and sketching which allows optimizing a function learned or sketched from data.

### 1.4 Paper organization

The main technical contribution of the paper is the algorithms for the three different regimes of $k$. The exposition of the algorithms is contained in sections 2, 3, and 4, which can be read independently from each other. For each algorithm, we suppress proofs and additional lemmas to the corresponding section in the appendix. All the algorithms employ smoothing arguments which can be found in Appendix A. The smoothing arguments are used as a black-box in the proofs of each algorithm, and are not required for reading the main exposition. In Section 5 we discuss extensions of the algorithms to related models. In Section 6 we prove the result for adversarial noise. Discussion about additional related work is in Section 7.

---

## 2 Optimization for Large $k$

In this section we describe the SLICK-GREEDY algorithm whose approximation guarantee is arbitrarily close to $1 - 1/e$ for sufficiently large $k$. The algorithm is deterministic and for any desired degree of accuracy $\epsilon > 0$ can be applied when the cardinality constraint $k$ is in $\Omega(\log \log n / \epsilon^2)$, or more specifically when $k \ge 3168 \log \log n / \epsilon^2$. We first describe and analyze the SMOOTH-GREEDY algorithm. This algorithm is then used as a subroutine by the SLICK-GREEDY algorithm.

### 2.1 The Smooth Greedy Algorithm

We begin by describing the smoothing technique used by SMOOTH-GREEDY. We select an *arbitrary* set $H$ and for a given element $a$, the smoothing neighborhood is simply $\mathcal{H} = \{H' \subseteq H : H' \cup a\}$. Throughout the rest of this section we assume that $H$ is an arbitrary set of size $\ell$, where $\ell$ depends on $k$. In the case where $k \ge 2400 \log n$ we will use $\ell = 25 \log n$, and when $k < 2400 \log n$ we will use $\ell = 33 \log \log n$ [^1]. The precise choice for $\ell$ will become clear later in this section. Intuitively, $\ell$ is on the one hand small enough so that we can afford to sacrifice $\ell$ elements for smoothing the noise, and on the other hand $\ell$ is large enough so that taking all its subsets gives us a large smoothing neighborhood which enables applying concentration bounds.

**Definition.** *For a set $S \subseteq N$ and some fixed set $H \subseteq N$ of size $\ell$, we use $H^{(1)}, \dots, H^{(t)}$ to denote all the subsets of $H$ and $k' = k - \ell$. The **smooth value**, **noisy smooth value** and **smooth marginal contribution** are, respectively:*
$$(1) \quad F(S \cup a) := \mathbb{E}\left[f(S \cup (H^{(i)} \cup a)\right] = \frac{1}{t} \sum_{i=1}^t f\left(S \cup (H^{(i)} \cup a)\right);$$
$$(2) \quad \tilde{F}(S \cup a) := \mathbb{E}\left[\tilde{f}(S \cup (H^{(i)} \cup a)\right] = \frac{1}{t} \sum_{i=1}^t \tilde{f}\left(S \cup (H^{(i)} \cup a)\right);$$
$$(3) \quad F_S(a) := \mathbb{E}\left[f_S((H^{(i)} \cup a))\right] = \frac{1}{t} \sum_{i=1}^t f_S\left(H^{(i)} \cup a\right).$$

[^1]: W.l.o.g. we assume that $k < n - 25 \log n$ as for sufficiently large $n$ this then implies that $k \ge (1-\epsilon)n$ and by submodularity optimizing with $k' = n - 25 \log n$ suffices to get the $1 - 1/e - \epsilon$ guarantee for any fixed $\epsilon > 0$.

#### 2.1.1 The algorithm

The smooth greedy algorithm is a variant of the standard greedy algorithm which replaces the procedure of adding $\arg\max_{a \in N} f(S \cup a)$ with its smooth analogue. The algorithm receives a set of elements $H$ of size $\ell$, initializes $S = \emptyset$ and at every stage adds to $S$ the element $a \notin H$ for which the smooth noisy value $\tilde{F}(S \cup a)$ is largest. A formal description is added below.

**Algorithm 1** SMOOTH-GREEDY
**Input:** budget $k$, set $H$
1: $S \leftarrow \emptyset$
2: **while** $|S| < k - |H|$ **do**
3:     $S \leftarrow S \cup \arg\max_{a \notin H} \tilde{F}(S \cup a)$
4: **end while**
5: **return** $S$

**Overview of the analysis.** At a high level, the idea behind the analysis is to compare the performance of the solution returned by the algorithm against an optimal solution which ignores the value of $H$ and any of its partial substitutes. More specifically, let $\texttt{OPT}$ denote the value of the optimal solution with $k$ elements evaluated on $f$ and $\texttt{OPT}_H$ denote the value of the optimal solution with $k' = k - \ell$ elements evaluated on $f_H$, where $f_H(T) = f(T \cup H) - f(H)$. Essentially, we will show that at every step SMOOTH-GREEDY selects an element whose marginal contribution is larger than that of an element from the optimal solution evaluated on $f_H$. Together with an inductive argument this suffices for a constant factor approximation.

**Relevant iterations.** One of the artifacts of noise is that our comparisons are not precise. Specifically, when we select an element that maximizes $\tilde{F}(S \cup a)$, our smoothing guarantee will be that this element respects $F_S(a) \ge (1 - \delta) \max_{b \notin H} F_S(b)$ for $\delta > 0$ that depends on $\epsilon$ and $k$. This can be guaranteed only for an iteration where two conditions are met: (i) there is at least a single element not yet selected (and not in $H$) whose marginal contribution is at least $\epsilon / k$ fraction of $\texttt{OPT}_H$, and (ii) $\texttt{OPT}_H$ is sufficiently large in comparison to $\texttt{OPT}$. We call such iterations $\epsilon$-relevant.

**Definition.** *For a given iteration of SMOOTH-GREEDY let $S$ be the set of elements selected in previous iterations. The iteration is **$\epsilon$-relevant** if (i) $\max_{b \notin H} f_{H \cup S}(b) \ge \frac{\epsilon \cdot \texttt{OPT}_H}{k}$ and (ii) $\texttt{OPT}_H \ge \frac{\texttt{OPT}}{e}$.*

We will analyze SMOOTH-GREEDY in the case where the iterations are $\epsilon$-relevant as it allows applying the smoothing arguments. In the analysis we will then ignore iterations that are not $\epsilon$-relevant at the expense of a negligible loss in the approximation guarantee. The main steps are:

1.  In Lemma 2.1 we show that in each $\epsilon$-relevant iteration the (non-noisy) smooth marginal contribution of the element selected in that iteration by the algorithm is w.h.p. an arbitrarily good approximation to $\max_{b \notin H} F_S(b)$. To do so we need claims B.1, B.2 and B.3;
2.  Next, in Claim 2.3 we show that the element $a$ whose smooth marginal contribution $F_S(a)$ is maximal has true marginal contribution $f_S(a)$ that is roughly a $k'$th fraction of the marginal contribution of the optimal solution over $f_H$;
3.  Finally, in Lemma 2.4 we apply a standard inductive argument to show that the fact that the algorithm selects an element with large smooth value in each step results in an approximation arbitrarily close to $1 - 1/e$ to $\texttt{OPT}_H$ (not $\texttt{OPT}$). In Corollary B.4 we show that the bound against $\texttt{OPT}_H$ can already be used to give a constant factor approximation to $\texttt{OPT}$. To get arbitrarily close to $1 - 1/e$, SLICK-GREEDY executes multiple instantiations of a generalization of SMOOTH-GREEDY as later described in Section 2.2.

#### 2.1.2 Smoothing guarantees

The first step is to prove Lemma 2.1. This lemma shows that at every step as SMOOTH-GREEDY adds the element that maximizes the noisy value $\arg\max_{a \notin H} \tilde{F}(S \cup a)$, that element nearly maximizes the (non-noisy) smooth marginal contribution $F_S$, with high probability.

**Lemma 2.1.** *For any fixed $\epsilon > 0$, consider an $\epsilon$-relevant iteration of SMOOTH-GREEDY where $S$ is the set of elements selected in previous iterations and $a \in \arg\max_{b \notin H} \tilde{F}(S \cup b)$. Then for $\delta = \epsilon^2 / 4k$ and sufficiently large $n$ we have that w.p. $\ge 1 - 1/n^4$:*
$$F_S(a) \ge (1 - \delta) \max_{b \notin H} F_S(b).$$

To prove the above lemma we use claims B.1, B.2, and B.3. The statements and proofs can be found in Appendix B and are best understood after reading the smoothing section in Appendix A.

#### 2.1.3 Approximation guarantee

Lemma 2.1 lets us forget about noise, at least for the remainder of the analysis of SMOOTH-GREEDY. We can now focus on the consequences of selecting an element $a$ which (up to factor $1 - \delta$) maximizes $F_S$ rather than the true marginal contribution $f_S$.

**Claim 2.2.** *For any $\epsilon > 0$, let $\delta \le \epsilon^2 / 4k$. Suppose that the iteration is $\epsilon$-relevant and let $b^* \in \arg\max_{b \notin H} f_{H \cup S}(b)$. If $F_S(a) \ge (1 - \delta)F_S(b^*)$, then:*
$$f_S(a) \ge (1 - \epsilon)f_{H \cup S}(b^*).$$

The principle is similar to Claim B.1. In this version we have a weaker condition since $F_S(a)$ is not greater than $F_S(b^*)$ but rather $(1 - \delta)F_S(b^*)$, but the claim is less general as it only needs to hold for $b^*$. We therefore use a slightly different approach to prove this claim (see Appendix B).

**Claim 2.3.** *For any fixed $\epsilon > 0$, consider an $\epsilon$-relevant iteration of SMOOTH-GREEDY with $S$ as the elements selected in previous iterations. Let $a \in \arg\max_{b \notin H} \tilde{F}(S \cup b)$. Then, w.p. $\ge 1 - 1/n^4$:*
$$f_S(a) \ge (1 - \epsilon)\left[ \frac{1}{k'} \Big(\texttt{OPT}_H - f(S)\Big) \right].$$

The proof is in Appendix B. We can now state the main lemma of this subsection.

**Lemma 2.4.** *Let $S$ be the set returned by SMOOTH-GREEDY and $H$ its smoothing set. Then, for any fixed $\epsilon > 0$ when $k \ge 3\ell/\epsilon$ with probability of at least $1 - 1/n^3$ we have that:*
$$f(S \cup H) \ge (1 - 1/e - \epsilon/3) \texttt{OPT}_H.$$

To prove the lemma we show that if $\texttt{OPT}_H < \texttt{OPT}/e$ then $H$ alone provides the approximation guarantee. Otherwise we can apply Claim 2.3 using a standard inductive argument to show that $S \cup H$ provides the approximation. The subtle yet crucial aspect of the proof is that the inductive argument is applied to analyze the quality of the solution against the optimal solution for $f_H$ and not against the optimal solution on $f$. The proof is in Appendix B.

As we will soon see, Lemma 2.4 plays a key role in the analysis of the SLICK-GREEDY algorithm. It is worth noting that this lemma can also be used to show that SMOOTH-GREEDY alone provides a constant ($\approx 0.387$) albeit suboptimal approximation guarantee (Corollary B.4).

### 2.2 Slick Greedy: Optimal Approximation for Sufficiently Large $k$

The reason SMOOTH-GREEDY cannot obtain an approximation arbitrarily close to $1 - 1/e$ is due to the fact that a substantial portion of the optimal solution's value may be attributed to $H$. This would be resolved if we had a way to guarantee that the contribution of $H$ is small. The idea behind SLICK-GREEDY is to obtain this type of guarantee. Intuitively, by running a large albeit constant number of instances of SMOOTH-GREEDY with different smoothing sets, selecting the "best" solution will ensure the contribution of the smoothing set is relatively minor.

#### 2.2.1 The algorithm

We can now describe the SLICK-GREEDY algorithm which is the main result of this section. Given a constant $\epsilon > 0$ we set $\delta = \epsilon/6$ and generate arbitrary sets $H_1, \dots, H_{1/\delta}$, each of size $\ell$ s.t. $H_i \cap H_j = \emptyset$ for every $i, j \in [1/\delta]$. We then run a modified version of SMOOTH-GREEDY $1/\delta$ times: in each iteration $j$ we initialize SMOOTH-GREEDY with $R_j = \cup_{i \neq j} H_i$ [^2] and use $H_j$ to generate the smoothing neighborhood. We denote this as SMOOTH-GREEDY$(k, R_j, H_j)$. We then compare the solution $T_j = S_j \cup H_j$ to the best $T_i = S_i \cup H_i$ we've seen so far using a procedure we call SMOOTH-COMPARE described below. The SMOOTH-COMPARE procedure compares $T_i$ and $T_j$ by using a set $H_{ij}$ s.t. $H_{ij} \cap (T_j \cup T_i) = \emptyset$ and $|H_{ij}| = \ell$. If $T_i$ wins, the procedure returns $T_i$ and otherwise returns $T_j$. The SLICK-GREEDY then returns the set $T_i$ that survived the SMOOTH-COMPARE tournament.

[^2]: By initializing the SMOOTH-GREEDY with $R_j$ we mean that the first iteration begins with $S = R_j$ rather than $S = \emptyset$ and following the initialization the algorithm greedily adds $k - |R_j| - |H_j|$ elements.

**Algorithm 2** SLICK-GREEDY
**Input:** budget $k$
1: Select $\ell/\delta$ elements in $N$ and partition them into disjoint sets of equal size $H_1 \dots, H_{1/\delta}$
2: $T_i \leftarrow \emptyset$
3: **for** $j \in [1/\delta]$ **do**
4:     $R_j \leftarrow \cup_{i \neq j} H_i$
5:     $T_j \leftarrow \text{SMOOTH-GREEDY}(k, R_j, H_j) \cup H_j$
6:     $H_{ij} \leftarrow \text{arbitrary set of } \ell \text{ elements disjoint from } T_i \cup T_j$
7:     $T_i \leftarrow \text{SMOOTH-COMPARE}(\{T_i, T_j\}, H_{ij})$
8: **end for**
9: **return** $T_i$

**Overview of the analysis.** Consider the smoothing sets $H_1, \dots, H_{1/\delta}$. Let $H_l$ be the smoothing set whose marginal contribution to the others is minimal, i.e. $H_l \in \arg\min_{i \in [1/\delta]} f_{R_i}(H_i)$. Notice that from submodularity we are guaranteed that $f_{R_l}(H_l) \le \delta f(R_l \cup H_l)$. In this case, the fact that the marginal contribution of $H_l$ to the rest of the smoothing sets $R_l$ is small, together with the fact that the solution is initialized with $R_l$, enables the tight analysis. The two main steps are:

1.  In Lemma 2.5 we show that w.h.p. $T_l$ provides an approximation arbitrarily close to $(1 - 1/e)$. Intuitively, this happens since the marginal contribution of $H_l$ to the rest of the smoothing sets $R_l = \cup_i H_i \setminus H_l$ is small, and since the solution to SMOOTH-GREEDY is initialized with $R_l$, losing the value of $H_l$ is negligible. The proof relies on Claim B.5 and Lemma B.7 that generalize the guarantees of SMOOTH-GREEDY to the case it is initialized (see Appendix);
2.  We then describe and analyze the SMOOTH-COMPARE procedure. In the absence of noise, one can simply select the set whose value is largest. To overcome noise, we run a tournament to extract the solution whose value is approximately largest, or at least arbitrarily close to $(1 - 1/e)\texttt{OPT}$. Specifically, we prove that w.h.p. the set $T_i$ that wins the SMOOTH-COMPARE tournament (i.e. the set $T_i$ returned by SLICK-GREEDY) satisfies $f(T_i) \ge (1 - \epsilon/3) \min\{f(T_l), (1 - 1/e - 2\epsilon/3)\texttt{OPT}\}$. Since $f(T_l)$ is arbitrarily close to $(1 - 1/e)\texttt{OPT}$, this concludes the proof.

#### 2.2.2 Generalizing guarantees of smooth greedy

**Lemma 2.5.** *Let $S_l$ be the set returned by SMOOTH-GREEDY that is initialized with $R_l$ and $H_l$ its smoothing set. Then, for any fixed $\epsilon > 0$ when $k \ge 36\ell/\epsilon^2$ w.p. at least $1 - 1/n^3$ we have that:*
$$f(S_l \cup H_l) \ge (1 - 1/e - 2\epsilon/3)\texttt{OPT}.$$

#### 2.2.3 The smooth comparison procedure

We can now describe the SMOOTH-COMPARE procedure we use in the algorithm. For a given set $H_{ij} \subseteq N$ of size $\ell$ and two sets $T_i, T_j \subseteq N \setminus H_{ij}$, we compare $\tilde{f}(T_i \cup H'_{ij})$ with $\tilde{f}(T_j \cup H'_{ij})$ for all $H'_{ij} \subset H_{ij}$. We select $T_i$ if in the majority of the comparisons with $H'_{ij} \subset H_{ij}$ (breaking ties lexicographically) we have that $\tilde{f}(T_i \cup H'_{ij}) \ge \tilde{f}(T_j \cup H'_{ij})$, and otherwise we select $T_j$.

**Algorithm 3** SMOOTH-COMPARE
**Input:** $T_i, T_j, H_{ij} \subseteq N \setminus (T_i \cup T_j)$
1: Compare $\tilde{f}(T_i \cup H'_{ij})$ with $\tilde{f}(T_j \cup H'_{ij})$ for all $H'_{ij} \subset H_{ij}$
2: if $T_i$ won the majority of comparisons **return** $T_i$ otherwise **return** $T_j$

**Lemma 2.6.** *Assume $k \ge 96\ell/\epsilon^2$. Let $T_i$ be the set that won the SMOOTH-COMPARE tournament. Then, with probability at least $1 - 1/n^2$:*
$$f(T_i) \ge \left(1 - \frac{\epsilon}{3}\right) \min \left\{ \left(1 - \frac{1}{e} - \frac{2\epsilon}{3}\right) \texttt{OPT}, \max_{j \in [1/\delta]} f(T_j) \right\}$$

The proof of this lemma has two parts.

1.  First we show in Claim B.8 that if a set $T_i$ has moderately larger value than another set $T_j$ (more specifically, if the gap is $1 - \epsilon\delta/3$) then as long as $f(T_j)$ is not arbitrarily close to $(1 - 1/e)\texttt{OPT}$ then $f(T_i \cup H'_{ij})$ is larger than $f(T_j \cup H'_{ij})$, for any $H'_{ij} \subseteq H_{ij}$. At a high level, this is because elements in $H'_{ij}$ are candidates for SMOOTH-GREEDY and the fact that they are not selected indicates that their marginal contribution to $T_j = S_j \cup H_j$ is low. Thus, elements in $H'_{ij}$ cannot add much value, and since $|H_{ij}| \ll k$ adding subsets of $H_{ij}$ does not distort the comparison by much. If $f(T_j)$ is arbitrarily close to $(1 - 1/e)\texttt{OPT}$, we may have that $T_j$ beats $T_i$, but this would still ultimately result in an approximation arbitrarily close to $1 - 1/e$;
2.  The next step (Claim B.9) then shows that if for every $H'_{ij}$ we have $f(T_i \cup H'_{ij}) \ge f(T_j \cup H'_{ij})$ then with high probability $T_i$ wins the comparison against $T_j$ in SMOOTH-COMPARE.

Using these two parts we then conclude since we are running the SMOOTH-COMPARE tournament between $1/\delta$ sets, the winner is an $(1 - \epsilon\delta/3)^{1/\delta} \ge (1 - \epsilon/3)$ approximation to the competing set with the highest value or a set whose approximation is arbitrarily close to $1 - 1/e$. The claims and proofs can be found in Appendix B.

#### 2.2.4 Approximation guarantee of SLICK GREEDY

Finally, putting everything together, we can prove the main result of this section.

**Theorem 2.1.** *Let $f : 2^N \to \mathbb{R}$ be a monotone submodular function. For any fixed $\epsilon > 0$, when $k \ge 3168 \log \log n / \epsilon^2$, then given access to a noisy oracle whose noise distribution has a generalized exponential tail, the SLICK-GREEDY algorithm returns a set which is a $(1 - 1/e - \epsilon)$ approximation to $\max_{S:|S|\le k} f(S)$, with probability at least $1 - 1/n$.*

---

## 3 Optimization for Small $k$

When $k$ is small we cannot use the smoothing technique from the previous section, since it requires including the smoothing set of size $\Theta(\log \log n)$ in the solution. In this section we describe the *sampled mean* method which can be applied to $k \in \Omega(1/\epsilon) \cap O(\log \log n)$ and results in a $1 - 1/e - \epsilon$ approximation. This result is obtained by applying a greedy algorithm on a surrogate function $F : 2^N \to \mathbb{R}_+$ which is what we call the *sampled mean* of $f$. The use of the surrogate function makes it relatively easy to obtain the $1 - 1/e - \epsilon$ approximation, albeit *in expectation*. The main technical challenge is the transition from a guarantee that holds in expectation to one that holds with high probability. This difficulty is what limits this method to be applicable only when $k$ ranges between $\Omega(1/\epsilon)$ and $O(\log \log n)$, and heavily exploits the generalized exponential tail property.

### 3.1 Combinatorial averaging

The sampled-mean method is based on averaging sets to find elements whose marginal contribution is high, which can then be greedily added to the solution. The intuition for this method comes from continuous optimization. Consider optimizing a function $f : \mathbb{R}^n \to \mathbb{R}$ given access to a noisy value oracle $\tilde{f} : \mathbb{R}^n \to \mathbb{R}$ which for each point $\mathbf{x} \in \mathbb{R}^n$ returns $\tilde{f}(\mathbf{x}) = \xi_{\mathbf{x}}f(\mathbf{x})$ where $\xi_{\mathbf{x}} \sim \mathcal{D}$. A natural approach would be to sample $t$ points $\mathbf{x}_1, \dots, \mathbf{x}_t$ from an $\epsilon$-ball $\mathcal{B}_\epsilon$ around $\mathbf{x}$, for some small $\epsilon > 0$, and estimate the value of $\mathbf{x}$ using the sampled mean:
$$\tilde{F}(\mathbf{x}) := \mathbb{E}\left[\tilde{f}(\mathbf{x})\right] = \frac{1}{t} \sum_{\mathbf{x}_i \sim \mathcal{B}_\epsilon} f(\mathbf{x}_i)$$

Under some smoothness assumptions on $f$, for sufficiently large $t$ and small $\epsilon$, concentration bounds kick in, and one can apply an optimization algorithm on $\tilde{F}$ to optimize $f$. The method in this section translates this idea to a combinatorial domain. To do so effectively, rather than considering singletons $a \in N$ we obtain multidimensionality by considering *bundles* of size $c \in O(1/\epsilon)$.

**Definition.** *Let $f : 2^N \to \mathbb{R}$. For a set $S \subseteq N$ and bundle $A \subseteq N$ of fixed size $c$, we define $A_{ij} := (A \setminus \{a_i\}) \cup \{a_j\}$ for $a_i \in A$ and $a_j \notin S \cup A$, and $t = c(n - c - |S|)$. The **mean value**, **noisy mean value**, and **mean marginal contribution** of $A$ given $S$ are, respectively:*
$$(1) \quad F(S \cup A) := \mathbb{E}[f(S \cup A_{ij})] = \frac{1}{t} \sum_{i \in A} \sum_{j \notin S \cup A} f(S \cup A_{ij});$$
$$(2) \quad \tilde{F}(S \cup A) := \mathbb{E}\left[\tilde{f}(S \cup A_{ij})\right] = \frac{1}{t} \sum_{i \in A} \sum_{j \notin S \cup A} \tilde{f}(S \cup A_{ij});$$
$$(3) \quad F_S(A) := \mathbb{E}[f_S(A_{ij})] = \frac{1}{t} \sum_{i \in A} \sum_{j \notin S \cup A} f_S(A_{ij}).$$

The above definition mimics the continuous case by considering a bundle of elements $A$ of fixed size $c$ (we will use $c \approx 1/\epsilon$) as a point, and the points in the $\epsilon$-ball are modeled by all the sets $A_{ij}$ obtained by replacing an element from $A$ with an element from $N \setminus (S \cup A)$. Although the combinatorial analogue is not as well-behaved as the continuous case, the sampled mean approach defined here extracts some of its desirable properties.

### 3.2 The Sampled Mean Greedy Algorithm

The SM-GREEDY begins with the empty set $S$ and at every iteration considers all bundles of size $c \in O(1/\epsilon)$ to add to $S$. At every iteration, the algorithm first identifies the bundle $A$ which maximizes the noisy mean value. After identifying $A$, it then considers all possible bundles $A_{ij}$ and takes the one whose noisy mean value is largest. We describe the algorithm formally below.

**Algorithm 4** SM-GREEDY
**Input:** budget $k$, precision $\epsilon > 0$, $c \in O(\frac{1}{\epsilon})$
1: $S \leftarrow \emptyset$
2: **while** $|S| < c \cdot \lfloor \frac{k}{c} \rfloor$ **do**
3:     $A \leftarrow \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$
4:     $S \leftarrow S \cup \arg\max_{i \in A, j \notin S \cup A} \tilde{f}(S \cup A_{ij})$
5: **end while**
6: **return** $S$

At a high level, the major steps in the analysis can be described as follows.

1.  We begin with smoothing guarantees. In Lemma 3.2 we apply Lemma 3.1 as well as other arguments to show that w.h.p. in each iteration $A \in \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$ well approximates the bundle with maximal (non-noisy) mean marginal contribution $\arg\max_{B:|B|=c} F_S(B)$;
2.  Lemma 3.3 argues that if the marginal contribution $f_S(\hat{A})$ of the set $\hat{A}$ we select at every iteration is close to the mean marginal contribution $F_S(A)$ we obtain an approximation arbitrarily close to $1 - 1/e$. This suffices for an approximation guarantee that holds in expectation;
3.  The last step is Lemma 3.4 which is the technical crux of this section. We show that taking $\hat{A} \in \arg\max_{i,j} \tilde{f}(S \cup A_{ij})$ in line 4 of the algorithm gives us, with sufficiently high probability that the marginal contribution $f_S(\hat{A})$ is arbitrarily close to the mean marginal contribution $F_S(A)$. We can therefore invoke Lemma 3.3 and recover the optimal approximation guarantee.

### 3.3 Smoothing Guarantees

We first show that the largest marginal contribution is well approximated by its mean contribution.

**Lemma 3.1.** *For any $\epsilon > 0$ and any set $S \subset N$, let $A^* \in \arg\max_{A:|A|=1/\epsilon} f_S(A)$. Then:*
$$(1 - \epsilon)f_S(A^*) \le F_S(A^*) \le f_S(A^*).$$

The proof is in Appendix C and exploits a natural property of submodular functions: the removal of a random element from a large set does not significantly affect its value, in expectation.

**Significant iterations.** Similar to the previous section, we define an assumption on the iterations of the algorithm which allows us to employ the smoothing technique in this section.

**Definition.** *Let $B \in \arg\max_{B:|B|=c} f_S(B)$. An iteration of SM-GREEDY is **$\epsilon$-significant** if for the given set $S$ selected before the iteration we have that $f_S(B) \ge \frac{\epsilon \cdot c \cdot \texttt{OPT}}{k}$.*

The following lemma implies that at every step we add a bundle whose smooth marginal contribution is comparable with the largest smooth marginal contribution obtainable.

**Lemma 3.2.** *Let $A \in \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$ where $c \ge \frac{16}{\epsilon}$, and assume that the iteration is $\frac{\epsilon}{4}$-significant. Then, with probability at least $1 - e^{-\Omega(n^{1/10})}$ we have that:*
$$F_S(A) \ge (1 - \epsilon) \max_{B:|B|=c} F_S(B).$$

The proof relies on arguments from the smoothing framework (Appendix A). In this case, the application of smoothing is a bit subtle as we do not apply smoothing on the noisy version of $F$ directly. The proof uses Lemma 3.1 above as well as Claim C.2 which bounds the variation in values of sets $A^*_{ij}$, when $A^* \in \arg\max_{B:|B|=c} f_S(B)$. Details and proofs are in Appendix C.

### 3.4 Approximation Guarantee in Expectation

**Lemma 3.3.** *Let $\delta > 0$ and assume $k > 16/\delta^2, c = 16/\delta$. Suppose that in every $\delta/4$-significant iteration of SM-GREEDY when $S$ are the elements selected in previous iterations, $A \in \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$, the bundle added $\hat{A}$ respects $f_S(\hat{A}) \ge (1 - \delta)F_S(A)$. Let $\bar{S}$ be the solution after $\lfloor k/c \rfloor$ iterations. Then, w.p. $\ge 1 - 1/n^2$:*
$$f(\bar{S}) = (1 - 1/e - 5\delta)\texttt{OPT}.$$

This lemma implicitly proves an approximation guarantee that holds *in expectation*. This is simply because we know that if we choose $\hat{A} = A \setminus \{a_i\} \cup \{a_j\}$ uniformly at random over all choices of $i \in [c], a_j \notin S \cup A$ we get $\mathbb{E}[f_S(\hat{A})] = F_S(A) > (1 - \delta)F_S(A)$ in every iteration, and thus by Lemma 3.3 we would be arbitrarily close to $1 - 1/e$, in expectation over all our choices.

### 3.5 From Expectation to High Probability

From Lemma 3.2 we know that $A \in \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$ has mean marginal contribution arbitrarily close to $\max_{B:|B|=c} F_S(B)$, but for Lemma 3.3 to hold we need the true marginal contribution $f_S(\hat{A})$ to be arbitrarily close to $\max_{B:|B|=c} F_S(B)$. Simply adding $A$ can easily lead to an arbitrarily bad approximation (see Appendix F). In order to prove that SM-GREEDY provides the desired approximation guarantee, we need to show that when $\hat{A} \in \arg\max_{i \in [c], j \notin S \cup A} \tilde{f}(S \cup A_{ij})$ then with sufficiently high probability $f_S(\hat{A})$ is arbitrarily close to $F_S(A)$ as required by Lemma 3.3.

**High-level overview to show high probability guarantee.** Let $A^* \in \arg\max_{B:|B|=c} f_S(B)$ and $A \in \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$. We will define two kinds of sets in $\{A_{ij}\}_{i \in [c], j \notin S \cup A}$, called **good** and **bad**. A good set is a set $G$ for which $f_S(G) \ge (1 - 2\epsilon)f_S(A^*)$ and a bad set is a set $B$ for which $f_S(B) \le (1 - 3\epsilon)f_S(A^*)$. Our goal is to prove $\arg\max \{\tilde{f}(S \cup A_{ij}) : a_i \in A, a_j \notin S \cup A\}$ is w.h.p. not bad. Doing so implies that in every iteration w.h.p. we add a bundle whose true marginal value is at least $(1 - 3\epsilon)$ of $f_S(A^*)$ which is an upper bound on $\max_{B:|B|=c} F_S(B)$ (and thus also on $F_S(A)$).

**Lemma 3.4.** *For any $\epsilon > 0$, suppose we run SM-GREEDY where in each iteration we add a bundle of size $c = 16/\epsilon$. For any $\epsilon/8$-significant iteration where the set previously selected is $S : |S| \in O(\log \log n)$, let $A \in \arg\max \tilde{F}(S \cup A)$ and $\hat{A} = \arg\max_{(i, j) \in A \times N \setminus S \cup A} \tilde{f}(S \cup A_{ij})$. Then, w.p. $\ge 1 - 3/\log n$ we have:*
$$f_S(\hat{A}) \ge (1 - 3\epsilon)F_S(A).$$

At a high level, the proof follows the following steps:

1.  In Claim C.4 we show that for $A \in \arg\max_{B:|B|=c} \tilde{F}(S \cup B)$, at least half of the sets in $\{A_{ij}\}_{i \in A, j \notin S \cup A}$ are good, and at most half are bad;
2.  Next, we define two thresholds: $\theta_g$ and $\theta_b$. Intuitively, $\theta_g$ is a lower bound on the maximum of noise multipliers from the good sets, and $\theta_b$ is an upper bound on the maximum of noise multipliers from bad sets. We then show in Lemma C.8 that $\theta_g \ge (1 - \gamma)\theta_b$, for any $\gamma = \Omega(1/\log \log n)$. This lemma is quite technical, and it is where we fully leverage the property of the generalized exponential tail distribution and the fact that $k \in O(\log \log n)$;
3.  From $\theta_g \ge (1 - \gamma)\theta_b$ and Claim C.4 we can prove that w.h.p. there is at least one good set whose noisy value is sufficiently larger than the noisy value of a bad set. The fact that a bad set loses to a good set implies that the value of the set we end up selecting must at least be as high as that of a bad set, i.e. $f_S(\hat{A}) \ge (1 - 3\epsilon)f_S(A^*)$. Notice that by definition $f_S(A^*)$ is an upper bound on $F_S(B)$ for any bundle $B$ of size $c$ which therefore completes the proof.

Lemma 3.4 above essentially tells us that at every iteration we select the bundle whose marginal contribution is almost maximal. Together with previous arguments from this section, this proves our main theorem for the case in which $k \in \Omega(1/\epsilon^2) \cap O(\log \log n)$. For $k \in \Omega(\frac{1}{\epsilon}) \cap O(\frac{1}{\epsilon^2})$ we run a single iteration of SM-GREEDY with $c = k$ (o.w. the approximation is $\approx 1/2$, when $k = 2c - 1$).

**Theorem 3.5.** *For any monotone submodular function $f : 2^N \to \mathbb{R}$ and $\epsilon > 0$, when $k \in \Omega(1/\epsilon) \cap O(\log \log n)$, there is a $(1 - 1/e - \epsilon)$ approximation for $\max_{S:|S|\le k} f(S)$, with probability $1 - 4/\log n$ given access to a noisy oracle whose distribution has a generalized exponential tail.*

---

## 4 Optimization for Very Small $k$

The smoothing guarantee from the previous section actually necessitates selecting bundles of size $c \in \Theta(1/\epsilon)$ and does not apply to very small values of $k \in O(1/\epsilon)$. For small constants we propose a different algorithm that uses a different smoothing technique. The algorithm is simple and applies the same principles as the ones from the previous section. We show that this simple algorithm obtains an approximation ratio arbitrarily close to $1 - 1/e$ w.h.p. when $k > 2$ and in expectation when $k = 2$. For $k = 1$ we get arbitrarily close to $1/2$, which is tight. We show lower bounds for small values of $k$ and in particular when $k = 1$ show that no algorithm can obtain an expected approximation ratio better than $1/2 + o(1)$. All proofs and details are in Appendix D.

### 4.1 Smoothing Guarantees

The smoothing here is straightforward. For every set $A$ consider the smoothing neighborhood $\mathcal{H}(A) = \{A \cup x : x \notin A\}$, $F(A) = \mathbb{E}_{X \in \mathcal{H}(A)}[f(X)]$ and $\tilde{F}(A) = \mathbb{E}_{X \in \mathcal{H}(A)}[\tilde{f}(X)]$.

**Lemma 4.1.** *Let $A \in \arg\max_{B:|B|=k} \tilde{F}(B)$. Then, for any fixed $\epsilon > 0$ w.p. $1 - e^{-\Omega(\epsilon^2(n-k))}$:*
$$F(A) \ge (1 - \epsilon) \max_{B:|B|=k} F(B).$$

### 4.2 An Approximation Algorithm for Very Small $k$

**Approximation guarantee in expectation.** The algorithm will simply select the set $\hat{A}$ to be a random set of $k$ elements from a random set of $\mathcal{H}(A)$ where $A \in \arg\max_{B:|B|=k} \tilde{F}(B)$. For any constant $k$ and any fixed $\epsilon > 0$ this is a $(k/(k + 1) - \epsilon)$ approximation in *expectation*.

**High probability.** To obtain a result that holds w.h.p. we will consider a modest variant of the algorithm above. The algorithm enumerates all possible subsets of size $k - 1$, and identifies the set $A \in \arg\max_{B:|B|=k-1} \tilde{F}(B)$. The algorithm then returns $\hat{A} \in \arg\max_{X \in \mathcal{H}(A)} \tilde{f}(X)$.

**Theorem 4.2.** *For any submodular function $f : 2^N \to \mathbb{R}$ and any fixed $\epsilon > 0$ and constant $k$, there is a $(1 - 1/k - \epsilon)$-approximation algorithm for $\max_{S:|S|\le k} f(S)$ which only uses a generalized exponential tail noisy oracle, and succeeds with probability at least $1 - 6/\log n$.*

### 4.3 Information Theoretic Lower Bounds for Constant $k$

Surprisingly, even for $k = 1$ no algorithm can obtain an approximation better than $1/2$, which proves a separation between large and small $k$. In Claim D.2 we show no randomized algorithm with a noisy oracle can obtain an approximation better than $1/2 + O(1/\sqrt{n})$ for $\max_{a \in N} f(a)$, and in Claim D.3 approximation better than $(2k - 1)/2k + O(1/\sqrt{n})$ for the optimal set of size $k$.

---

## 5 Extensions

In this section we consider extensions of the optimization under noise model. In particular, we show that the algorithms can be applied to several related problems: additive noise, marginal noise, correlated noise, degradation of information, and approximate submodularity.

### 5.1 Additive Noise

Throughout this paper we assumed the noise is multiplicative, i.e. we defined the noisy oracle to return $\tilde{f}(S) = \xi_S \cdot f(S)$. An alternative model is one where the noise is *additive*, i.e. $\tilde{f}(S) = f(S) + \xi_S$, where $\xi_S \sim \mathcal{D}$. The impossibility results for adversarial noise apply to the additive case as well.

From a modeling perspective, the fact that the noise may be independent of the value of the set queried may be an advantage or a disadvantage, depending on the setting. From a technical perspective, the problem remains non-trivial. Fortunately, all the algorithms described above apply to the additive noise model, modulo the smoothing arguments which become straightforward. That is, we still need to apply smoothing on the surrogate functions, but it is easy to show arguments like $A \in \arg\max_B \tilde{F}(S \cup B)$ implies w.h.p. $F_S(A) \ge (1 - \delta) \max_b F_S(B)$. In the additive noise model:
$$\tilde{F}(S \cup A) = \sum_{X \in \mathcal{H}(A)} \tilde{f}(S \cup X) = \sum_{X \in \mathcal{H}(A)} (f(S \cup X) + \xi_{S \cup X}) = \sum_{X \in \mathcal{H}(A)} f(S \cup X) + \sum_{X \in \mathcal{H}(X)} \xi_{S \cup X}$$

Thus, by applying a concentration bound we can show that a set $A$ whose smooth value is maximal implies that its non-noisy smooth marginal contribution $F_S(A)$ is approximately maximal as well.

### 5.2 Marginal Noise

An alternative noise model is one where the noise acts on the marginals of the distribution. In this model, a query to the oracle is a pair of sets $S, T \subseteq N$ and the oracle returns $\xi_{S, T} \cdot f_S(T)$ in the *multiplicative marginal noise* model and $f_S(T) + \xi_{S, T}$ in the *additive marginal noise* model.

**Adversarial additive marginal noise is generally impossible.** If the error is adversarial, and the noise is additive, the lower bound of 6.1 follows for any magnitude of the noise. Letting $\epsilon$ denote the maximal magnitude of the noise, we consider a function in which no element ever gives a contribution higher than $\epsilon$, and then getting marginal information does not help.

**Adversarial multiplicative marginal noise is approximable.** If the marginal error is adversarial but multiplicative within factor $\alpha$, it is well known one can obtain a $1 - 1/e^\alpha$ approximation.

**Marginal i.i.d noise is approximable.** If one is allowed to query the oracle on any two sets $S, T$ and get $\xi_{S, T} \cdot f_S(T)$ (or $f_S(T) + \xi_{S, T}$) where $\xi_{S, T}$ is drawn i.i.d for any pair $S, T$, then one can simply apply all the algorithms and analysis as is, by always considering $f_\emptyset(S \cup T)$. If one is only allowed to query $S, T$ where $|T| = 1$, the algorithms still work, but we need to be careful with the analysis, since we need to show that we are calling the oracle on different sets. It is easy to show that if the noise is weak and multiplicative (e.g. $\xi \in [1-\epsilon, 1+\epsilon]$) we can obtain a $(1 - 1/e - \epsilon)$ approximation.

### 5.3 Correlated Noise

As discussed in the Introduction, Theorem 6.1 implies that no algorithm can optimize a monotone submodular function under a cardinality constraint given access to a noisy oracle whose noise multipliers are arbitrarily correlated across sets, even when the support of the distribution is arbitrarily small. In light of this, one may wish to consider special cases of correlated distributions. We first show that even very simple correlations can result in inapproximability. We then show an interesting class of distributions we call $d$-*correlated*, for which optimal guarantees are obtainable.

**Impossibility result for correlated distributions.** Having taken the first step showing algorithms for the i.i.d. in space model, a natural question is whether this assumption is necessary.

**Theorem 5.1.** *Even for unit demand functions there are simple space-correlated distributions for which no algorithm can achieve an approximation strictly better than $1/n$.*

*Proof.* Consider a unit demand function $f(S) = \max_{a \in S} f(a)$ which operates on a ground set with $n$ elements. There are $n - 1$ *regular* elements and one *special* element $a^*$. The value of $f$ on any regular element is $1$, but $f(a^*) = M$ for some arbitrarily large $M$. The noise distribution is such that it returns $1$ on sets which do not contain $a^*$, and $1/M$ on sets that contain $a^*$. The best one can do in this case is to choose a random element without querying the oracle at all. ◻

**Guarantees for $d$-correlated distributions.** Our algorithms can be extended to a model in which querying similar sets may return results that are arbitrarily correlated, as long as querying sets which are sufficiently far from each other gives independent answers.

**Definition.** *We say that the noise distribution is **$d$-correlated** if for any two sets $S$ and $T$, such that $|S \setminus T| + |T \setminus S| > d$ we have that the noise is applied independently to $S$ and to $T$.*

Notice that if a distribution is $d$-correlated, any two points on the hypercube at distance at most $d$ can be arbitrarily correlated. For this model we show that when $k \in \Omega(\log \log n)$ then we can obtain an approximation arbitrarily close to $1 - 1/e$ for $O(\sqrt{k})$-correlated distributions. Alternatively, in this regime we can get this approximation guarantee for any distribution that is arbitrarily correlated when querying two sets $S, T$ whose symmetric difference is larger than $\sqrt{\max\{|T|, |S|\}}$. When $k \in \Omega(\log \log n)$ we can get arbitrarily close to $1 - 1/e$ for $O(1)$-correlated noise.

**Modification of algorithms for large $k$ for $\sqrt{k}$-correlated noise.** For large $k$, if we have that $k \gg d^2$, then the approximation guarantee we get is still arbitrarily close to $1 - 1/e$ even when $\mathcal{D}$ is $d$-correlated. To do this, we modify the smoothing neighborhood and the definition of smooth values as follows. Recall that in SMOOTH-GREEDY, we select an arbitrary set of elements $H$ of size $\ell$ for smoothing, and compute the noisy smooth value of $S \cup a$ by averaging all subsets of $H$:
$$\tilde{F}(S \cup a) = \frac{1}{2^\ell} \sum_{H' \subset H} \tilde{f}\Big(S \cup (a \cup H')\Big).$$

In the $d$-correlated case, for each $1 \le i \le d$ and $1 \le j \le \ell$ we choose a bundle $h(i)_j$ of $d$ elements, such that every two bundles are disjoint. Denote $H(i) = \{h(i)_1, \dots h(i)_\ell\}$, and $H = \bigcup_{i, j} h(i)_j$ the set of all elements we used. The noisy smooth value with smoothing set $H(i)$ is now:
$$\tilde{F}^{(i)}(S \cup a) = \frac{1}{2^\ell} \sum_{H' \subset H(i)} \tilde{f}(S \cup a \cup H')$$
where we abuse notation and use $S \cup a \cup H'$ instead of $S \cup \{a\} \cup_{h(i)_j \in H'} h(i)_j$.

We will run SMOOTH-GREEDY with the smoothing sets $H(1), \dots, H(d)$, where in each iteration $i \pmod d$ we use $H(i)$ as the smoothing set. Exactly as in the original algorithm, we generate $S$ by iteratively adding $k - |H|$ elements from $N \setminus H$ that maximize the smooth value in every iteration, and we then return $S \cup H$. As before, SLICK-GREEDY employs SMOOTH-GREEDY.

To prove correctness of the algorithm we need to show that the evaluations of the surrogate functions are independent. We will first show by induction on $|S|$ that between iterations, the oracle calls are independent.

**Claim 5.2.** *Any oracle call at iteration $i$ is independent of any previous oracle call at iteration $r < i$.*

*Proof.* Let $S(i)$ be the set of elements we have already committed to in stage $i$. Consider an evaluation of $\tilde{f}(S(i) \cup a \cup H')$ for some non empty $H' \subset H(i \pmod d)$ at iteration $i$, and an oracle evaluation $\tilde{f}(S(r) \cup b \cup H'')$ made at some iteration $r < s$ with some non empty $H'' \subset H(r \pmod d)$ and $b \notin S(r) \cup H$. If $r \le i - d$, then the symmetric difference between $S(i) \cup a$ and $S(r) \cup b$ is at least of size $d$. Since $a, b \notin H$, and $S(i) \cap H = \emptyset$, this means that the symmetric difference of $S(i) \cup a \cup H'$ and $S(r) \cup b \cup H''$ is at least of size $d$, for any $H'' \subset H(r \pmod d)$, and thus the calls are independent. If $r > s - d$, then $i \pmod d \neq r \pmod d$, and hence $S(i) \cup a \cup H'$ and $S(r) \cup b \cup H''$ are independent because of the symmetric difference between $H'$ and $H''$. ◻

**Claim 5.3.** *When evaluating $\tilde{F}^{(i)}(S \cup a)$, all noise multipliers are independent.*

*Proof.* When evaluating $\tilde{F}^{(i)}(S \cup a)$ we call the noisy oracle on sets of the form $S \cup a \cup H'$. Since each $H'$ corresponds to a different subset of $H(i)$, and $H(i)$ is a collection of $\ell$ bundles of size $d$, the symmetric difference between every two sets $H', H'' \subseteq H(i)$, is at least $d$. ◻

As in the original SMOOTH-GREEDY procedure, we can show that at every iteration, when $S$ is the set of elements we selected in previous iterations, an element $a$ added to $S$ implies that w.h.p. $F(S \cup a)$ is arbitrarily close to $\max_{b \notin H} F(S \cup b)$ (see Claim 5.3). Let $a_1, a_2, \dots a_{n - |S| - |H|}$ denote the elements which are being considered. For each element $a_i$, we have that if $F(S \cup a_i)$ is non negligible then w.h.p $\tilde{F}(S \cup a_i)$ approximates $F(S \cup a_i)$, and if $F(S \cup a_i)$ is negligible then so is $\tilde{F}(S \cup a_i)$. While for $a_i, a_j$ these events may well be correlated, since the probability of failure is inverse polynomially small and there are only $n - |S| - |H|$ events, we can take a union bound and say that with high probability for every $i$ if $F(S \cup a_i)$ is negligible so is $\tilde{F}(S \cup a_i)$, and if $F(S \cup a_i)$ is non negligible then it is well approximated by $\tilde{F}(S \cup a_i)$.

Thus, we know that at every iteration $i$ when $S$ is the set of elements selected in previous iterations, we have selected the element $a$ that is arbitrarily close to $\max_{b \notin H} F^{(i)}(S \cup b)$. From the arguments in the paper we know that this implies that for an arbitrarily small $\gamma > 0$ we have:
$$f_S(a) \ge (1 - \gamma) f_{S \cup H(i)}(b) \ge (1 - \gamma) f_{S \cup H}(b)$$

where the right inequality is due to submodularity and the fact that $H(i) \subseteq H$. The guarantees of SMOOTH-GREEDY therefore apply in this case as well. What remains to show is that SLICK-GREEDY is unaffected by this modification. This is easy to verify as SLICK-GREEDY takes $1/\delta$ disjoint sets $H_1, \dots, H_{1/\delta}$, and the arguments discussed apply for every such set. Since we apply SMOOTH-COMPARE $1/\delta$ times with sets of size $\ell$ it is easy to implement as well.

**Modification of algorithms for small $k$ for $O(1)$-correlated noise.** A similar idea works also for the small $k$ case, assuming $d$ is constant. In this case, we add $c \gg d/\epsilon$ elements at each phase of the algorithm. We modify the definition of $\tilde{F}$ in the following way. First we take an arbitrary partition $P_1, \dots P_{(n-|S|)/d}$ on the elements not in $S$, in which each $P_i$ is of size $d$, and a partition $Q_1 \dots Q_{(|S|+|A|)/d}$ of the elements in $S \cup A$. We estimate the value of a set $A$ given $S$ using:
$$\tilde{F}(S \cup A) = \frac{d^2}{(|S| + |A|)(|N| - |S| - |A|)} \sum_{Q_i \in A} \sum_{P_j} \tilde{f}(((S \cup A) \setminus Q_i) \cup P_j)$$
and modify the rest of the algorithm accordingly.

Correctness relies on three steps:
1.  First, when we are in iteration $i$ of the algorithm (after we already added $(i - 1)c$ elements to $S$), all the sets we apply the oracle on are of size $c \cdot i$, and hence they are independent of any set of size $c(i - 1)$ or less which were used in previous phases;
2.  Second, when we evaluate $\tilde{F}(S \cup A)$ for a specific set $A$, we only use sets which are independent in the comparison. Here we rely on changing $d$ elements in $A$ each time, and replacing them by another set of $d$ elements;
3.  Finally, we treat each set $A$ separately, and show that if its marginal contribution is negligible then w.h.p its mean smooth value is not too large, and if its marginal contribution is not negligible, then w.h.p. $\tilde{F}(S \cup A)$ approximates $F(S \cup A)$ well. Taking a union bound over all the bad events we get that the set $A$ chosen has large (non-noisy) smooth mean value.

### 5.4 Information Degradation

We have written the paper as if the algorithm gains no additional information for querying a point twice. The generalization to a case where the algorithm gets more information each time but there is a degradation of information is simple: whenever the algorithms we presented here want to query a point just query it multiple times, and feed the expected value of the point given all the information one has to the algorithm. Hence it makes sense to focus on the extreme case where only the first query is helpful, as common in the literature of noisy optimization (e.g. [12]).

### 5.5 Approximate Submodularity

In this paper our goal is to obtain near optimal guarantees as defined on the original function that was distorted through noise. That is, we assume that there is an underlying submodular function which we aim to optimize, and we only get to observe noisy samples of it. An alternative direction would be to consider the problem of optimizing functions that are *approximately* submodular:
$$\max_{S:|S|\le k} \tilde{f}(S)$$

The notion of approximate submodularity has been studied in machine learning [67, 23, 22, 33]. More generally, given the desirable guarantees of submodular functions, it is interesting to understand the limits of efficient optimization with respect to the function classes we aim to optimize.

**Impossibility for $\epsilon$-adversarial approximation.** If we assume that the function is an adversarial $(1 \pm \epsilon)$ approximation of a submodular function, our lower bound from Section 6 for erroneous oracles implies that no polynomial time algorithm can obtain a non-trivial approximation.

**Trivial reduction for noise in $[1-\epsilon, 1+\epsilon]$.** When $\mathcal{D} \subseteq [1-\epsilon, 1+\epsilon]$, and the noise is i.i.d across sets, the algorithms in the paper obtain a solution arbitrarily close to $\left( \frac{1-\epsilon}{1+\epsilon} \right) \left( 1 - \frac{1}{e} \right)$ of $\max_{S:|S|\le k} \tilde{f}(S)$.

**Impossibility for unbounded noise.** If we assume that a noisy process of a distribution with unbounded support altered a submodular function, then there are trivial impossibility results. Suppose that the initial submodular function is the constant function that gives $1$ to every set. If we apply (e.g.) Gaussian noise to it, then the optimal algorithm is just to try random sets and hope for the best, and no polynomial time algorithm can achieve a constant factor approximation.

**Optimal approximation via black-box reduction.** First, note that there is an algorithm which runs in time $n^k$ and finds the optimal subset of size $k$: query $\tilde{f}$ on all subsets of size at most $k$, and choose the maximal one. Notice that this is in contrast to the setting we study throughout the paper in which there is a lower bound of $(2k - 1)/2k + O(1/\sqrt{n})$. The interesting regime is $k = \omega(1)$, where there is a black-box reduction from the problem of maximizing a submodular function given an approximately submodular function, to the problem of maximizing an approximately submodular function. Since we can solve the original problem within a factor arbitrarily close to $1 - 1/e$ we get an optimal approximation guarantee in this case as well. Let $\max \mathcal{D}(t) = \mathbb{E}[\max_{\xi_1, \dots \xi_t \sim \mathcal{D}} \{\xi_1, \dots, \xi_t\}]$ be the expected maximum value of $t$ i.i.d samples of $\mathcal{D}$.

**Lemma 5.4.** *An algorithm which uses $t \le \binom{n}{k}$ queries to $\tilde{f}$ cannot achieve approximation ratio better than:*
$$\frac{\max \mathcal{D}(t)}{\max \mathcal{D}(\binom{n}{k})}.$$

*Proof.* Suppose that $f(S) = 1$ for every set $S$. The best that the algorithm can do is query $t$ sets with at most $k$ elements, and output the maximal one. The approximation ratio of this is exactly
$$\frac{\max \mathcal{D}(t)}{\max \mathcal{D}(\binom{n}{k})}$$
If the algorithm queries sets with more than $k$ elements, the approximation would deteriorate. ◻

**Lemma 5.5.** *Suppose there exists an algorithm which given $k \in \omega(1)$ returns a solution $S$ s.t. $f(S) \ge \gamma \max_{T:|T|\le k} f(T)$ using $q$ queries to a noisy oracle. Then, for any $t \in \text{poly}(n)$ there is an algorithm that uses $q + t$ to a noisy oracle and returns a solution $S'$ s.t.:*
$$\tilde{f}(S') \ge \Big(\gamma - o(1)\Big) \left(\frac{\max \mathcal{D}(t)}{\max \mathcal{D}(\binom{n}{k})}\right) \max_{T:|T|\le k} \tilde{f}(T).$$

*Proof.* Let $r$ be such that $\binom{n-k}{r} \ge t$. Since $t$ is polynomial in $n$, we have that $r$ is constant. Run the algorithm to obtain a set $G$ of size $k - r$. From submodularity and the fact that $r$ is constant:
$$f(G) \ge \gamma \max_{S:|S|\le k-r} f(S) \ge (1 - r/k)\gamma \max_{S:|S|\le k} f(S) \ge (1 - o(1))\gamma \max_{S:|S|\le k} f(S)$$

For every set of $r$ elements $\{x_1, \dots, x_r\}$ where $x_i \notin G$, the algorithm queries $\tilde{f}$ on $G \cup \{x_1, \dots x_r\}$, and chooses the set with maximum value. It is easy to see that the expected value of this set would be at least $\max \mathcal{D}(t)(1 - r/k)\gamma \max_{S:|S|\le k} f(S)$, which gives the ratio. ◻

---

## 6 Impossibility for Adversarial Noise

In this section we show that there are very simple submodular functions for which no randomized algorithm with access to an $\epsilon$-erroneous oracle can obtain a reasonable approximation guarantee with a subexponential number of queries to the oracle. Intuitively, the main idea behind this result is to show that a noisy oracle can make it difficult to distinguish between two functions whose values can be very far from one another. The functions we use are similar to those used to prove information theoretic lower bounds for submodular optimization and learning [79, 84, 36, 8, 95].

**Theorem 6.1.** *No randomized algorithm can obtain an approximation strictly better than $O(n^{-1/2+\delta})$ to maximizing monotone submodular functions under a cardinality constraint using $e^{n^\delta}/n$ queries to an $\epsilon$-erroneous oracle, for any fixed $\epsilon, \delta < 1/2$.*

*Proof.* We will consider the problem of $\max_{S:|S|\le k} f(S)$ where $k = n^{1/2+\delta}$. Let $X \subseteq N$ be a random set constructed by including every element from $N$ with probability $n^{-1/2+\delta}$. We will use this set to construct two functions that are close in expectation but whose maxima have a large gap, and show that access to a noisy oracle implies distinguishing between these two functions. The functions are:

*   $f_1(S) = \min \left\{ |S \cap X| \cdot n^{1/2} + \frac{n^{1/2+\delta}}{\epsilon}, |S| \cdot n^{1+\delta} \right\}$
*   $f_2(S) = \min \left\{ |S| \cdot n^\delta + \frac{n^{1/2+\delta}}{\epsilon}, |S| \cdot n^{1+\delta} \right\}$

Notice that both functions are normalized monotone submodular: when $S = \emptyset$ both functions evaluate to $0$, and otherwise are affine. By the Chernoff bound we know that $|X| \ge n^{1/2+\delta}/2$ with probability $1 - e^{-\Omega(n^{1/2+\delta})}$. Conditioned on this event we have that $\max_{S:|S|\le k} f_1(S) = f_1(X) \in O(n^{1+\delta})$ whereas $f_2$ is symmetric and $\max_{S:|S|\le k} f_2(S) \in O(n^{1/2+2\delta})$. Thus, an inability to distinguish between these two functions implies there is no approximation algorithm with approximation better than $O(n^{-1/2+\delta})$. We define the erroneous oracle as follows. If the function is $f_2$, its oracle returns the exact same value as $f_2$ for any given set. Otherwise, the function is $f_1$ and its erroneous oracle is defined as:
$$\tilde{f}(S) = 
\begin{cases}
f_2(S), & \text{if } (1 - \epsilon)f_1(S) \le f_2(S) \le (1 + \epsilon)f_1(S) \\
f_1(S) & \text{otherwise}
\end{cases}$$
Notice that this oracle is $\epsilon$-erroneous, by definition.

Suppose now that the set $X$ is unknown to the algorithm, and the objective is $\max_{S:|S|\le k} f_1(S)$. We will first show that no deterministic algorithm that uses a single query to the erroneous oracle $\tilde{f}$ can distinguish between $f_1$ and $f_2$, with exponentially high probability (equivalently, we will show that a single query to the algorithm cannot find a set $S$ for which $f_1(S) < (1 - \epsilon)f_2(S)$ or $f_1(S) > (1 + \epsilon)f_2(S)$ with exponentially high probability). For a single query algorithm, we can imagine that the set $X$ is chosen after the algorithm chooses which query to invoke, and compute the success probability over the choice of $X$. In this case, all the elements are symmetric, and the function value is only determined by the size of the set that the single-query algorithm queries.

In case the query is a set $S$ of cardinality smaller or equal to $n^{1/2}$, by the Chernoff bound we have that $|S \cap X| \le (1 + \beta)n^\delta$ for any $\beta < 1$ with probability at least $1 - e^{-\Omega(\beta^2 n^\delta)}$. Thus:
$$\frac{n^{1/2+\delta}}{\epsilon} \le f_1(S) \le \left(1 + \beta + \frac{1}{\epsilon}\right) n^{1/2+\delta}$$
$$\frac{n^{1/2+\delta}}{\epsilon} \le f_2(S) \le \left(1 + \frac{1}{\epsilon}\right) n^{1/2+\delta}$$

It is easy to verify that for $\beta < \epsilon/(1-\epsilon)$: $(1 - \epsilon)f_1(S) \le f_2(S) \le (1 + \epsilon)f_1(S)$. Thus, for any query of size less or equal to $n^{1/2}$ the likelihood of the oracle returning $f_1$ is $1 - e^{-\Omega(n^\delta)}$.

In case the oracle queries a set of size greater than $n^{1/2}$ then again by the Chernoff bound, for any $\beta < 1$ we have that with probability at least $1 - e^{-\Omega(\beta^2 n^{1/2})}$:
$$\left(1 - \beta\right) \frac{|S|}{n^{1/2-\delta}} \le |S \cap X| \le \left(1 + \beta\right) \frac{|S|}{n^{1/2-\delta}}$$

For $\beta \le \epsilon/(1 - \epsilon)$, this implies that:
$$(1 - \epsilon)f_1(S) \le f_2(S) \le (1 + \epsilon)f_1(S)$$

Therefore, for any fixed $\epsilon \in (0, 1)$, the algorithm cannot distinguish between $f_1$ and $f_2$ with probability $1 - e^{-\Omega(n^\delta)}$ by querying the erroneous oracle with a set larger than $n^{1/2}$. To conclude, by a union bound we get that with probability $1 - e^{-\Omega(n^\delta)}$ no algorithm can distinguish between $f_1$ and $f_2$ using a single query to the erroneous oracle, and the ratio between their maxima is $O(n^{1/2-\delta})$.

To complete the proof, suppose we had an algorithm running in time $e^{n^\delta}/n$ which can approximate the value of a submodular function, given access to an $\epsilon$-erroneous oracle with approximation ratio strictly better than $O(n^{-1/2+\delta})$ which succeeds with probability $2/3$. This would let us solve the following decision problem: *Given access to an $\epsilon$-erroneous oracle for either $f_1$ or $f_2$, determine which function is being queried*. To solve the decision problem, given access to an erroneous oracle of unknown function, we would use the hypothetical approximation algorithm to estimate the value of the maximal set of size $n^{1/2+\delta}$. If this value is strictly more than $n^{1/2+2\delta}$, the function is $f_1$ (since $f_1(X) = O(n^{1+\delta})$), and otherwise it is $f_2$.

The reduction allows us to show that distinguishing between the functions in time $e^{n^\delta}/n$ and success probability $2/3$ is impossible. For purpose of contradiction, suppose that there is a (randomized) algorithm for the decision problem, and let $p$ denote the probability that it outputs $f_2$ if it sees an oracle which is fully consistent with $f_2$. To succeed with probability $2/3$, it must be the case that whenever the algorithm gets $f_1$ as an input, it finds a set $S$ for which the noisy oracle returns $f_1(S)$ with probability at least $2/3 - p/2 \ge 1/6$. Whenever it finds such a set, the algorithm is done, since it can compute $f_2(S)$ without calling the oracle, and hence it knows that $f_1$ was chosen in the decision problem.

In this case, we know that the algorithm makes up to $e^{n^\delta}/n$ queries, until it sees a set for which it gets $f_1(S)$. But this means that there is an algorithm with success probability at least $O(n/6 e^{n^\delta})$ that makes a single query. This algorithm guesses some index $i < e^{n^\delta}/n$, and simulates the original algorithm for $i - 1$ steps (by feeding it with $f_2$ without using the oracle), and then using the oracle in step $i$. If the algorithm guesses $i$ to be the first index in which the exponential time algorithm sees $f_1(S)$, then the single query algorithm would succeed. Hence, since we showed that no single query (randomized) algorithm can find a set $S$ such that $f_1(S) < (1-\epsilon)f_2(S)$ or $f_1(S) > (1+\epsilon)f_2(S)$ with just one query this concludes the proof. ◻

The following remarks are worth mentioning:

*   The functions we used in the lower bound are very simple examples of coverage functions;
*   If one does not require the function to be normalized, then the lower bound holds for affine functions, i.e. $f(S) = \sum_{a \in S} f(a) + C$, where $C$ independent of $S$;
*   The lower bound is tight: for any $\epsilon$-erroneous oracle there is a $\frac{1-\epsilon}{1+\epsilon} \cdot \max\{n^{-1/2}, 1/k\}$ approximation by simply partitioning the ground sets to arbitrary sets of size $\min\{\sqrt{n}, k\}$, and select the set whose value according to the erroneous oracle is maximal;
*   The lower bound applies to additive noise by simply applying an additive version of the Chernoff bound.

Somewhat surprisingly, the above theorem suggests that a good approximation to a submodular function does not suffice to obtain reasonable approximation guarantees. In particular, guarantees from learning or sketching where the goal is to approximate a submodular function up to constant factors may not necessarily be meaningful for optimization. It is important to note that for some classes of submodular functions such as additive functions ($f(S) = \sum_{a \in S} f(a)$), we can obtain algorithms that are robust to adversarial noise. A very interesting open question is to characterize the class of submodular functions that are robust to adversarial noise.

---

## 7 More related work

**Submodular optimization.** Maximizing monotone submodular functions under cardinality and matroid constraints is heavily studied. The seminal works of [80, 46] show that the greedy algorithm gives a factor of $1-1/e$ for maximizing a submodular function under a cardinality constraint and a factor $1/2$ approximation for matroid constraints. For max-cover which is a special case of maximizing a submodular function under a cardinality constraint, Feige shows that no poly-time algorithm can obtain an approximation better than $1-1/e$ unless P=NP [35]. Vondrak presented the continuous greedy algorithm which gives a $1 - 1/e$ ratio for maximizing a monotone submodular function under matroid constraints [94]. This is optimal, also in the value oracle model [79, 61, 81]. It is interesting to note that with a demand oracle the approximation ratio is strictly better than $1 - 1/e$ [39]. When the function is not monotone, constant factor approximation algorithms are known to be obtainable as well [37, 73, 14, 15]. In general, in the past decade there has been a development in the theory of submodular optimization, through concave relaxations [1, 19], the multilinear relaxation [18, 94, 20], and general rounding technique frameworks [96]. In this paper, the techniques we develop arise from first principles: we only rely on basic properties of submodular functions, concentration bounds, and the algorithms are variants of the standard greedy algorithm.

**Submodular optimization in game theory.** Submodular functions have been studied in game theory almost fifty years ago [90]. In mechanism design submodular functions are used to model agents' valuations [74] and have been extensively studied in the context of combinatorial auctions (e.g. [27, 28, 26, 79, 16, 25, 83, 32, 29]). Maximizing submodular functions under cardinality constraints have been studied in the context of combinatorial public projects [84, 87, 17, 78] where the focus is on showing the computational hardness associated with not knowing agents valuations and having to resort to incentive compatible algorithms. Our adversarial lower bound implies that if agents err in their valuations, optimization may be hard, regardless of incentive constraints.

**Submodular optimization in machine learning.** In the past decade submodular optimization has become a central tool in machine learning and data mining (see surveys [65, 66, 11]). Problems include identifying influencers in social networks [59, 86] sensor placement [75, 50], learning in data streams [92, 52, 71, 5], information summarization [76, 77], adaptive learning [51], vision [58, 57, 63], and general inference methods [64, 57, 24]. In many cases the submodular function is learned from data, and our work aims to address the case in which there is potential for noise in the model.

**Learning submodular functions.** One of the main motivations we had for studying optimization under noise is to understand whether submodular functions that are learned from data can be optimized well. The standard framework in the literature for learning set functions is *Probably Mostly Approximately Correct* (`PMAC`) learnability due to Balcan and Harvey [9]. This framework nicely generalizes Valiant's notion of *Probably Approximately Correct* (`PAC`) learnability [93]. Informally, PMAC-learnability guarantees that after observing polynomially-many samples of sets and their function values, one can construct a surrogate function that is with constant probability over the distributions generating the samples, likely to be an approximation of the submodular function generating the data. Since the seminal paper of Balcan and Harvey there has been a great deal of work on learnability of submodular functions [41, 7, 4, 43, 45, 6]. As discussed in the paper, our lower bounds imply that one cannot optimize the surrogate function `PMAC` learned from data. If the approximation is via i.i.d noise on sets sufficiently far, this may be possible.

**Approximate submodularity.** The concept of approximate submodularity has been studied in machine learning for dictionary selection and feature selection in linear regression [67, 23, 22, 33]. Generally speaking, this line of work considers approximate submodularity by defining a notion of the *submodularity ratio* of a function, defined in terms of how close it is to have a diminishing returns property. This ratio depends on the instance, which in the worst-case may result in a function that poorly approximates a submodular function. In practice however, these works show that in a broad range of applications the functions of interest are sufficiently close to submodular. Recently, the notion of approximate *modularity* (i.e. additivity) has been studied in [21] which give an optimal algorithm for approximating an approximately modular function via a modular function. These notions of approximate modularity and approximate submodularity are the model in which we have noise on the marginals. As discussed in Section 5, if the error on the marginals is adversarial, there are regimes in which non-trivial guarantees are impossible. If one assumes the marginal approximations are i.i.d our positive results apply.

**Combinatorial optimization under noise.** Combinatorial optimization with noisy inputs can be largely studied through consistent (independent noisy answers when querying the oracle twice) and inconsistent oracles. For inconsistent oracles, it usually suffices to repeat every query $O(\log n)$ times, and eliminate the noise. To the best of our knowledge, submodular optimization has been studied under noise only in instances where the oracle is inconsistent or equivalently small enough so that it does not affect the optimization [59, 68]. One line of work studies methods for reducing the number of samples required for optimization (see e.g. [38, 10]), primarily for sorting and finding elements. On the other hand, if two identical queries to the oracle always yield the same result, the noise can not be averaged out so easily, and one needs to settle for approximate solutions, which has been studied in the context of tournaments and rankings [60, 12, 2].

**Convex optimization under noise.** Maximizing functions under noise is also an important topic in convex optimization. The analogue of our model here is one where there is a zeroth-order noisy oracle to a convex function. As discussed in the paper, the question of polynomial-time algorithms for noisy convex optimization is straightforward and the work in this area largely aims at improving the convergence rate [34, 47, 62, 72, 85].

---

## 8 Acknowledgements

A.H. was supported by ISF 1241/12; Y.S. was supported by NSF grant CCF-1301976, CAREER CCF-1452961, a Google Faculty Research Award, and a Facebook Faculty Gift. We thank Vitaly Feldman who pointed out the application to active learning. We are deeply indebted to Lior Seeman, who has carefully read previous versions of the manuscript and made multiple invaluable suggestions.
