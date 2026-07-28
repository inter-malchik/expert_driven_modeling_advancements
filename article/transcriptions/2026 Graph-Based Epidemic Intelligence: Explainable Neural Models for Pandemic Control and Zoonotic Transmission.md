# Graph-Based Epidemic Intelligence: Explainable Neural Models for Pandemic Control and Zoonotic Transmission

**Francesco Branda** $^1$, **Annamaria Defilippo** $^2$, **Ugo Lomoio** $^2$, **Patrizia Vizza** $^3$, **Fabio Scarpa** $^4$, **Massimo Ciccozzi** $^1$, **Pierangelo Veltri** $^{3,\dagger}$ and **Pietro Hiram Guzzi** $^{2,*,\dagger}$

$^1$ Unit of Medical Statistics and Molecular Epidemiology, Università Campus Bio-Medico di Roma, Via Álvaro del Portillo 21, 00128 Rome, Italy  
$^2$ Department of Surgical and Medical Sciences, University “Magna Graecia” of Catanzaro, 88100 Catanzaro, Italy  
$^3$ DIMES, University of Calabria, 88100 Rende, Italy  
$^4$ Department of Biomedical Sciences, University of Sassari, Viale San Pietro 43, 07100 Sassari, Italy  
$^*$ Correspondence: `hguzzi@unicz.it`  
$^\dagger$ These authors share the last authorship.

**Posted Date:** 15 June 2026  
**doi:** 10.20944/preprints202606.1151.v1  

**Keywords:** network epidemiology; graph neural networks (GNNs); explainable artificial intelligence (XAI); multilayer networks; public health decision support; vaccination optimization

---

### Abstract
Epidemics spread through contact, movement, behavior, and public health interventions, an inherently relational dynamic in which the infection travels along connections between people, places, or animal species. For this reason, we need mathematical and computational models capable of explicitly representing these connections. This paper introduces the theoretical foundations of network-based epidemic models, such as SIR and SEIR, and demonstrates how graph neural networks (GNNs) can learn the spatiotemporal patterns of transmission from data, overcoming the limitations of classical models. Three case studies are presented: measles, i.e., uneven vaccination coverage, COVID-19, i.e., targeted vaccination of the most central nodes in the contact network, and hantavirus, i.e., a multilevel model linking rodents, the environment, the molecular response, and human-to-human transmission). Since public health decisions must be justifiable, the work devotes particular attention to the explainability of the models: identifying which individuals, contacts, or territories are most critical and which alternative interventions could change the outcome of an epidemic. Finally, an operational pipeline is outlined to translate complex data into reliable and transparent decision support.

---

## 1. Introduction

Classical epidemic models aggregate populations into compartments and describe their evolution through systems of differential equations [1]. Such models are mathematically transparent and remain indispensable for estimating growth rates, reproduction numbers, and intervention effects. However, aggregation hides the intrinsic heterogeneity that may determine both the rise and fall of the outbreak. As highlighted in a recent scoping review on social, mobility and contact networks, traditional population-level models often overlook individual discrepancies and network effects, even though these interactions are now recognised as pivotal in shaping disease dynamics and transforming localised outbreaks into global pandemics [2]. For instance, the presence of highly connected individuals, clustered communities, vaccination gaps, and spatially heterogeneous susceptibility can lead to different outbreak outcomes [3].

Graphs provide the natural language for this heterogeneity. A graph represents epidemiological units as nodes and potential transmission channels as edges. Depending on the scale of analysis, nodes may denote persons, households, schools, municipalities, hospitals, farms, ecological patches, or countries. Edges may encode physical contact, mobility, shared environment, vector movement, trade, genetic similarity, or statistical dependence. Epidemic dynamics on graphs therefore connect mathematical epidemiology with network science, statistical learning, and control theory. Recent reviews have emphasised the importance of moving beyond single-layer representations: multiplex network analysis and generative agent-based modelling are promising approaches for integrating the complex interdependencies among social, mobility and contact networks into epidemic dynamics estimation [2,4].

The theoretical foundations of network epidemiology have matured considerably over the past two decades. The seminal work by Pastor-Satorras and Vespignani on epidemic spreading in scale-free networks established that the absence of an epidemic threshold in infinitely large networks fundamentally changes our understanding of disease invasion [5]. Subsequent research by Newman, Kiss, Miller and others provided rigorous frameworks for susceptible-infectious-recovered (SIR) and susceptible-infectious-susceptible (SIS) models on configuration models, random graphs, and real-world networks [5]. A key insight is the role of the spectral radius of the adjacency matrix: the epidemic threshold is given by $\mathcal{R}_0 = \beta/\gamma \cdot \rho(\mathbf{A})$ for the network SIR model, generalising the classical basic reproduction number [1,5]. This spectral condition directly links graph structure to controllability: interventions that reduce $\rho(\mathbf{A})$ can push a system below the epidemic threshold.

Recent work has shown the practical value of graph-based simulation for infectious-disease diffusion, including vaccination scenarios for measles and modular platforms that combine compartmental models, network simulations, graph neural networks (GNNs), and explainable artificial intelligence (XAI) for decision support [6,7]. A complementary line of work on COVID-19 demonstrated that vaccination and containment can be formulated as topology-aware graph interventions: when individuals are represented as nodes and contacts as edges, removing or immunizing central nodes can reduce the spectral radius of the contact network more efficiently than random removal, thereby lowering epidemic potential [1]. This spectral perspective has since been further developed, connecting optimal vaccination to the NP-hard (non-deterministic polynomial-time hard) Spectral Radius Minimisation problem, a connection that recent work has extended to settings where the underlying contact network is not fully known and must be learned from infection data [8]. The integration of graph and reinforcement learning offers new possibilities for vaccination distribution in complex networks [6].

For zoonotic disease, recent hantavirus work illustrates the need for multi-scale models that connect molecular host response, protein–protein interaction networks, rodent-to-human spillover, and, for Andes virus, possible human-to-human transmission in confined travel settings [9]. The importance of such approaches is underscored by studies showing that ecological and biogeographic factors, modelled through host-ectoparasite networks, can successfully predict novel reservoir hosts and guide active surveillance to mitigate spillover risk [10]. A One Health framework for exploring zoonotic interactions has introduced the concept of “zoonotic web” to describe the complex relationships between zoonotic agents, their hosts, vectors, and environmental sources [10]. Multi-layer networks are increasingly used to model spillover dynamics: for example, a two-layer community network model has been constructed to analyse how community structure influences epidemic spreading in multilayer networks [10]. For Andes virus, a coupled susceptible-exposed-infectious-recovered-deceased (SEIRD) formulation that incorporates both rodent-to-human spillover and human-to-human transmission has been developed, showing that reducing human exposure to rodent excreta is more effective than rodent control alone [9].

Deep learning has increasingly been used for epidemic forecasting, and GNNs have emerged as a progressively popular tool in epidemic research [4]. A comprehensive review of GNNs in epidemic modeling introduced hierarchical taxonomies for both epidemic tasks and methodologies, categorizing existing work into Neural Models (e.g., Graph Convolutional Network (GCN), Graph Attention Network (GAT), Message Passing Neural Network (MPNN)) and Hybrid Models that combine GNNs with mechanistic compartmental equations [4]. GNNs are particularly suitable because they learn functions equivariant to graph structure and can integrate node features (e.g., age, vaccination status), edge features (e.g., contact frequency, mobility flows), and temporal signals [4,5]. Spatio-temporal graph models further combine graph convolution with recurrent or temporal convolutional components, enabling forecasting on dynamic networks where both node states and graph structure evolve over time [10]. Recent hybrid approaches have shown that integrating mechanistic compartmental models with spatiotemporal GNNs can successfully estimate epidemiological parameters that vary across space and time [11]. For example, surrogates leveraging mechanistic expert knowledge for pandemic response have achieved execution times of less than a second, a significant speedup compared to metapopulation approaches [11]. This suggests that GNN surrogates can be integrated into low-barrier web applications for near real-time decision support. Physics-informed graph neural networks have also been proposed to embed differential equation constraints directly into the learning process, improving both accuracy and generalizability [12,13].

Explainable AI (XAI) is essential in this context. Epidemic models are used to allocate scarce resources and justify interventions that affect communities, so prediction alone is insufficient. A systematic review on XAI-based epidemiological research stresses that while AI models can be highly accurate, their black-box nature hampers the trust needed for confident public-health decision-making [14]. Consequently, there is a growing effort to develop explainable GNNs that can reveal the subgraph structures, node features, and spatiotemporal patterns most responsible for model predictions, thereby enhancing clinical and public-health trust. In epidemic modelling, explanation should not only justify predictions but also indicate which interventions are plausible, proportional, and effective. Recent work has proposed counterfactual explanations for GNN-based epidemic forecasts, allowing policymakers to ask “what if” questions about vaccination campaigns or mobility restrictions [15,16].

At the same time, broader developments in biomedical artificial intelligence are moving toward foundation models and agentic systems that combine prediction, retrieval, planning, action, and reflection; these trends motivate epidemic systems that do not merely forecast cases but also explain evidence and recommend controllable interventions [17]. The intersection of GNNs with differential equations has produced innovative approaches for physics-informed learning and spatiotemporal modelling, with direct applications to epidemic spreading [12]. However, several challenges remain: real contact networks are incomplete, biased, dynamic, and privacy-sensitive; surveillance data are delayed and under-reported; GNNs may overfit historical policies and fail under behavioural, ecological, or viral changes. For this reason, future models must combine mechanistic priors, uncertainty quantification, causal reasoning, and transparent reporting standards.

The aim of this paper is to define a rigorous mathematical background for epidemic modelling on graphs and to formulate how GNNs and explainability can support public-health control. We focus on four questions:
* **(Q1)** How can epidemic processes be represented as stochastic or deterministic dynamics on networks?
* **(Q2)** Which graph quantities determine epidemic risk, persistence, and controllability?
* **(Q3)** How can GNNs learn transmission dynamics from heterogeneous temporal data?
* **(Q4)** How can explanations be formulated so that model outputs become actionable for public-health decisions?

This work makes the following original contributions:
1. A unified mathematical framework for deterministic and stochastic epidemic processes on temporal multilayer graphs, including spectral thresholds and controlled reproduction numbers.
2. A formal interpretation of public-health interventions (vaccination, isolation, mobility reduction) as graph transformations that lower the spectral radius, with an explicit optimal control formulation.
3. A hybrid neural–mechanistic architecture that combines GNNs with compartmental constraints, enabling data-driven spatio-temporal forecasting while preserving epidemiological interpretability.
4. A comprehensive explainability pipeline for epidemic decision support, including node-, edge-, feature-, counterfactual, and uncertainty-aware explanations, with robustness criteria.
5. Three detailed case studies (measles, COVID-19, hantavirus) that demonstrate how the proposed framework unifies direct transmission, zoonotic spillover, and multilayer molecular–ecological modelling.

Specifically, in Section 2 we introduce the graph-theoretic and stochastic foundations of epidemic processes on networks (spectral thresholds, compartmental dynamics, observation models) and then formulate optimal control of epidemics on graphs, with emphasis on spectral interventions and vaccination allocation. Next, we present a unified eight-step pipeline that integrates graph construction, uncertainty quantification, hybrid GNN learning, explainability, and validation, comparing our approach with existing modelling families (Section 3). Three detailed case studies, i.e., measles, COVID-19, and hantavirus, demonstrate the framework’s adaptability across direct transmission, zoonotic spillover, and molecular data (Section 4). Finally, we discuss ethical considerations, limitations, and future perspectives (Section 5), and conclude with a summary of contributions and a call for reproducible empirical evaluation (Section 6).

---

## 2. Mathematical Background

### 2.1. Graphs, Compartmental Dynamics, and Stochastic Processes

**Definition 1 (Epidemiological graph).** *An epidemiological graph is a tuple*
$$\mathcal{G} = (\mathcal{V}, \mathcal{E}, \mathbf{A}, \mathbf{X}),$$
*where $\mathcal{V} = \{1, \dots, n\}$ is a set of epidemiological units, $\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}$ is a set of possible transmission relations, $\mathbf{A} \in \mathbb{R}_+^{n \times n}$ is a weighted adjacency matrix with $A_{ij} > 0$ if unit $j$ can contribute infection pressure to unit $i$, and $\mathbf{X} \in \mathbb{R}^{n \times d}$ stores node covariates such as population size, age structure, vaccination coverage, incidence, climate, mobility, deprivation indicators, or surveillance intensity.*

For undirected contact networks $A_{ij} = A_{ji}$, while for mobility networks directionality matters. Important structural quantities include the degree $k_i = \sum_j A_{ij}$, the degree matrix $\mathbf{D} = \operatorname{diag}(k_1, \dots, k_n)$, the graph Laplacian $\mathbf{L} = \mathbf{D} - \mathbf{A}$, and the normalized adjacency
$$\mathbf{\widehat{A}} = \mathbf{\widetilde{D}}^{-1/2}(\mathbf{A} + \mathbf{I})\mathbf{\widetilde{D}}^{-1/2}, \quad \mathbf{\widetilde{D}}_{ii} = 1 + \sum_j A_{ij}.$$

The **spectral radius** $\rho(\mathbf{A}) = \max\{|\lambda| : \lambda \text{ eigenvalue of } \mathbf{A}\}$ plays a central role in network epidemic thresholds: it quantifies the maximum amplification of infection pressure by the graph structure.

**Definition 2 (Temporal and multilayer epidemic graph).** *A temporal multilayer epidemic graph is a sequence*
$$\mathcal{G}_{1:T} = \{(\mathcal{V}, \mathcal{E}^{[1]}(t), \dots, \mathcal{E}^{[M]}(t), \mathbf{A}^{[1]}(t), \dots, \mathbf{A}^{[M]}(t), \mathbf{X}(t))\}_{t=1}^T,$$
*where each layer $m$ represents a different transmission or information channel. A single effective adjacency is $\mathbf{A}_{\text{eff}}(t) = \sum_{m=1}^M \omega_m(t)\mathbf{A}^{[m]}(t)$ with $\omega_m(t) \ge 0$.*

Let $S_i(t), I_i(t), R_i(t)$ be susceptible, infectious, and removed fractions at node $i$. The continuous-time network SIR model is
$$\frac{dS_i}{dt} = -\beta S_i(t) \sum_j A_{ij} I_j(t), \tag{1}$$
$$\frac{dI_i}{dt} = \beta S_i(t) \sum_j A_{ij} I_j(t) - \gamma I_i(t), \tag{2}$$
$$\frac{dR_i}{dt} = \gamma I_i(t), \tag{3}$$
with $\beta > 0$ transmissibility and $\gamma > 0$ recovery rate. Linearising around the disease-free equilibrium gives the network reproduction number
$$\mathcal{R}_{\mathcal{G}} = \frac{\beta}{\gamma}\rho(\mathbf{A}), \quad \text{invasion if } \mathcal{R}_{\mathcal{G}} > 1. \tag{4}$$

**Numerical example.** Consider a graph with three nodes in a chain: $1 - 2 - 3$, with unweighted edges $A_{12} = A_{21} = A_{23} = A_{32} = 1$, all other entries $0$. The adjacency matrix is
$$\mathbf{A} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix},$$
whose eigenvalues are $0, \pm\sqrt{2}$. Hence $\rho(\mathbf{A}) = \sqrt{2} \approx 1.414$. If $\beta = 0.3$ per day and $\gamma = 0.2$ per day, then $\mathcal{R}_{\mathcal{G}} = (0.3/0.2) \times 1.414 = 2.121 > 1$, so invasion is possible. If we remove node 2 (the central hub) – e.g., by vaccinating that individual – the graph becomes two isolated nodes, $\rho(\mathbf{A}) = 0$, and $\mathcal{R}_{\mathcal{G}} = 0$. This illustrates how targeted removal of a single node can completely stop an outbreak.

For individual-level models, let $Y_i(t) \in \{S, E, I, R\}$ be the state of node $i$. The infection hazard is
$$\lambda_i(t) = \beta \sum_j A_{ij}(t) \mathbf{1}\{Y_j(t) = I\} + \lambda_i^{\text{env}}(t),$$
and $Y(t)$ is a continuous-time Markov chain. A discrete-time approximation is
$$\Pr(Y_i(t+1) = I \mid Y_i(t) = S) = 1 - e^{-\Delta t \lambda_i(t)}, \quad \Pr(Y_i(t+1) = R \mid Y_i(t) = I) = 1 - e^{-\Delta t \gamma}.$$

The exponential form arises from assuming that, within a short interval $\Delta t$, the hazard $\lambda_i(t)$ is constant; thus the waiting time until the next event follows an exponential distribution. The probability of at least one event in $[t, t + \Delta t]$ is $1 - \exp(-\lambda_i(t)\Delta t)$, which for small $\Delta t$ approximates $\lambda_i(t)\Delta t$.

Finally, observed data $\mathbf{y}(t)$ are noisy, delayed measurements of the latent state $\mathbf{x}(t)$: $\mathbf{y}(t) \sim p_\eta(\mathbf{y}(t) \mid \mathbf{x}(t), \mathbf{q}(t))$.

---

### 2.2. Optimal Control and Intervention on Graphs

Let $u(t) \in \mathcal{U}$ represent interventions (vaccination, mobility restrictions, school closures, testing, treatment, environmental mitigation, communication campaigns). A generic control problem is
$$\min_{u(0),\dots,u(T)} \mathbb{E}\left[ \sum_{t=0}^T \left( \mathbf{C}_I^\top \mathbf{i}(t) + C_u(u(t)) \right) \right] \quad \text{subject to epidemic dynamics on } \mathcal{G}(t, u).$$

Here $\mathbf{C}_I$ weights disease burden (e.g., hospitalisations, deaths, quality-adjusted life years) and $C_u$ captures the cost of intervention. Realistic examples of $C_u(u(t))$ include:
* **Vaccination:** $C_u = \sum_i c_i^{\text{vacc}} v_i(t)$, where $c_i^{\text{vacc}}$ is the cost per dose (procurement, distribution, administration) and $v_i(t)$ is the number of vaccinated individuals at node $i$.
* **Lockdown or mobility restriction:** $C_u = c_{\text{GDP}} \cdot (1 - m(t))$, where $m(t) \in [0, 1]$ is the mobility reduction factor and $c_{\text{GDP}}$ is the estimated daily economic loss.
* **Isolation or quarantine:** $C_u = c_{\text{iso}} \cdot \#\{\text{isolated individuals}\}$, accounting for lost productivity and social support.
* **Communication campaigns:** fixed budget allocation over time.

Key strategies include degree-based targeting, spectral targeting (reducing $\rho(\mathbf{A})$), community-based control, and adaptive control. For vaccination, let $v_i \in [0, 1]$ denote coverage (fraction of node $i$ that is vaccinated) and $\epsilon \in [0, 1]$ vaccine efficacy. The next-generation matrix is
$$\mathbf{K}(v) = \frac{\beta}{\gamma} \operatorname{diag}(1 - \epsilon v_1, \dots, 1 - \epsilon v_n) \mathbf{A},$$
with controlled reproduction number $\mathcal{R}_{\mathcal{G}}(v) = \rho(\mathbf{K}(v))$. An optimal vaccination problem is
$$\min_{v \in [0,1]^n} \rho(\mathbf{K}(v)) \quad \text{subject to } \sum_i c_i v_i \le B,$$
where $B$ is available budget and $c_i$ is cost or population size of node $i$. This formulation is a special case of the **budgeted influence maximization** problem in networks, where the goal is to select a set of nodes (subject to budget) that minimises the spectral radius, which is known to be NP-hard but admits greedy approximations.

**Analytically solvable case: regular graph.** If the contact network is $d$-regular (every node has the same degree $d$), then the all-ones vector $\mathbf{1}$ is an eigenvector of $\mathbf{A}$ with eigenvalue $d$. The spectral radius is $\rho(\mathbf{A}) = d$. After homogeneous vaccination coverage $v$ (same for all nodes), the next-generation matrix becomes $\mathbf{K}(v) = (\beta/\gamma)(1 - \epsilon v)\mathbf{A}$, whose spectral radius is $(\beta/\gamma)(1 - \epsilon v)d$. The constraint $\mathcal{R}_{\mathcal{G}}(v) \le 1$ gives $v \ge (1 - \gamma/(\beta d))/\epsilon$. Thus the minimal budget required is $B_{\text{min}} = n c v$ (with $c$ the per-node cost). This closed-form solution provides a benchmark for evaluating greedy or spectral heuristics on heterogeneous graphs.

---

### 2.3. Graph Neural Networks for Epidemic Modelling

Let $\mathbf{H}^{(0)}(t) = \mathbf{X}(t)$. A message-passing layer is
$$\mathbf{m}_i^{(\ell)}(t) = \sum_{j \in \mathcal{N}(i)} \phi_\ell\left(\mathbf{h}_i^{(\ell)}(t), \mathbf{h}_j^{(\ell)}(t), A_{ij}(t), \mathbf{e}_{ij}(t)\right), \quad \mathbf{h}_i^{(\ell+1)}(t) = \psi_\ell\left(\mathbf{h}_i^{(\ell)}(t), \mathbf{m}_i^{(\ell)}(t)\right).$$

A simple graph convolutional layer is $\mathbf{H}^{(\ell+1)}(t) = \sigma(\mathbf{\widehat{A}}(t)\mathbf{H}^{(\ell)}(t)\mathbf{W}^{(\ell)})$. However, more expressive architectures can be used. For instance, a **Graph Attention Network (GAT)** layer computes attention coefficients $\alpha_{ij}$ over neighbours, allowing the model to weigh edges differently:
$$\mathbf{h}_i^{(\ell+1)} = \sigma\left( \sum_{j \in \mathcal{N}(i)} \alpha_{ij} \mathbf{W}^{(\ell)} \mathbf{h}_j^{(\ell)} \right), \quad \alpha_{ij} = \frac{\exp\left(\operatorname{LeakyReLU}\left(\mathbf{a}^\top [\mathbf{W}\mathbf{h}_i \parallel \mathbf{W}\mathbf{h}_j]\right)\right)}{\sum_{k \in \mathcal{N}(i)} \exp(\dots)}.$$

Temporal dynamics are added via recurrent or convolutional modules:
$$\mathbf{Z}(t+1) = F_\theta(\mathbf{Z}(t), \mathbf{X}(t), \mathbf{A}(t), u(t)), \quad \widehat{\mathbf{y}}(t+1) = G_\theta(\mathbf{Z}(t+1)).$$

**Attention over time.** To capture variable importance of past observations, one can employ **temporal attention** mechanisms. For example, a Transformer-style self-attention over time steps allows the model to focus on critical past days (e.g., peaks or policy change dates). The hidden state at time $t$ can be updated as
$$\mathbf{Z}(t) = \sum_{\tau=1}^t \beta_{t,\tau} \mathbf{\widetilde{Z}}(\tau), \quad \beta_{t,\tau} = \frac{\exp(\operatorname{score}(\mathbf{\widetilde{Z}}(t), \mathbf{\widetilde{Z}}(\tau)))}{\sum_{k=1}^t \exp(\operatorname{score}(\mathbf{\widetilde{Z}}(t), \mathbf{\widetilde{Z}}(k)))},$$
where $\mathbf{\widetilde{Z}}(\tau)$ is a temporally encoded representation.

**Handling dynamic graphs.** Real contact networks change over time (e.g., daily rhythms, school closures, behavioural adaptation). Two main strategies exist:
1. **Time-varying adjacency matrices:** $\mathbf{A}(t)$ is supplied at each time step. The GNN processes each snapshot independently (or via a recurrent connector). This requires knowledge of $\mathbf{A}(t)$ from data (e.g., proximity sensors, mobility traces).
2. **Learnable graph evolution:** a separate recurrent network (e.g., LSTM) predicts $\mathbf{A}(t+1)$ from $\mathbf{A}(t)$ and node features, enabling forecasting even when future contacts are unknown. This can be written as
$$\mathbf{A}(t+1) = \operatorname{softmax}(\operatorname{MLP}_\phi(\mathbf{Z}(t))) \quad \text{or} \quad \mathbf{A}(t+1) = \operatorname{LSTM}_\psi(\mathbf{A}(t), \mathbf{X}(t)).$$

Hybrid neural–mechanistic models preserve compartmental structure, e.g.
$$\mathbf{i}(t+1) = \mathbf{i}(t) + \Delta t \left[ \beta_\theta(t) \mathbf{s}(t) \odot \mathbf{A}_\theta(t)\mathbf{i}(t) - \gamma_\theta(t)\mathbf{i}(t) \right],$$
where $\mathbf{A}_\theta(t)$ may be a learned adjacency modifier.

**Training and scenario learning.** Given a collection of outbreaks $\mathcal{D} = \{(\mathcal{G}_{1:T}^{(r)}, \mathbf{X}_{1:T}^{(r)}, u_{1:T}^{(r)}, \mathbf{y}_{1:T}^{(r)})\}_{r=1}^R$, a forecasting loss is
$$\mathcal{L}_{\text{pred}}(\theta) = \sum_{r=1}^R \sum_{t=1}^{T-H} \ell(\mathbf{\widehat{y}}_{t+1:t+H}^{(r)}, \mathbf{y}_{t+1:t+H}^{(r)}),$$
with possible mechanistic regularisation. For counterfactual questions, the model estimates
$$p_\theta(\mathbf{y}_{t+1:t+H} \mid \mathcal{G}_{1:t}, \mathbf{X}_{1:t}, u_{1:t+H}).$$

---

### 2.4. Explainability, Uncertainty, and Robustness

**Definition 3 (Graph explanation).** *Given a trained predictor $f_\theta(\mathcal{G}, \mathbf{X})$, an explanation for output $f_\theta$ is a reduced object $\mathcal{E}_x = (\mathcal{V}_x, \mathcal{E}_x, \mathbf{X}_x)$ that preserves the decision-relevant quantity while being interpretable.*

Important explanation targets include node importance, edge importance, feature importance, counterfactuals, and uncertainty. We define **fidelity** as a measure of how well the explanation reproduces the original prediction. Formally, let $f_\theta(\mathcal{G}, \mathbf{X})[c]$ be the predicted probability for a target class $c$ (e.g., outbreak above threshold). Using only the subgraph $\mathcal{E}_x$ (with masked nodes/edges/features), the fidelity is
$$\operatorname{Fid}(\mathcal{E}_x; \mathcal{G}') = 1 - |f_\theta(\mathcal{G}, \mathbf{X})[c] - f_\theta(\mathcal{E}_x, \mathbf{X}_x)[c]|,$$
or alternatively the probability that the explanation alone yields the same decision. Higher fidelity means the explanation captures the essential information.

A counterfactual intervention can be formulated as
$$\min_{\Delta\mathbf{A}, \Delta\mathbf{X}, \Delta u} \|\Delta\mathbf{A}\|_0 + \lambda_X \|\Delta\mathbf{X}\|_0 + \lambda_u C_u(\Delta u) \quad \text{s.t.} \quad f_\theta(\mathcal{G}+\Delta\mathcal{G}, \mathbf{X}+\Delta\mathbf{X}, u+\Delta u) \le \tau.$$

**Epidemiologically-aware explainers.** General-purpose explainers like GNNExplainer can be adapted to respect epidemic constraints. For example, an edge explanation claiming transmission from $j$ to $i$ at time $t$ must be temporally consistent: if $Y_j(t')$ is infectious and $Y_i(t'')$ becomes infected with $t'' > t'$, the edge must exist at the relevant time window. Conversely, an edge that would require infection to travel backwards in time (i.e., $j$ infectious after $i$ becomes infected) is invalid. Such constraints can be encoded as penalty terms in the explanation objective:
$$\mathcal{L}_{\text{exp}} = \mathcal{L}_{\text{fidelity}} + \lambda_{\text{temp}} \sum_{(i,j)\in \mathcal{E}_x} \mathbb{1}[\text{time violation}].$$

**Robust explanations.** Let $\mathcal{P}(\mathcal{G})$ be a distribution over plausible graphs (from step 3 of the pipeline). A robust explanation maximises expected fidelity while controlling variability:
$$\max_{\mathcal{E}_x} \mathbb{E}_{\mathcal{G}' \sim \mathcal{P}(\mathcal{G})}[\operatorname{Fid}(\mathcal{E}_x; \mathcal{G}')] - \lambda \operatorname{Var}_{\mathcal{G}' \sim \mathcal{P}(\mathcal{G})}[\operatorname{Fid}(\mathcal{E}_x; \mathcal{G}')].$$

This prevents explanations that are valid only under a single arbitrary graph reconstruction.

Additionally, for node importance, one can compute *uncertainty intervals* by applying the explanation method to each graph in the ensemble and reporting the mean importance and standard deviation. This provides decision-makers with a measure of confidence.

---

## 3. Integrated Pipeline for Epidemic Decision Support: Comparison with Literature and Practical Implementation

The current landscape of epidemic modelling is characterised by a fragmentation of methods, each with complementary strengths and weaknesses. At one end, classical compartmental ordinary differential equation (ODE) models [18,19] provide interpretable, analytically tractable frameworks for estimating reproduction numbers and intervention effects under the assumption of homogeneous mixing. However, they cannot capture contact heterogeneity, superspreading events, or spatial clustering, which are critical for accurate outbreak prediction [20]. Network SIR/SEIR models [21,22] overcome the homogeneous mixing assumption by explicitly representing contacts as graph edges, and they offer spectral thresholds linking the largest eigenvalue of the adjacency matrix to epidemic invasion [1,20]. Yet these models require a fully known contact network and do not learn from data beyond estimating a few scalar parameters. At the other end, pure GNN [23–25] are highly flexible: they learn from rich, heterogeneous data (demographics, mobility, genomics) and can forecast complex spatio-temporal patterns [4,11]. Nevertheless, they often operate as black boxes, may violate basic epidemiological constraints (e.g., non-negative counts, conservation of mass), and lack built-in explainability. Recent hybrid models [11–13] combine GNNs with mechanistic priors, achieving faster execution than full mechanistic simulations, but they typically assume a fixed graph and provide limited uncertainty quantification or counterfactual explanations.

Table 1 summarises the pros and cons of these four families, referencing representative works from the literature. Our proposed framework directly addresses the identified limitations in four specific ways: (i) explicit graph uncertainty quantification (step 3) using bootstrap, imputation, or Bayesian methods [16]; (ii) a hybrid neural–mechanistic architecture (step 5) that enforces compartmental conservation and positivity [1,6]; (iii) a full explainability module (step 6) including node, edge, feature, counterfactual, and uncertainty-aware explanations [15,26,27]; and (iv) robustness evaluation across graph perturbations (step 8) [2,10].

##### Table 1. Comparison of pros and cons of epidemic modelling approaches as reported in the literature.
| Model family | Pros | Cons | Key refs |
| :--- | :--- | :--- | :--- |
| **Compartmental ODE** | Interpretable, fast, analytic thresholds | Homogeneous mixing, no network heterogeneity | [18,19] |
| **Network SIR/SEIR** | Explicit contact graph, spectral thresholds | Fixed graph, limited learning, no uncertainty | [20–22] |
| **Pure GNN** | Learns from rich data, handles heterogeneity | Black box, may violate mechanistic constraints | [4,23,24] |
| **Hybrid (existing)** | Faster than mechanistic, some constraints | Fixed graph, limited explainability, no uncertainty | [11–13] |
| **Our framework** | Graph uncertainty, hybrid constraints, full XAI, counterfactual control | Higher computational cost, more data required | [1,6,26] |

Based on this analysis, we present an eight-step pipeline (Figure 1) that operationalises the strengths of our framework while systematically addressing the gaps of previous approaches.

1. **Data integration:** collect and harmonize heterogeneous data sources: incidence (case counts, hospital admissions, deaths), vaccination coverage, demographic data (population density, age structure), mobility data (mobile phone aggregates, travel surveys), genomic sequences (viral lineages), environmental data (climate, land use, rodent abundance), and intervention records (policy dates, stringency indices). Data should be aligned to a common spatio-temporal resolution (e.g., daily, weekly; administrative units or grid cells).
2. **Graph construction:** define nodes (individuals, households, schools, municipalities, ecological patches) and edges (contacts, mobility flows, shared environment, phylogenetic similarity). Specify edge weights (e.g., contact frequency, traffic volume), temporal resolution (static, daily, or time-varying), and initial uncertainty over missing links (e.g., based on sampling fraction or imputation models).
3. **Graph uncertainty quantification:** real-world contact and mobility networks are never completely observed. This step quantifies and propagates uncertainty arising from:
   * *Missing edges:* use bootstrap resampling of observed contacts (e.g., re-sampling with replacement from diary data) or model-based imputation (e.g., logistic regression predicting edge presence from node attributes).
   * *Noisy edge weights:* assume a distribution (e.g., log-normal) around each weight and draw multiple graph realizations.
   * *Temporal incompleteness:* generate alternative contact timelines by jittering event times or using probabilistic generative models.
   * *Privacy-preserving aggregation:* treat aggregated flows (e.g., commute matrices) as uncertain via Bayesian smoothing.  
   The output is a set of plausible graphs $\{\mathcal{G}^{(1)}, \dots, \mathcal{G}^{(K)}\}$ or a distribution $\mathcal{P}(\mathcal{G})$ that will be used in subsequent steps for robust learning and explanation.
4. **Mechanistic baseline:** fit a network SIR/SEIR or reservoir model on the nominal graph and on the uncertainty ensemble. Estimate transmission rate $\beta$, recovery rate $\gamma$, and the network reproduction number $\mathcal{R}_{\mathcal{G}}$. Compare results across graph realizations to assess how uncertainty affects threshold estimates.
5. **GNN learning:** train spatio-temporal GNNs or hybrid neural–mechanistic models for forecasting and scenario simulation. Use the ensemble of graphs from step 3 to train models that are robust to structural uncertainty (e.g., by aggregating predictions or using distributionally robust optimization). Incorporate mechanistic constraints (positivity, conservation of mass) as soft or hard penalties.
6. **Explainability:** compute node, edge, feature, and counterfactual explanations for high-risk predictions. Evaluate explanation stability across the graph ensemble (e.g., fidelity variance). Provide uncertainty-aware explanations (e.g., confidence intervals for node importance).
7. **Control evaluation:** simulate interventions (vaccination allocation, isolation, mobility reduction, environmental mitigation, communication campaigns) under cost constraints. Use the ensemble of graphs to obtain robust estimates of intervention effectiveness (e.g., reduction in epidemic size or peak incidence) and to identify policies that perform well across plausible graph realizations.
8. **Validation:** assess calibration of probabilistic forecasts, out-of-sample accuracy (temporally and spatially), robustness to graph perturbations (e.g., by comparing predictions on the nominal graph vs. the uncertainty ensemble), and reproducibility (full code and data, random seeds).

```
 +-----------------------------------------------------------------------+
 | (1) DATA INTEGRATION                                                  |
 |     Integrate heterogeneous data sources                              |
 |     (cases, mobility, demographics, testing, vaccination, etc.)       |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (2) GRAPH CONSTRUCTION                                                |
 |     Construct a spatio-temporal contact network                       |
 |     (nodes: regions/locations, edges: interactions/flows)             |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (3) GRAPH UNCERTAINTY QUANTIFICATION                                  |
 |     Bootstrap resampling  /  Missing-edge imputation                  |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (4) MECHANISTIC BASELINE                                              |
 |     Network SIR/SEIR model on the constructed graph to capture        |
 |     disease transmission dynamics                                     |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (5) GNN LEARNING                                                      |
 |     Spatio-temporal graph neural network for forecasting and          |
 |     representation learning                                           |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (6) EXPLAINABILITY                                                    |
 |     Provide node-, edge-, and counterfactual explanations to          |
 |     understand model behavior and key drivers                         |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (7) CONTROL EVALUATION                                                |
 |     Evaluate vaccination strategies and interventions to reduce       |
 |     transmission and burden                                           |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 | (8) VALIDATION                                                        |
 |     Assess calibration (fit to data) and robustness (uncertainty,     |
 |     sensitivity, out-of-sample)                                       |
 +-----------------------------------------------------------------------+
```

> **Figure 1.** Schematic overview of the proposed eight-step pipeline for graph-based epidemic decision support. Steps are colour-coded by phase: data (blue), modelling (green), uncertainty (orange), learning (red), explanation (purple), and validation (grey).

---

## 4. Case Studies

### 4.1. Measles: Vaccination, Clustering, and Outbreak Prevention

Measles is one of the most transmissible human viruses ($\mathcal{R}_0$ typically 12–18) [28]. Small reductions in vaccination coverage can create susceptible clusters even when average coverage appears high. In a graph formulation, nodes may represent individuals, schools, municipalities, or age groups; edges represent contact, co-location, or mobility.

Contact networks for measles can be constructed from:
* **School enrolment and class rosters:** edges between students in the same class or school, weighted by contact duration. Vaccination coverage data at school level (e.g., from immunisation registries) allow identifying under-vaccinated clusters [28].
* **Census mobility data:** commuting flows between municipalities define edges for spatial spread. The adjacency matrix $\mathbf{A}$ can be built as $A_{ij} = \text{number of commuters from } i \text{ to } j$ (directed) or symmetrised.
* **Household and social contact diaries:** surveys (e.g., POLYMOD) provide age-stratified contact matrices that can be mapped onto network nodes.

The central mathematical object is the controlled next-generation matrix $\mathbf{K}(v)$. If vaccination is homogeneous, the classical herd-immunity condition is approximately $v > 1 - 1/\mathcal{R}_0$, adjusted for vaccine efficacy $\epsilon$. On a network, the relevant condition is spectral:
$$\rho\left(\frac{\beta}{\gamma} \operatorname{diag}(1 - \epsilon v_i) \mathbf{A}\right) < 1.$$

Thus, two populations with the same average vaccination level can have different outbreak risks if one contains clustered under-vaccinated communities. A measles case study should compare random vaccination decline with geographically or socially clustered decline, quantify final outbreak size, and identify nodes or communities where marginal vaccination produces the largest decrease in $\mathcal{R}_{\mathcal{G}}(v)$. This aligns with graph-based simulation studies of vaccination effects on measles spread [28].

---

### 4.2. COVID-19: Topology-Aware Vaccination and Contact-Network Control

COVID-19 provides a natural case study for topology-aware epidemic control because transmission depends strongly on heterogeneous human contacts, mobility, occupation, household structure, and behavioural adaptation [29].

Following the topology-aware vaccination perspective, a population is represented by a contact graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$, where each node is an individual and each edge a potential transmission contact [1]. The early growth condition is summarised by the spectral criterion
$$\frac{\beta}{\delta} \le \frac{1}{\lambda_{\max}(\mathbf{A})},$$
where $\beta$ is the infection rate, $\delta$ the recovery rate, and $\lambda_{\max}(\mathbf{A})$ the largest eigenvalue of the adjacency matrix. Interventions that remove, immunise, isolate, or protect nodes change $\mathbf{A}$ and thus $\lambda_{\max}$.

Figure 2 illustrates how different vaccination strategies reduce $\lambda_{\max}$. The left panel shows a scale-free network with colour-coded node centrality. The middle panel depicts random vaccination (many nodes partially vaccinated, small decrease in $\lambda_{\max}$). The right panel shows topology-aware vaccination (targeting the highest-eigenvector-centrality nodes), yielding a much larger reduction in $\lambda_{\max}$ with the same number of doses.

```
       [ Original scale-free network ]              [ Random vaccination (small Δλ_max) ]         [ Topology-aware vaccination (large Δλ_max) ]
             (eigenvector centrality)
                    o                                              o                                              o
                   / \                                            / \                                            / \
                  o---O---o                                      x---O---o                                      o---X---o
                 /|  /|\  |\                                    /|  /|\  |\                                    /|  /|\  |\
                o-o-O-O-O-o-o                                  o-x-O-x-O-o-x                                  o-o-O-O-O-o-o
                 \|  \|/  |/                                    \|  \|/  |/                                    \|  \|/  |/
                  o---O---o                                      o---x---o                                      o---X---o
                    \ /                                            \ /                                            \ /
                     o                                              o                                              o

            Low <---------> High                         λ_max (before) = 2.35                          λ_max (before) = 2.35
            Eigenvector centrality                        λ_max (after)  = 2.19                          λ_max (after)  = 0.62
                                                          Δλ_max         = 0.16 (small)                 Δλ_max         = 1.73 (large)
```

> **Figure 2.** Conceptual comparison of random vs. topology-aware vaccination on a scale-free network. Topology-aware targeting of high-centrality nodes reduces $\lambda_{\max}$ more effectively for the same number of vaccine doses.

A COVID-19 case study should compare at least four intervention policies: random, age-based, degree-/betweenness-based, and spectral prioritisation. The study by Petrizzelli et al. evaluates synthetic networks and real contact data (Infectious SocioPatterns Dublin), showing that removing topologically central nodes reduces $\lambda_{\max}$ more effectively than random removal [1]. Within the present GNN framework, this case study can be extended to dynamic contacts, learning intervention impact, and explainable policy design.

---

### 4.3. Hantavirus: From Host Transcriptomics to Rodent–Human and Human–Human Transmission Networks

Hantavirus infection requires a multi-scale representation that goes beyond direct respiratory transmission. Its epidemiology depends on the interplay among rodent reservoirs, environmental contamination, ecological drivers, human exposure, viral lineage diversity, and, in the case of Andes orthohantavirus (ANDV), possible person-to-person transmission. The following paragraphs describe three complementary layers (molecular, ecological-rodent, and human transmission) and how they can be encoded in a multilayer graph. Table 2 summarises the data sources and typical node/edge attributes for each layer, providing a concrete roadmap for constructing the graph from real-world data.

**Molecular layer: host response networks.** This layer is derived from transcriptomic data of infected endothelial cells. In the hantavirus study, HTNV-infected HUVECs showed marked upregulation of interferon-driven genes such as *CXCL10*, *STAT1*, and *DDX58* [9]. A protein–protein interaction (PPI) network of 176 nodes and 3,210 edges was constructed, with hubs including *ISG15* and *IRF1*. These molecular data can be used as node features (e.g., differential expression log-fold change, p-value) or as priors in a molecular GNN to identify host-response signatures associated with severe disease, antiviral defence, or candidate therapeutic targets.

**Ecological–rodent layer: spillover risk.** Rodent population dynamics and environmental contamination are modelled over spatial patches (e.g., grid cells, watersheds, or administrative units). Node attributes include rodent abundance indices (from trapping or ecological niche models), climatic variables (precipitation, NDVI), land use, and housing quality. Edges represent rodent dispersal pathways, such as hydrological connectivity (rivers, streams) or forest corridors. The environmental contamination level $E_i(t)$ evolves according to rodent shedding rates and decay. This layer captures the extrinsic drivers of spillover risk.

**Human transmission layer: spillover and person-to-person spread.** Humans can be infected via two routes: direct or indirect contact with rodent excreta (spillover) and, for ANDV, human-to-human contact. The hazard rates for a susceptible human in patch $i$ are:
$$\lambda_i^{RH}(t) = \beta_{RH} S_i^H(t) \left( E_i(t) + \sum_j M_{ij}^R I_j^R(t) \right), \tag{5}$$
$$\lambda_i^{HH}(t) = \beta_{HH} S_i^H(t) \sum_j A_{ij}^H(t) I_j^H(t), \tag{6}$$
$$\lambda_i^H(t) = \lambda_i^{RH}(t) + \lambda_i^{HH}(t), \tag{7}$$
where $I_j^R(t)$ are infectious rodents, $M^{R}$ is the rodent/environmental coupling matrix (dispersal or hydrological connectivity), and $A^H(t)$ is the human contact or travel matrix (which may be time-varying). This formulation explicitly distinguishes dead-end spillover from sustained human-to-human chains, which is critical for ANDV.

Table 2 maps each layer to its data sources and example attributes, providing a practical guide for constructing the multilayer graph $\mathcal{G}^H(t)$. For instance, the molecular layer relies on RNA-seq and PPI databases; the rodent layer uses trapping data and climate rasters; the environmental layer uses land use maps; the human contact layer uses contact diaries or census mobility traces; and the travel layer uses air/road traffic data.

##### Table 2. Layers of the hantavirus multilayer graph and corresponding data sources.
| Layer | Data sources | Example node/edge attributes |
| :--- | :--- | :--- |
| **Molecular ($\mathcal{G}^{\text{mol}}$)** | RNA-seq, proteomics, PPI databases | Differential expression ($\log \text{FC}$, p-value), centrality scores |
| **Rodent ($\mathcal{G}^{\text{rodent}}$)** | Trapping data, ecological niche models, climate | Rodent abundance, NDVI, precipitation, dispersal kernels |
| **Environmental ($\mathcal{G}^{\text{env}}$)** | Land use maps, soil sampling | Contamination level, habitat type, surface water |
| **Human contact ($\mathcal{G}^{\text{human}}$)** | Contact diaries, census, mobility traces | Household size, workplace contacts, travel flows |
| **Travel ($\mathcal{G}^{\text{travel}}$)** | Air/road traffic, mobile phone data | Daily passenger counts, route connectivity |

A comprehensive experiment should compare three scenarios: (i) classical rodent-to-human spillover (no human-to-human transmission), (ii) spatially structured spillover shaped by environmental and ecological forcing, and (iii) ANDV-specific spillover combined with human-to-human transmission. The original hantavirus study reported that reducing human exposure to rodent excreta (e.g., through hygiene education or improved housing) is more effective than rodent control alone, and that isolated rodent-control interventions may generate a dilution-like paradox under certain parameter regimes [9]. Our graph-based extension will assess whether these conclusions remain robust when spatial heterogeneity, travel-mediated dispersal, strain-level genomic variation, and uncertain contact networks are explicitly incorporated.

---

### 4.4. Cross-Case Integration: Toward General Epidemic Graph Intelligence

The three case studies, i.e., measles, COVID-19, and hantavirus, represent complementary epidemiological regimes. Measles exemplifies a highly transmissible, vaccine-preventable disease where clustering of under-vaccinated individuals drives outbreaks despite high average coverage. COVID-19 illustrates rapid, policy-driven dynamics on dense human contact networks, with time-varying interventions and asymptomatic spread. Hantavirus requires a multi-scale framework that integrates molecular host response, rodent reservoirs, environmental contamination, and occasional human-to-human transmission. A unified graph-learning framework must therefore accommodate direct transmission, environment-mediated spillover, and molecular data, while allowing pathogen-specific adaptations in graph layers, transition hazards, intervention variables, and explanation targets.

A comparison of intervention variables across the three pathogens (Table 3) reveals several patterns. Vaccination is central for measles and COVID-19 but plays no role for hantavirus (no vaccine currently available for ANDV); instead, exposure reduction (hygiene, rodent control) is the primary control. Isolation and quarantine are relevant for all three, but their implementation differs: for measles it is typically post-exposure prophylaxis of contacts; for COVID-19 it is symptom-based isolation and contact tracing; for hantavirus it applies only to ANDV cases where human-to-human transmission occurs. Mobility reduction (school closures, lockdowns, travel bans) is effective for measles (during outbreaks) and COVID-19, but not applicable to hantavirus, whose spillover is mainly local and environment-driven. Environmental mitigation, negligible for measles and COVID-19 (aside from ventilation), is crucial for hantavirus (rodent exclusion, decontamination). Finally, measurability differs: measles relies on vaccination registries and serosurveys; COVID-19 on case reports, mobility data, and policy indices; hantavirus on rodent abundance and environmental sampling. This comparison underscores that a flexible framework must support different intervention types and data availabilities.

##### Table 3. Comparison of intervention variables for the three case studies.
| Intervention | Measles | COVID-19 | Hantavirus |
| :--- | :--- | :--- | :--- |
| **Primary control** | Vaccination (closing coverage gaps) | Vaccination + NPIs (mask, distancing) | Exposure reduction (hygiene, rodent control) |
| **Isolation/quarantine** | Post-exposure prophylaxis for contacts | Symptom-based isolation, contact tracing | Isolation of ANDV cases (human-to-human) |
| **Mobility reduction** | School closures during outbreaks | Lockdowns, travel bans | Not applicable (spillover mainly local) |
| **Environmental mitigation** | None | Ventilation, surface disinfection | Rodent exclusion, environmental decontamination |
| **Communication** | Campaigns to increase coverage | Risk communication, vaccine promotion | Awareness of rodent excreta risks |
| **Measurability** | Vaccination registries, serosurveys | Case reports, mobility data, policy indices | Rodent abundance, environmental sampling |

Table 4 maps the proposed graph-learning framework onto the COVID-19 and hantavirus case studies (measles follows a similar logic to COVID-19 but with a focus on vaccination gaps and school networks). While the core components, i.e., primary graph, key control, mathematical target, learning task, and explanation target, remain conceptually the same, their instantiation changes drastically. For COVID-19, the primary graph is a human contact and mobility network, the mathematical target is reduction of $\lambda_{\max}(\mathbf{A})$ and epidemic size, and explanations target central nodes, bridge edges, and high-risk communities. For hantavirus, the primary graph becomes a multilayer structure (molecular, rodent, environmental, human, travel layers), the mathematical target shifts to reduction of spillover events and human transmission chains, and explanations target host-response hubs, ecological patches, and exposure routes. This adaptability is achieved by keeping the same algorithmic backbone (spectral thresholds, GNNs, hybrid constraints, XAI) while allowing pathogen-specific layers, transition hazards, and intervention variables to be plugged in.

##### Table 4. Mapping of the proposed graph-learning framework onto the COVID-19 and hantavirus case studies.
| Component | COVID-19 case study | Hantavirus case study |
| :--- | :--- | :--- |
| **Primary graph** | Human contact and mobility network | Molecular, rodent, environmental, human, travel layers |
| **Key control** | Vaccination, isolation, contact reduction | Exposure reduction, rodent/environmental management, isolation for ANDV |
| **Mathematical target** | Reduction of $\lambda_{\max}(\mathbf{A})$ and epidemic size | Reduction of spillover events and human transmission chains |
| **Learning task** | Forecasting incidence under alternative vaccination policies | Integrating molecular host response with spatial spillover risk |
| **Explanation target** | Central nodes, bridge edges, high-risk communities | Host-response hubs, ecological patches, exposure routes |

The unified framework is not limited to these three diseases. It can be extended to other zoonotic (e.g., Ebola, Nipah), vector-borne (e.g., Lyme disease, West Nile virus, dengue), and respiratory pathogens (e.g., influenza, RSV) by adding or removing layers and adjusting transition hazards accordingly. The modular design, where graph construction, uncertainty quantification, hybrid GNN learning, explainability, and control evaluation are separate but integrable steps, ensures that the pipeline remains operational even when data are sparse or partially observed. Ultimately, this work lays the foundation for a next-generation epidemic decision system that is predictive, interpretable, robust, and adaptable across a wide spectrum of infectious diseases.

---

### 4.5. Experimental Design

To convert the framework into an empirical study, experiments should be organized around three levels of evidence, progressively increasing in realism and decreasing in ground-truth control.

**Level 1: Synthetic benchmarks.** Uses completely synthetic graphs to allow full control over ground truth. One may generate Erdős–Rényi, scale-free, small-world, stochastic block, and metapopulation networks, then simulate SIR/SEIR dynamics with known parameters. The objectives are to evaluate whether models recover correct high-risk nodes, epidemic thresholds, and intervention effects. Synthetic experiments should vary graph density, clustering, assortativity, reporting noise, and missing-edge rates. Because the true transmission pathways and infection times are known, we can compute explanation accuracy: the fraction of top-$k$ predicted influential nodes or edges that match the ground truth (e.g., nodes that actually caused the largest number of secondary cases). Completeness can be measured as the proportion of the variance in the model’s prediction that is explained by the subgraph (or node set) identified by the explainer, for instance using the coefficient of determination $R^2$ between the original prediction and the prediction using only the explanatory subgraph. Stability across different random seeds or graph realizations can be assessed via the variance of explanation rankings, e.g., using Kendall’s $\tau$ rank correlation across multiple runs.

**Level 2: Semi-synthetic public-health scenarios.** Combines real data with simulated epidemic dynamics. This design is useful when true counterfactual outcomes are unavailable. For COVID-19, a semi-synthetic benchmark can use empirical contact networks such as the SocioPatterns Dublin data and simulate SIR/SEIR diffusion under random, age-based, centrality-based, and spectral vaccination policies. For hantavirus, one can combine public transcriptomic signatures, protein-protein interaction (PPI) network features, rodent/ecological covariates, and spatial exposure maps with a calibrated SEIRD spillover model. The key advantage is that intervention ground truth remains known (because the data-generating mechanism is controlled), while covariates and graph structure are realistic. In this setting, explanation stability can be quantified by perturbing the graph (e.g., adding or removing a fraction of edges via bootstrap) and measuring the rank correlation of node or edge importance scores across perturbations; low variance indicates robust explanations. Completeness can be evaluated by checking whether the explanation subgraph alone, when used as input to the model, yields a prediction close to the original (e.g., using fidelity as defined in Section 2.4). Additionally, one should perform a sensitivity analysis on the graph uncertainty ensemble generated in step 3 of the pipeline: for each plausible graph, retrain the GNN (or a lightweight surrogate) and compare the resulting predictions and explanations. This reveals how much structural uncertainty affects conclusions.

**Level 3: Real-world retrospective validation.** Uses temporally separated train, validation, and test periods to avoid information leakage. A robust strategy is walk-forward cross-validation: train on data up to time $t$, validate on $t + 1$ to $t + W$, then slide the window forward. Evaluation should include point accuracy (MAE, RMSE, MAPE), uncertainty calibration (e.g., CRPS, calibration curves), spatial generalisation (performance on unseen regions), and policy-relevant metrics such as peak reduction, hospital burden, and intervention cost. For explainability, real-world validation focuses on stability across different graph construction choices (e.g., alternative edge weighting schemes, different spatial aggregation levels) and expert agreement: how well the identified high-risk nodes or edges align with domain knowledge (e.g., known superspreader locations, travel hubs, or ecological risk zones). While ground-truth explanations are not available, consistency across multiple plausible graphs (as defined in step 3 of the pipeline) provides a proxy for reliability. Counterfactual plausibility can be assessed by checking whether the minimal interventions suggested by the explainer are epidemiologically reasonable, for example whether isolating a few central nodes indeed reduces the predicted outbreak size in a follow-up simulation using a different model (e.g., a mechanistic network SIR model). Moreover, one should report the computational cost of each pipeline step, including graph ensemble generation, GNN training, and explanation computation, to guide practical deployment.

Table 5 summarises the recommended evaluation tasks and the corresponding metrics for each level of evidence. For explanation fidelity, metrics include fidelity (agreement between original prediction and prediction using only the explanatory subgraph), sparsity (size of the explanation relative to the full graph), stability (variance of explanations across graph perturbations), and expert agreement (correlation with domain knowledge). Robustness is assessed by performance degradation and explanation variance when edges are missing or reporting is noisy.

##### Table 5. Recommended evaluation tasks for graph-based epidemic models.
*MAE: Mean Absolute Error; RMSE: Root Mean Square Error; MAPE: Mean Absolute Percentage Error; CRPS: Continuous Ranked Probability Score; AUROC: Area Under the Receiver Operating Characteristic curve; AUPRC: Area Under the Precision-Recall Curve; F1-score: harmonic mean of precision and recall.*

| Task | Objective | Suggested metrics |
| :--- | :--- | :--- |
| **Short-term forecasting** | Predict incidence or hospitalization over a fixed horizon | MAE, RMSE, MAPE, CRPS, calibration error |
| **Risk classification** | Identify nodes or regions likely to exceed a threshold | AUROC, AUPRC, sensitivity, specificity, F1-score |
| **Scenario simulation** | Estimate outcomes under alternative interventions | Difference in final size, peak reduction, time-to-peak delay |
| **Explanation fidelity** | Identify influential nodes, edges, and features | Fidelity, sparsity, stability, expert agreement |
| **Robustness** | Test sensitivity to missing edges and noisy reports | Performance degradation, explanation variance (across $\mathcal{P}(\mathcal{G})$) |

For all three levels, statistical significance of performance differences should be assessed using paired bootstrap tests or cross-validation t-tests, accounting for the non-independence of time series.

---

## 5. Discussion

Graphs make explicit the relational mechanisms of epidemic spread. They reveal why average quantities can be misleading, why clustered susceptibility is dangerous, and why targeted interventions can be more efficient than uniform policies. The COVID-19 case illustrates this principle in a direct human-contact setting: centrality- and spectrum-aware vaccination act by reshaping the contact graph. The hantavirus case illustrates the same principle in a zoonotic setting, where the relevant graph is not only a human contact network but a multilayer molecular–ecological–environmental–human system. Graph neural networks add flexibility by learning nonlinear diffusion patterns from heterogeneous data, while mechanistic constraints preserve epidemiological meaning. Explainability closes the loop between prediction and action: it translates mathematical and machine-learning outputs into interpretable risk pathways and counterfactual policies.

At the same time, the deployment of graph-based epidemic models raises several ethical, legal, and practical challenges that must be addressed proactively. Epidemic graph models may rely on sensitive information, including health records, mobility traces, household structure, workplace contacts, school attendance, genomic sequences, and ecological exposure. Responsible deployment requires data minimization, aggregation where possible, privacy-preserving computation (e.g., differential privacy, federated learning), transparent governance, and explicit communication of uncertainty. Because intervention recommendations may affect different communities unequally, fairness should be evaluated across geography, age, socioeconomic status, and access to care.

A particularly subtle risk is the amplification of existing surveillance biases. If the graph is constructed from surveillance data that under-represent certain communities, for example, due to lower testing rates, under-reporting of cases, or incomplete mobility traces in rural or low-income areas, then the resulting model will systematically underestimate transmission risks in those populations while overestimating them in well-represented ones. Consequently, explanations and recommendations may become unjust, directing resources away from the very communities that need them most. To mitigate this, we suggest several techniques for fairness-aware graph construction. First, use multiple data sources to cross-validate edge presence and node covariates, especially for under-represented groups (e.g., augmenting mobile phone data with travel surveys or census information). Second, apply graph imputation methods that explicitly model missingness as a function of demographic or economic indicators, for instance using a missing-graph mechanism akin to missing-not-at-random models. Third, compute fairness metrics on the graph itself, such as the disparity in average degree, clustering coefficient, or spectral radius across demographic groups, and reweight edges or nodes to balance representation before training. Fourth, during the explainability step, report explanation confidence intervals separately for each group and flag when explanations rely on edges or nodes that are known to be uncertain or biased. Fifth, consider using adversarially debiased GNNs that learn representations invariant to sensitive attributes (e.g., geographic region, socioeconomic status) while preserving predictive accuracy for epidemic outcomes. These fairness-aware construction and learning techniques should be integrated into step 2 (graph construction) and step 5 (GNN learning) of the proposed pipeline.

Another significant risk is automation bias. Public-health authorities may over-trust model outputs, especially when they are presented as precise forecasts or when explanations appear convincingly detailed. The proposed framework should therefore be used as decision support rather than decision replacement. Explanations should clarify assumptions, identify the most uncertain parts of the graph, and distinguish between what the model has learned from data and what has been imposed by mechanistic structure. Visualisation tools that highlight uncertainty (e.g., confidence intervals for node importance, edge shading based on reliability) can help mitigate over-confidence.

Turning to limitations, despite the strengths of the proposed framework, several important limitations must be acknowledged. These can be grouped into three categories. First, data limitations. Real contact networks are never completely observed. Edge lists derived from surveys, proximity sensors, or mobile phones suffer from sampling bias, temporal sparsity, and privacy-induced aggregation. Surveillance data (incidence, hospitalisations) are delayed, under-reported, and often non-specific (e.g., syndromic). For zoonotic diseases, rodent abundance and environmental contamination data are scarce and spatially coarse. These imperfections propagate through the pipeline and can lead to biased estimates of $\mathcal{R}_{\mathcal{G}}$ and unreliable explanations. Our uncertainty quantification step (step 3) partially addresses this, but it cannot compensate for systematic biases in the data generation process. Second, model limitations. The hybrid neural–mechanistic GNN assumes that the underlying dynamics are well approximated by a compartmental model (SIR/SEIR) with a graph structure that captures all relevant transmission pathways. In reality, behaviour changes endogenously (e.g., fear-driven distancing), viral evolution alters transmissibility, and interventions are not perfectly implemented. Moreover, the spectral radius condition $\mathcal{R}_{\mathcal{G}} = \frac{\beta}{\gamma} \rho(\mathbf{A}) > 1$ is a linearised threshold that may not accurately predict invasion when the network is small, highly clustered, or when the initial outbreak is not near the disease-free equilibrium. The NP-hardness of optimal spectral vaccination means that our greedy or heuristics-based solutions are only approximately optimal. Finally, GNNs are known to be vulnerable to distributional shifts; a model trained on one outbreak (e.g., a specific wave of COVID-19) may fail when applied to a new variant with different transmission characteristics. Third, computational and operational limitations. Generating a large ensemble of graphs (step 3) and training spatio-temporal GNNs on each can be computationally expensive, especially for large networks (e.g., national mobility graphs with millions of nodes). Real-time decision support requires fast inference; our pipeline may need to trade off ensemble size for speed. Additionally, the pipeline assumes a degree of technical expertise that may not be available in all public-health settings. Implementing fairness-aware graph construction and debiased GNNs adds further complexity.

Looking forward, several directions can extend and improve the framework. One promising direction is causal graph learning and inference. Current models exploit correlations, but public-health decisions often require causal estimates (e.g., “what would be the effect of a specific intervention in a specific community?”). Future work should integrate causal discovery methods (e.g., invariant causal prediction, structural causal models) with GNNs to estimate causal effects from observational network data. This is particularly important for counterfactual explanations and for distinguishing between a genuine transmission edge and a spurious correlation due to shared environment or testing bias. Another perspective is the development of foundation models for epidemic intelligence. The recent success of large language models and graph foundation models suggests the possibility of a pre-trained epidemic graph model that can be fine-tuned to different pathogens, regions, and data regimes with minimal additional data. Such a model would encode universal patterns of contact, mobility, and spillover, and could be deployed rapidly during an emerging outbreak. However, this requires massive, diverse, and well-curated training datasets, as well as solutions for domain adaptation and privacy. Online learning and adaptive control represent a third important direction. Epidemics evolve rapidly, and policies change dynamically. An online version of the pipeline that continuously updates graph estimates, model parameters, and explanations as new data arrive (e.g., daily) would be highly valuable. Techniques such as streaming GNNs, Bayesian online changepoint detection, and reinforcement learning for adaptive intervention could be integrated into steps 5–7. Fourth, integration with digital twins and simulation environments can further enhance the utility of the pipeline. The pipeline can be embedded within a digital twin of a region or country, where synthetic populations, mobility models, and intervention scenarios are simulated to explore what-if questions at scale. Coupling the GNN surrogate with a high-fidelity mechanistic simulator (as in hybrid models) can combine speed and accuracy. Fifth, human-in-the-loop explainability offers a path toward more trusted and usable systems. Future work should develop interactive explanation interfaces that allow epidemiologists to query the model, drill down into specific nodes or edges, and provide feedback that updates the explanation or even the model. This would build trust and enable iterative refinement. Finally, robustness to structural breaks is essential for real-world deployment. Methods to detect when the underlying graph or transmission process has changed (e.g., due to a new variant, a major policy change, or a seasonal migration) are needed. This could be achieved by monitoring explanation stability and prediction residuals, and triggering a re-estimation of the graph or retraining of the GNN when a break is detected.

---

## 6. Conclusion

This paper has formulated a rigorous mathematical foundation for using graphs, networks, graph neural networks, and explainable artificial intelligence in epidemic and pandemic modelling. Network epidemiology provides spectral thresholds, stochastic dynamics, and control objectives that link graph structure directly to disease invasion and intervention effectiveness. Graph neural networks extend these mechanistic models by learning nonlinear spatio-temporal diffusion patterns from heterogeneous, partially observed data while preserving relational structure. Explainable artificial intelligence offers interpretable evidence for intervention, including node, edge, feature, counterfactual, and uncertainty-aware explanations that are essential for public-health trust and accountability.

The proposed case studies on measles, COVID-19, and hantavirus illustrate how the same graph-based framework can represent vaccination gaps, topology-aware contact control, environmental reservoirs, host transcriptomic response, mobility-driven spread, and adaptive policy design across radically different epidemiological regimes. The unified eight-step pipeline integrates data, graph construction, uncertainty quantification, mechanistic baselines, hybrid GNN learning, explainability, control evaluation, and validation into a coherent decision-support system. Particular attention has been paid to fairness, robustness, and the mitigation of surveillance biases.

A complete research program should now move from formal modelling to reproducible empirical evaluation, integrating synthetic benchmarks, semi-synthetic scenarios, and retrospective public-health data. Such a program can support a new generation of epidemic decision systems that are predictive, interpretable, robust, and operationally meaningful for real-world public-health control.

The proposed framework, from spectral thresholds to hybrid GNNs, from uncertainty-aware explanations to fairness-aware graph construction, represents a significant step toward accountable, evidence-grounded, and adaptive public-health control. Realising its full potential will require close collaboration between modellers, epidemiologists, ethicists, policy makers, and software engineers, as well as open data and code sharing to enable external scrutiny and continuous improvement.

---

**Author Contributions:** Conceptualization, P.H.G. and F.B.; methodology, P.H.G, U.L., A.F. and F.S.; software, U.L. and A.F.; validation, P.Vi. and P.Ve.; formal analysis, P.Vi. and P.Ve.; supervision, P.Ve. and M.C; writing—original draft preparation, P.H.G, P.Vi. and F.B.; writing—review and editing, all the authors; funding acquisition, P.Ve All authors have read and agreed to the published version of the manuscript.

**Funding:** This work has been partially supported by the OFIDIAPlus (Operational Fire Danger preventIon plAtform Plus) project under the INTERREG GREECE-ITALY 2021-2027 PROGRAMME.

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** The data and code are available upon reasonable request from the corresponding author.

**Acknowledgments:** During the preparation of this manuscript, the authors used ChatGPT for syntax checking and language refinement. The schematic overview figure (Figure 1) was generated with the assistance of DALL-E, an AI image generation tool, and subsequently reviewed, edited, and adapted by the authors to ensure scientific accuracy and clarity. All AI-generated content has been critically evaluated; the authors assume full responsibility for the final content of this publication.

**Conflicts of Interest:** The authors declare no conflicts of interest.

---

## References

1. Petrizzelli, F.; Guzzi, P.H.; Mazza, T. Beyond COVID-19 pandemic: Topology-aware optimization of vaccination strategy for minimizing virus spreading. *Computational and Structural Biotechnology Journal* **2022**, *20*, 2664–2671.
2. Cheng, Z.; Ruktanonchai, N.W.; Wesolowski, A.; Pei, S.; Wang, J.; Cockings, S.; Tatem, A.J.; Lai, S. Social, mobility and contact networks in shaping health behaviours and infectious disease dynamics: a scoping review. *Infectious Diseases of Poverty* **2025**, *14*, 123.
3. Wang, L.; Wu, J.T. Characterizing the dynamics underlying global spread of epidemics. *Nature communications* **2018**, *9*, 218.
4. Liu, Z.; Wan, G.; Prakash, B.A.; Lau, M.S.; Jin, W. A review of graph neural networks in epidemic modeling. In *Proceedings of the 30th ACM SIGKDD conference on knowledge discovery and data mining*, 2024, pp. 6577–6587.
5. Bellingeri, M.; Bevacqua, D.; Scotognella, F.; Cassi, D. The critical role of networks to describe disease spreading dynamics in social systems: A perspective. *Mathematics* **2024**, *12*, 792.
6. Branda, F.; Veltri, P.; Chiodo, F.; Ciccozzi, M.; Scarpa, F.; Guzzi, P.H. Computational modeling of infectious diseases: insights from network-based simulations on measles. *BMC Medical Informatics and Decision Making* **2025**, *25*, 238.
7. Branda, F.; Defilippo, A.; Lomoio, U.; Puccio, B.; Ciccozzi, M.; Scarpa, F.; Veltri, P.; Guzzi, P.H. From data to decisions: a modular platform for modelling and simulation of infectious disease diffusion in networks. *BMC Medical Informatics and Decision Making* **2026**.
8. Elahi, S.; Mürmann, P.; Thiran, P. Learn to vaccinate: Combining structure learning and effective vaccination for epidemic and outbreak control. *arXiv preprint arXiv:2506.15397* **2025**.
9. Guzzi, P.H.; Branda, F.; Scarpa, F.; Ceccarelli, G.; Ciccozzi, M.; Giorgi, F.M.; Veltri, P. Integrated Downstream Analysis and Epidemiological Modelling of Hantavirus Infection: From Host Transcriptomics to Transmission Dynamics. *Pathogens* **2026**, *15*, 601.
10. Ma, J.; Wang, P. Epidemic spreading on multilayer community networks. *Physics Letters A* **2025**, *532*, 130199.
11. Schmidt, A.; Zunker, H.; Heinlein, A.; Kühn, M.J. Graph neural network surrogates to leverage mechanistic expert knowledge towards reliable and immediate pandemic response. *Scientific Reports* **2026**, *16*, 6361.
12. Elabid, Z.; Sasal, L.; Busby, D.; Hadid, A. TG-PhyNN: An Enhanced Physically-Aware Graph Neural Network framework for forecasting Spatio-Temporal Data. In *Proceedings of the Pacific Rim International Conference on Artificial Intelligence*. Springer, 2024, pp. 42–48.
13. Han, S.; Stelz, L.; Sokolowski, T.R.; Zhou, K.; Stöcker, H. Unifying physics-and data-driven modeling via novel causal spatiotemporal graph neural network for interpretable epidemic forecasting. *arXiv preprint arXiv:2504.05140* **2025**.
14. Khalili, H.; Wimmer, M.A. Towards improved XAI-based epidemiological research into the next potential pandemic. *Life* **2024**, *14*, 783.
15. Huang, Z.; Hwang, J.; Zhang, J.; Baik, J.; Zhang, W.; Wodarz, D.; Sun, Y.; Gu, Q.; Wang, W. Causal graph ode: Continuous treatment effect modeling in multi-agent dynamical systems. In *Proceedings of the ACM Web Conference 2024*, 2024, pp. 4607–4617.
16. Moore, S.; Hill, E.M.; Tildesley, M.J.; Dyson, L.; Keeling, M.J. Vaccination and non-pharmaceutical interventions for COVID-19: a mathematical modelling study. *The Lancet Infectious Diseases* **2021**, *21*, 793–802.
17. Branda, F.; Ahmed, M.M.; Ciccozzi, M.; Guzzi, P.H.; Scarpa, F. The next paradigm in bioinformatics: a review of multi-agent systems and foundational models for end-to-end scientific discovery. *Briefings in Bioinformatics* **2026**, *27*, bbag245.
18. Kermack, W.O.; McKendrick, A.G. A contribution to the mathematical theory of epidemics. *Proceedings of the Royal Society of London. Series A, Containing papers of a mathematical and physical character* **1927**, *115*, 700–721.
19. Anderson, R.M.; May, R.M. *Infectious diseases of humans: dynamics and control*; Oxford University Press, 1991.
20. Pastor-Satorras, R.; Castellano, C.; Van Mieghem, P.; Vespignani, A. Epidemic processes in complex networks. *Reviews of Modern Physics* **2015**, *87*, 925–979.
21. Newman, M.E. *Networks: an introduction*, 2010.
22. Kiss, I.Z.; Miller, J.C.; Simon, P.L.; et al. *Mathematics of epidemics on networks*. Cham: Springer **2017**, *598*, 31.
23. Scarselli, F.; Gori, M.; Tsoi, A.C.; Hagenbuchner, M.; Monfardini, G. The graph neural network model. *IEEE Transactions on Neural Networks* **2008**, *20*, 61–80.
24. Kipf, T.N.; Welling, M. Semi-supervised classification with graph convolutional networks. *arXiv preprint arXiv:1609.02907* **2016**.
25. Wu, Z.; Pan, S.; Chen, F.; Long, G.; Zhang, C.; Yu, P.S. A comprehensive survey on graph neural networks. *IEEE Transactions on Neural Networks and Learning Systems* **2020**, *32*, 4–24.
26. Ying, Z.; Bourgeois, D.; You, J.; Zitnik, M.; Leskovec, J. Gnnexplainer: Generating explanations for graph neural networks. *Advances in Neural Information Processing Systems* **2019**, *32*.
27. Luo, D.; Cheng, W.; Xu, D.; Yu, W.; Zong, B.; Chen, H.; Zhang, X. Parameterized explainer for graph neural network. *Advances in Neural Information Processing Systems* **2020**, *33*, 19620–19631.
28. Branda, F.; Giovanetti, M.; Petrosillo, N.; Ahmed, M.M.; Perra, M.; Sanna, D.; Ceccarelli, G.; Ciccozzi, M.; Bucci, E.; Scarpa, F. Measles and public health: an integrative approach. *Biology Direct* **2025**, *20*, 103.
29. Fauci, A.S.; Folkers, G.K. HIV/AIDS and COVID-19: shared lessons from 2 pandemics. *Clinical Infectious Diseases* **2025**, *80*, 1074–1079.

---

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.