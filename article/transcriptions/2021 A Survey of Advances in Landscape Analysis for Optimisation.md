# A Survey of Advances in Landscape Analysis for Optimisation

**Author:** Katherine Mary Malan  
**Journal:** *Algorithms*  
**Year:** 2021  
**Volume / Article:** 14, 40  
**DOI:** https://doi.org/10.3390/a14020040  
**Pages:** 16

---

## Document metadata

- **Title:** A Survey of Advances in Landscape Analysis for Optimisation
- **Author:** Katherine Mary Malan
- **Journal:** *Algorithms*
- **Year:** 2021
- **Volume / Article:** 14, 40
- **DOI:** https://doi.org/10.3390/a14020040
- **Publisher:** MDPI
- **License:** CC BY 4.0

---

## Notes

This Markdown file is a **source-faithful transcription** of the PDF text, cleaned for OCR artifacts and formatting issues.

Editorial notes:

- Obvious OCR corruption from ligatures/hidden characters has been corrected.
- Decorative icons and non-text journal graphics were omitted.
- Some source-level inconsistencies in the paper have been preserved exactly as printed.
  - Example: on page 7, the paper refers to ELA as “technique 26 in Table 1”, although ELA is listed earlier as Technique 24.

---

## Page 1

**algorithms**  
**Article**

# A Survey of Advances in Landscape Analysis for Optimisation

**Katherine Mary Malan**

Citation: Malan, K.M. A Survey of Advances in Landscape Analysis for Optimisation. *Algorithms* **2021**, *14*, 40.  
https://doi.org/10.3390/a14020040

Received: 30 November 2020  
Accepted: 11 January 2021  
Published: 28 January 2021

Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Copyright: © 2021 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

Department of Decision Sciences, University of South Africa, Pretoria 0002, South Africa; malankm@unisa.ac.za

**Abstract:** Fitness landscapes were proposed in 1932 as an abstract notion for understanding biological evolution and were later used to explain evolutionary algorithm behaviour. The last ten years has seen the field of fitness landscape analysis develop from a largely theoretical idea in evolutionary computation to a practical tool applied in optimisation in general and more recently in machine learning. With this widened scope, new types of landscapes have emerged such as multiobjective landscapes, violation landscapes, dynamic and coupled landscapes and error landscapes. This survey is a follow-up from a 2013 survey on fitness landscapes and includes an additional 11 landscape analysis techniques. The paper also includes a survey on the applications of landscape analysis for understanding complex problems and explaining algorithm behaviour, as well as algorithm performance prediction and automated algorithm configuration and selection. The extensive use of landscape analysis in a broad range of areas highlights the wide applicability of the techniques and the paper discusses some opportunities for further research in this growing field.

**Keywords:** fitness landscape; landscape analysis; violation landscape; error landscape; automated algorithm selection

## 1. Introduction

This survey is a follow-up from a previous survey published in *Information Sciences* journal in 2013 [1]. Back then, the field of fitness landscape analysis was not very active in the evolutionary computation community. The article states “despite extensive research on fitness landscape analysis and a large number of developed techniques, very few techniques are used in practice . . . It is hoped that this survey will invoke renewed interest in the field of understanding complex optimisation problems and ultimately lead to better decision making on the use of appropriate metaheuristics.” [1]. The hope of renewed interest in the field of fitness landscape analysis has indeed been realised, evident in the increase in the number of published papers on the topic as well as the appearance of tutorials, workshops and special sessions dedicated to this topic at all the major evolutionary computation conferences.

One of the changes that has emerged in the last few years is that the notion of fitness landscapes has been extended to include new types of landscapes such as multiobjective fitness landscapes, violation landscapes, dynamic and coupled landscapes and error or loss landscapes in the context of neural network training. These notions are discussed in Section 2.

A number of new techniques for analysing landscapes have been developed and these are described as an extension to the original survey [1] in Section 3, followed by a summary of contributions related to sampling and robustness of measures.

Landscape analysis has been applied widely for different purposes from the understanding of complex problems and algorithm behaviour, to predicting algorithm performance and automated algorithm selection. Section 4 provides a survey of these applications and highlights the value of landscape analysis in addressing the challenge of solving complex optimisation problems and Section 5 discusses some ideas for further research in landscape analysis.

---

## Page 2

# 2. Beyond Fitness Landscapes

The notion of a fitness landscape was introduced by Sewell Wright [2] at a congress on genetics in 1932. He proposed an abstract two-dimensional contour plot of fitness values as an intuitive picture of evolutionary processes taking place in high dimensional space. Because fitness landscapes have been used in contexts beyond biological and computational evolution, the fitness metaphor is no longer generally applicable and many studies have opted for more general terms such as *search space analysis*, *exploratory landscape analysis* or just *landscape analysis*.

A fitness landscape was originally defined as consisting of three elements [3]: (1) A set X of potential solutions to the problem; (2) a notion of neighbourhood, nearness, distance or accessibility on X, and (3) a fitness function \(f : X \to R\). Replacing \(f\) with a more general objective function, these three basic elements can be used to describe landscapes in a wide range of contexts such as combinatorial optimisation, continuous optimisation, search spaces of programs (as in genetic programming) and so on. There are some contexts, however, where these elements differ further from the original definition and these are discussed in this section.

### 2.1. Multiobjective Fitness Landscapes

Multiobjective optimisation differs from single objective optimisation at both the objective level (multiple fitness functions for each conflicting objective versus a single fitness function) and the solution-level (set of Pareto optimal solutions in the multiobjective case versus a single optimal solution in the single objective case). Verel et al. [4] propose a definition for multiobjective fitness landscapes where solutions are solution-sets, neighbourhood is defined using set-level operators and fitness is defined using a multiobjective quality measure. This formulation presents a completely different landscape from the fitness landscapes of the individual objectives but is arguably a more meaningful landscape to analyse when objectives are conflicting.

### 2.2. Violation Landscapes

Malan et al. [5] introduced the notion of a violation landscape as an additional view to fitness landscapes for constrained search spaces. A violation landscape is defined using the same elements as a fitness landscape, but the fitness function is replaced by a violation function that quantifies the extent to which a solution violates the constraints defined on the problem. A violation landscape is therefore defined above decision variable space and provides an additional landscape view to the fitness landscape. The features of violation landscapes can be analysed in relation to fitness landscapes to better understand constrained optimisation problems. Technique 28 in Table 1 describes metrics for characterising violation landscapes in relation to fitness landscapes.

### 2.3. Dynamic and Coupled Fitness Landscapes

Most landscape analysis assumes that the environment is constant, but there are many problems where the landscape is dynamic. Two scenarios where the dynamics of landscapes have been studied include applications where the objective function changes over time (due to changes in the problem environment) and in the case of coevolution, where landscapes are coupled [6] and influence each other.

An early approach to dynamic landscape analysis involved using existing landscape analysis techniques and simply interspersing landscape changes at set intervals during the search space sampling [6]. As an alternative, Richter [7,8] proposed using coupled map lattices for constructing fitness landscapes and modelling landscape dynamics. This framework was used to characterise landscape features (such as ruggedness and epistasis) over time as well as features specific to dynamic landscapes, such as change frequency and dynamic severity. Yazdani et al. [9] proposed an online approach to dynamic landscape analysis using a multipopulation method. In their framework, metrics are calculated based

---

## Page 3

on information collected by subpopulations tracking peaks for quantifying changes in the landscape (peak shift severity, height variance and fitness variance).

In the context of coevolution, there are two distinct landscapes to consider: the objective landscape (the view of the problem to be solved) and the subjective landscape (the coevolutionary algorithm’s view on the problem) [10]. It has been suggested that failure of coevolutionary algorithms could be due to disassociation between these two landscapes [11]. For coevolutionary games, Richter [12] proposed a dynamic landscape model based on a fitness interpretation of player payoff and used existing fitness landscape analysis techniques to analyse the game dynamics.

### 2.4. Error Landscapes

Part of neural network (NN) training involves optimisation, where the task is to search for the weight values that minimise the error of the network model on the training data. Analogous to a fitness landscape, the error or loss landscape can be analysed to better understand the nature of a particular NN weight optimisation problem instance. There are, however, some aspects of NN weight optimisation that make it different from most black-box optimisation problems and this affects the way that landscape analysis can be done.

Some of the distinguishing characteristics of NN weight optimisation are: ultra high-dimensional search spaces (even small NN models can have thousands of weights), expensive objective evaluation (evaluating the error value of a solution weight vector involves a full run through the training data set), unbounded search spaces (weights can theoretically take on any real value), the same solution can evaluate to different error values depending on the subset of data instances used for training and the availability of analytical gradient information of the objective function. In addition, there is the added complication that the NN training landscape may differ from the NN testing landscape. Choromanska et al. [13] theoretically and empirically analysed the loss surfaces of multilayered neural networks and found that the training and testing error became increasingly de-correlated with the size of the network. The implication of this is that finding the global optimum in the training loss landscape is of limited use, because it will most likely not correspond with the position of the global optimum in the testing loss landscape. This presents a different picture than with most other optimisation tasks, where the focus is usually on finding the global optimum within the landscape.

Dimension reduction techniques have been proposed for visualising portions of error surfaces [14,15]. For example, three-dimensional visualisations of error landscapes (https://losslandscape.com/) are based on samples of weight vectors that fall on a two-dimensional plane (a slice through the multidimensional weight space). The plane is positioned to pass through a point in the search space around which the landscape is visualised (such as the weight vector at the end of a training run). These visualisations provide a limited view that may not match the experience of a training algorithm in the high dimensional weight space. In addition, a form of numerical characterisation of error landscapes would be more useful for further analysis.

Bosman et al. [16–19] applied and adapted standard fitness landscape analysis techniques to error landscapes. Studies include: the influence of search space boundaries on the landscape analysis [16], the influence of regularisation on error surfaces [17], the influence of architecture settings on modality of the landscape [18], and the effect of different loss functions on the basins of attraction [19].

# 3. Advances in Landscape Analysis

This section discusses contributions to landscape analysis in the form of recently proposed techniques as well as studies in sampling and robustness of landscape analysis. For a background to the concepts and terminology of fitness landscape analysis, the reader is referred to earlier surveys [1,20].

---

## Page 4

### 3.1. Techniques for Landscape Analysis

An earlier survey of fitness landscapes in evolutionary computation [1] identified 22 techniques for analysing landscapes, from genetic algorithm (GA)-deception proposed by David Goldberg in 1987 [21] to accumulated escape probability by Xin Yao and coauthors in 2011 [22]. The aim of the original survey was to make the techniques more accessible to researchers by describing each technique in an understandable way and highlighting attributes affecting their implementation in practice.

Table 1 continues where the previous survey left off, introducing a further 11 techniques starting with technique 23 as local optima networks (LONs) [23]. Although LONs were mentioned in the previous survey as a model for describing the structure of landscapes, they were not listed as a practical technique for analysis. Since then the LON model has been extended and has evolved into one of the most widely used landscape analysis techniques today. The techniques in Table 1 appear in chronological order by the year of the first publication and are described under the following headings:

- **Technique #**: the name of the technique, citation and extensions (where the technique was adapted in subsequent studies).
- **Year**: the year the technique was first introduced in published form.
- **Focus**: refers to what is measured or predicted by the technique.
- **Assumptions**: any significant assumptions on which the technique is based.
- **Description**: summary of how the technique works.
- **Result**: describes the form of output produced by the technique (numerical, graphical, etc.).

When the original list of landscape analysis techniques was compiled, an attempt to classify the techniques was unsuccessful. This was because the possible dimensions on which to base a classification did not help to distinguish between techniques. For example, consider a distinction between local/global or exact/approximate landscape analysis techniques. Many techniques did not fit into either of these hard classes. Even if they did fit into one class, small adaptations would move them into a different class. Instead of a classification of techniques, the approach used was to highlight distinguishing features to assist practitioners in deciding which approaches could be applicable in different scenarios.

The choice of an appropriate technique (or set of techniques) to use should be guided by the nature of the problems to be analysed as well as the purpose of the analysis. The **Assumptions** field in Table 1 specifies whether the technique could be applied to the given problems, while the **Focus** and **Result** fields specify whether the aim is likely to be met by the technique. For example, say your aim is to understand why a particular algorithm is failing on a vehicle routing problem (a combinatorial problem). Technique 23 (LONs) could be applicable, since it is designed for discrete search spaces and has a focus on the global structure of landscapes, which is known to affect search behaviour. LONs could be generated for a range of problems to contrast the global structure of problems on which the algorithm was successful and those on which it failed, to hopefully shed light on possible explanations for why the algorithm is failing. In a similar way, Techniques 25, 29 (and 31 if the algorithm was population-based) could be used to provide a different view of the problem focusing on other aspects namely variations in gradients, local fitness patterns (and evolvability), respectively. Technique 28 would only be appropriate if the problem was modelled as a constrained problem, while Technique 32 would only be appropriate if the problem was modelled as a multiobjective problem. Techniques 24, 27 and 30 would not be applicable because they assume a continuous search space, and Techniques 26 and 33 would also not be appropriate because the problem scenarios are different (coevolution and neural networks, respectively).

---

## Page 5

### Table 1. Techniques for characterising landscapes as a continuation of Table 1 from [1].

**Technique 23: Local optima networks (LONs)** by Ochoa et al. [23] with extensions [24–31].  
**Year:** 2008  
**Focus:** Global landscape structure  
**Assumptions:** Requires a complete enumeration of a discrete search space. Later extensions are based on samples to produce approximate LONs [32,33] and are adapted for continuous spaces [34].  
**Description:**  
A LON is a graph-based abstraction of the search space representing the global structure, where each node of the LON is a local optimum and edges between nodes represent adjacency of the basins of optima (the possibility of search transitioning from one local optimum to another). The LON model is also extended to multiobjective problems to form pareto local optimal solutions networks (PLOS-nets) [30,31]. More detail and resources on LONs can be found on the website: http://lonmaps.com.  
**Result:** A graph visualisation showing the connectivity between local optima. Metrics can also be extracted from LONs such as number of optima, size of basins of attraction, shortest path to the global optimum [35], as well as funnel metrics [36,37], and PageRank centrality [38].

**Technique 24: Exploratory landscape analysis (ELA)** by Mersmann et al. [39] with extensions [40].  
**Year:** 2011  
**Focus:** Low-level features based on small samples  
**Assumptions:** Assumes a continuous search space.  
**Description:**  
Based on a small sample of random solutions (using Latin Hypercube sampling), six classes of low level features are defined: (1) convexity, (2) *y*-distribution, (3) levelset, (4) meta-model, (5) local search, and (6) curvature. Features are estimations of attributes such as the probability of the objective function being linear, the skewness of the distribution of the function values, the accuracy of fitted meta models, the number of local optima identified by local search, estimated numerical gradient and so on. The standard ELA feature set was later extended to include features based on general cell mapping (GCM) [40], but these are currently limited to low-dimensional spaces. ELA is supported by an online package in R, called flacco [41,42] (https://github.com/kerschke/flacco).  
**Result:** 50 numerical values for the standard ELA feature set and a further 44 values for GCM features.

**Technique 25: Length scale distribution** by Morgan and Gallagher [43] with extensions [44].  
**Year:** 2012  
**Focus:** Variation in gradient estimations across the search space  
**Assumptions:** Assumes a distance metric in solution space.  
**Description:**  
Based on a sample of solutions from a random Levy walk through the search space, the length scale (the absolute difference in fitness over the distance in space) is calculated for each pair of solutions in the sample. The length scale distribution is defined as the probability density function of length scales and is estimated using kernel density estimation on the sample of length scales.  
**Result:** Plot of length scale distribution and a single value for the estimated entropy of the length scale distribution.

**Technique 26: Codynamic landscape measures** by Richter [10].  
**Year:** 2014  
**Focus:** Similarity between the objective and subjective landscapes in coevolution  
**Assumptions:** Assumes a model of coevolution for fast evaluation of subjective and objective fitness values.  
**Description:**  
Given a sample of points in the search space and two coupled and codynamic landscapes: the objective landscape (the fitness landscape of the problem) and the subjective landscape (how the coevolution perceives the problem) landscape measures are defined to quantify differences between the landscapes.  
**Result:** Three numeric values at each generation, quantifying different aspects of similarity.

**Technique 27: Degree of separability** by Caraffini et al. [45].  
**Year:** 2014  
**Focus:** Nonseparability  
**Assumptions:** Assumes a continuous search space and the use of the covariance matrix adaptation evolution strategy (CMA-ES) search algorithm.  
**Description:**  
A portion of the budget of the CMA-ES algorithm is executed on the problem. After a limited number of generations, the matrix C evolves to estimate the covariance matrix describing the correlation between pairs of variables. The degree of separability is defined as the average of the absolute values of the Pearson correlation matrix of C (ignoring symmetrical and diagonal elements) after discretisation of the coefficients into classes in 0, 0.2, 0.4, 0.6, 0.8, 1.  
**Result:** An index in the range [0,1] where 0 indicates full separability and 1 indicates full nonseparability.

**Technique 28: Constrained landscape metrics** by Malan et al. [5].  
**Year:** 2015  
**Focus:** Constraint violation in relation to fitness  
**Assumptions:** Assumes that the extent to which constraints are violated can be quantified for all solutions.  
**Description:**  
Given a sequence of solutions based on a progressive random walk [46], with associated fitness and level of constraint violation for each solution, the following are estimated: (1) the proportion of feasible solutions in the search space (FsR), (2) the level of disjointedness between feasible areas, quantified as the ratio of feasible boundary crossings (RFB×), (3) the correlation between the fitness and violation (FVC), and (4) the proportion of solutions that are both high in fitness and low in constraint violation, in the form of two metrics: proportion of solutions in the top 50% percentile and 20% percentile for both fitness and violation.  
**Result:** A vector of five numerical values.

**Technique 29: Bag of local landscape features** by Shirakawa and Nagao [47].  
**Year:** 2016  
**Focus:** Relative fitness patterns in local neighbourhood  
**Assumptions:** Assumes a distance metric in solution space.  
**Description:**  
Given a sample of solutions of size \(\lambda\), the local neighbourhood of a solution is defined as the \(M\) nearest solutions in the sample, based on a distance metric in solution space. The LLP (local landscape pattern) of a solution is a pattern number corresponding to the binary sequence characterising the relative fitness of \(M\) nearest neighbours to the current solution. The LLP of \(x_i\) is 0 (string of \(M\) 0’s) if all \(M\) neighbours are fitter than \(x_i\), and \(2^M - 1\) (string of \(M\) 1’s) if \(x_i\) is fitter than all \(M\) neighbours. The Evo (evolvability) of \(x_i\) is defined as the number of better neighbours (out of \(M\)). Histograms are constructed to characterise the distribution of LLP and Evo values of all solutions in the sample.  
**Result:** Two vectors: BoLLP (of length \(2^M\)) and BoEvo (of length \(M + 1\)), representing the normalised histograms of LLP and Evo, respectively. Principle component analysis is used to reduce the dimensions of the vectors for analysis.

**Technique 30: Maximum entropic epistasis (MEE)** by Sun et al. [48].  
**Year:** 2017  
**Focus:** Variable interactions (direct and indirect)  
**Assumptions:** Assumes a continuous search space.  
**Description:**  
For each pair of decision variables \(x_i, x_j\), the interaction matrix for direct interactions (\(IM_d\)) is identified by calculating the maximal information coefficient (largest mutual information at different scales) between \(x_j\) and the estimated partial derivative of the objective with respect to \(x_i\). The \(IM_d\) is then used to construct an interaction graph to map the strongly connected components to identify the indirect interactions.  
**Result:** Three measures: (1) the degree of direct variable interaction (DDVI), (2) the degree of indirect variable interaction (DIVI), and (3) the degree of variable interactions (DVI).

---

## Page 6

### Table 1. Cont.

**Technique 31: Population evolvability metrics** by Wang et al. [49].  
**Year:** 2018  
**Focus:** Evolvability of a population  
**Assumptions:** Assumes a population-based algorithm for sampling.  
**Description:**  
Given a population of solutions and the set of neighbours (from one iteration of the algorithm), two metrics are defined: (1) *epp* is the probability that a population will evolve and is estimated by calculating the proportion of neighbours that are fitter than the best solution of the current population, and (2) *eap* is the evolutionary ability of the population, which is a quantity that increases with the absolute fitness improvement of the neighbours and decreases with the fitness diversity of the population.  
**Result:** A single value *evp* which is defined as *epp × eap*, with a range of [0, +∞].

**Technique 32: Local multiobjective landscape features** by Liefooghe et al. [50] including earlier contributions [51,52].  
**Year:** 2019  
**Focus:** Evolvability for multiobjective optimisation  
**Assumptions:** Assumes a discrete search space.  
**Description:**  
Given a sequence of solutions obtained through random walks and adaptive walks, features of the walk are derived from the sequence as a whole as well as the neighbourhood of solutions in terms of dominance and hypervolume improvement by neighbours.  
**Result:** 26 numerical values representing local features (17 from random walk sampling and 9 from adaptive walk sampling).

**Technique 33: Loss-gradient clouds** by Bosman et al. [19].  
**Year:** 2020  
**Focus:** Basins of attraction in neural network error landscapes  
**Assumptions:** Requires the numeric gradient of the loss function.  
**Description:**  
A sample of loss values and gradient values is obtained based on a number of random, progressive gradient walks [53]. Stationary points in the sample are determined to be local minima, local maxima or saddle points based on local curvature derived from the eigenvalues of the Hessian matrix. Stagnant sequences on the walk are detected by tracking the deviation in a smoothing of the error. Two quantities are measured: (1) the average number of times that stagnation was observed, and (2) the average length of the stagnant sequence.  
**Result:** A two-dimensional scatterplot of loss values against gradient values (loss-gradient cloud) and two metrics to estimate the number and extent of distinct-valued basins of attraction.

The first two techniques described in Table 1, LONs and ELA, are well established and have been widely used in studies involving landscape analysis, with LONs mostly applied in discrete optimisation and ELA in numerical optimisation. The wide adoption of these two approaches has been facilitated by the availability of code and online resources.

The previous survey [1] included techniques for detecting variable interdependence in binary search spaces (epistasis) but pointed out the absence of equivalent measures for continuous search spaces. This need has been addressed in the introduction of two techniques for quantifying nonseparability in continuous spaces (techniques 27 and 30).

A number of the new proposed techniques for landscape analysis apply to very specific optimisation contexts, such as coevolution (technique 26), constrained optimisation (technique 28), multiobjective optimisation (technique 32) and neural network training (technique 33). This corresponds to the extension of the notion of fitness landscapes to other types of landscapes discussed in Section 2.

### 3.2. Sampling and Robustness of Measures

Most landscape analysis techniques are based on a form of sampling of the search space. When considering the effect of the sampling on the analysis, it is not only the size of the sample that affects the outcome but also the sampling strategy [54,55].

Saleem et al. [56] proposed a method for evaluating landscape metrics in terms of the ability of the metric to identify trends in ordered sets of problems with specific landscape properties. They found that although some metrics can estimate features reliably using a small sample size, there are others that are very sensitive to the size of the sample. Muñoz et al. [57] proposed an experimental methodology for evaluating the reliability of landscape analysis methods that considers aspects such as vulnerability, volatility, stability and sensitivity to sample size. They showed that some landscape measures are highly volatile and that there is evidence of the *curse of modality*, requiring the sample size to increase with the number of local optima, rather than the dimension.

From the literature surveyed it is clear that random sampling techniques that are biased or structured in some form are more effective than more pure forms of random sampling for landscape analysis. For example, in the discrete domain (in the context of quadratic assignment problems), sampling strategies such as neutral walks were found to provide more insight into predicting problem hardness than random walks [58] and LON samples based on iterated local search had more predictive power for heuristic optimisation performance than samples based on random snowball sampling [37].

---

## Page 7

Alternative approaches to traditional random sampling for landscape analysis in the continuous domain include Latin hypercube design sampling [59], progressive random walk sampling [46] and gradient-based walks for sampling error surfaces of neural networks [53].

Online sampling, where the samples are based on solutions encountered by an algorithm during search, has become a popular alternative to random sampling for landscape analysis [60–62]. Enhancements to online sampling for continuous spaces include introducing a mechanism for correcting the error produced by the sampling bias [63] and the introduction of path relinking [64].

In an experimental study, Muñoz et al. [65] explored the effect that function translations had on landscape measures and found that translations could cause abrupt and severe changes in the values of some metrics. Škvorc et al. [66] also found that a large number of ELA features [39] (**technique 26 in Table 1**) were not invariant to shifting and scaling. Finally, Scott and De Jong [67] found that some landscape measures are very sensitive to the presence of noise in the fitness evaluation and that the error is difficult to correct for in an efficient way.

In some real-world optimisation scenarios, the objective function is very expensive to evaluate (such as in simulation-based optimisation) and surrogate models are used to approximate the fitness function. Werth et al. [68] performed a preliminary investigation into landscape analysis on surrogate functions and found that the landscape features were more indicative of the surrogate model than the original landscape.

# 4. Applications of Landscape Analysis

Landscape analysis has gained acceptance as a method for not only understanding complex problems and algorithm behaviour but also to support the prediction of algorithm performance and as part of automated algorithm configuration and selection.

### 4.1. Understanding Complex Problems

Landscape analysis has become popular as an approach to understanding complex optimisation problems by characterising problems using measured landscape features.

When using landscape analysis to characterise problems, one of the aims is to group problems into classes based on these features. This is based on the premise that algorithms may behave similarly on problems that are similar. A vast array of complex classic and real-world problems have been studied using landscape analysis. Some examples in the last ten years are listed under three categories: (1) benchmarks or random instances of classic optimisation problems, (2) real-world applications and (3) machine learning applications.

Many real-world problems can be reduced to variants of classic problems, such as the quadratic assignment problem or the travelling salesman problem. Studying large benchmarks or random instances of these classic problems using landscape analysis is useful as general insights gained should be applicable to scenarios containing these problems as subcomponents. Examples of the application of landscape analysis to the study of classic problems include: the quadratic assignment problem [69–71]; the maximum satisfiability problem [72,73]; permutation flow-shop scheduling [74–76]; packing problems [77,78]; travelling salesman problems [79–82]; the dense graph-colouring problem [83]; number partitioning problem [84]; vehicle routing problems [85]; and the travelling thief problem [86].

Landscape analysis has also been used to understand real-world problems. Examples include: the design of wind turbines [87]; university course timetabling [88]; genetic improvement of software [89–91]; automated test case generation for software testing [92,93]; computational protein design [94]; design of substitution boxes in cryptography [95]; hyperparameter optimisation for metaheuristics [96]; and building energy optimisation [97].

Since 2017 a new trend has emerged of landscape analysis applied in the context of machine learning. Examples include: analysis of weight search spaces in the context of neural network training for classification [98]; analysis of the feature selection problem

---

## Page 8

for classification [99,100]; analysis of policy search spaces in reinforcement learning [101]; analysis of machine learning pipeline configuration search spaces [102]; and analysis of neural architecture search spaces for image classification [103,104].

In each of the studies listed above, landscape analysis provided different insights into problem classes and the nature of the difficulty for search algorithms. To illustrate the kind of benefits that landscape analysis can provide, one study is described in more detail. In the field of genetic engineering, Simoncini et al. [94] analysed a computational protein design problem. The most popular software program used for solving these problems performed well on some instances but poorly on others. Landscape analysis revealed structural differences between the landscapes of an instance that was successfully solved by the software and one on which the software failed. It was observed that the algorithm performed poorly on a landscape that consisted of several suboptimal funnels that were disconnected from the global funnel. In this way, landscape analysis could explain why some problem instances were harder to solve than others. With this kind of understanding, algorithms can be adapted to be more effective on particular classes of problems.

### 4.2. Understanding and Explaining Algorithm Behaviour

The introduction of new metaheuristic algorithms is commonly justified on the basis of competitive experimental results on a limited set of benchmark problems. One of the problems with this approach is that these studies provide no scientific understanding as to why the algorithm performs well on the given problems, and more importantly, no understanding of when the algorithm will perform poorly.

Landscape analysis of optimisation problems provides a mechanism for explaining algorithm behaviour and identifying classes of problems that are suited to particular algorithms. Studies that describe the use of landscape analysis for understanding algorithm behaviour include: explaining evolutionary algorithm behaviour in dynamic environments [8] and the dynamics in coevolutionary games [12]; understanding the behaviour of local search algorithms [105,106]; explaining performance differences between search-and-score algorithms for learning Bayesian network structures [107]; explaining the effect of different mutation operators [108] and different function sets [109] in genetic programming; explaining the performance of different real-valued evolutionary algorithms [87]; explaining the performance of multiobjective evolutionary algorithms [52,110]; understanding evolvability in grammatical evolution [111]; understanding the effect of funnels in the landscape on metaheuristic performance [112]; and explaining the performance of evolutionary algorithms in generating unit tests for software [93].

The list above shows that landscape analysis has mostly been used to understand different evolutionary algorithms, but there are examples where other types of algorithms have been studied, such as local search algorithms and search-and-score algorithms.

### 4.3. Algorithm Performance Prediction

Although most metaheuristics can be easily understood in terms of their algorithmic elements, the behaviour that emerges is often unpredictable. Landscape analysis can be used to extract general features of problems to be used as input to machine learning models for predicting algorithm performance. These models are an important component in the wider aim of automated algorithm selection. Examples of the application of machine learning to predicting algorithm performance based on landscape features include the following:

- Bischl et al. [113] used one-sided support vector regression to predict the best-performing algorithm from a portfolio of four numerical optimisation algorithms based on ELA features. They showed that the model was able to generalise on new problem instances and predict the optimal or close to optimal algorithm from the portfolio.
- Muñoz et al. [114] used a neural network regression model to predict the performance of a CMA-ES algorithm based on landscape features and algorithm parameters. Per-

---

## Page 9

formance was measured in terms of the number of function evaluation required and they found that the model was able to predict the relative ranking values for given algorithm-parameter combinations effectively.
- Malan and Engelbrecht [115] used decision tree models to predict failure of seven variants on the particle swarm optimisation algorithm based on landscape features. The models of five of the algorithm variants achieved testing accuracy levels above 90%.
- Liefooghe et al. [30] used a random forest regression model to predict the performance of multiobjective optimisation algorithms in combinatorial optimisation based on a combination of landscape features and problem-specific features. They later developed a decision tree model for selecting the best performing algorithm out of three multiobjective algorithms [50]. Their model was able to predict the best performing algorithm in more than 98.4% of the cases.
- Jankovic and Doerr [116] proposed a random forest regression model for predicting the performance of CMA-ES algorithms based on ELA features in a fixed-budget setting. They obtained high-quality performance prediction by combining two regression models trained to predict target precision and the logarithm of the target precision.
- Thomson et al. [117] used random forest and linear regression models to predict algorithm performance for solving quadratic assignment problems based on landscape features derived from LON sampling. They found that random forest trees performed better at prediction than linear regression.

### 4.4. Automated Algorithm Selection

Performance complementarity is a phenomenon where different algorithms perform the best on different types of problem instances [118]. Automated algorithm selection is the process of deciding on the best algorithm for the problem at hand and depends on having features for distinguishing problems from each other. The features can be problem specific but can also be derived through landscape analysis, which can be more generally applied across problem types.

Algorithm configuration (choosing of algorithm parameters and strategies for particular problems) is closely related to algorithm selection but differs in that the set of possible configurations is much larger than a finite choice of algorithm candidates. The features used for algorithm configuration and selection can, however, be the same, so studies related to algorithm configuration are also mentioned here. Examples of algorithms that have been configured or dynamically adapted based on landscape characteristics include:

- **genetic algorithms:** using the fitness distance correlation landscape measure to dynamically adjust the migration period in a distributed genetic algorithm [119], selecting a crossover operator based on fitness landscape properties [120], using fitness landscape features to estimate the optimal population size [121];
- **differential evolution algorithms:** adapting the strategy and adjusting the control parameters based on detected landscape modality [122,123], adapting the mutation strategy based on landscape features [124,125], algorithm configuration based on exploratory landscape features with an empirical performance model [126];
- **memetic algorithms:** analysis of the separability of problems to automatically select operators [45] and the use of four fitness landscape analysis techniques to inform the most suitable crossover operator [127];
- selection of CMA-ES algorithm configuration using a trained model for predicting performance based on landscape features that was shown to outperform the default setting of CMA-ES [128];
- surrogate-assisted particle swarm optimisation, where fitness landscape analysis was used to select surrogate models [129]; and
- decomposition-based multiobjective evolutionary algorithms (MOEA/D), where the addition of landscape information improved the behaviour of the adaptive operator selection mechanism [130].

---

## Page 10

There are many attempts at automated algorithm selection using landscape features and the reader is referred to a survey by Kerschke et al. [118] for an overview of studies. Recent contributions not included in the Kerschke et al. survey include algorithm selection for the quadratic assignment problem [131,132], algorithm selection for the travelling salesman problem [133], algorithm selection for the permutation flowshop problem [134] and a form of automated algorithm selection for constraint handling techniques with differential evolution [61].

From the above, it is clear that landscape analysis is playing an important role in both algorithm performance prediction and automated algorithm configuration and selection.

# 5. Opportunities for Further Research

This survey highlights that fitness landscape analysis techniques are being applied in contexts beyond evolutionary computation. The wider scope of landscape analysis introduces interesting challenges and offers many opportunities for further research. Three ideas are discussed here.

Technique 26 in Table 1 proposes an approach to analysing the search space of coevolution by tracking differences between the objective and subjective landscapes. This notion of coupled landscapes, where landscapes are dynamic and a change in one effects the other, may be applicable in contexts wider than coevolution. For example, in generative adversarial networks (GANs), the error landscapes of the generator and discriminator networks are coupled in a similar way to the landscapes of coevolution. It would be interesting to investigate whether landscape analysis could be used in the context of GANs to better understand the dynamics of adversarial training.

Most of the research in landscape analysis is restricted to single objective search spaces. However, many real-world problems have multiple conflicting objectives. Technique 32 in the survey [50] is an important contribution as it provides a first set of numerical features for characterising local features of multiobjective problems. More work is needed in applying this approach to a wider range of problems and algorithms and also adapting the approach for use in continuous search spaces. There is still a gap in techniques for practically characterising global features of multiobjective search spaces. PLOS-nets [30,31] have been proposed for capturing the global structure of multiobjective landscapes, but it is still not clear how this approach can be scaled to large-size problems.

Surrogate modelling has become an important technique for managing optimisation problems that have computationally expensive objective functions. Initial investigations into landscape analysis of surrogate functions [68] were not very successful and further work is needed to identify landscape analysis techniques that are suitable for characterising surrogate functions so that the analysis is indicative of the characteristics of the actual landscape.

# 6. Conclusions

Research in landscape analysis has moved from being a theoretical topic in evolutionary computation to being extensively applied as a practical tool in the wider context of optimisation and has recently also been applied in machine learning. This survey describes advances in landscape analysis in the last decade, including a number of new techniques for landscape analysis and studies relating to sampling and robustness of measures. The survey also highlights the wide range of applications of landscape analysis in understanding complex problems, explaining algorithm behaviour, predicting algorithm performance and automatically configuring and selecting algorithms. Landscape analysis clearly has an important role to play in reducing the unpredictability of algorithms and advancing the field of optimisation and machine learning to a place where our technology can be trusted to solve real-world problems.

**Funding:** This research was funded by the National Research Foundation of South Africa (Grant Number: 120837).

**Conflicts of Interest:** The author declares no conflict of interest.

---

## References

1. Malan, K.M.; Engelbrecht, A.P. A survey of techniques for characterising fitness landscapes and some possible ways forward. *Inf. Sci.* 2013, 241, 148–163.
2. Wright, S. The Roles of Mutation, Inbreeding, Crossbreeding, and Selection in evolution. In *Proceedings of the Sixth International Congress on Genetics*, Ithaca, NY, USA, 24–31 August 1932; pp. 356–366.
3. Stadler, P.F. Fitness Landscapes. In *Biological Evolution and Statistical Physics*; Michael Lässig, A.V., Ed.; Lecture Notes in Physics; Springer: Berlin/Heidelberg, Germany, 2002; Volume 585, pp. 183–204.
4. Verel, S.; Liefooghe, A.; Dhaenens, C. Set-based multiobjective fitness landscapes: A preliminary study. In *Proceedings of the 13th annual Conference on Genetic and Evolutionary Computation*, Dublin, Ireland, 12–16 July 2011; pp. 769–776.
5. Malan, K.M.; Oberholzer, J.F.; Engelbrecht, A.P. Characterising constrained continuous optimisation problems. In *Proceedings of the 2015 IEEE Congress on Evolutionary Computation (CEC)*, Sendai, Japan, 25–28 May 2015; pp. 1351–1358.
6. Hordijk, W.; Kauffman, S.A. Correlation analysis of coupled fitness landscapes. *Complexity* 2005, 10, 41–49.
7. Richter, H. Evolutionary Optimization in Spatio-temporal Fitness Landscapes. In *Parallel Problem Solving from Nature—PPSN IX*; Springer: Berlin/Heidelberg, Germany, 2006; pp. 1–10.
8. Richter, H. Coupled map lattices as spatio-temporal fitness functions: Landscape measures and evolutionary optimization. *Phys. D Nonlinear Phenom.* 2008, 237, 167–186.
9. Yazdani, D.; Nguyen, T.T.; Branke, J. Robust Optimization Over Time by Learning Problem Space Characteristics. *IEEE Trans. Evol. Comput.* 2019, 23, 143–155.
10. Richter, H. Codynamic fitness landscapes of coevolutionary minimal substrates. In *Proceedings of the 2014 IEEE Congress on Evolutionary Computation (CEC)*, Beijing, China, 6–11 July 2014; pp. 2692–2699.
11. De Jong, E.D. Objective Fitness Correlation. In *Proceedings of the 9th Annual Conference on Genetic and Evolutionary Computation (GECCO ’07)*, London, UK, 7–11 July 2007; Association for Computing Machinery: New York, NY, USA, 2007; pp. 440–447.
12. Richter, H. Dynamic landscape models of coevolutionary games. *Biosystems* 2017, 153–154, 26–44.
13. Choromanska, A.; Henaff, M.; Mathieu, M.; Arous, G.B.; LeCun, Y. The Loss Surfaces of Multilayer Networks. In *Proceedings of the 18th International Conference on Artificial Intelligence and Statistics*, São Paulo, Brazil, 21–25 June 2015; pp. 192–204.
14. Im, D.J.; Tao, M.; Branson, K. An empirical analysis of the optimization of deep network loss surfaces. *arXiv* 2016, arXiv:1612.04010.
15. Li, H.; Xu, Z.; Taylor, G.; Studer, C.; Goldstein, T. Visualizing the Loss Landscape of Neural Nets. In *Advances in Neural Information Processing Systems 31*; Bengio, S., Wallach, H., Larochelle, H., Grauman, K., Cesa-Bianchi, N., Garnett, R., Eds.; Curran Associates, Inc.: Duchess County, NY, USA, 2018; pp. 6389–6399.
16. Bosman, A.S.; Engelbrecht, A.; Helbig, M. Search space boundaries in neural network error landscape analysis. In *Proceedings of the 2016 IEEE Symposium Series on Computational Intelligence (SSCI)*, Athens, Greece, 6–9 December 2016; pp. 1–8.
17. Bosman, A.; Engelbrecht, A.; Helbig, M. Fitness Landscape Analysis of Weight-Elimination Neural Networks. *Neural Process. Lett.* 2018, 48, 353–373.
18. Bosman, A.S.; Engelbrecht, A.; Helbig, M. Loss Surface Modality of Feed-Forward Neural Network Architectures. *arXiv* 2019, arXiv:1905.10268.
19. Bosman, A.S.; Engelbrecht, A.; Helbig, M. Visualising Basins of Attraction for the Cross-Entropy and the Squared Error Neural Network Loss Functions. *Neurocomputing* 2020, 400, 113–136.
20. Pitzer, E.; Affenzeller, M. A Comprehensive Survey on Fitness Landscape Analysis. In *Recent Advances in Intelligent Engineering Systems*; Springer: Berlin/Heidelberg, Germany, 2012; pp. 161–191.
21. Goldberg, D.E. Simple Genetic Algorithms and the Minimal Deceptive Problem. In *Genetic Algorithms and Simulated Annealing*; Davis, L., Ed.; Pitman: London, UK, 1987; Chapter 6, pp. 74–88.
22. Lu, G.; Li, J.; Yao, X. Fitness-Probability Cloud and a Measure of Problem Hardness for Evolutionary Algorithms. In *Evolutionary Computation in Combinatorial Optimization*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2011; Volume 6622/2011, pp. 108–117.
23. Ochoa, G.; Tomassini, M.; Vérel, S.; Darabos, C. A Study of NK Landscapes’ Basins and Local Optima Networks. In *Proceedings of the Genetic and Evolutionary Computation Conference*, Atlanta, GA, USA, 12–16 July 2008; pp. 555–562.
24. Vérel, S.; Ochoa, G.; Tomassini, M. The Connectivity of NK Landscapes’ Basins: A Network Analysis. In *Proceedings of the Eleventh International Conference on the Simulation and Synthesis of Living Systems*, Winchester, France, 5–8 August 2008; pp. 648–655.
25. Tomassini, M.; Vérel, S.; Ochoa, G. Complex-network analysis of combinatorial spaces: The NK landscape case. *Phys. Rev. E* 2008, 78, 066114.
26. Ochoa, G.; Vérel, S.; Tomassini, M. First-Improvement vs. Best-Improvement Local Optima Networks of NK Landscapes. In *Parallel Problem Solving from Nature—PPSN XI*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2010; Volume 6238, pp. 104–113.
27. Vérel, S.; Daolio, F.; Ochoa, G.; Tomassini, M. Local Optima Networks with Escape Edges. In *Artificial Evolution*; Springer: Berlin/Heidelberg, Germany, 2011; pp. 49–60.
28. Vérel, S.; Ochoa, G.; Tomassini, M. Local Optima Networks of NK Landscapes With Neutrality. *IEEE Trans. Evol. Comput.* 2011, 15, 783–797.
29. Herrmann, S.; Ochoa, G.; Rothlauf, F. Coarse-Grained Barrier Trees of Fitness Landscapes. In *Parallel Problem Solving from Nature—PPSN XIV*; Springer International Publishing: New York, NY, USA, 2016; pp. 901–910.
30. Liefooghe, A.; Derbel, B.; Vérel, S.; López-Ibáñez, M.; Aguirre, H.; Tanaka, K. On Pareto local optimal solutions networks. In *Proceedings of the International Conference on Parallel Problem Solving from Nature*, Coimbra, Portugal, 8–12 September 2018; Springer: Berlin/Heidelberg, Germany, 2018; pp. 232–244.
31. Fieldsend, J.E.; Alyahya, K. Visualising the Landscape of Multi-objective Problems Using Local Optima Networks. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion (GECCO ’19)*, Prague, Czech Republic, 13–17 July 2019; ACM: New York, NY, USA, 2019; pp. 1421–1429.
32. Iclanzan, D.; Daolio, F.; Tomassini, M. Data-driven Local Optima Network Characterization of QAPLIB Instances. In *Proceedings of the 2014 Annual Conference on Genetic and Evolutionary Computation (GECCO ’14)*, Vancouver, BC, Canada, 12–16 July 2014; pp. 453–460.
33. Verel, S.; Daolio, F.; Ochoa, G.; Tomassini, M. Sampling Local Optima Networks of Large Combinatorial Search Spaces: The QAP Case. In *Parallel Problem Solving from Nature—PPSN XV*; Springer: Cham, Switzerland, 2018; pp. 257–268.
34. Adair, J.; Ochoa, G.; Malan, K.M. Local Optima Networks for Continuous Fitness Landscapes. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion (GECCO ’19)*, Prague, Czech Republic, 13–17 July 2019; pp. 1407–1414.
35. Ochoa, G.; Vérel, S.; Daolio, F.; Tomassini, M. Local Optima Networks: A New Model of Combinatorial Fitness Landscapes. In *Recent Advances in the Theory and Application of Fitness Landscapes*; Richter, H., Engelbrecht, A., Eds.; Springer: Berlin/Heidelberg, Germany, 2014; pp. 233–262.
36. Ochoa, G.; Veerapen, N. Mapping the global structure of TSP fitness landscapes. *J. Heuristics* 2018, 24, 265–294.
37. Thomson, S.L.; Ochoa, G.; Verel, S. Clarifying the Difference in Local Optima Network Sampling Algorithms. In *Evolutionary Computation in Combinatorial Optimization*; Springer International Publishing: New York, NY, USA, 2019; pp. 163–178.
38. Herrmann, S.; Rothlauf, F. Predicting Heuristic Search Performance with PageRank Centrality in Local Optima Networks. In *Proceedings of the Genetic and Evolutionary Computation Conference, GECCO 2015*, Madrid, Spain, 11–15 July 2015; pp. 401–408.
39. Mersmann, O.; Bischl, B.; Trautmann, H.; Preuss, M.; Weihs, C.; Rudolph, G. Exploratory Landscape Analysis. In *Proceedings of the 13th Annual Conference on Genetic and Evolutionary Computation (GECCO ’11)*, Dublin, Ireland, 12–16 July 2011; pp. 829–836.
40. Kerschke, P.; Preuss, M.; Hernández, C.; Schütze, O.; Sun, J.Q.; Grimme, C.; Rudolph, G.; Bischl, B.; Trautmann, H. Cell Mapping Techniques for Exploratory Landscape Analysis. In *Advances in Intelligent Systems and Computing*; Springer International Publishing: Berlin/Heidelberg, Germany, 2014; pp. 115–131.
41. Kerschke, P.; Trautmann, H. The R-Package FLACCO for exploratory landscape analysis with applications to multi-objective optimization problems. In *Proceedings of the 2016 IEEE Congress on Evolutionary Computation (CEC)*, Vancouver, Canada, 24–29 July 2016; pp. 5262–5269.
42. Kerschke, P.; Trautmann, H. Comprehensive Feature-Based Landscape Analysis of Continuous and Constrained Optimization Problems Using the R-Package Flacco. In *Studies in Classification, Data Analysis, and Knowledge Organization*; Springer International Publishing: Berlin/Heidelberg, Germany, 2019; pp. 93–123.
43. Morgan, R.; Gallagher, M. Length scale for characterising continuous optimization problems. In *Proceedings of the 12th International Conference on Parallel Problem Solving from Nature—Part I*, Taormina, Italy, 1–5 September 2012; pp. 407–416.
44. Morgan, R.; Gallagher, M. Analysing and characterising optimization problems using length scale. *Soft Comput.* 2015, 21, 1735–1752.
45. Caraffini, F.; Neri, F.; Picinali, L. An analysis on separability for Memetic Computing automatic design. *Inf. Sci.* 2014, 265, 1–22.
46. Malan, K.M.; Engelbrecht, A.P. A progressive random walk algorithm for sampling continuous fitness landscapes. In *Proceedings of the IEEE Congress on Evolutionary Computation*, Beijing, China, 6–11 July 2014; pp. 2507–2514.
47. Shirakawa, S.; Nagao, T. Bag of local landscape features for fitness landscape analysis. *Soft Comput.* 2016, 20, 3787–3802.
48. Sun, Y.; Kirley, M.; Halgamuge, S.K. Quantifying Variable Interactions in Continuous Optimization Problems. *IEEE Trans. Evol. Comput.* 2017, 21, 249–264.
49. Wang, M.; Li, B.; Zhang, G.; Yao, X. Population Evolvability: Dynamic Fitness Landscape Analysis for Population-Based Metaheuristic Algorithms. *IEEE Trans. Evol. Comput.* 2018, 22, 550–563.
50. Liefooghe, A.; Daolio, F.; Verel, S.; Derbel, B.; Aguirre, H.; Tanaka, K. Landscape-Aware Performance Prediction for Evolutionary Multi-objective Optimization. *IEEE Trans. Evol. Comput.* 2019, 1.
51. Verel, S.; Liefooghe, A.; Jourdan, L.; Dhaenens, C. On the structure of multiobjective combinatorial search space: MNK-landscapes with correlated objectives. *Eur. J. Oper. Res.* 2013, 227, 331–342.
52. Liefooghe, A.; Verel, S.; Aguirre, H.; Tanaka, K. What Makes an Instance Difficult for Black-Box 0–1 Evolutionary Multiobjective Optimizers? In *Artificial Evolution*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2014; Volume 8752, pp. 3–15.
53. Bosman, A.S.; Engelbrecht, A.P.; Helbig, M. Progressive Gradient Walk for Neural Network Fitness Landscape Analysis. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion (GECCO ’18)*, Kyoto, Japan, 15–19 July 2018; pp. 1473–1480.
54. Morgan, R.; Gallagher, M. Sampling Techniques and Distance Metrics in High Dimensional Continuous Landscape Analysis: Limitations and Improvements. *IEEE Trans. Evol. Comput.* 2014, 18, 456–461.
55. Renau, Q.; Doerr, C.; Dreo, J.; Doerr, B. Exploratory Landscape Analysis is Strongly Sensitive to the Sampling Strategy. In *Parallel Problem Solving from Nature—PPSN XVI*; Springer International Publishing: New York, NY, USA, 2020; pp. 139–153.
56. Saleem, S.; Gallagher, M.; Wood, I. Direct Feature Evaluation in Black-Box Optimization Using Problem Transformations. *Evol. Comput.* 2019, 27, 75–98.
57. Muñoz, M.A.; Kirley, M.; Smith-Miles, K. Analyzing Randomness Effects on the Reliability of Landscape Analysis. 2020. Available online: https://www.researchgate.net/publication/325483674_Analyzing_randomness_effects_on_the_reliability_of_Landscape_Analysis (accessed on 15 November 2020).
58. Pitzer, E.; Beham, A.; Affenzeller, M. Generic Hardness Estimation Using Fitness and Parameter Landscapes Applied to Robust Taboo Search and the Quadratic Assignment Problem. In *Proceedings of the 14th Annual Conference Companion on Genetic and Evolutionary Computation*, Philadelphia, PA, USA, 12–16 July 2012; pp. 393–400.
59. Muñoz, M.A.; Kirley, M.; Halgamuge, S.K. Exploratory Landscape Analysis of Continuous Space Optimization Problems Using Information Content. *IEEE Trans. Evol. Comput.* 2015, 19, 74–87.
60. Moser, I.; Gheorghita, M. Combining search space diagnostics and optimisation. In *Proceedings of the 2012 IEEE Congress on Evolutionary Computation*, Brisbane, Australia, 10–15 June 2012.
61. Malan, K.M. Landscape-Aware Constraint Handling Applied to Differential Evolution. In *Theory and Practice of Natural Computing*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2018; Volume 11324, pp. 176–187.
62. Janković, A.; Doerr, C. Adaptive landscape analysis. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Prague, Czech Republic, 13–17 July 2019.
63. Muñoz, M.A.; Kirley, M.; Halgamuge, S.K. Landscape characterization of numerical optimization problems using biased scattered data. In *Proceedings of the IEEE Congress on Evolutionary Computation*, Brisbane, Australia, 10–15 June 2012; pp. 1–8.
64. Beham, A.; Pitzer, E.; Wagner, S.; Affenzeller, M. Integrating Exploratory Landscape Analysis into Metaheuristic Algorithms. In *Computer Aided Systems Theory—EUROCAST 2017*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2018; Volume 10671, pp. 473–480.
65. Muñoz, M.A.; Smith-Miles, K. Effects of function translation and dimensionality reduction on landscape analysis. In *Proceedings of the 2015 IEEE Congress on Evolutionary Computation (CEC)*, Sendai, Japan, 12–14 June 2015; pp. 1336–1342.
66. Škvorc, U.; Eftimov, T.; Korošec, P. Understanding the problem space in single-objective numerical optimization using exploratory landscape analysis. *Appl. Soft Comput. J.* 2020, 90, 106138.
67. Scott, E.O.; Jong, K.A.D. Landscape Features for Computationally Expensive Evaluation Functions: Revisiting the Problem of Noise. In *Parallel Problem Solving from Nature—PPSN XIV*; Springer: Cham, Switzerland, 2016; pp. 952–961.
68. Werth, B.; Pitzer, E.; Affenzeller, M. Surrogate-Assisted Fitness Landscape Analysis for Computationally Expensive Optimization. In *Computer Aided Systems Theory – EUROCAST 2019*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2020; pp. 247–254.
69. Daolio, F.; Vérel, S.; Ochoa, G.; Tomassini, M. Local Optima Networks of the Quadratic Assignment Problem. In *Proceedings of the IEEE Congress on Evolutionary Computation*, Barcelona, Spain, 18–23 July 2010; pp. 1–8.
70. Chicano, F.; Daolio, F.; Ochoa, G.; Vérel, S.; Tomassini, M.; Alba, E. Local Optima Networks, Landscape Autocorrelation and Heuristic Search Performance. In *Parallel Problem Solving from Nature—PPSN XII*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2012; Volume 7492, pp. 337–347.
71. Tayarani-N., M.H.; Prügel-Bennett, A. Quadratic assignment problem: A landscape analysis. *Evol. Intell.* 2015, 8, 165–184.
72. Prügel-Bennett, A.; Tayarani-Najaran, M. Maximum Satisfiability: Anatomy of the Fitness Landscape for a Hard Combinatorial Optimization Problem. *IEEE Trans. Evol. Comput.* 2012, 16, 319–338.
73. Ochoa, G.; Chicano, F. Local Optima Network Analysis for MAX-SAT. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Prague, Czech Republic, 13–17 July 2019; pp. 1430–1437.
74. Daolio, F.; Vérel, S.; Ochoa, G.; Tomassini, M. Local Optima Networks of the Permutation Flow-Shop Problem. In *Artificial Evolution—EA 2013*; Revised Selected Papers; Springer: Berlin/Heidelberg, Germany, 2013; Volume 8752, pp. 41–52.
75. Hernando, L.; Daolio, F.; Veerapen, N.; Ochoa, G. Local Optima Networks of the Permutation Flowshop Scheduling Problem: Makespan vs. total flow time. In *Proceedings of the IEEE Congress on Evolutionary Computation—CEC 2017*, San Sebastian, Spain, 5–8 June 2017; pp. 1964–1971.
76. Baioletti, M.; Santucci, V. Fitness Landscape Analysis of the Permutation Flowshop Scheduling Problem with Total Flow Time Criterion. In *Computational Science and Its Applications—ICCSA 2017*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2017; pp. 705–716.
77. Morgan, R.; Gallagher, M. Fitness Landscape Analysis of Circles in a Square Packing Problems; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2014; pp. 455–466.
78. Alyahya, K.; Rowe, J.E. Landscape Analysis of a Class of NP-Hard Binary Packing Problems. *Evol. Comput.* 2019, 27, 47–73.
79. Ochoa, G.; Veerapen, N.; Whitley, D.; Burke, E.K. The Multi-Funnel Structure of TSP Fitness Landscapes: A Visual Exploration. In *Artificial Evolution—EA 2015*; Lecture Notes in Computer Science; Revised Selected Papers; Springer: Berlin/Heidelberg, Germany, 2015; Volume 9554, pp. 1–13.
80. Veerapen, N.; Ochoa, G.; Tinós, R.; Whitley, D. Tunnelling Crossover Networks for the Asymmetric TSP. In *Parallel Problem Solving from Nature—PPSN XIV*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2016; Volume 9921, pp. 994–1003.
81. Ochoa, G.; Veerapen, N. Deconstructing the Big Valley Search Space Hypothesis. In *Evolutionary Computation in Combinatorial Optimization*; Springer: Cham, Switzerland, 2016; pp. 58–73.
82. Tayarani-N., M.H.; Prügel-Bennett, A. An Analysis of the Fitness Landscape of Travelling Salesman Problem. *Evol. Comput.* 2016, 24, 347–384.
83. Tayarani-N., M.H.; Prügel-Bennett, A. Anatomy of the fitness landscape for dense graph-colouring problem. *Swarm Evol. Comput.* 2015, 22, 47–65.
84. Ochoa, G.; Veerapen, N.; Daolio, F.; Tomassini, M. Understanding Phase Transitions with Local Optima Networks: Number Partitioning as a Case Study. In *Evolutionary Computation in Combinatorial Optimization—EvoCOP*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2017; Volume 10197, pp. 233–248.
85. Ventresca, M.; Ombuki-Berman, B.; Runka, A. Predicting Genetic Algorithm Performance on the Vehicle Routing Problem Using Information Theoretic Landscape Measures. In *Evolutionary Computation in Combinatorial Optimization*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2013; pp. 214–225.
86. Yafrani, M.E.; Martins, M.S.R.; Krari, M.E.; Wagner, M.; Delgado, M.R.B.S.; Ahiod, B.; Lüders, R. A fitness landscape analysis of the travelling thief problem. In *Proceedings of the Genetic and Evolutionary Computation Conference*, Kyoto, Japan, 15–19 July 2018; pp. 277–284.
87. Caamaño, P.; Bellas, F.; Becerra, J.A.; Díaz, V.; Duro, R.J. Experimental analysis of the relevance of fitness landscape topographical characterization. In *Proceedings of the IEEE Congress on Evolutionary Computation*, Brisbane, Australia, 10–15 June 2012; pp. 1–8.
88. Rodriguez-Maya, N.; Flores, J.J.; Graff, M. Predicting the RCGA Performance for the University Course Timetabling Problem. In *Intelligent Computing Systems*; Springer: Cham, Switzerland, 2016; pp. 31–45.
89. Haraldsson, S.O.; Woodward, J.R.; Brownlee, A.E.I.; Smith, A.V.; Gudnason, V. Genetic Improvement of Runtime and Its Fitness Landscape in a Bioinformatics Application. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion (GECCO ’17)*, Berlin, Germany, 15–19 July 2017; Association for Computing Machinery: New York, NY, USA, 2017; pp. 1521–1528.
90. Langdon, W.B.; Veerapen, N.; Ochoa, G. Visualising the Search Landscape of the Triangle Program. In *European Conference on Genetic Programming—EuroGP 2017*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2017; Volume 10196, pp. 96–113.
91. Veerapen, N.; Daolio, F.; Ochoa, G. Modelling genetic improvement landscapes with local optima networks. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Berlin, Germany, 15–19 July 2017.
92. Aleti, A.; Moser, I.; Grunske, L. Analysing the Fitness Landscape of Search-based Software Testing Problems. *Autom. Softw. Eng.* 2017, 24, 603–621.
93. Albunian, N.; Fraser, G.; Sudholt, D. Causes and effects of fitness landscapes in unit test generation. In *Proceedings of the 2020 Genetic and Evolutionary Computation Conference*, Cancún, Mexico, 8–12 July 2020; pp. 1204–1212.
94. Simoncini, D.; Barbe, S.; Schiex, T.; Verel, S. Fitness landscape analysis around the optimum in computational protein design. In *Proceedings of the Genetic and Evolutionary Computation Conference*, Kyoto, Japan, 15–19 July 2018.
95. Jakobovic, D.; Picek, S.; Martins, M.S.R.; Wagner, M. A Characterisation of S-Box Fitness Landscapes in Cryptography. In *Proceedings of the Genetic and Evolutionary Computation Conference (GECCO ’19)*, Prague, Czech Republic, 13–17 July 2019; Association for Computing Machinery: New York, NY, USA, 2019; pp. 285–293.
96. Harrison, K.R.; Ombuki-Berman, B.M.; Engelbrecht, A.P. The Parameter Configuration Landscape: A Case Study on Particle Swarm Optimization. In *Proceedings of the 2019 IEEE Congress on Evolutionary Computation (CEC)*, Wellington, New Zealand, 10–13 June 2019; pp. 808–814.
97. Waibel, C.; Mavromatidis, G.; Evins, R.; Carmeliet, J. A comparison of building energy optimization problems and mathematical test functions using static fitness landscape analysis. *J. Build. Perform. Simul.* 2019, 12, 789–811.
98. van Aardt, W.A.; Bosman, A.S.; Malan, K.M. Characterising neutrality in neural network error landscapes. In *Proceedings of the 2017 IEEE Congress on Evolutionary Computation (CEC)*, San Sebastian, Spain, 5–8 June 2017; pp. 1374–1381.
99. Mostert, W.; Malan, K.; Engelbrecht, A. Filter versus wrapper feature selection based on problem landscape features. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Kyoto, Japan, 15–19 July 2018; pp. 1489–1496.
100. Mostert, W.; Malan, K.M.; Ochoa, G.; Engelbrecht, A.P. Insights into the Feature Selection Problem Using Local Optima Networks. In *Evolutionary Computation in Combinatorial Optimization*; Springer: Cham, Switzerland, 2019; pp. 147–162.
101. Stapelberg, B.; Malan, K.M. Global structure of policy search spaces for reinforcement learning. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Prague, Czech Republic, 13–17 July 2019.
102. Pimenta, C.G.; de Sá, A.G.C.; Ochoa, G.; Pappa, G.L. Fitness Landscape Analysis of Automated Machine Learning Search Spaces. In *Evolutionary Computation in Combinatorial Optimization*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2020; Volume 12102, pp. 114–130.
103. Rodrigues, N.M.; Silva, S.; Vanneschi, L. A Study of Generalization and Fitness Landscapes for Neuroevolution. *IEEE Access* 2020, 8, 108216–108234.
104. Rodrigues, N.M.; Silva, S.; Vanneschi, L. A Study of Fitness Landscapes for Neuroevolution. In *Proceedings of the IEEE Congress on Evolutionary Computation*, Glasgow, UK, 19–24 July 2020.
105. Watson, J.P. An Introduction to Fitness Landscape Analysis and Cost Models for Local Search. In *Handbook of Metaheuristics*; Gendreau, M., Potvin, J.Y., Eds.; Springer: Boston, MA, USA, 2010; pp. 599–623.
106. Tari, S.; Basseur, M.; Goëffon, A. Sampled Walk and Binary Fitness Landscapes Exploration. In *Lecture Notes in Computer Science*; Springer: Cham, Switzerland, 2018; pp. 47–57.
107. Wu, Y.; McCall, J.; Corne, D. Fitness landscape analysis of Bayesian network structure learning. In *Proceedings of the 2011 IEEE Congress of Evolutionary Computation (CEC)*, New Orleans, LA, USA, 5–8 June 2011; pp. 981–988.
108. Nguyen, Q.U.; Nguyen, X.H.; O’Neill, M. Examining the Landscape of Semantic Similarity Based Mutation. In *Proceedings of the 13th Annual Conference on Genetic and Evolutionary Computation (GECCO ’11)*, Dublin, Ireland, 12–16 July 2011; pp. 1363–1370.
109. Nguyen, Q.U.; Truong, C.D.; Nguyen, X.H.; O’Neill, M. Guiding Function Set Selection in Genetic Programming Based on Fitness Landscape Analysis. In *Proceedings of the 15th Annual Conference Companion on Genetic and Evolutionary Computation, GECCO ’13 Companion*, Amsterdam, The Netherlands, 6–10 July 2013; pp. 149–150.
110. Daolio, F.; Liefooghe, A.; Verel, S.; Aguirre, H.; Tanaka, K. Global vs Local Search on Multi-Objective NK-Landscapes: Contrasting the Impact of Problem Features. In *Proceedings of the 2015 Annual Conference on Genetic and Evolutionary Computation, GECCO ’15*, Madrid, Spain, 11–15 July 2015; pp. 369–376.
111. Medvet, E.; Daolio, F.; Tagliapietra, D. Evolvability in Grammatical Evolution. In *Proceedings of the Genetic and Evolutionary Computation Conference (GECCO ’17)*, Berlin, Germany, 15–19 July 2017; Association for Computing Machinery: New York, NY, USA, 2017; pp. 977–984.
112. Thomson, S.L.; Ochoa, G.; Daolio, F.; Veerapen, N. The effect of landscape funnels in QAPLIB instances. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Berlin, Germany, 15–19 July 2017.
113. Bischl, B.; Mersmann, O.; Trautmann, H.; Preuß, M. Algorithm selection based on exploratory landscape analysis and cost-sensitive learning. In *Proceedings of the Genetic and Evolutionary Computation Conference*, Philadelphia, PA, USA, 13–27 July 2012; pp. 313–320.
114. Muñoz, M.A.; Kirley, M.; Halgamuge, S.K. A meta-learning prediction model of algorithm performance for continuous optimization problems. In *Parallel Problem Solving from Nature—PPSN XII*; Lecture Notes in Computer Science; Springer: Berlin/Heidelberg, Germany, 2012; pp. 226–235.
115. Malan, K.M.; Engelbrecht, A.P. Particle swarm optimisation failure prediction based on fitness landscape characteristics. In *Proceedings of the 2014 IEEE Symposium on Swarm Intelligence*, Orlando, FL, USA, 9–12 December 2014; pp. 1–9.
116. Jankovic, A.; Doerr, C. Landscape-Aware Fixed-Budget Performance Regression and Algorithm Selection for Modular CMA-ES Variants. In *Proceedings of the 2020 Genetic and Evolutionary Computation Conference*, Cancún, Mexico, 8–12 July 2020; Association for Computing Machinery: New York, NY, USA, 2020; pp. 841–849.
117. Thomson, S.L.; Ochoa, G.; Verel, S.; Veerapen, N. Inferring Future Landscapes: Sampling the Local Optima Level. *Evol. Comput.* 2020, 28, 1–22.
118. Kerschke, P.; Hoos, H.H.; Neumann, F.; Trautmann, H. Automated Algorithm Selection: Survey and Perspectives. *Evol. Comput.* 2019, 27, 3–45.
119. Salto, C.; Alba, E.; Luna, F. Using Landscape Measures for the Online Tuning of Heterogeneous Distributed Gas. In *Proceedings of the 13th Annual Conference Companion on Genetic and Evolutionary Computation*, Dublin, Ireland, 12–16 July 2011; pp. 691–694.
120. Picek, S.; Jakobovic, D. From Fitness Landscape to Crossover Operator Choice. In *Proceedings of the 2014 Annual Conference on Genetic and Evolutionary Computation (GECCO ’14)*, Vancouver, BC, Canada, 12–16 July 2014; pp. 815–822.
121. Gibbs, M.S.; Maier, H.R.; Dandy, G.C. Using characteristics of the optimisation problem to determine the Genetic Algorithm population size when the number of evaluations is limited. *Environ. Model. Softw.* 2015, 69, 226–239.
122. Takahama, T.; Sakai, S. Differential evolution with dynamic strategy and parameter selection by detecting landscape modality. In *Proceedings of the 2012 IEEE Congress on Evolutionary Computation*, Brisbane, Australia, 10–15 June 2012.
123. Takahama, T.; Sakai, S. Large scale optimization by differential evolution with landscape modality detection and a diversity archive. In *Proceedings of the 2012 IEEE Congress on Evolutionary Computation*, Brisbane, Australia, 10–15 June 2012.
124. Sallam, K.M.; Elsayed, S.M.; Sarker, R.A.; Essam, D.L. Differential Evolution with Landscape-Based Operator Selection for Solving Numerical Optimization Problems. In *Proceedings in Adaptation, Learning and Optimization*; Springer: Cham, Switzerland, 2016; pp. 371–387.
125. Sallam, K.M.; Elsayed, S.M.; Sarker, R.A.; Essam, D.L. Landscape-assisted multi-operator differential evolution for solving constrained optimization problems. *Expert Syst. Appl.* 2020, 162, 113033.
126. Belkhir, N.; Dréo, J.; Savéant, P.; Schoenauer, M. Feature Based Algorithm Configuration: A Case Study with Differential Evolution. In *Parallel Problem Solving from Nature—PPSN XIV*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2016; Volume 9921, pp. 156–166.
127. Consoli, P.A.; Mei, Y.; Minku, L.L.; Yao, X. Dynamic selection of evolutionary operators based on online learning and fitness landscape analysis. *Soft Comput.* 2016, 20, 3889–3914.
128. Belkhir, N.; Dréo, J.; Savéant, P.; Schoenauer, M. Per Instance Algorithm Configuration of CMA-ES with Limited Budget. In *Proceedings of the Genetic and Evolutionary Computation Conference (GECCO ’17)*, Berlin, Germany, 15–19 July 2017; pp. 681–688.
129. Yu, H.; Tan, Y.; Sun, C.; Zeng, J.; Jin, Y. An adaptive model selection strategy for surrogate-assisted particle swarm optimization algorithm. In *Proceedings of the 2016 IEEE Symposium Series on Computational Intelligence (SSCI)*, Athens, Greece, 6–9 December 2016.
130. Kuk, J.; Goncalves, R.; Pozo, A. Combining Fitness Landscape Analysis and Adaptive Operator Selection in Multi and Many-Objective Optimization. In *Proceedings of the 2019 8th Brazilian Conference on Intelligent Systems (BRACIS)*, Salvador, Brazil, 15–18 October 2019.
131. Beham, A.; Affenzeller, M.; Wagner, S. Instance-based Algorithm Selection on Quadratic Assignment Problem Landscapes. In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*, Berlin, Germany, 15–19 July 2017; pp. 1471–1478.
132. Beham, A.; Wagner, S.; Affenzeller, M. Algorithm Selection on Generalized Quadratic Assignment Problem Landscapes. In *Proceedings of the Genetic and Evolutionary Computation Conference (GECCO ’18)*, Kyoto, Japan, 15–19 July 2018; pp. 253–260.
133. Bożejko, W.; Gnatowski, A.; Niżyński, T.; Affenzeller, M.; Beham, A. Local Optima Networks in Solving Algorithm Selection Problem for TSP. In *Contemporary Complex Systems and Their Dependability*; Advances in Intelligent Systems and Computing; Springer: Cham, Switzerland, 2018; Volume 761, pp. 83–93.
134. Pavelski, L.M.; Delgado, M.R.; Kessaci, M.É. Meta-learning on flowshop using fitness landscape analysis. In *Proceedings of the Genetic and Evolutionary Computation Conference*, Prague, Czech Republic, 13–17 July 2019.
