```md
# Parameter Estimation Using Meta-Heuristics in Systems Biology: A Comprehensive Review

**Jianyong Sun, Jonathan M. Garibaldi, and Charlie Hodgman**

## Abstract

This paper gives a comprehensive review of the application of metaheuristics to optimization problems in systems biology, mainly focusing on the parameter estimation problem (also called the inverse problem or model calibration). It is intended for either the system biologist who wishes to learn more about the various optimization techniques available and/or the metaheuristic optimizer who is interested in applying such techniques to problems in systems biology. First, the parameter estimation problems emerging from different areas of systems biology are described from the point of view of machine learning. Brief descriptions of various metaheuristics developed for these problems follow, along with outlines of their advantages and disadvantages. Several important issues in applying metaheuristics to the systems biology modeling problem are addressed, including the reliability and identifiability of model parameters, optimal design of experiments, and so on. Finally, we highlight some possible future research directions in this field.

**Index Terms—** Systems biology, parameter estimation problem, model calibration, heuristic, metaheuristic, evolutionary algorithms.

---

## 1 INTRODUCTION

SYSTEMS biology has become an increasingly important interdisciplinary research area in recent years [7], [64], [73], [82], [83], [86], [116], [170]. Systems biology aims to understand the processes of living systems systematically: functionalities and spatial/temporal behavior of cellular components need to be characterized in a systematic manner rather than separately. It is well accepted that systems biology consists of two backbones. First, the need to systemically collect a large amount of experimental data for cellular components. Second, the need to theoretically model the living cells as a system that can be characterized by state variables, inputs, and outputs. As stated by Kremling and Saez-Rodriguez [86], one of the most important activities in systems biology is to analyze biological systems with respect to feedback characteristics, sensitivities, gain quantification, and structure identification, since this can improve our knowledge on cellular systems and offer new methods to develop models.

Mathematical descriptions of living cells can be qualitative or quantitative, deterministic or stochastic depending on the aims. Fisher and Henzinger characterize biological models as either computational models or mathematical models [44]. Mathematical models are used to represent actual quantitative relations between the components in the system. Generally, a system of differential equations and/or differential algebraic equations (DAEs) is used to represent the interaction and processes among the various components. These mathematical models are deterministic. They can be simulated, analyzed, and possibly solved, but require very detailed knowledge of the biological system. On the other hand, computational models, such as Boolean networks [49], [72] or Petri Nets [32], [126], encode abstract representations to mimic biological phenomena. They have an inherent execution scheme attached to the models, and relate different qualitative configurations (“states”) to each other. The computational models can be deterministic, nondeterministic and/or stochastic. They have the advantages to effectively represent the biological systems without precise quantitative relationships, or with many different components which may change over time.

In both computational and mathematical biological models, control parameters are used to define the behavior of the models. For example, S-systems [139], [140], [141], a type of mathematical model, are characterized by a set of kinetic parameters and rate parameters. In a Petri Net, the transition matrix among different variables exhibits an important role in defining the system. Some of these parameters usually cannot be experimentally determined. This leads to the need to attempt to estimate these parameters by computational methods.

A commonly used method to estimate the parameters is to transform the estimation problem to an optimization problem, in which optimization algorithms can be applied to find the best-fit parameters. A survey paper has been published recently reviewing the transformation to optimization problems in computational systems biology [18]. In this paper, optimization problems emerging from different areas of systems biology are listed and classified with respect to their characteristics. For example, some optimization problems are represented as linear programming, such as in metabolic flux balance analysis (FBA) [71], semidefinite programming (SDP) as in complex biological systems [87], bilevel optimization as in gene knockout strategy [29], metabolic pathways under satisfiability considerations [31] and metabolic engineering [46], mixed integer linear/nonlinear programming [37] as in time-delay gene regulatory networks and intracellular flux analysis and convex optimization as in bimolecular interaction networks [52], dynamic optimization as in dynamic flux balance analysis [99] and biological network design strategies [3], mixed integer dynamic optimization as in designing genetic circuits [38], nonlinear programming [157], etc.

Among these methods, most of them have been studied thoroughly by the computational optimization community. A variety of global optimization algorithms, such as branch and bound, branch and cut [27], etc., have been developed for guaranteed convergence to global optimum with solid mathematical foundations which can be applied to a restricted set of optimization problems, e.g., linear and mixed integer programming. Besides those deterministic global optimization methods, gradient-based algorithms like BFGS [26], Levenberg-Marquardt [91], SOLNP [168], SNOPT [47] and N2FB/DN2GB [66], and direct methods like NOMAD [2] and NEWUOA [128], have been developed in the optimization community [45]. These algorithms can only guarantee to converge to local optimum, hence are classified as local optimization methods. Many of these classical optimization methods have been applied to the parameter estimation problem and have achieved great success, such as in [10], [37], [78], [88], [99], [115], [124], [127], [142], [143], [161], and many others.

However, the deterministic global algorithms mentioned above are usually very time-consuming and highly computationally intensive. Hence, they cannot obtain satisfactory solutions in a reasonable time when applied to the practical estimation problems in systems biology with realistic problem sizes. Moreover, due to some inherent characteristics of the practical problems, such as the presence of noisy data caused by inevitable measurement errors in experiments and/or dynamics with state events, and nonsmooth and multimodal (nonconvex) search spaces, the application of these deterministic local optimization algorithms is seriously limited.

Alternatively, modern optimization approaches such as evolutionary algorithms (EAs) and other metaheuristics[^1] can manage to reach global or near-global optima in reasonable time for large size problems (for recent advances in EAs, see [1], and for metaheuristics, see [145]). Particularly, EAs have the advantages of robustness in noisy environments, and an inherent parallel algorithmic structure which can be exploited with modern computational hardware, including parallel processing. This motivates the application of EAs and metaheuristics to optimizing problems in systems biology.

In this paper, we give a comprehensive overview of the application of metaheuristics in different areas of systems biology. This paper is intended for either the system biologist who wishes to learn more about the various optimization techniques available and/or the metaheuristic optimizer who is interested in applying such techniques to problems in systems biology. The rest of the paper is organized as follows: Section 2 briefly characterizes the different biological processes in systems biology. Section 3 gives the mathematical formulation of the parameter estimation problem. Section 4 reviews the application of various metaheuristics to the parameter estimation problem. Important issues and future research directions are discussed in Section 5 and Section 6 concludes the paper.

[^1]: Strictly speaking, EAs can be regarded as a type of meta-heuristic. We distinguish EAs and metaheuristics only in order to emphasize the huge popularity of evolutionary algorithms, especially genetic algorithms, in industry, engineering, biology and many other domains.

---

## 2 BIOLOGICAL PROCESSES

Before describing the metaheuristics, we need to clarify the different types of biological or biochemical process found in living things, which may be investigated using systems biology. The computational and mathematical approaches [21] associated with these processes can be very different in nature, which should be kept in mind when calibrating the models. Traditionally there have been three types of biological process subjected to modeling, namely metabolic, signal-transduction, and gene-regulatory networks [75]. The following text will examine each of these in turn, though the reality within living cells is that these three processes are intermingled in “integrated” networks, which will also be examined.

Living cells and organisms require energy to carry out their various functionalities, such as to grow and reproduce, to maintain their structures and to respond to their environment. The overall process is referred to as “metabolism,” which refers to the many chemical reactions taking place in living cells to generate and use the free energy they need. Chemical compounds are converted into other chemical compounds, often catalyzed by specific proteins known as enzymes. These reactions are linked together in that the output of one known (referred to as the “product”) can be the input (known as the “substrate”) of another. These substrates, intermediates, and products are called “metabolites,” and they link together to form a “metabolic network,” of which a simplified version is shown in Fig. 1. Often in cells, certain chains of reactions have a higher flux of atoms and molecules through them, these are known as “metabolic pathways.” Every reaction in a metabolic network can be defined by its “stoichiometric equation,” hence the topology of the metabolic network can be defined by the “stoichiometric matrix” of equations for every reaction. Despite the complexity of metabolism, the concentrations of metabolites are kept low and largely constant, and this state is maintained by a sophisticated network of metabolic controls [43].

Signal transduction is the process of conversion of external signals, such as hormones, growth factors, neurotransmitters and cytokines, to a specific internal cellular response. Examples of the latter include changes to enzyme activity and expression of genes, which might in turn lead to gross cellular changes including cell division or cell suicide. Most processes of signal transduction involve ordered sequences of changes to macromolecules inside the cell. The most common examples are chains of protein kinases, which are enzymes that change the structure and hence activity of other enzymes that are themselves protein kinases. The chain ends when the protein is a metabolic enzyme or gene regulator. Thus, signal transduction pathways consist largely of molecular on/off switches that control the passing of information (signal) from one substance to the next. Such processes are usually rapid in the order of milliseconds or minutes and often result in a large amplification of the initial signal. However, some signals can take hours or even days to exert their effect, for example, the signal to commit bone-marrow cells to become red blood cells.

Gene expression is the combined processes of transcription and translation of a gene into a functional gene product, often a protein though some genes encode a functional RNA, such as ribosomal RNA. The various steps in the gene expression process may be modulated by other gene products or incoming signals. Gene regulation is the basis for cellular differentiation, morphogenesis, and the versatility and adaptability of any organism. The level of transcription can be measured using microarrays and other techniques, whereas protein levels are often harder to determine. The regulators of gene expression are usually referred to as Transcription Factors (TFs), and where they affect the expression level of other TFs, we can construct Gene Regulatory Networks. Fig. 2 shows an example of one such network.

As has become apparent from the details above, the reality of biological systems is that these three types of network are intimately connected. Increasingly, the most incisive understanding of biological systems is now coming from the study of integrated networks comprising two or more of the above types of network, for example, see Fig. 3. Given the ability of laboratory molecular biologists to generate large quantities of expression and biomolecular interaction data, it is now possible to construct, analyze, and simulate the networks underlying many biological processes [70].

**Fig. 1.** A metabolic network depicting the set of biochemical reactions that lie at the center of metabolism in all higher organisms.

**Fig. 2.** A gene regulatory network controlling the flowering time of *Arabidopsis*, reproduced from [4].

**Fig. 3.** Integrated network of Gibberellin-mediated plant cell growth.

---

## 3 PARAMETER ESTIMATION PROBLEMS

### 3.1 Definition

Nonlinear dynamic systems, as in systems biology, are usually modeled as a nonlinear programming problem with differential-algebraic constraints in the mathematical models. To model the nonlinear dynamic systems, usually differential-algebraic equations of the following form are applied:

\[
\frac{dy}{dt} = f(\mathbf{x}, \mathbf{y}, \mathbf{p}, \mathbf{v}, t), \tag{1}
\]

subject to

\[
\mathbf{x}(t_0) = \mathbf{x}_0,
\]
\[
\mathbf{h}(\mathbf{x}, \mathbf{y}, \mathbf{p}, \mathbf{v}) = 0,
\]
\[
\mathbf{g}(\mathbf{x}, \mathbf{y}, \mathbf{p}, \mathbf{v}) \leq 0,
\]
\[
\mathbf{p}^{L} \leq \mathbf{p} \leq \mathbf{p}^{U}, \tag{2}
\]

where \(\mathbf{p}\) is a vector of control parameters of the DAEs which needs to be estimated, with initial condition (2); \(\mathbf{x}\) is the differential state variables, \(\mathbf{v}\) is a vector of other parameters (e.g., parameters obtained through experimental studies, usually time-invariant) that do not need to be estimated; and \(\mathbf{h}\) and \(\mathbf{g}\) are the possible equality and inequality constraints that express additional requirements for the system performance. Finally, \(\mathbf{p}\) is subject to upper and lower bounds acting as inequality constraints.

On the other hand, in computational models, the dynamic bioprocesses are represented by a set of rules or programs, deterministically or stochastically. Petri Nets (in brief PNs, as shown in Fig. 4, which is reproduced from [32]) have been widely studied as an abstraction for bioprocesses, including signaling networks, gene regulatory networks, and metabolic networks. Readers are referred to [32], [126] for detailed descriptions of PNs. Given the precondition matrix as shown in Fig. 4b and the associated rules (the kinetic parameters and the Petri Net structure), a postcondition matrix can be obtained deterministically or stochastically (in stochastic Petri Nets) as the output.

In both computational and mathematical models, in order to make the model best describe the modeled biological process, we need to find the parameter vector \(\mathbf{p}\) (or the kinetic parameters in the Petri Net) that most likely minimize the difference between \(\mathbf{y}_{\exp}\), which is the experimental measure of a subset of the so-called output state variables, and \(\mathbf{y}(\mathbf{p}, t)\) which is the model prediction for those outputs (i.e., the solution of the DAEs or the output of the Petri Net). The problem of finding the optimal parameter \(\mathbf{p}\) is called the parameter estimation problem, the inverse problem, or model calibration. Very few theoretical results on the computational complexity of parameter estimation problems exist in the literature, especially in case \(\mathbf{p}\) is real. In [23], the authors transformed the gene regulatory network construction problem to the so-called set multicover problem, which is NP-hard.

In literature, solutions to the parameter estimation problem usually fall into two categories, namely the collocation methods [129], [131], [149] and the nonlinear least-squares approaches [102]. Collocation methods, also called basis function expansions and principal differential analysis, first employ data smoothing methods without considering the DAEs to obtain the regressed \(\hat{\mathbf{x}}\), then the parameters are obtained by minimizing a least squares fit of \(d\hat{\mathbf{x}}/dt\) to \(f(\hat{\mathbf{x}}, \mathbf{y}, \mathbf{p}, \mathbf{v}, t)\) with respect to the parameter \(\mathbf{p}\). The method is attractive when \(f\) is quasi-linear (i.e., having some properties of linearity) in \(\mathbf{p}\), but nonlinear in \(\mathbf{x}\). Collocation methods have been widely applied in the literature, such as in [6], [102], [158] using artificial neural network as data regression methods, in [34], [129], [131], [149], [158], [169] using spline regression, in [89] using alternating regression, in [144] based on fuzzy clustering, and in [5] based on a grid approach, etc. However, in most cases of the parameter estimation problem, the linearity with respect to the parameter \(\mathbf{p}\) does not hold.

In the nonlinear least square approaches, the parameter vector \(\mathbf{p}\) is to be obtained by minimizing [108]

\[
J = \int_{t_1}^{t_f}
(\mathbf{y}^{t}_{\exp} - \mathbf{y}(\mathbf{p}, t))^T
\mathbf{W}(t)
(\mathbf{y}^{t}_{\exp} - \mathbf{y}(\mathbf{p}, t))\,dt,
\]

where \(\mathbf{W}(t)\) is a weighting (or scaling) matrix, \(t\) is the time index ranging from \(t_1\) to \(t_f\). In practice, we do not have continuous experimental measures but only discrete measurements in a time series \([t_1,\ldots,t_N]\). The objective function can then be written as

\[
\tilde{J} =
\sum_{i=1}^{N}
(\mathbf{y}^{i}_{\exp} - \mathbf{y}(\mathbf{p}, t_i))^T
\mathbf{W}(t_i)
(\mathbf{y}^{i}_{\exp} - \mathbf{y}(\mathbf{p}, t_i)). \tag{3}
\]

From the machine learning point of view, the objective function is the result of the maximum likelihood estimation. Assuming that the experimental data are independently and identically distributed (i.i.d), and follow the normal distribution with mean \(\mathbf{y}_{\exp}\) and \(\sigma = diag(\sigma_1,\ldots,\sigma_N)\), the negative log-likelihood function \(\mathcal{J}\) of the data set is given as

\[
\mathcal{J} \propto \frac{1}{2}\sum_{i=1}^{N}
\left[
\log(\sigma_i)
+
\frac{\|\mathbf{y}_{\exp}(t_i)-\mathbf{y}(\mathbf{p}, t_i)\|^2}{\sigma_i^2}
\right]. \tag{4}
\]

Obviously, minimizing 4 is equivalent to minimizing 3 where \(\mathbf{W}(t_i)=\frac{1}{\sigma_i}\). Besides these measures, we shall see more measures that may be used for the goodness of the data fitting in the following sections.

### 3.2 Examples

To begin with, we provide three examples to show the typical characteristics of parameter estimation problems. The first example is the modeling of biosystems by stiff ordinary differential equations (ODEs) as presented in [102]. The metabolic pathway model is shown in Fig. 5. In the model, there are 16 real parameters, while the search ranges of these parameters are in \([0.1, 1,000]\). According to [102], the ODE model is stiff, which means that it will take a long time to reach a solution of the ODEs. Adopting the fourth order Runge-Kutta method as the ODE solver with a time step 0.0001, the fast algorithm developed in [102] still took about 10 hours to obtain an optimal solution with 10 percent relative error w.r.t the experimental data on a computer with Pentium 4, Xeon 2 GHz CPU with a memory size of 1,024 MB.

Another example is the stochastically simulated gene network as discussed in [153]. In the three-gene repressilator model as shown in Fig. 6, the concentration trajectories are simulated by a hybrid jump/continuous Markov process due to Salis and coworkers [137], [138], which is a stochastic simulation process. The stochastic nature of the simulation indicates the noisiness in evaluating the trajectories. To reduce the noisiness, the authors in [153] calculated the ensemble average of \(\eta\) simulations. In the simulated annealing (SA) algorithm developed for the three-gene model, to estimate the six positive real parameters, the authors required \(24 \cdot \eta\) Intel Itanium 2 CPU at 1.5 GHz hours.

Finally, in the community of computational biology, an S-system is usually applied to model a dynamic model for biochemical pathways such as metabolic pathways, protein pathways, etc. It has the following mathematical form:

\[
\dot{y}_i =
\alpha_i \prod_{j=1}^{n+m} y_j^{g_{ij}}
-
\beta_i \prod_{j=1}^{n+m} y_j^{h_{ij}},
\]

where \(n\) is the number of dependent variables, \(m\) is the number of independent variables, the \(y_j\)’s correspond to the current states (typically concentrations) of the different gene, metabolite, or proteins. The \(\dot{y}_i\)’s are the rates of change (differentials) in the concentrations, rate parameters \(\alpha_i, \beta_i\) and kinetic orders \(g_{ij}\), and \(h_{ij}\) are parameters measuring the influence of \(y_j\) on \(y_i\). From the parameter estimation point of view, the parameters that need to be estimated in an S-system include the network structure and these kinetic parameters. It can be seen that the number of kinetic parameters in a S-system that needs to be estimated is \(2n(n+1)\). Even for a small-size network, the number is prohibitively high, which casts great doubt on the estimation performances of the local search algorithms.

The three examples described show some basic characteristics of parameter estimation problems. The number of parameters could be very high (the S-system), and the domain ranges of these parameters differ by several orders of magnitude. The evaluation of a solution is either time-consuming (e.g., the stiff ODE model) or with noise (e.g., the three-gene model).

**Fig. 4.** An example of a Petri Net, reproduced from [32].

**Fig. 5.** The metabolic pathway model, which is modeled by a stiff ODE, shows five reactions with six reactants and one feedback loop in terms of enzyme concentration (reproduced from [102]).

**Fig. 6.** The three-gene repressilator model, reproduced from [153].

### 3.3 Optimization Methods

To minimize 3 with respect to \(\mathbf{p}\), many optimization algorithms can be used. The above nonlinear programming problem with differential-algebraic constraints often exhibits multimodal (nonconvex) characteristics because of the nonlinear and constrained nature. If local search algorithms, such as the standard Levenberg-Marquardt method [91], are to employed, it is very likely that the parameter(s) found will be of a local nature, as discussed in Mendes and Kell [106]. Moreover, many of the local search algorithms require first-order and/or second-order derivatives, such as Gauss-Newton methods, DN2GB [66], etc. In the case that the problem is nonsmooth and/or noisy (which are universally common in parameter estimation problems in systems biology), these local search algorithms are no longer effective or even not applicable. Instead, some other derivative-free local search methods, e.g., Nelder-Mead method [114], NOMADm [2], and NEWUOA [128] can be employed but will probably not be effective, again due to their local nature. An instinctive way to overcome the local nature of these optimization approaches is to apply them multiple times on different starting points. However, it is widely acknowledged in the evolutionary computation community that this multistart (MS) approach is not effective simply because there is no supervision in generating starting points. To this end, metaheuristics come into play for the reasons mentioned above. In the next section, we review the various metaheuristic approaches used in systems biology.

---

## 4 APPLICATION OF METAHEURISTICS IN PARAMETER ESTIMATION

In this section, we review the application of metaheuristics to the parameter estimation problem in terms of the variants of metaheuristics, including simulated annealing, genetic algorithms (GA), evolutionary programming (EP), differential evolution (DE), evolution strategies (ES), hybrid strategies, and so on, along with the specific models and corresponding biological processes. Table 1 lists the metaheuristics reviewed and the associated biological models. Moreover, the dimensions and representation of the decision variables used are shown.

### Table 1. The Metaheuristics Used for Parameter Estimation Problems in System Biology Models

| System Biology Model | Meta-heuristics | Dimensions | Solution Encoding | References |
|---|---|---:|---|---|
| biochemical networks (S-system) | SA | 18 | continuous | [50] |
| transcriptional regulatory network | SA | 3 | continuous | [39] |
| *in vitro* Oscillators | SA | 22/28 | continuous | [39] |
| stochastic gene network model | SA | 6 | continuous | [153] |
| transcriptional cascades network | SA | 16 | continuous | [24] |
| pulse generating network | SA | 15 | continuous | [24] |
| signal transduction network | GA | 18 | continuous | [107] |
| MSAC dynamical model | GA | 4 | continuous | [62] |
| insulin network | GA | 35 | binary | [13] |
| signalling transduction pathway | GA | 263 | continuous | [9] |
| cellular dynamic regulation network | Two-stage GA | 60/220 | continuous | [58] |
| gene regulatory network (S-system) | Co-evolutionary GA | 135/2460 | continuous | [80] |
| gene regulatory network | GA | 36 | integer | [101] |
| biosystem model | GA/RBF | 16 | continuous | [102] |
| metabolic pathways (Petri Net) | GA | 10-20 | integer | [120] |
| metabolic engineering | GA | 240 | binary/integer | [123] |
| gene regulatory network (S-system) | GA | 60 | continuous | [76] |
| gene regulatory network (S-system) | GA | NA | continuous | [152] |
| biological networks (S-system) | Multi-objective GA | 18/24 | continuous | [94] |
| metabolic pathways | GA | 8 | continuous | [48] |
| gene regulatory network | ES | NA | continuous | [134] |
| metabolic flux analysis | ES | 24 | continuous | [165] |
| HIV immunology model | ES | 9 | continuous | [103] |
| gene regulatory network (Petri Net) | GP | NA | tree | [81] |
| chemical reaction network (Petri Net) | GP | NA | tree | [85] |
| non-linear gene interaction model (Petri Net) | GP | NA | tree | [110] |
| non-linear gene interaction model (Petri Net) | GP | NA | tree | [109] |
| non-linear gene interaction model (Petri Net) | GP | NA | tree | [111] |
| gene regulatory network (S-system) | GP | NA | tree | [104] |
| isomerization reaction model | SS | 5 | continuous | [40] |
| dynamic biological model | SS | 5-20 | continuous | [133] |
| metabolic flux analysis | DE | 24 | continuous | [166] |
| gene regulatory network (S-system) | DE | 60 | continuous | [117] |
| gene regulatory network (S-system) | DE | 60 | continuous | [119] |
| gene regulatory network (S-system) | DE | 60 | continuous | [119] |
| biological networks (S-system) | DE | 27-60 | continuous | [154] |
| biological systems | SRES/DN2GB | 16 | continuous | [132] |
| biological systems | SRES/MS | 4-5 | continuous | [16] |
| gene regulatory network (Recurrent Neural Network) | DE/PSO | 72 | continuous | [164] |
| gene regulatory network (S-system) | GP/ES | 40 | tree/continuous | [77] |
| gene regulatory network (S-system) | GP/LMS | 3/60 | tree/continuous | [8] |
| gene regulatory network (S-system) | GA/ES | 60 | continuous | [147] |
| biological systems | GP/ES | NA | tree/continuous | [90] |

*“Dimensions” represents the number of the decision variables used, while “NA” in the table indicates that the dimensions are not specified in the reference.*

### 4.1 Simulated Annealing

The simulated annealing algorithm is widely applied in parameter estimation problems, if not as popular as GA. The basic components of SA include an objective function \(f\), a definition of neighborhood, a cooling schedule, an acceptance criterion, and a solution perturbation scheme. Starting from an initial solution \(\mathbf{x}\), the SA perturbs \(\mathbf{x}\) in the neighborhood to create a new solution \(\mathbf{x}'\). Then, \(\mathbf{x}'\) is checked for whether it is accepted as the current solution. Usually, if \(f(\mathbf{x}') < f(\mathbf{x})\), then \(\mathbf{x}'\) replaces \(\mathbf{x}\), otherwise the probability of replacing \(\mathbf{x}\) with \(\mathbf{x}'\) equals

\[
\exp\left(-\frac{f(\mathbf{x}')-f(\mathbf{x})}{T}\right)
\]

where \(T\) is called the cooling temperature. This process is repeated until the termination criterion is satisfied.

In [50], SA is applied to estimate the parameters incurred in the simulation of integrated biological systems exhibiting complex dynamics such as genetic circuits, signal transduction, and metabolic networks based on S-systems. In the developed SA, the present parameters \(\mathbf{p}\) are perturbed as follows:

\[
\mathbf{p} = \mathbf{p} + c\log_e(\sqrt{E}+1)\mathcal{N}(0,1),
\]

where \(c\) is a constant, \(\mathcal{N}(0,1)\) is a Gaussian distribution with zero mean and standard deviation of one. The acceptance probability of a candidate \(\mathbf{p}'\) is computed as

\[
p(\mathbf{p}'|\mathbf{p}) = e^{-\Delta E/T},
\]

where

\[
E = \sum_{i=1}^{n}\sum_{j=1}^{m}(y^j(i)-y^j_{\exp}(i))^2,
\]

is the objective function to be minimized. The cooling schedule is to lower the temperature \(T\) by multiplying the current value by 0.96.

In [39], the adaptive simulated annealing algorithm [65] is applied to optimize the least-squares residue with a regularization based on the Akaike information criterion (AIC). Given a set of candidate models \(M_1,\ldots,M_m\), the fitness function for the \(i\)th model is given by

\[
f_i(\mathbf{p}) \propto
\frac{1}{2}\log\left[
\sum_{j=1}^{N}\|\mathbf{y}(i)-\mathbf{y}_{\exp}(i)\|^2
\right]
+
\frac{P_i}{N},
\]

where \(P_i\) is the number of parameters in the model, and \(N\) is the number of time points. A modified AIC criterion is applied to carry out model selection when the sampling size is small, in [14]. Note that in case the number of candidate models is exponentially large, metaheuristics could be applied to find the best-fit model. It is worth comparing the AIC model selection criterion with the Laplacian criterion which will be discussed shortly.

In [153], the authors proposed to apply the simulated annealing method for parameter estimation in a stochastically simulated gene network model. The considered stochastic dynamical system is modeled as a hybrid jump/continuous Markov process, which is simulated with a Langevin equation

\[
dX_i(t)=\sum_{j=1}^{M} v_{ij}a_j(\mathbf{X}(t))dt
+\sum_{j=1}^{M} v_{ij}\sqrt{a_j(\mathbf{X}(t))}\,dW_j,
\]

where \(\mathbf{X}\) denotes reactions, and \(\mathbf{W}\) is a Wiener process. The solution to the differential-algebraic equations is based on the improved Gillespie algorithm. In the developed SA, the accept/reject decision is based on the ensemble average energy

\[
\langle E\rangle=\frac{1}{\eta}\sum_{i=1}^{\eta}|\lambda_i-\lambda_{goal}|,
\]

where \(\eta\) is the size of the neighborhood,

\[
\lambda_i = N \times \Delta t / j_{max}
\]

is the dominant period for the \(i\)th solution, and \(\lambda_{goal}\) is the desired period. Obviously, the considered dynamical system is of stochastic nature, which exhibits uncertain output. The application of the evolutionary algorithm specially developed for optimization under uncertain environments [167] could be applied in this instance.

In [24], adaptive simulated annealing [65] is applied to estimate parameters of two synthetic gene networks. The author first implemented a hybrid Gaussian filter to smooth the experimental data in order to compensate for noise and missing data points. Then, the SA was applied on the preprocessed data. The cost function is given by

\[
f(\mathbf{p}) = \sum_{i=1}^{n}(\log y(i)-\log y_{\exp}(i))^2.
\]

The SA optimization was performed multiple times using a different, randomized set of initial estimates of \(\mathbf{p}\), the kinetic parameters. It is doubtful whether the multistart SA performs better that of the multistart of the local search algorithms as described in Section 3.

### 4.2 Genetic Algorithms

Genetic algorithms are perhaps the most popular method used in the parameter estimation problem, partially because of their popularity to the public. A GA emulates Darwin’s principle of “survival of the fittest” and simulates the genetic evolution found in biology. It is a population-based iterative search algorithm. To construct a GA, a solution encoding (an individual should be decoded as a solution to the considered problem), a fitness function which distinguish the fitness among individuals, are required. The GA starts with a randomly or heuristically generated population (a population is a group of individuals). The population evolves through three operations: selection, recombination, and replacement. The selection operation selects high-fitness individuals, the recombination operators create new individuals (offsprings), and through replacement operation, the next generation of individuals is created.

In [107], real-coded genetic algorithms are used to estimate the parameters in a signal transduction network. The signal transduction, based on the law of mass action, is modeled by a set of coupled ordinary differential equations of the same form as (1). The objective function used to measure the difference between the experimental data and the model predictions is defined as

\[
f(\mathbf{p})=
\left(
\sum_{i=1}^{n}\sum_{j=1}^{m}
\left\{
\frac{|y^j(i)-y^j_{\exp}(i)|}{|y^j_{\exp}(i)|}
\right\}
\right)^2,
\]

where \(n\) is the number of data points for each experiment, \(m\) is the number of G-protein subtypes, \(\mathbf{y}_{\exp}\) represents the known experimental data, and \(\mathbf{y}\) is the simulated data of the steady state activated G-protein concentration, i.e., the solution of the ODEs. The Augmented Lagrangian Genetic Algorithm (ALGA) [35], [36] which is provided in the *Genetic Algorithm and Direct Search Toolbox for Matlab* was applied in the paper.

In [62], the authors have constructed and validated for the human MMSAC mechanism in an *in silico* dynamical model originating from the biochemical reactions for the underlying molecular processes. Nonlinear ordinary differential equations for the concentrations of 11 proteins and complexes of the MSAC are derived. Most of the kinetic constants are taken from literature, the remaining four unknown parameters are derived by an evolutionary optimization procedure for an objective function describing the dynamics of the APC:Cdc20 complex.

In [13], a binary genetic algorithm with a niching strategy is developed to determine the gene network structure which is modeled as a Bayesian network. The niching strategy, called deterministic crowding [100], is applied to reinforce diversity through the population and avoid the optimization algorithm getting trapped in local optima in the early stages of evolutionary learning. The Bayesian information criterion (BIC) offers a simple way to evaluate a Bayesian network for selecting optimal Bayesian network structure, and the evaluation is used as the fitness function in the binary GA. Given a Bayesian network \(G\), the best network structure is determined by minimizing the BIC

\[
\min_G \left\{
-2\log p(D|G,\theta) + K_G\log(s)
\right\},
\]

where \(s\) is the size of the parameter vector, \(p(D|G,\theta)\) is the probabilistic distribution defined for the Bayesian network, and \(K_G\) is the number of free parameters of model \(G\).

In [9], the parameter estimation problem of a kinetic model of a signaling pathway in a neuronal cell is addressed by using a genetic algorithm. The objective function to the signal transduction network is described as the inverse of the squared euclidean distance between the experimental time course of the concentration of the activated fraction of proteins and the simulated time course for the same species

\[
f(\mathbf{p}) =
\left[
\sum_{i=1}^{m}\sum_{j=1}^{N}
\left(y^j(i)-y^j_{\exp}(i)\right)^2
\right]^{-1}.
\]

The parameter estimation does not include the network topology learning process. The genetic algorithm developed maintains a number of subpopulations, and hence can be considered as a parallel genetic algorithm. A new selection operator is employed, in which the probability \(P_i\) of selecting the \(i\)th individual is defined as follows:

\[
S_i = f_i^{1/T}
\qquad
P_i = \frac{S_i}{\max\{S_j\}},
\]

where the constant parameter \(10^{-4}\leq T < 1\) is used to shape the distribution of the probabilities. Classical GA operators, i.e., one-point crossover and mutation, are applied to create new offspring. Each subpopulation evolves independently, while a percentage of best offsprings in each population frequently moves into a different subpopulation.

In [102], a combination of a genetic algorithm and a radial basis function network (RBF) is developed to estimate parameters in stiff equations[^2] of biosystems. In the developed algorithm, the RBF neural network is first applied to carry out data smoothing with respect to the experimental data. The RBF is used to overcome the time-consuming problem of solving the stiff ODEs due to the iterative numerical integrations. Consequently, the GA is applied for selecting additional data to improve the RBF learning accuracy. In the GA, called “additional data selection using GA” (ADSGA), the SPX crossover [155] is employed to generate new offspring. The method can be referred to as the hybridization of collocation methods and the nonlinear least-squares approach (cf. Section 3).

[^2]: The numerical solution of a stiff equation will be very time-consuming due to the fact that certain numerical methods for solving the equation are numerically unstable, unless the step size is taken to be extremely small.

In [101], a genetic algorithm with analog genetic encoding (AGE) [105] is developed to estimate the network topology and parameters in a biochemical network model from gene expression data. The analog genetic encoding exhibits some kinds of domain knowledge of the reverse engineering problem. The interpretation of an AGE solution allows simultaneous inference of model structure and numerical parameter values. In the paper, the state equations are written in a nonlinear dynamical model form as follows:

\[
\frac{dy_i}{dt}
=
\alpha_i \sigma\left(\sum_{j\in R_i}w_{ij}y_j\right)-\delta_i y_i,
\]

where \(y_i\) is the expression level of gene \(i\), \(\alpha_i\) is the maximum transcription rate, and \(\delta_i\) is the degradation rate. \(R_i\) is the set of regulators of gene \(i\) and \(w_{ij}\) represents the regulatory influence of gene \(j\) on gene \(i\), \(\sigma(\cdot)\) is the sigmoid function given by

\[
\sigma(x)=\frac{1}{1+e^{-x}}.
\]

The fitness function is defined as the least-square distance between the expression data generated from the target network and the inferred network. The AGE uses an implicit representation of the interaction between the metabolites that form the network, and allows operators such as duplication, deletion, and transpositions among genomes, which are crucial for the evolution and complexification of biological organisms. As studied in [68], proper incorporation of domain or prior knowledge can indeed improve the efficiency and effectiveness of GA. The study of the incorporation of domain and/or available knowledge of biological processes in GAs, as exemplified by the analog genetic encoding, remains an interesting topic of research.

The estimation problem of kinetic parameters in the S-system that describes a biochemical network is tackled in [58] by using an intelligent two-stage evolutionary algorithm. The S-system is first decoupled into a set of \(N\) subproblems. Each subproblem has \(2(N+1)\) parameters. These parameters are estimated by using an intelligent genetic algorithm (IGA). In an IGA, an intelligent crossover is proposed based on orthogonal array and factor analysis. After all the subproblems are optimized, the combination of these estimated parameters are considered as the initial solution of the orthogonal simulated annealing (OSA) algorithm. The fitness function for the \(i\)th gene is defined as follows:

\[
f(\mathbf{p})=
\sum_{t=1}^{T}
\left(
\frac{y^t(i)-y^t_{\exp}(i)}{y^t_{\exp}(i)}
\right)^2
+
c\sum_{j=1}^{N-I}(|g_{ij}|+|h_{ij}|),
\]

where \(c\) is the penalty weight and \(I\) is the maximum in-degree of the maximal number of genes that directly affect gene \(i\). Here, the penalty term exhibits a Laplace prior over the coefficients in the S-system, and can prevent overfitting. The Laplace prior is widely used in the statistical machine learning community for model selection [30]. Experimental comparison with a benchmark problem favors the proposed algorithm against SPXGA [76] (described below). The proposed intelligent genetic algorithm has been previously applied to the same problem as in [57]. The proposed two-stage approach greatly reduces the number of estimated parameters, which is good for any evolutionary search. However, in case that the parameters are highly interdependent, the solutions found may not be globally optimal.

The decoupling of S-systems for large network inference is also adopted in [80], where a coevolutionary algorithm is applied to estimate the entire set of kinetic parameters simultaneously. In the coevolutionary algorithm, a hybrid genetic algorithm (GA with local search) called GLSDC [79], evolves a cycle for each subproblem. The best solution so far is used as the estimated gene expression time-course. The estimated gene expression time-course data is updated at each iteration and used as a reference for the calculation of the fitness function in solving each subproblem.

In [120], the parameters including the network structure and sizing of the metabolic pathways modeled by Petri Net are estimated by using a genetic algorithm. In the GA, the Petri Net is represented as a discrete chromosome. The fitness function to be optimized is

\[
f(\mathbf{p})=
\sum_{i=1}^{n}\sum_{j=1}^{m}
\frac{|y^j(i)-y^j_{\exp}(i)|}{n_m n_p}
+
0.1n_r,
\]

where \(n_m\) is the number of metabolites, \(n_p\) is the number of time steps, and \(n_r\) is the number of reactions. In the developed algorithm, to evaluate an individual which represents a network structure, first a stochastic hill-climbing algorithm is applied to estimate the optimal network parameters given the network structure. Given the parameters, the fitness function can be evaluated. The proposed GA aims to find the optimal network structure. It can be seen that the proposed approach exhibits a hierarchical structure in which the underlying stochastic hill-climbing algorithm is responsible for parameter estimation with a fixed structure, while the structure is optimized in the higher level by using the GA. Moreover, to optimize the structure, Laplacian regularization [162] is adopted. The hierarchical approach may be more likely to locate the global optimum than the two-stage approach described above. However, the time-consuming nature of the underlying optimization algorithm will impede the (performance) efficiency of the whole algorithm.

In [123], the authors proposed to use a binary genetic algorithm for identifying gene deletion strategies for optimization of a desired phenotypic objective function. In the binary GA, an individual component is used to indicate that the corresponding gene is effective in describing the biochemical process. The one-point, two-point, and uniform crossover operators were tested in the applied binary GA, while the mutation operator used was flap-mutation. The fitness function can be calculated by using flux balance analysis, minimization of metabolic adjustment (MOMA), and regulatory on-off minimization (ROOM).

In [76], the estimation of S-systems parameters is based on a real-coded genetic algorithm, where the fitness function \(f(\mathbf{p})\) is the relative squared error

\[
\sum_{ij}
\left(
\frac{|y^j(i)-y^j_{\exp}(i)|}{|y^j_{\exp}(i)|}
\right)^2
+
cnT
\left\{
\sum_{i,j}|g_{ij}|+\sum_{i,j,i\neq j}|h_{ij}|
\right\},
\]

where \(c\) is the weighted coefficient that balances the two evaluation terms. In the real-coded GA, the simplex crossover developed by Tsutsui et al. [155] and Higuchi et al. [56], known as SPX, was applied. Moreover, to efficiently search for the large number of parameters, a gradual optimization strategy was employed. Though the gradual optimization strategy can gradually optimize for a large-scale networks, this procedure could be very time-consuming.

In [112], the authors presented the network-structure search evolutionary algorithm (NSS-EA) for inference of genetic networks modeled by the S-systems. NSS-EA efficiently finds multiple different network structures which explain gene-expression time-course data observed in biological experiments since, in general, it is difficult to obtain sufficient time-course data by which a network structure can be determined uniquely. In this paper, the authors try to solve the above problems by explicitly separating the process of searching network structure, i.e., searching the signs of the parameters of the S-system, and that of searching the values of the system parameters. Through some numerical experiments, the authors showed that the proposed method, NSS-EA, can efficiently find more different kinds of network structures than some conventional methods. This search for multiple solutions is of great importance since the experimental data are usually not sufficient in practice. This provokes the so-called parameter identifiability problem, which will be described in Section 5. Moreover, optimization algorithms [69] which have been specifically developed for optimizing multiple peak problems (problems with multiple global optima) should be adopted.

Early work on the application of GA to the parameter estimation problem, such as [152] and [48], the classical GA was adopted. In [152], GA was used to estimate the parameters of the S-system. The interesting contribution is that if some parameters is less than a given threshold, the value is reset to zero in subsequent generations (called structure skeletalizing). The structure skeletalizing aims to search for a sparse network. In [48], classical GA was applied to optimize for a metabolic pathway. Since only simple GAs are applied in these papers, the shortcomings of the conventional GA are inherited. Without doubt, these algorithms need to be improved.

Recent work on the parameter estimation problem using GA indicates that proper incorporation of biologists’ expert knowledge can indeed improve the search efficiency of GAs and this should be emphasized in the future research. The incorporation of expert knowledge could be implemented by proposing new solution representations, new reproduction operators, new search strategies, and so on. Indeed, expert knowledge should also be considered as much as possible in the design of any metaheuristics for parameter estimation problems.

### 4.3 Evolution Strategies and Evolutionary Programming

Though evolution strategies and evolutionary programming are both different variants of EA, it is becoming harder to distinguish them. Hence, we organize their application to the parameter estimation problem together.

As studied in [108], a set of metaheuristics, including the direct multilevel coordinate search algorithm (MCS) method implemented in Matlab, the improved controlled random search (ICRS) method, differential evolution, unconstrained evolution strategy (uES), evolution strategy using stochastic ranking (SRES) [135], and CMA-ES [54], have been compared with each other. The experimental results show that only evolutionary strategies, namely the SRES and uES methods, were able to successfully solve several examples of the parameter problem. This implies that evolutionary strategies might be the most competitive stochastic optimization method, especially for large problems.

In [134], the state of the gene regulatory networks for cellular morphogenesis is updated as follows:

\[
a_i(t+1)=\sigma\left(\sum_{j=1}^{N}w_{ij}a_j(t)-\theta_i\right),
\]

where \(w_{ij}\) is the level of the interaction from node \(j\) to node \(i\), \(\theta_i\) is the activation threshold for node \(i\), and \(\sigma(\cdot)\) is the sigmoid function. A \((1+1)\)-ES was adopted to minimize the fitness function

\[
f=\frac{625}{1+\sum_{t=1}^{T}\epsilon(t)},
\]

where

\[
\epsilon(t)=dr(t)+\sqrt{\frac{1}{N(t)}\sum_{i=1}^{N(t)}(dr_i(t)-dr(t))^2},
\]

with the summation over the \(N\) exterior cells.

In [84], the already-compared stochastic algorithms in [108] were applied to solve the parameter estimation problem in a biological pathways model. Due to the fact that the lower and upper bounds of the parameters are quite large \([10^{-12},10^{12}]\) (as is often the case in parameter estimation), a uniform sampling technique, i.e., the transforming of the parameter \(p_j\), was proposed as follows:

\[
p_j^{*}=-10^{p_j}-\mathrm{offset}_j,
\]

where \(\mathrm{offset}_j=\max\{\epsilon,-2L_j\}\) and \(L_j\) is the lower bound. The authors combined the strategy into several evolutionary algorithms, and claimed that nonuniform sampling can improve both the speed and robustness of the SRES and DE. We can take advantage of the nonuniform sampling strategy to deal with large-scale optimization problems.

A self-adaptive evolution strategy has been applied to metabolic flux analysis with the incorporation of singular value decomposition technique [165]. In their paper, the metabolic flux analysis is modeled as an error minimization problem. To decrease the high dimensionality of the problem, a singular value decomposition is applied to reduce the number of dimensions of the fluxes. In the self-adaptive evolution strategy, a log-normal distribution is applied to mutate current solution.

A self-adaptive scouting algorithm has been developed [102] in the context of optimizing the experimental design of a systems biology problem. The evolution strategy uses an adaptive mutation strength and population size. An offspring is created from the parent by adding a normally distributed value with mean zero and standard deviation \(\sigma\). The deviation \(\sigma\) is varied during the evolutionary search. Given the current solution value \(s\) and the current mutation strength \(\sigma\), the mutation strength is adapted as

\[
\sigma = \sigma e^{\hat{s}-s}/\hat{s},
\]

where \(\hat{s}\) is the average solution values over all past experiments. Moreover, at generation \(t\), the population size is increased until the fitness value of a generated solution is larger than

\[
\Theta(t)=\frac{1}{t-1}\sum_{k=1}^{t-1}s_{2;\lambda_k}^{k}
\qquad \text{for } g>1,\; \Theta(1)=0,
\]

where \(s_{2;\lambda_k}^{k}\) is the second-best individual out of the \(\lambda_k\) individuals of generation \(k\).

### 4.4 Genetic Programming (GP)

Genetic programming has been applied to find the optimal structure and sizing of chemical reaction network and gene regulatory network modeled by Petri Nets [85], [81] based on observed time-domain data. In [81], the GP’s chromosomes are encoded not only for Petri Nets but also for rate constants that the nets represented and thus the GP can evolve for both the PN’s structure and the rate constants.

A variant of GP, called grammatical evaluation [121], for parameter estimation in nonlinear gene interactions modeled by Petri Nets has been developed in [109], [110], [111]. The Petri Net is described by a Backus-Naur Form (BNF) grammar. The fitness function is determined by comparing the high risk and low risk assignments made by the Petri Net to those from the given nonlinear gene-gene interaction model.

The application of GP is specifically suitable for structure learning. It would be interesting to apply genetic programming to the estimation problem of the S-system. To our knowledge, we do not see many applications, except [104]. In [104], a developed GP is applied to estimate the S-system parameters of genetic networks.

In [151], the authors compared ES and GP for inferring gene regulatory networks from observed time series data of gene expression with respect to their performance on multiple problem instances with varying parameters. The authors showed that single problem instances are not sufficient to prove the effectiveness of a given strategy. Moreover, the GP approach is less prone to varying instances than the ES approach.

### 4.5 Differential Evolution

As described previously, traditional different evolution algorithms [150] have been applied [108], [132] to the parameter estimation problem. These studies have shown that DE performs very well, if not the best. Besides these DEs, the hybridization of DEs and local search algorithms has been developed in systems biology.

In [117] and [119], the authors developed the memetic differential evolution (memDE) to estimate parameters of gene regulatory networks modeled by S-systems. In the algorithm, the AIC criterion and Laplacian regularization are used to carry out model selection. In memDE, the differential evolution algorithm is combined with local search heuristics, which not only can improve the solution quality but also can decrease computational time.

In [118], a trigonometric differential evolution (TDE) [42] combined with a greedy local search is developed to estimate the parameters of a decoupled S-system. For a S-system that models biochemical networks, it can be decoupled to a set of subproblems, with a linear spline interpolation. The parameters of the \(i\)th subproblem is solved by the TDE with local search, in which the fitness function is defined as the relative square error with an AIC penalty term.

In [154], the parameter estimation problem of nonlinear dynamic biological systems are tackled by a hybrid differential evolution algorithm. The authors first applied the modified collocation method to convert the differential equations into a system of algebraic equations. The observed time series data are then substituted into the algebraic equations to decouple system interactions in order to obtain the approximate model profiles. The developed algorithm is not only suitable for parameter estimation, but also for structure identification.

### 4.6 Multiobjective Approaches

In [53], a comprehensive review of the application of multiobjective optimization in bioinformatics and computational biology is given. Please refer to this paper and the references therein. In this section, we focus specifically on using the multiobjective approach for parameter estimation.

In [51], a multiobjective approach, called MoPSwarm, which is based on particle swarm optimization (PSO) [74], was developed and applied to the parameter estimation problem in the ERK signaling pathway. In [130], the multiobjective approach based on the hybridization of GA and simplex method was developed for the parameter estimation of the rice flowering time model, in which the objective functions are the mean squared errors between the model solution and the actual data for flowering dates and the mRNA levels for short-day and long-day periods.

In [59], the author applied a multiobjective optimization algorithm, called MO-CMA-ES [63], to the parameter estimation problem associated with the segment polarity network of *drosophila*. The authors decomposed the single objective function that measures the deviation between the desired outcome and the experimental data into six different objectives w.r.t the three different genes and two different characteristics. The comparison with the single-objective strategy on the exploration of parameters showed the superiority of the multiobjective strategy.

In [94], [95], to address the S-system structure learning problem, the authors formulated the inference problem using a multiobjective approach to minimize simultaneously the concentration error \(J_1\), slope error \(J_2\), and an interaction measure \(J_3\)

\[
J_1=
\frac{1}{nm}
\sum_{i=1}^{n}\sum_{j=1}^{m}
\frac{(y^j_{\exp}(i)-y^j(i))^2}{\max_j\{y^j_{\exp}(i)\}},
\]

\[
J_2=
\frac{1}{nm}
\sum_{i=1}^{n}\sum_{j=1}^{m}
\frac{(\dot{y}^j_{\exp}(i)-\dot{y}^j(i))^2}{\max_j\{\dot{y}^j_{\exp}(i)\}},
\]

\[
J_3=
\sum_{i=1}^{n}\sum_{j=1}^{I}(|g_{ij}|+|h_{ij}|),
\]

where \(\dot{y}_{\exp}(i)\) is the approximate experimental slope (using Lagrange polynomial fitting) for the \(i\)th component, and \(I\) is a set of cardinal numbers indicating which kinetic orders should be pruned. The \(\epsilon\)-constraint method is proposed to transform the multiobjective formulation to a constrained optimization problem. The hybrid differential evolution algorithm [33] is then applied to solve the constrained optimization problem. The proposed algorithm was illustrated by application on a small-scale gene network and a kinetics model of ethanol fermentation, and showed promising performance.

To the best of our knowledge, multiobjective approaches have not been widely applied in parameter estimation. However, this approach provides us a possibility to incorporate as much as possible useful information in the model calibration process. For example, besides information like slope and the experimental data as used in [94], other information such as possible structure of the S-system could also be incorporated by using the multiobjective approach.

### 4.7 Hybrid Strategies

To carry out effective search, the hybrid strategy, i.e., the combination of different metaheuristics, has been considered one of the most promising paradigms [55]. Hybrid strategies were also developed and applied for the parameter estimation problem. In [16], the evolutionary search strategy is combined with a local multiple-shooting approach. SRES [135] or DE [150] is first applied to optimize the objective function, the multiple-shooting approach is then employed when the evolutionary algorithm has been converged. The solution found by the EA is employed as the starting point of the multiple-shooting approach. The transition from the local to global search is determined by a switching strategy rather than empirically as in [133]. The approach is an improved method to that developed in [17]. The experimental results show that the proposed algorithm significantly improves the multiple-shooting approach as developed in [124]. However, one of the drawbacks of the developed algorithm is that it is possible that the EA cannot reach the attraction basin of the global optimum. This will cause the failure of the search.

In [96], [97], [160], the authors developed a hybrid DE algorithm with geometric mean mutation to avoid generating individuals that are near the parameter search bound. The developed algorithm is applied to an inverse problem and show that the developed algorithm outperforms some compared algorithms. The developed hybrid DE algorithm has also been applied to carry out the inference of gene regulatory network using S-system in [98].

In [133], SRES is hybridized with several local search methods, such as DN2GB, NOMADm, and NEWUOA, to develop a robust parameter estimation in biochemical pathways. The switching strategy is determined empirically. In the developed algorithm, the objective function is given by

\[
f=
\sum_{i=1}^{m}\sum_{j=1}^{n}
\frac{(y^j_{\exp}(i)-y^j(i))^2}{2s_{ij}^{2}},
\]

where \(s_{ij}\) is the normalization term (i.e., the weighted least squares criterion).

In [164], the genetic regulation network is represented through a recurrent neural network formulation as follows:

\[
\tau_i\frac{de_i}{dt}
=
\sigma\left(
\sum_{j=1}^{N} w_{ij}e_j
+
\sum_{k=1}^{K} v_{ik}u_k
+
\beta_i
\right)
-\lambda_i e_i,
\]

where \(e_i\) is the gene expression level for the \(i\)th gene (\(1 \le i \le N\), \(N\) is the number of genes in the system), \(\sigma(\cdot)\) is a nonlinear function (usually a sigmoid function), \(w_{ij}\) represents the effect of the \(j\)th gene on the \(i\)th gene, \(u_k\) is the \(k\)th (\(1 \le k \le K\), \(K\) is the number of external variables) external variable, which could represent the externally added chemicals, nutrients, or other exogenous inputs, \(v_{ik}\) represents the effect of the \(k\)th external variable on the \(i\)th gene, \(\tau\) is the time constant, \(\beta\) is the bias term, and \(\lambda\) is the decay rate parameter. The formulation is described in a discrete term with some simplification to simulate the predication outputs as follows:

\[
e_i(t+\Delta t)
=
\frac{\Delta t}{\tau_i}
f\left(\sum_{j=1}^{N}w_{ij}e_j(t)+\beta_i\right)
+
\left(1-\frac{\Delta t}{\tau_i}\right).
\]

The fitness function is defined to measure the deviation of the network output \(e(t)\) from the real measurement (target) \(d(t)\), written as

\[
f(\mathbf{p})=
\frac{1}{TN}\sum_{t=0}^{T}\sum_{i=1}^{N}(e_i(t)-d_i(t))^2,
\]

where \(T\) is the number of time slots. The hybridization of differential evolution and particle swarm optimization, which has been developed by Zhang and Xie [172], is then employed to solve the problem.

In [77], the authors developed a multistage evolutionary algorithm for estimating the parameters of the S-system, which is used to model the biochemical pathway dynamics. In the developed algorithm, the first stage involves a genetic programming [22] (available software can be found in GPLib library http://www.cs.bham.ac.uk/~cmf/GPLib/GPLib.html) which is used to fit the curve of the experimental data. The second stage uses a hybridization of genetic algorithm and \((1+1)\)-ES with combined binary and real solution representation to estimate both the gene network structure and the parameters of the S-system. The objective function in GP regression is defined as

\[
f(\mathbf{p})=
\sum_{i=1}^{n}\sum_{t=1}^{t_N}
\left(
\frac{\dot{y}_i(t)-\dot{y}^{\,i}_{\exp}(t)}
{\dot{y}_i(t)}
\right)^2.
\]

Binary coding for representing the S-system structure and real vector for parameter values of the S-System are combined into a single chromosome. The objective function used in searching the network structure and parameters are defined as

\[
f(\mathbf{p})=
\sum_{i=1}^{n}\sum_{t=1}^{t_N}
\ddot{y}_i(t)
\left(
\frac{\dot{y}^{\,i}(t)-\dot{y}^{\,i}_{\exp}(t)}
{\dot{y}^{\,i}(t)}
\right)^2,
\]

where \(\dot{y}\) is the gradient calculated based on the GP regression, \(\ddot{y}\) is second-order differentiation, and \(\dot{y}\) is the calculated value of each equation in the S-system. The second-order differentiation is multiplied to each term of the evaluation function in order to make it easy to fit the data points with large second-order differentiation. A row exchange crossover and classical mutation operators are employed to produce new offspring with hopefully good structure. The restricted tournament selection (RTS) developed in the GPLib library is employed to prevent premature convergence. As has been seen in previous work on S-system structure learning, the objective function adopted in [77] may result in an overfitting structure due to the lack of model selection criterion.

A similar approach as described above has been applied in [8] for optimizing just the parameters of the S-system. Genetic programming is used as a data regression method, where the coefficients of the regression model are estimated by a least-mean-squares (LMS) approach. The fitness function in [8] is different from that of [77], in which a regularization term based on the minimum description length (MDL) criterion for model selection. The fitness function is defined as follows:

\[
f(\mathbf{p})=
\sum_{i=1}^{n}\sum_{t=1}^{t_N}
(y^i(t)-y^i_{\exp}(t))^2
+\alpha m,
\]

where \(m\) is the number of parameters, and \(\alpha\) is the weight constant.

In [147], a hybrid method with genetic algorithm and an evolution strategy is developed to estimate the topology and parameters of the S-system. The genetic algorithm evolves the network structure, while the evaluation of each structure is based on the evolution strategy. The evolution strategy is applied to find optimal parameters with respect to each network structure. In evaluating the fitness of a trial parameter vector, the fitness function is defined as the relative squared residue/error. This method is similar to the hierarchical approach developed in [120]. Due to the use of ES in evaluating a candidate S-system structure, the proposed algorithm will be inevitably time-consuming and be of stochastic nature.

A similar method to [147] has been developed for biochemical network construction and parameter estimation in [90]. In the developed algorithm, a new mutation operator, the duplication operator of a species with all its reactions, has been developed and studied. The fitness function is defined with a penalty term to represent AIC for model selection as follows:

\[
N\log\left(
\frac{1}{CS}
\sum_{c,i,j}
\frac{(x_{c,i}(t_j)-y_{c,i}(t_j))^2}{m_{c,i}}
\right)
+
2\frac{N}{N-k-1},
\]

where

\[
m_{c,i}=\sum_{j=1}^{T}(x_{c,i}(t_j)+y_{c,i}(t_j)),
\]

\(x\) is the resulting time series and \(y\) is the target time series data. Here, \(S\) is the number of evaluated species, \(C\) is the number of fitness cases, and \(k\) is the number of parameters to be estimated.

### 4.8 Comparison of Optimization Methods

According to the No Free Lunch theorem [163], “for any algorithm, any elevated performance over one class of problems is exactly paid for in performance over another class.” However, the various parameter estimation problems in systems biology have similar characteristics, and we can loosely categorize these problems in the same class. This makes the performance comparison between various optimization algorithms meaningful and necessary.

In most of the papers reviewed, the authors compare their newly proposed algorithm(s) with selected other metaheuristics. However, comprehensive comparisons among existing metaheuristics can provide more profound and objective understanding of the relative benefits of various metaheuristics. In [108] and [125], different optimization methods have been compared in solving the inverse problem. The authors concluded that global statistical approaches such as evolution strategies, genetic algorithms, and simulated annealing perform better than other local methods, especially the gradient-based methods.

In [148], the authors provided an genetic algorithm framework so that different reproduction operators of a genetic algorithm can be compared systematically. They concluded that “evolutionary algorithms are well suited for the problem of network inference.” In [146], seven metaheuristics, including five hybrid EAs and two classical EAs were implemented and compared in the parameter estimation problem of several gene regulatory networks. The authors concluded that pure EAs are powerful enough only to analyze very small-scale systems, while hybrid EAs are suitable for large networks.

However, only a small fraction of the existing metaheuristics have been compared in these studies. Moreover, different variants of specific metaheuristics should also be compared with each other. Other global optimization methods, such as hybrid metaheuristics, multiobjective methods, should also be included in the comparison. It is also interesting to see that the comparison can provide some guiding rules on the selection of most appropriate metaheuristics for parameter estimation problems with specific characteristics. However, to the best of our knowledge, no such comprehensive reviews of metaheuristics have yet been published.

According to the existing comparison results that are available, and based on our personal experience, for small and/or medium size parameter estimation problems, we recommend ES and DE as the starting point when parameter estimation problems have real parameters, while we recommend GP to deal with the structure learning requirement (such as in S-systems) associated with parameter estimation problems. For large size problems, specific divide-and-conquer techniques are required, although how to combine the suboptimal solutions of the divided subproblems into the optimal solution for the original problems is very important. Moreover, to increase the effectiveness and efficiency of metaheuristics, we believe hybridization with classical optimization algorithms should be given more attention. However, these are very tentative observations and should not be taken as evidence to exclude examination of other techniques. Essentially, it is not yet possible to make any definitive statements about which technique(s) to use in a given problem type: this remains a matter of open research.

### 4.9 Software Availability

Gepasi [106] provides a variety of implementations of deterministic and stochastic algorithms for the inverse problem in systems biology. Local and deterministic algorithms include Hooke and Jeeves [60], L-BFGS-B, Levenberg-Marquardt (L-M), Nelder and Mead (N& M), Praxis (Pr), Steepest Descent (StD), and Truncated Newton (TN). The stochastic algorithms include simulated annealing, genetic algorithms, evolutionary programming, multistart, and random search (RS).

COPASI [61] is a platform-independent and user-friendly biochemical simulator that offers a range of optimization methods. It is an improved version of Gepasi, which is available at http://www.copasi.org.

Besides COPASI and Gepasi, Matlab functions for the SRES and DE methods used in the papers described above are available from the following URLs:

- http://www.cs.princeton.edu/~stevenk/optimization
- http://www.bioanalyticsgroup.com/default-files/

Moreover, a set of classical and metaheuristic algorithms are available from SBML toolbox (http://www.sbml.org).

---

## 5 DISCUSSION AND FUTURE DIRECTIONS

As discussed in the overview of systems biology [82], [83], the process of model building in systems biology can be organized as a cycle (see Fig. 7). Models that have been initially developed need to be analyzed. Parameter estimation is performed to make the model work in terms of current knowledge (preliminary data, basic hypothesis, known a priori, knowledge). The current model must be validated with new experiments. Usually deficiencies of the current model will be exposed. The current model should be modified accordingly or even in the worse case, reconstructed. The process is repeated iteratively until the model is well validated.

After the parameter estimation step, the specified model needs to be validated. To validate the model effectively, the optimal experimental design (OED) problem emerges. The purpose of OED is to select a set of experiments that are maximally informative. The measure of the informativeness is based on the Fisher Information Matrix, interested readers are referred to [156], [25], [122] for details. Searching for OED in systems biology by using metaheuristics is in its very infancy. In [20], the OED is formulated as a dynamic optimization problem. Rather than using a sequential quadratic programming (SQP) approach, a hybridization of integrated controlled random search [19] and differential evolution is applied, and illustrated through application to several biological process models. Improved versions of the developed algorithm are developed and applied to different models in [133] and [15], respectively. Much work needs to be done in this area.

Another important problem is the parameter identifiability problem [11], [12], [93], [171]. The study of identifiability can help to determine the unidentifiable parameters. The incorporation of identifiability analysis in the parameter estimation process could improve the efficiency of any metaheuristic search technique being applied.

**Fig. 7.** Closed-loop learning is a process for making discoveries using the minimal amount of research effort, that involves close and frequent feedback between experimental observations and theoretical modeling.

### 5.1 Future Research Directions

As we have described, metaheuristics have been developed and applied for various optimization problems in systems biology, and have achieved great success. However, more research studies should be carried out. The following is a list of possible areas of interest in which, we believe, it will be useful to direct research efforts:[^3]

[^3]: It is not intended to be exhaustive.

- **In modeling gene regulatory networks by S-systems and/or Petri Nets**, it can be seen that not only the parameters (the number of which is the order of \(n^2\)) but also the network structure are to be estimated. Even for a medium-size network, the estimations for the structure and the parameters are extremely difficult. Developed strategies to deal with this problem are:
  1. incorporating a priori knowledge about the network structure, e.g., [105], but a priori knowledge is not usually available;
  2. first decoupling the S-systems parameter estimation problem into a set of subproblems, and then either learn the structure and the parameters in two stages (see [80]) or coevolve them simultaneously;
  3. applying Laplacian regularization or Bayesian information criterion on the fitness function for selecting optimal network structure and parameters simultaneously,[^4] e.g., [13], [76], [105], [120];
  4. taking the network structure learning process to carry out individual fitness evaluation, and using the metaheuristics for the parameter estimation (i.e., a hierarchical estimation strategy), e.g., [120];
  5. coevolving the parameters and the structure simultaneously by encoding the parameters and the structure in a whole, e.g., [81], [104].

  From our point of view, the hierarchical structure (e.g., adopted in [120]), the two-stage structure (e.g., in [58]) and the coevolution of the parameters and the structure with fitness regularization have higher potential than the other options. More studies should be carried out to improve the network structure and parameter estimation of both S-systems and Petri-Nets.

[^4]: By applying Laplacian regularization and BIC, the network structure will be automatically learned while the network arcs without enough support will be pruned out during the search.

- **To carry out parameter estimation using metaheuristics, the fitness function plays an important role.** However, it is very likely that the evaluation of solutions is in dynamic and/or uncertain environment. There are two possible reasons. One possible reason is due to the uncertainty of the experimental data since these data sets usually have missing data, measurement errors or noise, with the following possible causes:
  - instrumental calibration and physical limitations of devices;
  - human carelessness.

  Another reason lies in the solution to the biology models. For example, in stochastic modeling (as discussed in [153]) and some ODE systems, the predictions of such models are of stochastic nature.

  Very few algorithms have been specifically developed to take the measurement errors/noise, the missing mechanisms and the stochastic environment into consideration. In these uncertain environments, conventional approaches are not appropriate since they are usually based on exact solution evaluations. There are a variety of methods available to deal with optimization under highly uncertain environments. One approach is to hybridize the collocation methods with the least-squares methods. The collocation method could be used to smooth the experimental data, so that the noise and missing values can be imputed. Another approach is to develop and apply those metaheuristics specifically designed for uncertain environments (e.g., the EAs proposed in [167]). An alternative is to apply Bayesian methods [159], [92] so that posterior distributions rather than a “point” estimate of the parameters would be obtained. Yet another would be to use a fuzzy approach to represent uncertainty in the parameters being optimized [113], although the use of fuzzy methods in this context has been limited to date—see [67] for a recent review of fuzzy methods in systems biology or [136] for a detailed coverage of fuzzy methods in general.

- **It is surely important to increase efficiency and to guarantee robustness of the metaheuristics.** From our point of view, the best way is to adopt hybrid approaches. More work needs to be done in this direction.

- **The application of multiobjective approaches to incorporate domain and/or expert knowledge in the parameter estimation is promising.** So far, this approach has not been much investigated.

- **In case that the ODEs used to model the biological processes are stiff**, it is then time-consuming to compute the solutions of the model due to iterative numerical integrations with extremely small step sizes. As a consequence, the fitness calculations will be time-consuming. To deal with such a problem, one possible approach is to use surrogate model-based metaheuristics, e.g., [28], [173]. Such surrogate metaheuristics could also be applied in the optimal design of experiments, model validation, and model selection.

- **In addition to the mentioned metaheuristics, new methods are needed.** For example, scatter search [41] has shown promising results [40], [133].

---

## 6 CONCLUSION

In this paper, we have reviewed the application of current metaheuristic approaches to the parameter estimation problem in systems biology. Important issues in solving the parameter estimation problem are discussed. Possible research directions are listed. We hope the review will provide helpful insight into the application of metaheuristics, and hence attract more attention from computer scientists to this interesting and challenging research domain.

---

## REFERENCES

[1] A. Abraham, C. Grosan, and H. Ishibuchi, *Hybrid Evolutionary Algorithms*. Springer, 2007.  
[2] M.A. Abramson, C. Audet, and J.E. Dennis, “Generalized Pattern Searches with Derivative Information,” *Math. Programming*, vol. 100, no. 1, pp. 3-25, 2004.  
[3] B.S. Adiwijaya, P.I. Barton, and B. Tidor, “Biological Network Design Strategies: Discovery through Dynamic Optimization,” *Molecular Biosystems*, vol. 2, no. 12, pp. 650-659, 2006.  
[4] C.M. Alexandre and L. Hennig, “FLC or Not FLC: The Other Side of Vernalisation,” *J. Experimental Botany*, vol. 52, pp. 1127-1135, 2008.  
[5] R. Alfieri, E. Mosca, I. Merelli, and L. Milanesi, “Parameter Estimation for Cell Cycle Ordinary Differential Equation (ODE) Models Using a Grid Approach,” *Proc. HealthGrid 2007, Studies in Health Technology and Informatics*, vol. 126, pp. 93-102, 2007.  
[6] J.S. Almeida and E.O. Voit, “Neural-Network-Based Parameter Estimation in S-System Models of Biological Networks,” *Genome Informatics*, vol. 14, pp. 114-123, 2003.  
[7] U. Alon, *An Introduction to Systems Biology*. Chapman and Hall, 2006.  
[8] S. Ando, E. Sakamoto, and H. Iba, “Evolutionary Modeling and Inference of Gene Network,” *Information Science*, vol. 145, pp. 237-259, 2002.  
[9] I. Arisi, A. Cattaneo, and V. Rosato, “Parameter Estimate of Signal Transduction Pathways,” *BMC Neuroscience*, vol. 7, 2006, doi:10.1186/1471-2202-7-S1-S6.  
[10] N. Arora and L.T. Biegler, “A Trust Region SQP Algorithm for Equality Constrained Parameter Estimation with Simple Parameter Bounds,” *Computational Optimization and Applications*, vol. 28, pp. 51-86, 2004.  
[11] M. Ashyraliyev, J. Jaeger, and J.G. Blom, “Parameter Estimation and Determinability Analysis Applied to drosophila Gap Gene Circuits,” *BMC Systems Biology*, vol. 2, article 83, 2008.  
[12] S. Audoly, G. Bellu, L. D’Angiò, M.P. Saccomani, and C. Cobelli, “Global Identifiability of Nonlinear Models of Biological Systems,” *IEEE Trans. Biomedical Eng.*, vol. 48, no. 1, pp. 55-65, Jan. 2001.  
[13] C. Auliac, V. Frouin, X. Gidrol, and F. D’Alche-Buc, “Evolutionary Approaches for the Reverse-Engineering of Gene Regulatory Networks: A Study on a Biologically Realistic Dataset,” *BMC Bioinformatics*, vol. 9, article 91, 2008.  
[14] C.T.H. Baker, G.A. Bocharov, J.M. Ford, P.M. Lumb, S.J. Norton, C.A.H. Paul, T. Junt, P. Krebs, and B. Ludewig, “Computational Approaches to Parameter Estimation and Model Selection in Immunology,” *J. Computational and Applied Math.*, vol. 184, pp. 50-76, 2005.  
[15] E. Balsa-Canto, A.A. Alonso, and J.R. Banga, “Computational Procedures for Optimal Experimental Design in Biological Systems,” *IET Systems Biology*, vol. 2, no. 4, pp. 163-172, July 2008.  
[16] E. Balsa-Canto, M. Peifer, J.R. Banga, J. Timmer, and C. Fleck, “Hybrid Optimization Method with General Switching Strategy for Parameter Estimation,” *BMC System Biology*, vol. 2, no. 26, pp. 1-9, 2008.  
[17] E. Balsa-Canto, V. Vassiliadis, and J. Banga, “Dynamic Optimization of Single- and Multi-Stage Systems Using a Hybrid Stochastic-Deterministic Method,” *Industrial and Eng. Chemistry Research*, vol. 44, no. 5, pp. 1514-1523, 2005.  
[18] J.R. Banga, “Optimization in Computational Systems Biology,” *BMC Systems Biology*, vol. 2, article 47, 2008.  
[19] J.R. Banga and J.J. Casares, “Integrated Controlled Random Search: Application to a Wastewater Treatment Plant Model,” *Proc. IChemE Symp. Ser.* 100, pp. 183-192, 1987.  
[20] J.R. Banga, K.J. Versyck, and J.F. Van Impe, “Computation of Optimal Identification Experiments for Nonlinear Dynamic Process Models: A Stochastic Global Optimization Approach,” *Industrial and Eng. Chemistry Research*, vol. 41, no. 10, pp. 2452-2430, 2002.  

[21] H.T. Banks, H.T. Tran, and D. Gulick, *Mathematical and Experimental Modeling of Physical and Biological Processes*. Chapman and Hall, 2009.  
[22] W. Banzhaf, P. Nordin, R.E. Keller, and F.D. Francone, *Genetic Programming: An Introduction: On the Automatic Evolution of Computer Programs and Its Applications*. Morgan Kaufmann, 1998.  
[23] P. Berman, B. DasGupta, and E. Sontag, “Computational Complexities of Combinatorial Problems With Applications to Reverse Eng. of Biological Networks,” *Advances in Computational Intelligence: Theory & Applications*, pp. 303-316, World Scientific, 2006.  
[24] D. Braun, S. Basu, and R. Weiss, “Parameter Estimation for Two Synthetic Gene Networks: A Case Study,” *Proc. IEEE Int’l Conf. Acoustics, Speech, and Signal Processing*, vol. 5, pp. 769-772, 2005.  
[25] M. Brown, F. He, and L.F. Yeung, “Robust Measurement Selection for Biochemical Pathway Experimental Design,” *Proc. The First Int’l Symp. Optimization and Systems Biology*, pp. 259-266, Aug. 2007.  
[26] C.G. Broyden, “The Convergence of a Class of Double-Rank Minimization Algorithms,” *J. Inst. of Math. and Its Applications*, vol. 6, pp. 76-90, 1970.  
[27] M. Brusco and S. Stahl, “Branch-and-Bound Applications in Combinatorial Data Analysis,” *Ser. Statistics and Computing*, Springer, 2005.  
[28] D. Buche, N.N. Schraudolph, and P. Koumoutsakos, “Accelerating Evolutionary Algorithms with Gaussian Process Fitness Function Models,” *IEEE Trans. Systems, Man and Cybernetics, Part C: Applications and Rev.*, vol. 35, no. 2, pp. 183-194, May 2005.  
[29] A.P. Burgard, P. Pharkya, and C.D. Maranas, “OptKnock: A Bilevel Programming Framework fo Identifying Gene Knockout Strategies for Microbial Strain Optimization,” *Biotechnology and Bioeng.*, vol. 84, no. 6, pp. 647-657, 2003.  
[30] G.C. Cawley and N.L.C. Talbot, “Preventing Over-Fitting during Model Selection via Bayesian Regularisation of the Hyper-Parameters,” *J. Machine Learning Research*, vol. 8, pp. 841-861, 2007.  

[31] Y.J. Chang and N.V. Sahinidis, “Optimization of Metabolic Pathways under Stability Considerations,” *Computers and Chemical Eng.*, vol. 29, no. 3, pp. 467-479, 2005.  
[32] C. Chaouiya, “Petri Net Modelling of Biological Networks,” *Briefings in Bioinformatics*, vol. 8, pp. 210-219, 2007.  
[33] J.P. Chiou and F.S. Wang, “Hybrid Method of Evolution Algorithms for Static and Dynamic Optimization Problems with Application to a Fedbatch Fermentation Process,” *Computers and Chemical Eng.*, vol. 23, pp. 1277-1291, 1999.  
[34] I-C. Chou, H. Martens, and E.O. Voit, “Parameter Estimation in Biochemical Systems Models with Alternating Regression,” *Theoretical Biology and Medical Modelling*, vol. 3, no. 25, pp. 1-11, 2006.  
[35] A.R. Conn, N. Gould, and P.L. Toint, “A Globally Convergent Augmented Lagrangian Algortithm for Optimization with General Constraints and Simple Bounds,” *SIAM J. Numerical Analysis*, vol. 28, no. 2, pp. 545-572, 1991.  
[36] A.R. Conn, N. Gould, and P.L. Toint, “A Globally Congergent Lagrangian Barrier Algorithm for Optimization with General Inequality Constraints and Simple Bounds,” *Math. of Computation*, vol. 66, no. 217, pp. 261-288, 1997.  
[37] M. Dasika, A. Gupta, and C. Maranas, “A Mixed Integer Linear Programing (milp) Framework for Inferring Time Delay in Gene Regulatory Networks,” *Proc. Pacific Symp. Biocomputing*, pp. 474-486, 2004.  
[38] M.S. Dasika and C.D. Maranas, “Optcircuit: An Optimization Based Method for Computational Design of Genetic Circuits,” *BMC Systems Biology*, vol. 2, article 24, 2008.  
[39] M.J. Dunlop, E. Franco, and R.M. Murray, “A Multi-Model Approach to Identification of Biosynthetic Pathways,” *Proc. Am. Control Conf.*, pp. 1600-1605, July 2007.  
[40] J.A. Egea, M. Rodriguez-Fernandez, J.R. Banga, and R. Marti, “Scatter Search for Chemical and Bio-Process Optimization,” *J. Global Optimization*, vol. 37, pp. 481-503, 2007.  
[41] M. Laguna, F. Glover, and R. Marti, *Advances in Evolutionary Computation: Theory and Applications*, pp. 519-537. Springer-Verlag, 2003.  
[42] H.-Y. Fan and J. Lampinen, “A Trigonometric Mutation Operation to Differential Evolution,” *J. Global Optimization*, vol. 27, no. 1, pp. 105-129, 2003.  
[43] D. Fell, *Understanding the Control of Metabolism*. Portland Press, 1997.  
[44] J. Fisher and T.A. Henzinger, “Executable Cell Biology,” *Nature Biotechnology*, vol. 25, no. 11, pp. 1239-1249, 2007.  
[45] R. Fletcher, *Practical Methods of Optimization*. Wiley, 2000.  
[46] K.G. Gadkar, F.J. Doyle, and J.S. Edward, “Estimating Optimal Profiles of Genetic Alterations Using Constraint-Based Models,” *Biotechnology and Bioeng.*, vol. 89, no. 2, pp. 243-251, 2005.  
[47] E. Gill, W. Murray, and M.A. Saunders, “SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization,” *SIAM J. Optimization*, vol. 12, no. 4, pp. 979-1006, 2002.  
[48] A. Gilman and J. Ross, “Genetic-Algorithm Selection of a Regulatory Structure that Directs Flux in a Simple Metabolic Model,” *Biophysical J.*, vol. 69, pp. 1321-1333, 1995.  
[49] L. Glass and S.A. Kauffman, “The Logical Analysis of Continuous, Non-Linear Biochemical Control Networks,” *J. Theoretical Biology*, vol. 39, pp. 103-129, 1973.  
[50] O.R. Gonzalez, C. Kuper, K. Jung Jr., P.C. Naval, and E. Mendoza, “Parameter Estimation Using Simulated Annealing for S-System Models of Biochemical Networks,” *Bioinformatics*, vol. 23, no. 4, pp. 480-486, 2007.  
[51] X. Gu, “Systems Biology Approaches to the Computational Modelling of Tryanothione Metabolism in Trypanosoma Brucei,” PhD thesis, Univ. of Glasgow, 2010.  
[52] S. Han, Y. Yoon, and K.H. Cho, “Inferring Biomolecular Interaction Networks Based on Convex Optimization,” *Computational Biology and Chemistry*, vol. 31, nos. 5/6, pp. 347-354, 2007.  
[53] J. Handl, D.B. Kell, and J. Knowles, “Multiobjective Optimization in Bioinformatics and Computational Biology,” *IEEE/ACM Trans. Computational Biology and Bioinformatics*, vol. 4, no. 2, pp. 279-292, Apr.-June 2007.  
[54] N. Hansen, S.D. Muller, and P. Koumoutsakos, “Reducing the Time Complexity of the Derandomized Evolution Strategy with Covariance Matrix Adoption (CMA-ES),” *Evolutionary Computation*, vol. 11, no. 1, pp. 1-18, 2003.  
[55] *Recent Advances in Memetic Algorithms*, W.E. Hart, N. Krasnogor, and J.E. Smith, eds., vol. 166. Springer, 2005.  
[56] T. Higuchi, S. Tsutsui, and M. yamamura, “Theoretical Analysis of Simplex Crossover for Real-Coded Genetic Algorithms,” *Proc. Int’l Conf. Parallel Problem Solving from Nature*, pp. 365-374, 2000.  
[57] S.-Y. Ho, C.-H. Hsieh, and F.-C. Yu, “Inference of S-system Models for Large-Scale Genetic Networks,” *Proc. 21st Int’l Conf. Data Eng. (ICDE ’05)*, p. 1155, 2005.  
[58] S.-Y. Ho, C.-H. Hsieh, F.-C. Yu, and H.-L. Huang, “An Intelligent Two-Stage Evolutionary Algorithm for Dynamic Pathway Identification from Gene Expression Profiles,” *IEEE/ACM Trans. Computational Biology and Bioinformatics*, vol. 4, no. 4, pp. 648-704, Oct.-Dec. 2007.  
[59] T. Hohm and E. Zitzler, “Multiobjectivization for Parameter Estimation: A Case-Study on the Segment Polarity Network of Drosophila,” *Proc. 11th Ann. Conf. Genetic and Evolutionary Computation*, pp. 209-216, 2009.  
[60] R. Hooke and T.A. Jeeves, “‘Direct Search’ Solution of Numerical and Statistical Problems,” *J. the ACM*, vol. 8, no. 2, pp. 212-229, 1961.  
[61] S. Hoops, S. Sahle, R. Gauges, C. Lee, J. Pahle, N. Simus, M. Singhai, L. Xu, P. Mendes, and U. Kummer, “COPASI—A Complex Pathway Simulator,” *Systems Biology*, vol. 22, no. 24, pp. 3067-3074, 2006.  
[62] B. Ibrahim, S. Diekmann, E. Schmitt, and P. Dittrich, “In-Silico Modeling of the Mitotic Spindle Assembly Checkpoint,” *PLoS One*, vol. 3, no. 2:e1555, 2008, doi:10.1371/journal.pone.0001555.  
[63] C. Igel, N. Hansen, and S. Roth, “Covariance Matrix Adaptation for Multi-Objective Optimization,” *Evolutionary Computation J.*, vol. 15, no. 1, pp. 1-28, 2007.  
[64] F.J. Doyle III and J. Stelling, “Systems Interface Biology,” *J. Royal Soc. Interface*, vol. 3, pp. 603-616, 2006.  
[65] L. Ingber, “Very Fast Simulated Rea-Annealing,” *Math. and Computer Modelling*, vol. 12, no. 8, pp. 967-973, 1989.  
[66] J.E. Dennis Jr., D.M. Gay, and R.E. Welsch, “An Adaptive Nonlinear Least-Squares Algorithm,” *ACM Trans. Math. Software*, vol. 7, no. 3, pp. 348-368, 1981.  
[67] *Fuzzy Systems in Bioinformatics and Computational Biology*, vol. 242 of *Studies in Fuzziness and Soft Computing*, Y. Jin and L. Wang, eds. Springer, 2009.  
[68] *Knowledge Incorporation in Evolutionary Computation*, ser. *Studies in Fuzziness and Soft Computing*, Y.C. Jin, ed., vol. 167, Springer, 2005.  
[69] K.A. De Jong, “An Analysis of Behavior of a Class of Genetic Adaptive Systems,” PhD thesis, The Univ. of Michigan, 1975.  
[70] B.H. Junker and F. Schreiber, *Analysis of Biological Networks*. Wiley, 2008.  
[71] K.J. Kauffman, P. Prakash, and J.S. Edward, “Advances in Flux Balance Analysis,” *Current Opinion in Biotechnology*, vol. 14, no. 5, pp. 491-496, 2003.  
[72] S.A. Kauffman, “Metabolic Stability and Epigenesis in Randomly Constructed Genetic Nets,” *J. Theoretical Biology*, vol. 22, pp. 437-467, 1969.  
[73] D.B. Kell, “Metabolomics and System Biology: Making Sense of the Soup,” *Current Opinion in Microbiology*, vol. 7, pp. 296-307, 2004.  
[74] J. Kennedy and R.C. Eberhart, *Swarm Intelligence*. Morgan Kaufmann, 2001.  
[75] *Biological Networks*, ser. *Complex Systems and Interdisciplinary Science*, F. Kepes, ed., vol. 3, World Scientific, 2007.  
[76] S. Kikuchi, D. Tominaga, M. Arita, K. Takahashi, and M. Tomita, “Dynamical Modeling of Genetic Networks Using Genetic Algorithm and S-system,” *Bioinformatics*, vol. 19, no. 5, pp. 643-650, 2003.  
[77] K-Y. Kim, D-Y. Cho, and B-T. Zhang, “Multi-Stage Evolutionary Algorithms for Efficient Identification of Gene Regulatory Networks,” *Proc. EvoWorkshops*, pp. 45-56, 2006.  
[78] S. Kim, J. Kim, and K.H. Cho, “Inferring Gene Regulatory Networks from Temporal Expression Profiles Under Time-Delay and Noise,” *Computational Biology and Chemistry*, vol. 31, no. 4, pp. 239-245, 2007.  
[79] S. Kimura, M. Hatakeyama, and A. Konagaya, “Inference of S-System Models of Genetic Networks from Noisy Time-Series Data,” *Chem-Bio Informatics J.*, vol. 4, no. 1, pp. 1-14, 2004.  
[80] S. Kimura, K. Ide, A. Kashihara, M. Kano, M. Hatakeyama, R. Masui, N. Nakagawa, S. Yokoyama, S. Kuramitsu, and A. Konagaya, “Inference of S-System Models of Genetic Networks Using a Cooperative Coevolutionary Algorithm,” *Bioinformatics*, vol. 21, no. 7, pp. 1154-1163, 2005.  
[81] J. Kitagawa and H. Iba, “Identifying Metabolic Pathways and Gene Regulation Networks with Evolutionary Algorithms,” *Evolutionary Computation in Bioinformatics*, G.B. Fogel and D.W. Corne, eds., pp. 255-278, Morgan Kaufmann Publishers, 2003.  
[82] H. Kitano, “Computational Systems Biology,” *Nature*, vol. 420, no. 14, pp. 206-210, 2002.  
[83] H. Kitano, “System Biology: A Brief Overview,” *Science*, vol. 295, pp. 1662-1664, 2002.  
[84] S.H. Kleinstein, D. Bottino, and G.S. Lett, “Nonuniform Sampling for Global Optimization of Kinetic Rate Constants in Biological Pathways,” *Proc. Winter Simulation Conf.*, L.F. Perrone, F.P. Wieland, J. Liu, B.G. Lawson, D.M. Nicol, and R.M. Fujimoto, eds., pp. 1611-1616, 2006.  
[85] J.R. Koza, W. Mydlowec, G. Lanza, J. Yu, and M.A. Keane, “Reverse Engineering of Metabolic Pathways from Observed Data Using Genetic Programming,” *Proc. Pacific Symp. Biocomputing*, vol. 6, pp. 434-445, 2000.  
[86] A. Kremling and J. Saez-Rodriguez, “Systems Biology—An Engineering Perspective,” *J. Biotechnology*, vol. 129, pp. 329-351, 2007.  
[87] L. Kuepfer, U. Sauer, and P.A. Parrilo, “Efficient Classification of Complete Parameter Regions Based On Semidefinite Programming,” *BMC Bioinformatics*, vol. 8, article 12, 2007.  
[88] Z. Kutalik, W. Tucker, and V. Moulton, “S-System Parameter Estimation for Noisy Metabolic Profiles Using Newton-Flow Analysis,” *IET Systms Biology*, vol. 1, no. 3, pp. 174-180, May 2007.  
[89] R. Lall and E.O. Voit, “Parameter Estimation in Modulated, Unbranched Reaction Chains with Biochemical Systems,” *Computational Biology and Chemistry*, vol. 29, pp. 309-318, 2005.  
[90] T. Lenser, T. Hinze, B. Ibrahim, and P. Dittrich, “Towards Evolutionary Network Reconstruction Tools for Systems Biology,” *Proc. Fifth European Conf. Evolutionary Computation, Machine Learning and Data Mining in Bioinformatics (EvoBIO)*, pp. 132-142, 2007.  
[91] K. Levenberg, “A Method For the Solution of Certain Non-Linear Problems in Least Squares,” *The Quarterly of Applied Math.*, vol. 2, pp. 164-168, 1944.  
[92] W. Liebermeister and E. Klipp, “Bringing Metabolic Networks to Life: Integration of Kinetic, Metabolic, and Proteomic Data,” *Theoretical Biology and Medical Modelling*, vol. 3, article 42, 2006.  
[93] G. Liliacci and M. Khammash, “Parameter Estimation and Model Selection in Computational Biology,” *PLoS Computational Biology*, vol. 6, no. 3:e1000696, Mar. 2010., doi:10.1371/journal.pcbi.1000696.  
[94] P.-K. Liu and F.-S. Wang, “Inference of Biochemical Network Models in S-System Using Multiobjective Optimization Approach,” *Bioinformatics*, vol. 24, no. 8, pp. 1085-1092, 2008.  
[95] P.-K. Liu and F.-S. Wang, “Inverse Problems of Biological Systems Using Multi-Objective Optimization,” *J. the Chinese Inst. of Chemical Eng.*, vol. 39, no. 5, pp. 399-406, 2008.  
[96] P.-K. Liu and F.-S. Wang, “Hybrid Differential Evolution with Geometric Mean Mutation in Parameter Estimation of Bioreaction Systems with Large Parameter Search Space,” *J. Computers and Chemical Eng.*, vol. 33, pp. 1851-1860, 2009.  
[97] P.-K. Liu and F.-S. Wang, “Hybrid Differential Evolution Including Geometric Mean Mutation for Optimization of Biochemical Systems,” *J. Taiwan Inst. of Chemical Eng.*, vol. 41, pp. 65-72, 2010.  
[98] P.-K. Liu, C.-H. Yuh, and F.-S. Wang, “Inference of Genetic Regulatory Networks Using S-System and Hybrid Differential Evolution,” *Proc. IEEE Congress Evolutionary Computation*, pp. 1736-1743, 2008.  
[99] R. Mahadevan, J.S. Edwards, and F.J. Doyle III, “Dynamic Flux Balance Analysis of Diauxic Growth in Escherichia Coli,” *Biophysical J.*, vol. 83, pp. 1331-1340, Sept. 2002.  
[100] R. Manner, S.W. Mahfoud, and S.W. Mahfoud, “Crowding and Preselection Revisited,” *Parallel Problem Solving from Nature*, pp. 27-36, 1992.  

[101] D. Marbach, C. Mattiussi, and D. Floreano, “Bio-Mimetic Evolutionary Reverse Engineering of Genetic Regulatory Networks,” *Proc. Fifth European Conf. Evolutionary Computation, Machine Learning and Data Mining in Bioinformatics*, E. Marchiori, J.H. Moore, and J.C. Rajapakse, eds., pp. 155-165, 2007.  
[102] Y. Matsubara, S. Kikuchi adn, M. Sugimoto, and M. Tomita, “Parameter Estimation for Stiff Equations of Biosystems Using Radial Basis Function Networks,” *BMC Bioinformatics*, vol. 7, article 230, 2006.  
[103] N. Matsumaru, F. Centler, K.-P. Zauner, and P. Dittrich, “Self-Adaptive Scouting—Autonomous Experimentation for Systems Biology,” *Lecture Notes in Artificial Intelligence*, LNCS, vol. 3005, pp. 52-62, Springer, 2004.  
[104] K. Matsumura, H. Oida, and S. Kimura, “Inference of S-System Models of Genetic Networks by Function Optimization Using Genetic Programming,” *Trans. Information Processing Soc. Japan*, vol. 46, no. 11, pp. 2814-2830, 2005.  
[105] C. Mattiussi and D. Floreano, “Analog Genetic Encoding for the Evolution of Circuits and Networks,” *IEEE Trans. Evolutionary Computation*, vol. 11, no. 5, pp. 596-607, Oct. 2007.  
[106] P. Mendes and D.B. Kell, “Non-Linear Optimization of Biochemical Pathways: Applications to Metabolic Engineering and Parameter Estimation,” *Bioinformatics*, vol. 14, no. 1, pp. 869-883, 1998.  
[107] C. Modchang, W. Triampo, and Y. Lenbury, “Mathematical Modeling and Application of Genetic Algorithm to Parameter Estimation in Signal Transduction: Trafficking and Promiscuous Coupling of G-Protein Coupled Receptors,” *Computers in Biology and Medicine*, vol. 38, pp. 574-582, 2008.  
[108] C.G. Moles, P. Mendes, and J.R. Banga, “Parameter Estimation in Biochemical Pathways: A Comparison of Global Optimization Methods,” *Genome Research*, vol. 13, nos. 2467-2474, 2003.  
[109] J.H. Moore and L.W. Hahn, “Grammatical Evolution for the Discovery of Petri Net Models of Complex Genetic Systems” *Proc. Int’l Conf. Genetic and Evolutionary Computation*, Cantu-Paz et al., eds., pp. 2412-2413, 2003.  
[110] J.H. Moore and L.W. Hahn, “Petri Net Modeling of High-Order Genetic Systems Using Grammatical Evolution,” *BioSystems*, vol. 72, pp. 177-186, 2003.  
[111] J.H. Moore and L.W. Hahn, “Systems Biology Modeling in Huamn Genetics Using Petri Nets and Grammatical Evolution,” *Proc. Genetic and Evolutionary Computation (GECCO ’04) Conf.*, pp. 392-401, 2004.  
[112] R. Morishita, H. Imade, I. Ono, N. Ono, and M. Okamoto, “Finding Multiple Solutions Based on an Evolutionary Algorithm for Inference of Genetic Networks by S-System,” *Proc. Congress Evolutionary Computation (CEC ’03)*, vol. 1, pp. 615-622, 2003.  
[113] M. Motta Jafelice, B.F.Z. Bechara, L.C. Barros, R.C. Bassanezi, and F. Gomide, “Cellular Automata with Fuzzy Parameters in Microscopic Study of Positive HIV Individuals,” *Math. and Computer Modelling*, vol. 50, nos. 1/2, pp. 32-44, 2009.  
[114] J.A. Nelder and R. Mead, “A Simplex Method for Function Minimization,” *Computer J.*, vol. 7, pp. 308-313, 1965.  
[115] J. Nielsen, “Principles of Optimal Metabolic Network Operation,” *Molecular Systems Biology*, vol. 3, article 126, 2007.  
[116] D. Noble, “Systems Biology and the Heart,” *BioSystems*, vol. 83, pp. 75-80, 2006.  
[117] N. Noman and H. Iba, “Inference of Gene Regulatory Networks Using S-System and Differential Evolution,” *Proc. Conf. Genetic and Evolutionary Computation*, pp. 439-446, 2005.  
[118] N. Noman and H. Iba, “Reverse Engineering Genetic Networks Using Evolutionary Computation,” *Genome Informatics*, vol. 16, no. 2, pp. 205-214, 2005.  
[119] N. Noman and H. Iba, “Inferring Gene Regulatory Networks Using Differential Evolution with Local Search Heuristics,” *IEEE/ACM Trans. Computational Biology and Bioinformatics*, vol. 4, no. 4, pp. 634-647, Oct.-Dec. 2007.  
[120] J. Nummela and B.A. Julstrom, “Evolving Petri Nets to Represent Metabolic Pathways,” *Genetic and Evolutionary Computation Conf.*, Hans-Georg Beyer and Una-May O’Reilly, eds., pp. 2133-2139, 2005.  
[121] M. O’Neill and C. Ryan, “Grammatical Evolution,” *IEEE Trans. Evolutionary Computation*, vol. 5, no. 4, pp. 349-358, Aug. 2001.  
[122] M. Patan and B. Bogacka, “Optimum Experimental Designs for Dynamic Systems in the Presence of Correlated Errors,” *Computational Statistics & Data Analysis*, vol. 51, pp. 5644-5661, 2007.  
[123] K.R. Patil, I. Rocha, J. Forster, and J. Nielsen, “Evolutionary Programming as A Platform for in Silico Metabolic Engineering,” *BMC Bioinformatics*, vol. 6, no. 1, p. 308, 2005.  
[124] M. Peifer and J. Timmer, “Parameter Estimation in Ordinary Differential Equations for Biochemical Processes Using the Method of Multiple Shooting,” *IET System Biology*, vol. 1, no. 2, pp. 78-88, Mar. 2007.  
[125] A. Pettinen, O. Yli-Harja, and M-L. Linne, “Comparison of Automated Parameter Estimation Methods for Neuronal Signalling Networks,” *Neurocomputing*, vol. 69, pp. 1371-1374, 2006.  
[126] J.W. Pinney, D.R. Westhead, and G.A. McConkey, “Petri Net Representations in Systems Biology,” *Biochemical Soc. Trans.*, vol. 31, no. 6, pp. 1513-1515, 2003.  
[127] P.K. Polisetty, E.O. Voit, and E.P. Gatzke, “Identification of Metabolic System Parameters Using Global Optimization Methods,” *Theoretical Biology and Medical Modelling*, vol. 3, no. 4, pp. 1-15, 2006.  
[128] M.J.D. Powell, “The NEWUOA Software for Unconstrained Optimisation without Derivatives,” Technical Report NA2004/08, Dept. of Applied Math. and Theoretical Physics, Univ. of Cambridge, 2004.  
[129] A.A. Poyton, M.S. Varziri, K.B. McAuley, P.J. Mclellan, and J.O. Ramsay, “Parameter Estimation In Continuous-Time Dynamic Models Using Principal Differential Analysis,” *Computers and Chemical Eng.*, vol. 30, pp. 698-708, 2006.  
[130] K. Praveen, D. Sanjoy, and W. Stephen, “LRJ: A Multi-Objective GA-Simplex Hybrid Approach for Gene Regulatory Network Models,” *Proc. IEEE Congress Evolutionary Computation*, pp. 2084-2090, 2004.  
[131] J.O. Ramsay, G. Hooker, D. Campbell, and J. Cao, “Parameter Estimation for Differential Equations: A Generalized Smoothing Approach,” *J. the Royal Statistical Soc.: Series B (Statistical Methodology)*, vol. 69, no. 5, pp. 741-796, 2007.  
[132] M. Rodriguez-Fernandez, J.A. Egea, and J.R. Banga, “Novel Metaheuristic for Parameter Estimation in Nonlinear Dynamic Biological Systems,” *BMC Bioinformatics*, vol. 7, pp. 483-501, 2006.  
[133] M. Rodriguez-Fernandez, P. Mendes, and J.R. Banga, “A Hybrid Approach for Efficient and Robust Parameter Estimation in Biochemical Pathways,” *BioSystems*, vol. 83, pp. 248-265, 2006.  
[134] T. Rudge and N. Geard, “Evolving Gene Regulatory Networks for Cellular Morphogenesis,” *Proc. The Second Australian Conf. Artificial Life*, Dec. 2005.  
[135] T.P. Runarsson and X. Yao, “Stochastic Ranking for Constrained Evolutionary Optimization,” *IEEE Trans. Evolutionary Computation*, vol. 4, no. 3, pp. 284-294, Sept. 2000.  
[136] *Handbook of Fuzzy Computation*, E. Ruspini, P. Bonissone, and W. Pedrycz , eds. IOP Publishing, Ltd., 1998.  
[137] H. Salis and Y. Kaznessis, “Accurate Hybrid Stochastic Simulation of a System of Coupled Chemical or Biochemical Reactions,” *J. Chemical Physics*, vol. 122, no. 5: 54103, 2005.  
[138] H. Salis, V. Sotiropoulos, and Y.N. Kaznessis, “Multiscale Hy3S: Hybrid Stochastic Simulation for Supercomputers,” *BMC Bioinformatics*, vol. 7, article 93, 2006.  
[139] M.A. Savageau, “Biochemical Systems Analysis I: Some Mathematical Properties of the Rate Law for the Component Enzymatic Reactions,” *J. Theoretical Biology*, vol. 25, no. 3, pp. 365-369, 1969.  
[140] M.A. Savageau, “Biochemical Systems Analysis II: The Steady State Solutions for an N-Pool System Using a Power-Law Approximation,” *J. Theoretical Biology*, vol. 25, no. 3, pp. 370-379, 1969.  
[141] M.A. Savageau, “Biochemical Systems Analysis III: Dynamic Solutions Using a Power-Law Approximation,” *J. Theoretical Biology*, vol. 26, no. 2, pp. 215-226, 1970.  
[142] R. Schuetz, L. Kuepfer, and U. Sauer, “Systematic Evaluation of Objective Functions for Predicting Intracellular Fluxes in Escherichia Coli,” *Molecular Systems Biology*, vol. 3, article 119, 2007.  
[143] D. Segre, D. Vitkup, and G.M. Church, “Analysis of Optimality in Natural and Perturbed Metabolic Networks,” *Proc. Nat’l Academy of Sciences of USA*, vol. 99, no. 23, pp. 15112-15117, 2002.  
[144] S. Sheikh-Bahaei and C.A. Hunt, “Prediction of in vitro Heapatic Biliary Excretion Using Stochastic Agent-Based Modeling and Fuzzy Clustering,” *Proc. Winter Simulation Conf.*, L.F. Perrone, F.P. Wieland, J. Liu, B.G. Lawson, D.M. Nicol, and R.M. Fujimoto, eds., pp. 1617-1624, 2006.  
[145] *Advances in Metaheuristics for Hard Optimization*, *Natural Computing Series*, P. Siarry, and Z. Michalewicz, eds. Springer, 2008.  
[146] A. Sirbu, H.J. Ruskin, and M. Crane, “Comparison of Evolutionary Algorithms in Gene Regulatory Network Model Inference,” *BMC Bioinformatics*, vol. 11, no. 1, p. 59, 2010.  
[147] C. Spieth, F. Streichert, N. Speer, and A. Zell, “Optimizing Topology and Parameters of Gene Regulatory Network Models from Time-Series Experiments,” *Proc. Genetic and Evolutionary Computation Conf.*, K. Deb et al., eds., pp. 461-470, 2004.  
[148] C. Spieth, R. Worzischek, and F. Streichert, “Comparing Evolutionary Algorithms on the Problem of Network Inference,” *Proc. Eighth Ann. Conf. Genetic and Evolutionary Computation*, pp. 305-306, 2006.  
[149] J. Srividhya, E.J. Crampin, and P.E. McSharry, “Reconstructing Biochemical Pathways from Time Course Data,” *Proteomics*, vol. 7, pp. 828-838, 2007.  
[150] R. Storn and K. Price, “Differential Evolution—A Simple and Efficient Heuristic for Global Optimization over Continuous Spaces,” *J. Global Optimization*, vol. 11, pp. 341-359, 1997.  

[151] F. Streichert, H. Planatscher, C. Spieth, H. Ulmer, and A. Zell, “Comparing Genetic Programming and Evolution Strategies on Inferring Gene Regulatory Networks,” *Proc. Genetic and Evolutionary Computation Conf.*, pp. 471-480, 2004.  
[152] D. Tominaga, N. Koga, and M. Okamoto, “Efficient Numerical Optimization Algorithm Based on Genetic Algorithm for Inverse Problem: System for the Inference of Genetic Networks,” *Proc. Genetic and Evolutionary Computation Conf.*, pp. 251-258, 2000.  
[153] J. Tomshine and Y.N. Kaznessis, “Optimization of a Stochastically Simulated Gene Network Model via Simulated Annealing,” *Biophysical J.*, vol. 91, pp. 3196-3205, 2006.  
[154] K.-Y. Tsai and F.-S. Wang, “Evolutionary Optimization with Data Collocation for Reverse Engineering of Biological Networks,” *Bioinformatics*, vol. 21, no. 7, pp. 1180-1188, 2005.  
[155] S. Tsutsui, M. yamamura, and T. Higuchi, “Multi-Parent Recombination with Simplex Crossover in Real-Coded Genetic Algorithm,” *Proc. Genetic and Evolutionary Computation Conf.*, pp. 657-664, 1999.  
[156] P.A. Vanrolleghem and D. Dochain, “Model Identification,” *Advanced Instrumentation, Data Integration, and Control of Biotechnological Process*, J. Van Impe, P.A. Vanrolleghem, and D. Iserentant, eds., pp. 251-318, Kluwer Academic Publishers, 1998.  
[157] T.D. Vo, W.N.P. Lee, and P.O. Palsson, “Systems Analysis of Energy Metabolism Elucidates the Affected Respiratory Chain Complex in Leigh’s Syndrome,” *Molecular Genetics and Metabolism*, vol. 91, no. 1, pp. 15-22, 2007.  
[158] E.O. Voit and J. Almeida, “Decoupling Dynamical Systems for Pathway Identification from Metabolic Profiles,” *Bioinformatics*, vol. 20, no. 11, pp. 1670-1681, 2004.  
[159] V. Vyshemirsky and M. Girolami, “Biobayes: A Software Package for Bayesian Inference in Systems Biology,” *Bioinformatics*, vol. 24, no. 17, pp. 1933-1934, 2008.  
[160] F.-S. Wang and P.-K. Liu, “Inverse Problems of Biochemical Systems Using Hybrid Differential Evolution and Data Collocation,” *Int’l J. Systems and Synthetic Biology*, vol. 1, pp. 21-38, 2010.  
[161] Y. Wang, T. Joshi, X.-S. Zhang, D. Xu, and L. Chen, “Inferring Gene Regulatory Networks from Multiple Microarray Databases,” *Bioinformatics*, vol. 22, no. 19, pp. 2413-2420, 2006.  
[162] K.Q. Weinberger, F. Sha, Q. Zhu, and L.K. Saul, “Graph Laplacian Regularization for Large-Scale Semidefinite Programming,” *Advanced in Neural Information Processing System*, 2007.  
[163] D.H. Wolpert and W.G. Macready, “No Free Lunch Theorems for Optimization,” *IEEE Trans. Evolutionary Computation*, vol. 1, no. 1, pp. 67-82, Apr. 1997.  
[164] R. Xu, G.K. Venayagamoorthy, and D.C. Wunsch II, “Modeling of Gene Regulatory Networks with Hybrid Differential Evolution and Particle Swarm Optimization,” *Neural Networks*, vol. 20, pp. 917-927, 2007.  
[165] J. Yang, S. Wongsa, V. Kadirkamanathan, S.A. Billings, and P.C. Wright, “Metabolic Flux Estimation—A Self-Adaptive Evolutionary Algorithm with Singular Value Decomposition,” *IEEE/ACM Trans. Computational Biology and Bioinformatics*, vol. 4, no. 1, pp. 126-138, Jan.-Mar. 2007.  
[166] J. Yang, S. Woongsa, V. Kadirkamanathan, S.A. Billings, and P.C. Wright, “Differential Evolution and Its Application to Metabolic Flux Analysis,” *Proc. Evo Workshops ’05*, F. Rothlauf et al., eds., pp. 115-124, 2005.  
[167] *Evolutionary Computation in Dynamics and Uncertain Environments*, ser. *Studies in Computational Intelligence*, S.X. Yang, Y.-S. Ong, and Y.C. Jin, eds., vol. 51, Springer, 2007.  
[168] Y. Ye, “Interior Algorithms for Linear, Quadratic and Linearly Constrained Nonlinear Programming,” PhD thesis, Dept. of ESS, Stanford Univ., 1987.  
[169] M.K.S. Yeung, J. Tegner, and J.J. Collins, “Reverse Engineering Gene Networks Using Singular Value Decomposition and Robust Regression,” *Proc. Nat’l Academy of Sciences USA*, vol. 99, no. 9, pp. 6163-6168, 2002.  
[170] L. You, “Toward Computational Systems Biology,” *Cell Biochemistry and Biophysics*, vol. 40, pp. 167-184, 2004.  
[171] D.E. Zak, G.E. Gonye, J.S. Schwaber, and F.J. Doyle III, “Importance of Input Perturbations and Stochastic Gene Expression in the Reverse Engineering of Genetic Regulatory Networks: Insights from and Identifiability Analysis of an in Silico Network,” *Genome Research*, vol. 13, pp. 2396-2405, 2003.  
[172] W. Zhang and X. Xie, “DEPSO: Hybrid Particle Swarm with Differential Evolution Operator,” *Proc. IEEE Int’l Conf. Systems, Man and Cybernetics*, pp. 3816-3821, 2003.  
[173] Z. Zhou, Y.-S. Ong, P.B. Nair, A.J. Keane, and K.Y. Lum, “Combining Global and Local Surrogate Models to Accelerate Evolutionary Optimization,” *IEEE Trans. Systems, Man, and Cybernetics, Part C: Applications and Rev.*, vol. 37, no. 1, pp. 66-76, Jan. 2007.

---

## Author Information

### Jianyong Sun
Jianyong Sun received the BSc degree in computational mathematics from Xi’an Jiaotong University, China, the MSc degree in applied mathematics and the PhD degree in computer science from the University of Essex, United Kingdom in 1997, 1999, and 2005, respectively. He is currently a research fellow within the Centre for Plant Integrative Biology (CPIB) and the Intelligent Modeling and Analysis (IMA) Research Group in the School of Bioscience and the School of Computer Science at the University of Nottingham, United Kingdom, respectively. He has published more than 20 peer-reviewed papers on evolutionary algorithms and statistical machine learning in prestigious journals such as the *IEEE Transactions on Evolutionary Computation* and *IEEE Transactions on Neural Networks*. His main research interests are to improve the effectiveness and efficiency of evolutionary algorithms by combining classical hill-climbing local search algorithms, and to develop statistical machine learning algorithms for data analysis.

### Jonathan M. Garibaldi
Jonathan M. Garibaldi received the BSc (Hons) degree in physics from Bristol University, United Kingdom, the MSc degree in intelligent systems and the PhD degree in uncertainty handling in immediate neonatal assessment from the University of Plymouth, United Kingdom, in 1984, 1990, and 1997, respectively. He is currently an associate professor and reader within the Intelligent Modeling and Analysis (IMA) Research Group in the School of Computer Science at the University of Nottingham, United Kingdom. The IMA research group undertakes research into intelligent modeling, utilizing data analysis, and transformation techniques to enable deeper and clearer understanding of complex problems. He has published more than 40 papers on fuzzy expert systems and fuzzy modeling, including three book chapters, and has edited two books. His main research interests are modeling uncertainty in human reasoning and especially in modeling the variation in normal human decision making, particularly in medical domains. He has created and implemented fuzzy expert systems, and developed methods for fuzzy model optimization. He is a member of the IEEE.

### Charlie Hodgman
Charlie Hodgman’s research career has almost exclusively involved multidisciplinary working. For 18 years (1977-1995, from ICI through several departments in Cambridge), his research involved the simultaneous application of both laboratory and computational biological techniques to major research issues in plant, animal, medical, and biotechnological sciences. Gaining an international reputation in bioinformatics, he was recruited by GlaxoWellcome in 1995, where he both collaborated with laboratory scientists on specific pharmaceutical R&D projects and developed his own Bioinformatics R&D programme in what is now known as integrative systems biology. In 2004, he moved to the University of Nottingham to take up the chair in Bioinformatics and Systems Biology where he established the Multidisciplinary Centre for Integrative Biology. This center currently has a 12m research portfolio, which predominantly includes the BBSRC/EPSRC Centre for Plant Integrative Biology (of which he is director), focusing on plant and crop research, though there are also animal and microbial projects. He has served on various United Kingdom and EU Research funding panels, and the steering committee of the pan-European ERA-SysBio. He has also contributed to the development of national strategies for the Research Councils, DTI, and OST.

---

For more information on this or any other computing topic, please visit our Digital Library at www.computer.org/publications/dlib.
```