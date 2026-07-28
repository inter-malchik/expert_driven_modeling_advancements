```markdown
# Vanishing Stacked-Residual PINN for State Reconstruction of Hyperbolic Systems

Katayoun Eshkofti and Matthieu Barreau

## Abstract

In a more connected world, modeling multi-agent systems with hyperbolic partial differential equations (PDEs) offers a compact, physics-consistent description of collective dynamics. However, classical control tools need adaptation for these complex systems. Physics-informed neural networks (PINNs) provide a powerful framework to fix this issue by inferring solutions to PDEs by embedding governing equations into the neural network. A major limitation of original PINNs is their inability to capture steep gradients and discontinuities in hyperbolic PDEs. To tackle this problem, we propose a stacked residual PINN method enhanced with a vanishing viscosity mechanism. Initially, a basic PINN with a small viscosity coefficient provides a stable, low-fidelity solution. Residual correction blocks with learnable scaling parameters then iteratively refine this solution, progressively decreasing the viscosity coefficient to transition from parabolic to hyperbolic PDEs. Applying this method to traffic state reconstruction improved results by an order of magnitude in relative $L^2$ error, demonstrating its potential to accurately estimate solutions where original PINNs struggle with instability and low fidelity.

## I. INTRODUCTION

Quasi-linear hyperbolic partial differential equations (PDEs) are crucial in modern control problems, emerging in a wide range of applications, from fluid dynamics to electrical energy transportation and traffic flow [1]. A notable example is the role of the Hamilton-Jacobi equation in optimal and predictive control, highlighting the ubiquity of hyperbolic PDEs across both physical modeling and abstract optimization applications in control theory. State reconstruction and identification of systems governed by hyperbolic PDEs is of fundamental interest, as it allows for estimating the complete evolution of the system from partial and noisy observations. This capability is key for monitoring distributed systems and enables subsequent control.

However, model identification and state reconstruction for quasi-linear hyperbolic PDEs are challenging due to their nonlinear dynamics, discontinuities, non-uniqueness, and infinite-dimensional nature. Traditional model-based approaches typically require precise knowledge of the system model, low dimensionality, and favorable theoretical conditions to guarantee convergence, which are often difficult to ensure for complex systems. On the other hand, commonly used machine learning methods [2] require a large number of measurements, which often results in overfitting [3].

This work is partially supported by the Wallenberg AI, Autonomous Systems and Software Program (WASP) funded by the Knut and Alice Wallenberg Foundation and Digital Futures.

K. Eshkofti and M. Barreau are with the Division of Decision and Control Systems, Digital Futures, KTH Royal Institute of Technology, SE-100 44 Stockholm, Sweden {eshkofti,barreau}@kth.se

These issues encourage investigating learning-based approaches that handle model uncertainties and efficiently utilize data. To address this, the authors of [4] introduced physics-informed neural networks (PINNs), integrating governing equations directly within neural networks. By embedding physical models into the loss function and penalizing deviations, PINNs effectively learn solutions from sparse and noisy data. Specifically, [5] demonstrated that PINNs simultaneously identify unknown model parameters, reconstruct traffic flow states from sparse vehicle data, and extend predictions. This reveals the potential of PINN-based approaches for state reconstruction in hyperbolic PDEs and serves as an incentive for the present research.

Since the original PINN development, recent modifications have improved performance in complex scenarios. For example, [6] proposed a multi-fidelity stacking approach, iteratively training a PINN to refine outputs progressively. Physics-informed residual adaptive networks employ projected input coordinates within residual blocks featuring adaptive skip connections to address deep multilayer perceptron derivative initialization issues [7]. Integrating localized artificial viscosity into PINNs enables automatic learning of optimal viscosity, enhancing accuracy over non-adaptive methods [8]. Additionally, sequential and hierarchical PINN structures, such as multi-stage neural networks, have shown unique capabilities [9].

Although recent studies suggest PINNs outperform traditional deep learning methods [10], they have limitations, particularly for hyperbolic PDEs, where they struggle to capture sharp features like shocks or discontinuities [3]. Addressing these challenges motivates the development of more effective state estimation methods for hyperbolic PDEs. Moreover, no evidence demonstrates that PINN effectively learns the hyperbolic PDE underlying traffic state models with acceptable accuracy [3], making this an open and intriguing research area in traffic control.

Our contribution is to address this issue by incorporating prior knowledge in the form of a function series through an effective combination of the vanishing viscosity method from applied mathematics, curriculum learning from machine learning, and stacked PINNs. This approach ensures convergence to the unique entropic hyperbolic solution.

This paper consists of five sections. Section 2 reviews hyperbolic PDE formulations and the role of vanishing viscosity in ensuring stable, unique solutions. Section 3 introduces the vanishing stacked-residual PINN methodology, outlining its architecture and training with decreasing viscosity. Section 4 presents numerical experiments on traffic state reconstruction, highlighting shock-capturing capabilities and comparing performance with the original PINN. Section 5 concludes with key findings and future research directions.

**Notation:** Let $\mathbb{R}$ denote real numbers and $\mathbb{R}_+$ nonnegative real numbers. For differentiable single-variable functions, the prime notation $f'$ represents derivatives. Multivariate functions’ partial derivatives with respect to space and time are denoted by $\partial f$ with corresponding subscripts. Moreover, $C^1(\mathbb{R}_+ \times \mathbb{R})$ denotes continuously differentiable functions on the given domain. The sets $L^p(\Lambda)$, $H^k(\Lambda)$, and $L^\infty(\Lambda)$ represent Lebesgue, Sobolev, and essentially bounded function spaces on $\Lambda$, respectively.

arXiv:2503.14222v5 [eess.SY] 8 Sep 2025

## II. BACKGROUND ON PROBLEM STATEMENT

The main goal of this paper is to find a solution $u$ to the following 1d quasi-linear hyperbolic PDE posed on the spatiotemporal domain $\Lambda = [0, T] \times [0, L] \subset \mathbb{R}_+ \times \mathbb{R}$:

$$
\begin{cases}
\partial_t u + \partial_x f(u) = 0, & (t, x) \in \Lambda, \\
u(0, x) = u^0(x), & x \in [0, L], \\
u(t, 0) = u_b^-(t), \quad u(t, L) = u_b^+(t), & t \in [0, T].
\end{cases}
\tag{1}
$$

Here, $u^0$ is a function of bounded variation that represents the initial data [11, Definition 1.7.1]. Suitable boundary conditions $u_b^\pm$ should be considered for the PDE in (1) to be well-posed [1]. It is assumed that $f$ is a smooth flux function, at least $f \in C^2(\mathbb{R})$, so that the PDE is strictly hyperbolic. Moreover, to ensure that the mapping $u \mapsto f(u)$ remains bounded, it is assumed that $f$ is globally Lipschitz or has at most polynomial growth.

Since hyperbolic solutions can develop discontinuities in finite time, we can only investigate weak solutions, which belong to a distribution space [1]. However, these weak solutions are usually not unique unless an entropy condition is imposed. To this end, one can consider the Lax-E entropy condition, which adds a point-wise constraint in the form of $f'(u(t, x^-)) \leq f'(u(t, x^+))$ for $t, x \in \Lambda$. A weak solution that satisfies the entropy inequality is then called entropy-admissible. As stated in [11, Theorem 14.10.2], there is a unique entropic solution to (1).

Testing the Lax-E inequality at each point is numerically intractable. A more robust and practical way to construct weak entropy solutions is through the vanishing viscosity method. Consider the parabolic regularization of (1) as

$$
\partial_t u_\gamma + \partial_x f(u_\gamma) = \gamma \partial_{xx} u_\gamma, \quad \gamma > 0.
\tag{2}
$$

where $\gamma$ is a small viscosity coefficient. It is worth noting that $u_\gamma$ signifies the solution corresponding to viscosity $\gamma$. Under the standard assumptions previously mentioned, the parabolic PDE in (2) results in a unique classical solution $u_\gamma$ for each fixed $\gamma$ [12, Theorem 14.6]. By finding estimates that are uniform with respect to $\gamma$, it is proved that the sequence $\{u_\gamma\}$ remains bounded in appropriate norms [13]. Uniform energy estimates and the derivation of an entropy inequality enable passing to the limit as $\gamma \to 0$, thereby, as discussed in Chapter 2 of [13], obtaining a weak solution that is entropy-admissible and satisfies the additional regularity conditions outlined as
$u \in C^0([0, T]; H^2([0, L])) \cap C^1([0, T]; H^1([0, L]))$.

The rigorous justification of this limit passage and the well-posedness of the corresponding problem is established via a combination of compactness arguments and the construction of a basic quadratic Lyapunov function, as detailed in [1]. Moreover, the dissipativity of the boundary conditions is crucial to ensuring that the energy associated with the system decays over time. Consequently, by combining the vanishing viscosity method [14] with uniform energy and entropy estimates, the existence, uniqueness, and entropy admissibility of the solution to (1) are guaranteed.

Although vanilla PINNs have been successfully applied to various types of problems, particularly those classified as parabolic PDEs, a major limitation is their poor performance in terms of convergence and accuracy when solving hyperbolic PDEs [3]. Therefore, a modification to the PINN structure is necessary to enhance its ability to solve hyperbolic PDEs, leading to the following problem.

**Problem:** We want to efficiently and accurately approximate the entropic solution $u$ of a hyperbolic PDE specified in (1) using PINNs.

To achieve this objective, we introduce a novel variant of PINN called vanishing stacked-residual PINN, which incrementally refines a baseline approximation through stacked residual-correction subnetworks with vanishing viscosity. This approach incorporates both the PDE residual and data to enforce the governing equations while also guiding the solution in regions where the PDE may be insufficient or highly nonlinear.

In the following section, we demonstrate how adopting this smooth-to-sharp transition in the stacked residual PINN enhances the capture of discontinuities, enabling high-resolution reconstruction of hyperbolic PDE states.

## III. METHODOLOGY

This section first presents an overview of the proposed architecture, followed by a detailed discussion of its application to hyperbolic PDEs.

### A. Classical PINN

In the standard formulation of PINNs, the goal is to approximate the solution $u$ of PDE (1) using a dense feedforward neural network $\hat{u}(\cdot; \theta)$. Let the neural network have $L$ hidden layers, formulated as follows:

$$
\hat{u}(t, x; \theta) = W_L \times H_{L-1} \circ \cdots \circ H_1(t, x) + b_L
\overset{\mathrm{def}}{=} \mathcal{N}([t, x]; \theta),
\tag{3}
$$

for $(t, x) \in \Lambda$ where $(t, x)$ represents the input coordinates in the spatiotemporal domain. For each hidden layer $l = 1, \ldots, L-1$, the feature map is defined as $H_l(\nu) = \phi.(W_l \nu + b_l)$. The weights and biases at layer $l$ are represented by $W_l \in \mathbb{R}^{n_l \times n_{l-1}}$ and $b_l \in \mathbb{R}^{n_l}$. The entire set of network parameters is denoted $\theta = \{W_l, b_l\}_{l=1}^L$ and the element-wise activation function is $\phi \in C^\infty(\mathbb{R}, \mathbb{R})$.

**Figure 1:** Vanilla PINN structure. Black lines are forward pass, and red-dotted lines are backpropagation.

We are interested in approximating the unique entropic solution $u$ to (1), meaning that we want to solve the following constrained optimization problem:

$$
\theta^* = \mathrm{Argmin}_\theta \int_\Gamma \|u(\nu) - \hat{u}(\nu)\|^2 d\nu
$$

subject to

$$
\int_\Lambda |r_0(\cdot; \hat{u}(\cdot; \theta))|^2 = 0,
$$

where $\Gamma = \Gamma_{init} \cup \Gamma_{boundary}$ is the measured boundary of System (1) with

$$
\Gamma_{init} = \{(0, x) \mid x \in [0, L]\},
$$

$$
\Gamma_{boundary} = \{(t, 0) \mid t \in [0, T]\} \cup \{(t, L) \mid t \in [0, T]\},
$$

and $\hat{u}$ refers to $\hat{u}(\cdot, \theta)$ to ease the reading. The residual $r$ is also defined as:

$$
r_\gamma(\cdot; \hat{u}) = \partial_t \hat{u} + \partial_x f(\hat{u}) - \gamma \partial_{xx} \hat{u}.
\tag{4}
$$

The previous problem cannot be numerically solved because it contains integrals. Following the methodology in [15] using Monte-Carlo sampling and the Lagrangian formulation, we get the following relaxed but numerically tractable optimization problem:

$$
\theta^* = \mathrm{Argmin}_\theta \max_{\lambda > 0} \mathcal{L}_\lambda(\hat{u}, 0),
$$

where $\mathcal{L}_\lambda(\hat{u}, \gamma) = \mathcal{L}_{data}(\hat{u}(\cdot, \theta)) + \lambda \mathcal{L}_{phy}(\hat{u}(\cdot, \theta), \gamma)$.

$$
\mathcal{L}_{data}(\hat{u}) =
\frac{1}{|D_{data}|}
\sum_{(t,x)\in D_{data}}
|u(t, x) - \hat{u}(t, x)|^2,
$$

$$
\mathcal{L}_{phy}(\hat{u}, \gamma) =
\frac{1}{|D_{phy}|}
\sum_{(t,x)\in D_{phy}}
|r_\gamma(t, x; \hat{u})|^2,
$$

with $D_{phy} \subset \Lambda$ a discrete set of cardinal $|D_{phy}|$ and $D_{data} \subset \Gamma$ a discrete set of cardinal $|D_{data}|$. This problem is typically solved using a primal-dual strategy, alternating between gradient descent on the min problem over the tensor of parameters $\theta$ and the max over the Lagrange multiplier $\lambda$. A simpler and often efficient method is to fix $\lambda$ to a small constant and apply gradient descent only to the min problem. For simplicity, we consider this option in this paper.

The total loss function consists then of two terms: the data mismatch $\mathcal{L}_{data}$ and the PDE residual $\mathcal{L}_{phy}$. These losses are computed using the mean square error between the true and the approximated solution, transforming the optimization problem into a learning one. For the physics loss, we want to minimize the PDE residual $r_\gamma(\cdot; \theta)$ over $\Lambda$, bringing regularization and forcing the convergence to the solution of the PDE. The general structure of PINN is illustrated in Fig. 1.

As explained in [15], [16], the PINN methodology only succeeds in the case of a Lipschitz continuous PDE operator, which is never the case in hyperbolic problems such as (1). The following section provides a detailed discussion of a refined architecture that proposes a solution.

### B. Residual PINN

First, consider solving the regularized PDE in (2). If $\gamma$ is small enough, then the approximated solution will be close to the entropic solution of (1), based on the vanishing viscosity method [14]. To this end, the initial stage consists of a baseline PINN designed to approximate the solution $u_{\gamma_{init}}$ to the parabolic PDE (2) by $\hat{u}^{(0)}(\cdot; \theta_0)$. At this stage, the viscosity coefficient $\gamma_{init}$ is chosen to be large enough to ensure that $\hat{u}$ is entropic and that the PDE operator is sufficiently Lipschitz to guarantee that the PINN can successfully learn the approximated solution.

One key idea of this article is to combine the vanishing methodology with the residual-network architecture [17]. Subsequently, we introduce a residual stage where $\hat{u}^{(0)}$ is refined by a single residual correction network to get $\hat{u}^{(1)}$, as shown in Fig. 2. This residual-correction PINN bears a close resemblance to a Luenberger observer that feedbacks the difference $u - \hat{u}$ to update its estimate. In both cases, the discrepancy triggers the correction. At this second stage, the viscosity coefficient is $\gamma_1 = 0$, hence the solution to the hyperbolic PDE in (1) is approximated by $\hat{u}^{(1)}$. Consequently, the approximation at the second stage is:

$$
\hat{u}^{(1)}(t, x; \theta_1) =
\hat{u}^{(0)}(t, x; \theta_0) +
|\alpha_1| \mathcal{N}\left([t, x, \hat{u}^{(0)}(t, x)]; \theta_1\right).
\tag{5}
$$

In practice, the residual block is a feedforward neural network whose inputs include the spatiotemporal coordinates $(t, x)$ and the approximation at the previous step $\hat{u}^{(0)}(t, x)$. The scaling factor $|\alpha_1|$ is a learnable variable that determines and controls the extent to which each residual block contributes to the update. The coefficient $\alpha_1$ is introduced because we want to keep the correction small, such that we only correct slightly the parabolic solution, ensuring that the hyperbolic solution remains entropic. Indeed, a large $\alpha_1$ will probably signify that $\hat{u}^{(1)}$ is quite different from $\hat{u}^{(0)}$ which does not align with the vanishing viscosity method. The new optimization problem is

$$
\theta_0^*, \theta_1^* = \mathrm{Argmin}_{\theta_0,\theta_1,\alpha_1}
\mathcal{L}(\theta_0, \theta_1) + \alpha_1^2,
$$

where

$$
\mathcal{L}(\theta_0, \theta_1) =
\frac{1}{2}\left(
\mathcal{L}_\lambda(\hat{u}^{(0)}, \gamma_{init}) +
\mathcal{L}_\lambda(\hat{u}^{(1)}, 0)
\right).
$$

As discussed in Section 2, the vanishing viscosity principle ensures that the solution to the parabolic PDE in (2), with a small viscosity term, converges to the entropic weak solution to the corresponding hyperbolic PDE as the viscosity coefficient decreases to zero.

As a result, training a PINN on the parabolic form in the initial stage, which admits a unique smooth solution, and then transitioning to the hyperbolic PDE allows for acquiring both the stability of the parabolic regime and the fidelity of the hyperbolic limit.

**Figure 2:** Residual PINN structure. Black lines are forward pass, and red-dotted lines are backpropagation.

### C. Stacked residual PINN and vanishing viscosity approach

While a single residual correction block may succeed in simple problems, it can fail when dealing with sharp and localized solution features. Moreover, relying on a single residual PINN to approximate both smooth regions and shocks imposes a burden on the learning process.

The other key idea of this article is to adapt the iterative stacking method put forward by [6]. In our study, by stacking multiple residual blocks, each trained with a successively smaller $\gamma$, a multi-stage correction process is implemented following the vanishing viscosity method. In fact, each stage leverages the well-posedness of the parabolic PDE in (2) to compute a smooth and stable correction, which is then gradually refined to capture the sharper features of the hyperbolic PDEs. In other words, $\hat{u}^{(0)}$ is incrementally refined by stacking $n$ residual-correction subnetworks. The approximation at the $i$th stage is given by:

$$
\hat{u}^{(i)}(t, x; \theta_i) =
\hat{u}^{(i-1)}(t, x; \theta_{i-1}) +
|\alpha_i| \mathcal{N}\left([t, x, \hat{u}^{(i-1)}(t, x)]; \theta_i\right),
\tag{6}
$$

where $i \in \{1, \ldots, n\}$, and $|\alpha_i|$ is an adaptive parameter that scales the contribution of each residual block. As in the viscous Burgers equation, the Cole–Hopf transformation [18], [19] demonstrates that solutions depend exponentially on the viscosity parameter. As $\gamma$ decreases, the transformed solution exhibits rapid exponential changes. Therefore, integrating a superlinear $\gamma$, as

$$
\gamma_i = \gamma_{init} \left[1 - \left(\frac{i}{n}\right)^p\right]
\tag{7}
$$

with $p > 1$ so that $\gamma_0 = \gamma_{init} > 0$ and $\gamma_n = 0$, ensures that the stacked residual blocks smoothly capture the transition from parabolic to hyperbolic behavior without compromising stability.

As in stage 1, a physics-informed loss is imposed at each level $i$, ensuring that $r_{\gamma_i}(\cdot; \theta_i)$ remains small along with the usual boundary and initial conditions.

In other words, at stacked residual block $i$, the PDE residual is governed by $r_{\gamma_i}$ such that the first block gets the viscous coefficient $\gamma_{init}$ and the last stage $\gamma_n = 0$. The optimization problem can be formulated as:

$$
\{\theta_i^*, \alpha_i^*\}_{i=0}^n
=
\mathrm{Argmin}_{\{\theta_i,\alpha_i\}_{i=0}^n}
\mathcal{L}(\{\theta_i\}_{i=0}^n) + \sum_{i=1}^n \alpha_i^2
$$

where

$$
\mathcal{L}(\{\theta_i\}_{i=0}^n) =
\frac{1}{n+1}\sum_{i=0}^n \mathcal{L}_\lambda(\hat{u}^{(i)}, \gamma_i).
$$

Here $\mathcal{L}$ represents the total loss function, which consists of the base PINN and the stacked residual PINNs. The residual PINN block diagram is presented in Fig. 3.

**Figure 3:** Vanishing stacked-residual PINN. Black lines are forward pass, and red-dotted lines are backpropagation.

**Remark 1:** The stacked PINN method was initially introduced in [6], where they employed a multi-fidelity strategy that stacks PINNs. In this approach, each network’s output provides a lower-fidelity input for the next stage, incrementally refining the model’s expressivity. We share the same idea; however, our method employs a residual PINN at each stage. Contrary to [6], we use a different residual $r_\gamma$ at each stage to align with the vanishing viscosity method. ♦

With this approach, we obtain certain convergence guarantees, as stated in the following proposition.

**Proposition 1:** Consider the hyperbolic PDE in (1). Let $\gamma_{init} > 0$ and consider a sequence of viscosity coefficients defined as in (7), ensuring $\gamma_n = 0$. Assume the following:

1. For each $\gamma_i > 0$, the parabolic PDE in (2) admits a unique smooth solution $u_{\gamma_i}$, converging strongly in $L^1(\Lambda)$ to the entropy solution of $u$ in (1) as $\gamma_i \to 0$.
2. At each stage $i$, the neural network $\hat{u}^{(i)}(\cdot, \theta_i)$ has sufficient expressivity such that the approximation error is bounded by $\varepsilon_i$, that is:
   $$
   \|\hat{u}^{(i)} - u_{\gamma_i}\|_{L^2(\Lambda)} \leq \varepsilon_i,
   \quad \text{where } \varepsilon_i \to 0 \text{ as } i \to n.
   $$

Then, the stacked residual PINN solution $\hat{u}^{(n)}$ converges to the entropy solution of (1).

**Proof:** According to the vanishing viscosity theorem [14], for the sequence $\{\gamma_i\}$ with $\gamma_i \to 0$ as $i \to n$, we have
$$
\lim_{i \to n} \|u_{\gamma_i} - u\|_{L^1(\Lambda)} = 0.
$$

Considering the second assumption [20], the residual correction mechanism ensures that the discrepancy between $\hat{u}^{(i)}$ and the viscous solution $u_{\gamma_i}$ is minimized through the physics loss $\mathcal{L}_{phy}(\gamma_i, \hat{u}^{(i)})$. The total error at stage $i$ decomposes as:

$$
\|\hat{u}^{(i)} - u\|_{L^1(\Lambda)}
\leq
\sqrt{|\Lambda|}\|\hat{u}^{(i)} - u_{\gamma_i}\|_{L^2(\Lambda)}
+
\|u_{\gamma_i} - u\|_{L^1(\Lambda)}
$$

that is,

$$
\|\hat{u}^{(i)} - u\|_{L^1(\Lambda)}
\leq
\sqrt{|\Lambda|}\,\varepsilon_i + \delta_i,
$$

where $\delta_i = \|u_{\gamma_i} - u\|_{L^1(\Lambda)}$.

By the first assumption, $\delta_i \to 0$ as $\gamma_i \to 0$. By the second assumption, with a sufficiently large network, $\varepsilon_i \to 0$. For the sequence $\{\hat{u}^{(i)}\}$, we have

$$
\|\hat{u}^{(n)} - u\|_{L^1(\Lambda)}
\leq
\sqrt{|\Lambda|}\sum_{i=0}^n \varepsilon_i + \sum_{i=0}^n \delta_i.
$$

Since both series converge under assumptions 1 and 2, the proof is complete.

## IV. RESULTS

In this section, our goal is to estimate vehicle density over a road $[0, L]$ from local density measurements by employing the proposed vanishing stacked-residual PINN [^1].

In the example considered, the PDE (1) represents the LWR model [21], [22]. The normalized density $u$ is defined such that $u = 0$ corresponds to an empty road, while $u = 1$ represents bumper-to-bumper traffic conditions. Two density measurements are provided at the boundaries $x \in \{0, L\}$ and can be collected using loop detectors.

Additionally, $f(u) = V_f u(1 - u)$ is referred to as the Greenshields flow equation [23], which describes the relationship between vehicle velocity and density. The parameter $V_f$ denotes the free-flow velocity. The Greenshields function serves as the advection term, and its nonlinear dependence on $u$ can lead to shock formation or discontinuities.

By employing the vanishing viscosity limit, the governing equation in (2) is considered, and a small initial viscosity coefficient $\gamma_{init} = 0.1$. To investigate the impact of stacked layers on the improvement of results, the algorithm is implemented while considering four different numbers of stacked residual blocks, $n = \{0, 1, 3, 5\}$, where $n = 0$ represents vanilla PINN. To compute the data loss $\mathcal{L}_{data}$ in the total loss function of PINN, density measurements are supplied via Godunov simulation of (1).

The baseline PINN at the initial stage consists of three hidden layers, each with 30 neurons. Each residual correction block comprises three hidden layers, each with 40 neurons. Vanishing viscosity is implemented via the function defined in (7), where $p = 2$.

It is worth noting that, to ensure a fair comparison across all scenarios, the same number of hidden layers and neurons is utilized. Additionally, a 15,000-iteration schedule is set for all scenarios, combined with an early stopping criterion using a patience parameter, so that training would automatically terminate once the loss plateaus. Under these conditions, the modified stacked PINN converged and stopped at iteration 11,000, while the other variants continued running through all 15,000 iterations.

[^1]: The code and data are available at https://github.com/KatayounEshkofti/VanishingStackedResidualPINN

### Table I

**Relative $L^2$ error for various numbers of stacked residual blocks.**

| # Stacked residual blocks | 0 | 1 | 3 | 5 |
|---|---:|---:|---:|---:|
| Relative $L^2$ error ($\times 10^{-2}$) | 18.98 | 13.86 | 4.86 | 4.66 |

The results are compared with solutions obtained from the Godunov simulation, and the relative $L^2$ error is defined as the evaluation metric:

$$
\text{relative } L^2 = \frac{\|u - \hat{u}\|_2^2}{\|u\|_2^2}.
\tag{8}
$$

The relative $L^2$ error quantifies the percentage discrepancy between the estimated density and exact values. As shown in Table I, increasing stacked residual blocks from 0 to 5 consistently reduces the error from about 19% to 4%. This suggests that additional residual blocks enhance estimation accuracy, though the smaller gain from 3 to 5 blocks may indicate diminishing returns.

Moreover, we plot the distribution of point-wise errors across the entire spatio-temporal test domain in Fig. 4 to compare the performance of our method with the vanilla PINN [4], PINN with adaptive localized artificial viscosity [8], and the original stacked PINN [6]. Note that the modified stacked PINN [6] integrates vanishing viscosity into stacked networks. The baseline stacked PINN, the modified stacked PINN, and the vanishing stacked-residual PINN each consist of three stacked networks, with three hidden layers and 40 neurons per network. For fairness, the vanilla PINN and PINN with adaptive artificial viscosity consist of nine hidden layers, each with 40 neurons. As shown in Fig. 4, although multiple shocks are present, the proposed vanishing stacked-residual PINN achieves a lower median error over test data.

The accuracy of the proposed method can be seen from Fig. 5, where both the speed and shape of the propagating shocks are correctly caught. More specifically, Fig. 6 shows that the first residual block $\alpha_1 \mathcal{N}(\cdot, \theta_1)$ is far from being zero, indicating that it is grasping more shocks and sharpening the existing ones from the previous block.

These results indicate that progressively stacking networks enhances reconstruction accuracy, while residual correction networks further stabilize learning, leading to lower errors and reduced variability in state estimations.

### Figure 4

**Official caption:** Distribution of errors over the test data for five methods applied to the traffic reconstruction problem.

**Description:**  
Figure 4 is a boxplot comparing test-error distributions for five methods:

- Vanilla
- Adaptive Viscosity
- Baseline Stacked
- Modified Stacked
- Vanishing Stacked-Residual

The vertical axis is labeled **Test error** and uses a logarithmic scale ranging approximately from $10^{-8}$ to $10^{0}$. The vanishing stacked-residual method shows the lowest median among the displayed methods and a relatively compact spread, indicating improved accuracy and reduced variability. The vanilla and baseline stacked methods exhibit higher medians and broader upper whiskers. The adaptive viscosity and modified stacked methods improve over vanilla, but remain visually worse than the proposed vanishing stacked-residual approach.

### Figure 5

**Official caption:** Numerical examples on the state reconstruction.

**Description:**  
Figure 5 contains two subplots over the same spatiotemporal domain:

- Horizontal axis: **Time (h)**, ranging approximately from 0 to 2.0
- Vertical axis: **Position (km)**, ranging approximately from 0 to 5

**(a) $u$**  
A 2D color map of the reference density field. The colorbar is labeled **Density** and ranges approximately from 0.3 to 1.0. The plot displays several propagating bands and sharp transition fronts, corresponding to traffic waves and shocks moving through the road segment.

**(b) $\hat{u}^{(3)} - u$**  
A 2D color map of the reconstruction error for the three-stage approximation. The colorbar ranges approximately from $-0.4$ to $0.4$. Most of the domain appears close to zero error (light/neutral tones), with narrow red and blue streaks concentrated near propagating discontinuities and wave fronts. This indicates generally accurate reconstruction, with the largest errors localized around sharp shocks.

### Figure 6

**Official caption:** Value of the residual block $\alpha_1 \mathcal{N}(\cdot; \theta_1)$.

**Description:**  
Figure 6 is a 2D color map over:

- Horizontal axis: **Time (h)**, approximately 0 to 2.0
- Vertical axis: **Position (km)**, approximately 0 to 5

The colorbar is labeled **Residual Correction** and ranges roughly from $-0.2$ to $0.2$. The map shows structured red and blue bands aligned with major traffic-wave regions. This indicates that the first residual block contributes nontrivial corrections across the domain, especially near shock-like patterns, rather than collapsing to zero. The strongest corrections appear along elongated diagonal or horizontal regions corresponding to dynamically significant wave fronts.

## V. CONCLUSION AND FUTURE WORKS

This paper introduced the vanishing stacked-residual PINN, a variation of the PINN framework designed to reconstruct states of hyperbolic PDEs. By adopting the vanishing viscosity principle, the approach progressively enhances solution approximation, effectively capturing discontinuities and shocks. Applied to a traffic state reconstruction problem, the method demonstrated an order of magnitude improvement in accuracy over the vanilla PINN.

Future work will focus on extending the methodology to higher-dimensional and more complex hyperbolic PDEs, aiming to confirm its broader applicability, particularly in control engineering.

## REFERENCES

[1] G. Bastin and J.-M. Coron, *Stability and Boundary Stabilization of 1-D Hyperbolic Systems*. Birkhauser Cham, 2016. [неразборчиво]

[2] N. G. Polson and V. O. Sokolov, “Deep learning for short-term traffic flow prediction,” *Transportation Research Part C: Emerging Technologies*, 2017.

[3] A. J. Huang and S. Agarwal, “On the limitations of physics-informed deep learning: Illustrations using first-order hyperbolic conservation law-based traffic flow models,” *IEEE Open Journal of Intelligent Transportation Systems*, 2023.

[4] M. Raissi, P. Perdikaris, and G. E. Karniadakis, “Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations,” *Journal of Computational Physics*, 2019.

[5] M. Barreau, M. Aguiar, J. Liu, and K. H. Johansson, “Physics-informed learning for identification and state reconstruction of traffic density,” in *60th IEEE Conference on Decision and Control*, 2021.

[6] A. A. Howard, S. H. Murphy, and al., “Stacked networks improve physics-informed training: Applications to neural networks and deep operator networks,” *Foundations of Data Science*, 2025.

[7] S. Wang, B. Li, Y. Chen, and P. Perdikaris, “Piratenets: Physics-informed deep learning with residual adaptive networks,” *Journal of Machine Learning Research*, 2025.

[8] E. J. R. Coutinho, M. Dall’Aqua, L. McClenny, M. Zhong, U. Braga-Neto, and E. Gildin, “Physics-informed neural networks with adaptive localized artificial viscosity,” *Journal of Computational Physics*, 2023.

[9] Y. Wang and C.-Y. Lai, “Multi-stage neural networks: Function approximator of machine precision,” *Journal of Computational Physics*, 2024.

[10] A. J. Huang and S. Agarwal, “Physics informed deep learning for traffic state estimation,” in *2020 IEEE 23rd International Conference on Intelligent Transportation Systems (ITSC)*, 2020.

[11] C. M. Dafermos, *Hyperbolic Conservation Laws in Continuum Physics; 3rd ed.*, ser. *Grundlehren der mathematischen Wissenschaften*. Dordrecht: Springer, 2010.

[12] H. Amann, “Nonhomogeneous linear and quasilinear elliptic and parabolic boundary value problems,” in *Function spaces, differential operators and nonlinear analysis*. Springer, 1993.

[13] C. M. Dafermos, *Hyperbolic Conservation Laws in Continuum Physics*. Springer Berlin, Heidelberg, 2016.

[14] S. N. Kruzkov, “First order quasilinear equations in several independent variables,” *Mathematics of the USSR-Sbornik*, 1970. [неразборчиво]

[15] M. Barreau and H. Shen, “Accuracy and robustness of weight-balancing methods for training PINNs,” *Arxiv*, 2025.

[16] J. Sirignano and K. Spiliopoulos, “DGM: A deep learning algorithm for solving partial differential equations,” *Journal of computational physics*, 2018.

[17] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in *Proceedings of the IEEE conference on computer vision and pattern recognition*, 2016.

[18] J. D. Cole, “On a quasi-linear parabolic equation occurring in aerodynamics,” *Quarterly of applied mathematics*, 1951.

[19] E. Hopf, “The partial differential equation $u_t + u u_x = \mu u_{xx}$,” *Communications on Pure and Applied mathematics*, 1950.

[20] K. Hornik, “Approximation capabilities of multilayer feedforward networks,” *Neural networks*, 1991.

[21] P. I. Richards, “Shock waves on the highway,” *Operations Research*, 1956.

[22] M. J. Lighthill and G. B. Whitham, “On kinematic waves II. a theory of traffic flow on long crowded roads,” *Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences*, 1955.

[23] B. D. Greenshields, J. R. Bibbins, W. S. Channing, and H. H. Miller, “A study of traffic capacity,” in *Highway research board proceedings*, 1935.
```

### Примечания по качеству распознавания
- Общая точность: высокая.
- Есть отдельные артефакты OCR в символах диакритики и типографике ссылок:
  - `Birkhauser` / `Birkhäuser` [неразборчиво в источнике OCR]
  - `Kruzkov` / `Kruzhkov` [неразборчиво]
  - в [6] указано `and al.` — вероятно OCR-артефакт вместо `et al.`, но оставлено без исправления по вашему правилу не интерпретировать.
- Формулы и обозначения приведены в LaTeX с максимально точным сохранением структуры.
- Рисунки 1–3 не были подробно описаны, так как это схемы архитектуры, а их подписи и роль в тексте однозначны; при необходимости я могу дополнительно воссоздать их в Mermaid.
- Если хотите, я могу на следующем шаге:
  1. **очистить OCR-артефакты и нормализовать Markdown**,  
  2. **сделать “публикационную” версию Markdown**,  
  3. **добавить Mermaid-схемы для Fig. 1–3**.