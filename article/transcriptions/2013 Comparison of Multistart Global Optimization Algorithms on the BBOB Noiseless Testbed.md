

# Comparison of Multistart Global Optimization Algorithms on the BBOB Noiseless Testbed

**László Pál**  
Sapientia - Hungarian University of Transylvania  
530104 Miercurea-Ciuc, Piata Libertatii, Nr. 1, Romania  
pallaszlo@sapientia.siculorum.ro

## ABSTRACT

Multi Level Single Linkage is a multistart, stochastic global optimization method which relies on random sampling and local search. In this paper, we benchmarked three variants of the MLSL algorithm by using two gradient based and a derivative-free local search method on the noiseless function testbed. The three methods were also compared with a commercial multistart solver, called OQNLP (OptQuest/NLP).

Our experiment showed that, the results may be influenced essentially by the applied local search procedure. Depending of the type of the problem the gradient based local search methods are faster in the initial stage of the optimization, while the derivative-free method show a superior performance in the final phase for moderate dimensions. Considering the percentage of the solved problems, OQNLP is similar or even better (for multi-modal and weakly structured functions) in 5-D than the MLSL method equipped with the gradient type local search methods, while on 20-D the latter algorithms are usually more faster.

### Categories and Subject Descriptors

G.1.6 [Numerical Analysis]: Optimization—*global optimization, unconstrained optimization*; F.2.1 [Analysis of Algorithms and Problem Complexity]: Numerical Algorithms and Problems

### General Terms

Algorithms

### Keywords

Benchmarking, Black-box optimization, Multi level methods, Multistart heuristic, Scatter search

---

## 1. INTRODUCTION

Multistart global optimization algorithms were introduced in the 1980s for bound constrained optimization problems.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.  
**GECCO’13 Companion, July 6–10, 2013, Amsterdam, The Netherlands.**  
Copyright 2013 ACM 978-1-4503-1964-5/13/07 ...$15.00.

Two important multistart type methods are the Clustering [1] and Multi Level Single Linkage (MLSL) [9] algorithms. The basic idea behind these methods is to form groups (clusters) of points around the local minimizers from a uniform sampled domain and start local searches no more than once in each of those groups.

The aim of the paper is to compare three variants of the MLSL method using the COCO framework [3] with OQNLP (OptQuest/NLP) [11], an other well known commercial multistart type algorithm.

The rest of this article is organized as follows. Section 2 reviews the MLSL and OQNLP algorithms. In Section 3, we describe the experiment procedure together with the algorithms parameter settings. The results are presented in Section 4 and discussed in Section 5. Section 6 concludes the paper and points out some directions for future work.

---

## 2. ALGORITHMS

Multi Level Single Linkage (MLSL) has two phases: a global and a local one. The global phase consists of sampling, while the local phase is based on local searches. The local minimizer points are found by means of a local search procedure (LS), starting from appropriately chosen points from the sample drawn uniformly within the set of feasibility. A local search procedure is applied to every sample point from the reduced sample, except if there is another sample point within some critical distance \(r_k\) (defined in [9]), which has a lower function value (see Algorithm 1). The reduced sample consists of the \(\gamma kN\) best points (\(0 < \gamma \le 1\)) from the cumulated sample \(x_1,\ldots,x_{kN}\).

The local search method is an essential part of the MLSL. Depending on the applied local search procedure the quality of the found solution may vary significantly. Thus in this study we tested three MLSL variants by applying two gradient based and a derivative-free local search method (more details in Sec. 3).

OQNLP is a solver designed to find global optima of smooth constrained nonlinear problems. It is a multistart heuristic method which runs a local search from a variety of starting points in order to find a global minimum, or multiple local minima. The solver uses a scatter-search mechanism for generating start points. The solver steps are presented in the Algorithm 2. After an initial call to \(LS\) at the user-provided initial point, \(x_0\), \(N_1\) trial points are generated (Stage 1). The best point is chosen as the starting point for the next call to \(LS\). In Stage 2, \(N_2\) iterations are performed in which candidate starting points are generated and \(LS\) is started at any one which passes the distance and merit filter tests.

The distance filter helps insure that the starting points for \(LS\) are diverse, in the sense that they are not too close to any previously found local solution. Its goal is to prevent \(LS\) from starting more than once within the basin of attraction of any local optimum.

Based on some recent comparative studies [10] on bound constrained problems, OQNLP show superior performance in terms of refining a near-optimal solution.

In our comparisons we used the commercial optimization software TOMLAB/OQNLP [5].

---

### Algorithm 1: The MLSL algorithm

1. \(X^* \leftarrow \emptyset;\; k \leftarrow 0\)  
2. **repeat**  
3. \(k \leftarrow k + 1\)  
4. Generate \(N\) points \(x_{(k-1)N+1}, \ldots, x_{kN}\) with uniform distribution on \(X\).  
5. Determine the reduced sample \((X_r)\) consisting of the \(\gamma kN\) best points from the cumulated sample \(x_1, \ldots, x_{kN}\).  
6. **for** \(i \leftarrow 1\) **to** length\((X_r)\) **do**  
7. **if** NOT (there is such a \(j\) that \(f(x_j) < f(x_i)\) and \(\|x_j - x_i\| < r_k\)) **then**  
8. Start a local search method \((LS)\) from \(x_i\).  
9. \(x^* \leftarrow LS(x_i)\)  
10. \(X^* \leftarrow X^* \cup \{x^*\}\)  
11. **until** Some global stopping rule is satisfied.  
12. **return** The smallest local minimum value found.

### Algorithm 2: The OQNLP solver steps

1. **Stage 1:**  
2. Set \(x_0\), user initial point.  
3. Start a local search method \(LS\) from \(x_0\).  
4. Generate \(N_1\) trial points using the scatter-search mechanism on the domain \(X\).  
5. Start a local search from the best trial point among the \(N_1\) points.  
6. Initialize the regions of attraction, counters, threshold.  
7. **Stage 2:**  
8. **for** \(i \leftarrow 1\) **to** \(N_2\) **do**  
9. Generate a new trial point \(x_i\).  
10. Start \(LS\) from \(x_i\) if passes the distance and merit filter tests.  
11. **return** The smallest local minimum value found.

---

## 3. EXPERIMENT DESIGN

The main purpose of the experiment is to investigate the impact of the different local search algorithms on the MLSL method and to compare the results with those obtained by the OQNLP solver. For this reason we fixed the parameters of the MLSL algorithm to specific values and alternated the local searches.

Each of the algorithms was run on 15 instances of all the 24 functions in dimensions 2, 3, 5, 10, and 20. The maximal evaluations budget (for the MLSL) was set to \(2 \cdot 10^4 D\) for each run.

MLSL has four parameters to set: the number of sample points in an iteration, the size of the reduced sample, the maximum number of function evaluations for local search, and the used local search procedure. The sample was generated from a Sobol quasi-random sequence [6] and its size was set to \(50D\). From the actual sample only the best \(5D\) points are considered for further analysis.

We benchmarked three variants of the MLSL algorithm by using 2 gradient type and a derivative-free local search method. The garadient based methods are the following: a quasi-Newton type (fminunc) and an interior point (fmincon) procedure from MATLAB. The first is a well-known quasi-Newton method which approximates the Hessian by the BFGS formula, while the second is an interior-point algorithm for constrained nonlinear problems. The third local search algorithm is the Nelder-Mead [7] simplex method which belongs to the class of direct search methods. All the three version of the algorithms were run on the whole testbed in all dimensions. The maximum number of function evaluations for local search was set to 10% of the total budget while the termination tolerance parameter value was set to \(10^{-12}\).

In the case of the OQNLP method, we used the default parameters (see in [5]) except the iteration limit which was set to \(300D\). Using this limit we get approximately the same maximal budget as in the case of MLSL. Furthermore it is important that OQNLP changes its search strategy depending on the iteration limit. The local search used by OQNLP is the LSGRG2, a generalized gradient projection method.

---

## 4. RESULTS

Results from experiments according to [3] on the benchmark functions given in [2, 4] are presented in Figures 1, 2 and 3 and in Tables 1 and 2. The expected running time (ERT), used in the figures and table, depends on a given target function value, \(f_t = f_{\mathrm{opt}} + \Delta f\), and is computed over all relevant trials as the number of function evaluations executed during each trial while the best function value did not reach \(f_t\), summed over all trials and divided by the number of trials that actually reached \(f_t\) [3, 8]. Statistical significance is tested with the rank-sum test for a given target \(\Delta f_t\) (\(10^{-8}\) as in Figure 1) using, for each trial, either the number of needed function evaluations to reach \(\Delta f_t\) (inverted and multiplied by \(-1\)), or, if the target was not reached, the best \(\Delta f\)-value achieved, measured only up to the smallest number of overall function evaluations for any unsuccessful trial under consideration.

### 4.1 CPU Timing Experiments

The timing experiments were carried out with \(f_8\) on a machine with Intel Dual-Core processor, 2.6 Ghz, with 2 GB RAM, on Windows 7 64bit in MATLAB R2011b 64bit. The average time per function evaluation in 2, 3, 5, 10, 20, 40 dimensions was about \(13, 9.4, 7.1, 5.2, 3.9, 3.7 \times 10^{-4}\) s for fmincon, about \(6.1, 5.5, 3.9, 3.1, 2.9, 2.7 \times 10^{-4}\) s for fminunc, about \(4.5, 3.3, 2.9, 3.3, 4.6, 8.8 \times 10^{-4}\) s for simplex, and about \(8.1, 7.6, 5.7, 4.1, 3.9, 3.1 \times 10^{-4}\) s for OQNLP.

---

## 5. DISCUSSION

Although the MLSL method cannot find the final solution in many cases, our aim was to reveal the differences between the applied local search methods during the different stages of the optimization.

Considering the ERT numbers in different dimensions, we can state that the gradient type methods are usually more faster than the simplex method. Nevertheless there are situations when the latter method is significantly better in lower dimensions than the other methods. Such cases can be observed on the \(f_7\), \(f_{10}\), \(f_{11}\), \(f_{13}\), \(f_{14}\), \(f_{16}\), and \(f_{23}\) functions (see Figure 1). The OQNLP solver is faster than the MLSL method with fmincon and fminunc on the \(f_5\), \(f_7\), \(f_{20}\), and \(f_{24}\) functions. On \(f_{24}\) OQNLP is even faster than the best BBOB-2009 algorithm for 2, 3, and 5 dimensions.

Regarding the proportion of solved instances, the general aspect is that the gradient type methods are faster on the initial phase of the optimization, while the derivative-free simplex method provides a better performance in the final stage for 2, 3, and 5 dimensions.

Considering all functions aggregated in 5-D (see Figure 2), the proportion of the solved problems by the algorithms varies between 62% and 78%. fminunc is the fastest for #FEs < \(100D\), while between \(100D\) and \(1000D\) the fmincon solves the largest proportion of problems. After \(1000D\) evaluations the simplex method becomes the leader by solving 78% of the problems up to the final budget. This behavior is more pronounced on the ill-conditioned functions subgroup. For #FEs < \(200D\), the fmincon is the best algorithm solving more than 60% of the problems, followed by fminunc, OQNLP and simplex solving 50%, 45% and 8% of the problems. For #FEs > \(700D\), the simplex becomes the best competitor by solving 100% of the problems up to the final budget. This huge progress is due to the robustness of the method on the \(f_{10}, f_{11}, f_{12}, f_{13}\) and \(f_{14}\) functions. The OQNLP is slightly faster than the simplex algorithm on the multi-modal and weakly structured functions. This behavior is caused by the success of the OQNLP method on the \(f_{19}\) and \(f_{24}\) functions.

In the 20-D space (see Figure 3), the previously observed advantageous properties of the simplex method cannot be further observed. The largest proportion of solved problems by simplex is about 22% on the separable functions subgroup, while on the moderate group is the lowest (about 2%). Considering all functions aggregated, fmincon is the fastest by solving about 58% of the problems, followed by fminunc, OQNLP, and simplex solving 55%, 50% and 15% of the problems. The previous ranking of the algorithms can be observed for the other function groups too.

---

## 6. CONCLUSIONS

We benchmarked three variants of the MLSL algorithm by using two gradient based and a derivative-free local search method on the noiseless function testbed. The three methods were also compared with OQNLP (OptQuest/NLP), a heuristic, multistart solver.

The results show that depending of the type of the problem, the gradient based local search methods are faster in the initial stage of the optimization, while the derivative-free method show a superior performance in the final phase for moderate dimensions. Considering the percentage of the solved problems, OQNLP is similar or even better (for multi-modal and weakly structured functions) in 5-D than the MLSL method equipped with the gradient type local search methods, while on 20-D the latter algorithms are usually more faster.

As a feature work we propose a strategy which tries to automatically select the best local search algorithm during the optimization.

### Acknowledgements

This work was supported by the Sapientia Foundation - Institute for Scientific Research with the grant No. 101/9/2013.

---

## 7. REFERENCES

[1] C. G. E. Boender, A. H. G. Rinnooy Kan, G. T. Timmer, and L. Stougie. A stochastic method for global optimization. *Mathematical Programming*, 22:125–140, 1982.

[2] S. Finck, N. Hansen, R. Ros, and A. Auger. Real-parameter black-box optimization benchmarking 2009: Presentation of the noiseless functions. Technical Report 2009/20, Research Center PPE, 2009. Updated February 2010.

[3] N. Hansen, A. Auger, S. Finck, and R. Ros. Real-parameter black-box optimization benchmarking 2012: Experimental setup. Technical report, INRIA, 2012.

[4] N. Hansen, S. Finck, R. Ros, and A. Auger. Real-parameter black-box optimization benchmarking 2009: Noiseless functions definitions. Technical Report RR-6829, INRIA, 2009. Updated February 2010.

[5] K. Holmström, A. O. Göran, and M. M. Edvall. User’s Guide for TOMLAB/OQNLP. Tomlab Optimization, 2007.

[6] H. S. Hong and F. J. Hickernell. Algorithm 823: Implementing Scrambled Digital Sequences. *ACM Transactions on Mathematical Software*, 29:95–109, 2003.

[7] J. Nelder and R. Mead. The downhill simplex method. *Computer Journal*, 7:308–313, 1965.

[8] K. Price. Differential evolution vs. the functions of the second ICEO. In *Proceedings of the IEEE International Congress on Evolutionary Computation*, pages 153–157, 1997.

[9] A. H. G. Rinnooy Kan and G. T. Timmer. Stochastic global optimization methods part II: Multi level methods. *Mathematical Programming*, 39:57–78, 1987.

[10] L. M. Rios and N. V. Sahinidis. Derivative-free optimization: a review of algorithms and comparison of software implementations. *Journal of Global Optimization*, 19(3):1–47, 2012.

[11] Z. Ugray, L. Lasdon, J. Plummer, R. Glover, J. Kelly, and R. Marti. Scatter Search and Local NLP Solvers: A Multistart Framework for Global Optimization. *INFORMS Journal on Computing*, 19(3):328–340, 2007.

---

# Figure 1 panel titles

1 Sphere  
2 Ellipsoid separable  
3 Rastrigin separable  
4 Skew Rastrigin-Bueche separ  
5 Linear slope  
6 Attractive sector  
7 Step-ellipsoid  
8 Rosenbrock original  
9 Rosenbrock rotated  
10 Ellipsoid  
11 Discus  
12 Bent cigar  
13 Sharp ridge  
14 Sum of different powers  
15 Rastrigin  
16 Weierstrass  
17 Schaffer F7, condition 10  
18 Schaffer F7, condition 1000  
19 Griewank-Rosenbrock F8F2  
20 Schwefel x*sin(x)  
21 Gallagher 101 peaks  
22 Gallagher 21 peaks  
23 Katsuuras  
24 Lunacek bi-Rastrigin

### Figure 1 caption

**Figure 1:** Expected running time (ERT in number of \(f\)-evaluations) divided by dimension for target function value \(10^{-8}\) as \(\log_{10}\) values versus dimension. Different symbols correspond to different algorithms given in the legend of \(f_1\) and \(f_{24}\). Light symbols give the maximum number of function evaluations from the longest trial divided by dimension. Horizontal lines give linear scaling, slanted dotted lines give quadratic scaling. Black stars indicate statistically better result compared to all other algorithms with \(p < 0.01\) and Bonferroni correction number of dimensions (six). Legend: ○:fmincon, ▽:fminunc, ⋆:simplex, □:OQNLP

---

# Figure 2 subplot titles

separable fcts  
moderate fcts  
ill-conditioned fcts  
multi-modal fcts  
weakly structured multi-modal fcts  
all functions

### Figure 2 caption

**Figure 2:** Bootstrapped empirical cumulative distribution of the number of objective function evaluations divided by dimension (FEvals/D) for 50 targets in \(10^{[-8..2]}\) for all functions and subgroups in 5-D. The “best 2009” line corresponds to the best ERT observed during BBOB 2009 for each single target.

---

# Figure 3 subplot titles

separable fcts  
moderate fcts  
ill-conditioned fcts  
multi-modal fcts  
weakly structured multi-modal fcts  
all functions

### Figure 3 caption

**Figure 3:** Bootstrapped empirical cumulative distribution of the number of objective function evaluations divided by dimension (FEvals/D) for 50 targets in \(10^{[-8..2]}\) for all functions and subgroups in 20-D. The “best 2009” line corresponds to the best ERT observed during BBOB 2009 for each single target.

---

# Table 1 caption

**Table 1:** Expected running time (ERT in number of function evaluations) divided by the respective best ERT measured during BBOB-2009 (given in the respective first row) for different \(\Delta f\) values in dimension 5. The central 80% range divided by two is given in braces. The median number of conducted function evaluations is additionally given in *italics*, if ERT(\(10^{-7}\)) \(= \infty\). #succ is the number of trials that reached the final target \(f_{\mathrm{opt}} + 10^{-8}\). Best results are printed in bold.

# Table 2 caption

**Table 2:** Expected running time (ERT in number of function evaluations) divided by the respective best ERT measured during BBOB-2009 (given in the respective first row) for different \(\Delta f\) values in dimension 20. The central 80% range divided by two is given in braces. The median number of conducted function evaluations is additionally given in *italics*, if ERT(\(10^{-7}\)) \(= \infty\). #succ is the number of trials that reached the final target \(f_{\mathrm{opt}} + 10^{-8}\). Best results are printed in bold.

