```markdown
# RRaPINNs: Residual Risk-Aware Physics Informed Neural Networks

Ange-Clement Akazan´  
1,2, Issa Karambal 2, Jean Medard Ngnotchouye1, and Abebe Geletu Selassie. W3

1University of KwaZulu Natal  
2AIMS Research and Innovation Centre  
3AIMS Rwanda

November 25, 2025

## Abstract

Physics-informed neural networks (PINNs) typically minimize average residuals, which can conceal large, localized errors. We propose Residual Risk-Aware PINNs (RRaPINNs), a single-network framework that optimizes tail-focused objectives using Conditional Value-at-Risk (CVaR), we also introduced a Mean-Excess (ME) surrogate penalty to directly control worst-case PDE residuals. This casts PINN training as risk-sensitive optimization and links it to chance-constrained formulations. The method is effective and simple to implement. Across several partial differential equations (PDEs) such as Burgers, Heat, Korteweg-de-Vries, and Poisson (including a Poisson interface problem with a source jump at $x=0.5$) equations, RRaPINNs reduce tail residuals while maintaining or improving mean errors compared to vanilla PINNs, Residual-Based Attention and its variant using convolution weighting; the ME surrogate yields smoother optimization than a direct CVaR hinge. The chance constraint reliability level $\alpha$ acts as a transparent knob trading bulk accuracy (lower $\alpha$) for stricter tail control (higher $\alpha$). We discuss the framework limitations, including memoryless sampling, global-only tail budgeting, and residual-centric risk, and outline remedies via persistent hard-point replay, local risk budgets, and multi-objective risk over BC/IC terms. RRaPINNs offer a practical path to reliability-aware scientific ML for both smooth and discontinuous PDEs.

## 1 Introduction

Physics-Informed Neural Networks (PINNs), a framework introduced by [Lagaris et al., 1998] and later on improved by [Raissi et al., 2019], have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding physical laws into neural network training. By replacing or augmenting data-driven losses with PDE residuals and boundary/initial conditions, PINNs provide a mesh-free framework for scientific machine learning, with demonstrated success across fluid dynamics, elasticity, and transport phenomena Karniadakis et al. [2021].

However, as first demonstrated by Rahaman et al. [2019], neural networks inherently learn low-frequency functions (the smooth, easy parts of a solution) far more quickly than high-frequency functions (sharp gradients, shocks, or singularities). The classical PINN formulation, which minimizes the mean-squared residual, exacerbates this problem. The optimizer rapidly reduces the low-frequency error across the bulk of the domain, causing the global average loss to drop. This averaging obscures the localized failures in high-frequency regions, leading to a false sense of convergence while the solution at these critical points remains catastrophically wrong [Wang and Zhang, 2022, Luo et al., 2025]. Moreover, ill-conditioned physics-informed losses, can also yield highly unbalanced gradient signals across the domain [Rahaman et al., 2019, Wang et al., 2021]. Together, these often lead non-Gaussian, heavy-tailed residual distribution, where the standard MSE loss is no longer a statistically robust or meaningful objective. Such failure modes undermine the reliability of PINNs, especially in safety-critical domains.

Adaptive weighting schemes have been proposed to mitigate this pathology. These include balancing PDE vs. boundary losses [McClenny and Braga-Neto, 2020], gradient norm balancing [Wang et al., 2021], adaptive sampling of collocation points [Lu et al., 2021], and curriculum-based strategies [Yang et al., 2022]. These methods mainly attempt to force the optimizer to pay attention to these high-frequency, high-residual regions. Despite their successes, these approaches remain largely heuristic. What is missing is a systematic, mathematically rigorous framework that directly targets the statistical properties of this heavy-tailed error distribution. Addressing this requires moving beyond simple reweighting toward robust error control. In this work, we propose a framework which formulates the training problem as a probabilistic (chance)-constrained optimization [Charnes and Cooper, 1959]. Rather than minimizing average residuals only, we also enforce a probabilistic constraint on the residual.

$$
P\big(|r(x;\theta)| \le \varepsilon\big) \ge \alpha, \tag{1}
$$

where $r(x;\theta)$ is the PDE residual, $\varepsilon$ a tolerance, and $\alpha$ the desired confidence level (e.g. 95%).

Beyond heuristic reweighting, our view is to re-frame PINN training as a probabilistic (chance)-constrained problem: we require that a large fraction $(\alpha)$ of collocation points meet a at most a residual tolerance $\epsilon$. This formulation naturally induces a quantile-driven objective, targeting the $(1-\alpha)$-quantile (also known as Value-at-Risk or VaR) of the residual distribution. However, quantiles are ill-suited for gradient-based optimization. As a risk measure, VaR is non-coherent; as an objective, it is piecewise-constant, yielding zero gradients almost everywhere and providing sparse, unstable signals to modern optimizers.We therefore turn to Conditional Value-at-Risk (CVaR), the expected loss given that the loss exceeds the VaR. CVaR is a coherent, convex, and smoothly optimizable measure of tail risk [Rockafellar et al., 2000]. Crucially, it provides dense, informative gradients from the entire tail, not just a single point. This perspective is central to modern risk-averse and distributionally robust learning, which use tail-aware objectives to harden models against rare but consequential errors [Namkoong and Duchi, 2017, Duchi et al., 2018]. We bring this risk-averse perspective directly to the physics loss in PINNs, thereby introducing Residual Risk-Aware PINNs (RRaPINNs). In addition to the physics loss, this framework penalizes the positive excess of the residual tail beyond an adaptive tolerance $\epsilon$, allowing the optimizer to explicitly target and shape the worst $(1-\alpha)$ slice of the residual distribution.

To the best of our knowledge, our risk-based formulation is the first to elevate PINN training from heuristic reweighting to a principled, distributionally robust framework that unifies precision with reliability. We motivate and apply coherent risk measures (CVaR) directly to the PDE residual loss to explicitly model and control the upper $(1-\alpha)$ tail of the error distribution. We provide a theoretical derivation showing that this CVaR formulation induces a principled, data-dependent reweighting of residuals. We architect a novel and stable composite-loss framework (RRaPINN). Instead of a naive two-stage switch, we augment the standard MSE base loss with our CVaR-based penalty. To solve the critical problem of loss-scale mismatch, a primary source of instability in high-order PDEs, we introduce a dynamic loss-balancing mechanism. This key adaptively tunes the penalty weight $(\lambda_p)$ using the ratio of detached, exponentially-moving-average (EMA) scales of the base and penalty losses. This ensures a stable, multi-objective optimization of both the average and worst-case residuals without manual tuning. We demonstrate the efficacy of RRaPINN on a comprehensive benchmark of five PDE problems. Our method consistently outperforms Vanilla (baseline) PINNs [Raissi et al., 2019], residual based attention Anagnostopoulos et al. [2024] and convolution weighting PINN [Si and Yan, 2025] in controlling not only the average relative $L_2$ error but also the $L_\infty$ norm and high-percentile residual errors. We provide definitive visual evidence via an empirical Complementary Cumulative Distribution Function (CCDF) plots, which explicitly show our method’s ability to pull in and suppress the extreme tail of the residual distribution.

The remainder of this work is structured as follows: section 2 describes the background of this research, section 3 discusses some of the most important related works. The next section 4 discusses the methodology adopted in this research. Section 5 describes and discusses the experimental results and investigates the impact of the tail size parameter $\alpha$ on accuracy and residual tail control.

## 2 Background

This section provides the background of this research, describing the PINNs initial framework.

### 2.1 PINNs and the Challenge of Adaptive Weighting

**Problem Setup.** Let $\Omega \subset \mathbb{R}^d$ be a spatial domain and $[0,T]$ a time interval. The full spatio-temporal domain is $D = \Omega \times (0,T]$. The boundary is composed of the spatial boundary $\partial \Omega \times [0,T]$ and the initial-time boundary $\Omega \times \{0\}$. We consider a parameterized PDE:

$$
\mathcal{N}[u](x,t) = f(x,t), \quad (x,t)\in D, \tag{2}
$$

subject to boundary conditions $\mathcal{B}$ and initial conditions $\mathcal{I}$:

$$
\mathcal{B}[u](x,t)=g(x,t), \quad (x,t)\in \partial\Omega\times[0,T], \qquad \mathcal{I}[u](x,0)=h(x), \quad x\in\Omega. \tag{3}
$$

A neural network $u_\theta(x,t)$ with parameters $\theta$ is used to approximate the solution $u$. The training objective is defined by minimizing three terms: the PDE residual, the boundary discrepancy, and the initial discrepancy:

$$
r(x,t;\theta):=\mathcal{N}[u_\theta](x,t)-f(x,t), \tag{4}
$$

$$
b(x,t;\theta):=\mathcal{B}[u_\theta](x,t)-g(x,t), \tag{5}
$$

$$
i(x;\theta):=\mathcal{I}[u_\theta](x,0)-h(x). \tag{6}
$$

Let $\mu_r,\mu_b,\mu_i$ be sampling measures on the corresponding domains. The classical (vanilla) PINN objective minimizes the empirical $L_2$ loss over the defined sampling measures:

$$
L_b^{\text{PINN}}(\theta)=\lambda_r L_r(\theta)+\lambda_b L_b(\theta)+\lambda_i L_i(\theta), \tag{7}
$$

where

$$
L_r(\theta)=\frac{1}{N_r}\sum_{j=1}^{N_r} r(x_j^r,t_j^r;\theta)^2,\quad
L_b(\theta)=\frac{1}{N_b}\sum_{j=1}^{N_b} b(x_j^b,t_j^b;\theta)^2,\quad
L_i(\theta)=\frac{1}{N_i}\sum_{j=1}^{N_i} i(x_j^i;\theta)^2. \tag{8}
$$

The static weights $(\lambda_r,\lambda_b,\lambda_i)\in \mathbb{R}_+^3$, are notoriously difficult to tune. A naive choice (e.g., all equal to 1) often leads to failed training due to the pathological nature of the PINN loss landscape. The core issue lies in the disparate gradient magnitudes from each loss term. The residual loss $L_r$, which involves high-order derivatives, often produces gradients that are orders of magnitude stiffer (or vanishingly small) than the simple data-fitting losses $L_b$ and $L_i$. Furthermore, the spectral bias of neural networks [Rahaman et al., 2019] causes the model to rapidly learn low-frequency boundary conditions while struggling to fit the high-frequency components of the PDE residual. This imbalance creates a conflict where one loss term dominates the optimization, leading to a converged model that may satisfy the boundary conditions but violates the governing physics, or vice versa [Wang et al., 2021, 2022]. To alleviate this issue, several adaptive strategies have been proposed, including adaptive weighting, adaptive sampling, and curriculum learning approaches that dynamically redistribute the training effort across loss terms or regions of the domain.

**Figure 1: Computational graph of a standard PINN.** The neural network $u_\theta$ is evaluated at different sets of collocation points and processed through corresponding operators (PDE, BC, IC) to compute distinct loss terms. These terms are weighted (multiplied) and summed to form the final training objective $L_b^{\text{PINN}}$.

## 3 Related Works

This section discusses the main adaptive strategies that dynamically redistribute the training effort across loss terms or regions of the domain.

**Adaptive Weighting Strategies in PINNs** Balancing heterogeneous loss components remains a core challenge in Physics-Informed Neural Networks (PINNs), where PDE residuals, boundary, and initial terms may differ by orders of magnitude Lagaris et al. [1998], Raissi et al. [2019]. Without correction, training often suffers from gradient domination or vanishing updates in certain constraints. The adaptive weighting methods have emerged to address this imbalance. **Gradient-based schemes.** Wang et al. [2021] proposed a GradNorm-inspired attention mechanism that rescales losses based on gradient statistics, enabling the optimizer to emphasize under-trained terms. While effective in early training, such schemes introduce noise sensitivity and require additional tuning to prevent oscillatory reweighting. **NTK-based weighting** Wang et al. [2022] derive the NTK-PINN and show that mismatched NTK spectra across loss components (e.g., PDE residual vs. boundary terms) cause unequal convergence rates. They propose an adaptive scheme that updates the loss coefficients $\{\lambda_i\}$ using spectral information from the corresponding NTK blocks (e.g., traces/eigenvalue magnitudes), so that each component’s error decays at a comparable rate. The approach improves balance but requires computing (or approximating) NTK spectral quantities during training, which limits scalability. **Self-Adaptive Schemes.** McClenny and Braga-Neto [2023] proposed SA-PINNs, where trainable pointwise weights act as soft-attention masks to focus learning on high-residual regions. This joint ascent-descent optimization improves convergence on stiff PDEs and balances loss terms through localized adaptivity. However, the method is sensitive to learning-rate tuning and lacks a principled probabilistic basis, making it largely heuristic despite its clear practical gains. **Residual-based attention.** To bypass gradient computations, Anagnostopoulos et al. [2024] introduced a residual-based attention (RBA) mechanism that adjusts weights as bounded functions of cumulative residuals. RBA accelerates convergence and highlights difficult regions, though its heuristic design lacks explicit guarantees on tail-residual control. **Convolution-weighting Scheme.** More recently, Si and Yan [2025] introduced CWP a method that smooths residuals through local convolutions, enforcing spatial coherence in adaptive weights. This primal-dual formulation mitigates overfitting to isolated points and improves convergence on stiff PDEs. While effective and theoretically grounded, it depends on kernel hyperparameters and may oversmooth sharp features, limiting flexibility in highly nonlocal or discontinuous problems.

**Adaptive Collocation Points Sampling in PINNs.** Adaptive resampling aims to reallocate collocation points toward regions where the PDE residual remains large, thus improving solution fidelity in underresolved or shock regions. Lu et al. [2021] introduced DeepXDE which fosters residual-based refinement, by iteratively adding points with the highest residuals to enhance local accuracy. **Failure-Informed Adaptive Sampling (FI-PINNs).** Gao et al. [2023] proposed the Failure-Informed PINN (FI-PINN), which defines a failure probability as the likelihood that the PDE residual exceeds a user-defined threshold. When this probability surpasses a tolerance, new collocation points are added in the high-residual (failure) region using a self-adaptive importance sampling scheme based on truncated Gaussian proposals. The method provides rare theoretical error bounds for adaptive PINNs and achieves superior accuracy on stiff and high-dimensional PDEs. Its main limitations lie in the need to tune the residual and probability thresholds combined with its reliance on Gaussian assumptions, which may underperform in highly anisotropic or multimodal residual landscapes. Wu et al. [2023] extended the residual-based refinement by formulating sampling as a probability distribution, where each point is drawn with likelihood proportional to its normalized residual magnitude. This probabilistic view avoids redundant sampling and improves efficiency when the sampling budget is limited. More recently, Si and Yan [2025] coupled resampling with convolution-weighted training, using smoothed residuals to guide point updates, thereby ensuring spatial consistency. While these methods significantly improve convergence and robustness, most rely on heuristic thresholds or empirical schedules and lack formal convergence guarantees or uncertainty-aware sampling criteria.

**Curriculum Methods.** Curriculum strategies aim to ease PINN optimization by introducing physical constraints or domain complexity gradually rather than enforcing all conditions simultaneously. In this spirit, Yang et al. [2022] proposed the Curriculum PINN (C-PINN), where training begins with simpler tasks, such as satisfying boundary conditions or low-frequency components, and progressively includes full PDE residuals as the model stabilizes. Krishnapriyan et al. [2021] highlighted that premature enforcement of difficult regions often leads to convergence failures, motivating curricula that schedule constraint difficulty. Jagtap and Karniadakis [2021] addressed similar issues via domain decomposition (XPINNs), effectively providing a spatial curriculum that trains subdomains before coupling them. More recently, Wang et al. [2023] proposed Causal PINNs, where temporal weights enforce causality by prioritizing earlier time segments, improving stability for transient problems. Overall, curriculum approaches stabilize training and accelerate convergence but depend on heuristic scheduling and problem-specific tuning, lacking general criteria for optimal curriculum design.

**Risk-averse neural operators** Related work applies CVaR to neural operators to improve out-of-distribution generalization on supervised, function-to-function tasks [Liu et al., 2025]. Our setting differs along two axes. (i) PINNs solve a specific PDE by enforcing the governing equations and boundary/initial conditions, rather than learning a global operator from paired functions. (ii) we apply risk directly to the physics residual and can train without labeled solutions (physics-only), whereas neural operators apply risk to supervised prediction losses and require function-pair datasets. As a result, the algorithms, training dynamics, and evaluation criteria diverge; our approach complements NO-based OOD robustness.

These PINN-based approaches share a common premise: dynamically adjusting the effective weights assigned to loss terms or training points to balance learning across the domain.

Despite their empirical success, these methods do not fundamentally alter the $L_2$ (MSE) objective itself, which remains risk-neutral and highly sensitive to outliers. They also remain mostly heuristic, the weighting rules are often ad hoc (e.g., proportional to gradient magnitudes or residual norms) and lack a rigorous optimization-theoretic coupled with probabilistic foundation. Moreover, none of these strategies incorporate an explicit uncertainty-aware mechanism to characterize or control the distribution of residual errors. Consequently, they provide no guarantees that the trained model achieves uniformly reliable accuracy across the domain. In fact, they often demonstrate systematic underperformance in rare but critical regions, such as shocks, singularities, or stiff regimes, where large residuals persist despite apparent global convergence.

## 4 Residual Risk-Aware PINN (RRaPINN) Methodology

This part provides a structured methodology starting by elaborating our PINNs-based probabilistic framework, the benefit of using the CVaR instead of the VaR probabilistic constraint. We then jump into the main RRaPINN formulation based on theoretical analogies between CVaR and the top-k loss. We also provided some training tips to improve our methods, and the metrics used in this study.

### 4.1 From Mean Errors to Probabilistic Guarantees

The objective (7) controls only the mean residual and can hide large localized errors, which may deteriorate the approximation performance. To resolve this, we introduce a distributional guarantee on the absolute residual which is considered as a random variable given random collocation points.

$$
R_\theta := |r(X;\theta)|,\quad X\sim \mu, \tag{9}
$$

via the chance constraint

$$
P\big(R_\theta \le \varepsilon\big)\ge \alpha,\quad \text{for some }\alpha\in(0.5,1),\ \varepsilon>0. \tag{10}
$$

Thus, (7) becomes which gives the following probabilistic constrained problem:

$$
\min_\theta L_{\text{PINN}}(\theta) \tag{11}
$$

s.t.

$$
P\big(R_\theta \le \varepsilon\big)\ge \alpha \tag{12}
$$

$\varepsilon$ can be either learned or adaptive while allowing the model to choose a tolerance consistent with the physics and capacity).

#### 4.1.1 Quantile Formulation (Value-at-Risk).

Considering the residual magnitudes $R_\theta := |r(X;\theta)|$, let $F_\theta(t):=P(R_\theta\le t)$ denote the CDF of $R_\theta$, and let $Q_{R_\theta}(\alpha):=\inf\{t\in \mathbb{R}_+: F_\theta(t)\ge \alpha\}$ be its $\alpha$-quantile. As demonstrated in [Nemirovski and Shapiro, 2007], the chance constraint (10) is therefore equivalent to

$$
\mathrm{VaR}_\alpha(R_\theta):=Q_{R_\theta}(\alpha)\le \varepsilon, \tag{13}
$$

where VaR$_\alpha$ (Value-at-Risk) [Duffie and Pan, 1997] is the classical surrogate risk measure widely used in quantitative finance. For $\alpha\in(0,1)$, VaR$_\alpha(R_\theta)$ specifies the threshold below which at least a fraction $\alpha$ of residuals lie. While this captures where the “worst” $(1-\alpha)$ proportion of the distribution begins, it says nothing about the magnitude of those extreme values. Moreover, empirical estimates of VaR are piecewise-constant and hence non-differentiable with respect to $\theta$, so their gradients vanish almost everywhere and are unstable near order-statistic ties. VaR also fails to satisfy key axioms of a coherent risk measure, such as sub-additivity. These limitations make it ill-suited as a training objective and motivate the use of a smoother, tail-sensitive alternative: the Conditional Value-at-Risk (CVaR) [Rockafellar et al., 2000].

#### 4.1.2 Conditional Value-at-Risk (CVaR).

The Conditional Value-at-Risk refines VaR by measuring the expected loss in the tail, i.e., the average of outcomes that exceed the VaR threshold:

$$
\mathrm{CVaR}_\alpha(R_\theta)=\mathbb{E}\left[R_\theta\mid R_\theta\ge \mathrm{VaR}_\alpha(R_\theta)\right]. \tag{14}
$$

Unlike VaR, CVaR is a coherent risk measure, convex, and explicitly sensitive to the severity of extreme losses. This property makes CVaR particularly suitable in the PINN setting, where collocation regions often contain localized uncertainties, shocks, or singularities that can lead to disproportionately large residuals. By directly penalizing the average severity of these extreme events, CVaR provides a principled, optimization-friendly surrogate for robust residual control. Therefore our robust formulation can be written as:

$$
\min_{\theta,\varepsilon>0} \underbrace{L_{\text{PINN}}(\theta)}_{\text{physics + boundary}}
\quad \text{s.t.} \quad
\underbrace{\mathrm{CVaR}_\alpha\big(|r(X;\theta)|\big)}_{\text{tail risk of residuals}} \le \varepsilon. \tag{15}
$$

As Rockafellar et al. [2000] demonstrated, the Conditional Value-at-Risk at the confidence level $\alpha$ can be rewritten as the Rockafellar-Uryasev (RU) program as follows

$$
\mathrm{CVaR}_\alpha(R):=\inf_{\eta\in\mathbb{R}}\phi(\eta),\qquad
\phi(\eta)=\eta+\frac{1}{1-\alpha}\mathbb{E}\big((R-\eta)_+\big), \tag{16}
$$

$$
(x)_+ := \max\{x,0\}. \tag{17}
$$

The empirical CVAR RU objective is defined as follows:

$$
\hat{\phi}_N(\eta)=\eta+\frac{1}{1-\alpha}\cdot \frac{1}{N}\sum_{i=1}^N (R_i-\eta)_+. \tag{18}
$$

Unlike VaR, $\phi(\eta)$ is convex and (sub)differentiable in both $\eta$ and in the neural network’s parameters $\theta$, enabling stable stochastic optimization.

### 4.2 From Empirical CVAR to Residual Adaptive Weighting View.

#### 4.2.1 Top-k Set Definition

Given a randomly sampled minibatch $\{x_i\}_{i=1}^N$, define residual magnitudes $R_i(\theta):=|r(x_i;\theta)|$, $i=1,\dots,N$. Let the order statistics be $R_{(1)}(\theta)\le \cdots \le R_{(N)}(\theta)$ and let $\pi$ be a permutation such that $R_{(\ell)}(\theta)=R_{\pi(\ell)}(\theta)$. Fix $k:=\lfloor N(1-\alpha)\rfloor$ and define the Top-k index set

$$
I_{\text{top-k}}(\theta):=\{\pi(N-k+1),\dots,\pi(N)\}. \tag{19}
$$

The associated threshold (the smallest value included in the Top-k) is $\tau(\theta):=R_{(N-k+1)}(\theta)$.

**Ties at the threshold.** Let $E(\theta):=\{i: R_i(\theta)=\tau(\theta)\}$ denote indices equal to the threshold. If there are ties at $\tau(\theta)$, the set $I_{\text{top-k}}(\theta)$ is not unique; any selection with cardinality $k$ that includes all strictly larger values and an arbitrary subset of $E(\theta)$ of the required size is valid. All such selections yield the same empirical CVaR value.

**Remark 4.1.** All the ascendant residual order statistics $(R_{(1)}(\theta)\le \cdots \le R_{(N)}(\theta))$ provided in this study are training-specific and may vary from one epoch to the other.

**Proposition 4.2 (Proof1).** Let $R_{(1)}(\theta)\le \cdots \le R_{(N)}(\theta)$ be order statistics and set $t=(1-\alpha)N$, $m=\lfloor t\rfloor$ ($\lfloor t\rfloor$ being the floor of $t$), $s=t-m$. Then the empirical RU objective

$$
\hat{\phi}_N(\eta)=\eta+\frac{1}{t}\sum_{i=1}^N (R_i-\eta)_+ \tag{20}
$$

has minimizers

$$
\arg\min_\eta \hat{\phi}_N(\eta)\in
\begin{cases}
\{R_{(N-m)}\}, & \text{if } s>0 \text{ and there are no ties at } R_{(N-m)},\\
[R_{(N-m)},R_{(N-m+1)}], & \text{if } s=0 \text{ or there is a tie at the boundary.}
\end{cases} \tag{21}
$$

**Proposition 4.3 (Proof 2).** Let $R_1,\dots,R_N\in \mathbb{R}$ and let $R_{(1)}\le \cdots \le R_{(N)}$ be the order statistics (ascending). Fix $\alpha\in(0,1)$ and set $t:=(1-\alpha)N$, $m:=\lfloor t\rfloor$, $s:=t-m\in[0,1)$. Consider the empirical Rockafellar-Uryasev objective

$$
\hat{\phi}_N(\eta)=\eta+\frac{1}{(1-\alpha)N}\sum_{i=1}^N (R_i-\eta)_+
=\eta+\frac{1}{t}\sum_{i=1}^N (R_i-\eta)_+.
$$

Then the minimum value (the empirical CVaR) is

$$
\widehat{\mathrm{CVaR}}_\alpha(R):=\inf_{\eta\in\mathbb{R}}\hat{\phi}_N(\eta)
=\frac{1}{t}\left(\sum_{i=N-m+1}^N R_{(i)} + sR_{(N-m)}\right). \tag{22}
$$

Proposition 4.3 shows that the empirical CVaR$_\alpha$ can be expressed as the average of the $m$ largest individual losses (when $s=0$), and as a convex combination of the Top-$m$ and a fractional contribution from $R_{(N-m)}$ (when $s>0$).

Considering $N$ residual samples, let $t=(1-\alpha)N$, $m=\lfloor t\rfloor$, and $s=t-m\in[0,1)$, the proposition 4.3 shows that the empirical CVaR always depends only on the tail set of worst residuals:

$$
\widehat{\mathrm{CVaR}}_\alpha(R)=\frac{1}{t}\left(\sum_{i=N-m+1}^N R_{(i)} + sR_{(N-m)}\right). \tag{23}
$$

If $s=0$ (i.e. $t$ is equal to is floor $m$), this reduces to a Top-$t$ average:

$$
\widehat{\mathrm{CVaR}}_\alpha(R)=\frac{1}{t}\sum_{i\in I_{\text{top-t}}} R_i,\qquad
I_{\text{top-t}}:=\{\text{indices of the } t \text{ largest residuals}\}. \tag{24}
$$

When $s>0$, the value is a convex combination of the Top-$m$ and a fractional contribution from $R_{(N-m)}$, but the same tail weighting principle holds: only the largest residuals matter. This admits a natural adaptive weighting interpretation. Define weights

$$
w_i=
\begin{cases}
\frac{N}{t}, & i\in I_{\text{tail-t}},\\
0, & \text{otherwise},
\end{cases} \tag{25}
$$

where $I_{\text{tail-t}}$ is the tail set: the top-$t$ residuals if $s=0$, or the top-$m$ plus a fractional contribution from $R_{(N-m)}$ if $s>0$.

$$
\widehat{\mathrm{CVaR}}_\alpha(R)=\frac{1}{N}\sum_{i=1}^N w_i R_i. \tag{26}
$$

Thus CVaR can be viewed as a weighted empirical mean in which optimization effort is concentrated adaptively on the worst residuals. Unlike heuristic reweighting schemes commonly used in PINNs, the weights $(w_i)$ are uniquely determined by the coherent risk measure CVaR and thereby operationalize the probabilistic constraint $P(|r(X;\theta)|\le \varepsilon)\ge \alpha$.

### 4.3 RRaPINN Formulation

#### 4.3.1 CVaR Hinge Penalty

The empirical squared $L_1$ exact penalty relaxation [Fletcher, 1985, Smith et al., 1997], of the problem (15) is written as:

$$
L_b^{\text{robust}}(\theta,\varepsilon)=L_b^{\text{PINN}}(\theta)+\lambda_p\big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big)_+^2+\gamma_\varepsilon \varepsilon, \tag{27}
$$

$R_i=|r(x_i;\theta)|$, and $(\cdot)_+=\max\{0,\cdot\}$. The term $\gamma_\varepsilon \varepsilon$ prevents the trivial solution $\varepsilon\to\infty$ and encodes a prior preference for tighter tolerances, $\lambda_p$ controls the strength of the penalty when the tail average exceeds $\varepsilon$. Substituting the value of CVaR$_\alpha(R)$ given in Eq. (26), into the equation (27), yield the final RRAPINN objective

$$
L_b^{\text{robust}}(\theta,\varepsilon)=L_b^{\text{PINN}}(\theta)+\lambda_p\left(\frac{1}{N}\sum_{i=1}^N w_i R_i-\varepsilon\right)_+^2+\gamma_\varepsilon \varepsilon, \tag{28}
$$

where the weights $(w_i)$ as defined in (25), concentrate on the worst $t$ residuals (Top-$t$ average if $t\in\mathbb{N}$, fractional tail if $t\notin\mathbb{N}$). This formulation provides a principled, data-driven reweighting scheme derived from a coherent risk measure. The final loss (28) exhibits the weighting system explicitly, which is now a residual risk aware mean that shifts training focus onto the most problematic regions of the PDE domain in each batch.

#### 4.3.2 RRaPINN-Based Weighted Mean Squared (RRaPINN-WMS): CVaR Mean Excess Surrogate.

**Proposition 4.4 (Proof 3).** Fix $\alpha\in(0,1)$ and Let $(R_i)_{i=1}^N$ be nonnegative residual magnitudes, let $t:=(1-\alpha)N$ be an integer (equal to its floor and ceiling). Considering $\varepsilon\ge 0$, the weights $w_i=
\begin{cases}
\frac{N}{t}, & i\in I_{\text{tail-t}},\\
0, & \text{otherwise},
\end{cases}
$
satisfy

$$
\frac{1}{N}\sum_{i=1}^N w_i = 1 \quad \text{(equivalently, } \sum_i w_i = N\text{)}. \tag{29}
$$

and defining the mean-squares robust penalty as $P_{\text{ms}}(R;\varepsilon,w):=\frac{1}{N}\sum_{i=1}^N w_i(R_i-\varepsilon)_+^2$, the following inequality hold:

$$
P_{\text{ms}}(R;\varepsilon,w)\ge \big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big)_+^2. \tag{30}
$$

**Empirical RRaPINN-WMS Top-k/ Mean Excess Penalty** Under the conditions given in eq. (30), we can formulate the RRA weighted mean squared surrogate as follows:

$$
L_b^{\text{surrogate}}(\theta,\varepsilon)=L_b^{\text{PINN}}(\theta)+\lambda_p \cdot \frac{1}{N}\sum_{i=1}^N w_i(R_i-\varepsilon)_+^2+\gamma_\varepsilon \varepsilon, \tag{31}
$$

which preserves the CVaR weighting principle while producing stronger gradient signals in the presence of rare but extreme misfits.

### 4.4 Adaptive Gradient-Free Tail Threshold $\varepsilon$

Treating $\varepsilon$ as a learnable parameter is fragile because the optimizer can reduce the hinge penalty by inflating $\varepsilon$ instead of shrinking tail residuals [^4]. We therefore do not backpropagate through $\varepsilon$ and update it from a detached tail statistic. We then move $\varepsilon$ toward a margin-shifted gradient-free empirical CVaR using the following formula $t=(1-\gamma)\widehat{\mathrm{CVaR}}_\alpha(|r_\theta|)$, with $\beta=0.95$ using an EMA that smooths upward changes and a cap that makes downward changes immediate: $\varepsilon \leftarrow \min\big(\beta \varepsilon + (1-\beta)t,\ t\big)$. With this strategy, no gradients flow through $\varepsilon$, so there is no incentive to inflate it. The margin keeps a positive gap so the tail penalty remains active near convergence. The EMA used here reduces sampling noise while the cap prevents overshoot(K-averaging can be added for extra smoothing, but was not required in our runs.)

### 4.5 Two-Phase Training with Dynamic Balancing

We use a two-phase loss. Warmup (first $K$ epochs; $K=1000$ unless stated) minimizes $L_{\text{base}}+L_{\text{BC}}+L_{\text{IC}}$. Tail-control (epochs $>K$) adds a remove $L_{\text{base}}$ and risk term $L_{\text{pen}}=\lambda_p L_{\text{core}}$ where $L_{\text{core}}$ is either CVaR–hinge $([\mathrm{CVaR}_\alpha(|r|)-\varepsilon]_+)^2$ or mean–excess $\mathbb{E}([|r|-\varepsilon]^2_+)$. To match scales we set

$$
\lambda_p \propto \frac{S_b}{S_p},
\quad \text{where } S_b=\mathrm{EMA}_{\eta_{\mathrm{EMA}}=0.9}[\mathrm{det}(L_{\text{base}})],\ 
S_p=\mathrm{EMA}_{\eta_{\mathrm{EMA}}=0.9}[\mathrm{det}(L_{\text{core}})].
$$

Balancing is optional, however it auto-balances bulk vs tail gradients. For stiff problems we optionally invert the schedule (tail-first, then bulk). [^5]

### 4.6 Benchmarks and Error Metrics

#### 4.6.1 Benchmark Models

We respectively denote our models RRaPINN and its variant RRaPINN-WMS as RRa and RRaWMS and compared them to Convolutional Weighting PINN (CWP)[Si and Yan, 2025], Residual-Based Attention PINN (RBAPINN) [Anagnostopoulos et al., 2024] and PINN Baseline (Base) [Raissi et al., 2019], using the metrics defined in the next subsection. All benchmark models were trained using their default parameters.

#### 4.6.2 Metrics

**Relative $L_2$ and $L_\infty$ errors.** Given a reference (ground-truth) solution $u^\star$ and a prediction $\hat{u}$ on a spatial domain $\Omega\subset \mathbb{R}^d$ (and optionally time $t\in(0,T]$), we report

$$
\mathrm{Rel}L_2(u)=\frac{\|\hat{u}-u^\star\|_{L_2(\Omega)}}{\|u^\star\|_{L_2(\Omega)}}, \qquad
L_\infty(u)=\|\hat{u}-u^\star\|_{L_\infty(\Omega)}. \tag{32}
$$

In practice, we approximate these by sampling a finite set $\{x_j\}_{j=1}^N\subset \Omega$ (or space-time points $(x_j,t_j)$) and use the Monte Carlo approach defined as follows:

$$
\mathrm{Rel}L_2(u)\approx
\frac{\left(\sum_{j=1}^N|\hat{u}_j-u^\star_j|^2\right)^{1/2}}
{\left(\sum_{j=1}^N|u^\star_j|^2\right)^{1/2}},
\qquad
L_\infty(u)\approx \max_{1\le j\le N}|\hat{u}_j-u^\star_j|. \tag{33}
$$

**$\alpha$-th-percentile:** The $\alpha$-percentile $(Q_\alpha)$ of absolute point-wise residuals was also determnined for $\alpha=0.95$.

**Empirical Tail Plot $(1-\mathrm{CDF})$ plot.** Let $r$ denote the residual magnitude and let $F(x)=Pr(|r|\le x)$ be its cumulative distribution function (CDF). The plotted quantity is the survival (complementary CDF)

$$
S(x)=1-F(x)=Pr(|r|>x),
$$

shown on a logarithmic $y$-axis. At any fixed threshold $x$, a lower curve means a smaller fraction of the domain has residuals larger than $x$ (i.e., better tail behavior). Two useful readouts are: (i) the crossing at $S(x)=0.05$, which yields the 95th percentile $Q_{95}$ (since 5% of points exceed $x$), and (ii) the rightmost extent of a curve, which approximates $L_\infty=\max|r|$. Moreover, the area under $S(x)$ over the worst $(1-\alpha)$ mass is directly related to $\mathrm{CVaR}_\alpha$ (the average residual in the upper tail).

## 5 Experiments

In all the experiments, we used the Adam optimizer [Kingma and Ba, 2017]; to improve convergence, we employ a cosine annealing learning rate schedule with minimum value $\eta_{\min}=10^{-5}$. Formally, the learning rate at epoch $t$ is given by

$$
\eta_t=\eta_{\min}+\frac{1}{2}(\eta_0-\eta_{\min})
\left(1+\cos\left(\frac{T_{\mathrm{cur}}}{T_{\max}}\pi\right)\right), \tag{34}
$$

where $T_{\mathrm{cur}}$ is the current epoch and $T_{\max}$ is the maximum number of epochs. The initial learning rate $\eta_0$ was problem-specific. For the RRaPINN-based models, unless stated otherwise, we use $\alpha=0.95$ and $\lambda_p=0.03$; for RRa-based model, gradients are clipped to a maximum norm of 5.0 for stability.

### 5.1 1D Heat Equation

We assess our methods on the 1D heat equation with high-frequency dynamics [Fernandez-Cara and Münch, 2013, Si and Yan, 2025]:

$$
\frac{\partial u}{\partial t}(t,x)=\alpha \frac{\partial^2 u}{\partial x^2}(t,x), \qquad (t,x)\in (0,T]\times(0,1),
$$

we consider $T=1$ and $\alpha=\frac{1}{400\cdot \pi^2}$, with initial and boundary conditions

$$
u(t,0)=u(t,1)=0,\quad t\ge 0,
$$

$$
u(0,x)=\sin(20\pi x),\quad x\in[0,1].
$$

To guarantee satisfaction of the initial and boundary conditions, we enforce the neural network output in the form

$$
\hat{u}(t,x)=tx(1-x)\hat{u}_{NN}(t,x)+\sin(20\pi x), \tag{35}
$$

where $\hat{u}_{NN}(t,x)$ is the raw output of the neural network.

**Figure 2: Reference solution for the 1D heat equation.**

**Neural network architecture and traininhg details.** The approximation $\hat{u}_{NN}$ is produced by a fully connected feedforward neural network with 4 hidden layers of width 80, each equipped with emphhyperbolic tangent activation functions. All weights are initialized using Xavier initialization and biases are set to zero. For training, we adopt the emphAdam optimizer with a given learning rate $\eta_0=9\times 10^{-3}$ over 15, 0000 iterations. We used $N_{tr}=5000$ interior point for the training and use another $N_{te}=5000$ and initialization to foster diversity between train and test interior points). The average runtime per iteration was about 0.035 s for RRa CVaR hinge and 0.04 s for the RRa mean excess.

**Figure 3: Tail Plot for the 1D heat equation**

| Method | $L_2^{\text{rel}}$ | $L_\infty$ | $Q_{95}$ |
|---|---:|---:|---:|
| Baseline | 0.003340 | 0.019804 | 0.001676 |
| RRa | 0.001331 | 0.008581 | 0.000826 |
| RRaWMS | 0.001490 | 0.009460 | 0.000732 |
| CWP | 0.001640 | 0.006712 | 0.001726 |
| RBA | 0.003498 | 0.019458 | 0.002145 |

**Table 1: Performance comparison across methods for the 1D heat equation.**

Table 1 compares the performance of different methods on the 1D heat equation. RRa achieves the lowest relative $L_2$ error and MSE, indicating the most accurate prediction on average. CWP shows the smallest $L_\infty$ norm, suggesting better control over the worst-case pointwise errors. Looking at the 0.95-quantile metric, RRaWMS attains the lowest value, reflecting superior performance in nearly all points while still ignoring extreme outliers. Both RBA and Baseline perform similarly, indicating that residual-based weighting does not provide significant benefits for this smooth 1D heat equation problem. The tail plot in figure 3, reveals that the RRa-based methods provide the steepest decay especially RRaWMS, followed by CWP. RBA and and Baseline PINN shows heavier tails. This indicates that RRa-based methods foster better robustness and extreme residual values control.

### 5.2 2D Poisson Equation

The Poisson equation is a fundamental elliptic PDE that models steady-state diffusion or potential fields, such as electrostatic or gravitational potentials. In two dimensions, it captures spatial interactions governed by Laplacian operators over a bounded domain. Owing to its smooth, well-posed nature and availability of analytical or high-accuracy numerical solutions, the 2D Poisson equation is widely used as a benchmark in physics-informed neural networks (PINNs). It provides a controlled setting to assess how well PINNs approximate spatial gradients, enforce boundary conditions, and generalize across varying geometries Suhendar et al. [2024].

On a bounded Lipschitz domain $\Omega\subset \mathbb{R}^2$, the Poisson problem reads

$$
-\Delta u(x,y)=f(x,y)\quad \text{in }\Omega, \tag{36}
$$

with either Dirichlet or Neumann boundary data:

$$
u=g \text{ on }\partial\Omega \quad \text{or} \quad \partial_n u=h \text{ on }\partial\Omega, \tag{37}
$$

where $\partial_n$ denotes the outward normal derivative. For $f(x,y)=2\pi^2\sin(\pi x)\sin(\pi y)$, a common solution instance on $\Omega=(0,1)^2$ is

$$
u^\star(x,y)=\sin(\pi x)\sin(\pi y). \tag{38}
$$

we use $g=u^\star|_{\partial\Omega}$.

**Figure 4: Exact Solution for the 2D Poisson equation.**

**Neural network architecture and training details.** We approximate $u(x,y)$ with a fully-connected multilayer perceptron (MLP) of depth 6 and width 64 with tanh activations. The input is the spatial coordinate $(x,y)\in(0,1)^2$; the output is the scalar field value. We impose homogeneous Dirichlet data strongly by adding a boundary loss term. With gradient clipping at 5 we train with Adam (learning rate $5\times 10^{-3}$) and a cosine annealing schedule down to $10^{-5}$ over the full horizon. We use a warm-up of 1000 epochs during which $L_{\text{tail}}$ is inactive, and then enable it after warm up. All experiments use single-precision on a single GPU. We use 10, 000 interior points and 200 boundary point. For reporting, relative $L_2$ error is measured on a $101\times 101$ grid against the manufactured solution $u^\star$. The average runtime per iteration was about 0.010 s for RRa CVaR hinge and 0.011 s for the RRa mean excess.

**Figure 5: Tail Plot for the 2D Poisson equation**

| Methods | $L_2^{\text{rel}}$ | $L_\infty$ | $Q_{95}$ |
|---|---:|---:|---:|
| Baseline | 0.000765 | 0.001689 | 0.000886 |
| RBA | 0.000156 | 0.000632 | 0.000141 |
| CWP | 0.000426 | 0.000947 | 0.000471 |
| RRa | 0.000212 | 0.000874 | 0.000207 |
| RRaWMS | 0.000118 | 0.000347 | 0.000127 |

**Table 2: Performance comparison across methods for the 2D Poisson equation.**

Table (2) shows that the best model across all metrics is the RRaWMS, which is seconded by RBA and then RRa. CWP and Baseline PINN provide the worse metrics. Figure 5 shows survival curves $S(a)=Pr(|r|>a)$ for the 2D Poisson problem. RRAWMS (purple) lies farthest left with the steepest decay, indicating a uniformly thinner residual distribution from bulk to tail; this is consistent with its design that down-weights emerging large errors while preserving pressure on the bulk. RBA (orange) is next best and excels in the extreme tail (sharp drop near $5\times 10^{-4}$), reflecting its targeted suppression of rare outliers. RRA (red) improves the mid-tail but cuts off later, while CWP (green) remains between RRA and the BASELINE (blue), whose heavy tail reveals persistent hotspots. Therefore, it is worth saying that for a smooth elliptic PDE like 2D poisson, where residuals correlate closely with global $H^1/L^2$ error and errors diffuse spatially, the leftward shift of the entire curve delivered by RRAWMS is particularly beneficial.

### 5.3 The Korteweg-de Vries (KdV) equation.

The Korteweg-de Vries (KdV) equation is a classical nonlinear partial differential equation that models the propagation of weakly nonlinear and weakly dispersive waves in shallow water channels Korteweg and de Vries [1895], Raissi et al. [2019]. It describes the interplay between nonlinear steepening and dispersive spreading, leading to the emergence of solitary wave solutions known as *solitons* that retain their shape and velocity during propagation. This soliton travels without distortion at speed $c$, exemplifying the balance between nonlinearity and dispersion in Eq. (40).

From an optimization standpoint, KdV is nontrivial for PINNs because the third-order spatial derivative amplifies small numerical errors and sampling jitter, often producing heavy residual tails even when the bulk error is small. These features nonlinearity, higher-order dispersion, and periodic constraints stress both the autodifferentiation stack and the loss geometry, motivating risk-aware formulations (e.g., tail-sensitive penalties) alongside standard mean-squared residual minimization.

**Neural network architecture and training details.** We approximate $u(x,y)$ with a fully-connected multilayer perceptron (MLP) of depth 4 and width 128 using SiLU activations. Homogeneous Dirichlet data are imposed by adding a boundary loss term computed on $n_{\text{bnd}}=512$ boundary samples per epoch; the interior residual is evaluated on $n_{\text{int}}=10{,}000$ points. We train with AdamW (learning rate $1\times 10^{-2}$) and a cosine annealing schedule down to $10^{-5}$ over 10,000 epochs, with gradient clipping at 1. A warm-up of 1,000 epochs keeps the tail mechanism inactive; afterward, risk control is enabled with a broad tail split at $\alpha=0.95$. All runs use double precision on a single GPU. For reporting, the relative $L_2$ error is measured on a $201\times 201$ grid against the manufactured solution $u^\star$; residual-tail plots use the same grid. The average runtime per iteration was about 0.074 s for RRa CVaR hinge and 0.077 s for the RRa mean excess.

We considered the one-dimensional form of the KdV equation written as

$$
\frac{\partial u}{\partial t}(x,t)+6u(x,t)\frac{\partial u}{\partial x}(x,t)+\frac{\partial^3 u}{\partial x^3}(x,t)=0, \tag{39}
$$

$$
x\in \mathbb{R},\ t\ge 0, \tag{40}
$$

where $u(x,t)$ denotes the wave amplitude, $x$ the spatial coordinate, and $t$ the time variable. We consider the problem on a bounded periodic spatial domain $x\in[X_{\min},X_{\max}]=[-10,10]$ and temporal domain $t\in[T_{\min},T_{\max}]=[0,1]$, with periodic boundary conditions

$$
u(X_{\min},t)=u(X_{\max},t), \quad u_x(X_{\min},t)=u_x(X_{\max},t), \tag{41}
$$

$$
u_{xx}(X_{\min},t)=u_{xx}(X_{\max},t),
$$

and the analytical single-soliton initial condition, where $c>0$ (we considered $c=1$) denotes the soliton velocity and $x_0$ its initial position.

$$
u(x,0)=\frac{c}{2}\,\mathrm{sech}^2\left(\frac{\sqrt{c}}{2}(x-x_0)\right), \tag{42}
$$

**Figure 6: Exact Solution for the 1D Korteweg-de Vries Equation.**

**Figure 7: Tail Plot for the 1D KdV equation**

| Model | $L_2^{\text{rel}}$ | $L_\infty$ | $Q_{95}$ |
|---|---:|---:|---:|
| Baseline | 0.000297 | 0.000697 | 0.000057 |
| RRa | 0.000264 | 0.000645 | 0.000058 |
| RRaWMS | 0.000239 | 0.000613 | 0.000048 |
| CWP | 0.000276 | 0.000586 | 0.000072 |
| RBA | 0.000273 | 0.000522 | 0.000069 |

**Table 3: KdV PINN Performancees**

Table (3) shows that for the periodic, dispersive KdV dynamics (where errors in $u_{xxx}$ can diffuse and contaminate the field), RRaWMS attains the lowest $L_2^{\text{rel}}$ and best $Q_{95}$, indicating uniformly small errors across space and tighter residual tails, desirable when third-derivative terms propagate local inaccuracies. RBA delivers the best $L_\infty$, meaning peaks/crests are clipped most tightly, but its higher $L_2^{\text{rel}}$ and $Q_{95}$ suggest more localized hotspots elsewhere. CWP offers a balanced compromise (good $L_\infty$, mid $L_2^{\text{rel}}$) but it provided $Q_{95}$), while RRa provided the second best $L_2^{\text{rel}}$ mid $Q_{95}$ and bad $L_\infty$. The Baseline provided the worse $L_2^{\text{rel}}$ and $L_\infty$ but the second best $Q_{95}$.

Figure 7 plots the complementary cumulative density function of absolute residual on a log scale: curves further left/down indicate better residual. In the bulk range $(|r|\lesssim 3\times 10^{-4})$, RRAWMS stays lowest, implying fewer moderate violations and explaining its superior $L_2^{\text{rel}}$ and $Q_{95}$. In the extreme tail $(|r|\gtrsim 4\times 10^{-4})$, RBA drops off most sharply, yielding the best $L_\infty$ by suppressing rare, large errors. The BASELINE has the heaviest tail, indicating persistent large residuals. For KdV, the third-order dispersive term $u_{xxx}$ magnifies curvature/high-frequency errors; thus, strong mid-tail control (as in RRAWMS) improves global waveform fidelity, while targeted suppression of extremes (as in RBA) prevents crest overshoots near steep gradients and dispersive fronts.

### 5.4 1D Viscous Burgers’ Equation

The Burgers’ equation serves as a canonical testbed for nonlinear advection-diffusion, illustrating the interplay between nonlinear steepening and viscous smoothing. In one dimension, the viscous Burgers’ equation is often regarded as a stiff problem, since strong nonlinear advection can generate sharp gradients or shock-like structures that require fine temporal and spatial resolution to resolve, especially when viscosity is small [Li et al., 2015].

We solve the viscous Burgers PDE defined as follows.

$$
\partial_t u(x,t)+u(x,t)\partial_x u(x,t)=\nu \partial_{xx}u(x,t), \tag{43}
$$

$$
(x,t)\in \Omega\times(0,1],\quad \Omega=(-1,1), \tag{44}
$$

with kinematic viscosity $\nu>0$, initial condition

$$
u(x,0)=-\sin(\pi x), \quad x\in[-1,1], \tag{45}
$$

and homogeneous Dirichlet boundary conditions

$$
u(-1,t)=u(1,t)=0,\quad t\in[0,1]. \tag{46}
$$

**Figure 8: Reference solution for the viscous Burgers equation.**

We adopt the standard reference viscosity parameter $\nu=0.01/\pi$. The initial and boundary conditions were enforced in hard form, i.e., the network output was wrapped in a trial solution of the form

$$
U_{\text{Enf}}(x,t)=t(1-x^2)U_{NN}(x,t)-\sin(\pi x), \tag{47}
$$

which guarantees satisfaction of the prescribed constraints by construction. Figures (9) present the high resolution numerical solutions and their spatial gradients at $t=0.5$ and $t=0.7$. A pronounced gradient is clearly observed around $x=0$, highlighting the formation of a steep transition layer. This steepening is consistent with the characteristic dynamics of the viscous Burgers equation, demonstrating that the model accurately captures regions of rapid variation and sharp changes in the solution profile.

**Figure 9: Predicted vs Actual 1D solution and gradients at fixed times.**  
(a) $u$ at $t=0.7$  
(b) Gradient at $t=0.7$  
(c) $u$ at $t=0.5$  
(d) Gradient at $t=0.5$

**Neural network architecture and traininhg details.** For this set of experiments, the model was trained for 20,000 epochs using a fully connected feed-forward neural network with 7 hidden layers, each consisting of 20 neurons. The hyperbolic tangent (tanh) activation function was employed throughout the network, with the final activation also set to tanh. Optimization was performed using the Adam optimizer with a learning rate of $\eta_0=5\times 10^{-3}$. To improve convergence, a cosine learning rate scheduler was applied. The number of residual interior points was fixed at 10,000. For evaluation, at each training iteration we sampled a test set of 90,000 points (with new random initialization at every evaluation). The relative $L_2$ error was computed and recorded every 500 epochs. The average runtime per iteration was about 0.021 s for RRa CVaR hinge and 0.03 s for the RRa mean excess.

**Figure 10: Pointwise L2 Relative Error Plot for the 1D Burger Equation**

Figures (10) show that all the model predictions grow unexpectedly around $x=0$ and $t\in[0.4,1]$, however, RRA display the most controlled performances among all models, as well as the lowest $L_2$ relative error overall which is followed by CWP, then RBAPINN, RRAWMS and the poorer result was delivered by the PINN Baseline.

**Figure 11: Tail Plot of Residuals (Residual vs Cummulative Proportion)**

| Method | \multicolumn{3}{c|}{$t=0.5$} | \multicolumn{3}{c}{$t=0.7$} |
|---|---:|---:|---:|---:|---:|---:|
|  | $L_2^{\text{rel}}$ | $L_\infty$ | $Q_{95}$ | $L_2^{\text{rel}}$ | $L_\infty$ | $Q_{95}$ |
| Base | 0.00990 | 0.03940 | 0.02786 | 0.01041 | 0.03598 | 0.02727 |
| RRa | 0.00692 | 0.02581 | 0.01707 | 0.00616 | 0.01942 | 0.01440 |
| RRaWMS | 0.00953 | 0.03775 | 0.02730 | 0.00596 | 0.01753 | 0.01469 |
| CWP | 0.00799 | 0.03083 | 0.01957 | 0.00732 | 0.02421 | 0.01578 |
| RBA | 0.00665 | 0.02371 | 0.01821 | 0.00677 | 0.02136 | 0.01535 |

**Figure 12: Comparison of methods on error metrics at the shock region for $t=0.5$ and $t=0.7$ (lower is better).**

Table (12) shows a clear split: RBA leads at the earlier time $(t=0.5)$ on both global accuracy $(L_{2,\text{rel}})$ and worst-case error $(L_\infty)$, while RRaWMS takes the lead later $(t=0.7)$ on the same metrics. RRa is the most consistent at controlling the error tail (lower $Q_{95}$) across both times. CWP performs solidly, but remains in the middle group overall. Figure (11) reports the survival function of the absolute residuals on a log scale, highlighting the tail behavior of the error distributions across methods. The RRa-based approaches (RRa and RRaWMS) exhibit the steepest decay, indicating a substantially reduced frequency of large residuals. In contrast, the Base and CWP models show heavier tails, while RBA further extends the error distribution, occasionally producing markedly larger residuals. These results suggest that the RRa-based methods not only improve average predictive accuracy but also enhance robustness by suppressing extreme errors, however, it may overlook some important spots $(t=0.5)$ because of the random collocation points resampling.

### 5.5 The 2D Discontinuous Poisson Problem

We aim to solve the 2D Poisson equation with constant conductivity $(k=1)$ on the unit square, governed by a discontinuous right-hand side (RHS):

$$
-\Delta u = f(x,y)\quad \text{in } \Omega=(0,1)^2
$$

$$
u=0 \quad \text{on } \partial\Omega
$$

The primary challenge stems from the forcing term $f(x,y)$, which is piecewise defined with a jump discontinuity at the interface $x=0.5$:

$$
f(x,y)=
\begin{cases}
2\pi^2\sin(\pi x)\sin(\pi y), & \text{if } x<0.5\\
-6\pi^2\sin(\pi x)\sin(\pi y), & \text{if } x\ge 0.5
\end{cases}
$$

**Figure 13: Numerical Solution for the 2D Discontinuous Poisson Equation.**

Because the diffusion coefficient is constant, the physics dictates that the solution $u$ and its normal derivative $\partial_x u$ must be continuous across the interface. This forces the second derivative $\partial_{xx}u$ to have a jump discontinuity, creating a $C^1$ that standard $C^\infty$ sharp twist (kink) MLPs cannot represent without numerical oscillations (Gibbs phenomenon). We augmented the standard loss with two explicit penalty terms to enforce the $C^1$ continuity at the interface $x=0.5$: the $C^0$ continuity loss $L_{\text{iface},u}=\mathbb{E}_{y\sim U[0,1]}[(u(0.5^-,y)-u(0.5^+,y))^2]$ and the $C^1$ continuity loss $L_{\text{iface},u_x}=\mathbb{E}_{y\sim U[0,1]}[(\partial_x u(0.5^-,y)-\partial_x u(0.5^+,y))^2]$.

**Neural network architecture and training details.** We approximate the solution $u(x,y)$ with a fully-connected multilayer perceptron (MLP) of depth 6 and width 64 using Tanh activations. The total loss is a composite of four distinct terms: the PDE residual $L_{\text{pde}}$, the Zero-Dirichlet boundary $L_{\text{bc}}$, and two explicit interface penalties, $L_{\text{iface},u}$ ($C^0$ continuity) and $L_{\text{iface},u_x}$ ($C^1$ continuity) at the $x=0.5$ discontinuity. The $L_{\text{pde}}$ is evaluated on $n_{\text{int}}=4096$ interior points, resampled each epoch from a biased distribution that oversamples the interface. The $L_{\text{bc}}$ and $L_{\text{iface}}$ terms are evaluated on $n_{\text{bc}}=2000$ and $n_{\text{iface}}=2000$ points, respectively. We train with Adam (learning rate $1\times 10^{-3}$) and a cosine annealing schedule down to $10^{-5}$ over 15,000 epochs, with gradient clipping at 1.0. A warm-up of 3,000 epochs is used, during which the optimizer only sees the $L_{\text{pde}}$ and $L_{\text{bc}}$ terms. After warmup, risk control is enabled: the interface losses $(L_{\text{iface},u}$ and $L_{\text{iface},u_x})$ are bundled with the CVaR penalty $(L_{\text{cvar}})$ at $\alpha=0.95$ to form a single $L_{\text{pen}}$ term. This $L_{\text{pen}}$ is then dynamically balanced against the $L_{\text{pde}}$ term using our adaptive weighting scheme. The $L_{\text{bc}}$ term remains active throughout with a static weight. All runs use double precision. For reporting, the metrics are measured on an independent $201\times 201$ grid against a high-resolution finite difference solution $u^\star$. The average runtime per iteration was about 0.014 s for RRa CVaR hinge and 0.016 s for the RRa mean excess.

**Figure 14: Tail Plot for the 2D Discontinuous Poisson equation**

| Model | $L_2^{\text{rel}}$ | $L_\infty$ | $Q_{95}$ |
|---|---:|---:|---:|
| RBA | 0.09435 | 0.3331 | 8.901 |
| CWP | 0.1030 | 0.3445 | 6.243 |
| RRa | 0.08626 | 0.2997 | 6.340 |
| RRaWMS | 0.08305 | 0.3276 | 5.749 |
| Baseline | 0.1019 | 0.3442 | 6.283 |

**Figure 15: 2D Discontinuous Poisson Performances**

The CCDF plot (Figure 14) of absolute residuals and table 15 for the discontinuous 2D Poisson case show that the two risk-aware variants dominate the tail. In particular, RRaPINN-WMS (ME surrogate) achieves the lowest $P_{95}$ residual (5.749), improving on the Baseline (6.283) and RBA (8.901) by roughly 8.5% and 35%, respectively, and closely followed by RRaPINN (CVar hinge surrogate) (6.340) and CWP (6.243). The extreme right tail in the CCDF reveals a markedly heavier tail for RBA, with non-negligible mass persisting beyond residual levels $r\approx 40$-55, whereas the other methods decay around $r\approx 38$-41. This indicates that RBA can leave rare, large violations near the interface, while risk-aware training explicitly suppresses such extremes. RRaPINN-WMS also delivers the best bulk error $(L_2 \text{ rel}=0.08305)$, improving on the Baseline $(0.1019)$; RRaPINN attains the lowest $L_\infty$ $(0.2997$ vs Baseline $0.3442)$, suggesting fewer localized spikes. Overall, the RRaPINN-based method reduce high-quantile residuals without sacrificing bulk accuracy, yielding a more reliable solution under discontinuities than the Baseline PINN (Vanilla), RBA its variants CWP.

### 5.6 Ablation study on the tail level $\alpha$

We study how the tail level $\alpha$, for $\alpha\in\{0.50,0.75,0.85,0.95,0.99\}$ affects accuracy and residual control across three PDEs on $[0,1]$, using the 1D heat, 1D viscous Burgers, and 2D Poisson to provide stable insights [^6]. The network is a fully-connected multilayer perceptron (MLP) with 4 hidden layers and 80 neurons per layer, employing the TanH activation function, with Adam optimizer learning rate $5\cdot 10^{-3}$, boundary/initial weights similar as the above mentioned experiments, and training budget are held fixed. After a T-warmup $(T=1000$ epochs), we switch to a tail-only objective with a mean-excess penalty and CVaR hinge ; the tail threshold $\varepsilon_t$ was updated each step from a detached CVaR estimate via an EMA with a small relative margin (no gradients flow through $\varepsilon_t$) and initialized at $\varepsilon_{t=0}=0.5$ for all problems. We trained our models over 10,000 iterations for $\alpha\in\{0.50,0.75,0.85,0.95,0.99\}$, and report test metrics on uniform grids $(250\times 250)$. We compute the relative $L_2$ error, the mean absolute residual, and the final threshold $\varepsilon$; and average of these metrics over the three PDEs (per-problem curves are provided in the appendix), which are presented in the figures 17. This setup isolates the effect of $\alpha$ on the active tail set and the strength of the tail gradients while keeping all other factors constant.

#### 5.6.1 CVaR-hinge penalty

**Figure 16: Ablation of the tail level $\alpha$ for the CVaR-hinge penalty, averaged over the 1D heat, 1D viscous Burgers, and 2D Poisson problems. We report relative $L_2$, mean absolute residual, and the final threshold $\varepsilon_t$.**

In Figure 16 metrics such as (Rel.$L_2$ and the mean absolute residual) improve as $\alpha$ increases from 0.50 to the mid range $(\alpha\approx 0.75$-0.85), then worsen again for very large $\alpha$. However, the mean absolute residual takes its smallest value decreases again $\alpha=0.99$ while the final $\varepsilon$ keeps on increasing as $\alpha$ increases. This matches the behavior of the CVaR-hinge, $P_{\text{hinge}}(\theta,\varepsilon)=\big[\mathrm{CVaR}_\alpha(R_\theta)-\varepsilon\big]_+^2$, with $\varepsilon$ updated by a detached EMA toward $(1-\text{margin})\,\mathrm{CVaR}_\alpha$. At low $\alpha$ the “tail” is broad, gradients resemble a smoothed MSE and dilute attention to the worst regions. Mid-range $\alpha$ concentrates weight on the hardest samples while preserving enough coverage for stable, low-variance updates, hence the best average errors. As $\alpha$ grows further, $\mathrm{CVaR}_\alpha$ (and thus $\varepsilon_t$) rises, the active set shrinks, and training over-focuses on a few extremes; this helps worst-case control but hurts bulk metrics (relative $L_2$ and mean residual).

**Practical takeaway.** For CVaR-hinge, a moderate tail level is a better spot: $\alpha\in[0.75,0.85]$ typically balances tail minimization and bulk accuracy. Use a small relative margin (5-20%) and an EMA $\beta\in[0.7,0.9]$; increase $\alpha$ (and possibly $\lambda_p$) only if the goal is stricter $L_\infty$ control.

#### 5.6.2 Mean-excess penalty

**Figure 17: Ablation of the tail level $\alpha$ for the mean-excess penalty, averaged over the 1D heat $(x,t)$, 1D viscous Burgers $(x,t)$, and 2D Poisson $(x,y)$ problems. We report relative $L_2$, mean absolute residual, and the final threshold $\varepsilon_t$.**

Figure 17 shows a clear trend: as the tail level $\alpha$ increases (i.e., the tail becomes tighter), the average relative $L_2$ error, the mean absolute residual, and the final threshold $\varepsilon_t$ all increase. This behavior is consistent with how the mean-excess penalty works. For smaller $\alpha$ the active set contains a larger portion of the domain, yielding lower-variance gradients and more benefit to the bulk error. As $\alpha$ grows, the penalty concentrates on ever rarer extremes; the CVaR at level $\alpha$ rises, so the EMA-driven threshold $\varepsilon_t\approx (1-\text{margin})\mathrm{CVaR}_\alpha$ also rises, and fewer points remain above the threshold. The result is stronger pressure on worst-case errors (useful for $L_\infty$ control) but less improvement on average metrics.

**Practical takeaway.** For mean-excess, moderate tails typically balance stability and coverage: $\alpha\in[0.5,0.95]$ with a small relative margin (5-20%) and EMA $\beta\in[0.7,0.9]$ are recommended. Very large $\alpha$ focuses too narrowly, inflates $\varepsilon_t$, and can under-serve the bulk.

## 6 Conclusion and Future Work

In this work, we introduce the Residual Risk-Aware Physics-Informed Neural Network (RRaPINN) framework. Our formulation unifies adaptive weighting in PINNs with distributionally robust optimization, yielding models that explicitly control high quantiles of the residual distribution rather than only the average discrepancy. We further derive a mean-excess (ME) surrogate for the CVaR penalty, which retains the same risk-sensitive interpretation while being easier to implement and tune. Classical weighting heuristics can be reinterpreted as special cases of our probabilistic view, and by leveraging CVaR-style risk measures we provide a direct bridge between risk-sensitive optimization and scientific machine learning. This offers a principled pathway toward PINNs that are not only accurate on average but whose worst-case residuals can be targeted and, in principle, bounded across the domain.

Practically, RRaPINNs leave both the PDE formulation and the network architecture unchanged: they operate purely at the loss level, keeping the standard mean residual as a base term and augmenting it with a simple risk-aware tail penalty. In this sense, they can be viewed as a drop-in modification of the residual loss with a small, interpretable set of knobs (notably the reliability level $\alpha$) that trades bulk accuracy (lower $\alpha$) against tail control (higher $\alpha$). Across 1D viscous Burgers, 1D heat, KdV, and Poisson equations (including a discontinuous forcing variant), RRaPINNs consistently improved tail behavior, reducing high residual quantiles and $L_\infty$ error while maintaining or improving bulk error relative to vanilla PINNs and strong baselines such as Residual-Based Attention, even in discontinuity regimes. In our experiments, the mean-excess (ME) surrogate of the CVaR was numerically more stable and achieved stronger tail control than a direct CVaR hinge.

Despite these benefits, RRaPINNs retain several limitations that point to natural improvements. Because collocation points are resampled independently at each epoch, the method is effectively memoryless, so difficult regions can be under-visited and the tail objective may chase transient hotspots rather than persistently fixing the same defects. The current risk is also applied to a global residual distribution, which can allow a single high-error subregion (e.g., a sharp interface) to dominate the tail budget and leave other parts of the domain under-corrected. Finally, risk-awareness is restricted to PDE residuals, while boundary, initial, and data-fidelity terms remain in standard MSE form, even when they drive the overall error. Future work could introduce lightweight memory mechanisms for hard points, adopt spatially localized risk budgets, and extend risk-aware training to BC/IC and data terms to better balance bulk accuracy and tail control.

Clarifying these questions would turn RRaPINNs from an empirically strong method into one with principled guaranties for both smooth and discontinuous PDEs.

## 7 Acknowledgement

This work was made possible by a grant from Carnegie Corporation (provided through the African Institute for Mathematical Sciences). I extend my sincere gratitude to my graduating institution, the University of KwaZulu-Natal (UKZN), for providing a rigorous academic environment and the opportunities that have shaped my personal and professional growth.

## References

Sokratis J. Anagnostopoulos, Juan Diego Toscano, Nikolaos Stergiopulos, and George Em Karniadakis. Residual-based attention in physics-informed neural networks. *Computer Methods in Applied Mechanics and Engineering*, 421:116805, 2024. ISSN 0045-7825. doi: https://doi.org/10.1016/j.cma.2024.116805. URL https://www.sciencedirect.com/science/article/pii/S0045782524000616.

Abraham Charnes and William W Cooper. Chance-constrained programming. *Management science*, 6(1):73–79, 1959.

John C Duchi, Tatsunori B Hashimoto, and Hongseok Namkoong. Learning models with uniform performance via distributionally robust optimization. In *AISTATS*, 2018.

Darrell Duffie and Jun Pan. An overview of value at risk. *Journal of derivatives*, 4(3):7–49, 1997.

Yanbo Fan, Siwei Lyu, Yiming Ying, and Baogang Hu. Learning with average top-k loss. In I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, *Advances in Neural Information Processing Systems*, volume 30. Curran Associates, Inc., 2017. URL https://proceedings.neurips.cc/paper_files/paper/2017/file/6c524f9d5d7027454a783c841250ba71-Paper.pdf.

Enrique Fernandez-Cara and Arnaud Münch. Strong convergent approximations of null controls for the 1d heat equation. *SeMA journal*, 61(1):49–78, 2013.

R Fletcher. An l1 penalty method for nonlinear constraints. *Numerical optimization*, 1984:26–40, 1985.

Zhiwei Gao, Liang Yan, and Tao Zhou. Failure-informed adaptive sampling for pinns, 2023. URL https://arxiv.org/abs/2210.00279.

Ameya D. Jagtap and George Em Karniadakis. Extended physics-informed neural networks (xpinns): A generalized space-time domain decomposition based deep learning framework for nonlinear partial differential equations. In *AAAI Spring Symposium on Machine Learning for Physical Sciences*, 2021.

George Em Karniadakis, Ioannis G Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and Liu Yang. Physics-informed machine learning. *Nature Reviews Physics*, 3(6):422–440, 2021.

Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization, 2017. URL https://arxiv.org/abs/1412.6980.

Diederik J. Korteweg and Gustav de Vries. On the change of form of long waves advancing in a rectangular canal, and on a new type of long stationary waves. *Philosophical Magazine*, 39(240):422–443, 1895.

Aditi Krishnapriyan, Amir Gholami, Shandian Zhe, Robert Kirby, and Michael W Mahoney. Characterizing possible failure modes in physics-informed neural networks. *Advances in Neural Information Processing Systems*, 34:26548–26560, 2021.

I.E. Lagaris, A. Likas, and D.I. Fotiadis. Artificial neural networks for solving ordinary and partial differential equations. *IEEE Transactions on Neural Networks*, 9(5):987–1000, 1998. ISSN 1045-9227. doi: 10.1109/72.712178. URL http://dx.doi.org/10.1109/72.712178.

Y Li, M Li, and YC Hon. Improved finite integration method for multi-dimensional nonlinear burgers’ equation with shock wave. *Neural Parallel Sci. Comput*, 23:63–86, 2015.

Huafeng Liu, Yiran Fu, Jingyue Shi, Liping Jing, and Jian Yu. Learning ood robust neural operator with risk-averse stochastic optimization. In *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2*, KDD ’25, page 1799–1810, New York, NY, USA, 2025. Association for Computing Machinery. ISBN 9798400714542. doi: 10.1145/3711896.3737020. URL https://doi.org/10.1145/3711896.3737020.

Lu Lu, Xuhui Meng, Zhiping Mao, and George Em Karniadakis. Deepxde: A deep learning library for solving differential equations. *SIAM Review*, 63(1):208–228, 2021.

Kuang Luo, Jingshang Zhao, Yingping Wang, Jiayao Li, Junjie Wen, Jiong Liang, Henry Soekmadji, and Shaolin Liao. Physics-informed neural networks for pde problems: a comprehensive review. *Artificial Intelligence Review*, 58, 07 2025. doi: 10.1007/s10462-025-11322-7.

Levi McClenny and Ulisses Braga-Neto. Self-adaptive physics-informed neural networks using a soft attention mechanism. In *ICASSP*, 2020.

Levi D. McClenny and Ulisses M. Braga-Neto. Self-adaptive physics-informed neural networks. *Journal of Computational Physics*, 474:111722, 2023. doi: 10.1016/j.jcp.2022.111722. URL https://doi.org/10.1016/j.jcp.2022.111722.

Hongseok Namkoong and John C Duchi. Variance-based regularization with convex objectives. In *NeurIPS*, 2017.

Arkadi Nemirovski and Alexander Shapiro. Convex approximations of chance constrained programs. *SIAM Journal on Optimization*, 17(4):969–996, 2007.

Nasim Rahaman, Aristide Baratin, Devansh Arpit, Felix Draxler, Min Lin, Fred Hamprecht, Yoshua Bengio, and Aaron Courville. On the spectral bias of neural networks. In *International conference on machine learning*, pages 5301–5310. PMLR, 2019.

Maziar Raissi, Paris Perdikaris, and George Em Karniadakis. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *Journal of Computational Physics*, 378:686–707, 2019.

R Tyrrell Rockafellar, Stanislav Uryasev, et al. Optimization of conditional value-at-risk. *Journal of risk*, 2:21–42, 2000.

Jonathan J Ruel and Matthew P Ayres. Jensen’s inequality predicts effects of environmental variation. *Trends in Ecology & Evolution*, 14(9):361–366, 1999.

Chenhao Si and Ming Yan. Convolution-weighting method for the physics-informed neural network: A primal-dual optimization perspective, 2025. URL https://arxiv.org/abs/2506.19805.

Alice E Smith, David W Coit, Thomas Baeck, David Fogel, and Zbigniew Michalewicz. Penalty functions. *Handbook of evolutionary computation*, 97(1):C5, 1997.

Haris Suhendar, Muhammad Ridho Pratama, and Michael Setyanto Silambi. Mesh-free solution of 2d poisson equation with high frequency charge patterns using data-free physics informed neural network. In *Journal of Physics: Conference Series*, volume 2866, page 012053. IOP Publishing, 2024.

Han Wang and Zhi-Qin John Zhang. When and why pinns fail to train: A neural tangent kernel perspective. *Journal of Computational Physics*, 449:110768, 2022.

Sifan Wang, Yujun Teng, and Paris Perdikaris. Understanding and mitigating gradient pathologies in physics-informed neural networks. *SIAM Journal on Scientific Computing*, 43(5):A3055–A3081, 2021.

Sifan Wang, Xinling Yu, and Paris Perdikaris. When and why pinns fail to train: A neural tangent kernel perspective. *Journal of Computational Physics*, 449:110768, 2022. doi: 10.1016/j.jcp.2021.110768.

Sifan Wang, Shyam Sankaran, and Paris Perdikaris. Respecting causality improves training of physics-informed neural networks. *Computer Methods in Applied Mechanics and Engineering*, 404:115783, 2023. doi: 10.1016/j.cma.2022.115783.

Chenxi Wu, Min Zhu, Qinyang Tan, Yadhu Kartha, and Lu Lu. A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks. *Computer Methods in Applied Mechanics and Engineering*, 403:115671, 2023.

Yibo Yang, Zhiping Mao, Sifan Wang, and George Em Karniadakis. Learning physical constraints with neural networks: A curriculum learning approach. *Neural Networks*, 145:113–127, 2022.

## Appendix

## .1 Residual Risk Aware PINNs Formulation

We have recast PINN training as a risk-aware program:

$$
\min_{\theta,\varepsilon>0}
\underbrace{L_{\text{PINN}}(\theta)}_{\text{physics + boundary}}
\quad \text{s.t.}\quad
\underbrace{\mathrm{CVaR}_\alpha\big(|r(X;\theta)|\big)}_{\text{tail risk of residuals}} \le \varepsilon,
$$

and provided its empirical, optimizable relaxation (31), whose adaptive Top-k weighting arises necessarily from the convex CVaR formulation. This yields a principled, tail-robust PINN that targets reliability beyond average accuracy and stands in contrast to heuristic reweighting or sampling rules.

## .2 RRaPINN Algorithm Details

### .2.1 RRaPINN Algorithm Pseudocode

The core of our method is a two-phase training process. After a standard MSE-based warmup, the algorithm transitions to a “strict tail” phase. In this phase, the optimizer is driven only by the anchor (IC/BC) losses and a dynamic risk-averse penalty. Crucially, the weight of this penalty, $\lambda_p$, is computed dynamically using detached, exponentially-moving-average (EMA) scales of the base (MSE) loss and the core penalty, a mechanism inspired by risk-balancing adaptation.

```text
Algorithm 1 RRaPINN (CVaR-Hinge or Mean-Excess) with Stiff/Smooth Scheduling

Require: epochs E, warmup W, CVaR level α, anchor weights (λic, λbc), base penalty seed
λcfg, risk init εinit, EMA decays (βs, βε), margin η, bounds (λmin, λmax), schedule ∈
{SMOOTH_FIRST, STIFF_FIRST}

1: Init: ε ← εinit, λp ← λcfg, Sb ← 1, Sp ← 1, optimizer O
2: for e = 1, . . . , E do
3:   Sample interior Xint, IC (Xic, uic), BC (XL, uL, XR, uR)
4:   Lic ← MSE(fθ(Xic), uic); Lbc ← 1/2 (MSE(fθ(XL), uL) + MSE(fθ(XR), uR))
5:   r ← R(Xint; θ); Lbase ← mean(r^2)
6:   Lanchor ← λic Lic + λbc Lbc
7:   Tail stat & threshold (short): c ← CVaRα(|r|); ε ← min(ε, EMAβε((1 − η)c, ε))
8:   Penalty core:
9:   if HINGE then Lcore ← (max(0, c − ε))^2
10:  else (ME) Lcore ← mean(max(0, |r| − ε)^2)
11:  end if
12:  Partial balancer (Optional):
     Sb ← EMAβs(Sb, stopgrad(Lbase));
     Sp ← EMAβs(Sp, stopgrad(Lcore));
     λp ← clip(λcfg Sb / (Sp + δ), λmin, λmax)
13:  Schedule & loss:
14:  if SMOOTH_FIRST then
15:      if e ≤ W then L ← Lbase + λic Lic + λbc Lbc
16:      else L ← Lbase + λp Lcore + Lanchor
17:      end if
18:  else (STIFF_FIRST)
19:      if e ≤ W then L ← λp Lcore + Lanchor
20:      else L ← Lbase + λp Lcore + λic Lic + λbc Lbc
21:      end if
22:  end if
23:  Update: θ ← Step(O, ∇θL) with gradient clipping
24: end for
25: return θ
```

**Note.** For stiff problems, prefer `STIFF_FIRST`: control the tail (penalty) during warmup, then emphasize bulk. For smooth problems, prefer `SMOOTH_FIRST`: warm up on the bulk, then add tail control.

## .3 From CVar to the Empirical CVaR via the Rockafellar-Uryasev Program

**Remark .1 (Connection between CVaR and Average Top-k Loss).** The empirical CVaR$_\alpha$ formulation,

$$
\mathrm{CVaR}_\alpha(R)=\min_{\lambda\in\mathbb{R}}
\left\{
\lambda+\frac{1}{(1-\alpha)N}\sum_{i=1}^N [R_i-\lambda]_+
\right\}, \tag{48}
$$

is mathematically equivalent to the Average Top-k (ATk) loss introduced by Fan et al. [2017],

$$
L_{\text{ATk}}=\min_{\lambda\ge 0}
\left\{
\frac{1}{N}\sum_{i=1}^N [R_i-\lambda]_+ + \frac{k}{N}\lambda
\right\}. \tag{49}
$$

Identifying $\alpha=1-\frac{k}{N}$ shows that minimizing CVaR at level $\alpha$ is equivalent to averaging the largest $k$ individual losses, that is, the top-k tail of the empirical loss distribution as defined in [Fan et al., 2017]. This provides a direct bridge between risk-sensitive learning based on CVaR and the robust-learning interpretation of top-k averaging.

**Proposition .2 (Empirical RU minimizer and value).** Let $R_{(1)}(\theta)\le \cdots \le R_{(N)}(\theta)$ be the order statistics of $R_1,\dots,R_N$. Fix $\alpha\in(0,1)$ and set $t:=(1-\alpha)N$, $m:=\lfloor t\rfloor$, $s:=t-m\in[0,1)$. Consider

$$
\hat{\phi}_N(\eta)=\eta+\frac{1}{t}\sum_{i=1}^N (R_i-\eta)_+,\qquad (u)_+ := \max\{u,0\}. \tag{50}
$$

Then

$$
\arg\min_{\eta\in\mathbb{R}} \hat{\phi}_N(\eta)=
\begin{cases}
\{R_{(N-m)}\}, & \text{if } s>0 \text{ and there are no ties at } R_{(N-m)},\\
[R_{(N-m)},R_{(N-m+1)}], & \text{if } s=0 \text{ or there is a tie at the boundary.}
\end{cases} \tag{51}
$$

**Proof.** 1) Subgradient of $\hat{\phi}_N$. For fixed $R_i$, the function $\eta\mapsto (R_i-\eta)_+$ is convex and piecewise linear with

$$
\frac{d}{d\eta}(R_i-\eta)_+ =
\begin{cases}
-1, & \eta<R_i,\\
[-1,0], & \eta=R_i,\\
0, & \eta>R_i.
\end{cases} \tag{52}
$$

Summing and dividing by $t$,

$$
\partial \hat{\phi}_N(\eta)=\left[
1-\frac{1}{t}\#\{i:R_i\ge \eta\},\ 
1-\frac{1}{t}\#\{i:R_i>\eta\}
\right], \tag{53}
$$

Where the sign $\#G$ means cardinality (number of element) in the set $G$. By convex optimality, $\eta^\star$ minimizes $\hat{\phi}_N$ iff $0\in \partial\hat{\phi}_N(\eta^\star)$, i.e.

$$
\#\{i:R_i>\eta^\star\}\le t \le \#\{i:R_i\ge \eta^\star\}. \tag{54}
$$

2) What happens between consecutive order statistics. Fix an index $j\in\{0,1,\dots,N\}$ and consider $\eta\in(R_{(j)},R_{(j+1)})$ (with the conventions $R_{(0)}=-\infty$, $R_{(N+1)}=+\infty$). In this open interval, the active set is constant:

$$
\#\{i:R_i>\eta\}=N-j,\qquad \#\{i:R_i\ge \eta\}=N-j. \tag{55}
$$

Hence the one-sided derivatives coincide and

$$
\frac{d}{d\eta}\hat{\phi}_N(\eta)=1-\frac{N-j}{t}\qquad \text{for } \eta\in(R_{(j)},R_{(j+1)}). \tag{56}
$$

In particular, on the special interval $(R_{(N-m)},R_{(N-m+1)})$ the slope equals

$$
1-\frac{m}{t}=\frac{s}{t}. \tag{57}
$$

3) Left and right behaviour at the boundary $R_{(N-m)}$. We will examine $\hat{\phi}_N$ immediately to the left and to the right of $R_{(N-m)}$.

Right of $R_{(N-m)}$. By (56)-(57), for every $\eta\in(R_{(N-m)},R_{(N-m+1)})$

$$
\frac{d}{d\eta}\hat{\phi}_N(\eta)=\frac{s}{t}\ge 0. \tag{58}
$$

Thus $\hat{\phi}_N$ is nondecreasing to the right of $R_{(N-m)}$ and strictly increasing there if $s>0$.

Left of $R_{(N-m)}$ (no ties case). If there are no ties at $R_{(N-m)}$, then for $\eta\in(R_{(N-m-1)},R_{(N-m)})$ we have $\#\{i:R_i>\eta\}=m+1$, so by (56)

$$
\frac{d}{d\eta}\hat{\phi}_N(\eta)=1-\frac{m+1}{t}=\frac{s-1}{t}<0, \tag{59}
$$

because $s\in[0,1)$.

At the boundary with ties. Let $\vartheta:=R_{(N-m)}$ and denote $A:=\#\{i:R_i>\vartheta\}$ and $B:=\#\{i:R_i=\vartheta\}$. By ranking, $A\le m$ (at most $m$ elements exceed $\vartheta$) and $B\ge 1$. Since $t=m+s\in[m,m+1)$, we have

$$
A\le m\le t\le m+1 \le A+B. \tag{60}
$$

Therefore the optimality condition (54) holds at $\eta=\vartheta$ even when $B>1$ (ties), i.e. $0\in \partial\hat{\phi}_N(\vartheta)$.

4) Minimizer set by cases.

**Case $s>0$ and no ties at $R_{(N-m)}$.** By (59) $\hat{\phi}_N$ is strictly decreasing just to the left of $R_{(N-m)}$, and by (58) it is strictly increasing just to the right. By convexity, the unique minimizer is the junction point:

$$
\eta^\star = R_{(N-m)}. \tag{61}
$$

**Case $s=0$ (integer tail size).** Then (58) says the slope on $(R_{(N-m)},R_{(N-m+1)})$ is 0, so $\hat{\phi}_N$ is constant on that open interval. Convexity and the left derivative $<0$ (as in (59) with $s=0$) imply that every point in the closed interval

$$
\eta^\star \in [R_{(N-m)},R_{(N-m+1)}] \tag{62}
$$

is a minimizer (a flat bottom).

**Case ties at the boundary.** From the boundary check above, $0\in\partial\hat{\phi}_N(R_{(N-m)})$, so $R_{(N-m)}$ is a minimizer. If, in addition, $R_{(N-m)}=R_{(N-m+1)}$ numerically, the set $[R_{(N-m)},R_{(N-m+1)}]$ is a singleton equal to that tied value, hence also a valid description of the minimizers in the statement. (When $s=0$ and there are ties, the whole flat interval of minimizers remains valid.)

This completes the case analysis and the characterization of $\arg\min \hat{\phi}_N$.

**Proposition .3 (Empirical CVaR equals a fractional tail average (Proof of the proposition (4.3))).** Let $R_1,\dots,R_N\in\mathbb{R}$ and let $R_{(1)}\le \cdots \le R_{(N)}$ be the order statistics (ascending). Fix $\alpha\in(0,1)$ and set $t:=(1-\alpha)N$, $m:=\lfloor t\rfloor$, $s:=t-m\in[0,1)$. Consider the empirical Rockafellar-Uryasev objective

$$
\hat{\phi}_N(\eta)=\eta+\frac{1}{(1-\alpha)N}\sum_{i=1}^N (R_i-\eta)_+
=\eta+\frac{1}{t}\sum_{i=1}^N (R_i-\eta)_+.
$$

Then its minimum value (the empirical CVaR) is

$$
\widehat{\mathrm{CVaR}}_\alpha(R):=\inf_\eta \hat{\phi}_N(\eta)
=
\frac{1}{t}\left(\sum_{i=N-m+1}^N R_{(i)} + sR_{(N-m)}\right). \tag{63}
$$

In particular, if $s=0$ (i.e., $t$ is an integer), then

$$
\widehat{\mathrm{CVaR}}_\alpha(R)=\frac{1}{t}\sum_{i=N-t+1}^N R_{(i)},
$$

the average of the top $t$ samples. If there is a tie at the boundary $(R_{(N-m)}=R_{(N-m+1)})$, the same Top-k form holds with $k=\lceil t\rceil$.

**Proof via the primal RU objective.** Let $t=(1-\alpha)N=m+s$ with $m=\lfloor t\rfloor$ and $s\in[0,1)$. Fix $\eta\in(R_{(N-m)},R_{(N-m+1)})$, so exactly the top $m$ samples exceed $\eta$. Then

$$
\sum_{i=1}^N (R_i-\eta)_+
=
\sum_{i=N-m+1}^N (R_{(i)}-\eta)
=
\sum_{i=N-m+1}^N R_{(i)} - m\eta. \tag{64}
$$

Substituting in $\hat{\phi}_N(\eta)=\eta+\frac{1}{t}\sum(R_i-\eta)_+$ gives the affine form

$$
\hat{\phi}_N(\eta)=\frac{1}{t}\sum_{i=N-m+1}^N R_{(i)}+\frac{s}{t}\eta, \tag{65}
$$

so on this interval the slope is $s/t$.

**Case 1: $s>0$ and no ties at $R_{(N-m)}$.** For $\eta$ just below $R_{(N-m)}$, at least $m+1$ samples exceed $\eta$, so

$$
\hat{\phi}_N'(\eta^+)=1-\frac{1}{t}\#\{i:R_i>\eta\}<0. \tag{66}
$$

Immediately to the right, using the affine form (65) of $\hat{\phi}_N(\eta)$ we see that the slope is $s/t>0$. Hence $\hat{\phi}_N$ decreases up to $\eta=R_{(N-m)}$ and increases after, so the unique minimizer is

$$
\eta^\star = R_{(N-m)}. \tag{67}
$$

**Case 2: $s=0$ (integer tail).** Then the slope on $(R_{(N-m)},R_{(N-m+1)})$ is 0, hence $\hat{\phi}_N$ is constant there. By convexity, every point in the closed interval

$$
\eta^\star \in [R_{(N-m)},R_{(N-m+1)}] \tag{68}
$$

is a minimizer.

**Case 3: Ties at the boundary.** If $R_{(N-m)}=R_{(N-m+1)}$, the numeric interval degenerates, but the value attained at that boundary is the same; the (dual) fractional mass $s$ may be distributed across the tied block without changing the value.

In all cases, evaluating at $\eta=R_{(N-m)}$ yields

$$
\inf_\eta \hat{\phi}_N(\eta)
=
\frac{1}{t}\sum_{i=N-m+1}^N R_{(i)}+\frac{s}{t}R_{(N-m)}, \tag{69}
$$

which is the fractional tail average.

## .4 CVaR-consistency of the mean-squares RRA Formulation.

**Proposition .4.** Fix $\alpha\in(0,1)$ and Let $(R_i)_{i=1}^N$ be nonnegative residual magnitudes, let $t:=\lfloor(1-\alpha)N\rfloor$ be an integer. Consider $\varepsilon\ge 0$, and the weights $w_i=\frac{N}{t}\ge 0$ for $i\in I_{\text{tail-t}}$ and 0 otherwise, satisfying the following

$$
\frac{1}{N}\sum_{i=1}^N w_i = 1 \quad \text{(equivalently, } \sum_i w_i = N\text{)}. \tag{70}
$$

Define the mean-squares robust penalty as $P_{\text{ms}}(\theta,\varepsilon,w):=\frac{1}{N}\sum_{i=1}^N w_i(R_i-\varepsilon)_+^2$. Then

$$
P_{\text{ms}}(\theta,\varepsilon,w)\ge \big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big)_+^2. \tag{71}
$$

**Proof.** Let $z_i:=(R_i-\varepsilon)_+\ge 0$ and $\tilde{w}_i:=w_i/N$ so that $\tilde{w}_i\ge 0$ and $\sum_i \tilde{w}_i=1$ by (70). By Jensen’s inequality for the convex map $x\mapsto x^2$,

$$
\frac{1}{N}\sum_{i=1}^N w_i z_i^2
=
\sum_{i=1}^N \tilde{w}_i z_i^2
\ge
\left(\sum_{i=1}^N \tilde{w}_i z_i\right)^2
=
\left(\frac{1}{N}\sum_{i=1}^N w_i z_i\right)^2, \tag{72}
$$

Therefore, we have

$$
P_{\text{ms}}(R;\varepsilon,w)\ge
\left(
\frac{1}{N}\sum_{i=1}^N w_i(R_i-\varepsilon)_+
\right)^2. \tag{73}
$$

Since $x\mapsto (x-\varepsilon)_+$ is convex and nondecreasing, Jensen’s inequality [Ruel and Ayres, 1999] yields

$$
\frac{1}{N}\sum_{i=1}^N w_i(R_i-\varepsilon)_+
\ge
\left(
\frac{1}{N}\sum_{i=1}^N w_i R_i - \varepsilon
\right)_+, \tag{74}
$$

Therefore, we have

$$
\left(
\frac{1}{N}\sum_{i=1}^N w_i(R_i-\varepsilon)_+
\right)^2
\ge
\left(
\frac{1}{N}\sum_{i=1}^N w_i R_i - \varepsilon
\right)_+^2. \tag{75}
$$

from Eq. (73) and (75) we conclude that:

$$
P_{\text{ms}}(\theta,\varepsilon,w)\ge
\left(
\frac{1}{N}\sum_{i=1}^N w_iR_i-\varepsilon
\right)_+^2. \tag{76}
$$

Fix $\alpha\in(0,1)$ and let $t:=\lfloor(1-\alpha)N\rfloor$. As defined in eq. (26), if $w_i=\frac{N}{t}$ for $i\in I_{\text{tail-t}}$ and $w_i=0$ otherwise, we have

$$
\frac{1}{N}\sum_{i=1}^N w_iR_i
=
\frac{1}{t}\sum_{i\in I_{\text{tail-t}}}R_i
=
\widehat{\mathrm{CVaR}}_\alpha(R), \tag{77}
$$

Therefore, (76) implies the bound

$$
P_{\text{ms}}(\theta,\varepsilon,w)\ge
\big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big)_+^2. \tag{78}
$$

$\square$

## .5 Statistical Interpretation of the Empirical CVaR

**Interpretation of averaging the tail.** Recall $R:=|r(X;\theta)|$ with $X\sim\mu$, and let $\mathrm{CVaR}_\alpha(R)$ be defined by the Rockafellar-Uryasev (RU) program

$$
\mathrm{CVaR}_\alpha(R)=\inf_{\eta\in\mathbb{R}}
\left\{
\phi(\eta):=\eta+\frac{1}{1-\alpha}\mathbb{E}\big((R-\eta)_+\big)
\right\}. \tag{79}
$$

At any minimizer $\eta^\star\in[q_\alpha^-,q_\alpha^+]$,

$$
\mathrm{CVaR}_\alpha(R)=\eta^\star+\frac{1}{1-\alpha}\mathbb{E}\big((R-\eta^\star)_+\big),
$$

which is the average level of $R$ over the worst $(1-\alpha)$ fraction of outcomes. When the CDF is continuous at the quantile, this reduces exactly to the conditional mean $\mathbb{E}[R\mid R\ge \mathrm{VaR}_\alpha(R)]$; otherwise, it averages the strict upper tail and includes just enough of the atom at $\eta^\star$ to fill the $(1-\alpha)$ mass.

## .6 Gradients and Subgradients

**Lemma .5 (Local constancy and measure-zero switches).** If $R_i(\theta)\ne R_j(\theta)$ for all $i\ne j$, then there exists a neighborhood $U$ of $\theta$ in which the permutation $\pi$ is constant and hence $I_{\text{top-k}}(\theta)$ is constant. The set of $\theta$ where some $R_i(\theta)=R_j(\theta)$ or $R_i(\theta)=\varepsilon$ (or $r(x_i;\theta)=0$) is a finite union of co-dimension $\ge 1$ manifolds and thus has Lebesgue measure zero.

**Idea.** Distinct order statistics remain distinct under small perturbations, so the sorting permutation is locally constant; equalities $R_i=R_j$, $R_i=\varepsilon$, $r=0$ define level sets of smooth maps.

### .6.1 CVaR violation penalty.

Ignoring measure-zero tie sets (Lemma .5), $I_{\text{top-k}}$ is locally constant and for

$$
P_{\text{hinge}}(\theta,\varepsilon)=\lambda_p\big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big)_+^2,
$$

we have

$$
\nabla_\theta P_{\text{hinge}}(\theta,\varepsilon)
=
2\cdot \mathbf{I}\{\widehat{\mathrm{CVaR}}_\alpha(R)>\varepsilon\}
\big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big)\cdot \nabla_\theta R_i(\theta),
\qquad
\nabla_\theta R_i(\theta)=\nabla_\theta |r(x_i;\theta)|. \tag{80}
$$

Whenever $r(x_i;\theta)\ne 0$,

$$
\nabla_\theta |r(x_i;\theta)|
=
\mathrm{sign}\big(r(x_i;\theta)\big)\nabla_\theta r(x_i;\theta). \tag{81}
$$

At $r(x_i;\theta)=0$, the Clarke subdifferential is

$$
\partial_\theta |r(x_i;\theta)|
=
\{s\nabla_\theta r(x_i;\theta): s\in[-1,1]\}.
$$

**Gradients w.r.t. $\varepsilon$ and its parameter $\xi$.** With $\varepsilon=\psi(\xi)=\log(1+e^\xi)$ (softplus to ensure positivity), we have $\frac{\partial \varepsilon}{\partial \xi}=\psi'(\xi)=\sigma(\xi)=\frac{1}{1+e^{-\xi}}$. We have the following derivatives

$$
\frac{\partial P_{\text{hinge}}(\theta,\varepsilon)}{\partial \varepsilon}
=
-2\cdot \mathbf{I}\{\widehat{\mathrm{CVaR}}_\alpha(R)>\varepsilon\}
\big(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\big). \tag{82}
$$

$$
\frac{\partial P_{\text{hinge}}(\theta,\varepsilon)}{\partial \xi}
=
\frac{\partial P_{\text{hinge}}(\theta,\varepsilon)}{\partial \varepsilon}
\cdot
\frac{\partial \varepsilon}{\partial \xi}
=
-2\cdot \mathbf{I}\{\widehat{\mathrm{CVaR}}_\alpha(R)>\varepsilon\}
\left(\widehat{\mathrm{CVaR}}_\alpha(R)-\varepsilon\right)\cdot \sigma(\xi). \tag{83}
$$

### .6.2 Squared-violation penalty.

For $v_i(\theta,\varepsilon):=(R_i(\theta)-\varepsilon)_+$ and any fixed Top-k selection,

$$
\nabla_\theta
\left[
\frac{1}{k}\sum_{i\in I_{\text{top-k}}} v_i^2
\right]
=
\frac{2}{k}\sum_{i\in I_{\text{top-k}}}
\mathbf{I}\{R_i>\varepsilon\}(R_i-\varepsilon)\nabla_\theta R_i. \tag{84}
$$

At $R_i=\varepsilon$, take any subgradient in the interval between one-sided limits or smooth $(\cdot)_+$ (e.g., softplus/Huber).

**Gradients w.r.t. $\varepsilon$ and its parameter $\xi$.**

$$
\frac{\partial}{\partial \varepsilon}
\left[
\frac{1}{k}\sum_{i\in I_{\text{top-k}}} v_i^2
\right]
=
-\frac{2}{k}\sum_{i\in I_{\text{top-k}}}
\mathbf{I}\{R_i>\varepsilon\}(R_i-\varepsilon), \tag{85}
$$

Hence,

$$
\frac{\partial}{\partial \xi}
\left[
\frac{1}{k}\sum_{i\in I_{\text{top-k}}} v_i^2
\right]
=
-\frac{2}{k}
\left(
\sum_{i\in I_{\text{top-k}}}
\mathbf{I}\{R_i>\varepsilon\}(R_i-\varepsilon)
\right)\sigma(\xi). \tag{86}
$$

Adding the regularizer $\gamma_\varepsilon \varepsilon$ contributes $\partial_\xi(\gamma_\varepsilon \varepsilon)=\gamma_\varepsilon \sigma(\xi)$. We can confirm via the above derivation results that the update of $\varepsilon$ is very sensible and depends on factors such as $\gamma_\varepsilon$and the values of the tail excess or individual excess.

## .7 Training Curves

These curves were are $L_2$ relative error recorded every 500 epochs using validation data sets randomly generated.

### .7.1 1D Viscous Burger Equation

The training history, including the evolution of the relative error, is presented in Figure (18). From this plot, we can clearly notice that the RRaPINN-based models have a more stable performance amelioration compare to CWPINN, RBAPINN, and Baseline PINN.

**Figure 18: L2 Relative Error Training History for the 1D Viscous Burger Equation**

### .7.2 1D Heat Equation

The most stable learning curves appears to be that of RBA followed by the baseline. CWP reached a very low values very quickly but jumped unexpectedly later on and after get more stable towards the end. RRa-based models seems to have similar behavior with CWP, but achieve lower values toward the end when the robust tail manages to accomplish its duty.

**Figure 19: L2 Relative Error Training History for the 1D Heat Equation**

### .7.3 KdV Equation

All methods are very unstable before epoch 8k, and get stabilized after . RRaWMS and RBA have the most important decays, followed by RRa, CWP and Baseline PINNs.

### .7.4 2D Poisson Equation

All methods are very unstable before epoch 11k, and get stabilized after . RRaWMS and RBA have the most important decays, followed by RRa, CWP and Baseline PINNs.

**Figure 20: L2 Relative Error Training History for the KdV Equation**

**Figure 21: L2 Relative Error Training History for the 2D Poisson Equation**

## .8 Ablation study Curves

### .8.1 CVaR Hinge penalty

**Figure 22: Ablation on $\alpha$ for the 1D viscous Burgers equation.**  
(a) Relative $L_2$ vs. $\alpha$  
(b) Mean absolute residual vs. $\alpha$

**Figure 23: Ablation on $\alpha$ for the 1D heat equation.**  
(a) Relative $L_2$ vs. $\alpha$  
(b) Mean absolute residual vs. $\alpha$

### .8.2 Mean Excess penalty

**Figure 24: Ablation on $\alpha$ for the 2D Poisson equation.**  
(a) Relative $L_2$ vs. $\alpha$  
(b) Mean absolute residual vs. $\alpha$

**Figure 25: Ablation on $\alpha$ for the 1D viscous Burgers equation.**  
(a) Relative $L_2$ vs. $\alpha$  
(b) Mean absolute residual vs. $\alpha$

**Figure 26: Ablation on $\alpha$ for the 1D heat equation.**  
(a) Relative $L_2$ vs. $\alpha$  
(b) Mean absolute residual vs. $\alpha$

**Figure 27: Ablation on $\alpha$ for the 2D Poisson equation.**  
(a) Relative $L_2$ vs. $\alpha$  
(b) Mean absolute residual vs. $\alpha$

---

[^4]: Theoretical justification in Appendix .6  
[^5]: More details about the algorithm are provided in the appendix .2  
[^6]: Individual plot are provided in the Appendix .8
```

Примечания по качеству транскрипции:
- Основа текста извлечена полно по 38 страницам.
- Формулы приведены в LaTeX/Markdown по возможности точно.
- Некоторые места исходного OCR содержат явные артефакты или опечатки автора/OCR:
  - `emphhyperbolic`, `emphAdam`, `15, 0000`, `Performancees`, `CVar`, `Cummulative`, `guaranties` и др.
  - Я сохранил их максимально близко к источнику, не исправляя смысл.
- Иллюстрации с графиками и heatmap’ами воспроизведены как подписи/описания, без попытки реконструкции самих графиков в коде.
- Если хотите, следующим сообщением я могу:
  1. сделать **очищенную версию Markdown** с исправлением OCR-ошибок без изменения смысла;
  2. оформить это как **готовый `.md` файл**;
  3. отдельно извлечь только **таблицы**, только **формулы**, или только **bibliography**.