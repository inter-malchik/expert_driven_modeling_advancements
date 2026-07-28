# A novel statistical approach for comparing meta-heuristic stochastic optimization algorithms according to the distribution of solutions in the search space☆

**Tome Eftimov**^a,*^, **Peter Korošec**^a,b^

^a^ Computer Systems Department, Jožef Stefan Institute, Jamova cesta 39, Ljubljana 1000, Slovenia  
^b^ Faculty of Mathematics, Natural Sciences and Information Technologies, University of Primorska, Glagoljaška ulica 8, Koper 6000, Slovenia

## Article info

- **Received:** 21 March 2018
- **Revised:** 21 March 2019
- **Accepted:** 22 March 2019
- **Available online:** 23 March 2019

**Keywords:**  
Statistical comparison  
Benchmarking  
Single objective problems  
Exploration power  
Exploitation power

## Abstract

In this paper a novel statistical approach for comparing meta-heuristic stochastic optimization algorithms according to the distribution of the solutions in the search space is introduced, known as extended Deep Statistical Comparison. This approach is an extension of the recently proposed Deep Statistical Comparison approach used for comparing meta-heuristic stochastic optimization algorithms according to the solutions values. Its main contribution is that the algorithms are compared not only according to obtained solutions values, but also according to the distribution of the obtained solutions in the search space. The information it provides can additionally help to identify exploitation and exploration powers of the compared algorithms. This is important when dealing with a multimodal search space, where there are a lot of local optima with similar values. The benchmark results show that our proposed approach gives promising results and can be used for a statistical comparison of meta-heuristic stochastic optimization algorithms according to solutions values and their distribution in the search space.

© 2019 The Authors. Published by Elsevier Inc.  
This is an open access article under the CC BY-NC-ND license.  
(http://creativecommons.org/licenses/by-nc-nd/4.0/)

---

☆ Fully documented templates are available in the elsarticle package on http://www.ctan.org/tex-archive/macros/latex/contrib/elsarticle CTAN.  
* Corresponding author.  
E-mail addresses: tome.eftimov@ijs.si (T. Eftimov), peter.korosec@ijs.si (P. Korošec).  
https://doi.org/10.1016/j.ins.2019.03.049  
0020-0255/© 2019 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license.  
(http://creativecommons.org/licenses/by-nc-nd/4.0/)

## 1. Introduction

In mathematics and computer science, an optimization problem is one that involves finding the best solution from all feasible solutions, where the global optimal solution is the best one. However, when dealing with a multimodal optimization problem [43] we are concerned with finding the global optimal solutions among multiple different local optima. A local optimum is a solution, which is better than all its neighboring solutions, but is not the global optimal solution. When the values of local solutions are similar, we can have a situation where the performances of two algorithms are not statistically significant, but one has obtained solutions spread over the search space, while the other has them clustered. There are scenarios when one would desire them to be clustered (required stability of solutions) and vice-versa (required diversity with good quality, e.g., in engineering).

Over the years, many meta-heuristic stochastic optimization algorithms have been developed, which makes an analysis of the performance of any new algorithm a crucial task, so that it can be compared with the performance of state-of-the-art algorithms [8]. Benchmarking is a key for discovering the “best” algorithm, but finding a good one is a difficult task [34]. The first step in benchmarking theory is to define the problem domain. Finding good test functions is challenging because they must be “uniformly” distributed in the space of all possible functions from the problem domain. Currently, many of the papers published in the field of evolutionary algorithms use the black-box optimization algorithm benchmarking (BBOB) [22]. Once the set of benchmark functions has been chosen, the benchmarking results will depend on the performance metrics and statistical ranking techniques. Statistical analyses are crucial and must be made carefully, since they provide the data on which the conclusions are based. A common way to do this is to use statistical tests as a comparison technique based on the obtained solutions values (i.e., fitness function values), which follow the idea of hypothesis testing, while neglecting the distribution of the obtained solutions in the search space. Information about the solutions’ search space distribution can be used in many ways. One way is according to the desire of the users (this requires an optimization algorithm that provides sparsely or clustered solutions), but it can be also used to reveal the strengths and weaknesses of the compared algorithms. In theory, we can have four scenarios, with regard to a comparison of the obtained solutions according to their values and their distribution in the search space:

- The compared algorithms are not statistically significant with regard to the obtained solutions values and their distribution. In this case, the compared algorithms have the same exploration and exploitation power.
- There is no statistical significance between the performances of the compared algorithms with regard to the obtained solutions values, but there is a statistical significance with respect to the distribution of the obtained solutions in the search space. In this scenario the decision about algorithm preference is determined according to user needs (sparse or clustered solutions). In this case, it is assumed that the algorithm with the sparser distribution of obtained solutions has better exploration power.
- There is a statistical significance between the compared algorithms with regard to the obtained solutions values, but there is no statistical significance as to the distribution of the obtained solutions in the search space. This is a much more interesting scenario, since it tells us that the compared algorithms have the same exploration power (the compared algorithms are able to find a region with good solutions), but have different exploitation powers (one is able to find statistically better solutions than the other in the same region). Such a result indicates that the “losing” algorithm must improve its exploitation power.
- The compared algorithms have statistically significant performance in their obtained solutions values and their distribution. Here, the poorer performing algorithm lacks exploration power, while its exploitation power cannot be assessed and therefore the exploration power needs to be improved. Such analyses can be helpful for both users of optimization algorithms or developers, who want information on what their algorithm lacks.

To enable additional insight into algorithm performance, we propose an extended DSC approach that provides information on the exploration and exploitation powers of compared algorithms.

The paper is organized as follows: Section 2 gives an overview of the related work. Section 3 introduces an extended approach for comparing meta-heuristic stochastic optimization algorithms, in which the comparison is not only made according to the obtained solutions values, but also in accordance with their distribution in the search space. Section 4 presents a statistical comparison of stochastic optimization algorithms on multiple problems using an extended approach. Discussion of results is presented in Section 5. Section 6 presents a discussion of the power analysis and the conclusions are presented in Section 7.

## 2. Related work

Benchmarking in evolutionary computation is a task that must be performed when comparing a new algorithm to existing ones. It is related to the three questions that should be treated equally: which problems to choose [22], how to setup the experiments [1,2], and how to evaluate the performance of the compared algorithms. In this paper, we focus on the last question related to different statistical approaches that can be used for comparison, when problems are already chosen and experiments are set up. Further, this question can be divided into two questions: (i) which performance metric to select and (ii) which ranking scheme to use.

To the best of our knowledge, there are no published papers that focus on statistical comparison of stochastic optimization algorithms according to the distribution of the obtained solutions in the search space. This is, however, crucial for obtaining information about the exploration powers of compared algorithms and can provide a deeper understanding of the methodologies used to improve the exploration power of the algorithms. For example, Martino et al. [33], proposed a novel parallel interacting Markov Chain Monte Carlo scheme, known as orthogonal MCMC, in order to foster better exploration of the state space, especially in high-dimensional applications. Also, there are studies of using different versions of Monte Carlo sampling methods in order to find the search space in which the approximate solutions are located [6,20]. To see the benefits of using them, statistical analysis according to the distribution of the obtained solutions in the search space should be performed.

Existing approaches for making a statistical comparison of meta-heuristic stochastic optimization algorithms only focus on performance analysis with respect to the obtained solutions values (i.e., fitness function values), without considering where these values are in the search space. Some of these approaches are presented in [5,9,12,18,40,42].

Garcia et al. [10,18] used nonparametric tests for analyzing the behavior of evolutionary algorithms over optimization problems. Their study includes single-problem analysis and multiple-problem analysis. Single-problem analysis is a scenario where the data derives from multiple runs of the stochastic optimization algorithms on one problem (e.g., test function). While the multiple-problem analysis, is the scenario when several stochastic optimization algorithms are compared using multiple problems. This scenario in one in which the benchmarking theory is used. The authors also presented a statistical approach for convergence analysis of evolutionary algorithms performance [9]. In contrast, Veček et al. [42] presented an empirical approach known as a chess rating system for evolutionary algorithms (CRS4EAs). Another recently proposed approach is the Deep Statistical Comparison (DSC) [12], which is an approach for making a statistical comparison of stochastic optimization algorithms over multiple single-objective problems. It is termed deep statistics because it uses the DSC ranking scheme that is based on the whole distribution instead of using some simple statistics such as averages or medians. It enables calculation of more robust statistics and any wrong conclusions, resulting from the presence of outliers or the ranking scheme used by some standard statistical tests, can be avoided.

### 2.1. Deep statistical comparison

Using the approach of Garcia et al. [18], one needs to be aware that averages are sensitive to outliers. A common approach is to use medians because they are less sensitive to outliers. However, in both cases the results can still be affected by the ranking scheme. This happens when differences between the averages or medians are in some ε-neighborhood (e.g., 10^−9^, 10^−10^, etc.), and means that the algorithms obtain different rankings because there are no ties present. For these reasons, Deep Statistical Comparison (DSC) for comparing meta-heuristic stochastic optimization algorithms was recently proposed [12].

#### 2.1.1. DSC ranking scheme

The main contribution of the DSC approach is its ranking scheme, which is based on the whole distribution, instead of using only one statistic to describe the distribution, such as the average or median. The approach consists of two steps. The first step uses a newly proposed ranking scheme to obtain data in order to make a statistical comparison. The ranking scheme is based on comparing distributions using a statistical test, such as, a two-sample Kolmogorov-Smirnov (KS) test or a two-sample Anderson-Darling (AD) test [14]. All pairwise comparisons between the compared algorithms must be made, and the obtained p-values are organized in a matrix. Further, because multiple pairwise comparisons are made, these p-values are corrected using the Bonferroni correction [18] in order to control the family-wise error, FWER [21]. The FWER is the probability of making one or more false discoveries (type I errors) among all the hypotheses when performing multiple pairwise hypotheses tests. The matrix is then checked for transitivity, and on this basis the algorithms obtain their rankings. The second step is a standard omnibus statistical test, which uses data obtained by the DSC ranking scheme as the input data.

## 3. Extended deep statistical comparison

Deep Statistical Comparison works with one-dimensional data and cannot be used to compare distributions of the obtained solutions in either the search space, or for high-dimensional data. For this purpose, an extended version of the DSC is proposed, called extended Deep Statistical Comparison (eDSC) approach, in which a generalization of the DSC ranking scheme for high-dimensional space is introduced. The main contribution of eDSC is that the comparison takes into account not just the obtained solutions values, but also their distribution in the search space. The eDSC consists of two parts (see Algorithm 1). The first part is a comparison that takes into account the obtained solutions values using a recently proposed DSC [12]. The DSC ranking scheme is slightly modified and uses the two-sample Anderson-Darling (AD) test instead of the two-sample Kolmogorov-Smirnov (KS) test to compare the distributions of two samples. The benefits of using a two-sample AD test instead of the two-sample KS test are given in [14]. The results of using the DSC ranking scheme with the two-sample AD test compared to the results obtained using the DSC ranking scheme with the two-sample KS test are presented in [13]. The second part compares the distributions of the obtained solutions in the search space, using the eDSC ranking scheme. Both parts consist of two steps. The first step uses an appropriate (DSC or eDSC) ranking scheme to transform the raw data from multiple runs on a given problem into data that will be further used as the input data for the statistical comparison involved in benchmarking. The second step involves performing a standard omnibus statistical test (parametric or nonparametric); the choice of which depends on the required conditions for the safe use of parametric tests. The first step of the eDSC defines a diversity-based performance metric, while the second step uses the results of the first step in an appropriate omnibus statistical test.

**Algorithm 1. eDSC approach.**
1. Compare the obtained solutions values using DSC ranking scheme;
2. Compare distributions of the obtained solutions in the search space using eDSC ranking scheme;

### 3.1. Extended deep statistical comparison ranking scheme

Let `m` be the number of algorithms, `k` the number of problems, `n` the number of runs performed by each algorithm on a single problem, and `d` the dimension of the search space (i.e., `d ≥ 2`).

Let `X_{i,l}` be a `n × d` matrix, where, `i = 1, . . ., k`, and `l = 1, . . ., m`. Because each problem is defined as `y = f(x) = f(x_1, x_2, . . ., x_d), f : R^d → R`, the value of solution `y` corresponds to the point in the search space, `x = (x_1, x_2, . . ., x_d)`. According to this, the rows of the matrix `X_{i,l}` are `d`-dimensional vectors, which are the points in the search space that correspond to the obtained solutions by `n` runs on the `i`th problem of the `l`th algorithm. So for the `i`th problem, we have a set of matrices `{X_{i,1}, X_{i,2}, . . ., X_{i,m}}`, where one matrix corresponds to one algorithm that is involved in the comparison.

The main difference with the DSC ranking scheme is that high-dimensional data is involved and the ranking scheme needs to compare probability distributions for high dimensions of each algorithm on each problem. Classical statistical tests used for one-dimensional data, such as the two-sample Kolmogorov-Smirnov (KS) test and the two-sample Anderson-Darling (AD) test, do not have a natural distribution-free extension to the high-dimensional data. A class of consistent, asymptotic distribution free tests for the high-dimensional space is based on nearest neighbors in the Euclidean distance metric [25,38]. Szekely and Rizzo [41] presented a multivariate E test, which is universally consistent against all alternatives (not necessarily continuous) with finite second moments. The computational complexity of this test does not depend on dimension or on the number of samples and it is a powerful competitor to the nearest neighbor tests. The results presented in [41] suggest that the multivariate E test may be one of the most powerful tests available for high-dimensional data.

Let `α_X` be the significance level used by the statistical test used for comparing distributions in high dimensions. By using a statistical test, `m · (m − 1) / 2` pairwise comparisons between the algorithms are performed, and the results are organized in a `m × m` matrix, `N_i` as follows:

\[
N_i[p, q] =
\begin{cases}
p_{\text{value}}, & p \ne q \\
1, & p = q
\end{cases}
\tag{1}
\]

where `p` and `q` are different algorithms and `p, q = 1, . . ., m`.

Because multiple pairwise comparisons are made, the Bonferroni correction is used to correct the p-values in order to control the FWER. The Bonferroni correction is based on the idea of testing `u` different hypotheses, which in our case is `u = C_m^2 = {m \choose 2} = m·(m−1)/2`. In the proposed ranking scheme, the Bonferroni correction is used to present only the methodology, however other corrections for all-vs-all pairwise comparisons, such as Shaffer’s correction, can be used [18].

The matrix `N_i` is reflexive, symmetric, but the key point for the ranking scheme is the transitivity, since the ranking is made according to it. For this purpose the matrix `N'_i` is introduced using the following equation:

\[
N'_i[p, q] =
\begin{cases}
1, & N_i[p, q] \ge \alpha_X / C_m^2 \\
0, & N_i[p, q] < \alpha_X / C_m^2
\end{cases}
\tag{2}
\]

The elements of the matrix `N'_i` are defined with regard to the obtained p-values using a statistical test for comparing distributions corrected by the Bonferroni correction. Before any ranking is performed, the matrix `N'^2_i` is calculated to check its transitivity. Only if the `N'_i` has a one in each position for which `N'^2_i` has a non-zero element, the transitivity is satisfied.

Before we explain how the ranking is made, first let us focus on the main difference between the DSC and the eDSC ranking scheme. In the DSC ranking scheme, if the distributions of the obtained solutions values from multiple runs are the same, the performance of the algorithms is the same. But if the distributions of the obtained solutions values from multiple runs are different, the ranking is made according to the average value. The algorithm with an average closest to the optimum of the problem is considered the best. However, working with high-dimensional data, a metric that determines which search space is better, must be defined. A question arises concerning which distribution of the obtained solutions in the search space is preferable. In general, this can be any metric that describes the preferred distribution. In our case, the preference is either a “wider” distribution (sparse type of solutions) or a “narrower” distribution (clustered type of solutions). According to the goal of the researchers, the distribution type of the obtained solutions in the search space (wider or narrow), which depends also on the problem to be solved, needs to be included as a parameter in the eDSC ranking scheme.

Let `ν` be the parameter used in the eDSC ranking scheme that defines the desirable type of the distribution of the obtained solutions in the search space, `ν ∈ {0, 1}`. If `ν = 0`, we are interested in a narrow distribution of the obtained solutions in the search space, so the best algorithm has the narrowest distribution, while if `ν = 1`, we are interested in a wide distribution of the obtained solutions in the search space, so the best algorithm has the widest distribution. To estimate the distribution of the obtained solutions in the search space, the measure of multivariate spread needs to be defined. For this purpose, by using the random matrix theory, the square root of the determinant of the covariance matrix [11] is used. This gives us the hypervolume, incorporating both shape (correlation) and size (standard deviation) information, which is the product of the standard deviations of the principal components [28]. The determinant of the covariance matrix is basically a shape factor, ranging from zero for degenerate distributions up to one when all components are uncorrelated.

Let `Σ_{i,l}` be a `d × d` covariance matrix for the matrix `X_{i,l}`. The covariance matrix is a positive-definite matrix [7]. A symmetric `d × d` matrix, `S`, is said to be positive-definite if the scalar `z^T S z` is positive for every non-zero column vector `z ∈ R^d`. One of the properties of positive-definite matrices is that all their eigenvalues are positive. However, it can happen that the covariance matrix is not positive-definite because it is singular, which means that at least one of the variables can be expressed as a linear combination of the others. In this case, we first need to perform dimensionality reduction [15], which is the process of reducing the number of variables under consideration, by obtaining a set of principal variables, or by computing the nearest positive-definite matrix to an approximate one [26] and then calculate the hypervolume. The hypervolume covered by the distribution is a measure of multivariate spread, which is used in the case of high-dimensional data to compare the search spaces.

The hypervolume covered by the distribution is given as

\[
V_{i,l} = \sqrt{\det(\Sigma_{i,l})} = \prod_{d_i=1}^{d} \sqrt{\lambda_{d_i}}
\tag{3}
\]

where `λ_{d_i}` are the eigenvalues of the matrix `Σ_{i,l}`, which can be obtained by using eigenvalue decomposition [16].

If the transitivity of the matrix `N'_i` is satisfied, the first step is to split the set of algorithms into `w` disjoint sets of algorithms `Ψ_f`, `f = 1, . . ., w`, such that each algorithm belongs only to one set. Each set contains the indices of the algorithms that are used in the comparison for which the transitivity is satisfied. The cardinality of the union of these sets needs to be `m`, `\sum_{f=1}^{w} |\Psi_f| = m`. The next step is to define a `w × 2` matrix, `Z_i`. The elements of this matrix are defined by the equation

\[
Z_i[f, x] =
\begin{cases}
V_{i,\Psi_f\{h\}}, & x = 1 \\
|\Psi_f|, & x = 2
\end{cases}
\tag{4}
\]

where `h` is the number that is ceiled to the nearest integer of a number obtained by the uniform distribution of a random variable `Y ∼ U(1, |\Psi_f|)`. Because the matrix `Z_i` involves only one hypervolume value for each set and each set can consist of more algorithms, the hypervolume (or an algorithm) that will be used for each set is chosen randomly from the hypervolumes (algorithms) from that set because the data samples for all the algorithms that belong to the same set come from the same distribution. Then the rows of the matrix are reordered according to the parameter value `ν`, which is set by the researcher. If `ν = 0`, the rows are reordered according to the first column that is sorted in ascending order. If the parameter value is set to `1`, `ν = 1`, the rows are reordered according to the first column that is sorted in descending order.

Let `V_i` and `C` be `w × 1` vectors that correspond to the first and the second column of the matrix `Z_i`, respectively. Finally, the rankings for the sets, `Ψ_f`, need to be assigned and organized into a `w × 1` vector `Rank_{x,s}`. For the set with a hypervolume value, `V_i[1]`, the ranking is defined as

\[
Rank_{x,s}[1] = \sum_{r=1}^{C[1]} r / C[1].
\tag{5}
\]

For remaining sets, the ranking is defined as

\[
Rank_{x,s}[f] =
\frac{\sum_{r=C[f-1]+1}^{C[f-1]+C[f]} r}{C[f]}.
\tag{6}
\]

After obtaining the rankings of the sets, each algorithm obtains its ranking according to the set to which it belongs by using the equation

\[
Rank_x[i, l] = Rank_{x,s}[f], \quad l \in \Psi_f.
\tag{7}
\]

If the transitivity of the matrix `N'_i` is not satisfied, the first step is to define two `1 × m` vectors, `Index_{x,i}` and `V_i`, whose elements are the indices of the algorithms and the hypervolume values of each algorithm, respectively. Both vectors are sorted according to the hypervolume values, in an order defined by the parameter `ν`. If `ν = 0`, the vectors are sorted in ascending order, while if `ν = 1`, they are sorted in descending order. Then, the rankings of the sorted algorithms are organized into a `1 × m` vector, `Rank_{x,s}`, according to

\[
Rank_{x,s}[l] =
\begin{cases}
l, & \exists !\, V_i[l] \in V_i \\
\sum_{r=l-c+1}^{l} r / c, & \text{otherwise}
\end{cases}
\tag{8}
\]

where `c` is the number of elements from `V_i` that have a value `V_i[l]`. Finally, the algorithms obtain their rankings according to the rankings assigned to their hypervolume values using the equation

\[
Rank_x[i, Index_{x,i}[l]] = Rank_{x,s}[l].
\tag{9}
\]

By using the ranking scheme for the algorithms on each problem, a `k × m` matrix, `Rank_x`, is defined. The `i`th row of this matrix, `Rank_x[i]`, corresponds to the rankings of the algorithms obtained by the ranking scheme using the data samples from the `i`th problem. The matrix `Rank_x` is used as input data for making a statistical comparison for multiple-problem analysis.

For an easier and better understanding of the eDSC ranking scheme, the pseudocode of a ranking for a given single problem is presented in Algorithm 2.

**Algorithm 2. Ranking scheme used to rank algorithms on the `i`th problem.**
1. Calculate the matrix `N_i` by using Eq. (1)
2. Calculate the matrix `N'_i` by using Eq. (2)
3. Check the transitivity for the matrix `N'_i`
4. For each algorithm do
5. Calculate its hypervolume (`V`) by using Eq. (3)
6. End for
7. Select the value for the parameter `ν`
8. If transitivity is satisfied then
9. Split the set of algorithms into `w` disjoint sets `Ψ_f`
10. Calculate the matrix `Z_i` by using Eq. (4)
11. Obtain the vectors `V_i` and `C`
12. Sort the vectors `V_i` and `C` regarding the selected value of `ν`
13. Calculate the vector `Rank_{x,s}` by using Eqs. (5) and (6)
14. Calculate the vector `Rank_x[i]` by using Eq. (7)
15. Else
16. Calculate the vectors `V_i` and `Index_{x,i}`
17. Sort the vectors `V_i` and `Index_{x,i}` regarding the selected value of `ν`
18. Calculate the vector `Rank_{x,s}` by using Eq. (8)
19. Calculate the vector `Rank_x[i]` by using Eq. (9)
20. End if
21. Return `Rank_x[i]`

### 3.2. Selection of an appropriate omnibus statistical test

After ranking the algorithms, the next step is to choose an appropriate statistical test. Using the new ranking scheme we transformed only the data that is available as input data for statistical comparison, while everything else remained the same. So the required conditions for the safe use of the parametric test (i.e., normality of the data, homoscedasticity of variances, and independence) should be checked regarding the transformed data and an appropriate omnibus statistical test should be selected. The guidelines on how to select an appropriate statistical test are presented in [18].

## 4. Evaluation

### 4.1. Black-box benchmarking 2009 test functions

To evaluate the eDSC approach, the results from the Black-Box Benchmarking 2009 (BBOB 2009) competition [24] were used. BBOB 2009 is a competition that provides single-objective functions for benchmarking. The reason for choosing this benchmark was that all the data is provided on their website and the problem seeds, which determine the location of global optimum, were the same for all instances used by competitors, so a fair comparison of the distribution in search space was possible. In later years, according to our tests, this was no longer the case.

We selected from the competition 17 out of the 32 algorithms for evaluation since the omitted algorithms did not provide data organized in the template provided by the BBOB 2009. The algorithms used were: Cauchy-EDA, ALPS, AMALGAM, EDA-PSO, FULLNEWUOA, G3PCX, GA, iAMALGAM, LSfminbnd, LSstep, MCS, NELDERDOERR, POEMS, PSO, PSO_Bounds, Rosenbrock, and VNS. More details about the algorithms can be found in [23]. For each, the results for 22 different noiseless test functions in 5 dimensionality (2, 3, 5, 10, and 20) were selected. More details can be found in [24]. For each algorithm, the BBOB 2009 provided data for 15 runs on each problem, which is the data we used in our experiments.

### 4.2. Experiments

The statistical comparisons were performed using the R programming language. To compare the distributions of one-dimensional data, a two-sample Anderson-Darling test is used, which is a part of the `kSamples` package [39]. While for high-dimensional data the multivariate E test is used, which is a part of the `energy` package [37]. The normality condition is checked using the Kolmogorov-Smirnov test for normality that is part of the `stats` package [36]. Homoscedasticity is checked by applying the Levene’s test that is part of the `lawstat` package [19]. After checking the required conditions for the safe use of the parametric tests for each comparison in our experiments, nonparametric statistical tests were selected. For a pairwise comparison, the Wilcoxon signed-rank test that is a part of the `stats` package was used. While for a comparison of more than two algorithms the nonparametric Friedman test from the `scmamp` package [4] was used. In the multivariate case if the covariance matrix is singular, the `nearPD` function from the package `Matrix` [3] is used to compute the nearest positive definite matrix to the covariance matrix.

**Fig. 1.** Flowchart of the eDSC ranking scheme used to rank algorithms on the `i`th problem.

To see how the proposed methodology works, three experiments are performed. In the first one, the focus is on benchmarking of three algorithms over multiple problems, and the dimension is fixed to `2`, `d = 2`. In the second one, a statistical comparison of three algorithms over multiple problems is presented and the dimension is set to `10`, `d = 10`. In the last experiment, we make multiple comparisons with a control algorithm in which more than three algorithms are involved and the dimension is `10`, `d = 10`.

#### 4.2.1. Comparison of three algorithms with `d = 2`

We randomly generated 100 random combinations without repetition that were involved in the benchmarking. We did this in order to cover all possible scenarios. Each combination is a statistical comparison of three randomly selected algorithms. Data for the statistical comparison were generated using the DSC ranking scheme to compare the algorithms regarding the solutions values, and using the eDSC ranking scheme to compare the algorithms regarding the distribution of the solutions in the search space. After obtaining rankings from both ranking schemes for each combination, the data was analyzed using the Friedman test, which was selected as an appropriate omnibus statistical test.

Looking at the results from the statistical comparisons of 100 randomly generated combinations, there are two possible scenarios using the BBOB 2009 benchmarking. However, we need to point out that when different benchmarking tests are used, the number of possible scenarios increases to four. The first one is that there is no statistical significance between the performance of the algorithms over multiple problems according to the obtained solutions values and their distributions in the search space. In the second one, there is a statistical significance between the performance of the algorithms according to the obtained solutions values over multiple problems and there is no statistical significance between the performance of the algorithms according to the distributions of the obtained solutions in the search space over multiple problems. In our case, there are 41 out of 100 combinations that belong to the first scenario, while in the second case there are 59. From each scenario, 5 combinations are selected and presented in Table 1. The `pvalueY` and `pvalueX` correspond to the p-values for comparing the obtained solutions values and comparing the distributions of the obtained solutions in the search space over multiple problems, respectively.

**Table 1. Statistical comparisons of 3 algorithms.**

| # | Algorithms | pvalueY | pvalueX |
|---|---|---:|---:|
| 1 | Cauchy-EDA, MCS, iAMALGAM | (.44) | (.95) |
| 2 | FULLNEWUOA, ALPS, Cauchy-EDA | (.47) | (.95) |
| 3 | Cauchy-EDA, AMALGAM, MCS | (.33) | (.95) |
| 4 | PSO_Bounds, Cauchy-EDA, POEMS | (.98) | (.97) |
| 5 | Cauchy-EDA, Rosenbrock, EDA-PSO | (.57) | (.95) |
| 6 | EDA-PSO, LSstep, Rosenbrock | *(.00) | (.87) |
| 7 | PSO_Bounds, LSfminbnd, MCS | *(.00) | (.86) |
| 8 | LSfminbnd, VNS, iAMALGAM | *(.00) | (.97) |
| 9 | GA, LSstep, G3PCX | *(.00) | (.87) |
| 10 | G3PCX, Rosenbrock, LSfminbnd | *(.00) | (.87) |

\* Indicates that the null hypothesis is rejected, using `α = 0.05`.  
`pvalueY` corresponds to the p-value for comparing the obtained solutions values by the Friedman test.  
`pvalueX` corresponds to the p-value for comparing distributions of the obtained solutions in search space by the Friedman test.

To explain the results, one example from each scenario is randomly selected and explained on the level of a single problem. We did this because the benchmarking result depends on the rankings obtained for each problem separately. For the first scenario, the first combination is selected, where a statistical comparison is made between the algorithms Cauchy-EDA, MCS, and iAMALGAM. The DSC rankings at the single problem level used for making a comparison of the solutions values are presented in Table 2a, while in Table 2b the eDSC rankings are presented, which are the rankings obtained at the single problem level regarding the distribution of the solutions in the search space.

**Table 2. Rankings for the algorithms Cauchy-EDA, MCS, and iAMALGAM.**

| F | Cauchy-EDA | MCS | iAMALGAM |
|---|---:|---:|---:|
| *a) DSC ranking scheme* ||||
| f1 | 2.50 | 1.00 | 2.50 |
| f2 | 1.50 | 3.00 | 1.50 |
| f3 | 2.50 | 1.00 | 2.50 |
| f4 | 3.00 | 1.50 | 1.50 |
| f5 | 2.00 | 2.00 | 2.00 |
| f6 | 2.00 | 2.00 | 2.00 |
| f7 | 2.00 | 2.00 | 2.00 |
| f8 | 2.50 | 1.00 | 2.50 |
| f9 | 2.50 | 1.00 | 2.50 |
| f10 | 1.50 | 3.00 | 1.50 |
| f11 | 1.50 | 3.00 | 1.50 |
| f12 | 2.00 | 2.00 | 2.00 |
| f13 | 1.50 | 3.00 | 1.50 |
| f14 | 1.50 | 3.00 | 1.50 |
| f15 | 2.00 | 2.00 | 2.00 |
| f16 | 1.50 | 3.00 | 1.50 |
| f17 | 2.50 | 1.00 | 2.50 |
| f18 | 2.50 | 1.00 | 2.50 |
| f19 | 3.00 | 1.50 | 1.50 |
| f20 | 3.00 | 1.00 | 2.00 |
| f21 | 2.50 | 1.00 | 2.50 |
| f22 | 3.00 | 1.00 | 2.00 |

| F | Cauchy-EDA | MCS | iAMALGAM |
|---|---:|---:|---:|
| *b) eDSC ranking scheme* ||||
| f1 | 2.00 | 2.00 | 2.00 |
| f2 | 2.00 | 2.00 | 2.00 |
| f3 | 2.00 | 2.00 | 2.00 |
| f4 | 2.00 | 2.00 | 2.00 |
| f5 | 3.00 | 1.00 | 2.00 |
| f6 | 2.00 | 2.00 | 2.00 |
| f7 | 2.00 | 2.00 | 2.00 |
| f8 | 2.00 | 2.00 | 2.00 |
| f9 | 2.00 | 2.00 | 2.00 |
| f10 | 2.00 | 2.00 | 2.00 |
| f11 | 2.00 | 2.00 | 2.00 |
| f12 | 2.00 | 2.00 | 2.00 |
| f13 | 2.00 | 2.00 | 2.00 |
| f14 | 2.00 | 2.00 | 2.00 |
| f15 | 2.00 | 2.00 | 2.00 |
| f16 | 2.00 | 2.00 | 2.00 |
| f17 | 2.00 | 2.00 | 2.00 |
| f18 | 2.00 | 2.00 | 2.00 |
| f19 | 2.00 | 2.00 | 2.00 |
| f20 | 2.00 | 2.00 | 2.00 |
| f21 | 2.00 | 2.00 | 2.00 |
| f22 | 2.00 | 2.00 | 2.00 |

Let us now focus on the single problems: the 5th, 7th, and 20th problem (Table 2). For the 5th problem, the DSC rankings are 2.00, 2.00, and 2.00. In this case the algorithms are compared according to the obtained solutions values. The three algorithms have a 0 fitness value in all 15 runs, so they have the same distribution of the obtained solutions values. Proof of the result is also shown by the two-sample AD test that gives a p-value of 1.00 for all involved pairwise comparisons. These p-values are further corrected using the Bonferroni correction. In this case, the transitivity of the DSC ranking scheme is satisfied, but the set of all algorithms is not split into disjoint sets because all algorithms belong to one set, `{Cauchy-EDA, MCS, iAMALGAM}`. The cumulative distribution functions for the obtained solutions values are presented in Fig. 2, from where we can see that there is no difference between them.

The second step is then to compare the distributions of the obtained solutions in the search space, for which the eDSC ranking scheme is used. The eDSC rankings for the three algorithms are 3.00, 1.00, and 2.00. In Fig. 3, contour plots for the probability density functions of the obtained 2-dimensional solutions for each algorithm on f5 are presented. Using this figure, it is difficult to compare the distributions because each one has its own color scale and different values on the x1 and x2 axis, which was done for better visualization. A different color scale is here used because if we were to use only one color scale i.e., the one used in Fig. 3b, then both the contour plots Fig. 3a and c will be blue. Also, if we used the same values on the x1 and x2 axis, these would be the values from Fig. 3a, the plots shown in Fig. 3b and c would be too narrow and it would not be possible to see the shape of the distribution. In Fig. 4, the contour plots for cumulative distribution functions of the obtained 2-dimensional data for each algorithm on function f5 are presented. For this figure the color scale is the same, but for better visualization we used different values on the x1 and x2 axes.

Looking at Figs. 3 and 4, the shapes of the distributions and the different spread in the search space that can be seen from the different values presented on the x1 and x2 axes, one may assume that there is a difference between distributions of the obtained solutions in the search space. To check this, the multivariate E test was used and the p-values for the pairwise comparisons are 0.01 (Cauchy-EDA, MCS), 0.26 (Cauchy-EDA, iAMALGAM), and 0.22 (MCS, iAMALGAM). Because multiple pairwise comparisons are made, these p-values are corrected using the Bonferroni correction, or each p-value is compared with a significance level of 0.02. The results of the comparison are obtained in the matrix `N'_5`, from which further the matrix `N'^2_5` is calculated. The obtained matrices are:

\[
N_5 =
\begin{bmatrix}
1.00 & 0.01 & 0.26 \\
0.01 & 1.00 & 0.22 \\
0.26 & 0.22 & 1.00
\end{bmatrix},
\quad
N'_5 =
\begin{bmatrix}
1.00 & 0.00 & 1.00 \\
0.00 & 1.00 & 1.00 \\
1.00 & 1.00 & 1.00
\end{bmatrix},
\quad
N'^2_5 =
\begin{bmatrix}
2.00 & 1.00 & 2.00 \\
1.00 & 2.00 & 2.00 \\
2.00 & 2.00 & 3.00
\end{bmatrix}.
\]

Only if `N'_5` has a one in each position for which `N'^2_5` has a non-zero element the transitivity is satisfied, which is not the case in our example. The transitivity is also not satisfied because the obtained solutions for Cauchy-EDA and iAMALGAM come from the same distribution in the search space, the obtained solutions for MCS and iAMALGAM come from the same distribution in the search space, but obtained solutions for Cauchy-EDA and MCS are not from the same distribution in the search space. In this case, the rankings are obtained using Eq. (9), for which the hypervolume covered by the distribution needs to be calculated as a measure of the multivariate spread. To calculate this, first the covariance matrix for each algorithm must be calculated from the matrix where the points of the obtained solutions in the search space are stored for that algorithm, `X_{5,l}, l = 1, . . ., 3`. For each algorithm, we then calculate the eigenvalue decomposition of its covariance matrix to obtain the eigenvalues that are needed to calculate the hypervolume for each algorithm. The hypervolumes are 20,775.698 (Cauchy-EDA), 19.166 (MCS), and 84.063 (iAMALGAM). In this example `ν = 0`, so we are interested in a narrow search space. According to these values, the eDSC rankings are 3.00, 1.00 and 2.00. If `ν = 1`, the eDSC rankings would be 1.00, 3.00, and 2.00. So by comparing these three algorithms on f5, we can see that there is no statistical significance between them according to the obtained solutions values, but there is a statistical significance between them according to the distribution of the obtained solutions in the search space.

In the case of the 7th problem, the DSC rankings are 2.00, 2.00, and 2.00. In Fig. 5 the cumulative distribution functions for the obtained solutions values for f7 are presented. It is not clear if there is a statistical significance between the cumulative distribution functions of Cauchy-EDA, MCS, and iAMALGAM. To check this, a two-sample AD test was used with p-values for the pairs of algorithms of 0.39 (Cauchy-EDA, MCS), 0.64 (Cauchy-EDA, iAMALGAM), and 0.05 (MCS, iAMALGAM). Further, these p-values are corrected using the Bonferroni correction, the transitivity of the DSC ranking scheme is satisfied, but the set of all algorithms is not split into disjoint sets because all algorithms belong to one set, `{Cauchy-EDA, MCS, iAMALGAM}`.

For the same problem and for the comparison made according to the distribution of the obtained solutions in the search space, the eDSC rankings are 2.00, 2.00, and 2.00. The contour plots for the probability density functions and cumulative distribution functions of the obtained 2-dimensional solutions for each algorithm for f7 are presented in Figs. 6 and 7, respectively.

It is clear there is no difference between the distributions of the obtained solutions in the search spaces given the similar shape of the distributions and the same spread in the search space. The multivariate E test also proved this by giving p-values for the pairwise comparisons of 0.98 (Cauchy-EDA, MCS), 0.99 (Cauchy-EDA, iAMALGAM), and 0.98 (MCS, iAMALGAM), which were further corrected using the Bonferroni correction. Performing these steps we obtain the following matrices:

\[
N_7 =
\begin{bmatrix}
1.00 & 0.98 & 0.99 \\
0.98 & 1.00 & 0.98 \\
0.99 & 0.98 & 1.00
\end{bmatrix},
\quad
N'_7 =
\begin{bmatrix}
1.00 & 1.00 & 1.00 \\
1.00 & 1.00 & 1.00 \\
1.00 & 1.00 & 1.00
\end{bmatrix},
\quad
N'^2_7 =
\begin{bmatrix}
3.00 & 3.00 & 3.00 \\
3.00 & 3.00 & 3.00 \\
3.00 & 3.00 & 3.00
\end{bmatrix}.
\]

In this case, the transitivity of the matrix `N'_7` is satisfied and the eDSC rankings are obtained using Eq. (7). From here, it follows that all algorithms have the same distribution of obtained solutions in the search space so they are ranked similarly. Comparing the algorithms for f7, there is no statistical significance between them according to the obtained solutions values and their distributions in the search space.

Looking at the 20th problem, the DSC rankings are 3.00, 1.00, and 2.00. In Fig. 8 the cumulative distribution functions for the obtained solutions values for f20 are presented. There is a statistical significance between the cumulative distribution functions of Cauchy-EDA, MCS, and iAMALGAM. This is also proved using the two-sample AD test that gives the p-values: 0.00 (Cauchy-EDA, MCS), 0.00 (Cauchy-EDA, iAMALGAM), and 0.00 (MCS, iAMALGAM).

The eDSC rankings for f20 are 2.00, 2.00, and 2.00. The contour plots of the probability density functions (Fig. 9) and cumulative distribution functions (Fig. 10) of the obtained 2-dimensional data for each algorithm show no difference between the distributions of the obtained solutions in the search space.

This result was also shown using the multivariate E test, which gave p-values of 0.88 (Cauchy-EDA, MCS), 0.88 (Cauchy-EDA, iAMALGAM), and 0.88 (MCS, iAMALGAM).

When comparing the algorithms for f20, there is a statistical significance between the obtained solutions values, but there is no statistical significance between them according to their distribution in the search space. Here we would like to emphasize that having the same distributions in the search space, does not mean that the same, exact solutions were obtained by all algorithms, but only their distribution (space where they are located) is the same. So small differences in locations can translate into statistical significance regarding solution values, which was the case in this example. This tells us that all three algorithms are able to find the same region with good solutions, but one of them is able to find statistically better solutions than the other two from the same region. We can conclude, therefore, that the algorithms have the same exploration power, while MCS has a better exploitation power than the other two algorithms.

When comparing Cauchy-EDA, MCS, and iAMALGAM, three out of four possible scenarios that can happen at the single problem level are presented and explained in detail. The only missing scenario is the scenario in which there is a statistical significance between the performance of the algorithms according to solutions values and their distribution in the search space.

Further, the 7th combination (see Table 1) is selected, in which a statistical comparison is made between the algorithms PSO_Bounds, LSfminbnd, and MCS. The DSC rankings are presented in Table 3a and the eDSC rankings are presented in Table 3b. Here we only focus on the scenario in which there is a statistical significance between the performance of the algorithms according to solutions values and their distributions in the search space. If we focus on the problem f8, the DSC rankings are 2.00, 3.00, and 1.00. In Fig. 11 the cumulative distribution functions for the obtained solutions values for f8 are presented. For better visualization, we used a logarithmic scale on the x-axis. There is a statistical significance between the cumulative distribution functions of PSO_Bounds, LSfminbnd, and MCS, which is further checked using the two-sample AD test. The p-values for the pairs of algorithms are: 0.00 (PSO_Bounds, LSfminbnd), 0.00 (PSO_Bounds, MCS), and 0.00 (LSfminbnd, MCS). These p-values are further corrected using the Bonferroni correction and the transitivity of the DSC ranking scheme is not satisfied, so they obtain different rankings.

To compare the distribution of the obtained solutions in the search space, the eDSC rankings are 1.50, 3.00, and 1.50. The contour plots for the probability density functions and cumulative distribution functions of the obtained 2-dimensional solutions for each algorithm for f8 are presented in Figs. 12 and 13, respectively.

There is no difference between the distributions of the obtained solutions in the search space of PSO_Bounds and MCS, but their distributions differ from the distribution of LSfminbnd. To check this, the multivariate E test was used and the p-values for the pairwise comparisons are 0.01 (PSO_Bounds, LSfminbnd), 0.98 (PSO_Bounds, MCS), and 0.01 (LSfminbnd, MCS). After correcting the p-values and making the comparison, we obtained the following matrices:

\[
N_8 =
\begin{bmatrix}
1.00 & 0.01 & 0.98 \\
0.01 & 1.00 & 0.01 \\
0.98 & 0.01 & 1.00
\end{bmatrix},
\quad
N'_8 =
\begin{bmatrix}
1.00 & 0.00 & 1.00 \\
0.00 & 1.00 & 0.00 \\
1.00 & 0.00 & 1.00
\end{bmatrix},
\quad
N'^2_8 =
\begin{bmatrix}
2.00 & 0.00 & 2.00 \\
0.00 & 1.00 & 0.00 \\
2.00 & 0.00 & 2.00
\end{bmatrix}.
\]

The transitivity of the matrix `N'_8` is satisfied, so the set of algorithms is split into two disjoint sets of algorithms, `{PSO_Bounds, MCS}` and `{LSfminbnd}`. The eDSC rankings are obtained using Eq. (7), for which the hypervolume covered by the distribution is calculated as a measure of the multivariate spread. In this example, we need to calculate the hypervolume for each set. For the first set, we need to calculate the hypervolume only for one algorithm since they have the same distribution and the hypervolumes of the algorithms that belong to this set are only in some small ε-neighborhood. The hypervolumes for each set of algorithms are 0.829 `{PSO_Bounds, MCS}` and 5.601 `{LSfminbnd}`. In this example `ν = 0`, so we are interested in a narrow search space. The eDSC rankings are 1.50, 3.00 and 1.50. If `ν = 1`, the eDSC rankings would be 2.50, 1.00 and 2.50. Comparing these three algorithms for f8, there is a statistical significance between the algorithms according to the obtained solutions values, and there is also a statistical significance according to their distribution in the search space.

**Table 3. Rankings for the algorithms PSO_Bounds, LSfminbnd, and MCS.**

| F | PSO_Bounds | LSfminbnd | MCS |
|---|---:|---:|---:|
| *a) DSC ranking scheme* ||||
| f1 | 3.00 | 2.00 | 1.00 |
| f2 | 2.00 | 1.00 | 3.00 |
| f3 | 2.00 | 3.00 | 1.00 |
| f4 | 1.50 | 3.00 | 1.50 |
| f5 | 2.00 | 2.00 | 2.00 |
| f6 | 1.50 | 3.00 | 1.50 |
| f7 | 1.50 | 3.00 | 1.50 |
| f8 | 2.00 | 3.00 | 1.00 |
| f9 | 2.00 | 3.00 | 1.00 |
| f10 | 2.00 | 3.00 | 1.00 |
| f11 | 2.50 | 2.50 | 1.00 |
| f12 | 2.00 | 3.00 | 1.00 |
| f13 | 1.00 | 2.50 | 2.50 |
| f14 | 1.00 | 3.00 | 2.00 |
| f15 | 2.00 | 3.00 | 1.00 |
| f16 | 3.00 | 2.00 | 1.00 |
| f17 | 1.00 | 3.00 | 2.00 |
| f18 | 1.00 | 3.00 | 2.00 |
| f19 | 1.50 | 3.00 | 1.50 |
| f20 | 2.00 | 3.00 | 1.00 |
| f21 | 3.00 | 2.00 | 1.00 |
| f22 | 3.00 | 2.00 | 1.00 |

| F | PSO_Bounds | LSfminbnd | MCS |
|---|---:|---:|---:|
| *b) eDSC ranking scheme* ||||
| f1 | 2.00 | 2.00 | 2.00 |
| f2 | 2.00 | 2.00 | 2.00 |
| f3 | 2.00 | 2.00 | 2.00 |
| f4 | 2.00 | 2.00 | 2.00 |
| f5 | 2.00 | 2.00 | 2.00 |
| f6 | 2.00 | 2.00 | 2.00 |
| f7 | 2.00 | 2.00 | 2.00 |
| f8 | 1.50 | 3.00 | 1.50 |
| f9 | 2.00 | 2.00 | 2.00 |
| f10 | 2.00 | 3.00 | 1.00 |
| f11 | 2.00 | 2.00 | 2.00 |
| f12 | 2.00 | 2.00 | 2.00 |
| f13 | 2.00 | 2.00 | 2.00 |
| f14 | 2.00 | 2.00 | 2.00 |
| f15 | 2.00 | 2.00 | 2.00 |
| f16 | 2.00 | 2.00 | 2.00 |
| f17 | 2.00 | 2.00 | 2.00 |
| f18 | 2.00 | 2.00 | 2.00 |
| f19 | 2.00 | 2.00 | 2.00 |
| f20 | 2.00 | 2.00 | 2.00 |
| f21 | 2.00 | 2.00 | 2.00 |
| f22 | 2.00 | 2.00 | 2.00 |

#### 4.2.2. Comparison of three algorithms with `d = 10`

Again, 100 random combinations without repetition were generated and used for statistical comparisons. Table 4 presents the p-values for 10 selected combinations. The data for each combination are generated using the DSC and eDSC ranking scheme, respectively. For each combination, the Friedman test was used as an appropriate omnibus statistical test.

The first 5 combinations (1–5) tell us that there is no statistical significance between the performance of the algorithms according to the obtained solutions values, and there is also no statistical significance between the performance of the algorithms according to the distribution of the obtained solutions in the search space and their number is 20 out of 100. The next 5 combinations (6–10) tell us that there is a statistical significance between the performance of the algorithms according to the obtained solutions values over multiple problems but there is no statistical significance between the performance of the algorithms according to their distribution in the search space and their number is 80 out of 100. The explanation of these results for a single problem level is the same as in the case when the dimension is 2, `d = 2`.

**Table 4. Statistical comparisons of 3 algorithms.**

| # | Algorithms | pvalueY | pvalueX |
|---|---|---:|---:|
| 1 | Cauchy-EDA, POEMS, GA | (.19) | (.90) |
| 2 | POEMS, FULLNEWUOA, EDA-PSO | (.47) | (.95) |
| 3 | GA, PSO, FULLNEWUOA | (.58) | (.80) |
| 4 | EDA-PSO, FULLNEWUOA, NELDERDOERR | (.41) | (.95) |
| 5 | Rosenbrock, PSO, PSO_Bounds | (.08) | (.66) |
| 6 | Rosenbrock, PSO, G3PCX | *(.01) | (.73) |
| 7 | NELDERDOERR, LSstep, PSO | *(.00) | (.80) |
| 8 | LSstep, VNS, Cauchy-EDA | *(.00) | (.49) |
| 9 | PSO_Bounds, iAMALGAM, LSstep | *(.00) | (.31) |
| 10 | EDA-PSO, PSO, POEMS | *(.02) | (.95) |

\* Indicates that the null hypothesis is rejected, using `α = 0.05`.  
`pvalueY` corresponds to the obtained p-value for comparing the obtained solutions values by the Friedman test.  
`pvalueX` corresponds to the obtained p-value for comparing distributions of the obtained solutions in the search space by the Friedman test.

#### 4.2.3. Comparison of 10 algorithms

In the third experiment, multiple comparisons with a control algorithm are presented. For this reason, 10 algorithms were selected and a comparison was made with one of them against the other 9 algorithms. The compared algorithms were: Cauchy-EDA, POEMS, GA, PSO_Bounds, VNS, LSfminbnd, NELDERDOERR, PSO, EDA-PSO, and AMALGAM.

Since, the DSC and eDSC ranking schemes are based on comparing distributions, multiple pairwise comparisons are made and the p-values are corrected by the Bonferroni correction in order to control the FWER. However, the correction comes at the cost of increasing the probability of producing false negatives, or reducing the statistical power [17]. This is a general criticism, which can be applied to any FWER control approach and it is not specific only to the Bonferroni correction. When the number of algorithms involved in the comparison increases, the correction can influence the rankings. More information about this is presented in [12].

To avoid this, the best way to perform multiple comparisons with a control algorithm is to apply multiple Wilcoxon tests for each pairwise comparison. The Wilcoxon test performs a comparison between the two algorithms. The p-values in pairwise comparisons are independent from each other when we are performing multiple comparisons with a control algorithm (i.e., one vs. all). If we try to extract a conclusion by using a larger number of pairwise comparisons, we accumulate error arising from combining pairwise comparisons, and consequently we lose control of the FWER. The true statistical significance [18] for combining pairwise comparisons is given by

\[
pvalue = 1 - \prod_{i=1}^{k-1} [1 - pvalue_{H_i}].
\tag{10}
\]

The p-values using the Wilcoxon test for each hypothesis, when a comparison is made according to the obtained solutions values, are presented in Table 5a, while the p-values using the Wilcoxon test for each hypothesis, when the comparison is made according to the distribution of the obtained solutions in the search spaces, are presented in Table 5b.

**Table 5. Multiple comparisons with a control algorithm (VNS) by using multiple Wilcoxon tests.**

| j | VNS vs. | pvalue |
|---|---|---:|
| *a) DSC ranking scheme* |||
| 1 | Cauchy-EDA | 1.1140e-03 |
| 2 | POEMS | 1.0570e-04 |
| 3 | GA | 2.1813e-05 |
| 4 | PSO_Bounds | 6.23780e-05 |
| 5 | LSfminbnd | 6.9214e-04 |
| 6 | NELDERDOERR | 5.1880e-02 |
| 7 | PSO | 3.6864e-05 |
| 8 | EDA-PSO | 3.7595e-04 |
| 9 | AMALGAM | 2.3572e-01 |

| j | VNS vs. | pvalue |
|---|---|---:|
| *b) eDSC ranking scheme* |||
| 1 | Cauchy-EDA | 2.3303e-01 |
| 2 | POEMS | 4.2371e-01 |
| 3 | GA | 7.7282e-01 |
| 4 | PSO_Bounds | 7.7282e-01 |
| 5 | LSfminbnd | 7.7282e-01 |
| 6 | NELDERDOERR | 1.0000e+00 |
| 7 | PSO | 1.0000e+00 |
| 8 | EDA-PSO | 7.7282e-01 |
| 9 | AMALGAM | 3.4577e-01 |

Before the FWER is not controlled (Table 5a), one would assume that the VNS algorithm has a statistically significant performance, according to the obtained solutions values, than the following 8 algorithms: Cauchy-EDA, POEMS, GA, PSO_Bounds, LSfminbnd, PSO, and EDA-PSO, with a significance level `α = 0.05`, but this incorrect. The VNS algorithm has a statistically significant performance than each of the 8 algorithms, separately, since the p-values are smaller than `α = 0.05`. The true statistical significance for combining pairwise comparisons for these 8 hypotheses can be obtained using Eq. (10), which in our case is 0.002, and is smaller than the significance level used `α = 0.05`. From this we can conclude that the VNS has statistically significant performance than the 8 algorithms, according to the obtained solutions values.

Similarly the conclusion is that the VNS algorithm has a statistically significant performance, according to the distribution of the obtained solutions in the search space, compared to Cauchy-EDA, POEMS, GA, PSO_Bounds, LSfminbnd, NELDERDOERR, PSO, EDA-PSO, and AMALGAM, with a significance level `α = 0.05` is incorrect (Table 5). The VNS algorithm is not statistically significant from each of the 9 algorithms when considering independent pairwise comparisons because the p-values are greater than `α = 0.05`. The true statistical significance for combining pairwise comparisons for these 9 hypotheses can be obtained using Eq. (10), which in our case is 1.00 and we can conclude that the performance of the VNS is not statistically significant than the other 9 algorithms, according to the distribution of the obtained solutions in the search space.

## 5. Discussion

The distribution of the found solutions over the problem space is mostly ignored, which is not the case for the proposed eDSC approach. Using information about the solutions’ search space distribution can provide additional information about the strengths and weaknesses of the compared algorithms with regard to their exploitation and exploration powers. In theory and also from the experimental results, four scenarios are possible, when making a comparison between the obtained solutions according to its values and its distribution.

The first is when the compared algorithms are either equal or there is no statistical significance between them according to the obtained solutions values and their distributions in the search space. An example of this scenario can be seen in Section 4.2.1, in the comparison made between Cauchy-EDA, MCS, and iAMALGAM for f7. A comparison of the algorithms for this problem shows that they have the same exploitation and exploration power.

The second scenario is when the compared algorithms are not statistically significant with regard to the obtained solutions values, but they are statistically significant according to their distribution in the search space. An example of this scenario is seen in Section 4.2.1, in the comparison made between Cauchy-EDA, MCS, and iAMALGAM for f5. From this example, we can assume that the compared algorithms have the same exploitation power, but different exploration powers. In this case, the algorithm preference needs to be determined according to the user needs (sparse or clustered solutions). In this example, the preference is on clustered solutions, so the algorithm that has the narrowest distribution is the best one (i.e., MCS). If the algorithm preference is changed to sparse solutions, it follows that Cauchy-EDA has the best exploration power. So by altering our preference, we can identify which algorithm is best suited to our needs not only with regard to the quality of the solutions but also to their distribution in the search space. This distinction is very useful in real-world cases. The third scenario is when the performances of the compared algorithms are statistically significant regarding the obtained solutions values, but have the same distribution of the obtained solutions in the search space. An example of it is shown in Section 4.2.1, in the comparison made between Cauchy-EDA, MCS, and iAMALGAM for f20. From this example, it follows that the compared algorithms have different exploitation powers, but the same exploration power. This example also provides us the information that all three algorithms are able to find a region with good solutions, but only one of them is able to find statistically better solutions than the other two in the same region. In this example, MCS is able to find statistically better solutions in the same region than Cauchy-EDA and iAMALGAM.

The last scenario is when the compared algorithms are statistically significant regarding the obtained solutions values and their distributions in the search space. An example of this scenario is shown in Section 4.2.1, in the comparison of PSO_Bounds, LSfminbnd, and MCS for f8. The rankings obtained comparing them regarding the obtained solution values are 2.00, 3.00, and 1.00, while the rankings regarding the comparison according to the distribution of the obtained solutions are 1.50, 3.00, and 1.50. PSO_Bounds and MCS are able to find a region of good solutions as shown by the distribution rankings, but MCS is able to find statistically better solutions than PSO_Bounds in the same region and so has a better exploitation power. However, both algorithms have better exploration power than the LSfminbnd. LSfminbnd could not find a region with good solutions, which prevents us from determining its exploitation power.

Such analyses can be helpful either for users of optimization algorithms or developers, who would like information about what their algorithm lacks. These kind of analyses could turn out to be especially useful in analyzing and understanding algorithms that are applied to large-scale continuous optimization problems, which is currently one of the most active research areas in optimization [27,29,31,32,35]. In large-scale dimensional problems, compared to low-dimensional problems, it is even harder to understand the reasons for the differences in performances of the compared algorithms, due to enormous sizes and complexities of hundred or even thousand dimensional search spaces. In [41], the authors showed that the multivariate E-test, which is used in eDSC ranking scheme, can be successfully applied on hundred dimensional search spaces. The theory behind it also covers higher dimensional search spaces, however this yet needs to be proven with experiments.

Another possible usage of the proposed approach is to estimate how the search ability of the algorithms depends on either their initial conditions or on the parameters. For this purpose we can take one algorithm with different initial conditions, so we will have different instances of the same algorithm because they differ in the initial conditions. Next we can treat each instance as a different algorithm, so using the proposed approach we can compare them in order to see which of the initial conditions give the best results. This can be on a single problem level, or also for a multiple-problem scenario in order to give some more general explanation. The same can be also made for different parameters in order to see how the parameters influence the search ability of an algorithm.

The real advantage of this approach is in the transformation of the data because it can provide more robust statistical results. In most cases a diversity-based performance metric is defined as a real number that is a metric (i.e., a mathematical function) that transforms the high-dimensional data into a scalar value. For example, let us assume that as a diversity-based performance metric (i.e., a measure for multivariate spread), a hypervolume of the distribution is used. However it can happen that the distributions of the obtained solutions in the search space for two algorithms are the same, but the hypervolumes of the algorithms are in some small insignificant ε-neighborhood. If this data is further included in some omnibus statistical test, let us assume a nonparametric one, no matter the size/level of insignificant difference, the algorithms will be ranked differently by the fractional ranking scheme used by most of the nonparametric statistical tests. However, they have the same distribution and they need to be ranked as the same. For example, let us assume that we compare three algorithms, of which the first and the second have the same distribution of the obtained solutions in the search space, which differs from the distribution of the third one, and the obtained hypervolumes are: 0.829, 0.830, and 5.601. Using the fractional ranking scheme they will be ranked as 1.00, 2.00, and 3.00, however they need to be ranked as 1.50, 1.50, and 3.00. These rankings obtained on one benchmarking problem influence the test statistic of the selected omnibus statistical test and the end result of the comparison. Further, the question arises if the information about the ε-neighborhood can be included as a priori information. This is a difficult task because each benchmarking problem has a different search space with regard to the data range of each dimension, so a unique ε-neighborhood for each benchmarking problem does not exist, and even if the search spaces are normalized it will still be an open question. By comparing distributions of the obtained solutions in the search space, ε-neighborhood is dynamically handled for each benchmarking problem without having a priori information about the problem to be solved.

Because the key idea behind the eDSC ranking scheme is comparing distributions in high-dimensions, we used the multivariate E-test, which is one of the most powerful tests available for high dimensional data. Its sensitivity analysis and its comparison with other statistical tests are presented in [41]. However, there is also a theoretical explanation on how this test is able to detect a difference between two distributions. To find a statistical significance between distributions in the search space of two algorithms, the E test should reject the null hypothesis. This will happen when the test statistic, which is used by this test is greater than a critical value for a given significance level:

\[
E_{n_1,n_2} > c_\alpha,
\tag{11}
\]

where `n1` and `n2` are the numbers of points in the search space obtained from both algorithms, respectively, and `c_α` is a critical value.

Let us assume that `x_1, ... , x_{n_1}` and `x'_1, ... , x'_{n_2}` are locations of the obtained solutions in the search space `R^d, d ≥ 2`, that are obtained by two algorithms. In this case, the two-sample test statistic is defined as

\[
\mathcal{E}_{n_1,n_2} =
\frac{n_1n_2}{n_1+n_2}
\left(
\frac{2}{n_1n_2}\sum_{i=1}^{n_1}\sum_{j=1}^{n_2}\|x_i - x'_j\|
-
\frac{1}{n_1^2}\sum_{i=1}^{n_1}\sum_{j=1}^{n_1}\|x_i - x_j\|
-
\frac{1}{n_2^2}\sum_{l=1}^{n_2}\sum_{j=1}^{n_2}\|x'_l - x'_j\|
\right).
\tag{12}
\]

The first double sum in the above equation gives the distance between locations of the obtained solutions in the search space from both algorithms, the second double sum gives the so-called within distance between the locations of the obtained solutions in the search space from one algorithm, and the third double sum gives the within distance between the locations of the obtained solutions in the search space from the other algorithm. It is theoretically shown that this test statistic has a degenerate two-sample V-statistic and there exists a constant `c_α` satisfying `\lim_{n\to+\infty} P( \frac{n_1n_2}{n_1+n_2} V_{n_1,n_2} > c_α ) = α` when the test will reject the null hypothesis [30]. The theoretical explanation is, that the test will detect a statistical significance when the multivariate E-distance, or the subtraction of the sum of both within distances from the between distance should be greater than a critical value, which can be calculated from a degenerate two-sample V-statistic for a given significance level `α`.

The source code of eDSC ranking scheme is publicly available at http://cs.ijs.si/dl/scripts/eDSC.R.

## 6. Power analysis

The power of a statistical test is defined as the probability that the test will (correctly) reject the false null hypothesis. In this paper we did not focus on power analysis because the power analysis of the DSC approach for one-dimensional data is presented in our previous work [12]. The comparison of the statistical power of the two-sample KS test and the two-sample AD test is presented in [14]. The power analysis for the multivariate E test and its comparisons with some other neighbor statistical tests are presented in [25], where the authors show that it is one of the most powerful tests for comparing distributions in high-dimensions. In the same paper, the authors also presented what kind of differences between distributions can be detected.

## 7. Conclusion

In this paper, a novel approach to statistical comparison of stochastic optimization algorithms, known as extended Deep Statistical Comparison (eDSC), is introduced. The main contribution of the proposed approach is that the algorithms are not compared only according to the obtained solutions values, but also according to the distribution of the obtained solutions in the search space. The eDSC ranking scheme can be used to determine solutions spread according to user’s needs and also for identifying exploitation and exploration powers of the compared algorithms. The approach consists of two parts, a comparison according to the obtained solutions values and a comparison according to the distribution of the obtained solutions in the search space. An evaluation of the eDSC approach performed using the results from the Black-Box Benchmarking 2009 (BBOB 2009) shows that DSC and eDSC give promising results and can be used for statistical comparison of meta-heuristic stochastic optimization algorithms.

For our future work we are planning to evaluate if the eDSC approach can be successfully applied to large-scale continuous optimization problems. We will also investigate the application of the eDSC idea for the identification of exploration and exploitation level of the population-based algorithm at every iteration. This information could be used for more efficient online tuning of the algorithm. Additionally, we plan to investigate if the eDSC approach or a modification of it can be used for making statistical comparisons in combinatorial optimization and multi-objective optimization.

## Acknowledgment

This work was supported by the project from the Javna Agencija za Raziskovalno Dejavnost RS (research core funding No. P2-0098) and from the European Union’s Horizon 2020 research and innovation program under grant agreement No. 692286.

## References

[1] T. Bartz-Beielstein, How to create generalizable results, in: *Springer Handbook of Computational Intelligence*, Springer, 2015, pp. 1127–1142.

[2] T. Bartz-Beielstein, M. Preuss, M. Zaefferer, Statistical analysis of optimization algorithms with R, in: *Proceedings of the 14th annual conference companion on Genetic and evolutionary computation*, ACM, 2012, pp. 1259–1286.

[3] D. Bates, M. Maechler, *Matrix: Sparse and Dense Matrix Classes and Methods*, 2017. R package version 1.2–8.

[4] B. Calvo, G. Santafe, Scmamp: statistical comparison of multiple algorithms in multiple problems, *R. J.* 15 (6) (2015) 848–870.

[5] E.G. Carrano, E.F. Wanner, R.H. Takahashi, A multicriteria statistical based comparison methodology for evaluating evolutionary algorithms, *IEEE Trans. Evol. Comput.* 15 (6) (2011) 848–870.

[6] V. Černý, Thermodynamical approach to the traveling salesman problem: an efficient simulation algorithm, *J. Optim. Theory Appl.* 45 (1) (1985) 41–51.

[7] G.B. Dantzig, R.W. Cottle, *Positive (Semi-)Definite Matrices and Mathematical Programming*, Technical Report, DTIC Document, 1963.

[8] S. Das, Evaluating the evolutionary algorithms - classical perspectives and recent trends, in: H. Ishibuchi (Ed.), *Computational Intelligence*, vol. I, EOLSS, 2013, pp. 297–333.

[9] J. Derrac, S. García, S. Hui, P.N. Suganthan, F. Herrera, Analyzing convergence performance of evolutionary algorithms: a statistical approach, *Inf. Sci.* 289 (2014) 41–58.

[10] J. Derrac, S. García, D. Molina, F. Herrera, A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms, *Swarm. Evol. Comput.* 1 (1) (2011) 3–18.

[11] A. Edelman, N.R. Rao, Random matrix theory, *Acta Numerica* 14 (2005) 233–297.

[12] T. Eftimov, P. Korošec, B.K. Seljak, A novel approach to statistical comparison of meta-heuristic stochastic optimization algorithms using deep statistics, *Inf. Sci.* 417 (2017) 186–215.

[13] T. Eftimov, P. Korošec, B. Koroušić Seljak, The behavior of deep statistical comparison approach for different criteria of comparing distributions, in: *Proceedings of the 9th International Conference on Computational Intelligence (IJCCI 2017)*, 1, 2017, pp. 73–82.

[14] S. Engmann, D. Cousineau, Comparing distributions: the two-sample Anderson-Darling test as an alternative to the Kolmogorov–Smirnov test, *J. Appl. Quantit. Methods* 6 (3) (2011) 1–17.

[15] I.K. Fodor, A survey of dimension reduction techniques, Lawrence Livermore National Lab., CA (US), 2002.

[16] J.N. Franklin, *Matrix Theory*, Courier Corporation, 2012.

[17] S. García, A. Fernández, J. Luengo, F. Herrera, Advanced nonparametric tests for multiple comparisons in the design of experiments in computational intelligence and data mining: experimental analysis of power, *Inf. Sci.* 180 (10) (2010) 2044–2064.

[18] S. García, D. Molina, M. Lozano, F. Herrera, A study on the use of non-parametric tests for analyzing the evolutionary algorithms behaviour: a case study on the CEC2005 special session on real parameter optimization, *J. Heuristics* 15 (6) (2009) 617–644.

[19] J.L. Gastwirth, Y.R. Gel, W.L. Wallace Hui, V. Lyubchich, W. Miao, K. Noguchi, *lawstat: Tools for Biostatistics, Public Policy, and Law*, 2015. R package version 3.0.

[20] C.J. Geyer, Markov Chain Monte Carlo Maximum Likelihood (1991).

[21] V. Gontscharuk, *Asymptotic and Exact Results on FWER and FDR in Multiple Hypotheses Testing*, Ph.D. dissertation, Heinrich-Heine-Universität Düsseldorf, 2010.

[22] N. Hansen, A. Auger, O. Mersmann, T. Tusar, D. Brockhoff, Coco: a platform for comparing continuous optimizers in a black-box setting, arXiv:1603.08785 (2016).

[23] N. Hansen, A. Auger, R. Ros, S. Finck, P. Pošík, Comparing results of 31 algorithms from the black-box optimization benchmarking BBOB-2009, in: *Proceedings of the 12th annual conference companion on Genetic and evolutionary computation*, ACM, 2010, pp. 1689–1696.

[24] N. Hansen, S. Finck, R. Ros, A. Auger, *Real-Parameter Black-Box Optimization Benchmarking 2009: Noiseless Functions Definitions*, INRIA, 2009.

[25] N. Henze, A multivariate two-sample test based on the number of nearest neighbor type coincidences, *Ann. Stat.* (1988) 772–783.

[26] N.J. Higham, Computing the nearest correlation matrix—a problem from finance, *IMA J. Numer. Anal.* 22 (3) (2002) 329–343.

[27] X.-M. Hu, F.-L. He, W.-N. Chen, J. Zhang, Cooperation coevolution with fast interdependency identification for large scale optimization, *Inf. Sci.* 381 (2017) 142–160.

[28] I. Jolliffe, *Principal Component Analysis*, Wiley Online Library, 2002.

[29] A. LaTorre, S. Muelas, J.-M. Peña, A comprehensive comparison of large scale global optimizers, *Inf. Sci.* 316 (2015) 517–549.

[30] A. Leucht, M.H. Neumann, Consistency of general bootstrap methods for degenerate u-type and v-type statistics, *J. Multivar. Anal.* 100 (8) (2009) 1622–1633.

[31] X. Li, K. Tang, P.N. Suganthan, Z. Yang, Editorial for the special issue of information sciences journal (ISJ) on nature-inspired algorithms for large scale global optimization, *Inf. Sci.* 316 (C) (2015) 437–439.

[32] M. Lozano, D. Molina, F. Herrera, Editorial scalability of evolutionary algorithms and other metaheuristics for large-scale continuous optimization problems, *Soft Comput.* 15 (11) (2011) 2085–2087.

[33] L. Martino, V. Elvira, D. Luengo, J. Corander, F. Louzada, Orthogonal parallel MCMC methods for sampling and optimization, *Digit. Signal Process.* 58 (2016) 64–84.

[34] O. Mersmann, M. Preuss, H. Trautmann, Benchmarking evolutionary algorithms: Towards exploratory landscape analysis, in: *International Conference on Parallel Problem Solving from Nature*, Springer, 2010, pp. 73–82.

[35] M.N. Omidvar, X. Li, K. Tang, Designing benchmark problems for large-scale continuous optimization, *Inf. Sci.* 316 (2015) 419–436.

[36] R Core Team, *R: A Language and Environment for Statistical Computing*, R Foundation for Statistical Computing, Vienna, Austria, 2015.

[37] M.L. Rizzo, G.J. Szekely, *energy: E-Statistics: Multivariate Inference via the Energy of Data*, 2016. R package version 1.7-0.

[38] M.F. Schilling, Multivariate two-sample tests based on nearest neighbors, *J. Am. Stat. Assoc.* 81 (395) (1986) 799–806.

[39] F. Scholz, A. Zhu, *kSamples: K-Sample Rank Tests and their Combinations*, 2016. R package version 1.2–4.

[40] D. Shilane, J. Martikainen, S. Dudoit, S.J. Ovaska, A general framework for statistical performance comparison of evolutionary computation algorithms, *Inf. Sci.* 178 (14) (2008) 2870–2879.

[41] G.J. Székely, M.L. Rizzo, Testing for equal distributions in high dimension, *InterStat* 5 (2004) 1–6.

[42] N. Veček, M. Mernik, M. Crepinšek, A chess rating system for evolutionary algorithms: a new method for the comparison and ranking of evolutionary algorithms, *Inf. Sci.* 277 (2014) 656–679.

[43] X.-S. Yang, Firefly algorithms for multimodal optimization, in: *International symposium on stochastic algorithms*, Springer, 2009, pp. 169–178.
