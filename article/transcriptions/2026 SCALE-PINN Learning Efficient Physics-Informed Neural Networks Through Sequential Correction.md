```markdown
# Scale-PINN: Learning Efficient Physics-Informed Neural Networks Through Sequential Correction

Pao-Hsiung Chiu1†, Jian Cheng Wong1*†, Chin Chun Ooi1,2, Chang Wei3, Yuchen Fan3, Yew-Soon Ong2,4

1 Institute of High Performance Computing, A*STAR, Singapore.  
2 Centre for Frontier AI Research, A*STAR, Singapore.  
3 School of Mechanical Engineering, Tianjin University, China.  
4 College of Computing and Data Science, Nanyang Technological University, Singapore.

*Corresponding author(s). E-mail(s): wongj@a-star.edu.sg;  
Contributing authors: chiuph@a-star.edu.sg; ooicc@a-star.edu.sg;  
wei chang@tju.edu.cn; fanyuchen@tju.edu.cn; asysong@ntu.edu.sg;  
†These authors contributed equally to this work.

## Abstract

Physics-informed neural networks (PINNs) have emerged as a promising mesh-free paradigm for solving partial differential equations, yet adoption in science and engineering is limited by slow training and modest accuracy relative to modern numerical solvers. We introduce the Sequential Correction Algorithm for Learning Efficient PINN (Scale-PINN), a learning strategy that bridges modern physics-informed learning with numerical algorithms. Scale-PINN incorporates the iterative residual-correction principle, a cornerstone of numerical solvers, directly into the loss formulation, marking a paradigm shift in how PINN losses can be conceived and constructed. This integration enables Scale-PINN to achieve unprecedented convergence speed across PDE problems from different physics domain, including reducing training time on a challenging fluid-dynamics problem for state-of-the-art PINN from hours to sub-2 minutes while maintaining superior accuracy, and enabling application to representative problems in aerodynamics and urban science. By uniting the rigor of numerical methods with the flexibility of deep learning, Scale-PINN marks a significant leap toward the practical adoption of PINNs in science and engineering through scalable, physics-informed learning. Codes are available at https://github.com/chiuph/SCALE-PINN.

**Keywords:** Physics-informed neural networks, sequential correction algorithm, loss function, PINN benchmark, fluid-dynamics

## 1 Introduction

Physics-Informed Neural Networks (PINNs) have emerged as a promising paradigm for solving partial differential equations (PDEs) by embedding governing physics into the training loss. Their mesh-free nature, ability to integrate physics with sparse data, and suitability for inverse problems have sparked widespread interest across computational science, from fluid and solid mechanics to electromagnetism, optics, earth sciences, materials science, electrochemistry, and epidemiology, underscoring their growing prominence as an alternative to numerical simulation methods [1–7].

However, a key limitation of PINNs thus far, even when employing improved neural architectures and state-of-the-art learning strategies [8–12], is their high computational cost-accuracy trade-off. First, the use of dense training samples and large batch sizes improves accuracy but significantly increase computational demands. Second, adaptive sampling and neural tangent kernel-based adaptive loss weighting methods introduce considerable overhead to overcome spectral bias and complex loss landscape issues. Third, the need for curriculum and sequence-to-sequence training to gradually refine the solution from an initial guess to prevent premature convergence is very costly in more complex problems, such as stiff and multi-scale PDEs. Fourth, some studies have turned to second-order optimization methods, including BFGS algorithm and Quasi-Newton variants, to improve accuracy through more precise updates. All of them substantially increase the computational costs as a trade-off for achieving quality outcome. As a result, PINN training is much slower than numerical solvers, limiting their broader adoption in real-world scientific and engineering problems [13]. Curiously, these strategies derive primarily from the general machine learning literature and do not leverage insights from scientific computing.

In seeking to overcome this limitation, we recognize that the scientific computing community has developed a wealth of knowledge and algorithmic techniques over the past decades for efficiently solving complex PDEs—many of which can be potentially adopted to advance PINN methodologies. For example, realizing that lack of neighborhood dependencies information may lead to training failure, numerical differentiation techniques, including the finite difference, finite volume and finite element discretizations, have been employed to successfully enhance physics-informed learning by enforcing local spatial coupling [14–19]. Furthermore, combining automatic differentiation and numerical discretization for PINNs has proven effective in improving both accuracy and computational efficiency [20, 21]. The artificial eddy viscosity and pseudo-time stepping methods are other notable examples for improving training stability [22–24]. These early successes highlight a promising direction of integrating algorithmic insights from scientific computing into PINN for designing practical and scalable physics-informed learning frameworks.

While these developments demonstrate the power of infusing discretization wisdom into the PINN framework, they have largely drawn from only one of the two pillars of numerical simulation: discretization and iterative method. Modern numerical methods not only discretize governing equations but also solve the resulting linear systems through carefully designed iterative schemes that guarantee convergence, stability, and precision. Building on this foundation, we demonstrate that the second pillar—iterative schemes—can be a rich source of algorithmic insight for efficient physics-informed learning. In this work, we establish that iterative residual correction, which is a principle at the core of many numerical solvers, can be explicitly realized within the PINN loss formulation with remarkable gains in PINN learning.

Our proposed Sequential Correction Algorithm for Learning Efficient PINN (Scale-PINN) embodies this idea: by embedding a sequential correction mechanism within the training process through an auxiliary loss function, Scale-PINN achieves both speed and sample efficiency. This perspective marks a paradigm shift in how PINN losses are conceived and constructed, by drawing on the foundations of iterative methods that have long powered scientific computing. The inherently iterative nature of these updates aligns seamlessly with the current state-of-the-art mini-batch stochastic gradient descent (SGD) optimizers. On representative stiff-conditioned lid-driven cavity benchmarks, Scale-PINN reaches a target accuracy of relative error $\le 2e^{-2}$ in sub-2 minutes, compared with 15 hours for prior state-of-the-art training strategies [12], and attains improved accuracy. A schematic diagram of Scale-PINN is illustrated in Fig. 1. Our proposed framework is generic and easy to implement with broad applicability to domains such as aerodynamics and urban science, and it opens new possibilities for tackling practical problems in computational science with PINNs.

## 2 Results

### 2.1 Sequential correction algorithm for learning efficient PINN models

We introduce Scale-PINN as a neural PDE solver for scientific simulations, emphasizing its capability to predict physical outcomes in fully specified systems governed by PDEs and the prescribed initial conditions (IC) and boundary conditions (BC). By reformulating the simulation as a physics-informed learning task, we seek to optimize the network weights $w$ such that the output function $f$ satisfies the requisite PDE constraints.

The objective (loss) function for PINN weight parameters optimization can be expressed as $L(w) = L_{pde} + \lambda_{ic} L_{ic} + \lambda_{bc} L_{bc}$ which comprises contributions from the PDE, ICs, and BCs (see Method 4.1). Among the three loss components, the governing PDE loss,

$$
L_{pde} = \|N_\vartheta[f(\cdot; w)] - h(\cdot)\|^2_{L^2(\Omega \times (0,T])}
\tag{1}
$$

greatly affect the PINN training difficulty. Highly nonlinear PDEs, such as the Navier-Stokes (N-S) equations, often exhibit steep gradients and strong interactions among variables. This makes it difficult for PINNs to satisfy all governing equations simultaneously. Moreover, small training perturbations can substantially change the PDE dynamics across the domain, hindering convergence to the correct solution. These factors, in addition to the high dimensionality and non-linear characteristics of neural networks, contribute to a rugged PDE loss landscape, resulting in multiple local minima, oscillatory optimization paths, and hence a higher likelihood of becoming trapped in suboptimal solutions [25].

PINN training is commonly performed using iterative optimization methods, such as SGD and Adam algorithms. They progressively evolve the weight parameters from an initial guess $w^0$, over many iterations along the descent direction of the loss function

$$
w^{k+1} = w^k - \eta \nabla L(w^k)
\tag{2}
$$

where the current iteration number $k$ is denoted in superscript, and $\eta$ is a problem-dependent learning rate. This approach, often implemented via mini-batch training, exploits a varying set of sample points for loss (and gradient) evaluation at each iteration. In the context of PINNs, training with incomplete and continuously changing system information introduces an additional layer of instability, amplifying optimization oscillations and making stable convergence in a complex loss landscape more difficult.

Mathematically derived from the iterative scheme (see Method 4.2 for details), we propose Scale-PINN by introducing a sequential correction term (auxiliary sequence) $F$ at iteration $k > 0$, which modifies the PDE loss term $L_{pde}$ to improve convergence:

$$
L^{k}_{sc-pde} = \left\|N_\vartheta[f(\cdot; w^k)] - h(\cdot) + \frac{1}{\tau_{sc}}F \right\|^2_{L^2(\Omega \times (0,T])}
\tag{3a}
$$

$$
F = B\big(f(\cdot; w^k) - f(\cdot; w^{k-1})\big)
\tag{3b}
$$

$\tau_{sc}$ is the hyperparameter. The matrix $B$ constitutes a key design element of the iterative framework, as it determines the operator used in the update. $B$ can be flexibly selected to reflect problem-dependent structure or to promote specific solution properties. The standard PINN loss function is obtained as the limiting case $B = 0$.

In present study, we instantiate $B \equiv P_\alpha = (I - \alpha^2 \nabla^2)$ as the residual smoothing operator applied to the change in solution $f(\cdot; w^k)-f(\cdot; w^{k-1})$ during iterative optimization. We show equivalence to the implicit residual smoothing method (see Method 4.3 for details), with associated enhanced stability and reduced oscillation during training. $L_{sc-pde}$ from equation (3) can then be recast as:

$$
L^{k}_{sc-pde}
=
\left\|N_\vartheta[f(\cdot; w^k)] - h(\cdot) + \frac{1}{\tau_{sc}}F - \frac{\gamma}{\tau_\alpha}\nabla^2F \right\|^2_{L^2(\Omega \times (0,T])}
=
\|N_\vartheta[f(\cdot; w^k)] - h(\cdot) + (M_f - M_v)\|^2_{L^2(\Omega \times (0,T])}
\tag{4a}
$$

$$
M_f = \frac{1}{\tau_{sc}}f(\cdot; w^k) - \frac{\gamma}{\tau_\alpha}\nabla^2 f(\cdot; w^k)
\tag{4b}
$$

$$
M_v = \frac{1}{\tau_{sc}}f(\cdot; w^{k-1}) - \frac{\gamma}{\tau_\alpha}\nabla^2 f(\cdot; w^{k-1})
\tag{4c}
$$

with tunable hyperparameters $\tau_{sc} > 0$, $\gamma > 0$, and $\tau_\alpha > 0$ ($\alpha^2 = \tau_{sc}\frac{\gamma}{\tau_\alpha}$).

Different from standard PDE loss, two additional auxiliary terms, i.e., stabilization term $M_f$ (residual smoothing operator) and consistency term $M_v$ (counter term compensates for the inclusion of $M_f$), are introduced to enhance the PINN training behavior as well as ensure the final solution will converge to original system. Equation (4) is straightforward to implement, as the auxiliary terms in $M_f$ are already computed for the standard PDE loss. The new required operations are storing of the network weights from the previous iteration, $w^{k-1}$, performing a forward pass to compute $f(\cdot; w^{k-1})$, and conducting two backward passes to evaluate $\nabla^2 f(\cdot; w^{k-1})$ on the latest iteration mini-batch samples, all of which incur negligible additional computational overhead during training. Algorithm 1 (Method 4.3) summarizes the overall computational procedure of the Scale-PINN, which integrates seamlessly with widely used iterative optimization methods such as SGD and Adam.

**Figure 1.** *Scale-PINN schematic and result highlights.*  
Figure shows:  
- A schematic of Scale-PINN with input variables, neural network, PDE loss, IC/BC loss, sine-based activation with frequency annealing, and sequential correction term using $P_\alpha = (I-\alpha^2\nabla^2)$.  
- Example governing equations for Navier–Stokes, Grey-Scott, Allen-Cahn, Kuramoto–Sivashinsky, and Korteweg–De Vries systems.  
- A convergence plot comparing Scale-PINN against numerical solvers on lid-driven cavity flow at $Re=3200$.  
- Representative prediction/reference/error panels for multiple PDEs.  
Official caption: Scale-PINN includes a sequential correction term through application of the residual smoothing operator $P_\alpha = (I - \alpha^2\nabla^2)$ to the change in solution $F := f(\cdot; w^k) - f(\cdot; w^{k-1})$ during iterative optimization. A convergence plot on the Navier-Stokes (N-S) example, lid-driven cavity flow at $Re = 3200$, shows competitive time-to-accuracy versus numerical solvers. Compared to other PINN methods, Scale-PINN solves the lid-driven cavity flow to state-of-the-art accuracy with unprecedented speed, i.e., $\sim 90$s for $Re = 3200$ and $\sim 150$s for $Re = 7500$. Results for Kuramoto–Sivashinsky (K-S), Grey–Scott (G-S), Korteweg–De Vries (KdV), and Allen–Cahn (AC) equations demonstrate accuracy across diverse dynamics. Scale-PINN model architecture and training strategies are detailed in Method 4.5.

### 2.2 Efficient scientific simulation with Scale-PINN

We demonstrate Scale-PINN on a classical benchmark problem in computational fluid dynamics (CFD), the lid-driven cavity flow (Method 4.4.1). The fluid flow inside a 2D unit square, $x \in [0, 1]$, $y \in [0, 1]$, is driven by the top lid velocity ($u_{lid} = 1$), and governed by the steady-state incompressible N-S equations for velocity $\vec{u} = [u, v]^\top$ and pressure $p$:

$$
\nabla \cdot \vec{u} = 0
\tag{5a}
$$

$$
(\vec{u} \cdot \nabla)\vec{u} = \frac{1}{Re}\nabla^2 \vec{u} - \nabla p
\tag{5b}
$$

Complex physical phenomenon can be observed when the Reynolds number ($Re$) increases, such as $Re \ge 3200$, making it notoriously difficult for PINN methods to solve (e.g., require hours to tens of hours of training) even with the help of some labeled data or transfer and curriculum learning [10, 11]. In contrast, Scale-PINN is fast and effective at tackling this very challenging PINN benchmark problem (see results highlighted in Fig. 1-Fig. 3).

Building on equation (4) as per the Scale-PINN methodology, the loss function for momentum equations (5b) can be defined as below:

$$
L^{k}_{sc-pde}(M_u) =
\left\|
u^k \frac{\partial u^k}{\partial x}
+
v^k \frac{\partial u^k}{\partial y}
-
\frac{1}{Re}
\left(
\frac{\partial^2 u^k}{\partial x^2}
+
\frac{\partial^2 u^k}{\partial y^2}
\right)
+
\frac{\partial p^k}{\partial x}
+
SM_u
\right\|^2_{L^2(\Omega)}
\tag{6a}
$$

$$
L^{k}_{sc-pde}(M_v) =
\left\|
u^k \frac{\partial v^k}{\partial x}
+
v^k \frac{\partial v^k}{\partial y}
-
\frac{1}{Re}
\left(
\frac{\partial^2 v^k}{\partial x^2}
+
\frac{\partial^2 v^k}{\partial y^2}
\right)
+
\frac{\partial p^k}{\partial y}
+
SM_v
\right\|^2_{L^2(\Omega)}
\tag{6b}
$$

$$
SM_u
=
\frac{1}{\tau_{sc}}(u^k-u^{k-1})
-
\frac{\gamma_{uv}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2 u^k}{\partial x^2}
+
\frac{\partial^2 u^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2 u^{k-1}}{\partial x^2}
+
\frac{\partial^2 u^{k-1}}{\partial y^2}
\right)
\right]
\tag{6c}
$$

$$
SM_v
=
\frac{1}{\tau_{sc}}(v^k-v^{k-1})
-
\frac{\gamma_{uv}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2 v^k}{\partial x^2}
+
\frac{\partial^2 v^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2 v^{k-1}}{\partial x^2}
+
\frac{\partial^2 v^{k-1}}{\partial y^2}
\right)
\right]
\tag{6d}
$$

with the integration of sequential correction terms $SM_u$ and $SM_v$ as defined by the choice of the Helmholtz residual smoothing operator ($P_\alpha = (I - \alpha^2\nabla^2)$). In this study we set $\gamma_{uv} = \frac{1}{Re}$ based on prior knowledge of the governing physical system. Values of $\tau_{sc}$ and $\tau_\alpha$ are fine-tuned empirically.

A fundamental difficulty in solving incompressible N-S equations is that the pressure variable does not appear explicitly in the continuity equation and only appears through its gradient in the momentum equations [27, 28]. Thus, several numerical schemes proposed to modify the continuity formulation to relax the incompressibility constraint by explicitly establishing a dynamic relationship between pressure and continuity [28–30]. Guided by the same principle, the Scale-PINN loss function for the continuity equation (5a) is defined as follows:

$$
L^{k}_{sc-pde}(C_n)
=
\left\|
\frac{\partial u^k}{\partial x}
+
\frac{\partial v^k}{\partial y}
+
SC_n
\right\|^2_{L^2(\Omega)}
\tag{7a}
$$

$$
SC_n = \frac{1}{\tau_{sc}}(p^k-p^{k-1})
\tag{7b}
$$

Scale-PINN allows $SC_n$ to be introduced into the continuity loss term to explicitly provide a relation between pressure and the continuity equation, thereby improving convergence. Together with a BC loss term $L_{bc}$ to enforce the top lid velocity $u_{lid} = 1$, $v_{lid} = 0$ and no-slip wall condition $u = v = 0$, the Scale-PINN objective function for simulating the lid-driven cavity flow is thus defined as:
$L_{sc}(w^k) = L^{k}_{sc-pde}(M_u) + L^{k}_{sc-pde}(M_v) + L^{k}_{sc-pde}(C_n) + \lambda_{bc}L^{k}_{bc}$.

Our experimental analysis (Fig. 2) suggests that the principal barrier for vanilla PINNs is not merely insufficient compute but an unstable optimization landscape. At $Re = 400$, with a small batch size and large learning rate, the convergence is slow (over 500k iterations, training time $\sim 780$s) and susceptible to premature locking into suboptimal flow patterns. Increasing the batch ten-fold (400→4,000) and reducing the learning rate ten-fold ($1e^{-3}\to1e^{-4}$) stabilizes convergence, but it also leads to significantly increased training time ($\sim 1800$s). In contrast, Scale-PINN attains much lower error (MSE $< 1e^{-5}$) in only 50k iterations (training time $\sim 90$s) using the smaller batch and larger learning rate. Visual snapshot across training iterations show that Scale-PINN resolves the primary vortex and corner eddies earlier, and its mid-section $u$- and $v$-profiles match the classical Ghia et al. [26] cut-lines, indicating physically faithful pressure-velocity coupling. At $Re = 3200$, Scale-PINN continues to converge without increasing batch size or iteration budget, whereas vanilla PINN becomes trapped in incorrect local minima. These contrast supports our interpretation that the sequential correction in Scale-PINN effectively smooths the PDE residuals, enabling steady progress with standard first-order optimizers.

The cross-regime results summarized in Fig. 3(a) underscore that Scale-PINN not only attains state-of-the-art accuracy but also establishes a new benchmark in efficiency across an unprecedented range of Reynolds numbers. Scale-PINN remains both accurate and fast from $Re = 400$ to $Re = 20k$, with relative error rising only modestly ($1.4e^{-2}\to4.4e^{-2}$) as the problem complexity increases (learning stiffness intensifies), while training time stays under seven minutes ($\sim 380$s) even at $Re = 20k$. Scale-PINN demonstrates favorable scaling of optimization cost with problem complexity, despite deliberately increased resolution ($100^2\to256^2$), batch size (400→2400), and number of iterations (50k→100k) to resolve thinner boundary layers and stronger shear at higher Reynolds number. For all simulated cases, their mid-section $u$ and $v$-velocity profiles show excellent agreement with canonical benchmarks (Ghia et al. [26] up to $Re = 10k$ and Erturk [31] at $Re = 20k$), thereby demonstrating, for the first time, that a PINN approach can deliver accurate and efficient N-S solutions at the high-Reynolds regime. The results highlight Scale-PINN as a scalable method across regimes, with predictions consistent with established numerical standards.

We benchmark Scale-PINN against recent PINN methods at $Re = 3200$, which features in several state-of-the-art PINN literature as a challenging regime, where many PINNs fail to converge. We include methods whose original paper reports successfully solving the problem with relative error below $1e^{-1}$: Wong et al. (2023, LSA-PINN) [32], Wang et al. (2024, PirateNets) [11], Khademi & Dufour (2025, TSA-PINN) [33], and Wei et al. (2025, FFV-PINN) [34]. LSA-PINN and PirateNets are reproduced in-house on a single RTX 3090 (Scale-PINN trained on the same hardware) using available source code. We also include $Re = 5000$ results from Wang et al. (2025, SOAP) [12], a second-order optimizer and successor to PirateNets, and Tsai et al. (2025, MLD-PINN) [35], because they disclose timing; this offers a useful speed-accuracy reference despite the higher Reynolds number. As shown in Fig. 3(b), Scale-PINN’s sub-2 minutes training regime represents a new state-of-the-art speed-accuracy Pareto frontier for $Re = 3200$. Scale-PINN is trained from scratch, i.e., He initialization [36], without pre-training, curriculum schedules, or data supervision. Contemporary PINN variants are often aided by curriculum strategies (e.g., $Re$: 100→400→1000→...→3200) [11, 12], numerical differentiation loss [32, 34, 35], or additional data supervision [33], and many of them still require hours of training to approach comparable prediction accuracy.

Fig. 3(c) illustrates the convergence behavior of Scale-PINN relative to other methods as the problem complexity increases ($Re$: 400→3200). Scale-PINN maintains excellent convergence speed and accuracy across regimes. In contrast, LSA-PINN training increases from less than 10 minutes to more than 1 hour, accompanied by a significant degradation in accuracy, while PirateNets requires up to 12-15 hours to achieve comparable accuracy. This contrast highlights the superior scalability of Scale-PINN: as the problem becomes more challenging, its convergence speed degrades far more slowly than competing methods, enabling the solution of increasingly complex fluid dynamics problems within feasible computational budgets.

The impressive improvements in Scale-PINN training regime motivate, for the first time in a PINN study, direct comparisons with high-fidelity CFD solvers. We compare Scale-PINN against an in-house CFD solver [37], which has been demonstrated to produce high-fidelity solutions for the incompressible N-S equations, and the widely-used commercial solver Ansys Fluent, recognized for its reliability, generality, and parallel performance.

We first run the in-house solver on a $96 \times 96$ mesh and record the runtime and accuracy along the convergence trajectory. Given a runtime of around 80s, Scale-PINN achieves higher converged accuracy (Fig. 1), establishing a new speed-accuracy Pareto frontier. We then utilize similar simulation settings in Fluent on a finer $128\times128$ mesh. Its converged accuracy is much poorer than both the in-house code (on $96\times96$ mesh) and Scale-PINN. Finally, we perform the simulations on a much finer $192 \times 192$ mesh using four CPU cores for both Fluent and the in-house code. With the optimized parallelization, results from Fluent now match our method’s accuracy in around 120s runtime. The in-house solver, with a basic OpenMP implementation, took nearly twice as long to achieve the same accuracy, although it should be acknowledged that it can eventually reach the highest accuracy with additional runtime.

These comparisons suggest that mesh-free PINN methods may be well suited for practical scientific and engineering problems under fixed computational budgets. In scientific computing, practitioners often choose the coarsest mesh that delivers physics-resolved accuracy, balancing fidelity against cost; achieving higher accuracy typically requires finer meshes and substantially more compute. Leveraging theoretically exact automatic differentiation for derivative evaluation, Fig. 1 shows that Scale-PINN can outperform a conventional second-order numerical scheme as employed by Fluent on a relatively coarse mesh (e.g., $128 \times 128$). In practical terms, under a limited time budget, Fluent on a $128 \times 128$ mesh yields the best accuracy within $\sim 30$s runtime; Scale-PINN provides the best accuracy within $\sim 120$s; and if runtime is unconstrained, the in-house solver on a fine mesh achieves the highest accuracy.

**Figure 2.** *Experimental analysis on lid-driven cavity flow.*  
Official caption:  
(a) Experimental analysis on lid-driven cavity flow at $Re = 400$ shows that the convergence of a vanilla PINN can be improved by increasing batch size (400→4,000) and reducing learning rate ($1e^{-3}\to1e^{-4}$), albeit at a slower pace ($\sim 1800$s). Scale-PINN requires substantially less training iterations to reach orders of magnitude higher accuracy ($\sim 90$s), while using 1 order of magnitude smaller batch size and higher learning rate. Comparing their intermediate flow fields progressing from a few iterations to 50k-500k iterations, and mid-section profiles against the Ghia et al. [26] benchmark, Scale-PINN attains accurate flow structures far earlier.  
(b) Scale-PINN can converge to an accurate solution even when the Reynolds number is increased to $Re = 3200$, without the need to increase batch size and number of training iterations. A vanilla PINN struggles to solve the $Re = 3200$ case, as it becomes trapped in incorrect flow patterns, indicating premature convergence.

**Figure 3.** *Scale-PINN performance across regimes and comparison with other PINN methods for lid-driven cavity flow.*  
Panel (a) includes a summary table:

| Re | MSE | Relative error | Training time (s) | No. iterations | Initial learning rate | Batch size / iter. | No. training sample | Network size (no. parameters) |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| 400 | 8.98e-6 | 1.43e-2 | less than 90 | 50,000 | 1e-3 | 400 | 100x100 | 15,424 |
| 3200 | 1.48e-5 | 1.73e-2 | 90 | 50,000 | 5e-4 | 400 | 100x100 | 15,424 |
| 7500 | 4.29e-5 | 2.97e-2 | 150 | 50,000 | 5e-4 | 1,000 | 150x150 | 59,520 |
| 10k | 3.43e-5 | 2.74e-2 | 360 | 80,000 | 5e-4 | 2,000 | 256x256 | 59,520 |
| 20k | 9.39e-5 | 4.43e-2 | 380 | 100,000 | 5e-4 | 2,400 | 256x256 | 59,520 |

Official caption:  
(a) Scale-PINN solves the lid-driven cavity flow from $Re = 400$ to $Re = 20k$ with state-of-the-art accuracy and efficient training, as shown in the summary table of error, training time, and other parameters, alongside the representative velocity fields and absolute error maps ($Re = 400$ and $Re = 20k$) to confirm that residuals remain small and largely confined to shear layers and vortex cores. For all simulated cases, their MSE consistently below $1e^{-4}$, and their mid-section $u$ and $v$-velocity profiles (colored lines) show excellent agreement with the classic benchmark results (marked points) for numerical solvers, i.e., Ghia [26] for up to $Re = 10k$ and Erturk [31] for $Re = 20k$.  
(b) Scale-PINN establishes a sub-2 minutes training regime on lid-driven cavity flow ($Re = 3200$), whereas recent PINN variants require hours to approach comparable accuracy.  
(c) Scale-PINN scales favorably with problem complexity ($Re$: 400→3200), enabling the solution of more complex problems within a feasible time scale.

### 2.3 Navier–Stokes flow simulation for engineering and urban science

To demonstrate the applicability beyond lid-driven cavity benchmarks, we present Scale-PINN results on two representative aerodynamic problems: (1) flow past a single NACA0012 airfoil at $Re = 1000$ and $7^\circ$ angle of attack (AoA); and (2) flow past two-staggered NACA0012 airfoils at $Re = 500$ and $7^\circ$ AoA (Method 4.4.1). NACA airfoil problems are classical benchmarks, where fast and reliable flow simulations are crucial for advancing the design and optimization of aerodynamic structures such as aircraft and wind turbines.

For the single-airfoil case, Scale-PINN predictions produce the expected wake patterns (Fig. 4a) and show excellent agreement between component-wise velocity $(u, v)$ and pressure $(p)$ fields and CFD reference solutions. Even for the more complex scenario of two-staggered airfoils, Scale-PINN successfully captures the altered wake structures and aerodynamic interactions between the bodies, with predicted velocity and pressure fields aligning well with CFD (Fig. 4b). For both cases, absolute error maps indicate that minor and localized discrepancies are mainly confined within the leading edge and near-wake regions. The pressure coefficient ($C_p$) distribution along the airfoil surfaces compare well with both CFD and literature data from Kurtulus [38], even capturing the suction peak at the leading edge and subsequent pressure recovery.

Scale-PINN requires only $\sim 180$s of training to produce solutions in excellent agreement with CFD ground truth. In contrast, Xiao et al. [39] report a training time of $\sim 7800$s and the need for additional sensor points to achieve comparable accuracy for airfoil flows, highlighting the superior efficiency and accuracy of Scale-PINN. Scale-PINN demonstrates robust performance across both single-body configurations and multi-body aerodynamic interactions, underscoring its potential for aerodynamic design and optimization with multi-element airfoils.

We next simulate flow past three staggered square cylinders at $Re = 25$, a canonical proxy for wind flow around buildings (Method 4.4.1). Scale-PINN accurately recovers wake structures and recirculation zones, with velocity and pressure fields closely matching CFD references and errors confined to shear layers and separation points (Fig. 5a). These results confirm Scale-PINN’s robustness for bluff-body aerodynamics in open domains, where reliable prediction of flow interactions are commonly used to inform urban ventilation design and pollutant dispersion.

We further validate Scale-PINN on buoyancy-driven Rayleigh–Bénard convection at $Ra = 100k$ to demonstrate its versatility in modeling multiphysics transient dynamics, where thermal instabilities give rise to convection rolls and their transient evolution into complex patterns (Method 4.4.1). Scale-PINN predictions remain in close agreement with CFD benchmarks across multiple time snapshots between 1s and 50s, with low residuals sustained over time (Fig. 5b). By capturing the onset and development of natural convection, Scale-PINN demonstrates its capacity to model thermally-driven flows of direct importance to energy efficiency, ventilation, and thermal comfort in the built environment and urban sustainability studies.

Our results further confirm the superior sampling points (or mesh fidelity) to accuracy trade-off enabled by Scale-PINN (relative to CFD). With temporal step size of 0.001, CFD solution achieves an MSE of $4.0e^{-5}$ and $3.32e^{-5}$ for temperature and velocity magnitude, respectively, on a fine spatial mesh ($384 \times 96$). It only achieves an MSE of $1.3e^{-4}$ and $1.1e^{-4}$ with a coarse mesh ($256 \times 64$). Scale-PINN with $258 \times 66 \times 501$ spatio-temporal sample points, which is on par with CFD coarse mesh, can produce temperature and velocity MSEs of $4.5e^{-5}$ and $3.1e^{-5}$, respectively. This further highlights the potential for PINNs to have a unique place within the Pareto set of models for use when one might need to trade-off accuracy and computational cost (time) for scientific simulations.

**Figure 4.** *Scale-PINN predictions for airfoil flow problems.*  
Official caption: Scale-PINN predictions, with streamlines overlaid on velocity magnitude contours, for flow past (a) a single-airfoil at $Re = 1000$ and (b) staggered airfoils at $Re = 500$ are compared to reference solutions obtained from CFD. Component-wise fields $(u, v, p)$ and absolute error maps indicate good agreement between Scale-PINN and CFD across the domain, including wakes behind airfoil. Surface pressure-coefficient ($C_p$) traces along the airfoil(s) closely match CFD and literature curves. Only the near-field region is shown for clarity, where the flow patterns around the airfoil(s) emerge; the actual computational domain extends well beyond the visualized region. Scale-PINN reaches accurate solutions within $\sim 180$s of training, achieving near-field velocity relative errors of $1.7e^{-2}$ ($3.47e^{-3}$ full domain) for the single-airfoil case and $1.96e^{-2}$ ($4.79e^{-3}$ full domain) for the staggered airfoils case. These results validate the accuracy and efficiency of Scale-PINN in resolving canonical aerodynamic flow features at moderate Reynolds number.

**Figure 5.** *Scale-PINN simulations for urban-flow proxy and Rayleigh–Bénard convection.*  
Official caption:  
(a) Scale-PINN simulates the flow past square cylinders in open domain, where the predicted fields $(u, v, p)$ accurately capture the wake structure and recirculation zones, with consistently low absolute errors against the reference solution obtained from CFD. Contours are shown in the near field for clarity; the actual computational domain extends further. Scale-PINN reaches accurate solutions within $\sim 285$s of training, achieving near-field velocity relative errors of $9.21e^{-3}$ ($4.86e^{-3}$ full domain).  
(b) Scale-PINN simulates Rayleigh–Bénard convection at $Ra = 100k$. The temperature contours, overlaid with velocity streamlines, show close agreement between predicted roll patterns and reference solutions obtained from CFD, across multiple time snapshots (1-50s). Scale-PINN achieves accurate solutions within $\sim 390$s of training, with relative errors $1.99e^{-2}$ for velocity and $3.2e^{-2}$ for temperature. These cases validate the method’s robustness across bluff-body geometries in open domain and thermally driven, time-dependent convection.

### 2.4 Performance on benchmark problems

We demonstrate the effectiveness of Scale-PINN across several benchmark PDE problems: Kuramoto-Sivashinsky, Grey-Scott, Korteweg-de Vries, Allen-Cahn, and N-S equations at $Re = 3200, 7500$. Detailed descriptions of the problems are given in Method 4.4. These PDEs span a wide range of physical phenomena and application domains: N-S underpins fluid dynamics; Kuramoto–Sivashinsky models instabilities in physical systems such as chemical reaction dynamics and thin-film flows; Grey-Scott captures reaction-diffusion pattern formation in chemistry and biology; Korteweg-de Vries describes shallow-water and plasma solitary waves; and Allen-Cahn governs phase separation and interface motion in materials science. To isolate the contribution of our sequential corrected loss from conventional PDE loss in PINN training, we perform a simple ablation: we keep the model architecture (moderate-sized multilayer perceptron) and training settings identical and change only the PDE loss term, i.e., sequential corrected (Scale-PINN) vs. standard PDE loss (baseline). Each problem is run for five optimization trails from distinct model initializations using He method [36], evaluating robustness to initialization. Their error-time convergence and representative initial and final solutions are illustrated in Fig. 6, showing rapid convergence of Scale-PINN. A concise summary of accuracy and runtime is also provided.

Scale-PINN substantially accelerates learning to achieve accurate solutions within 10 minutes, whereas the baseline fails to simulate the correct patterns for N-S, Kuramoto-Sivashinsky, and Grey-Scott equations. The ablation validates that the sequential corrected PDE loss is the driver of the gains. Notably, our prediction accuracy on the benchmark PDE problems approaches that reported by Wang et al. (2025, SOAP) [12] which uses second-order optimizer for PINN and requires hours to tens of hours of training.

**Figure 6.** *Scale-PINN performance on benchmark PDE problems.*  
Summary table reproduced from figure:

| Problem | Training time | Relative error (5 runs), best | Relative error (5 runs), average |
|---|---:|---:|---:|
| Navier-Stokes equations ($Re=3200$) | 88s | 1.73e-2 | 3.79e-2 |
| Navier-Stokes equations ($Re=7500$) | 147s | 2.97e-2 | 4.93e-2 |
| Kuramoto-Sivashinsky equation | 537s | 2.56e-2 | 3.91e-2 |
| Grey-Scott equations | 679s | 8.42e-4 | 1.39e-3 |
| Korteweg-De Vries equation | 560s | 2.82e-4 | 6.79e-4 |
| Allen-Cahn equation | 535s | 5.30e-5 | 7.54e-5 |

Official caption: Scale-PINN attains state-of-the-art, minute-scale training efficiency on a range of PDE benchmarks, converging within $\sim 10$ minutes while achieving accuracy on par with second-order optimization method (typically requires hours of training). For each PDE benchmark problem, relative error (log scale) versus training time is shown for five independent initializations; the final (best) Scale-PINN solution, final baseline PINN solution, and their corresponding initial (random initialization) solution are shown alongside error-time curves. We keep the model architecture (moderate-sized multilayer perceptron) and training settings identical and change only the PDE residual term, i.e., sequential corrected (Scale-PINN) vs. standard PDE loss (baseline). The accompanying table reports training times and best/average errors over the five runs, demonstrating robustness to initialization and broad applicability across PDE families.

## 3 Discussion

Scale-PINN reframes how physics-informed loss functions are conceived and constructed: moving beyond PDE and discretization towards embedding the principle of iterative methods directly into the loss formulation. By introducing a sequential residual-correction mechanism, Scale-PINN converges rapidly and stably without sacrificing accuracy, establishing it as a state-of-the-art neural PDE solver. More broadly, this reformulation encourages the computational science community to regard the loss function not merely as an error metric, but as a mechanism for encoding the mathematics of convergence.

The framework is designed for immediate adoption and re-engineering. In this work, the residual-smoothing operator is chosen and shown to be advantageous across diverse physical systems, and can be readily adapted to different architectures and optimizers. Nonetheless, the sequential-correction principle naturally extends to incorporation of algorithmic insights from other iterative methods in scientific computing (described in Methods 4.2 & 4.3). Beyond its algorithmic contribution, our work offers a conceptual bridge between scientific computing and modern AI. We anticipate that this sequential correction learning paradigm will stimulate a new generation of physics-informed learning frameworks that fuse scientific computing and machine learning more coherently, advancing PINNs toward the reliability, scalability, and rigor long achieved by traditional numerical methods.

## 4 Methods

### 4.1 PINN models for scientific simulations

PINNs are a class of universal function approximators capable of learning a mapping $f$ between the input variables $(x, t)$ and output solution $u$ while satisfying specified differential equation constraints that represent the physical phenomenon or dynamical process of interest. Consider differential equations of the general form:

$$
\text{PDE: } N_\vartheta[u(x,t)] = h(x,t), \quad x \in \Omega,\ t \in (0,T]
\tag{8a}
$$

$$
\text{IC: } u(x,t=0) = u_0(x), \quad x \in \Omega
\tag{8b}
$$

$$
\text{BC: } B[u(x,t)] = g(x,t), \quad x \in \partial\Omega,\ t \in (0,T]
\tag{8c}
$$

where the general differential operator $N_\vartheta[u(x,t)]$ can be parameterized by $\vartheta$ and can include linear and/or nonlinear combinations of temporal and spatial derivatives of $u$, with an arbitrary source term $h(x,t)$, in the computational domain $x \in \Omega$, $t \in (0,T]$. The equation (8b) specifies the initial condition (IC), $u_0(x)$, at time $t = 0$. The equation (8c) specifies the boundary condition (BC) at the domain boundary $\partial\Omega$ that $B[u(x,t)]$ equates to $g(x,t)$, where $B[\cdot]$ can either be an identity (Dirichlet BC), a differential (Neumann BC), or a mixed identity-differential (Robin BC) operator.

Fundamentally, a PINN model can arrive at an accurate and physics-compliant prediction by forcing its output $f(\cdot; w)$ function to satisfy equation (8) through training, i.e., optimizing its network weight parameters $w$. The objective (loss) function of PINN weight parameters optimization can be written as:

$$
L(w) = L_{pde} + \lambda_{ic}L_{ic} + \lambda_{bc}L_{bc}
\tag{9a}
$$

$$
L_{pde} = \|N_\vartheta[f(\cdot; w)] - h(\cdot)\|^2_{L^2(\Omega \times (0,T])}
\tag{9b}
$$

$$
L_{ic} = \|f(\cdot, t=0; w) - u_0(\cdot)\|^2_{L^2(\Omega)}
\tag{9c}
$$

$$
L_{bc} = \|B[f(\cdot; w)] - g(\cdot)\|^2_{L^2(\partial\Omega \times (0,T])}
\tag{9d}
$$

and these are to be evaluated on a set of completely label-free training points (collocation points) sampled from the respective spatio-temporal domain during PINN training. The PINN loss usually consists of multiple components for PDEs, ICs, and BCs, where the incorporation of relative weights $\lambda_{ic} \ge 0$ and $\lambda_{bc} \ge 0$ is essential to control the trade-off between these components.

PINN models usually have a rugged loss landscape, resulting in multiple local minima, oscillatory optimization paths, and a higher likelihood of becoming trapped in suboptimal solutions during training. Consequently, large batch sizes and small learning rates are often needed to stabilize PINN training, but they significantly increase computation time and remain vulnerable to premature convergence. Many studies also adopt curriculum learning, where the model training starts with the PDE settings of an easier problem and gradually transitions to the target problem. However, this approach requires manually setting up intermediate problems and training configurations, demands a good understanding of the system’s behavior under changing PDE settings, and involves long training times through solving multiple intermediate problems.

### 4.2 Integration of iterative solver principle into physics-informed learning

To solve equation (8), nearly all conventional numerical simulation approaches begin by converting the continuous governing PDEs into a finite-dimensional linear system,

$$
Au = h
\tag{10}
$$

where $A$ is the coefficient matrix determined by the chosen discretization scheme, $u$ is the solution vector and $h$ is the source term vector. To efficiently solve the above linear system, iterative numerical algorithms have been continually developed and refined over decades, and this is one of the cornerstones of the field of scientific computing [40]. The fundamental idea is that, rather than solving the linear system directly, residual-based error corrections are introduced to incrementally improve the solution in sequence. This leads to a generic formulation:

$$
u^{k+1} = u^k + B^{-1}r^k
\tag{11a}
$$

$$
r^k = h - Au^k
\tag{11b}
$$

where $B$ is the key matrix designed to mitigate the computational cost of matrix inversion, thereby improving the robustness and efficiency of the iterative algorithm and enabling memory- and time-efficient computations [41, 42].

A classical example is the modified Richardson iteration:

$$
u^{k+1} = u^k + \xi r^k
\tag{12}
$$

where $\xi > 0$ is the relaxation factor ensuring convergence of the solution [40]. Another example is the Jacobi iterative method:

$$
u^{k+1} = u^k + D^{-1}r^k
\tag{13a}
$$

$$
A = D + L + U
\tag{13b}
$$

In the above, $D$ is the diagonal matrix, and $L$ and $U$ denote the lower and upper triangular parts of $A$. Similarly, the Gauss–Seidel iterative method can be written as:

$$
u^{k+1} = u^k + (D+L)^{-1}r^k
\tag{14}
$$

We mathematically demonstrate that this iterative residual-correction principle can be effectively integrated into physics-informed learning and explicitly realized within the PINN loss formulation. We begin by reformulating the generic iterative residual-correction in equation (11), into the following loss function form:

$$
L^{k}_{sc-ND} = B(u^{k+1}-u^k) + (Au^k-h)
\tag{15}
$$

for any intermediate iteration step $k > 0$. However, in practice, it is infeasible to directly employ the above expression, as $u^{k+1}$ is unknown and must be estimated from the known $u^k$. To bridge this gap, we adopt a second-order extrapolation based on the Taylor-series expansion:

$$
u^{k+1} = 2u^k - u^{k-1}
\tag{16}
$$

which yields the following reformulated loss:

$$
L^{k}_{sc-ND} = B(u^k-u^{k-1}) + (Au^k-h)
\tag{17}
$$

In the context of PINN training, the change in the solution $u^k-u^{k-1}$ can be approximated by the PINN model predictions $f(\cdot; w^k)-f(\cdot; w^{k-1})$, while the PDE residuals, $Au^k-h$ are represented by $N_\vartheta[f(\cdot; w)] - h(\cdot)$ during iterative optimization. Without constraining to any specific discretization scheme, the generic iterative residual-correction PINN loss can therefore be expressed as:

$$
L^{k}_{sc-pde}
=
\left\|
N_\vartheta[f(\cdot; w^k)] - h(\cdot) + B(f(\cdot; w^k)-f(\cdot; w^{k-1}))
\right\|^2_{L^2(\Omega \times (0,T])}
\tag{18}
$$

This formulation allows the loss to be computed flexibly via automatic differentiation at arbitrary sample locations. We refer to the term $B(f(\cdot; w^k)-f(\cdot; w^{k-1}))$ as a sequential correction term (or auxiliary sequence), which augments the conventional PDE loss. This leads to what we call the sequential correction loss, a paradigm shift in how PINN losses are formulated that draws on the foundations of iterative methods that have long powered scientific computing. The design of the matrix $B$ plays a key role in this iterative framework. Notably, the conventional PINN loss function is recovered as a special case when $B = 0$.

### 4.3 Sequential correction algorithm for learning efficient PINN models

This section presents a specific formulation of the sequential correction loss using a special residual-smoothing operator $P_\alpha$ derived from the implicit residual smoothing method and realized through modified Richardson iteration, which is parametrized by $\alpha$ and offers several desirable theoretical properties.

For numerical approaches, it is essential to employ high-order, high-resolution numerical schemes together with a mesh of sufficient resolution to accurately capture complex physical features. However, high-order schemes and fine meshes impose severe restrictions on the time-step size, i.e., often requiring it to be very small, when the problem is solved using an explicit scheme [43]. This is analogous to PINN training, where stable convergence often depends on small learning rates, large batch sizes, and curriculum learning. These stability constraints make convergence slow and computationally expensive in both cases.

The implicit residual-smoothing method, rooted in the traditions of scientific computing, modifies the residuals using smoothing operators before each update step [44, 45]. It has been shown theoretically that this technique alleviates stability-related limitations in numerical simulations [46] and can significantly accelerate convergence by permitting larger time steps.

Scale-PINN aims to improve convergence behavior by instantiating the sequential correction term through a residual-smoothing operator $P_\alpha\big(f(\cdot; w^k)-f(\cdot; w^{k-1})\big)$, thereby achieving more efficient PINN training. The proposed sequential correction algorithm can then be seamlessly integrated with mainstream iterative optimization methods for PINN training, i.e., Section 2 equation (2) (see schematic in Fig. 1).

The derivation of the sequential correction term begins by reformulating the PDE constraint in equation (8a) as an iterative update based on modified Richardson iteration (i.e., $B=I$) under an intermediate iteration step $k$:

$$
f(\cdot; w^k) - f(\cdot; w^{k-1}) = \tau_{sc}R
\tag{19}
$$

where $R = h(\cdot)-N_\vartheta[f(\cdot; w^k)]$ is the residual and $\tau_{sc}$ is the hyperparameter. We introduce the auxiliary function $F(= f(\cdot; w^k)-f(\cdot; w^{k-1}))$ that modifies the PDE loss at each optimization iteration to help prevent premature convergence in a poor local minima. Drawing inspiration from the implicit residual smoothing method, equation (19) can be casted as:

$$
f(\cdot; w^k) - f(\cdot; w^{k-1}) = \tau_{sc}R
\tag{20}
$$

$$
R = \Gamma * R
$$

is a smoothed residual obtained by performing convolution operator $\Gamma$, such that it can provide sufficient smoothing to improve convergence while being computationally efficient. The following numerical convolution operator is chosen in this study:

$$
\Gamma \approx \Gamma_\alpha = (I - \alpha^2\nabla^2)^{-1}
\tag{21}
$$

where $\alpha$ is filtered length and acts as a hyperparameter.

It is noted that the above function is associated with Green function of Helmholtz equation, which has been utilized in Leray-$\alpha$ turbulence model [47] as well as a smoothing kernel [48, 49]. It has also been shown that based on choice of filtered length, $\alpha$, this function has the ability to filter the corresponding wavenumber [46, 47, 50], so as to improve convergence in typical PDE solvers. By substituting equation (21) into equation (20), and defining residual smoothing operator $P \equiv \Gamma^{-1}$, the following equations can be derived:

$$
\frac{1}{\tau_{sc}}F = \Gamma_\alpha * R = (I-\alpha^2\nabla^2)^{-1}R
\tag{22a}
$$

$$
\frac{1}{\tau_{sc}}P_\alpha F = R
\tag{22b}
$$

where $P_\alpha = (I-\alpha^2\nabla^2)$. When the solution is fully converged, the auxiliary term $F = f(\cdot; w^k)-f(\cdot; w^{k-1})$ will vanish, ensuring the PDE residual $R = h(\cdot)-N_\vartheta[f(\cdot; w^k)]$ still equates to zero.

We employ the above equation (22b) as the sequential corrected PDE loss function $L_{sc-pde}$ at iteration $k > 0$,

$$
L^{k}_{sc-pde}
=
\left\|
N_\vartheta[f(\cdot; w^k)] - h(\cdot) + \frac{1}{\tau_{sc}}P_\alpha\big(f(\cdot; w^k)-f(\cdot; w^{k-1})\big)
\right\|^2_{L^2(\Omega \times (0,T])}
\tag{23}
$$

Algorithm 1 summarizes the computational procedures for the present Scale-PINN. In summary, the algorithm: (1) infuses the concept of numerical algorithms with enhanced robustness and stability to improve convergence; (2) converges to the original system when the loss value approaches zero, so it does not affect the ultimate accuracy; and (3) remains simple and easy to implement so as to ensure that the overall computational time does not increase significantly.

#### Algorithm 1 Sequential Correction Algorithm for Learning Efficient PINN (Scale-PINN)

**INPUT:** network architecture $f$, initial network weights $w^0$, $w^{-1} = w^0$ and learning algorithm hyperparameters $(\tau_{sc}, \tau_\alpha, \gamma, \lambda_{ic}, \lambda_{bc}, \eta)$  
**OUTPUT:** $f(\cdot; w)$

1. for $k = 0, \ldots, N$ do  
2. Compute the loss terms $L_{ic}$ and $L_{bc}$ through equation 9c and equation 9d:  
   $$
   L^{k}_{ic} = \|f(\cdot, t=0; w^k) - u_0(\cdot)\|^2_{L^2(\Omega)}
   $$
   $$
   L^{k}_{bc} = \|B[f(\cdot; w^k)] - g(\cdot)\|^2_{L^2(\partial\Omega \times (0,T])}
   $$
3. Compute the sequential corrected PDE loss term $L^{k}_{sc-pde}$ by equation 23:  
   $$
   L^{k}_{sc-pde}
   =
   \left\|
   N_\vartheta[f(\cdot; w^k)] - h(\cdot) + \frac{1}{\tau_{sc}}P_\alpha F
   \right\|^2_{L^2(\Omega \times (0,T])}
   $$
   $$
   \frac{1}{\tau_{sc}}P_\alpha F
   =
   \frac{1}{\tau_{sc}}\big(f(\cdot; w^k)-f(\cdot; w^{k-1})\big)
   -
   \frac{\gamma}{\tau_\alpha}
   \big(\nabla^2 f(\cdot; w^k)-\nabla^2 f(\cdot; w^{k-1})\big)
   $$
4. Compute the Scale-PINN objective function:  
   $$
   L_{sc}(w^k) = L^{k}_{sc-pde} + \lambda_{ic}L^{k}_{ic} + \lambda_{bc}L^{k}_{bc}
   $$
5. Update the parameters $w$ via gradient descent (such as SGD and Adam algorithms) with learning rate $\eta$:  
   $$
   w^{k+1} = w^k - \eta \nabla L_{sc}(w^k)
   $$
6. end for

Other choices of the residual smoothing operator $P$ can be made based on prior knowledge, domain expertise, and desired convergence properties specific to the physics. For example, bi-Laplacian operator has been chosen in [46], resulting in solutions with better accuracy. It is also noted that equation (19) is a special case of equation (20), when the identity operator $I$ is chosen as the residual smoothing operator ($P = P_I = I$).

### 4.4 Description of the PINN simulation problem

#### 4.4.1 Incompressible Navier-Stokes equations

Under the isothermal and steady-state assumption, the incompressible N-S equations that govern the fluid flows can be expressed as continuity and momentum equations:

$$
\nabla \cdot \vec{u} = 0
\tag{24a}
$$

$$
(\vec{u} \cdot \nabla)\vec{u} = \frac{1}{Re}\nabla^2\vec{u} - \nabla p
\tag{24b}
$$

The dependent variables $\vec{u} = [u, v]^\top$ represent the velocity, and $p$ represents the pressure. The non-dimensional parameter $Re$ represents the ratio between inertial forces and viscous forces. Complex physical phenomenon can be observed with an increased Reynolds number ($Re$). The N-S equations are notoriously difficult to accurately solve, due to the high nonlinearity, convection instability and the strict constraint of mass conservation.

The sequential corrected PDE loss terms are derived in Section 2 equations (6-7), with $\gamma$ set as $1/Re$. We fine-tune $\tau_{sc}$ and $\tau_\alpha$ for each problem below.

##### Lid-driven cavity flow problems

We simulate the lid-driven cavity flow with the top lid velocity ($u_{lid} = 1$) inside a 2D unit square, $x \in [0, 1]$, $y \in [0, 1]$, from $Re = 400$ to $Re = 20k$. To validate the Scale-PINN results, we generate high-fidelity reference solutions using the coupled version of improved divergence-free-condition compensated coupled (IDFC2) method [37], based on the quasi multi-moment framework and dispersion-relation preserving finite volume convection scheme. Ansys Fluent is also employed to generate the simulation results for time comparisons of the lid-driven cavity problem with $Re = 3200$. To ensure the accuracy of the solution, QUICK scheme [51] is chosen for the convection term, while the SIMPLE method [52] is utilized for the velocity-pressure coupling. For generating reference solution of lid-driven cavity flow problem with $Re = 20k$, a pseudo-transient coupled solver is employed to ensure convergence. The resultant linear system is solved by the algebraic multi-grid solver. These reference solutions, under mesh resolution of $512 \times 512$ as ground truth (mesh-independence tests confirm that a $512 \times 512$ mesh provides a converged ground-truth solution), are then down-sampled to $100\times100$ ($Re = 400, 3200$), $150\times150$ ($Re = 7500$), and $256\times256$ ($Re = 10k, 20k$) sample points for the PINN validation.

##### Flow past obstacles problems

Three scenarios of flow past obstacles have been investigated in this study to validate the applicability and efficiency of Scale-PINN:

1. Single NACA0012 airfoil with $7^\circ$ angle of attack, $Re = 1000$
2. Two-staggered NACA0012 airfoils with $7^\circ$ angle of attack, $Re = 500$
3. Three-staggered square cylinders, $Re = 25$

The above canonical problems are relevant for engineering applications in aerodynamics and urban flow. The computational domain for the single airfoil scenario is $x \in [-3, 5]$, $y \in [-2, 2]$. For the two staggered airfoils case, the horizontal and vertical distances between the two staggered airfoils are 0.5 and 0.2 respectively, in the domain $x \in [-3, 7]$, $y \in [-2.5, 2.5]$. For the three staggered square cylinders case (a canonical proxy for wind flow around buildings), three unit squares are located at $(8, -2)$, $(10, 2)$, $(12, 0)$ in a domain defined by $x \in [0, 30]$, $y \in [-7.5, 7.5]$. For all three flow past obstacles problems, uniform inlet is employed at left boundary ($u = 1, v = 0$), pressure outlet is employed at right boundary ($p = 0$), while the slip boundary condition is employed for side boundaries $\left( \frac{\partial u}{\partial y} = 0, v = 0 \right)$.

IDFC2, together with the convolutional direct forcing immersed boundary (cDFIB) method [49], is employed to generate high-fidelity reference solutions with the complex geometries, under the mesh resolutions of $2048\times1024$, $2560\times1280$, and $1024\times512$, respectively, for single-airfoil, two-staggered airfoils, and three-staggered square cylinders. These reference solutions are then down-sampled to $801\times401$ (single-airfoil) and $1001\times501$ (two-staggered airfoils and three-staggered square cylinders) sample points for the PINN validation.

##### Rayleigh-Bénard convection problem

Rayleigh-Bénard convection is a thermal instability phenomenon due to the temperature difference between the bottom hot plane and the top cold plane [53]. When the buoyancy forces overcome the viscous forces, flow starts to develop and result in convection cells, and can lead to transient and chaotic behavior when the temperature-gradient-driven buoyancy forces dominates. The problem is particularly relevant in urban sustainability studies, where modeling natural convection processes can inform energy efficiency, ventilation, and thermal comfort assessment.

The governing equations of the multiphysics transient dynamics can be written as follows:

$$
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0
\tag{25a}
$$

$$
\frac{\partial u}{\partial t}
+
u\frac{\partial u}{\partial x}
+
v\frac{\partial u}{\partial y}
=
\sqrt{\frac{Pr}{Ra}}
\left(
\frac{\partial^2 u}{\partial x^2}
+
\frac{\partial^2 u}{\partial y^2}
\right)
-
\frac{\partial p}{\partial x}
\tag{25b}
$$

$$
\frac{\partial v}{\partial t}
+
u\frac{\partial v}{\partial x}
+
v\frac{\partial v}{\partial y}
=
\sqrt{\frac{Pr}{Ra}}
\left(
\frac{\partial^2 v}{\partial x^2}
+
\frac{\partial^2 v}{\partial y^2}
\right)
-
\frac{\partial p}{\partial y}
+
T
\tag{25c}
$$

$$
\frac{\partial T}{\partial t}
+
u\frac{\partial T}{\partial x}
+
v\frac{\partial T}{\partial y}
=
\frac{1}{\sqrt{Pr\,Ra}}
\left(
\frac{\partial^2 T}{\partial x^2}
+
\frac{\partial^2 T}{\partial y^2}
\right)
\tag{25d}
$$

In the above, the dependent variables $\vec{u} = [u, v]^\top$ represent the velocity, $p$ represents the pressure, and $T$ represents the temperature. $Ra$ is the Rayleigh number that describes the ratio between buoyancy forces and viscous forces, and $Pr$ is the Prandtl number that represents the ratio between momentum diffusivity and thermal diffusivity.

We simulate the transient dynamic in a spatial domain $x \in [0, 4]$, $y \in [0, 1]$, and time domain $t \in [0, 50]$, with $Ra = 100k$ and $Pr = 0.71$, and boundary conditions $T = 0.5$ for the bottom hot plane and $T = -0.5$ for the top cold plane. The side boundary conditions are set as adiabatic. In this study, the steady-state solution with $Ra = 2k$ is used as initial condition to ensure the uniqueness of the transient behavior (the problem is sensitive to the initial condition [54, 55]). The reference solution is generated under mesh resolution of $1024 \times 256$ with time step size 0.001 by second order backward differentiation formula using IDFC2 solver. This reference solution is then down-sampled to $258 \times 66 \times 501$ spatio-temporal sample points for PINN validation.

The Scale-PINN objective function for simulating the Rayleigh-Bénard convection is thus defined as:
$L_{sc}(w^k) = L^{k}_{sc-pde}(R_c) + L^{k}_{sc-pde}(R_u) + L^{k}_{sc-pde}(R_v) + L^{k}_{sc-pde}(R_T) + \lambda_{bc}L^{k}_{bc} + \lambda_{ic}L^{k}_{ic}$.

We derive the sequential corrected PDE loss terms for equations (25a-25d) as:

$$
L^{k}_{sc-pde}(R_c) =
\left\|
\frac{\partial u^k}{\partial x}
+
\frac{\partial v^k}{\partial y}
+
SR_c
\right\|^2_{L^2(\Omega)}
\tag{26a}
$$

$$
L^{k}_{sc-pde}(R_u) =
\left\|
\frac{\partial u^k}{\partial t}
+
u^k\frac{\partial u^k}{\partial x}
+
v^k\frac{\partial u^k}{\partial y}
-
\sqrt{\frac{Pr}{Ra}}
\left(
\frac{\partial^2 u^k}{\partial x^2}
+
\frac{\partial^2 u^k}{\partial y^2}
\right)
+
\frac{\partial p^k}{\partial x}
+
SR_u
\right\|^2_{L^2(\Omega)}
\tag{26b}
$$

$$
L^{k}_{sc-pde}(R_v) =
\left\|
\frac{\partial v^k}{\partial t}
+
u^k\frac{\partial v^k}{\partial x}
+
v^k\frac{\partial v^k}{\partial y}
-
\sqrt{\frac{Pr}{Ra}}
\left(
\frac{\partial^2 v^k}{\partial x^2}
+
\frac{\partial^2 v^k}{\partial y^2}
\right)
+
\frac{\partial p^k}{\partial y}
+
SR_v
\right\|^2_{L^2(\Omega)}
\tag{26c}
$$

$$
L^{k}_{sc-pde}(R_T) =
\left\|
\frac{\partial T^k}{\partial t}
+
u^k\frac{\partial T^k}{\partial x}
+
v^k\frac{\partial T^k}{\partial y}
-
\sqrt{\frac{1}{Pr\,Ra}}
\left(
\frac{\partial^2 T^k}{\partial x^2}
+
\frac{\partial^2 T^k}{\partial y^2}
\right)
+
SR_T
\right\|^2_{L^2(\Omega)}
\tag{26d}
$$

$$
SR_c = \frac{1}{\tau_{sc}}(p^k-p^{k-1})
\tag{26e}
$$

$$
SR_u =
\frac{1}{\tau_{sc}}(u^k-u^{k-1})
-
\frac{\gamma_{Ruv}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2 u^k}{\partial x^2}
+
\frac{\partial^2 u^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2 u^{k-1}}{\partial x^2}
+
\frac{\partial^2 u^{k-1}}{\partial y^2}
\right)
\right]
\tag{26f}
$$

$$
SR_v =
\frac{1}{\tau_{sc}}(v^k-v^{k-1})
-
\frac{\gamma_{Ruv}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2 v^k}{\partial x^2}
+
\frac{\partial^2 v^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2 v^{k-1}}{\partial x^2}
+
\frac{\partial^2 v^{k-1}}{\partial y^2}
\right)
\right]
\tag{26g}
$$

$$
SR_T =
\frac{1}{\tau_{sc}}(T^k-T^{k-1})
-
\frac{\gamma_{RT}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2 T^k}{\partial x^2}
+
\frac{\partial^2 T^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2 T^{k-1}}{\partial x^2}
+
\frac{\partial^2 T^{k-1}}{\partial y^2}
\right)
\right]
\tag{26h}
$$

where $\gamma_{Ruv} = \sqrt{\frac{Pr}{Ra}}$, $\gamma_{RT} = \sqrt{\frac{1}{PrRa}}$ (same as the diffusion coefficient), while $\tau_{sc}$ and $\tau_\alpha$ are separate tuning hyperparameters.

#### 4.4.2 Kuramoto-Sivashinsky equation

The Kuramoto-Sivashinsky equation is a fourth order nonlinear PDE that models fluid film flows [56]:

$$
\frac{\partial u}{\partial t}
+
a_1 u\frac{\partial u}{\partial x}
+
a_2\frac{\partial^2u}{\partial x^2}
+
a_3\frac{\partial^4u}{\partial x^4}
=
0
\tag{27}
$$

Due to the interaction between the nonlinear term with the diffusion and anti-diffusion terms, the solutions of Kuramoto-Sivashinsky equation exhibit chaotic spatio-temporal patterns. We apply Scale-PINN to solve for the solution in spatial domain $x \in [0, 2\pi]$ and time domain $t \in [0, 0.4]$ with periodic spatial boundary condition and initial condition $u_0(x) = \cos(x)(1 + \sin(x))$, where $a_1 = \frac{100}{16}$, $a_2 = \frac{100}{16^2}$ and $a_3 = \frac{100}{16^2}$. The above settings make the system very stiff, and intrinsically hard to solve by a PINN model. The reference ($512\times101$) solution is obtained from [10], generated using the Chebfun package [57] employing a fourth-order stiff time-stepping scheme (ETDRK4) [58].

The Scale-PINN objective function for simulating Kuramoto-Sivashinsky solution is thus defined as:
$L_{sc}(w^k) = L^{k}_{sc-pde}(KS) + \lambda_{bc}L^{k}_{bc} + \lambda_{ic}L^{k}_{ic}$.
We derive the sequential corrected PDE loss for Kuramoto-Sivashinsky equation:

$$
L^{k}_{sc-pde}(KS) =
\left\|
\frac{\partial u^k}{\partial t}
+
a_1u^k\frac{\partial u^k}{\partial x}
+
a_2\frac{\partial^2u^k}{\partial x^2}
+
a_3\frac{\partial^4u^k}{\partial x^4}
+
S_{KS}
\right\|^2_{L^2(\Omega)}
\tag{28a}
$$

$$
S_{KS}
=
\frac{1}{\tau_{sc}}(u^k-u^{k-1})
-
\frac{\gamma_{KS}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2u^k}{\partial x^2}
+
\frac{\partial^2u^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2u^{k-1}}{\partial x^2}
+
\frac{\partial^2u^{k-1}}{\partial y^2}
\right)
\right]
\tag{28b}
$$

We set $\gamma_{KS} = a_2$, which is the same magnitude of the anti-diffusion coefficient, while $\tau_{sc}$ and $\tau_\alpha$ are then fine-tuned.

#### 4.4.3 Grey-Scott equations

The Gray–Scott equations describe nonlinear chemical kinetics governed by coupled reaction–diffusion dynamics [59]:

$$
\frac{\partial u^k}{\partial t}
=
\epsilon_1
\left(
\frac{\partial^2u}{\partial x^2}
+
\frac{\partial^2u}{\partial y^2}
\right)
+
b_1(1-u)
-
c_1uv^2
\tag{29a}
$$

$$
\frac{\partial v}{\partial t}
=
\epsilon_2
\left(
\frac{\partial^2v}{\partial x^2}
+
\frac{\partial^2v}{\partial y^2}
\right)
-
b_2v
+
c_2uv^2
\tag{29b}
$$

We follow the settings in [11], i.e., $\epsilon_1 = 0.2$, $\epsilon_2 = 0.1$, $b_1 = 40$, $b_2 = 100$ and $c_1 = c_2 = 1000$, with periodic spatial boundary condition. We apply Scale-PINN to solve for the solution in the spatio-temporal domain, $x \in [-1, 1]$, $y \in [-1, 1]$, and $t \in [0, 0.5]$, given the initial condition:

$$
u_0(x,y) = 1 - \exp\left(-10\big((x+0.05)^2 + (y+0.02)^2\big)\right)
\tag{30a}
$$

$$
v_0(x,y) = \exp\left(-10\big((x-0.05)^2 + (y-0.02)^2\big)\right)
\tag{30b}
$$

The reference ($200\times200\times26$) solution is obtained from [11], generated with the ETDRK4 numerical scheme using Chebfun package.

The Scale-PINN objective function for simulating Gray–Scott solutions is thus defined as:
$L_{sc}(w^k) = L^{k}_{sc-pde}(GS_u) + L^{k}_{sc-pde}(GS_v) + \lambda_{bc}L^{k}_{bc} + \lambda_{ic}L^{k}_{ic}$.
We derive the sequential corrected PDE loss for Gray–Scott equations:

$$
L^{k}_{sc-pde}(GS_u) =
\left\|
\frac{\partial u^k}{\partial t}
-
\epsilon_1
\left(
\frac{\partial^2u^k}{\partial x^2}
+
\frac{\partial^2u^k}{\partial y^2}
\right)
-
b_1(1-u^k)
+
c_1u^k(v^k)^2
+
SGS_u
\right\|^2_{L^2(\Omega)}
\tag{31a}
$$

$$
L^{k}_{sc-pde}(GS_v) =
\left\|
\frac{\partial v^k}{\partial t}
-
\epsilon_2
\left(
\frac{\partial^2v^k}{\partial x^2}
+
\frac{\partial^2v^k}{\partial y^2}
\right)
+
b_2v^k
-
c_2u^k(v^k)^2
+
SGS_v
\right\|^2_{L^2(\Omega)}
\tag{31b}
$$

$$
SGS_u =
\frac{1}{\tau_{sc}}(u^k-u^{k-1})
-
\frac{\gamma_{GSu}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2u^k}{\partial x^2}
+
\frac{\partial^2u^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2u^{k-1}}{\partial x^2}
+
\frac{\partial^2u^{k-1}}{\partial y^2}
\right)
\right]
\tag{31c}
$$

$$
SGS_v =
\frac{1}{\tau_{sc}}(v^k-v^{k-1})
-
\frac{\gamma_{GSv}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2v^k}{\partial x^2}
+
\frac{\partial^2v^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2v^{k-1}}{\partial x^2}
+
\frac{\partial^2v^{k-1}}{\partial y^2}
\right)
\right]
\tag{31d}
$$

We set $\gamma_{GSu} = \epsilon_1$, $\gamma_{GSv} = \epsilon_2$, while $\tau_{sc}$ and $\tau_\alpha$ are then fine-tuned.

#### 4.4.4 Korteweg–De Vries equation

The Korteweg–De Vries equation is a third order nonlinear dispersive PDE that models shallow water waves [60]:

$$
\frac{\partial u}{\partial t}
+
u\frac{\partial u}{\partial x}
+
\nu\frac{\partial^3u}{\partial x^3}
=
0
\tag{32}
$$

We apply Scale-PINN to solve for the solution for $\nu = \left(\frac{11}{500}\right)^2$ in spatial domain $x \in [-1, 1]$ and time domain $t \in [0, 1]$ with periodic spatial boundary condition and initial condition $u_0(x) = \cos(\pi x)$. The reference ($512\times201$) solution is obtained from [11], generated with the ETDRK4 numerical scheme using Chebfun package.

The Scale-PINN objective function for simulating Korteweg–De Vries solution is thus defined as:
$L_{sc}(w^k) = L^{k}_{sc-pde}(KdV) + \lambda_{bc}L^{k}_{bc} + \lambda_{ic}L^{k}_{ic}$.
We derive the sequential corrected PDE loss for Korteweg–De Vries equation:

$$
L^{k}_{sc-pde}(KdV) =
\left\|
\frac{\partial u^k}{\partial t}
+
u^k\frac{\partial u^k}{\partial x}
+
\nu\frac{\partial^3u^k}{\partial x^3}
+
S_{KdV}
\right\|^2_{L^2(\Omega)}
\tag{33a}
$$

$$
S_{KdV} =
\frac{1}{\tau_{sc}}(u^k-u^{k-1})
-
\frac{\gamma_{KdV}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2u^k}{\partial x^2}
+
\frac{\partial^2u^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2u^{k-1}}{\partial x^2}
+
\frac{\partial^2u^{k-1}}{\partial y^2}
\right)
\right]
\tag{33b}
$$

We set $\gamma_{KdV} = \sqrt{\nu}$, which is the square-root of the dispersion coefficient, while $\tau_{sc}$ and $\tau_\alpha$ are then fine-tuned.

#### 4.4.5 Allen-Cahn equation

Both Korteweg–De Vries and Allen–Cahn equations are commonly studied benchmark problems in the PINN literature. The Allen–Cahn equation models crystal growth and phase separation as a diffusion–reaction process [61]:

$$
\frac{\partial u}{\partial t}
-
\alpha\frac{\partial^2u}{\partial x^2}
+
\delta(u^3-u)
=
0
\tag{34}
$$

We apply Scale-PINN to solve for the solution for $\alpha = 0.0001$ and $\delta = 5$ in spatial domain $x \in [-1, 1]$ and time domain $t \in [0, 1]$ with periodic spatial boundary condition and initial condition $u_0(x) = x^2\cos(\pi x)$. The reference ($512\times201$) solution is obtained from [11], generated with the ETDRK4 numerical scheme using Chebfun package.

The Scale-PINN objective function for simulating Allen–Cahn solution is thus defined as:
$L_{sc}(w^k) = L^{k}_{sc-pde}(AC) + \lambda_{bc}L^{k}_{bc} + \lambda_{ic}L^{k}_{ic}$.
We derive the sequential corrected PDE loss for Allen–Cahn equation:

$$
L^{k}_{sc-pde}(AC) =
\left\|
\frac{\partial u^k}{\partial t}
-
\alpha\frac{\partial^2u^k}{\partial x^2}
+
\delta\big((u^k)^3-u^k\big)
+
S_{AC}
\right\|^2_{L^2(\Omega)}
\tag{35a}
$$

$$
S_{AC} =
\frac{1}{\tau_{sc}}(u^k-u^{k-1})
-
\frac{\gamma_{AC}}{\tau_\alpha}
\left[
\left(
\frac{\partial^2u^k}{\partial x^2}
+
\frac{\partial^2u^k}{\partial y^2}
\right)
-
\left(
\frac{\partial^2u^{k-1}}{\partial x^2}
+
\frac{\partial^2u^{k-1}}{\partial y^2}
\right)
\right]
\tag{35b}
$$

In the above, $\gamma_{AC}$ is set as $\alpha$. $\tau_{sc}$ and $\tau_\alpha$ are then fine-tuned.

### 4.5 Scale-PINN model architecture and training strategies

#### 4.5.1 Neural architecture and activation function design

Scale-PINN employs a multi-layer perceptron (MLP) architecture as the backbone network, chosen for its proven effectiveness in approximating dynamical process, as well as its flexible design and ease of implementation. To more effectively learn a model output—mapped from the spatio-temporal input coordinates—that captures high-frequency features, which are prevalent in many dynamical systems, we initialize the network with artificial high-frequency components by modulating the first hidden layer with a factor of $F\pi$ in combination with a sine activation, as illustrated in Fig. 1. Here, $F$ serves as a problem-specific tuning parameter that controls the initial high-frequency range. During training, these frequencies are naturally reduced to an appropriate range—a process we refer to as frequency annealing.

Two specialized MLP architectures are designed to accommodate the characteristics of different PDE problems.

##### N-S flow network

The network consists of multiple shared hidden layers mapped from spatio-temporal input coordinates, which then branch into variable-specific hidden layers for $u$, $v$, and $p$, respectively. For Rayleigh-Bénard convection problem, the network contains an additional branch for $T$.

```text
f_u(x,t;w) = W_{u,L} x_{u,L}      (output layer: u)
x_{u,L} = ψ(W_{u,L-1}x_{u,L-1} + b_{u,L-1})
...
f_v(x,t;w) = W_{v,L} x_{v,L}      (output layer: v)
x_{v,L} = ψ(W_{v,L-1}x_{v,L-1} + b_{v,L-1})
...
f_p(x,t;w) = W_{p,L} x_{p,L}      (output layer: p)
x_{p,L} = ψ(W_{p,L-1}x_{p,L-1} + b_{p,L-1})
...
x_{u,1}, x_{v,1}, x_{p,1} ← x_L   (multi-branch)
x_L = ψ(W_{L-1}x_{L-1} + b_{L-1}) (shared hidden layers)
...
x_3 = ψ(z_2)                      (after activation)
z_2 = W_2x_2 + b_2               (2nd hidden layer)
x_2 = sin(z_1)                    (frequency annealing)
z_1 ← Fπ z_1                      (frequency annealing)
z_1 = W_1x_1 + b_1               (1st hidden layer)
x_1 ≡ (x,t)                       (input)
```

where
$w = [W_1,b_1,\ldots,W_{L-1},b_{L-1},\ldots,W_{u,L-1},b_{u,L-1},W_{u,L},\ldots,W_{v,L},\ldots,W_{p,L}]$.
The N–S flow network uses the SiLU activation function starting from the second hidden layer. We note that N–S flow network is a robust and highly performant neural architecture for many N-S flow problems [20, 21, 34].

##### Skip connections network

The network utilizes concatenative skip connections such that all the nonlinear hidden layers are concatenated at the final hidden layer.

```text
f(x,t;w) = W_L x_L                (output layer)
x_L ← concatenate(x_L, x_{L-1}, ..., x_2)   (skip connections)
x_L = ψ(z_{L-1})
...
x_3 = ψ(z_2)                      (after activation)
z_2 = W_2x_2 + b_2               (2nd hidden layer)
x_2 = sin(z_1)                    (frequency annealing)
z_1 ← Fπ z_1                      (frequency annealing)
z_1 = W_1x_1 + b_1               (1st hidden layer)
x_1 ≡ (x,t)                       (input)
```

where $w = [W_1, b_1, \ldots, W_L]$. The skip connections network uses either the SiLU or softplus activation function starting from the second hidden layer. This neural architecture design allows us to increase the output layer width by stacking multiple hidden layers, thereby effectively improving the expressivity of the network, while maintaining a moderate number of nodes in each hidden layer. In addition, we note that the final hidden layer concatenation bears similarity to the way one constructs a polynomial basis space such as the monomial basis space. The additional operations at each hidden layer are analogous to the recurrence relations used in generating Chebyshev polynomials, and incorporation and concatenation of more hidden layers in the MLP essentially results in the creation of a larger (albeit finite) and more expressive basis space (with less truncation).

#### 4.5.2 Model training and hyperparameters

Scale-PINN is trained using the Adam optimizer with a warm-up cosine decay learning rate schedule, where the minimum learning rate is set to $1e^{-10}$. Table A1 provides a summary of the Scale-PINN model architecture and training settings for all the studied PDE problems.

#### 4.5.3 Computational Environment

All benchmark experiments are conducted on a workstation using a single NVIDIA GeForce RTX 3090 GPU. The Scale-PINN algorithm is implemented in the JAX framework to leverage its efficiency in automatic differentiation and linear algebra operations [62, 63].

**Code availability.** The example codes with instructions are available at https://github.com/chiuph/SCALE-PINN.

## Appendix A Extended Data

Table A1 provides a summary of the Scale-PINN model architecture and training settings for all the studied PDE problems.

### Table A1 Scale-PINN model architecture and training settings

| Problem | Neural architecture1 | Frequency aneling, [F]π | Activation | Batch size /iter. | No. training iter. | Initial learning rate | Loss function, λic, λbc | Sequential corrected loss term, τsc, τα |
|---|---|---|---|---:|---:|---|---|---|
| 1a Navier-Stokes equations: lid-driven cavity flow Re = 400 − 3200 | (x, y) − 128 − 32 − 32 − [32 − 32 − 32 − (u), 32 − 32 − 32 − (v), 32 − 32 − 32 − (p)] | 2π | silu | 400 | 50k | 1e-3 - 5e-4 | -, 10 - 15 | 0.06 - 0.095, 0.5 - 1 |
| 1b Navier-Stokes equations: lid-driven cavity flow Re = 7500 − 20k | (x, y) − 256 − 64 − 64 − [64 − 64 − 64 − (u), 64 − 64 − 64 − (v), 64 − 64 − 64 − (p)] | 2π | silu | 1,000 - 2,400 | 50k - 100k | 5e-4 | -, 10 - 20 | 0.095 - 0.11, 0.5 - 0.6 |
| 2 Navier-Stokes equations: 1-NACA0012 airfoil | (x, y) − 64 − 32 − 32 − [32 − 32 − 32 − (u), 32 − 32 − 32 − (v), 32 − 32 − 32 − (p)] | π | silu | 4,000 | 50k | 5e-3 | -, 5 | 0.1, 0.5 |
| 3 Navier-Stokes equations: 2-staggered airfoils | (x, y) − 64 − 32 − 32 − [32 − 32 − 32 − (u), 32 − 32 − 32 − (v), 32 − 32 − 32 − (p)] | π | silu | 4,000 | 50k | 5e-3 | -, 5 | 0.05, 1 |
| 4 Navier-Stokes equations: 3-staggered square cylinders | (x, y) − 64 − 32 − 32 − [32 − 32 − 32 − (u), 32 − 32 − 32 − (v), 32 − 32 − 32 − (p)] | π | silu | 4,000 | 80k | 5e-3 | -, 5 | 0.035, 15 |
| 5 Navier-Stokes equations: Rayleigh-Bénard convection | (x, y, t) − 128 − 64 − 64 − [64 − 64 − 64 − (u), 64 − 64 − 64 − (v), 64 − 64 − 64 − (p), 64 − 64 − 64 − (T)] | 4π | silu | 4,000 | 50k | 5e-3 | 1, 10 | 0.1, 1.5 |
| 6 Kuramoto-Sivashinsky equation | (x, t) − 128 − 128 − 128 − 128 + − (u) | 4π | silu | 1,000 | 200k | 1e-3 | 500, 5000 | 0.2, 1.5 |
| 7 Grey-Scott equations | (x, y, t) − 128 − 128 − 128 − 128 + − (u, v) | 2π | silu | 1,000 | 300k | 2e-3 | 5000, 1000 | 0.02, 10 |
| 8 Korteweg–De Vries equation | (x, t) − 128 − 128 − 128 − 128 + − (u) | 2π | softplus | 1,000 | 300k | 1e-3 | 1000, 1000 | 0.1, 20 |
| 9 Allen-Cahn equation | (x, t) − 128 − 128 − 128 − 128 − (u) | 2π | silu | 1,000 | 500k | 2e-3 | 100, 100 | 0.4, 1.5 |

1For the MLP architecture, the numbers in between input and output represent the number of nodes in each hidden layer. For example, $(x) − 64 − 32 − 32 − 32 + − (u)$ indicates a single input $x$, followed by 4 hidden layers with 64, 32, 32 and 32 nodes in each layer, and a single output $u$. We apply the sinusoidal features mapping [64] to replace first hidden layer (frequency annealing) and initialize all network weights using He method. Besides, the superscript $+$ at final hidden layer indicates a concatenative skip connections such that all the nonlinear hidden layers are concatenated at the final hidden layer.

## References

[1] Karniadakis, G.E., Kevrekidis, I.G., Lu, L., Perdikaris, P., Wang, S., Yang, L.: Physics-informed machine learning. *Nature Reviews Physics* 3(6), 422–440 (2021)

[2] Park, C., Saha, S., Guo, J., Zhang, H., Xie, X., Bessa, M.A., Qian, D., Chen, W., Wanger, G.J., Cao, J., et al.: Unifying machine learning and interpolation theory via interpolating neural networks. *Nature Communications* 16(1), 8753 (2025)

[3] Tang, Y., Fan, J., Li, X., Ma, J., Qi, M., Yu, C., Gao, W.: Physics-informed recurrent neural network for time dynamics in optical resonances. *Nature computational science* 2(3), 169–178 (2022)

[4] Okazaki, T., Ito, T., Hirahara, K., Ueda, N.: Physics-informed deep learning approach for modeling crustal deformation. *Nature Communications* 13(1), 7092 (2022)

[5] Raabe, D., Mianroodi, J.R., Neugebauer, J.: Accelerating the design of compositionally complex materials via physics-informed artificial intelligence. *Nature computational science* 3(3), 198–209 (2023)

[6] Wang, F., Zhai, Z., Zhao, Z., Di, Y., Chen, X.: Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis. *Nature Communications* 15(1), 4332 (2024)

[7] Kharazmi, E., Cai, M., Zheng, X., Zhang, Z., Lin, G., Karniadakis, G.E.: Identifiability and predictability of integer-and fractional-order epidemiological models using physics-informed neural networks. *Nature Computational Science* 1(11), 744–753 (2021)

[8] Liu, Z., Liu, Y., Yan, X., Liu, W., Nie, H., Guo, S., Zhang, C.-a.: Automatic network structure discovery of physics informed neural networks via knowledge distillation. *Nature Communications* 16(1), 9558 (2025)

[9] Zhou, W., Song, H., Chu, X.: Automated design for physics-informed modeling with convolutional neural networks. *Communications Physics* (2025)

[10] Wang, S., Sankaran, S., Wang, H., Perdikaris, P.: *An Expert’s Guide to Training Physics-informed Neural Networks* (2023). https://arxiv.org/abs/2308.08468

[11] Wang, S., Li, B., Chen, Y., Perdikaris, P.: Piratenets: Physics-informed deep learning with residual adaptive networks. *Journal of Machine Learning Research* 25(402), 1–51 (2024)

[12] Wang, S., Bhartari, A.K., Li, B., Perdikaris, P.: Gradient alignment in physics-informed neural networks: A second-order optimization perspective. *arXiv preprint* arXiv:2502.00604 (2025)

[13] McGreivy, N., Hakim, A.: Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations. *Nature machine intelligence* 6(10), 1256–1269 (2024)

[14] Jiang, Q., Shu, C., Zhu, L., Yang, L., Liu, Y., Zhang, Z.: Applications of finite difference-based physics-informed neural networks to steady incompressible isothermal and thermal flows. *International Journal for Numerical Methods in Fluids* 95, 1565–1597 (2023) https://doi.org/10.1002/fld.5217

[15] Zou, Y., Li, T., Lu, L., Wang, J., Zou, S., Zhang, L., Deng, X.: Finite-difference-informed graph network for solving steady-state incompressible flows on block-structured grids. *Physics of Fluids* 36, 103608 (2024) https://doi.org/10.1063/5.0228104

[16] Roy, N., Dürr, R., Bück, A., Sundar, S.: Finite difference physics-informed neural networks enable improved solution accuracy of the Navier-Stokes equations (2024). https://arxiv.org/abs/2501.00014

[17] Xiao, Y., Yang, L.M., Shu, C., Dong, H., Du, Y.J., Song, Y.X.: Least-square finite difference-based physics-informed neural network for steady incompressible flows. *Computers & Mathematics with Applications* 175, 33–48 (2024) https://doi.org/10.1016/j.camwa.2024.08.035

[18] Yan, X., Lin, J., Ju, Y., Zhang, Q., Zhang, Z., Zhang, L., Yao, J., Zhang, K.: A finite-volume based physics-informed fourier neural operator network for parametric learning of subsurface flow. *Advances in Water Resources*, 105087 (2025)

[19] Yamazaki, Y., Harandi, A., Muramatsu, M., Viardin, A., Apel, M., Brepols, T., Reese, S., Rezaei, S.: A finite element-based physics-informed operator learning framework for spatiotemporal partial differential equations on arbitrary domains. *Engineering with Computers* 41(1), 1–29 (2025)

[20] Chiu, P.-H., Wong, J.C., Ooi, C., Dao, M.H., Ong, Y.-S.: Can-pinn: A fast physics-informed neural network based on coupled-automatic–numerical differentiation method. *Computer Methods in Applied Mechanics and Engineering* 395, 114909 (2022) https://doi.org/10.1016/j.cma.2022.114909

[21] Wong, J.C., Chiu, P.-H., Ooi, C., Dao, M.H., Ong, Y.-S.: Lsa-pinn: Linear boundary connectivity loss for solving pdes on complex geometry. In: *2023 International Joint Conference on Neural Networks (IJCNN)*, pp. 1–10 (2023). https://doi.org/10.1109/IJCNN54540.2023.10191236

[22] Wang, Z., Meng, X., Jiang, X., Xiang, H., Karniadakis, G.E.: Solution multiplicity and effects of data and eddy viscosity on Navier-Stokes solutions inferred by physics-informed neural networks (2023). https://arxiv.org/abs/2309.06010

[23] Cao, W., Zhang, W.: TSONN: Time-stepping-oriented neural network for solving partial differential equations (2023). https://arxiv.org/abs/2310.16491

[24] Cao, Z., Liu, K., Luo, K., Wang, S., Jiang, L., Fan, J.: Surrogate modeling of multi-dimensional premixed and non-premixed combustion using pseudo-time stepping physics-informed neural networks. *Physics of Fluids* 36(11), 113616 (2024) https://doi.org/10.1063/5.0235674

[25] Wong, J.C., Gupta, A., Ooi, C.C., Chiu, P.-H., Liu, J., Ong, Y.-S.: Evolutionary optimization of physics-informed neural networks: Evo-pinn frontiers and opportunities. *IEEE Computational Intelligence Magazine* 21(1), 16–36 (2026)

[26] Ghia, U., Ghia, K., Shin, C.: High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. *J. Comput. Phys.* 48, 387–411 (1982) https://doi.org/10.1016/0021-9991(82)90058-4

[27] Toutant, A.: General and exact pressure evolution equation. *Physics Letters A* 381(44), 3739–3742 (2017) https://doi.org/10.1016/j.physleta.2017.10.008

[28] Toutant, A.: Numerical simulations of unsteady viscous incompressible flows using general pressure equation. *Journal of Computational Physics* 374, 822–842 (2018) https://doi.org/10.1016/j.jcp.2018.07.058

[29] Chorin, A.J.: A numerical method for solving incompressible viscous flow problems. *Journal of Computational Physics* 2(1), 12–26 (1967) https://doi.org/10.1016/0021-9991(67)90037-X

[30] Chiu, P.-H.: An improved divergence-free-condition compensated method for solving incompressible flows on collocated grids. *Computers & Fluids* 162, 39–54 (2018) https://doi.org/10.1016/j.compfluid.2017.12.005

[31] Erturk, E.: Discussions on driven cavity flow. *International journal for numerical methods in fluids* 60(3), 275–294 (2009)

[32] Wong, J.C., Chiu, P.-H., Ooi, C., Dao, M.H., Ong, Y.-S.: Lsa-pinn: Linear boundary connectivity loss for solving pdes on complex geometry. In: *2023 International Joint Conference on Neural Networks (IJCNN)*, pp. 1–10 (2023). IEEE

[33] Khademi, A., Dufour, S.: Physics-informed neural networks with trainable sinusoidal activation functions for approximating the solutions of the navier-stokes equations. *Computer Physics Communications*, 109672 (2025)

[34] Wei, C., Fan, Y., Wong, J.C., Ooi, C.C., Wang, H., Chiu, P.-H.: Ffv-pinn: A fast physics-informed neural network with simplified finite volume discretization and residual correction. *Computer Methods in Applied Mechanics and Engineering* 444, 118139 (2025)

[35] Tsai, Y.-H., Juan, H.-T., Chiu, P.-H., Lin, C.-A.: Mld-pinn: A multi-level datasets training method in physics-informed neural networks. *Computers & Fluids*, 106849 (2025)

[36] He, K., Zhang, X., Ren, S., Sun, J.: Delving deep into rectifiers: Surpassing human-level performance on imagenet classification. In: *Proceedings of the IEEE International Conference on Computer Vision*, pp. 1026–1034 (2015)

[37] Chiu, P.-H., Poh, H.J.: Development of an improved divergence-free-condition compensated coupled framework to solve flow problems with time-varying geometries. *International Journal for Numerical Methods in Fluids* 93, 44–70 (2021) https://doi.org/10.1002/fld.4874

[38] Kurtulus, D.F.: On the unsteady behavior of the flow around naca 0012 airfoil with steady external conditions at re=1000. *International Journal of Micro Air Vehicles* 7(3), 301–326 (2015) https://doi.org/10.1260/1756-8293.7.3.301

[39] Xiao, Y., Yang, L.M., Shu, C., Shen, X., Du, Y.J., Song, Y.X.: Immersed boundary method-incorporated physics-informed neural network for simulation of incompressible flows around immersed objects. *Ocean Engineering* 319, 120239 (2025) https://doi.org/10.1016/j.oceaneng.2024.120239

[40] Saad, Y.: *Iterative Methods for Sparse Linear Systems*, 2nd edn. Society for Industrial and Applied Mathematics, Philadelphia (2003). https://doi.org/10.1137/1.9780898718003

[41] Xu, J.: Iterative methods by space decomposition and subspace correction. *SIAM Review* 34(4), 581–613 (1992) https://doi.org/10.1137/1034116

[42] Morton, K.W., Mayers, D.F.: *Numerical Solution of Partial Differential Equations: An Introduction*. Cambridge University Press, New York (2005)

[43] Choi, H., Moin, P.: On the space-time characteristics of wall-pressure fluctuations. *Physics of Fluids A: Fluid Dynamics* 2(8), 1450–1460 (1990) https://doi.org/10.1063/1.857593

[44] Cinnella, P., Content, C.: High-order implicit residual smoothing time scheme for direct and large eddy simulations of compressible flows. *Journal of Computational Physics* 326, 1–29 (2016) https://doi.org/10.1016/j.jcp.2016.08.023

[45] Wesseling, P.: *Principles of Computational Fluid Dynamics* vol. 29. Springer, Berlin, Springer Series in Computational Mathematics (2001)

[46] Bienner, A., Gloerfelt, X., Yalçın, O., Cinnella, P.: Multiblock parallel high-order implicit residual smoothing time scheme for compressible navier–stokes equations. *Computers & Fluids* 269, 106138 (2024) https://doi.org/10.1016/j.compfluid.2023.106138

[47] Cheskidov, A., D., H., Olson, E., Titi, E.S.: On a Leray-α model of turbulence. *Proc. R. Soc. A* 461, 629–649 (2004) https://doi.org/10.1098/rspa.2004.1373

[48] Chiu, P.-H., Lin, Y.-T.: A conservative phase field method for solving incompressible two-phase flows. *J. Comput. Phys.* 230, 185–204 (2011) https://doi.org/10.1016/j.jcp.2010.09.021

[49] Chiu, P.-H.: cDFIB: A convolutional direct forcing immersed boundary method for solving incompressible flows with time-varying geometries. *J. Comput. Phys.* 487, 112178 (2023) https://doi.org/10.1016/j.jcp.2023.112178

[50] Ilyin, A., Lunasin, E., Titi, E.: A modified-leray-alpha subgrid scale model of turbulence. *Nonlinearity* 19, 879–897 (2006) https://doi.org/10.1088/0951-7715/19/4/006

[51] Leonard, B.P.: A stable and accurate convective modelling procedure based on quadratic upstream interpolation. *Computer Methods in Applied Mechanics and Engineering* 19, 59–98 (1979) https://doi.org/10.1016/0045-7825(79)90034-3

[52] Patankar, S.: *Numerical Heat Transfer and Fluid Flow*. CRC press, Boca Raton (2018)

[53] Castaing, B., Gunaratne, G., Heslot, F., Kadanoff, L., Libchaber, A., Thomae, S., Wu, X.-Z., Zaleski, S., Zanetti, G.: Scaling of hard thermal turbulence in rayleigh-bénard convection. *Journal of Fluid Mechanics* 204, 1–30 (1989) https://doi.org/10.1017/S0022112089001643

[54] Soong, C.Y., Tzeng, P.Y., Chiang, D.C., Sheu, T.S.: Numerical study on mode-transition of natural convection in differentially heated inclined enclosures. *International Journal of Heat and Mass Transfer* 39(14), 2869–2882 (1996) https://doi.org/10.1016/0017-9310(95)00378-9

[55] Li, Y.-R., Ouyang, Y.-Q., Peng, L., Wu, S.-Y.: Direct numerical simulation of rayleigh-bénard convection in a cylindrical container of aspect ratio 1 for moderate prandtl number fluid. *Physics of Fluids* 24(7), 074103 (2012) https://doi.org/10.1063/1.4731296

[56] Kalogirou, A., Keaveny, E.E., Papageorgiou, D.T.: An in-depth numerical study of the two-dimensional kuramoto–sivashinsky equation. *Proc. R. Soc. A.* 471, 20140932 (2015) https://doi.org/10.1098/rspa.2014.0932

[57] Driscoll, T.A., Hale, N., Trefethen, L.N.: *Chebfun guide* (2014)

[58] Cox, S.M., Matthews, P.C.: Exponential time differencing for stiff systems. *J. Comput. Phys.* 176, 430–455 (2002) https://doi.org/10.1006/jcph.2002.6995

[59] Gray, P., Scott, S.K.: *Chemical Oscillations and Instabilities: Non-linear Chemical Kinetics*. Clarendon Press, Oxford (1994)

[60] Korteweg, D.J., Vries, G.: Xli. on the change of form of long waves advancing in a rectangular canal, and on a new type of long stationary waves. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science* 39, 422–443 (1895) https://doi.org/10.1080/14786449508620739

[61] Allen, S.M., Cahn, J.W.: Coherent and incoherent equilibria in iron-rich iron-aluminum alloys. *Acta Metallurgica* 23, 1017–1026 (1975) https://doi.org/10.1016/0001-6160(75)90106-6

[62] Bradbury, J., Frostig, R., Hawkins, P., Johnson, M.J., Leary, C., Maclaurin, D., Necula, G., Paszke, A., VanderPlas, J., Wanderman-Milne, S., et al.: Jax: composable transformations of python+ numpy programs (2018)

[63] Tang, Y., Tian, Y., Ha, D.: Evojax: Hardware-accelerated neuroevolution. *arXiv preprint* arXiv:2202.05008 (2022)

[64] Wong, J.C., Ooi, C., Gupta, A., Ong, Y.-S.: Learning in sinusoidal spaces with physics-informed neural networks. *IEEE Transactions on Artificial Intelligence* (2022) https://doi.org/10.1109/TAI.2022.3192362
```

Если хотите, я могу на следующем шаге:

1. **сделать более чистую версию Markdown** с исправлением OCR-артефактов и унификацией формул,  
2. **отдельно вынести все рисунки и таблицы** в аккуратно оформленные блоки,  
3. **собрать это в `.md`-файл целиком** без пояснений вокруг.