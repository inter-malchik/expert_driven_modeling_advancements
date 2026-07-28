# Artificial Intelligence Review (2023) 56:13187–13257
https://doi.org/10.1007/s10462-023-10470-y

## An exhaustive review of the metaheuristic algorithms for search and optimization: taxonomy, applications, and open challenges

**Kanchan Rajwar¹ · Kusum Deep¹ · Swagatam Das²**

Published online: 9 April 2023  
© The Author(s), under exclusive licence to Springer Nature B.V. 2023

---

## Abstract

As the world moves towards industrialization, optimization problems become more challenging to solve in a reasonable time. More than 500 new metaheuristic algorithms (MAs) have been developed to date, with over 350 of them appearing in the last decade. The literature has grown significantly in recent years and should be thoroughly reviewed. In this study, approximately 540 MAs are tracked, and statistical information is also provided. Due to the proliferation of MAs in recent years, the issue of substantial similarities between algorithms with different names has become widespread. This raises an essential question: can an optimization technique be called ‘novel’ if its search properties are modified or almost equal to existing methods? Many recent MAs are said to be based on ‘novel ideas’, so they are discussed. Furthermore, this study categorizes MAs based on the number of control parameters, which is a new taxonomy in the field. MAs have been extensively employed in various fields as powerful optimization tools, and some of their real-world applications are demonstrated. A few limitations and open challenges have been identified, which may lead to a new direction for MAs in the future. Although researchers have reported many excellent results in several research papers, review articles, and monographs during the last decade, many unexplored places are still waiting to be discovered. This study will assist newcomers in understanding some of the major domains of metaheuristics and their real-world applications. We anticipate this resource will also be useful to our research community.

**Keywords** Optimization · Metaheuristic algorithm · Nature inspired algorithm · Parameter

**Swagatam Das**  
swagatam.das@isical.ac.in

**Kanchan Rajwar**  
krajwar@ma.iitr.ac.in

**Kusum Deep**  
kusum.deep@ma.iitr.ac.in

¹ Department of Mathematics, Indian Institute of Technology Roorkee, Roorkee, Uttarakhand 247667, India  
² Electronics and Communication Sciences Unit, Indian Statistical Institute, Kolkata, West Bengal 700108, India

---

# 1 Introduction

The term ‘meta’ is becoming more prevalent nowadays; it generally translates to ‘beyond’ or ‘higher level’. Although there is no agreed mathematical definition, the continued development of heuristic algorithms is usually referred to as MAs (Yang 2020). A heuristic algorithm is a method for producing acceptable solutions to optimization problems through trial and error. Intelligence is found not only in humans but also in animals, microorganisms, and other minute aspects of nature, such as ants, bees, and other creatures. Nature serves as a source of inspiration for many MAs, which are referred to as nature-inspired algorithms (NIAs) (Yang 2010a). Nature performs all tasks optimally, whether it’s moving light through space in the shortest path, carrying out the work function of any living organ with the least amount of energy expansion, or forming bubbles with the least amount of surface area that is a sphere. Natural selection favors optimization. That is the most efficient method of completing any task successfully and hassle-free. This simple concept can be applied to any type of work that we perform in our everyday lives. However, when it comes to large-scale operations, such as those in businesses, national security, distribution in large areas, and the design of some structures, we require a concrete method or tool to ensure that resources are utilized properly and that are maximized, which leads to operations research (OR). During the last decade, metaheuristics have emerged as a powerful optimization tool in OR. Also, MAs are becoming more critical in computational intelligence because they are flexible, adaptive, and have an extensive search capacity. MAs are used in NP-Hard problems, fixture and manufacturing cell design, soft computing, foreign exchange trading, robotics, medical science, behavioral science, photo-voltaic models, and so on, which is evidence of the importance of MAs. As MAs are stochastic by nature, they cannot guarantee the achievement of the optimal solution. As a result, the question naturally arises: Is it a worthy choice? It is roughly akin to ‘something is better than nothing.’ When others fail, MAs provide us with a satisfactory ‘something’. In practice, we achieve a satisfactory or workable solution in a reasonable amount of time. Most of the algorithms have been tested for lower dimensions. It is necessary to test them for a higher dimensional problem and improve them if necessary to tackle the ‘curse of dimensionality’. A significant research gap between theory and implementation has been shown, which should be taken care of. As exploration and exploitation are the fundamental strategies of most MAs, balancing them is another challenge. The main contributions of this study can be summarized as:

- The article presents a recent metaheuristics survey. The data set for this study contains about 540 MAs.
- This study provides critical yet constructive analysis, addressing improper methodological practices to accomplish helpful research.
- A new classification of MAs is proposed based on the number of parameters.
- The limitations of metaheuristics, as well as open challenges, are highlighted.
- Several potential future research directions for metaheuristics have been identified.

The rest of this paper is organized as follows. A brief history is discussed in Sect. 2. A compilation of existing MAs and other literary works are provided in Sect. 3. In Sect. 4, few statistical data are provided, while constructive criticism has been done in Sect. 5. MAs are classified into subgroups based on four different points of view in Sect. 6. In addition, Sect. 7 contains some real-world metaheuristics applications. A few limitations, including some open challenges, are addressed in Sect. 8. A brief overview of the potential future directions of metaheuristics is provided in Sect. 9. Finally, conclusions are drawn in Sect. 10.

---

# 2 Brief history

What was the first use of (meta) heuristic? Because the heuristic process automatically dominates the human mind, humans may have employed it from the beginning, whether they realized it or not: the use of fire, the acquisition of number systems, and the usage of the wheel are all examples of heuristic process applications. Any practical problem can be modeled mathematically for optimization—this is a challenging task; even the more challenging task is to optimize it. To address this situation, scientists proposed several approaches that are now referred to as ‘conventional methods’. They are mainly as follows:

- **Direct search:** random search method, uni-variant method, pattern search method, convex optimization, linear programming, interior-point method, quadratic programming, trust-region method, etc.
- **Gradient-based method:** steepest descent method, conjugate gradient method, Newton–Raphson method, quasi-Newton method, etc.

Since the most realistic optimization problems are discontinuous and highly non-linear, conventional methods fail to prove their efficiency, robustness, and accuracy. Researchers devised alternative approaches to tackle such problems. It is worth noting that nature has inspired us since the beginning–whether making fire from a jungle blaze or making ships from floating wood. In general, all are gifted by nature, directly or indirectly.

However, Hungarian mathematician George Pólya wrote the book *How to Solve It* about the subject in 1945, where he gave an idea about heuristic searches and mentioned four steps to grasping a problem as follows: (a) understand the problem, (b) devising a plan, (c) looking back, and (d) carrying the plan (Polya 2004). The book gained immense attraction and was translated into several languages, selling over a million copies. Still, the book is used in mathematical education, Pólya work inspired Douglas Lenat’s Automated Mathematician and Eurisko artificial intelligence programs.

Also, scientists all over the world tried to solve many practical problems. In this case, in 1945, the first success came by breaking the Enigma ciphers’ code at Bletchley Park by using heuristic algorithms; British scientist Turing called his method ‘heuristic search’ (Hodges 2012). He was one of the designers of the bombe, used in World War II. After then, he proposed a ‘learning machine’ in 1950, which would parallel the principle of evolution. Barricelli started work with computer simulation as early as 1954 at the Institute for Advanced Study, New Jersey. Although his work was not noticed widely, his work in evolution is considered pioneering in artificial life research. Artificial evolution became a well-recognized optimization approach in the 1960s and early 1970s due to the work of Rechenberg and Schwefel (sulfur 1977). Rechenberg solved many complex engineering problems through evolution strategies. Next, Fogel proposed generating artificial intelligence. Decision Science Inc. was probably the first company to use evolutionary computation to solve real-world problems in 1966. Owens and Burgin further expanded the methodology, and the Adaptive Maneuvering Logic flight simulator was initially deployed at Langley Research Center for air-to-air combat training (Burgin and Fogel 1972). Fogel and Burgin also experimented with simulations of co-evolutionary games in Decision Science. They also worked on the real-world applications of evolutionary computation in many ways, including modeling human operators and thinking about biological communication (Fogel et al. 1970). In the early 1970s, Holland formalized a breakthrough programming technique, the genetic algorithm (GA), which he summarised in his book *Adaptation in Natural and Artificial Systems* (Holland 1991). He worked to extend the algorithm’s scope during the next decade by creating a genetic code representing any computer program structure. Also, he developed a framework for predicting the next generation’s quality, known as Holland’s schema theorem. Kirkpatrick et al. (1983) proposed simulated annealing (SA), which is a single point-based algorithm inspired by the mechanism of metallurgy’s annealing process. Glover (1989) formalized the tabu search computer-based optimization methodology. This is based on local search, which has a high probability of getting stuck in local optima. Another interesting artificial life program, called boid, was developed by Reynolds (1987), which simulates birds’ flocking behavior. It was used for visualizing information and optimization tasks. Moscato et al. (1989) introduced a memetic algorithm in his technical report inspired by Darwinian principles of natural evolution and Dawkins’ notion of a meme. The memetic algorithm was an extension of the traditional genetic algorithm. It was used as a local search technique to reduce the likelihood of premature convergence. Another nature-inspired algorithm from the early years was developed in 1989 by Bishop and Torr (1992), later referred to as stochastic diffusion search (SDS). Kennedy and Eberhart (1995) developed particle swarm optimization (PSO), which was first intended for simulating social behaviour. This is one of the simplest and most widely used algorithm. In the next two years, an appreciable and controversial work, the no free lunch theorem (NFL) for optimization, was introduced and proved explicitly by Wolpert and Macready (1997). While some researchers argue that NFL has some significant insight, others argue that NFL has little relevance to machine learning research. But the main thing is that NFL unlocks a golden opportunity to further research for developing new domain-specific algorithms. The validity of the NFL for higher dimensions is still under investigation. Later on, several efficient algorithms have been developed, such as differential evolution (DE) by Storn and Price (1997), ant colony optimization (ACO) by Dorigo et al. (2006), artificial bee colony (ABC) by Karaboga and Basturk (2007), and others, as shown in the following section.

---

# 3 Metaheuristics

It is difficult to summarize all existing MAs and other valuable data in a single article. In this section, we collect as many existing MAs as possible. Here about 540 existing MAs are complied. It enables us to comprehend the broader context in order to offer constructive criticism in this area, and this can be used as a toolbox (Table 1).

Not only algorithms but also related research works have increased rapidly in the last decade (Fig. 4). Apart from algorithm development, the literature in this field mainly includes the following categories of studies:

## 3.1 Enhanced of algorithms

There are many techniques that can be employed to enhance the algorithm’s average performance. Such few techniques have been described by Wang and Tan (2017). Numerous improved methods have been developed to get better results in comparison with the original ones. Random grey wolf optimizer is such an efficient modified algorithm due to Gupta and Deep (2019). An enhanced salp swarm algorithm has propose by Hegazy et al. (2020). The chaotic dragonfly method is modified to an improved one, by Sayed et al. (2019b). Many more modified algorithms are available in literature, such as improved genetic algorithm (Dandy et al. 1996) and improved particle swarm optimization (Jiang et al. 2007). To achieve high computational efficiency, researchers introduce a powerful notion parallelism. Mainly three parallelism techniques have been recorded in literature as they are (a) parallel moves model, (b) parallel multi-start model, and (c) move acceleration model (Alba et al. 2005).

## 3.2 Hybridization of algorithms

The idea of hybridizing metaheuristics is not new but dates back to their origins. Several classifications of hybrid metaheuristics can be found in the literature. Hybrid metaheuristics can be classified based on many objectives as the level of hybridization, the order of execution, the control strategy, etc. (Raidl 2006).

### 3.2.1 Level of hybridization

Hybrid MAs are distinguished into two types based on the level (or strength) at which the various algorithms are combined: high-level and low-level combinations. High-level combinations retain the individual identities of the original algorithms while cooperating over a relatively well-defined interface. In contrast, low-level combinations heavily rely on each other, exchanging individual components or functions of the algorithms. Because both the original algorithms are strongly independent in high-level combinations, it is sometimes referred to as ‘weak coupling’. In contrast, in low-level combinations, it is referred to as ‘strong coupling’ because they are both dependent on each other.

### 3.2.2 Order of execution

Hybrid MAs can be divided based on the execution process as a batch, interleaved, and parallel. The batch model employs a one-way data flow in which each algorithm is executed sequentially. On the contrary, we have interleaved and parallel models in which the algorithms might interact in more sophisticated ways (Alba 2005).

### 3.2.3 Control strategy

Based on their control strategy, we may further subclass hybrid MAs into integrative (coercive) and collaborative (cooperative) combinations. In integrative approaches, one algorithm is considered a subordinate or embedded part of another. This method is quite common. For example, the memetic algorithm is embedded in an evolutionary algorithm for locally improving candidate solutions obtained from variation operators. Algorithms in collaborative combinations share information but are not embedded. For example, Klau et al. (2004) combined a memetic algorithm with integer programming to solve the prize-collecting steiner tree problem heuristically.

## 3.3 Comparison of MAs

In industries, determining which algorithm works best for a particular type of problem is a practical concern. Generally, the difficulty of an optimization task is measured based on its objective function. A fitness landscape consists essentially of the objective values of all variables within the decision variable space. To characterize the fitness landscape of a particular optimization problem, fitness landscape analysis (FLA) is a valuable and potent analytic tool (Wang et al. 2017). Thus, many research papers evolve by comparison of MAs. FLA is essential for studying how complex problems are for MAs to solve. The number of local optima is the first and most apparent fitness landscape characteristic to consider when determining the complexity of a particular optimization problem. Horn and Goldberg (1995) have found that multimodal optimization problems with half the points in the search space are more accessible to solve than unimodal problems. That is, only considering the number of local optima is neither sufficient nor necessary for an optimization algorithm. Another significant characteristic of the fitness landscape is the basin of attraction on local optima. Basins of attraction are classified into two types (Pitzer et al. 2010): strong basins of attraction, in which all individuals from the basin of attraction can approach a single optimum exclusively, and weak basins of attraction, in which some individuals from the basin of attraction can approach to another optimum. When determining the complexity of a specific optimization problem, basins of attraction might potentially offer additional helpful information about the size, shape, stability, and distribution of local optima. Recent developments in FLA can be found in (Zou et al. 2022).

## 3.4 Multi/many objective optimization

Most real life problems naturally involve multiple objectives. Multiple conflicting objectives are common and make optimization problems challenging to solve. Problems with more than one conflicting objective, there is no single optimum solution. There exist a number of solutions which are all optimal. Without more information, none of the optimum solutions may be deemed superior to the others. This is the fundamental difference between a single-objective (except in multimodal optimization scenarios where multiple optimal solutions exist) and multi-objective optimization task. In multi-objective optimization, a number of optimal solutions arise because of trade-offs between conflicting objectives.

To address multi-objective optimization, several extended versions of MAs are proposed. Few most popular examples are non-dominated sorting genetic algorithm II (NSGA-II) (Deb et al. 2002), multi-objective evolutionary algorithm based on decomposition (MOEA/D) (Zhang and Li 2007), and non-dominated sorting genetic algorithm III (NSGA-III) (Deb and Jain 2013). When the number of functions are greater than three, the majority of solutions in the NSGA-II search spaces become non-dominated, resulting in a rapid loss of search capability. MOEA/D decomposes a multi-objective optimization problem into a number of scalar optimization subproblems and optimizes them simultaneously. Also, each subproblem is optimized by only using information from its several neighbouring subproblems, which makes MOEA/D have lower computational complexity at each generation. NSGA-III uses the basic framework of NSGA-II. It uses a well-spread reference point mechanism to maintain diversity. NSGA-III was developed to solve optimization problems with more than four objectives.

## 3.5 Review articles

These studies offer young researchers a valuable perspective on the current state of existing works and their potential future prospects, which can be highly beneficial for their research. Some important articles are highlighted as follows. A novel taxonomy of 100 algorithms based on movement of population along with a few significant conclusions are given by Molina et al. (2020). Some significant future directions of metaheuristics are addressed by Del Ser et al. (2019). Tzanetos and Dounias (2021) have strongly criticised the unethical practises and have given few ideas for the future. A comprehensive overview and classification along with bibliometric analysis is given by Ezugwu et al. (2021). A recent survey of the multi-objective optimization algorithms, their variants, applications, open challenges and future directions can be found in (Sharma and Kumar 2022).

## 3.6 Benchmark test functions

Numerous test or benchmark functions have been reported in the literature; however, no standard list or set of benchmark functions for evaluating the performance of an algorithm exists. To combat this, CEC benchmark functions are published regularly (Liang et al. 2014). 175 benchmark functions are collected by Jamil and Yang (2013). Mirjalili and Lewis (2019) have provided a set of benchmark optimization functions considering different levels of difficulty. 67 non-symmetric benchmark functions have collected by Gao et al. (2021b).

---

# 4 Statistical analysis

Approximate 540 new MAs have been developed, with about 385 of them appearing in the last decay. Furthermore, in the year 2022 alone, around 47 ‘novel’ MAs are proposed. A graphical representation is shown in Fig. 1. It can be seen in Fig. 1 that, the trend line, with coefficient of determination (R²) = 0.926, is highly upward. R² is a measure that provides information about the goodness of fit of a model. A trend line is most reliable when its R² value is at or near 1. It is clear from the high valuation of R² that, the development of ‘novel’ MAs is growing rapidly.

Figure 2 is a summary of the top 10 MAs that have been cited the most, based on Google Scholar (GS). The most widely used algorithm is particle swarm optimization (PSO), which has more than 75000 citations on its own. Genetic algorithm (GA) is ranked as the second most popular algorithm with more than 70000 citations. Ant colony optimization (ACO), differential evolution (DE), and simulated annealing (SA) are ranked third, fourth, and fifth, respectively, with more than 50,000, 30,000, and 15,000 citations respectively. In order of most-cited algorithms to date, tabu search (TS), grey wolf optimizer (GWO), artificial bee colony (ABC), cuckoo search (CS), and harmony search (HS) are rated fifth, sixth, seventh, eighth, ninth, and tenth, respectively.

Additionally, Fig. 3 shows GS-citations for the most popular MAs during the last decade. The graph demonstrates how quickly these algorithms are gaining popularity. Grey wolf optimizer (GWO) has gained the attention of researchers and become one of the most popular in a short period of time. Other algorithms, such as the particle swarm optimization (PSO), genetic algorithm (GA), simulated annealing (SA), and differential evolution (DE), have attracted interest at a nearly steady pace during the last decade.

Another very interesting question: How much metaheuristic research is being carried out now? We require data to address this question. Extraction of data from radically various types of repositories is a difficult task. However, we address this question and ascertain the present knowledge regarding metaheuristic studies. Our investigation is made based on available data in Scopus. Even though we do not have complete statistics, our data provide a picture of metaheuristics and leads to significant insights. To identify metaheuristic documents, we use two screening processes: The publications whose titles, abstracts, or keywords include the term ‘optimization’ are listed first. In the second step to identifying only the metaheuristic subdomain of optimization, we consider publications that contain at least one of the terms ‘meta-heuristic’, ‘metaheuristic’, ‘bio-inspired optimization’, ‘bio inspired optimization’, ‘nature-inspired algorithm’, ‘nature inspired algorithm’, ‘nature-inspired technique’, ‘nature inspired technique’, and ‘evolutionary algorithm’ in the titles, abstracts, or keywords. The period is taken from 2000 to 2022. Figure 4 depicts the search results. Each year there are more publications on metaheuristics than the year before. The trend line with R² = 0.995 indicates that metaheuristic research is expanding significantly. Table 2 lists the various document types. Statistics show that most of the weight in this metaheuristics domain publication comes from articles and conference papers.

---

## Table 2 Different types of published documents with the word ‘optimization’ in the title/abstract/keywords and at least one of the words ‘meta-heuristic’, ‘metaheuristic’, ‘bio-inspired optimization’, ‘bio inspired optimization’, ‘nature-inspired algorithm’, ‘nature inspired algorithm’, ‘nature-inspired technique’, ‘nature inspired technique’, and ‘evolutionary algorithm’ in the title/abstract/keywords

**Data source—Scopus on December 31, 2022**

| Document type | Total number | Percentage (%) |
|---|---:|---:|
| Article | 54,158 | 54.22 |
| Conference Paper | 40,788 | 40.84 |
| Conference Review | 1292 | 1.29 |
| Review | 1093 | 1.09 |
| Book | 145 | 0.15 |
| Editorial | 88 | 0.09 |
| Retracted | 61 | 0.06 |
| Erratum | 37 | 0.04 |
| Data Paper | 9 | 0.01 |
| Undefined | 18 | 0.02 |
| **Total** | **99,877** | **100** |

---

# 5 Constructive criticism

According to statistical data, numerous MAs appear one after the other; on average, approximately 38 algorithms have appeared yearly during the last decade. In light of this, it seems that metaheuristics is nearing the pinnacle of research effort, but is this the case? Many research community members have expressed alarm about this unanticipated scenario (Aranha et al. 2021; Del Ser et al. 2019). Genetic algorithm (GA), particle swarm optimization (PSO), ant colony optimization (ACO), and differential evolution (DE) were probably developed in a context when scientists lacked alternative optimization methods. Each has its own set of feathers and controlling equations. Many algorithms, particularly those of the most recent generation, are alleged to be non-unique. Furthermore, they are unable to deliver impactful effects. Criticizing this overcrowded situation, Osaba et al. (2021) have pointed out three factors: (a) being unable to provide beneficial containment rather than causing confusion in this area, (b) statistical data authenticity, and (c) unfair comparisons to promote own algorithms. Readers should be aware that several front-line algorithms have been claimed to have lost their novelty. Noted cases are BHO vs PSO (Piotrowski et al. 2014), GWO vs PSO (Villalón et al. 2020), FA vs PSO (Villalón et al. 2020), BA vs PSO (Piotrowski et al. 2014), IWD vs ACO (Camacho-Villalón et al. 2018), and HS vs ES (Weyland 2010). Constructive debate is essential to strengthening this area. Steer et al. (2009) separate the sources of inspiration for NIAs into two groups as well. The first group includes ‘strong’ inspiration algorithms, which mimic mechanisms that address real-world phenomena. Algorithms with ‘weak’ inspiration go into the second group since they do not precisely adhere to the norms of a phenomenon. A significant proportion of these algorithms are remarkably similar to other already available ones. Algorithms with little creativity usually keep their titles to distinguish themselves from other popular metaheuristic approaches that function similarly. Many algorithms, such as bacterial foraging optimization (BFO), birds swarm algorithm (BSA), krill herd (KH), cat swarm optimization (CSO), chicken swarm optimization (CSO), and blue monkey algorithm (BMA), are alleged to be PSO-like algorithms in (Tzanetos and Dounias 2021). Although there are numerous improved versions, new algorithms are frequently compared to older versions of well-known algorithms like GA and PSO. The intriguing aspect here is that each author individually codes these algorithms, and the results are often questionable due to the lack of transparency as the code is kept private. In another study, Molina et al. (2020) determine which algorithms are most influential for developing other algorithms. They compile other algorithms that can be considered variants of the classical algorithms. From this group, the following conclusions can be drawn: about 57 algorithms that are similar to PSO, including african buffalo optimization (ABO) and bee colony optimization (BCO), about 24 algorithms that are similar to GA, including crow search algorithm (CSA) and earthworm optimization algorithm (EOA), and about 24 algorithms that are similar to DE, including artificial cooperative search (ACS) and differential search algorithm (DSA). Research on ‘duplicate’ algorithms is just a repetition of research concepts already investigated in the context of the original algorithm, resulting in a waste of resources and time. However, several algorithms in recent years have demonstrated their efficacy in various real-world challenges, opening up new avenues for research. A new algorithm should be produced when the existing algorithms cannot generate a satisfactory solution to a real-world optimization problem or when a more intelligent mechanism is identified that makes the new algorithm more efficient than others.

---

# 6 Taxonomy

In the literature, there are several classifications for MAs. For example, classification based on the source of inspiration (6.1) is the most common, but it does not provide us with any mathematical inside of algorithms. Another classification based on the number of finding agents (6.2) provides insight into the number of agents deployed in an iteration. However, this is highly non-uniform because relatively few algorithms fall into one group while the remainder falls into another. Molina et al. (2020) categorize MAs based on their behavior (6.3), rather than their source of inspiration, as (a) Differential Vector Movement and (b) Solution Creation, which provides additional information about the inner workings of MAs. An additional essential tool is employed in this study to classify the existing MAs. Parameters are pretty sensitive in any algorithm. Tuning a parameter for a new situation is difficult since we do not have a chart or set of instructions. Because of a lack of detailed mathematical analysis of algorithms and problems, we must execute the algorithms numerous times for different parameter values in this case. Thus, it is crucial to study the parameters of algorithms to improve the result. This study presents a novel classification based on the number of parameters (6.4).

## 6.1 Taxonomy by source of inspiration

This is the oldest classification. Furthermore, it is a beneficial classification because nature-inspired algorithms or metaheuristics concept is primarily based on natural or biological phenomena. Depending on the source of inspiration, MAs have been categorized in various ways by different authors. Fister Jr et al. (2013) have classified it into four categories as swarm intelligence (SI) based algorithms, bio-inspired (not SI) based algorithms, physic-chemistry based algorithms, and the rest as another algorithm, whereas Siddique and Adeli (2015) have divided it into three subgroups as physics-based, chemistry-based and biology-based algorithms. Molina et al. (2020) have classified it into six subgroups as breeding-based evolutionary algorithms, SI-based algorithms, physics-chemistry-based algorithms, human social behavior-based algorithms, and plant-based algorithms, and the rest part are mentioned as miscellaneous. The widely recognized classification is addressed in this text. Hence, in this study, MAs are classified into four subgroups (Fig. 5), which are as follows:

### 6.1.1 Evolutionary algorithms (EAs)

Darwinian ideas of natural selection or survival of the fittest inspired EAs. EAs start with a population of individuals and simulate sexual reproduction and mutation in order to create a generation of offspring. The practice is repeated to maintain genetic material that makes an individual more adapted to a particular environment while eliminating that which makes it weaker.

Charles Darwin’s theory of natural evolution motivates genetic algorithm (GA) and differential evolution (DE), while genetic programming (GP) is based on the paradigm of biological evolution. EAs examples include gene expression programming (GEP), learning classifier systems (LCS), neuroevolution (NE), evolution strategy (ES), and so on.

### 6.1.2 Swarm intelligence (SI) algorithms

Although Beni and Wang (1993) invented the term ‘Swarm Intelligence’ in 1989 in the context of cellular robotic systems, SI has since become a sensational topic in many industries. SI is defined as a decentralized and self-organized system’s collective behavior. The swarm system’s primary qualities are adaptability (learning by doing), high communication, and knowledge-sharing. While organisms cannot perform tasks like defending themselves against a vast predator or attacking for food on their own, they rely heavily on swarming. Even when they are looking for food, they swarm. SI has inspired a vast number of MAs; for example, the intelligent social behavior of birds flock motivates particle swarm optimization (PSO), the monkey climbing process on trees while looking for food motivates monkey search (MS), grey wolf leadership hierarchy and hunting mechanism motivates grey wolf optimizer (GWO), and so on. SI examples include, but are not limited to, ant lion optimizer (ALO), bat algorithm (BA), firefly algorithm (FA), ant colony optimization (ACO), cuckoo search (CS), artificial bee colony (ABC), and glowworm swarm optimization (GSO).

### 6.1.3 Physical law-based algorithms (PhAs)

Algorithms that are inspired by physical and chemical law fall under this subcategory. Furthermore, PhAs can be subclassified as:

**(i) Physics based algorithms:**  
Gravitation, big bang, black hole, galaxy, and field are the primary key source of the idea of this subcategory. The consumption of stars by a black hole and the formation of new beginnings motivate the black hole algorithm (BH). Harmony search (HS) is developed based on the improvisation of musicians. Simulated annealing (SA) is based on metallurgy’s annealing process, where metal is heated quickly, then cooled slowly, increasing strength and making it simpler to work with. Among these are the big bang-big crunch algorithm (BBBC), central forces optimization (CFO), charged systems optimization (CSO), electro-magnetism optimization (EMO), galaxy-based search algorithm (GBS), and gravitational search algorithm (GSA).

**(ii) Chemistry based algorithms:**  
MAs inspired by the principle of chemical reactions, such as molecular reaction, Brownian motion, molecular radiation, etc. come under this category. Gases brownian motion optimization (GBMO), artificial chemical process (ACP), ions motion optimization algorithm (IMOA), and thermal exchange optimization (TEO) are a few examples of this category.

### 6.1.4 Miscellaneous

Algorithms based on miscellaneous ideas like human behaviors, game strategy, mathematical theorems, politics, artificial thoughts, and other topics fall into this category. The creation, movement, and spread of clouds inspire the atmosphere clouds model optimization algorithm (ACMO), whereas trading shares on the stock market motivates the exchange market algorithm (EMA). Several other examples are the grenade explosion method (GEM), heart optimization (HO), passing vehicle search (PVS), simple optimization (SO), small world optimization (SWO), ying-yang pair optimization (YYPO), and great deluge algorithm (GDA).

### Fig. 5 Classification of MAs based on the source of inspiration
(confirmed from screenshot)

- **Evolutionary Algorithms (EAs)**
  - Genetic Algorithm (GA)
  - Differential Evolution (DE)
  - Evolution Strategy (ES)
  - Genetic Programming (GP)
  - Gene Expression Programming (GEP)

- **Swarm Intelligence (SI) algorithms**
  - Particle Swarm Optimization (PSO)
  - Ant Colony Optimization (ACO)
  - Artificial Bee Colony (ABC)
  - Firefly Algorithm (FA)
  - Grey Wolf Optimizer (GWO)
  - Salp Swarm Algorithm (SSA)
  - Cuckoo Search (CS)
  - Ant Lion Optimizer (ALO)
  - Bat Algorithm (BA)
  - Whale Optimization Algorithm (WOA)

- **Physical law based Algorithms (PhAs)**
  - **Physics based Algorithm**
    - Simulated Annealing (SA)
    - Harmony Search (HS)
    - Gravitational Search Algorithm (GSA)
    - Central Forces Optimization (CFO)
    - Multi-Verse Optimizer (MVO)
    - Big-Bang Big-Crunch (BBBC)
  - **Chemistry based Algorithms**
    - Artificial Reaction Algorithm (ARA)
    - Thermal Exchange Optimization (TEO)
    - Artificial Chemical Process (ACP)
    - Gases Brownian Motion Optimization (GBMO)
    - Ions Motion Optimization Algorithm (IMOA)
    - Kinetic Gas Molecules Optimization (KGMO)

- **Miscellaneous**
  - Small World Optimization (SWO)
  - Great Deluge Algorithm (GDA)
  - Atmosphere Clouds Model Optimization (ACMO)
  - Heart Optimization (HO)
  - Passing Vehicle Search (PVS)
  - River Formation Dynamics (RFD)
  - Football Game Inspired Algorithm (FGIA)
  - Imperialist Competitive Algorithm (ICA)
  - Teaching Learning-Based Algorithm (TLBA)
  - Ying-Yang Pair Optimization (YYPO)
  - Football Game Inspired Algorithm (FGIA)
  - Interior Search Algorithm (ISA)

---

## 6.2 Taxonomy by population size

Multiple agents work better together than a single agent, and there are several advantages, such as information sharing, data remembering, etc. Inspired by it; researchers try to discover the best solution with multiple agents. When it comes to investigating a region, several agents have shown to be superior to a single agent. In our literature, existing algorithms are classified into two categories as trajectory-based and population-based algorithms (Fig. 6) (Yang 2020).

### 6.2.1 Trajectory-based algorithms (TAs)

In contrast, most classical algorithms are built on trajectories, which implies that the movement of the solution during each iteration constitutes a single trajectory. At the beginning of the procedure, a random estimate was made, and the result was refined with each subsequent step. For example, simulation annealing (SA) involves a single agent or solution that moves piece-wise through the design or search space in which it is applied. Better moves and solutions are always welcome, whereas less-than-ideal moves are more likely to be accepted. These actions create a path through the search space, and there is a nonzero probability that this path will lead to the global optimal solution. Hill climbing (HC), tabu search (TS), great deluge algorithm (GDA), iterated local search (ILS), and greedy randomized adaptive search procedures (GRASP) are a few examples of this category.

### 6.2.2 Population-based algorithms (PAs)

This category encompasses all significant algorithms. Because population-based algorithm utilizes multiple finding agents, it enables an extraordinary exploration of the search space’s diversification, sometimes called an exploration-based algorithm. Elitism can be used easily here, which is a bonus point. Genetic algorithm (GA), particle swarm optimization (PSO), ant colony optimization (ACO), and firefly algorithm (FA) are a few examples of this category.

### Fig. 6 Classification of MAs based on the size of the population
(confirmed from screenshot)

- **Trajectory based Algorithms (TAs)**
  - Hill Climbing (HC)
  - Tabu Search (TS)
  - Great Deluge Algorithm (GDA)
  - Iterated Local Search (ILS)
  - Greedy Randomized Adaptive Search Procedures (GRASP)

- **Population based Algorithms (PAs)**
  - Genetic Algorithm (GA)
  - Differential Evolution (DE)
  - Artificial Bee Colony (ABC)
  - Particle Swarm Optimization (PSO)
  - Ant Colony Optimization (ACO)
  - Grey Wolf Optimizer (GWO)

---

## 6.3 Taxonomy by movement of population

Molina et al. (2020) have attempted to categorize based on its behavior rather than its source of inspiration. How the population for the next iteration is updated remains the key feature of this classification. This classification is a good tool for understanding the same type of algorithms. According to them, MAs can be classified as algorithms based on differential vector movement and algorithms based on solution creation (Fig. 7).

### 6.3.1 Differential vector movement (DVM)

DVM is a method of creating new solutions by shifting or mutating an existing one. The newly generated solution could compete against earlier ones or other solutions in the population to obtain space and remain there in the following search cycles. That decision further subdivides this category. The movement—and thus the search—can be guided by (i) the entire population; (ii) only the meaningful/relevant solutions, e.g., the best and/or worst candidates in the population; and (iii) a small group, which could represent the neighborhood around each solution or, in subpopulation based algorithms, only the subpopulation to which each solution belongs.

### 6.3.2 Solution creation (SC)

New solutions are created by merging many solutions (such that there is no single parent solution) or another similar mechanism, rather than through mutation/movement of a single reference solution. This is further subdivided into two categories based on how the new solution is created as (i) a combination, or crossover, of several solutions, and (ii) stigmergy, in which there is indirect coordination between the different solutions or agents, usually through the use of an intermediate structure, to generate better ones.

Genetic algorithm (GA), gene expression (GE), harmony search (HS), bee colony optimization (BCO), cuckoo search (CS), and dolphin search (DS) are some examples of the first subcategory. In contrast, ant colony optimization (ACO), termite hill algorithm (THA), river formation dynamics (RFD), intelligence water drops algorithm (IWDA), water-flow optimization algorithm (WFOA), and virtual bees algorithm (VBA) are some examples of the second subcategory.

---

## 6.4 Taxonomy by number of parameters

Parameters are a critical component in the configuration of metaheuristics. The performance of MAs is highly dependent on the settings of the parameters. Choosing the best values of parameters for a MA (parameter tuning) is an intricate problem that may need its own study area for metaheuristics (Talbi 2009). MA’s flexibility and robustness are parameter-dependent. A smaller collection of parameters simplifies parameter tuning. In addition, the parameter values are defined by the optimization problem considered in the calculation. The number of parameters affects the complexity of an algorithm.

No classification in the literature takes this parametric trait into account. We require a classification based on this to identify algorithms that employ the same number of parameters. This classification will allow us to obtain an additional mathematical understanding of MAs. Many parameters influence an algorithm’s performance, including the population’s size and the number of iterations. Even though the population size and the number of iterations have a substantial impact on the output, these two parameters are shared by all algorithmic methods. In other words, these two parameters provide no information about the internal structure of algorithms. This type of parameter is referred to as a ‘secondary’ parameter. We concentrate on so-called ‘primary’ parameters that are not shared by all algorithms and are particularly sensitive to their values. This study proposes a novel classification framework for MAs based on the number of primary parameters employed.

The majority of algorithms are found to have between 0 and 5 primary parameters. Consequently, most algorithms are covered if we classify them into six categories based on the number of 0, 1, 2, 3, 4, and 5 primary parameters. Those not covered by the preceding six categories, i.e., those with more than five primary parameters, fall under the miscellaneous group. Accordingly, to maintain uniformity across subcategories and cover all MAs with a smaller number of classifications, we have classified them into seven subgroups as follows:

### 6.4.1 Free-parameter based algorithms (FPAs)

FPAs refer to algorithms that have no primary parameters in their structure. FPA is regarded as one of the most user-friendly of the various alternatives because no primary parameter is used. FPA is adaptive, flexible, and easy to utilize in different optimization problems. Generally, the governing equations of FPAs are pretty simple. It is potentially more generic to adapt to a broader class of optimization problems. FPA includes algorithms such as teaching-learning-based optimization (TLBO), black hole algorithm (BH), multi-particle collision algorithm (M-PCA), symbiosis organisms search (SOS), vortex search optimization (VS), forensic-based investigation (FBI), and lightning attachment procedure optimization (LAPO).

### 6.4.2 Mono-parameter based algorithms (MPAs)

MPAs refer to the algorithms that have single primary parameters in their structure. Mainly this parameter is used to change the state of exploration to exploitation and vice versa, which is extremely important. ‘Limit’ is the only primary parameter of the artificial bee colony (ABC) algorithm that determines the food source to be abandoned (Akay and Karaboga 2009). The parameter ‘c1’ is utilized to balance exploration and exploitation in the governed Eq. (3.1) of the salp swarm algorithm (SSA) (Mirjalili et al. 2017). The probability of biological interaction (p) is the only primary parameter in artificial cooperative search (ACS) (Civicioglu 2013a). This value specifies the maximum number of passive individuals allowed in each sub-superorganism. The probability (pa) is the only primary parameter in cuckoo search (CS) that essentially controls the elitism and the balance of the randomization and local search (Yang and Deb 2009). In harris hawks optimizer (HHO), the parameter ‘E’ is used to toggle between soft (|E| ≤ 0.5) and hard besiege (|E| > 0.5) processes (Heidari et al. 2019).

Similarly, a few examples include gravitational interactions optimization (GIO), interior search algorithm (ISA), killer whale algorithm (KWA), kinetic gas molecules optimization (KGMO), social spider optimization (SSO), stochastic fractal search (SFS), social group optimization (SGO), and fitness dependent optimizer (FDO).

### 6.4.3 Bi-parameter based algorithms (BPAs)

BPAs refer to algorithms that have two primary parameters in their structure. Differential evolution (DE) comprises two direct control parameters, namely, the amplification factor of the difference vector and the crossover constant, which simultaneously regulate the exploration and exploitation search in different stages (Storn and Price 1997). Simulated annealing (SA) has two primary parameters: the initial temperature and the cool-down factor. Grey wolf optimizer (GWO) has only two primary parameters to be adjusted. They are ‘a’ and ‘C’ (Mirjalili et al. 2014). The parameter a is decreased from 2 to 0. The adaptive values of parameter a allow for a smooth transition between exploration and exploitation. Different places around the best agent can be reached concerning the current position by adjusting the value a and C vectors. The whale optimization algorithm (WOA) has two primary internal parameters that must be modified to transition from exploration to exploitation, namely A and C (Mirjalili and Lewis 2016). The parameter A enables the algorithm to transition seamlessly between exploration and exploitation: by decreasing A, specific iterations are allocated to exploration (|A| ≥ 1), while the remainder is devoted to exploitation (|A| < 1). By altering the values of the parameters A and C, several locations around the optimal agent can be attained relative to the current position. The marine predators algorithm (MPA) has two control parameters: FADs and P. The parameters FADs affect exploration, while the parameter P helps exaggerate the steps taken by predators or prey.

Crow search algorithm (CSA), flower pollination algorithm (FPA), grasshopper optimization algorithm (GOA), multi-verse optimizer (MVO), political optimizer (PO), seeker optimization algorithm (SOA), tunicate swarm algorithm (TSA), moth flame optimization (MFO), artificial chemical reaction optimization algorithm (ACROA), spiral dynamics optimization (SDO), zombie survival optimization (ZSO) and artificial jellyfish search optimizer (AJSO) are few examples of BPAs.

### 6.4.4 Tri-parameter based algorithms (TrPAs)

TrPAs refer to the algorithms that have three primary parameters in their structure. The genetic algorithm (GA) has three primary parameters: the selection criterion for the new population, the mutation rate, and the crossover rate (Holland 1991). The most often used selection methods are roulette wheel selection, rank selection, tournament selection, and Boltzmann selection, each of which has distinct advantages and disadvantages. Depending on the application, a suitable method of selection can be employed. Excavation from local minima is usually influenced by the rate of mutation, but the crossover rate impacts solution accuracy. Harmony search (HS) have three primary parameters: harmony memory considering rate (HMCR), pitch adjusting rate (PAR), and distance bandwidth (BW) (Kumar et al. 2012). The HMCR and PAR parameters are used for global searching and improving local solutions, respectively. Firefly algorithm (FA) is executed by three parameters: attractiveness, randomization, and absorption (Yang 2009). The attractiveness parameter is based on light intensity between two fireflies and defined with exponential functions. When this parameter is set to zero, it happens to the random walk corresponding to the randomization parameter, which is determined by the Gaussian distribution principle as generating the number from the [0, 1] interval. On the other hand, absorption parameters affect the value of attractiveness parameters as changing from zero to infinity. And, for the case of converging to infinity, the movement of fireflies appears as a random walk. Similarly, the squirrel search algorithm (SSA) has three parameters, namely: the number of food sources (Nfs), gliding constant (Gc), and predator presence probability (Pdp) (Jain et al. 2019). The parameter Nfs is an attribute of the algorithm that provides flexibility to vary the exploration capability of the algorithm. The parameter Gc maintains a balance between exploration and exploitation. The natural behavior of flying squirrels is modeled by Pdp. Three parameters should be tuned in across neighborhood search (ANS) to suit different optimization problems: the cardinality of the superior solution set, the across-search degree, and the standard deviation of the Gaussian distribution (Wu 2016). The convergence curve formula, the effective radius, and epsilon are the three primary parameters for dolphin echolocation optimization (DEO) (Kaveh and Farhoudi 2013).

A few examples of TrPAs are the firefly algorithm (FA), krill herd (KH), spring search algorithm (SSA), artificial algae algorithm (AAA), gases brownian motion optimization (GBMO), hurricane based optimization algorithm (HOA), orca optimization algorithm (OOA), social spider algorithm (SSA), water cycle algorithm (WCA), equilibrium optimizer (EO), parasitism predation algorithm (PPA), and heap-based optimizer (HBO).

### 6.4.5 Tetra-parameter based algorithms (TePAs)

TePAs refer to the algorithms that have four primary parameters in their structure. In general, the algorithmic framework has many governed equations that are weighted according to the parameters for exploration and exploitation in subsequent iterations. Four primary parameters need to be selected in ant colony optimization (ACO): the information heuristic factor ( ), the expectation heuristic factor ( ), the pheromone evaporation factor ( ), and the pheromone strength (Q). Sine cosine algorithm (SSA) has four primary parameters: r1, r2, r3, and r4. The parameter r1 specifies the next position’s area (or direction), which may be within or beyond the space between the solution and destination. The parameter r2 specifies the direction of movement with respect to or away from the destination. The parameter r3 brings a random weight for the destination in order to stochastically emphasize (r3 > 1) or de-emphasize (r3 ≤ 1) the effect of the destination in defining the distance. Finally, the parameter r4 equally switches between the sine and cosine components in Eq. (3.3) used in (Mirjalili 2016b). Archimedes optimization algorithm (AOA) has four parameters, namely c1, c2, c3, and c4 together control the exploration and exploitation (Hashim et al. 2021).

Similarly few examples of this category are football game algorithm (FGA), group counseling optimization (GCO), migrating birds optimization (MBO), space gravitational algorithm (SGA), spider monkey optimization (SMO), movable damped wave algorithm (MDWA), gravitational search algorithm (GSA), and football game algorithm (FGA).

### 6.4.6 Penta-parameter based algorithms (PPAs)

PPAs refer to algorithms that have five primary parameters in their structure. Particle swarm optimization (PSO) has five primary parameters: topology, cognitive constant (C1), social constant (C2), inertia weight (W), and velocity limit. The gbest and the lbest topologies were proposed in the original work. Many recent studies have investigated how different topologies, such as cycles, wheels, stars, and random graphs with N particles and N edges, affect the performance (Liu et al. 2016). A total of 1343 random topologies and six special topologies were tested in (Kennedy and Mendes 2002), including gbest, lbest, pyramid, star, small, and von Neumann. The parameters C1 and C2 control how much weight should be given between refining the particle’s search result and recognizing the swarm’s search result. There are also proposals to decrease the parameter C1 while increasing the parameter C2 to encourage exploration at the beginning and exploitation at the end. The parameter W specifies global and local search capabilities, whereas the parameter velocity limit serves as a convergent speed accelerator.

A few examples of this category are the cheetah chase algorithm (CCA), and farmland fertility algorithm (FFA) (Shayanfar and Gharehchopogh 2018).

### 6.4.7 Miscellaneous

This category includes algorithms with more than five primary parameters in their structure. Tuning all primary parameters simultaneously for a black-box optimization problem is complex, which is a disadvantage of this category. The six primary parameters of biogeography-based optimization (BBO) are the probability of modifying a habitat, the probability of immigration limits, the size of each step, the probability of mutation, I, and E (Simon 2008). The cluster number, M1, M2, , , , L1, L2, L3, I1, I2, and I3 are the twelve primary parameters of henry gas solubility optimization (HGSO) (Hashim et al. 2019). Tuning them is a time-consuming task for a variety of optimization problems. We require sensitive analysis when dealing with a large number of parameter sets. The minimum and maximum temperatures, the initial supply and endurance, the visibility, the camel caravan, and the death rate are the seven primary parameters in the camel algorithm (CA) (Ibrahim and Ali 2016).

A few examples of miscellaneous are the cheetah chase algorithm (CCA), exchange market algorithm (EMA), forest optimization algorithm (FOA), african buffalo optimization (ABO), magnetic optimization algorithm (MFO), roach infestation optimization (RIO), worm optimization (WO), intelligent water drop algorithm (IWD), see-see partridge chicks optimization (SSPCO), ground-tour algorithm (GTA), bonobo optimizer (BO), hunting Search (HuS), and swallow swarm optimizer (SWO) (Fig. 8).

The classification based on the source of inspiration shows how researchers are convinced by various ideas found in nature and how they mathematically describe them to use them as an optimization tool. On the other hand, this classification reveals nothing about the mathematics hidden within. The classification based on the number of finding agents gives us a glimpse into each algorithm, allowing us to understand better how it operates. Multi-agent systems provide several advantages, including the ability to explore the environment and exploit elitism while increasing computing costs. The third classification is based on algorithmic behavior, giving us an essential insight into how the population is updated for the next generation. The classification according to the number of parameters allows us to look into the number of control parameters involved and their roles in each of the algorithms. Another aspect of the number of parameters is how algorithms are set up and how sensitive they are to changes in the parameters they contain. Less parameter-based MAs, in general, are easy to handle for any optimization problem. Consequently, fewer parameters with highly efficient MAs are preferable for industrial optimization problems.

### Fig. 8 Classification of MAs based on the number of primary parameters
(confirmed from screenshot)

- **Free-Parameter based Algorithms (FPAs)**
  - Teaching Learning Based Algorithm (TLBA)
  - Black Hole Algorithm (BH)
  - Multi-Particle Collision Algorithm (M-PCA)
  - Symbiosis Organisms Search (SOS)
  - Vortex Search Optimization (VS)

- **Mono-Parameter based Algorithms (MPAs)**
  - Cuckoo Search (CS)
  - Artificial Cooperative Search (ACS)
  - Salp Swarm Algorithm (SSA)
  - Harris Hawks Optimizer (HHO)
  - Social Group Optimization (SGO)

- **Bi-Parameter based Algorithms (BPAs)**
  - Differential Evolution (DE)
  - Multi-Verse Optimizer (MVO)
  - Whale Optimization Algorithm (WOA)
  - Grey Wolf Optimizer (GWO)

- **Tri-Parameter based Algorithms (TrPAs)**
  - Genetic Algorithm (GA)
  - Harmony Search (HS)
  - Firefly Algorithm (FA)
  - Squirrel Search Algorithm (SSA)
  - Equilibrium Optimizer (EO)

- **Tetra-Parameter based Algorithms (TePAs)**
  - Sine Cosine Algorithm (SSA) [as shown in figure]
  - Archimedes Optimization Algorithm (AOA)
  - Gravitational Search Algorithm (GSA)
  - Football Game Algorithm (FGA)

- **Penta-Parameter based Algorithms (PPAs)**
  - Particle Swarm Optimization (PSO)
  - Farmland Fertility Algorithm (FFA)
  - Cheetah Chase Algorithm (CCA)

- **Miscellaneous**
  - Biogeography Based Optimization (BBO)
  - Henry Gas Solubility Optimization (HGSO)
  - Bonobo Optimizer (BO)
  - Intelligent Water Drop Algorithm (IWD)

---

# 7 Applications

MAs are usually more computationally expensive; it is not employed to solve simple real-world optimization problems that can be solved using standard gradient-based optimization tools. These problems are frequently non-linear and constrained by many non-linear constraints, raising numerous issues such as time restrictions and ‘cures of dimensionality’ in search of the optimal solution. We highlight a number of applications that are highly dependent on MAs.

## 7.1 NP-hard problems

NP-Hardness is a property of problems that are ‘at least as hard as the hardest problems in NP’. Exhaustive search methods are not applicable to find the best solution for large NP-Hard instances, due to their high computational cost.

- The most well-known problem in combinatorial optimization NP-Hard is the Travelling Salesman Problem (TSP), which poses the following question: ‘Given a list of cities and the distances between each pair of cities, what is the shortest route that visits each city precisely once and returns to the initial city?’ (Gutin and Punnen 2006). For example, there are approximately 1.22 × 10¹⁷ feasible solutions for a TSP with 20 cities. Thus, an exhaustive search to find a global optimum solution would take a long time. The high computational cost involved in solving TSP problems can be significantly reduced by the use of MAs, which are often able to provide near-optimal solutions in reasonable time (Panwar and Deep 2021). A generalization of TSP is the vehicle routing problems (VRPs) that are more realistic since they typically correspond to industry challenges, notably in logistics. Because such problems are multi-objective, they are widely utilized to represent real-world settings. Metaheuristics such as ant colony optimization (ACO), particle swarm optimization (PSO), genetic algorithm (GA) are now frequently used to solve them (Jozefowiez et al. 2008).

- Job Shop Scheduling (JSS) is a well-known NP-Hard problem, which means no algorithm can solve it in polynomial time in terms of problem size. Because it contains a finite set of jobs that must be processed on a limited set of machines, JSS is the most general sort of scheduling problem. Numerous researchers have attempted to cope with JSS using simulated annealing (SA), firefly algorithm (FA), bat algorithm (BA), cuckoo search (CS), and artificial bee colony (ABC), among others (Zhang et al. 2017a). Prakasam and Savarimuthu (2015) have shown that it is possible to solve other related NP-Hard problems using the generic implementation based on polynomial turing reduction.

## 7.2 Medical science

Electronic chips and computers are the backbones of many medical imaging, diagnostic, monitoring, and treatment devices. These devices, made up of numerous hardware components, are maintained and controlled by software based on algorithms.

de Carvalho Filho et al. (2014) used a genetic algorithm to find a way to find and classify solitary lung nodules automatically. The designed algorithm could detect lung nodules with about 86% sensitivity, 98% specificity, and 98% accuracy. In several studies, genetic algorithm (GA) was successfully employed to align MRI and CT scan pictures (Valsecchi et al. 2012). Another study used genetic algorithm (GA) to merge PET and MRI images to create coloured breast cancer images (Baum et al. 2011). Aneuploidy occurs when one or a few chromosomes in a cell’s nucleus are above or below the species typical chromosome count. However, the time required for these approaches necessitates the development of speedier diagnostic tests. To this objective, the proteomic profile of amniotic fluid samples was determined by mass spectrometry and analyzed by genetic algorithm (GA). The suggested approach could detect aneuploidy with 100% sensitivity, 72–96% specificity and 11–50% positive and 100% negative predictive values (Wang et al. 2005). Castiglione et al. (2004) devised a GA-based approach for selecting the optimal HAART treatment plan for HIV control and immunological reconstitution. The most common complication of insulin therapy in patients with type-1 diabetes mellitus is hypoglycemia (T1DM). Hypoglycemia can cause changes in electroencephalogram patterns (EEGs). Nguyen et al. (2013) used a combination of genetic algorithm (GA), artificial neural network, and Levenberg–Marquardt (LM) training techniques to detect hypoglycemia based on EEG signals. A more advanced computer-aided decision-support system for classifying tumors and identifying cancer stages through the use of neural networks in conjunction with particle swarm optimization (PSO) and ant colony optimization (ACO) is described in (Suganthi and Madheswaran 2012). In histopathology (to the microscopic examination of tissue to study the manifestations of the disease), artificial bee colon (ABC) has been used widely. To examine color, retinal scientists use the firefly algorithm (FA). A technique based on the artificial bee colony (ABC) algorithm is proposed for determining the IIR filter coefficients capable of removing doppler noise in the aortic valve efficiently (Koza et al. 2012). Particle swarm optimization (PSO) algorithm is used to improve the dynamic programming for segmenting the masses in the breast. Additionally, the ant colony optimization (ACO) hybridized Fuzzy technique is used to detect brain cancer. The capacity of these powerful algorithms to offer solutions to the myriad complicated difficulties physicians face every day has not been adequately explored in medicine.

## 7.3 Semantic web

The semantic web is an extension of the World Wide Web (WWW), whose primary goal is to make internet data machine-readable. The World Wide Web is a vast collection of web pages. SNOMED CT’s medical terminology ontology alone includes 370,000 class names, and current technology has not yet eliminated all semantically repetitive terms. GA-based algorithms and automated reasoning systems have been dealing with this currently. For the discovery of multi-relational association rules in the semantic web, Alippi et al. (2009) have used genetic algorithm (GA). Hsinchun et al. (1998) utilized genetic algorithm (GA) to develop a personalized search agent, and also he developed the quality of web search. Another multi-agent tool to perform a dynamic web search, Infospider, was developed by Menczer et al. (2004) with the help of genetic algorithm (GA) and artificial nural network. For the automatic composition of semantic web services, Wang et al. (2012) used ant colony optimization (ACO). Page classification, content mining, and also for organizing the web content dynamically scientists have used ant colony optimization (ACO).

## 7.4 Industry

Industry 4.0 is a result of next-level stuffs. The self-driving automobile is one of example. The automated control problem in self-driving cars includes routing. Shalamov et al. (2019) address the self-driving taxi routing problem formalized as the Pickup and Delivery Problem (PDP) by using common variable neighborhood search (VNS) algorithm and genetic algorithm (GA) for solution search. 5G will have more system capacity and spectral efficiency than 4G, as well as a greater number of network-connected wireless devices. Furthermore, the wireless communications infrastructure that exists today will not match the requirements of a 5G environment since a big number of traffic flows will be generated between a huge number of heterogeneous devices. The deployment strategy is one of the promising solutions to meet the expected demands of 5G. A major issue is the deployment of wireless communication and a hyper-dense deployment problem (HDDP) for 5G specifications. Tsai et al. (2015) provide a simple example of how a metaheuristic algorithm can solve the HDDP. Also, NSGA-II, MOEA/D, and NSGA-III are widely used in wireless sensor networks, electrical distribution system, and network reconfiguration for losses reduction (Sharma and Kumar 2022). The majority of optimization algorithms are only suitable to certain problems with superior characteristics. Thus, a hybrid of two or more algorithms is used to handle very complicated optimization problems in order to find the optimal solution. Ojugo et al. (2013) have proposed a hybrid artificial neural network-gravitational search algorithm model to train the neural network to simulate future flood occurrence and provides a lead time warning for flood management. A recent advances of metaheuristics in training neural networks for industrial applications can be found in (Chong et al. 2021).

## 7.5 Swarm drones and robotics

Unmanned Aerial Vehicles (UAVs) are widely favored for civil and military operations due to their vertical take-off and landing capabilities, stable hovering, and exceptionally agile movement in congested environments. It is critical for the success of the missions that the UAVs follow a desired trajectory accurately and quickly in civilian activities such as mapping, logistics, search and rescue, and exploration and surveillance, as well as a variety of military missions such as defense, attack, surveillance, and supervision. Numerous studies have implemented MAs for parameter optimization to accomplish these tasks. Altan (2020) uses particle swarm optimization (PSO) and harris hawks optimizer (HHO) to tune the parameters for this task. Both control algorithms have been evaluated on pathways with various shapes, including rectangle, circle, and lemniscate. The acquired findings have been compared to the performance of a conventional PID controller, and it has been found that the suggested controller outperforms both the conventional PID and PSO-based controllers. Goel et al. (2018) used metaheuristics for path planning of Unmanned Aerial Vehicles (UAVs) in three dimensional dynamic environment which is considered a challenging task in the field of robotics. Recently, metaheuristics have made a substantial effect on the application fields of collaborative robots. Improving the particle swarm optimization (PSO) algorithm to get a superior robotic search method seems to be on trend. Martinez-Soto et al. (2012) presented a hybrid PSO-GA strategy for creating the best fuzzy logic controller for each search robot. A review on metaheuristics applications in robotics can be found in (Fong et al. 2015).

Amazon and other online retailers are already filing patents for multi-level drone-beehive fulfillment centers, allowing for the deployment of this technology within the built environment. The use of drones for parcel delivery has been extensively studied in recent years, particularly in the area of logistics optimization.

## 7.6 Differential equation

Many highly non-linear problems in engineering and science involve one or more ordinary differential equations (ODEs). Analytic methods frequently fail to solve ODEs. To find ODE solutions, approximate analytical methods are used. The variational iteration method (VIM), the homotopy analysis method (HAM), the bilaterally bounded method (MBB), and the Adomian double decomposition method (ADDM) are a few examples. Approximation methods were used in many studies to solve integrodifferential equations (linear/non-linear). Each of these numerical approximation techniques, however, has its own set of operational constraints. As a result, these approximate techniques may fail to solve a particular problem. ADDM was unable to generate physically plausible data for the Glauert-jet problem (Torabi et al. 2012). Furthermore, the HAM and VIM failed to accurately predict solid particle motion in a fluid for some parameter values. It is clear that there is a lack of a proper approach that meets the majority of engineering demands with unconventional and non-linear ODEs. The approximation is the best solution for differential equations or other problems that cannot be solved analytically. In recent years, the use of MAs to approximate ODE solutions has grown rapidly. They differ in terms of the strategy employed and the base approximate function.

For example, Lee (2006) has used a different approach called the bilaterally bounded method in conjunction with particle swarm optimization (PSO) to solve the blasius equation. Sadollah et al. (2015) demonstrate an intriguing fact: harmony search (HS), particle swarm optimization (PSO), and genetic algorithm (GA) are used to approximate solve real-life ODEs for longitudinal heat transfer fins with a variety of profiles (rectangular, trapezoidal, and concave parabolic profiles). In engineering heat transfer problem, genetic algorithm (GA) and particle swarm optimization (PSO) have been the most widely used algorithms. Partial differential equations (PDEs) have also been attempted to solve by MAs because the existing techniques are not promising for a few extremely difficult problems. Panagant and Bureerat (2014) have successfully implemented the differential algorithm (DE) for the solution of a number of PDEs. By defining a global approximate function, a PDE problem is transformed into an optimization problem constrained by equality constraints imposed by the PDE boundary conditions. The acquired findings are displayed and contrasted with the actual solutions. It is demonstrated that the proposed method has the potential to become a future meshless tool if the metaheuristic’s search performance is significantly improved.

## 7.7 Image processing

Preprocessing, segmentation, object identification, denoising, and recognition are the most important tasks in image processing. Image segmentation is an important step to solve the image processing problems. Decomposing and partitioning a picture is computationally intensive. Chouhan et al. (2018) use genetic algorithm (GA) to solve this problem because of its greater search capabilities. Genetic algorithm (GA) has been used to eliminate noise from a noisy image. Also, it has been used to improve natural contrast and magnify images (Dhal et al. 2019). Li et al. (2016a) propose a modified discrete variant of grey wolf optimizer (GWO) to address the multi-level image thresholding problem. Also, to obtain optimal thresholds for multi-level thresholding in an image, cuckoo search (CS) algorithm is used (Agrawal et al. 2013). Particle swarm optimization (PSO) has been applied in many areas in image processing, such as color segmentation, clustering, denoising, and edge detection of images (Djemame et al. 2019).

Table 3 provides a quick summary of the many applications of the most prominent MAs, including their source of inspiration, number of parameters, solution updation equations/operators, and total number of function evaluations.

---

## Table 3 Summary of applications of most popular MAs with their source of inspiration and number of parameters

### Particle Swarm Optimization (PSO)
- **Source of inspiration:** Bird swarm behaviour
- **Parameters:** 5
- **Updating equations/Operators:**
  - \( X_i(t + 1) = X_i(t) + V_i(t + 1) \)
  - \( V_i(t + 1) = V_i(t) + c_1 \cdot R_1 \cdot (P_i - X_i(t)) + c_2 \cdot R_2 \cdot (G - X_i(t)) \)
  - Where:
    - \(P_i\): personal best
    - \(G\): global best
    - \(c_1\): cognitive coefficient, \(0 \le c_1 \le 4\)
    - \(c_2\): social coefficient, \(0 \le c_2 \le 4\)
    - \(R_1, R_2\): uniform random number in \((0,1)\)
- **Function evaluations:** Population size (N) + N × number of iterations (T)
- **Applications:**
  - Healthcare:
    - Intelligence diagnosis
    - Disease detection and classification
    - Medical image segmentation
  - Environmental:
    - Agriculture monitoring
    - Flood control and routing
    - Pollutant concentration monitoring
  - Industrial:
    - Economic dispatch problem
    - Phasor measurement unit placement
  - Commercial:
    - Risk assessment
    - Predicting cost and price
  - Smart city:
    - Smart home
    - Traffic monitoring and scheduling
- **Reference:** Gad (2022)

### Genetic Algorithm (GA)
- **Source of inspiration:** Darwin’s theory of evolution
- **Parameters:** 3
- **Updating equations/Operators:**
  - Selection Operator
  - Crossover Operator
  - Mutation Operator
- **Function evaluations:** N + N × T
- **Applications:**
  - Operation management:
    - Facility layout and Scheduling
    - Inventory control
    - Forecasting and network design
  - Multimedia:
    - Information security
    - Image processing
    - Video processing and Gaming
  - Wireless networking:
    - Load balancing
    - Localization
    - Bandwidth and channel allocation
- **Reference:** Katoch et al. (2021)

### Ant Colony Optimization (ACO)
- **Source of inspiration:** The foraging behaviour of ant colonies
- **Parameters:** 5
- **Updating equations/Operators:**
  - Pheromones updation
  - \( \tau_{ij}^{new} = (1 - \rho)\cdot \tau_{ij}^{old} + \sum_k \Delta \tau_{ij}^k \)
  - Where:
    - \(\rho\): evaporation rate
    - \(\Delta \tau_{ij}^k\): pheromone amount laid by kth ant
- **Function evaluations:** Basic ACO was developed for TSP. The best path is chosen based on the density of pheromone. Pheromone is calculated for every path in each iteration.
- **Applications:**
  - Transportation:
    - Traveling salesman problem
    - Vehicle routing search
  - Set problems:
    - Set partitioning and covering
    - Maximum independent set
    - Bin packing
  - Scheduling:
    - Job shop scheduling
    - Flow shop scheduling
  - Bio-informatics:
    - Protein folding
    - DNA sequencing
- **Reference:** Dorigo and Stützle (2019)

### Differential Evolution Algorithm (DE)
- **Source of inspiration:** Darwin’s theory of evolution
- **Parameters:** 2
- **Updating equations/Operators:**
  - Mutation operator
  - Crossover operator
  - Selection operator
- **Function evaluations:** N + N × T
- **Applications:**
  - Electrical and power systems:
    - Economic dispatch
    - Power system stabilizer
    - Optimal power flow
  - Robotics and Expert Systems:
    - Space trajectory optimization
    - Satellite orbit reconfiguration
    - Guidance of unmanned vehicles
  - Artificial Neural Networks:
    - Optimal network topology
    - Neural network training
    - Non-linear system identification
  - Operation Research:
    - Transport in docking systems
    - Manufacturing optimization
    - Scheduling
- **Reference:** Das et al. (2016)

### Simulated Annealing (SA)
- **Source of inspiration:** Annealing process in metallurgy
- **Parameters:** 2
- **Updating equations/Operators:**
  - Generate a new point \(x(k)\) randomly in a neighborhood of the current point
- **Function evaluations:** 1 + T
- **Applications:**
  - Telecommunication:
    - Mobile network design
    - Routing
    - Channel allocation
  - Chemical industry:
    - Antenna array synthesis
    - Refinery model problem
  - Operational:
    - Facility layout problems
    - Flexible Manufacturing system
- **References:** Suman and Kumar (2006); Delahaye et al. (2019)

### Tabu Search (TA)
- **Source of inspiration:** Social tabu
- **Parameters:** 2
- **Updating equations/Operators:** Moves
- **Function evaluations:** 1 + number of created neighbors in each iteration × T
- **Applications:**
  - Transportation:
    - Travelling salesman problem
    - Vehicle routing Problem
    - Quadratic assignment problem
  - Neural network:
    - Multi-layer network
    - Training
  - Others:
    - Economic dispatch problems
    - Telecommunication
    - Clustering
- **References:** Skorin-Kapov (1990); Amuthan and Thilak (2016)

### Grey Wolf Optimizer (GWO)
- **Source of inspiration:** leadership hierarchy and hunting mechanism of grey wolves
- **Parameters:** 2
- **Updating equations/Operators:**  
  OCR-damaged vector equations, approximately:
  - \( \vec{X}(t+1) = \vec{X_p}(t) - \vec{A}\cdot \vec{D} \)
  - \( \vec{D} = |\vec{C}\cdot \vec{X_p}(t) - \vec{X}(t)| \)
  - \( \vec{A} = 2\vec{a}\cdot \vec{r_1} - \vec{a} \)
  - \( \vec{C} = 2\cdot \vec{r_2} \)
  - \(\vec{A}\) and \(\vec{C}\) are coefficient vectors
  - \(\vec{X_p}\): position vector of the prey
  - \(\vec{X}\): position vector of a grey wolf
  - \(r_1, r_2 \in U[0,1]\)
- **Function evaluations:** N + N × T
- **Applications:**
  - Medical and Bio-informatics:
    - Parkinson’s disease diagnosis
    - Breast cancer diagnosis
  - Environmental applications:
    - Water pollution assessment
    - Thermal pollution assessment
  - Machine learning:
    - Feature selection
    - Training neural networks
    - Clustering applications
  - Engineering applications:
    - Design and tuning controllers
    - Power dispatch problems
    - Robotics and path planning
  - Image processing:
    - Multi-level image threshold problem
    - Template matching problems
    - Hyper-spectral image classification
- **Reference:** Faris et al. (2018)

### Artificial Bee Colony (ABC)
- **Source of inspiration:** the foraging behavior of honey bees when seeking a quality food source
- **Parameters:** 1
- **Updating equations/Operators:**
  - \( v_{ij} = x_{ij} + \phi_{ij}(x_{ij} - x_{kj}) \)
  - Where:
    - \(x_k\): randomly selected food source
    - \(i\): randomly chosen parameter index
    - \(\phi_{ij}\): random number within the range \([-1,1]\)
- **Function evaluations:** \(N + [2N + \text{number of scout bees}] \times T\)
- **Applications:**
  - Neural networks:
    - Signal processing applications
    - Machine learning
  - Electrical engineering:
    - Distribution system
    - Accident diagnosis in nuclear plant
    - Radial distribution system
  - Civil engineering:
    - Grinding parameter optimization
    - Heat exchangers
    - Truss structures
  - Data mining:
    - Fuzzy clustering
    - Chilli expert advisory system
  - Software engineering:
    - Automated maintenance of software
    - Software test suite optimization
- **Reference:** Karaboga et al. (2014)

### Cuckoo Search (CS)
- **Source of inspiration:** the brood parasitism of some cuckoo species
- **Parameters:** 1
- **Updating equations/Operators:**
  - \( x_i^{t+1} = x_i^t + \alpha \oplus \text{Levy}(\lambda) \)
  - Where:
    - \(\alpha\) = Step size
    - \(\lambda\) = Levy exponent
    - \(\oplus\) = Entry wise multiplication
- **Function evaluations:** N + 2NT
- **Applications:**
  - Medical applications:
    - Medical image segmentation
    - Disease detection and classification
  - Image processing:
    - Image segmentation
    - Enhancement
    - Clustering
  - Engineering applications:
    - Economic dispatch problem
    - Design and tuning controllers
- **References:** Shehab et al. (2017); Agrawal et al. (2013)

### Harmony Search (HS)
- **Source of inspiration:** musical performance process
- **Parameters:** 3
- **Updating equations/Operators:**
  - \( x_{ij} = x_{ij} + r_1 \times BW \)
  - \( x_{ij} = l_{ij} + r_2 \times (u_{ij} - l_{ij}) \)
  - Where:
    - BW: band width
    - \(r_1, r_2\): uniform random number in \((0,1)\)
    - \(u_{ij}\): upper bound of \(x_{ij}\)
    - \(l_{ij}\): lower bound of \(x_{ij}\)
- **Function evaluations:** N + N × T
- **Applications:**
  - Industrial application:
    - Logistics
    - Tour planning
    - Self driving car
  - Computer science:
    - Web page and document clustering
    - Internet routing
    - Robotics
  - Electrical engineering:
    - Energy system dispatch
    - Power system design
    - Photo electronic detection
  - Medical Studies:
    - RNA structure prediction
    - Medical image
    - Forecasting influenza season
- **Reference:** Ala’a et al. (2019)

---

# 8 Limitation and open problem

The main difference between deterministic and stochastic algorithms is that a deterministic algorithm, such as the simplex method, always provides the optimal solution. In comparison, a stochastic algorithm does not guarantee optimality, but rather a satisfactory solution. This is a significant disadvantage of MAs. However, the deterministic method fails miserably when confronted with increased complexity, such as a higher dimension or a non-differentiable function. This fact, however, can be interpreted as a ‘give and take’ policy. We must give up ‘something’ in order to gain ‘something’. We get a decent result, but we risk losing perfect precision. The ‘curse of dimensionality’ affects the performance of several MAs as the problem size increases. MAs used to solve problems involving a large number of choice variables, referred to as large scale global optimization (LSGO) problems, typically have a significant computational cost. A lack of mathematical analysis is a drawback for many MAs. There is currently no strong theoretical notion that overcomes this limitation: critics argue that, in comparison to physics, chemistry, or mathematics, the field of metaheuristics is still in its infancy. Despite the fact that metaheuristics have been demonstrated to handle a wide range of NP-Hard problems, this field is still missing in terms of convergence rate, complexity, and run time analysis, according to the study. Theoretically, if time is not a constraint, MAs can locate the optimal solution. However, since time is limited, we have to find a solution at a reasonable time. Therefore, there is a gap between theory and practical implementation. To prove the efficiency of the algorithm, a set of benchmark functions is chosen. How do these common benchmark test sets and evaluation criteria represent real-world problem characteristics? This benchmark function is complex but is these really can be used as a practical optimization problem? The answer is ‘No’. As a result, many algorithms can demonstrate their efficacy in papers yet fail miserably when applied to real-world problems. There is no single unified work to compare all MAs. Most of them need good parameter tuning and a better convergence rate. Many researchers work with them and find some way to enhance them by parallelism. We need a much stronger notion to cope with this situation. Some open challenges are as follows:

- How to provide a unified framework for mathematically analyzing all MAs to determine their convergence, rate of convergence, stability, and robustness? (Yang 2020)
- How to optimize an algorithm’s parameters for a certain group of problems? How to alter or adjust these parameters to optimize an algorithm’s performance? (Yang 2020)
- What benchmarks are useful? Do free lunches exist, and if so, under what circumstance? Can you prepare a genuine set of reliable benchmark functions? (Yang 2020)
- What performance measurements should be used to compare all algorithms fairly? Is it feasible to compare all algorithms honestly and rigorously? (Yang 2020)
- How to efficiently scale up algorithms that perform well for LSGO, real-world challenges? (Yang 2020)
- What is the NFL in terms of several dimensions?
- Two essential principles in the MAs are exploration and exploitation. These are diametrically opposed to one another, so how do you balance them for the best performance? (Črepinšek et al. 2013)

---

# 9 Future scope

Almost every science and engineering problem, and almost every life problem in general, can be framed as an optimization problem if we look closely enough. MAs, as given in the application Sect. 7, solve a wide range of problems. There are numerous future scopes. Several of them are listed below.

- Metaheuristics have been implemented to enhance parallel or distributed computation in modern technology of parallel computing. Alba (2005) explores metaheuristics in this domain and highlights relevant research paths to strengthen outcomes. They are unquestionably the most powerful optimization algorithms that will have a major impact on future generation computing.

- There have been very few efforts yet to further strengthen the scalability of the LSGO methods for addressing LSGO benchmark test sets with dimensions greater than 1000. Scalability of LSGO methods becomes a critical prerequisite, with significant implications for future study (Mahdavi et al. 2015).

- In NP-hard problems such as the TSP, JSS, and Knapsack Problems, metaheuristics are still in their infancy. Despite numerous scholars’ efforts to use metaheuristics to overcome these difficulties, they remain critical. For example, UAV (drone) task assignment in logistics, 3D path planning in dynamic environment, 5 G cell deployment challenge, etc. can all bring about a revolution. Consequently, scholars should focus on these challenges.

- A significant area of study that needs to explore is intelligent sampling and surrogate modeling. The boundaries of the issue space are decreased by intelligent sampling, allowing for confined searching to the best neighborhoods, whilst surrogate approaches aid metaheuristics in evaluating computationally costly functions by approximating the actual objective function. The limited work that has been done in this approach has shown tremendous promise. Mann and Singh (2017), for example, enhanced performance of artificial bee colony (ABC) by using a sampling technique called the Student’s-t distribution.

- Another useful study area is the evaluation of structural bias in population-based heuristics, which is the limitation of particular metaheuristics to focus on a subset of the solution space (Kononova et al. 2015). Due to the intrinsic algorithmic structure of such algorithms, they may sample solutions more frequently near the origin, near the boundary, or near any other specific area of the search space. Structural bias can drastically affect the performance of various popular MAs, as demonstrated by Piotrowski and Napiorkowski (2018). Similar research should be conducted with newer metaheuristics to clarify their behavior when sampling the solution space. Furthermore, Markov chain theory, self-organized systems, filter theory, discrete and continuous dynamical systems, Bayesian statistics, computational complexity analysis, and other frameworks can be used to investigate intriguing algorithmic aspects (Yang 2018).

- Numerous billions of pages compose the World Wide Web. SNOMED CT’s ontology of medical terminology contains 370,000 in class names alone, and current technology has not yet eliminated all semantically redundant terms. Additionally, the Semantic Web’s shortcomings include ambiguity, inconsistency, and deception. Numerous studies have been undertaken in this area, and genetic algorithm (GA) addresses a number of the issues, while there are still a few unknown areas. One such area is the use of new generation algorithms such as grey wolf optimizer (GWO), cuckoo search (CS), and harmony search (HS) to semantic web reasoning, which is the future focus of study in this area.

- A promising but not fully explored direction is to solve highly non-linear ODEs and PDEs in engineering, physics, economics, fluids, and other disciplines. The ODEs and PDEs can be represented as an optimization problem with the Fourier series as the base approximate function.

- The algorithm selection task for black-box optimization problems is considered an important task. FLA has been demonstrated to be a useful tool for analyzing the hardness of an optimization problem by extracting its features. Wang et al. (2017) introduced the concept of population evolvability, which is an extension of dynamic FLA, to quantify the effectiveness of population-based metaheuristics for solving a given problem. This area should be investigated for more sophisticated user-friendly FLA techniques.

- According to Zelinka (2015), there are still many unsolved questions. Several of the problems may be consolidated into one: can controlling the dynamics of a swarm and evolutionary algorithms considerably increase their performance and diversity in search operations? The study suggests many prospective potential research avenues for the future, ranging from swarm robotics to evolvable hardware to disrupting terrorist communication.

- Metaheuristic and artificial intelligence can be combined to design a more effective optimization tool. In recent years, interest in the research of evolutionary transfer learning (ETO) has increased (Tan et al. 2021). ETO is a paradigm that combines EAs with knowledge learning and transfer across related domains to improve optimization efficiency and performance. Evolutionary multitasking is a very promising example of ETO, demonstrating that this might be a very valuable concept in the real world application (Gupta et al. 2015).

---

# 10 Conclusion

This study aims to conduct a state-of-the-art survey of metaheuristics. In order to develop a toolkit for researchers, this study assembled most of the existing MAs (approximately 540). Also, for better comprehension, statistical data is collected and analyzed. It can be concluded from the statistical data that during the last decade, approximately 38 MAs come on average each year. However, the majority of new generation algorithms lack originality and resemble to existing algorithms such as particle swarm optimization (PSO), genetic algorithm (GA), differential algorithm (DE), ant colony optimization (ACO), and artificial bee colony (ABC).

Various existing taxonomies of MAs based on source of inspiration, population size, and population movement are addressed along with their advantages and disadvantages. In this study, a novel taxonomy of MAs based of number of primary parameters is proposed. The existing MAs are classified in seven categories based on the different number of primary parameters. The MAs having 0, 1, 2, 3, 4, and 5 primary parameters are classified as free parameter, mono-parameter, bi-parameter, tri-parameter, tetra-parameter, and penta-parameter based algorithms respectively. The MAs having more than five parameters are kept in miscellaneous category. In general, increase in the number of parameters raises the complexity of parameter tuning. Also, when dealing with a black box problem, tuning large number of parameters is a laborious task. That is why, efficient algorithms with less parameters are welcome to solve the complex industrial optimization problems. Apart from the classification of algorithms, a handful of the remarkable application areas of MAs such as medical, industry, robotics and swarm drones have been highlighted in this study. Additionally, theoretical lacks of existing MAs and open problems are discussed which can be addressed in future. Several significant avenues for future research have been mentioned.

As an extension of this study, further investigation may be necessary to identify the overall level of complexity that arises as the number of primary parameters increase. In addition, a state-of-the-art survey of all the recent variants of most popular algorithms such as particle swarm optimization (PSO), genetic algorithm (GA), differential algorithm (DE), and ant colony optimization (ACO) can be done. We believe this extensive survey of metaheuristics will assist our research community and newcomers in seeing the broad domain of metaheuristics and give it the proper direction it deserves.

---

## Acknowledgements

One of the authors, Kusum Deep, would like to acknowledge with thanks SERB, Govt. of India, under Grant No. SPG/2021/001416, for providing financial support to carry out this research. Additionally, all the authors appreciate the anonymous reviewers for their valuable feedback and insightful comments, which significantly improved the quality of the paper.

---

# Table 1 Metaheuristic algorithms (up to 2022)

Below is the full algorithm list as supplied.

| SN | Algorithm | References |
|---:|---|---|
| 1 | Across Neighbourhood Search (ANS) | Wu (2016) |
| 2 | Adaptive Social Behavior Optimization (ASBO) | Singh (2013) |
| 3 | African Buffalo Optimization (ABO) | Odili et al. (2015) |
| 4 | African Vultures Optimization Algorithm (AVOA) | Abdollahzadeh et al. (2021a) |
| 5 | African Wild Dog Algorithm (AWDA) | Subramanian et al. (2013) |
| 6 | Algorithm of the Innovative Gunner (AIG) | Pijarski and Kacejko (2019) |
| 7 | Ali Baba and the Forty Thieves Optimization (AFT) | Braik et al. (2022b) |
| 8 | Anarchic Socity Optimization (ASO) | Ahmadi-Javid (2011) |
| 9 | Andean Condor Algorithm (ACA) | Almonacid and Soto (2019) |
| 10 | Animal Behavior Hunting (ABH) | Naderi et al. (2014) |
| 11 | Animal Migration Optimization Algorithm (AMO) | Li et al. (2014) |
| 12 | Ant Colony Optimization (ACO) | Dorigo et al. (2006) |
| 13 | Ant Lion Optimizer (ALO) | Mirjalili (2015a) |
| 14 | Aphid-Ant Mutualism (AAM) | Eslami et al. (2022) |
| 15 | Aphids Optimization Algorithm (AOA) | Liu et al. (2022) |
| 16 | Archerfish Hunting Optimizer (AHO) | Zitouni et al. (2021) |
| 17 | Archery Algorithm (AA) | Zeidabadi et al. (2022) |
| 18 | Archimedes Optimization Algorithm (AOA) | Hashim et al. (2021) |
| 19 | Arithmetic Optimization Algorithm (AOA) | Abualigah et al. (2021b) |
| 20 | Aritificial Algae Algorithm (AAA) | Uymaz et al. (2015) |
| 21 | Artificial Atom Algorithm (A3) | Karci (2018) |
| 22 | Artificial Bee Colony (ABC) | Karaboga and Basturk (2007) |
| 23 | Artificial Beehive Algorithm (ABA) | Munoz et al. (2009) |
| 24 | Artificial Butterfly Optimization (ABO) | Qi et al. (2017) |
| 25 | Artificial Chemical Process (ACP) | Irizarry (2004) |
| 26 | Artificial Chemical Reaction Optimization Algorithm (ACROA) | Alatas (2011) |
| 27 | Artificial Cooperative Search (ACS) | Civicioglu (2013a) |
| 28 | Artificial Coronary Circulation System (ACCS) | Kaveh and Kooshkebaghi (2019) |
| 29 | Artificial Ecosystem Algorithm (AEA) | Adham and Bentley (2014) |
| 30 | Artificial Ecosystem-based Optimization (AEO) | Zhao et al. (2020b) |
| 31 | Artificial Electric Field Algorithm (AEFA) | Yadav et al. (2019) |
| 32 | Artificial Feeding Birds Algorithm (AFB) | Lamy (2019) |
| 33 | Artificial Fish Swarm Algorithm (AFSA) | Li (2003) |
| 34 | Artificial Flora Optimization Algorithm (AF) | Cheng et al. (2018) |
| 35 | Artificial Gorilla Troops Optimizer (GTO) | Abdollahzadeh et al. (2021b) |
| 36 | Artificial Hummingbird Algorithm (AHA) | Zhao et al. (2022b) |
| 37 | Artificial Infection Disease Optimization (AIO) | Huang (2016) |
| 38 | Artificial Jellyfish Search Optimizer (AJSO) | Chou and Truong (2021) |
| 39 | Artificial Lizard Search Optimization (ALSO) | Kumar et al. (2021) |
| 40 | Artificial Photosynthesis and Phototropism Mechanism (APPM) | Cui and Cai (2011) |
| 41 | Artificial Physics Optimization (APO) | Xie et al. (2009) |
| 42 | Artificial Plants Optimization Algorithm (APO) | Zhao et al. (2011) |
| 43 | Artificial Raindrop Algorithm (ARA) | Jiang et al. (2014) |
| 44 | Artificial Reaction Algorithm (ARA) | Melin et al. (2013) |
| 45 | Artificial Searching Swarm Algorithm (ASSA) | Chen et al. (2009) |
| 46 | Artificial Showering Algorithm (ASA) | Ali et al. (2015) |
| 47 | Artificial Swarm Intelligence (ASI) | Rosenberg and Willcox (2018) |
| 48 | Artificial Tribe Algorithm (ATA) | Chen et al. (2012) |
| 49 | Asexual Reproduction Optimization (ARO) | Farasat et al. (2010) |
| 50 | Atmosphere Clouds Model Optimization (ACMO) | Gao-Wei and Zhanju (2012) |
| 51 | Atomic Orbital Search (AOS) | Azizi (2021) |
| 52 | Backtracking Search Optimization (BSO) | Civicioglu (2013b) |
| 53 | Bacterial Chemotaxis Optimization (BCO) | Muller et al. (2002) |
| 54 | Bacterial Colony Optimization (BCO) | Niu and Wang (2012) |
| 55 | Bacterial Evolutionary Algorithm (BEA) | Numaoka (1996) |
| 56 | Bacterial Foraging Optimization Algorithm (BFOA) | Das et al. (2009) |
| 57 | Bacterial Swarming Algorithm (BSA) | Tang et al. (2007) |
| 58 | Bacterial-GA Foraging (BF) | Chen et al. (2007) |
| 59 | Bald Eagle Search (BES) | Alsattar et al. (2020) |
| 60 | Bar Systems (BS) | Del Acebo and de-la Rosa (2008) |
| 61 | Bat Algorithm (BA) | Yang and He (2013) |
| 62 | Bat Inspired Algorithm (BIA) | Yang (2010b) |
| 63 | Bat Intelligence (BI) | Malakooti et al. (2012) |
| 64 | Battle Royale Optimization (BRO) | Rahkar Farshi (2021) |
| 65 | Bean Optimization Algorithm (BOA) | Zhang et al. (2010) |
| 66 | Bear Smell Search Algorithm (BSSA) | Ghasemi-Marzbali (2020) |
| 67 | Bee Colony Optimization (BCO) | Teodorovic and Dell’Orco (2005) |
| 68 | Bee Conoly-Inspired Algorithm (BCIA) | Häckel and Dippold (2009) |
| 69 | Bee Swarm Optimization (BSO) | Akbari et al. (2010) |
| 70 | Bee System (BS) | Sato and Hagiwara (1998) |
| 71 | Bee System.1 (BS.1) | Lucic and Teodorovic (2002) |
| 72 | BeeHive (BH) | Wedde et al. (2004) |
| 73 | Bees Algorithm (BA) | Pham et al. (2006) |
| 74 | Bees Life Algorithm (BLA) | Bitam et al. (2018) |
| 75 | Beetle Swarm Optimization Algorithm (BSOA) | Wang and Yang (2018) |
| 76 | Beluga Whale Optimization (BWO) | Zhong et al. (2022) |
| 77 | Big Bang-Big Crunch (BBBC) | Erol and Eksin (2006) |
| 78 | Billiards-Inspired Optimization Algorithm (BOA) | Kaveh et al. (2020b) |
| 79 | Binary Slime Mould Algorithm (BSMA) | Abdel-Basset et al. (2021) |
| 80 | Binary Whale Optimization Algorithm (bWOA) | Reddy K et al. (2019) |
| 81 | Biogeography-Based Optimization (BBO) | Simon (2008) |
| 82 | Biology Migration Algorithm (BMA) | Zhang et al. (2019) |
| 83 | Bioluminiscent Swarm Optimization (BSO) | de Oliveira et al. (2011) |
| 84 | Biomimicry of Social Foraging Bactera for Distributed (BSFBD) | Passino (2002) |
| 85 | Bird Mating Optimization (BMO) | Askarzadeh (2014) |
| 86 | Bird Swarm Algorithm (BSA) | Meng et al. (2016) |
| 87 | Bison Behavior Algorithm (BBA) | Kazikova et al. (2017) |
| 88 | Black Hole Algorithm (BH.1) | Hatamlou (2013) |
| 89 | Black Hole Mechanics Optimization (BHMO) | Kaveh et al. (2020c) |
| 90 | Blind, Naked Mol-Rats Algorithm (BNMR) | Taherdangkoo et al. (2013) |
| 91 | Blue Monkey Algorithm (BM) | Mahmood and Al-Khateeb (2019) |
| 92 | Boids | Reynolds (1987) |
| 93 | Bonobo Optimizer (BO) | Das and Pratihar (2019) |
| 94 | Brain Storm Optimization (BSO) | Shi (2011) |
| 95 | Bull Optimization Algorithm (BOA) | FINDIK (2015) |
| 96 | Bumble Bees Mating Optimization (BBMO) | Marinakis et al. (2010) |
| 97 | Bus Transport Algorithm (BTA) | Bodaghi and Samieefar (2019) |
| 98 | Butterfly Optimization Algorithm (BOA) | Arora and Singh (2019) |
| 99 | Butterfly Optimizer (BO) | Kumar et al. (2015) |
| 100 | Buzzards Optimization Algorithm (BOA) | Arshaghi et al. (2019) |
| 101 | Camel Algorithm (CA) | Ibrahim and Ali (2016) |
| 102 | Camel Herd Algorithm (CHA) | Al-Obaidi et al. (2017) |
| 103 | Capuchin Search Algorithm (CapSA) | Braik et al. (2021) |
| 104 | Car Tracking Optimization Algorithm (CTOA) | Chen et al. (2018) |
| 105 | Cat Swarm Optimization (CSO) | Chu et al. (2006) |
| 106 | Catfish Particle Swarm Optimization (CatfishPSO) | Chuang et al. (2008) |
| 107 | Central Force Optimizartion (CFO) | Formato (2008) |
| 108 | Chaos Game Optimization (CGO) | Talatahari and Azizi (2021) |
| 109 | Chaos Optimization Alfgorithm (COA) | JIANG (1998) |
| 110 | Chaotic Dragonfly Algorithm (CDA) | Sayed et al. (2019b) |
| 111 | Charged System Search (CSS) | Kaveh and Talatahari (2010) |
| 112 | Cheetah Based Algorithm (CBA) | Klein et al. (2018) |
| 113 | Cheetah Chase Algorithm (CCA) | Goudhaman (2018) |
| 114 | Cheetah Optimizer (CO) | Akbari et al. (2022) |
| 115 | Chef-Based Optimization Algorithm (CBOA) | Trojovská and Dehghani (2022) |
| 116 | Chemical Reaction Optimization (CRO) | Alatas (2011) |
| 117 | Chicken Swarm Optimization (CSO) | Meng et al. (2014) |
| 118 | Child Drawing Development Optimization (CDDO) | Abdulhameed and Rashid (2022) |
| 119 | Chimp Optimization Algorithm (ChOA) | Khishe and Mosavi (2020) |
| 120 | Circle Search Algorithm (CSA) | Qais et al. (2022) |
| 121 | Circular Structures of Puffer Fish Algorithm (CSPF) | Catalbas and Gulten (2018) |
| 122 | Circulatory System-based Optimization (CSBO) | Ghasemi et al. (2022) |
| 123 | City Councils Evolution (CCE) | Pira (2022) |
| 124 | Clonal Selection Algorithm (CSA) | De Castro and Von Zuben (2000) |
| 125 | Cloud Model-Based Differential Evolution Algorithm (CMDE) | Zhu and Ni (2012) |
| 126 | Cockroach Swarm Optimization (CSO) | ZhaoHui and HaiYan (2010) |
| 127 | Cognitive Behavior Optimization Algorithm (COA) | Li et al. (2016b) |
| 128 | Collective Animal Behavior (CAB) | Cuevas et al. (2012a) |
| 129 | Collective Decision Optimization Algorithm (CDOA) | Zhang et al. (2017b) |
| 130 | Colliding Bodies Optimization (CBO) | Kaveh and Mahdavi (2014) |
| 131 | Color Harmony Algorithm (CHA) | Zaeimi and Ghoddosian (2020) |
| 132 | Community of Scientist Optimization (CoSO) | Milani and Santucci (2012) |
| 133 | Competitive Learning Algorithm (CLA) | Afroughinia and Kardehi M (2018) |
| 134 | Competitive Optimization Algorithm (COOA) | Sharafi et al. (2016) |
| 135 | Consultant Guide Search (CGS) | Wu and Banzhaf (2010) |
| 136 | Co-Operation of Biology Related Algorithm (COBRA) | Akhmedova and Semenkin (2013) |
| 137 | Coral Reefs Optimization (CRO) | Salcedo-Sanz et al. (2014) |
| 138 | Corona Virus Optimization (CVO) | Salehan and Deldari (2022) |
| 139 | Coronavirus Herd Immunity Optimizer (CHIO) | Al-Betar et al. (2021) |
| 140 | Coronavirus Optimization Algorithm (COVIDOA) | Khalid et al. (2022) |
| 141 | Covariance Matrix Adaptation-Evolution Strategy (CMAES) | Hansen et al. (2003) |
| 142 | Coyote Optimization Algorithm (COA) | Pierezan and Coelho (2018) |
| 143 | Cricket Algorithm (CA) | Canayaz and Karcı (2015) |
| 144 | Cricket Behaviour-Based Algorithm (CBA) | Canayaz and Karci (2016) |
| 145 | Cricket Chirping Algorithm (CCA) | Deuri and Sathya (2018) |
| 146 | Crow Search Algorithm (CSA) | Askarzadeh (2016) |
| 147 | Crystal Energy Optimization Algorithm (CEO) | Feng et al. (2016) |
| 148 | Crystal Structure Algorithm (CryStAl) | Talatahari et al. (2021b) |
| 149 | Cuckoo Optimization Algorithm (COA) | Rajabioun (2011) |
| 150 | Cuckoo Search (CS) | Yang and Deb (2009) |
| 151 | Cultural Algorithm (CA) | Jin and Reynolds (1999) |
| 152 | Cultural Coyote Optimization Algorithm (CCOA) | Pierezan et al. (2019) |
| 153 | Cuttlefish Algorithm (CA) | Eesa et al. (2013) |
| 154 | Cyclical Parthenogenesis Algorithm (CPA) | Kaveh and Zolghadr (2017) |
| 155 | Dandelion Optimizer (DO) | Zhao et al. (2022a) |
| 156 | Deer Hunting Optimization Algorithm (DHOA) | Brammya et al. (2019) |
| 157 | Dendritic Cells Algorithm (DCA) | Greensmith et al. (2005) |
| 158 | Deterministic Oscillatory Search (DOS) | Archana et al. (2017) |
| 159 | Dialectic Search (DS) | Kadioglu and Sellmann (2009) |
| 160 | Differential Evolution (DE) | Storn and Price (1997) |
| 161 | Differential Search Algorithm (DSA) | Civicioglu (2012) |
| 162 | Dolphin Echolocation (DE) | Kaveh and Farhoudi (2013) |
| 163 | Dolphin Partner Optimization (DPO) | Shiqin et al. (2009) |
| 164 | Dragonfly Algorithm (DA) | Mirjalili (2016a) |
| 165 | Driving Training-Based Optimization (DTBO) | Dehghani et al. (2022b) |
| 166 | Duelist Algorithm (DA) | Biyanto et al. (2016) |
| 167 | Dynamic Differential Annealed Optimization (DDAO) | Ghafil and Jármai (2020) |
| 168 | Dynastic Optimization Algorithm (DOA) | Wagan et al. (2020) |
| 169 | Eagle Strategy (ES) | Yang and Deb (2010) |
| 170 | Earthwarm Optimization Algorithm (EOA) | Wang et al. (2018a) |
| 171 | Ebola Optimization Search Algorithm (EOSA) | Oyelade and Ezugwu (2021) |
| 172 | Ecogeography-Based Optimization (EBO) | Zheng et al. (2014) |
| 173 | Eco-inspired Evolutionary Algorithm (EEA) | Parpinelli and Lopes (2011) |
| 174 | Egyptian Vulture Optimization (EV) | Sur et al. (2013) |
| 175 | Election-Based Optimization Algorithm (EBOA) | Trojovský and Dehghani (2022a) |
| 176 | Electromagnetic Field Optimization (EFO) | Abedinpourshotorban et al. (2016) |
| 177 | Electro-Magnetism Optimization (EMO) | Cuevas et al. (2012b) |
| 178 | Electromagnetism-Like Mechanism Optimization (EMO) | Birbil and Fang (2003) |
| 179 | Electron Radar Search Algorithm (ERSA) | Rahmanzadeh and Pishvaee (2020) |
| 180 | Elephant Clan Optimization (ECO) | Jafari et al. (2021) |
| 181 | Elephant Herding Optimization (EHO) | Wang et al. (2015) |
| 182 | Elephant Search Algorithm (ESA) | Deb et al. (2015) |
| 183 | Elephant Swarm Water Search Algorithm (ESWSA) | Mandal (2018) |
| 184 | Emperor Penguin Optimizer (EPO) | Dhiman and Kumar (2018) |
| 185 | Emperor Penguins Colony (EPC) | Harifi et al. (2019) |
| 186 | Escaping Bird Search (EBS) | Shahrouzi and Kaveh (2022) |
| 187 | Eurasian Oystercatcher Optimiser (EOO) | Salim et al. (2022) |
| 188 | Evolution Strategies (ES) | Beyer and Schwefel (2002) |
| 189 | Exchange Market Algorithm (EMA) | Ghorbani et al. (2017) |
| 190 | Extremal Optimization (EO) | Boettcher and Percus (1999) |
| 191 | Farmland Fertility Algorithm (FFA) | Shayanfar and Gharehchopogh (2018) |
| 192 | Fast Bacterial Swarming Algorithm (FBSA) | Chu et al. (2008) |
| 193 | Fertilization Optimization Algorithm (FOA) | Ghafil et al. (2022) |
| 194 | Fibonacci Indicator Algorithm (FIA) | Etminaniesfahani et al. (2018) |
| 195 | FIFA Word Cup Competitions (FIFA) | Razmjooy et al. (2016) |
| 196 | Find-Fix-Finish-Exploit-Analyze Algorithm (F3EA) | Kashan et al. (2019) |
| 197 | Fire Hawk Optimizer (FHO) | Azizi et al. (2022) |
| 198 | Firefly Algorithm (FA) | Yang (2009) |
| 199 | Fireworks Algorithm (FA) | Tan and Zhu (2010) |
| 200 | Fireworks Optimization Algorithm (FOA) | Ehsaeyan and Zolghadrasli (2022) |
| 201 | Fish School Search (FSS) | Bastos Filho et al. (2008) |
| 202 | Fish Swarm Algorithm (FSA) | Tsai and Lin (2011) |
| 203 | Fitness Dependent Optimizer (FDO) | Abdullah and Ahmed (2019) |
| 204 | Flock by Leader (FL) | Bellaachia and Bari (2012) |
| 205 | Flocking Based Algorithm (FA) | Cui et al. (2006) |
| 206 | Flow Direction Algorithm (FDA) | Karami et al. (2021) |
| 207 | Flow Regime Algorithm (FRA) | Tahani and Babayan (2019) |
| 208 | Flower Pollination Algorithm (FPA) | Yang (2012) |
| 209 | Flying Elephant Algorithm (FEA) | Xavier and Xavier (2016) |
| 210 | Football Game Algorithm (FGA) | Fadakar and Ebrahimi (2016) |
| 211 | Forensic Based Investigation (FBI) | Chou and Nguyen (2020) |
| 212 | Forest Optimization Algorithm (FOA) | Ghaemi and Feizi-Derakhshi (2014) |
| 213 | Fox Optimizer (FOX) | Mohammed and Rashid (2022) |
| 214 | Fractal-Based Algorithm (FA) | Kaedi (2017) |
| 215 | Frog Call Inspired Algorithm (FCA) | Mutazono et al. (2009) |
| 216 | Fruit Fly Optimization Algorithm (FOA) | Pan (2012) |
| 217 | Gaining Sharing Knowledge Based Algorithm (GSK) | Mohamed et al. (2020) |
| 218 | Galactic Swarm Optimization (GSO) | Muthiah-Nakarajan and Noel (2016) |
| 219 | Galaxy Based Search Algorithm (GBS) | Shah-Hosseini (2011) |
| 220 | Gannet Optimization Algorithm (GOA) | Pan et al. (2022) |
| 221 | Gases Brownian Motion Optimization (GBMO) | Abdechiri et al. (2013) |
| 222 | Gene Expression (GE) | Ferreira (2002) |
| 223 | Genetic Algorithm (GA) | Holland (1991) |
| 224 | Genetic Programming (GP) | Koza et al. (1994) |
| 225 | Geometric Octal Zones Distance Estimation Algorithm (GOZDE) | Kuyu and Vatansever (2022) |
| 226 | Giza Pyramids Construction Algorithm (GPC) | Harifi et al. (2020) |
| 227 | Global Neighborhood Algorithm (GNA) | Alazzam and Lewis (2013) |
| 228 | Glowworm Swarm Optimization (GSO) | Zhou et al. (2014) |
| 229 | Golden Ball Algorithm (GB) | Osaba et al. (2014) |
| 230 | Golden Eagle Optimizer (GEO) | Mohammadi-Balani et al. (2021) |
| 231 | Golden Jackal Optimization (GJO) | Chopra and Ansari (2022) |
| 232 | Golden Search Optimization Algorithm (GSO) | Noroozi et al. (2022) |
| 233 | Golden Sine Algorithm (Gold-SA) | Tanyildizi and Demir (2017) |
| 234 | Good Lattice Swarm Optimization (GLSO) | Su et al. (2007) |
| 235 | Goose Team Optimizer (GTO) | Wang and Wang (2008) |
| 236 | Gradient Evolution Algorithm (GE) | Kuo and Zulvia (2015) |
| 237 | Gradient-Based Optimizer (GBO) | Ahmadianfar et al. (2020) |
| 238 | Grasshoper Optimization Algorithm (GOA) | Saremi et al. (2017) |
| 239 | Gravitational Clustering Algorithm (GCA) | Kundu (1999) |
| 240 | Gravitational Emulation Local Search (GELS) | Barzegar et al. (2009) |
| 241 | Gravitational Field Algorithm (GFA) | Zheng et al. (2010) |
| 242 | Gravitational Interactions Optimization (GIO) | Flores et al. (2011) |
| 243 | Gravitational Search Algorithm (GSA) | Rashedi et al. (2009) |
| 244 | Great Deluge Algorithm (GDA) | Dueck (1993) |
| 245 | Greedy Politics Optimization (GPO) | Melvix (2014) |
| 246 | Grenade Explosion Method (GEM) | Ahrari and Atai (2010) |
| 247 | Grey Wolf Optimizer (GWO) | Mirjalili et al. (2014) |
| 248 | Group Counseling Optimization (GCO) | Eita and Fahmy (2014) |
| 249 | Group Escape Behavior (GEB) | Min and Wang (2011) |
| 250 | Group Leaders Optimization Algorithm (GIOA) | Daskin and Kais (2011) |
| 251 | Group Mean-Based Optimizer (GMBO) | Dehghani et al. (2021) |
| 252 | Group Search Optimizer (GSO) | He et al. (2009) |
| 253 | Group Teaching Optimization Algorithm (GTOA) | Zhang and Jin (2020) |
| 254 | Harmony Element Algorithm (HEA) | Cui et al. (2008) |
| 255 | Harmony Search (HS) | Lee and Geem (2005) |
| 256 | Harris Hawks Optimizer (HHO) | Heidari et al. (2019) |
| 257 | Heart Optimization (HO) | Hatamlou (2014) |
| 258 | Heat Transfer Optimization Aalgorithm (HTOA) | Asef et al. (2021) |
| 259 | Heat Transfer Search Agorithm (HTS) | Patel and Savsani (2015) |
| 260 | Henry Gas Solubility Optimization (HGSO) | Hashim et al. (2019) |
| 261 | Hirerarchical Swarm Model (HSM) | Chen et al. (2010) |
| 262 | Honey Badger Algorithm (HBA) | Hashim et al. (2022) |
| 263 | Honeybee Social Foraging (HSF) | Quijano and Passino (2007) |
| 264 | Honeybees Mating Optimization Algorithm (HMOA) | Haddad et al. (2006) |
| 265 | Hoopoe Heuristic (HH) | El-Dosuky et al. (2012) |
| 266 | Human Evolutionary Model (HEM) | Montiel et al. (2007) |
| 267 | Human Felicity Algorithm (HFA) | Veysari et al. (2022) |
| 268 | Human Group Formation (HGF) | Thammano and Moolwong (2010) |
| 269 | Human Mental Search (HMS) | Mousavirad and Ebrahimpour (2017) |
| 270 | Human-Inspired algorithm (HIA) | Zhang et al. (2009) |
| 271 | Hunting Search (HuS) | Oftadeh et al. (2010) |
| 272 | Hurricane Based Optimization Algorithm (HOA) | Rbouh and El Imrani (2014) |
| 273 | Hydrological Cycle Algorithm (HCA) | Wedyan et al. (2017) |
| 274 | Hysteresis for Optimization (HO) | Zarand et al. (2002) |
| 275 | Ideology Algorithm (IA) | Huan et al. (2017) |
| 276 | Imperialist Competitive Algorithm (ICA) | Atashpaz-Gargari and Lucas (2007) |
| 277 | Improve Genetic Immune Algorithm (IGIA) | Tayeb et al. (2017) |
| 278 | Integrated Radiation Optimization (IRO) | Chuang and Jiang (2007) |
| 279 | Intelligent Ice Fishing Algorithm (IIFA) | Karpenko and Kuzmina (2021) |
| 280 | Intelligent Water Drop Algorithm (IWD) | Shah-Hosseini (2009) |
| 281 | Interactive Autodidactic School Algorithm (IAS) | Jahangiri et al. (2020) |
| 282 | Interior Search Algorithm (ISA) | Gandomi (2014) |
| 283 | Invasive Tumor Growth Optimization (ITGO) | Tang et al. (2015) |
| 284 | Invasive Weed Optimization Algorithm (IWO) | Karimkashi and Kishk (2010) |
| 285 | Ions Motion Optimization (IMO) | Javidy et al. (2015) |
| 286 | Jaguar Algorithm (JA) | Chen et al. (2015) |
| 287 | Japanese Tree Frogs Calling Algorithm (JTFCA) | Hernández and Blum (2012) |
| 288 | Jaya Algorithm (JA) | Rao (2016) |
| 289 | Kaizen Programming (KP) | De Melo (2014) |
| 290 | Kernel Search Optimization (KSO) | Dong and Wang (2020) |
| 291 | Keshtel Algorithm (KA) | Hajiaghaei and Aminnayeri (2014) |
| 292 | Killer Whale Algorithm (KWA) | Biyanto et al. (2017) |
| 293 | Kinetic Gas Molecules Optimization (KGMO) | Moein and Logeswaran (2014) |
| 294 | Komodo Mlipir Algorithm (KMA) | Suyanto et al. (2021) |
| 295 | Kril Herd (KH) | Gandomi and Alavi (2012) |
| 296 | Lambda Algorithm (LA) | Cui et al. (2010) |
| 297 | Laying Chicken Algorithm (LCA) | Hosseini (2017) |
| 298 | Leaders and Followers Algorithm (LFA) | Gonzalez-Fernandez and Chen (2015) |
| 299 | League Championship Algorithm (LCA) | Kashan (2014) |
| 300 | Lévy Flight Distribution (LFD) | Houssein et al. (2020) |
| 301 | Light Ray Optimization (LRO) | Shen and Li (2010) |
| 302 | Lightning Attachment Procedure Optimization (LAPO) | Nematollahi et al. (2017) |
| 303 | Lightning Search Algorithm (LSA) | Shareef et al. (2015) |
| 304 | Linear Prediction Evolution Algorithm (LPE) | Gao et al. (2021a) |
| 305 | Lion Algorithm (LA) | Rajakumar (2012) |
| 306 | Lion Optimization Algorithm (LOA) | Yazdani and Jolai (2016) |
| 307 | Locust Search (LS) | Cuevas et al. (2015) |
| 308 | Locust Swarm Optimization (LSO) | Chen (2009) |
| 309 | Ludo Game-Based Swarm Intelligence Algorithm (LGSI) | Singh et al. (2019) |
| 310 | Magnetic Charged System Search (MCSS) | Kaveh et al. (2013) |
| 311 | Magnetic Optimization Algorithm (MFO) | Tayarani-N and Akbarzadeh-T (2008) |
| 312 | Magnetotactic Bacteria Optimization Algorithm (MBOA) | Mo and Xu (2013) |
| 313 | Marine Predator Algorithm (MPA) | Faramarzi et al. (2020) |
| 314 | Marriage in Honey Bees Optimization (MHBO) | Abbass (2001) |
| 315 | Material Generation Algorithm (MGA) | Talatahari et al. (2021a) |
| 316 | Mean Euclidian Distance Threshold (MEDT) | Kaveh et al. (2022) |
| 317 | Meerkats Inspired Algorithm (MIA) | Klein and dos Santos Coelho (2018) |
| 318 | Melody Search (MS) | Ashrafi and Dariane (2011) |
| 319 | Membrane Algorithm (MA) | Nishida (2006) |
| 320 | Memetic Algorithm (MA) | Moscato et al. (1989) |
| 321 | Method of Musical Composition (MMC) | Mora-Gutiérrez et al. (2014) |
| 322 | Migrating Birds Optimization (MBO) | Duman et al. (2012) |
| 323 | Mine Blast Algorithm (MBA) | Sadollah et al. (2013) |
| 324 | MOEA/D | Zhang and Li (2007) |
| 325 | Momentum Search Algorithm (MSA) | Dehghani and Samet (2020) |
| 326 | Monarch Butterfly Optimization (MBO) | Feng et al. (2017) |
| 327 | Monkey Search (MS) | Mucherino and Seref (2007) |
| 328 | Mosquito Flying Optimization (MFO) | Alauddin (2016) |
| 329 | Moth Flame Optimization Algorithm (MFO) | Mirjalili (2015b) |
| 330 | Moth Search Algorithm (MSA) | Wang (2018) |
| 331 | Mouth Breeding Fish Algorithm (MBF) | Jahani and Chizari (2018) |
| 332 | Mox Optimization Algorithm (MOX) | Arif et al. (2011) |
| 333 | Multi-Objective Beetle Antennae Search (MOBAS) | Zhang et al. (2021) |
| 334 | Multi-Objective Trader algorithm (MOTR) | Masoudi-Sobhanzadeh et al. (2021) |
| 335 | Multi-Particle Collision Algorithm (M-PCA) | da Luz et al. (2008) |
| 336 | Multivariable Grey Prediction Model Algorithm (MGPEA) | Xu et al. (2020) |
| 337 | Multi-Verse Optimizer (MVO) | Mirjalili et al. (2016) |
| 338 | Naked Moled Rat (NMR) | Salgotra and Singh (2019) |
| 339 | Namib Beetle Optimization (NBO) | Chahardoli et al. (2022) |
| 340 | Natural Aggregation Algorithm (NAA) | Luo et al. (2016) |
| 341 | Natural Forest Regeneration Algorithm (NFR) | Moez et al. (2016) |
| 342 | Neuronal Communication Algorithm (NCA) | A Gharebaghi and Ardalan A (2017) |
| 343 | New Caledonian Crow Learning Algorithm (NCCLA) | Al-Sorori and Mohsen (2020) |
| 344 | Newton Metaheuristic Algorithm (NMA) | Gholizadeh et al. (2020) |
| 345 | Nomadic People Optimizer (NPO) | Salih and Alsewari (2020) |
| 346 | Old Bachelor Acceptance (OBA) | Hu et al. (1995) |
| 347 | OptBees (OB) | Maia et al. (2013) |
| 348 | Optics Inspired Optimization (OIO) | Kashan (2015) |
| 349 | Optimal Foraging Algorithm (OFA) | Sayed et al. (2019a) |
| 350 | Optimal Stochastic Process Optimizer (OSPO) | Xu and Xu (2021) |
| 351 | Orca Optimization Algorithm (OOA) | Golilarz et al. (2020) |
| 352 | Orca Predation Algorithm (OPA) | Jiang et al. (2021) |
| 353 | Oriented Search Algorithm (OSA) | Zhang et al. (2008) |
| 354 | Paddy Field Algorithm (PFA) | Kong et al. (2012) |
| 355 | Parliamentary Optimization Algorithm (POA) | Borji and Hamidi (2009) |
| 356 | Particle Collision Algorithm (PCA) | Sacco et al. (2007) |
| 357 | Particle Swarm Optimization (PSO) | Eberhart and Kennedy (1995) |
| 358 | Passing Vehicle Search (PVS) | Savsani and Savsani (2016) |
| 359 | Pathfinder Algorithm (PFA) | Yapici and Cetinkaya (2019) |
| 360 | Pearl Hunting Algorithm (PHA) | Chan et al. (2012) |
| 361 | Pelican Optimization Algorithm (POA) | Trojovský and Dehghani (2022b) |
| 362 | Penguins Search Optimization Algorithm (PeSOA) | Gheraibia and Moussaoui (2013) |
| 363 | Photon Search Algorithm (PSA) | Liu and Li (2020) |
| 364 | Photosyntetic Algorithm (PA) | Murase (2000) |
| 365 | Pigeon Inspired Optimization (PIO) | Duan and Qiao (2014) |
| 366 | Pity Beetle Algorithm (PBA) | Kallioras et al. (2018) |
| 367 | Plant Competition Optimization (PCO) | Rahmani and AliAbdi (2022) |
| 368 | Plant Growth Optimization (PGO) | Cai et al. (2008) |
| 369 | Plant Propagation Algorithm (PPA) | Sulaiman et al. (2014) |
| 370 | Plant Self-Defense Mechanism Algorithm (PSDM) | Caraveo et al. (2018) |
| 371 | Plasma Generation Optimization (PGO) | Kaveh et al. (2020a) |
| 372 | Political Optimizer (PO) | Askari et al. (2020) |
| 373 | Poplar Optimization Algorithm (POA) | Chen et al. (2022) |
| 374 | POPMUSIC | Taillard and Voss (2002) |
| 375 | Population Migration Algorithm (PMA) | ZongXXSlahUndXXyuan (2003) |
| 376 | Prairie Dog Optimization (PDO) | Ezugwu et al. (2022) |
| 377 | Predator–Prey Optimization (PPO) | Narang et al. (2014) |
| 378 | Prey Predator Algorithm (PPA) | Tilahun and Ong (2015) |
| 379 | Projectiles Optimization (PRO) | Kahrizi and Kabudian (2020) |
| 380 | Quantum-Inspired Bacterial Swarming Optimization (QBSO) | Cao and Gao (2012) |
| 381 | Queen-Bees Evolution (QBE) | Jung (2003) |
| 382 | Queuing Search Algorithm (QSA) | Zhang et al. (2018) |
| 383 | Raccoon Optimization Algorithm (ROA) | Koohi et al. (2018) |
| 384 | Radial Movement Optimization (RMO) | Rahmani and Yusof (2014) |
| 385 | Rain Optimization Algorithm (ROA) | Moazzeni and Khamehchi (2020) |
| 386 | Rain Water Algorithm (RWA) | Biyanto et al. (2019) |
| 387 | Rain-Fall Optimization (RFO) | Kaboli et al. (2017) |
| 388 | Raven Roosting Optimization Algorithm (RRO) | Brabazon et al. (2016) |
| 389 | Ray Optimization (RO) | Kaveh and Khayatazad (2012) |
| 390 | Red Deer Algorithm (RDA) | Fard and Hajiaghaei k (2016) |
| 391 | Reincarnation Algorithm (RA) | Sharma (2010) |
| 392 | Remora Optimization Algorithm (ROA) | Jia et al. (2021) |
| 393 | Reptile Search Algorithm (RSA) | Abualigah et al. (2021a) |
| 394 | Rhino Herd Behavior (RHB) | Wang et al. (2018b) |
| 395 | Ring Toss Game-Based Optimization Algorithm (RTGBO) | Doumari et al. (2021) |
| 396 | Ringed Seal Search (RSS) | Saadi et al. (2016) |
| 397 | River Formation Dynamics (RFD) | Rabanal et al. (2007) |
| 398 | Roach Infestation Optimization (RIO) | Havens et al. (2008) |
| 399 | Root Growth Optimizer (RGO) | He et al. (2015) |
| 400 | Root Tree Optimization Algorithm (RTO) | Labbi et al. (2016) |
| 401 | RUNge Kutta optimizer (RUN) | Ahmadianfar et al. (2021) |
| 402 | Runner Root Algorithm (RRA) | Merrikh-Bayat (2015) |
| 403 | SailFish Optimizer (SFO) | Shadravan et al. (2019) |
| 404 | Salp Swarm Algorithm (SSA) | Mirjalili et al. (2017) |
| 405 | SaMW | Tychalas and Karatza (2021) |
| 406 | Saplings Growing Up Algorithm (SGUA) | Karci (2007) |
| 407 | Satin Bowerbird Optimizer (SBO) | Moosavi and Bardsiri (2017) |
| 408 | Scatter Search Algorithm (SS) | Glover (1977) |
| 409 | Scientific Algorithm (SA) | Felipe et al. (2014) |
| 410 | Search Group Algorithm (SGA) | Gonçalves et al. (2015) |
| 411 | Search in Forest Optimizer (SFO) | Ahwazian et al. (2022) |
| 412 | Seed based Plant Propagation Algorithm (SPPA) | Sulaiman and Salhi (2015) |
| 413 | Seeker Optimization Algorithm (SOA) | Dai et al. (2006) |
| 414 | See-See Partidge Chicks Optimization (SSPCO) | Omidvar et al. (2015) |
| 415 | Self-Organizing Migrating Algorithm (SOMA) | Zelinka (2004) |
| 416 | Self-Driven Particles (SDP) | Vicsek et al. (1995) |
| 417 | Seven-spot Labybird Optimization (SLO) | Wang et al. (2013) |
| 418 | Shark Search Algorithm (SSA) | Hersovici et al. (1998) |
| 419 | Shark Smell Algorithm (SSA) | Abedinia et al. (2016) |
| 420 | Sheep Flock Heredity Model (SFHM) | Nara et al. (1999) |
| 421 | Sheep Flock Optimization Algorithm (SFOA) | Kivi and Majidnezhad (2022) |
| 422 | Shufed Complex Evolution (SCE) | Duan et al. (1993) |
| 423 | Shuffled Frog Leaping Algorithm (SFLA) | Eusuff et al. (2006) |
| 424 | Shuffled Shepherd Optimization Algorithm (SSOA) | Kaveh and Zaerreza (2020) |
| 425 | Simple Optimization (SO) | Hasançebi and K Azad (2012) |
| 426 | Simulated Annealing (SA) | Kirkpatrick et al. (1983) |
| 427 | Simulated Bee Colony (SBC) | McCaffrey (2009) |
| 428 | Sine Cosine Algorithm (SCA) | Mirjalili (2016b) |
| 429 | Skip Salp Swam Algorithm (SSSA) | Arunekumar and Joseph (2022) |
| 430 | Slime Mold Optimization Algorithm (SMOA) | Monismith and Mayfield (2008) |
| 431 | Small World Optimization (SWO) | Du et al. (2006) |
| 432 | Smart Flower Optimization Algorithm (SFOA) | Sattar and Salim (2021) |
| 433 | Snake Optimizer (SO) | Hashim and Hussien (2022) |
| 434 | Snap-Drift Cuckoo Search (SDCS) | Rakhshani and Rahati (2017) |
| 435 | Soccer Game Optimization (SGO) | Purnomo (2014) |
| 436 | Soccer League Competition (SLC) | Moosavian and Roodsari (2014) |
| 437 | Social Cognitive Optimization (SCO) | Xie et al. (2002) |
| 438 | Social Cognitive Optimization Algorithm (SCOA) | Wei et al. (2010) |
| 439 | Social Emotional Optimization Algorithm (SEOA) | Xu et al. (2010) |
| 440 | Social Spider Algorithm (SSA) | James and Li (2015) |
| 441 | Social Spider Optimization (SSO) | Cuevas et al. (2013) |
| 442 | Society and Civilization Algorithm (SCA) | Ray and Liew (2003) |
| 443 | Sonar Inspired Optimization (SIO) | Tzanetos and Dounias (2017) |
| 444 | Space Gravitational Algorithm (SGA) | Hsiao et al. (2005) |
| 445 | Special Relativity Search (SRS) | Goodarzimehr et al. (2022) |
| 446 | Sperm Motility Algorithm (SMA) | Raouf and Hezam (2017) |
| 447 | Sperm Swarm Optimization Algorithm (SSO) | Shehadeh et al. (2018) |
| 448 | Sperm Whale Algorithm (SWA) | Ebrahimi and Khamehchi (2016) |
| 449 | Spherical Search Algorithm (SSA) | Misra et al. (2020) |
| 450 | Spherical Search Optimizer (SSO) | Zhao et al. (2020a) |
| 451 | Spider Monkey Optimization (SMO) | Bansal et al. (2014) |
| 452 | Spiral Dynamics Optimization (SDO) | Tamura and Yasuda (2011) |
| 453 | Spiral Optimization Algorithm (SOA) | Jin and Tran (2010) |
| 454 | Spotted Hyena Optimizer (SHO) | Dhiman and Kumar (2017) |
| 455 | Spring Search Algorithm (SSA) | Dehghani et al. (2017) |
| 456 | Spy Algorithm (SA) | Pambudi and Kawamura (2022) |
| 457 | Squirrel Search Algorithm (SSA) | Jain et al. (2019) |
| 458 | Star Graph Algorithm (SGA) | Gharebaghi et al. (2017) |
| 459 | Starling Murmuration Optimizer (SMO) | Zamani et al. (2022) |
| 460 | States Matter Optimization Algorithm (SMOA) | Cuevas et al. (2014) |
| 461 | Stem Cells Algorithm (SCA) | Taherdangkoo et al. (2011) |
| 462 | Stochastic Difusion Search (SDS) | Al-Rifaie and Bishop (2013) |
| 463 | Stochastic Focusing Search (SFS) | Weibo et al. (2008) |
| 464 | Stochastic Fractal Search (SFS) | Salimi (2015) |
| 465 | Stochastic Search Network (SSN) | Bishop (1989) |
| 466 | Strawberry Algorithm (SA) | Merrikh-Bayat (2014) |
| 467 | String Theory Algorithm (STA) | Rodriguez et al. (2021) |
| 468 | Student Psychology Based Optimization (SPBO) | Das et al. (2020) |
| 469 | Success History Intelligent Optimizer (SHIO) | Fakhouri et al. (2021) |
| 470 | Sunflower Optimization (SFO) | Gomes et al. (2019) |
| 471 | Superbug Algorithm (SA) | Anandaraman et al. (2012) |
| 472 | Supernova Optimizer (SO) | Hudaib and Fakhouri (2018) |
| 473 | Surface Simplex Swarm Evolution Algorithm (SSSE) | Quan and Shi (2017) |
| 474 | Swallow Swarm Optimizer (SWO) | Neshat et al. (2013) |
| 475 | Swarm Inspired Projection Algorithm (SIP) | Su et al. (2009) |
| 476 | Swine Influenza Models Based Optimization (SIMBO) | Pattnaik et al. (2013) |
| 477 | Symbiosis Organisms Search (SOS) | Cheng and Prayogo (2014) |
| 478 | Synergistic Fibroblast Optimization (SFO) | Subashini et al. (2017) |
| 479 | Tabu Search (TS) | Glover (1989) |
| 480 | Tangent Search Algorithm (TSA) | Layeb (2021) |
| 481 | Tasmanian Devil Optimization (TDO) | Dehghani et al. (2022a) |
| 482 | Teaching-Learning Based Optimization Algorithm (TLBO) | Rao et al. (2011) |
| 483 | Team Game Algorithm (TGA) | Mahmoodabadi et al. (2018) |
| 484 | Termite Colony Optimizer (TCO) | Hedayatzadeh et al. (2010) |
| 485 | Termite Life Cycle Optimizer (TLCO) | Minh et al. (2022) |
| 486 | Termite-hill Algorithm (ThA) | Zungeru et al. (2012) |
| 487 | The Great Salmon Run (TGSR) | Mozaffari et al. (2013) |
| 488 | Thermal Exchange Optimization (TEO) | Kaveh and Dadras (2017) |
| 489 | Tiki-Taka Algorithm (TTA) | Rashid (2020) |
| 490 | Transient Search Optimization Algorithm (TSO) | Qais et al. (2020) |
| 491 | Tree Growth Algorithm (TGA) | Cheraghalipour et al. (2018) |
| 492 | Tree Physiology Optimization (TPO) | Halim and Ismail (2018) |
| 493 | Tree Seed Algorithm (TSA) | Kiran (2015) |
| 494 | Trees Social Relations Optimization Algorithm (TSR) | Alimoradi et al. (2022) |
| 495 | Triple Distinct Search Dynamics (TDSD) | Li et al. (2020) |
| 496 | Tug of War Optimization (TWO) | Kaveh and Zolghadr (2016) |
| 497 | Tuna Swarm Optimization (TSO) | Xie et al. (2021) |
| 498 | Tunicate Swarm Algorithm (TSA) | Kaur et al. (2020) |
| 499 | Unconscious Search (US) | Ardjmand and Amin-Naseri (2012) |
| 500 | Vapor Liquid Equilibrium Algorithm (VLEA) | Taramasco et al. (2020) |
| 501 | Variable Mesh Optimization (VMO) | Puris et al. (2012) |
| 502 | Variable Neighborhood Descent Algorithm (VND) | Hertz and Mittaz (2001) |
| 503 | Vibrating Particles System (VPS) | Kaveh and Ghazaan (2017) |
| 504 | Virtual Ants Algorithm (VAA) | Yang et al. (2006) |
| 505 | Viral Systems Optimization (VS) | Cortés et al. (2008) |
| 506 | Virtual Bees Algorithm (VBA) | Yang (2005) |
| 507 | Virulence Optimization Algorithm (VOA) | Jaderyan and Khotanlou (2016) |
| 508 | Virus Colony Search (VCS) | Li et al. (2016c) |
| 509 | Virus Optimization Algorithm (VOA) | Juarez et al. (2009) |
| 510 | Virus Spread Optimization (VSO) | Li and Tam (2020) |
| 511 | Volcano Eruption Algorithm (VCA) | Hosseini et al. (2021) |
| 512 | Volleyball Premier League Algorithm (VPL) | Moghdani and Salimifard (2018) |
| 513 | Vortex Search Algorithm (VS) | Doğan and Ölmez (2015) |
| 514 | War Strategy Optimization (WSO) | Ayyarao et al. (2022) |
| 515 | Wasp Swarm Optimization (WSO) | Pinto et al. (2005) |
| 516 | Water Cycle Algorithm (WCA) | Eskandar et al. (2012) |
| 517 | Water Evaporation Algorithm (WEA) | Saha et al. (2017) |
| 518 | Water Evaporation Optimization (WEO) | Kaveh and Bakhshpoori (2016) |
| 519 | Water Flow Algorithm (WFA) | Basu et al. (2007) |
| 520 | Water Flow-Like Algorithm (WFA) | Yang and Wang (2007) |
| 521 | Water Optimization Algorithm (WAO) | Daliri et al. (2022) |
| 522 | Water Strider Algorithm (WSA) | Kaveh and Eslamlou (2020) |
| 523 | Water Wave Optimization (WWO) | Zheng (2015) |
| 524 | Water Wave Optimization.1 (WWO.1) | Kaur and Kumar (2021) |
| 525 | Water-Flow Algorithm Optimization (WFO) | Tran and Ng (2011) |
| 526 | Weed Colonization Optimization (WCO) | Mehrabian and Lucas (2006) |
| 527 | Weightless Swarm Algorithm (WSA) | Ting et al. (2012) |
| 528 | Whale Optimization Algorithm (WOA) | Mirjalili and Lewis (2016) |
| 529 | White Shark Optimizer (WSO) | Braik et al. (2022a) |
| 530 | Wind Driven Optimization (WDO) | Bayraktar et al. (2010) |
| 531 | Wingsuit Flying Search (WFS) | Covic and Lacevic (2020) |
| 532 | Wisdom of Artificial Crowds (WoAC) | Yampolskiy and El-Barkouky (2011) |
| 533 | Wolf Colony Algorithm (WCA) | Liu et al. (2011) |
| 534 | Wolf Pack Search (WPS) | Yang et al. (2007) |
| 535 | Wolf Search Algorithm (WSA) | Tang et al. (2012) |
| 536 | Woodpecker Mating Algorithm (WMA) | Karimzadeh Parizi et al. (2020) |
| 537 | Worm Optimization (WO) | Arnaout (2014) |
| 538 | Xerus Optimization Algorithm (XOA) | Samie Yousefi et al. (2019) |
| 539 | Yin-Yang-Pair Optimization (YYPO) | Punnathanam and Kotecha (2016) |
| 540 | Zombie Survival Optimization (ZSO) | Nguyen and Bhanu (2012) |

---

# Table 3: Summary of applications of most popular MAs with their source of inspiration and number of parameters

---

### 1. Particle Swarm Optimization (PSO)

* **Source of Inspiration:** Bird swarm behaviour
* **Parameters:** 5
* **Updating Equations / Operators:**
  $$X_i(t + 1) = X_i(t) + V_i(t + 1)$$
  $$V_i(t + 1) = V_i(t) + c_1 \cdot R_1 \cdot (P_i - X_i(t)) + c_2 \cdot R_2 \cdot (G - X_i(t))$$
  *Where:*
  * $P_i$: personal best
  * $G$: global best
  * $c_1$: cognitive coefficient, $0 \le c_1 \le 4$
  * $c_2$: social coefficient, $0 \le c_2 \le 4$
  * $R_1, R_2$: uniform random number in $(0, 1)$
* **Function Evaluations:** Population size ($N$) + $N \times$ number of iterations ($T$)
* **Applications:**
  * **Healthcare**
    * (i) Intelligence diagnosis
    * (ii) Disease detection and classification
    * (iii) Medical image segmentation
  * **Environmental**
    * (i) Agriculture monitoring
    * (ii) Flood control and routing
    * (iii) Pollutant concentration monitoring
  * **Industrial**
    * (i) Economic dispatch problem
    * (ii) Phasor measurement unit placement
  * **Commercial**
    * (i) Risk assessment
    * (ii) Predicting cost and price
  * **Smart city**
    * (i) Smart home
    * (ii) Traffic monitoring and scheduling *(Gad 2022)*

---

### 2. Genetic Algorithm (GA)

* **Source of Inspiration:** Darwin’s theory of evolution
* **Parameters:** 3
* **Updating Equations / Operators:**
  * Selection Operator
  * Crossover Operator
  * Mutation Operator
* **Function Evaluations:** $N + N \times T$
* **Applications:**
  * **Operation management**
    * (i) Facility layout and Scheduling
    * (ii) Inventory control
    * (iii) Forecasting and network design
  * **Multimedia**
    * (i) Information security
    * (ii) Image processing
    * (iii) Video processing and Gaming
  * **Wireless networking**
    * (i) Load balancing
    * (ii) Localization
    * (iii) Bandwidth and channel allocation *(Katoch et al. 2021)*

---

### 3. Ant Colony Optimization (ACO)

* **Source of Inspiration:** The foraging behaviour of ant colonies
* **Parameters:** 5
* **Updating Equations / Operators:**
  * Pheromones updation:
    $$\tau_{ij}^{new} = (1 - \rho) \cdot \tau_{ij}^{old} + \sum_{k} \Delta \tau_{ij}^{k}$$
    *Where:*
    * $\rho$: evaporation rate
    * $\Delta \tau_{ij}^{k}$: pheromone amount laid by $k^{\text{th}}$ ant
* **Function Evaluations:** Basic ACO was developed for TSP. The best path is chosen based on the density of pheromone. Pheromone is calculated for every path in each iteration.
* **Applications:**
  * **Transportation:**
    * (i) Traveling salesman problem
    * (ii) Vehicle routing search
  * **Set problems:**
    * (i) Set partitioning and covering
    * (ii) Maximum independent set
    * (iii) Bin packing
  * **Scheduling:**
    * (i) Job shop scheduling
    * (ii) Flow shop scheduling
  * **Bio-informatics:**
    * (i) Protein folding
    * (ii) DNA sequencing *(Dorigo and Stützle 2019)*

---

### 4. Differential Evolution Algorithm (DE)

* **Source of Inspiration:** Darwin’s theory of evolution
* **Parameters:** 2
* **Updating Equations / Operators:**
  * Mutation operator
  * Crossover operator
  * Selection operator
* **Function Evaluations:** $N + N \times T$
* **Applications:**
  * **Electrical and power systems:**
    * (i) Economic dispatch
    * (ii) Power system stabilizer
    * (iii) Optimal power flow
  * **Robotics and Expert Systems:**
    * (i) Space trajectory optimization
    * (ii) Satellite orbit reconfiguration
    * (iii) Guidance of unmanned vehicles
  * **Artificial Neural Networks:**
    * (i) Optimal network topology
    * (ii) Neural network training
    * (iii) Non-linear system identification
  * **Operation Research:**
    * (i) Transport in docking systems
    * (ii) Manufacturing optimization
    * (iii) Scheduling *(Das et al. 2016)*

---

### 5. Simulated Annealing (SA)

* **Source of Inspiration:** Annealing process in metallurgy
* **Parameters:** 2
* **Updating Equations / Operators:**
  * Generate a new point $x(k)$ randomly in a neighborhood of the current point
* **Function Evaluations:** $1 + T$
* **Applications:**
  * **Telecommunication:**
    * (i) Mobile network design
    * (ii) Routing
    * (iii) Channel allocation
  * **Chemical industry:**
    * (i) Antenna array synthesis
    * (ii) Refinery model problem
  * **Operational:**
    * (i) Facility layout problems
    * (ii) Flexible Manufacturing system *(Suman and Kumar 2006; Delahaye et al. 2019)*

---

### 6. Tabu Search (TA)

* **Source of Inspiration:** Social tabu
* **Parameters:** 2
* **Updating Equations / Operators:**
  * Moves
* **Function Evaluations:** $1 + \text{number of created neighbors in each iteration} \times T$
* **Applications:**
  * **Transportation:**
    * (i) Travelling salesman problem
    * (ii) Vehicle routing Problem
    * (iii) Quadratic assignment problem
  * **Neural network:**
    * (i) Multi-layer network
    * (ii) Training
  * **Others:**
    * (i) Economic dispatch problems
    * (ii) Telecommunication
    * (iii) Clustering *(Skorin-Kapov 1990; Amuthan and Thilak 2016)*

---

### 7. Grey Wolf Optimizer (GWO)

* **Source of Inspiration:** Leadership hierarchy and hunting mechanism of grey wolves
* **Parameters:** 2
* **Updating Equations / Operators:**
  $$\vec{X}(t + 1) = \vec{X}_p(t) - \vec{A} \cdot \vec{D}$$
  *Where:*
  $$\vec{D} = |\vec{C} \cdot \vec{X}_p(t) - \vec{X}(t)|$$
  $$\vec{A} = 2\vec{a} \cdot \vec{r}_1 - \vec{a}$$
  $$\vec{C} = 2 \cdot \vec{r}_2$$
  * $\vec{A}$ and $\vec{C}$ are coefficient vectors
  * $\vec{X}_p$: position vector of the prey
  * $\vec{X}$: position vector of a grey wolf
  * $r_1, r_2 \in U[0, 1]$
* **Function Evaluations:** $N + N \times T$
* **Applications:**
  * **Medical and Bio-informatics:**
    * (i) Parkinson’s disease diagnosis
    * (ii) Breast cancer diagnosis
  * **Environmental applications:**
    * (i) Water pollution assessment
    * (ii) Thermal pollution assessment
  * **Machine learning:**
    * (i) Feature selection
    * (ii) Training neural networks
    * (iii) Clustering applications
  * **Engineering applications:**
    * (i) Design and tuning controllers
    * (ii) Power dispatch problems
    * (iii) Robotics and path planning
  * **Image processing:**
    * (i) Multi-level image threshold problem
    * (ii) Template matching problems
    * (iii) Hyper-spectral image classification *(Faris et al. 2018)*

---

### 8. Artificial Bee Colony (ABC)

* **Source of Inspiration:** The foraging behavior of honey bees when seeking a quality food source.
* **Parameters:** 1
* **Updating Equations / Operators:**
  $$v_{ij} = x_{ij} + \phi_{ij}(x_{ij} - x_{kj})$$
  *Where:*
  * $x_k$: randomly selected food source
  * $i$: randomly chosen parameter index
  * $\phi_{ij}$: random number within the range $[-1, 1]$
* **Function Evaluations:** $N + [2N + \text{number of scout bees}] \times T$
* **Applications:**
  * **Neural networks:**
    * (i) Signal processing applications
    * (ii) Machine learning
  * **Electrical engineering:**
    * (i) Distribution system
    * (ii) Accident diagnosis in nuclear plant
    * (iii) Radial distribution system
  * **Civil engineering:**
    * (i) Grinding parameter optimization
    * (ii) Heat exchangers
    * (iii) Truss structures
  * **Data mining:**
    * (i) Fuzzy clustering
    * (ii) Chilli expert advisory system
  * **Software engineering:**
    * (i) Automated maintenance of software
    * (ii) Software test suite optimization *(Karaboga et al. 2014)*

---

### 9. Cuckoo Search (CS)

* **Source of Inspiration:** The brood parasitism of some cuckoo species
* **Parameters:** 1
* **Updating Equations / Operators:**
  $$x_i^{t+1} = x_i^t + \alpha \oplus \text{Lévy}(\lambda)$$
  *Where:*
  * $\alpha$: Step size
  * $\lambda$: Levy exponent
  * $\oplus$: Entry wise multiplication
* **Function Evaluations:** $N + 2NT$
* **Applications:**
  * **Medical applications:**
    * (i) Medical image segmentation
    * (ii) Disease detection and classification
  * **Image processing:**
    * (i) Image segmentation
    * (ii) Enhancement
    * (iii) Clustering
  * **Engineering applications:**
    * (i) Economic dispatch problem
    * (ii) Design and tuning controllers *(Shehab et al. 2017; Agrawal et al. 2013)*

---

### 10. Harmony Search (HS)

* **Source of Inspiration:** Musical performance process
* **Parameters:** 3
* **Updating Equations / Operators:**
  $$x_{ij} = x_{ij} + r_1 \times BW$$
  $$x_{ij} = l_{ij} + r_2 \times (u_{ij} - l_{ij})$$
  *Where:*
  * $BW$: band width
  * $r_1, r_2$: uniform random number in $(0, 1)$
  * $u_{ij}$: upper bound of $x_{ij}$
  * $l_{ij}$: lower bound of $x_{ij}$
* **Function Evaluations:** $N + N \times T$
* **Applications:**
  * **Industrial application:**
    * (i) Logistics
    * (ii) Tour planning
    * (iii) Self driving car
  * **Computer science:**
    * (i) Web page and document clustering
    * (ii) Internet routing
    * (iii) Robotics
  * **Electrical engineering:**
    * (i) Energy system dispatch
    * (ii) Power system design
    * (iii) Photo electronic detection
  * **Medical Studies:**
    * (i) RNA structure prediction
    * (ii) Medical image
    * (iii) Forecasting influenza season *(Ala’a et al. 2019)*

----
Here is the unified markdown table transcribing all the references from the provided review paper on metaheuristic algorithms:

| Authors | Year | Title | Journal / Source & Details |
| :--- | :--- | :--- | :--- |
| Abdollahzadeh B, Gharehchopogh FS, Mirjalili S | 2021 | African vultures optimization algorithm: A new nature-inspired metaheuristic algorithm for global optimization problems | *Computers & Industrial Engineering*, 158(107):408 |
| Abdollahzadeh B, Soleimanian Gharehchopogh F, Mirjalili S | 2021 | Artificial gorilla troops optimizer: A new nature-inspired metaheuristic algorithm for global optimization problems | *Int J Intell Syst*, 36(10):5887–5958 |
| Abdulhameed S, Rashid TA | 2022 | Child drawing development optimization algorithm based on child’s cognitive development | *Arab J Sci Eng*, 47(2):1337–1351 |
| Abdullah JM, Ahmed T | 2019 | Fitness dependent optimizer: inspired by the bee swarming reproductive process | *IEEE Access*, 7:43,473–43,486 |
| Abedinia O, Amjady N, Ghasemi A | 2016 | A new metaheuristic algorithm based on shark smell optimization | *Complexity*, 21(5):97–116 |
| Abedinpourshotorban H, Shamsuddin SM, Beheshti Z et al | 2016 | Electromagnetic field optimization: A physics-inspired metaheuristic optimization algorithm | *Swarm Evol Comput*, 26:8–22 |
| Abualigah L, Diabat A, Mirjalili S et al | 2021 | The arithmetic optimization algorithm | *Comput Methods Appl Mech Eng*, 376(113):609 |
| Abualigah L, Abd Elaziz M, Sumari P, et al | 2021a | Reptile search algorithm (rsa): A nature-inspired metaheuristic optimizer | *Expert Systems with Applications*, p. 116158 |
| Adham MT, Bentley PJ | 2014 | An artificial ecosystem algorithm applied to static and dynamic travelling salesman problems | *2014 IEEE International Conference on Evolvable Systems*, pp. 149–156, doi:10.1109/ICES.2014.7008734 |
| Afroughinia A, Kardehi MR | 2018 | Competitive learning: a new meta-heuristic optimization algorithm | *Int J Artif Intell Tools*, 27(08):1850,035 |
| Agrawal S, Panda R, Bhuyan S et al | 2013 | Tsallis entropy based optimal multilevel thresholding using cuckoo search algorithm | *Swarm Evol Comput*, 11:16–30 |
| Ahmadianfar I, Bozorg-Haddad O, Chu X | 2020 | Gradient-based optimizer: A new metaheuristic optimization algorithm | *Inf Sci*, 540:131–159 |
| Ahmadianfar I, Heidari AA, Gandomi AH et al | 2021 | Run beyond the metaphor: an efficient optimization algorithm based on runge kutta method | *Expert Syst Appl*, 181(115):079 |
| Ahmadi-Javid A | 2011 | Anarchic society optimization: A human-inspired method | *2011 IEEE Congress of Evolutionary Computation*, pp. 2586–2592, doi:10.1109/CEC.2011.5949940 |
| Ahrari A, Atai AA | 2010 | Grenade explosion method-a novel tool for optimization of multimodal functions | *Appl Soft Comput*, 10(4):1132–1140 |
| Ahwazian A, Amindoust A, Tavakkoli-Moghaddam R et al | 2022 | Search in forest optimizer: a bioinspired metaheuristic algorithm for global optimization problems | *Soft Comput*, 26(5):2325–2356 |
| Akay B, Karaboga D | 2009 | Parameter tuning for the artificial bee colony algorithm | *International Conference on Computational Collective Intelligence*, Springer, pp. 608–619 |
| Akbari R, Mohammadi A, Ziarati K | 2010 | A novel bee swarm optimization algorithm for numerical function optimization | *Commun Nonlinear Sci Numer Simul*, 15(10):3142–3155 |
| Akbari MA, Zare M, Azizipanah-Abarghooee R et al | 2022 | The cheetah optimizer: A nature-inspired metaheuristic algorithm for large-scale optimization problems | *Sci Rep*, 12(1):1–20 |
| Akhmedova S, Semenkin E | 2013 | Co-operation of biology related algorithms | *2013 IEEE Congress on Evolutionary Computation*, IEEE, pp. 2207–2214 |
| Ala’a A, Alsewari AA, Alamri HS et al | 2019 | Comprehensive review of the development of the harmony search algorithm and its applications | *IEEE Access*, 7:14,233–14,245 |
| Alatas B | 2011 | Acroa: artificial chemical reaction optimization algorithm for global optimization | *Expert Syst Appl*, 38(10):13,170–13,180 |
| Alauddin M | 2016 | Mosquito flying optimization (mfo) | *2016 International Conference on Electrical, Electronics, and Optimization Techniques (ICEEOT)*, IEEE, pp. 79–84 |
| Alazzam A, Lewis HW | 2013 | A new optimization algorithm for combinatorial problems | *International Journal of Advanced Research in Artificial Intelligence*, 2(5) |
| Alba E | 2005 | Parallel metaheuristics: a new class of algorithms | Vol. 47. Wiley, Hoboken |
| Alba E, Talbi E, Luque G, et al | 2005 | Metaheuristics and parallelism | *Parallel Metaheuristics: A New Class of Algorithms*, Wiley, pp. 79–104 |
| Al-Betar MA, Alyasseri ZAA, Awadallah MA et al | 2021 | Coronavirus herd immunity optimizer (chio) | *Neural Comput Appl*, 33(10):5011–5042 |
| Alimoradi M, Azgomi H, Asghari A | 2022 | Trees social relations optimization algorithm: A new swarm-based metaheuristic technique to solve continuous and discrete optimization problems | *Math Comput Simul*, 194:629–664 |
| Alippi C, Polycarpou MM, Panayiotou C, et al | 2009 | Artificial Neural Networks–ICANN 2009: 19th International Conference, Limassol, Cyprus, September 14-17, 2009, Proceedings, Part II | Vol. 5769. Springer |
| Ali J, Saeed M, Luqman M, et al | 2015 | Artificial showering algorithm: a new meta-heuristic for unconstrained optimization | DSpace |
| Almonacid B, Soto R | 2019 | Andean condor algorithm for cell formation problems | *Nat Comput*, 18(2):351–381 |
| Al-Obaidi ATS, Abdullah HS, et al | 2017 | Camel herds algorithm: A new swarm intelligent algorithm to solve optimization problems | *International Journal on Perceptive and Cognitive Computing*, 3(1) |
| Al-Rifaie MM, Bishop JM | 2013 | Stochastic diffusion search review | *Paladyn, Journal of Behavioral Robotics*, 4(3):155–173 |
| Alsattar H, Zaidan A, Zaidan B | 2020 | Novel meta-heuristic bald eagle search optimisation algorithm | *Artif Intell Rev*, 53(3):2237–2264 |
| Al-Sorori W, Mohsen AM | 2020 | New caledonian crow learning algorithm: A new metaheuristic algorithm for solving continuous optimization problems | *Appl Soft Comput*, 92(106):325 |
| Altan A | 2020 | Performance of metaheuristic optimization algorithms based on swarm intelligence in attitude and altitude control of unmanned aerial vehicle for path following | *2020 4th International Symposium on Multidisciplinary Studies and Innovative Technologies*, IEEE, pp. 1–6 |
| Amuthan A, Thilak KD | 2016 | Survey on tabu search meta-heuristic optimization | *2016 International Conference on Signal Processing, Communication, Power and Embedded System*, IEEE, pp. 1539–1543 |
| Anandaraman C, Sankar AVM, Natarajan R | 2012 | A new evolutionary algorithm based on bacterial evolution and its application for scheduling a flexible manufacturing system | *Jurnal Teknik Industri*, 14(1):1–12 |
| Aranha C, Camacho Villalón CL, Campelo F, et al | 2021 | Metaphor-based metaheuristics, a call for action: the elephant in the room | *Swarm Intelligence*, pp. 1–6 |
| Archana N, Vidhyapriya R, Benedict A et al | 2017 | Deterministic oscillatory search: a new meta-heuristic optimization algorithm | *Sādhanā*, 42(6):817–826 |
| Ardjmand E, Amin-Naseri MR | 2012 | Unconscious search-a new structured search algorithm for solving continuous engineering optimization problems based on the theory of psychoanalysis | *International Conference in Swarm Intelligence*, Springer, pp. 233–242 |
| Arif M et al | 2011 | Mox: A novel global optimization algorithm inspired from oviposition site selection and egg hatching inhibition in mosquitoes | *Appl Soft Comput*, 11(8):4614–4625 |
| Arnaout JP | 2014 | Worm optimization: A novel optimization algorithm inspired by c. elegans | *Proceedings of the 2014 International Conference on Industrial engineering and operations management*, Indonesia, pp. 2499–2505 |
| Arora S, Singh S | 2019 | Butterfly optimization algorithm: a novel approach for global optimization | *Soft Comput*, 23(3):715–734 |
| Arshaghi A, Ashourian M, Ghabeli L | 2019 | Buzzard optimization algorithm: A nature-inspired metaheuristic algorithm | *Majlesi Journal of Electrical Engineering*, 13(3):83–98 |
| Arunekumar N, Joseph KS | 2022 | Skip salp swam algorithm for feature selection | *Information and Communication Technology for Competitive Strategies (ICTCS 2020)*, Springer, p. 231–240 |
| Asef F, Majidnezhad V, Feizi-Derakhshi MR, et al | 2021 | Heat transfer relation-based optimization algorithm (htoa) | *Soft Computing*, pp. 1–30 |
| Ashrafi S, Dariane A | 2011 | A novel and effective algorithm for numerical optimization: melody search (ms) | *2011 11th International Conference on Hybrid Intelligent Systems (HIS)*, IEEE, pp. 109–114 |
| Askari Q, Younas I, Saeed M | 2020 | Political optimizer: A novel socio-inspired meta-heuristic for global optimization | *Knowledge-Based Systems*, p. 105709 |
| Askarzadeh A | 2014 | Bird mating optimizer: an optimization algorithm inspired by bird mating strategies | *Commun Nonlinear Sci Numer Simul*, 19(4):1213–1228 |
| Askarzadeh A | 2016 | A novel metaheuristic method for solving constrained engineering optimization problems: crow search algorithm | *Computers & Structures*, 169:1–12 |
| Atashpaz-Gargari E, Lucas C | 2007 | Imperialist competitive algorithm: an algorithm for optimization inspired by imperialistic competition | *2007 IEEE Congress on Evolutionary Computation*, IEEE, pp. 4661–4667 |
| Ayyarao TS, RamaKrishna N, Elavarasan RM et al | 2022 | War strategy optimization algorithm: a new effective metaheuristic algorithm for global optimization | *IEEE Access*, 10:25,073–25,105 |
| Azizi M | 2021 | Atomic orbital search: A novel metaheuristic algorithm | *Appl Math Model*, 93:657–683 |
| Azizi M, Talatahari S, Gandomi AH | 2022 | Fire hawk optimizer: A novel metaheuristic algorithm | *Artificial Intelligence Review*, pp. 1–77 |
| Bansal JC, Sharma H, Jadon SS et al | 2014 | Spider monkey optimization algorithm for numerical optimization | *Memetic Computing*, 6(1):31–47 |
| Barzegar B, Rahmani AM, Zamanifar K, et al | 2009 | Gravitational emulation local search algorithm for advanced reservation and scheduling in grid computing systems | *2009 Fourth International Conference on Computer Sciences and Convergence Information Technology*, IEEE, pp. 1240–1245 |
| Bastos Filho CJ, de Lima Neto FB, Lins AJ, et al | 2008 | A novel search algorithm based on fish school behavior | *2008 IEEE International Conference on Systems, Man and Cybernetics*, IEEE, pp. 2646–2651 |
| Basu S, Chaudhuri C, Kundu M et al | 2007 | Text line extraction from multi-skewed handwritten documents | *Pattern Recogn*, 40(6):1825–1839 |
| Baum KG, Schmidt E, Rafferty K et al | 2011 | Evaluation of novel genetic algorithm generated schemes for positron emission tomography (pet)/magnetic resonance imaging (mri) image fusion | *J Digit Imaging*, 24(6):1031–1043 |
| Bayraktar Z, Komurcu M, Werner DH | 2010 | Wind driven optimization (wdo): A novel nature-inspired optimization algorithm and its application to electromagnetics | *2010 IEEE Antennas and Propagation Society International Symposium*, IEEE, pp. 1–4 |
| Bellaachia A, Bari A | 2012 | Flock by leader: a novel machine learning biologically inspired clustering algorithm | *International Conference in Swarm Intelligence*, Springer, pp. 117–126 |
| Beni G, Wang J | 1993 | Swarm intelligence in cellular robotic systems | *Robots and biological systems: towards a new bionics?*, Springer, p. 703–712 |
| Beyer HG, Schwefel HP | 2002 | Evolution strategies-a comprehensive introduction | *Nat Comput*, 1(1):3–52 |
| Birbil ŞI, Fang SC | 2003 | An electromagnetism-like mechanism for global optimization | *J Global Optim*, 25(3):263–282 |
| Bishop J | 1989 | Stochastic searching networks | *1989 First IEE International Conference on Artificial Neural Networks*, (Conf. Publ. No. 313), IET, pp. 329–331 |
| Bishop J, Torr P | 1992 | The stochastic search network | *Neural networks for vision, speech and natural language*, Springer, p. 370–387 |
| Bitam S, Zeadally S, Mellouk A | 2018 | Fog computing job scheduling optimization based on bees swarm | *Enterprise Information Systems*, 12(4):373–397 |
| Biyanto TR, Fibrianto HY, Nugroho G, et al | 2016 | Duelist algorithm: an algorithm inspired by how duelist improve their capabilities in a duel | *International Conference in Swarm Intelligence*, Springer, pp. 39–47 |
| Biyanto TR, Matradji, Febrianto HY, et al | 2019 | Rain water algorithm: Newton’s law of rain water movements during free fall and uniformly accelerated motion utilization | *AIP Conference Proceedings*, AIP Publishing LLC, p. 020053 |
| Biyanto TR, Irawan S, Febrianto HY et al | 2017 | Killer whale algorithm: an algorithm inspired by the life of killer whale | *Procedia Computer Science*, 124:151–157 |
| Bodaghi M, Samieefar K | 2019 | Meta-heuristic bus transportation algorithm | *Iran Journal of Computer Science*, 2(1):23–32 |
| Boettcher S, Percus AG | 1999 | Extremal optimization: Methods derived from co-evolution | arXiv preprint arXiv:math/9904056 |
| Borji A, Hamidi M | 2009 | A new approach to global optimization motivated by parliamentary political competitions | *International Journal of Innovative Computing, Information and Control*, 5(6):1643–1653 |
| Brabazon A, Cui W, O’Neill M | 2016 | The raven roosting optimisation algorithm | *Soft Comput*, 20(2):525–545 |
| Braik M, Sheta A, Al-Hiary H | 2021 | A novel meta-heuristic search algorithm for solving optimization problems: capuchin search algorithm | *Neural Comput Appl*, 33(7):2515–2547 |
| Braik M, Hammouri A, Atwan J et al | 2022 | White shark optimizer: A novel bio-inspired meta-heuristic algorithm for global optimization problems | *Knowl-Based Syst*, 243(108):457 |
| Braik M, Ryalat MH, Al-Zoubi H | 2022 | A novel meta-heuristic algorithm for solving numerical optimization problems: Ali baba and the forty thieves | *Neural Comput Appl*, 34(1):409–455 |
| Brammya G, Praveena S, Ninu Preetha N, et al | 2019 | Deer hunting optimization algorithm: a new nature-inspired meta-heuristic paradigm | *The Computer Journal* |
| Burgin GH, Fogel LJ | 1972 | Air-to-air combat tactics synthesis and analysis program based on an adaptive maneuvering logic | *Journal of Cybernetics* |
| Cai W, Yang W, Chen X | 2008 | A global optimization algorithm based on plant growth theory: plant growth optimization | *2008 International Conference on Intelligent Computation Technology and Automation*, IEEE, pp. 1194–1199 |
| Camacho-Villalón CL, Dorigo M, Stützle T | 2018 | Why the intelligent water drops cannot be considered as a novel algorithm | *International Conference on Swarm Intelligence*, Springer, pp. 302–314 |
| Canayaz M, Karcı A | 2015 | Investigation of cricket behaviours as evolutionary computation for system design optimization problems | *Measurement*, 68:225–235 |
| Canayaz M, Karci A | 2016 | Cricket behaviour-based evolutionary computation technique in solving engineering optimization problems | *Appl Intell*, 44(2):362–376 |
| Cao J, Gao H | 2012 | A quantum-inspired bacterial swarming optimization algorithm for discrete optimization problems | *International Conference in Swarm Intelligence*, Springer, pp. 29–36 |
| Caraveo C, Valdez F, Castillo O | 2018 | A new optimization meta-heuristic algorithm based on self-defense mechanism of the plants with three reproduction operators | *Soft Comput*, 22(15):4907–4920 |
| Castiglione F, Poccia F, D’Offizi G et al | 2004 | Mutation, fitness, viral diversity, and predictive markers of disease progression in a computational model of hiv type 1 infection | *AIDS Research & Human Retroviruses*, 20(12):1314–1323 |
| Catalbas MC, Gulten A | 2018 | Circular structures of puffer fish: A new metaheuristic optimization algorithm | *2018 Third International Conference on Electrical and Biomedical Engineering, Clean Energy and Green Computing*, IEEE, pp. 1–5 |
| Chahardoli M, Eraghi NO, Nazari S | 2022 | Namib beetle optimization algorithm: a new meta-heuristic method for feature selection and dimension reduction | *Concurrency and Computation: Practice and Experience*, 34(1):e6524 |
| Chan CY, Xue F, Ip W, et al | 2012 | A hyper-heuristic inspired by pearl hunting | *International Conference on Learning and Intelligent Optimization*, Springer, pp. 349–353 |
| Chen CC, Tsai YC, Liu I, et al | 2015 | A novel metaheuristic: Jaguar algorithm with learning behavior | *2015 IEEE International Conference on Systems, Man, and Cybernetics*, IEEE, pp. 1595–1600 |
| Chen S | 2009 | An analysis of locust swarms on large scale global optimization problems | *Australian Conference on Artificial Life*, Springer, pp. 211–220 |
| Chen TC, Tsai PW, Chu SC, et al | 2007 | A novel optimization approach: bacterial-ga foraging | *Second International Conference on Innovative Computing, Information and Control (ICICIC 2007)*, IEEE, pp. 391–391 |
| Chen T, Wang Y, Li J | 2012 | Artificial tribe algorithm and its performance analysis | *Journal of Software*, 7(3):651–656 |
| Chen J, Cai H, Wang W | 2018 | A new metaheuristic algorithm: car tracking optimization algorithm | *Soft Comput*, 22(12):3857–3878 |
| Chen D, Ge Y, Wan Y et al | 2022 | Poplar optimization algorithm: A new meta-heuristic optimization technique for numerical optimization and image segmentation | *Expert Syst Appl*, 200(117):118 |
| Cheng MY, Prayogo D | 2014 | Symbiotic organisms search: a new metaheuristic optimization algorithm | *Computers & Structures*, 139:98–112 |
| Cheng L, Wu X, Wang Y | 2018 | Artificial flora (af) optimization algorithm | *Appl Sci*, 8(3):329 |
| Chen T, Pang L, Du J, et al | 2009 | Artificial searching swarm algorithm for solving constrained optimization problems | *2009 IEEE International Conference on Intelligent Computing and Intelligent Systems*, IEEE, pp. 562–565 |
| Chen H, Zhu Y, Hu K, et al | 2010 | Hierarchical swarm model: a new approach to optimization | *Discrete Dynamics in Nature and Society*, 2010 |
| Cheraghalipour A, Hajiaghaei-Keshteli M, Paydar MM | 2018 | Tree growth algorithm (tga): A novel approach for solving optimization problems | *Eng Appl Artif Intell*, 72:393–414 |
| Chong HY, Yap HJ, Tan SC et al | 2021 | Advances of metaheuristic algorithms in training neural networks for industrial applications | *Soft Comput*, 25(16):11,209–11,233 |
| Chopra N, Ansari MM | 2022 | Golden jackal optimization: A novel nature-inspired optimizer for engineering applications | *Expert Syst Appl*, 198(116):924 |
| Chou JS, Nguyen NM | 2020 | Fbi inspired meta-optimization | *Appl Soft Comput*, 93(106):339 |
| Chou JS, Truong DN | 2021 | A novel metaheuristic optimizer inspired by behavior of jellyfish in ocean | *Appl Math Comput*, 389(125):535 |
| Chouhan SS, Kaul A, Singh UP | 2018 | Soft computing approaches for image segmentation: a survey | *Multimedia Tools and Applications*, 77(21):28,483–28,537 |
| Chu SC, Tsai PW, Pan JS | 2006 | Cat swarm optimization | *Pacific Rim International Conference on Artificial Intelligence*, Springer, pp. 854–858 |
| Chuang CL, Jiang JA | 2007 | Integrated radiation optimization: inspired by the gravitational radiation in the curvature of space-time | *2007 IEEE Congress on Evolutionary Computation*, IEEE, pp. 3157–3164 |
| Chuang LY, Tsai SW, Yang CH | 2008 | Catfish particle swarm optimization | *2008 IEEE Swarm Intelligence Symposium*, IEEE, pp. 1–5 |
| Chu Y, Mi H, Liao H, et al | 2008 | A fast bacterial swarming algorithm for high-dimensional function optimization | *2008 IEEE Congress on Evolutionary Computation*, IEEE, pp. 3135–3140 |
| Civicioglu P | 2012 | Transforming geocentric cartesian coordinates to geodetic coordinates by using differential search algorithm | *Computers & Geosciences*, 46:229–247 |
| Civicioglu P | 2013 | Artificial cooperative search algorithm for numerical optimization problems | *Inf Sci*, 229:58–76 |
| Civicioglu P | 2013 | Backtracking search optimization algorithm for numerical optimization problems | *Appl Math Comput*, 219(15):8121–8144 |
| Cortés P, García JM, Onieva L, et al | 2008 | Viral system to solve optimization problems: An immune-inspired computational intelligence approach | *International Conference on Artificial Immune Systems*, Springer, pp. 83–94 |
| Covic N, Lacevic B | 2020 | Wingsuit flying search-a novel global optimization algorithm | *IEEE Access*, 8:53,883–53,900, doi:10.1109/ACCESS.2020.2981196 |
| Črepinšek M, Liu SH, Mernik M | 2013 | Exploration and exploitation in evolutionary algorithms: A survey | *ACM Comput Surv*, 45(3):1–33 |
| Cuevas E, Oliva D, Zaldivar D et al | 2012 | Circle detection using electro-magnetism optimization | *Inf Sci*, 182(1):40–55 |
| Cuevas E, Cienfuegos M, Zaldívar D et al | 2013 | A swarm optimization algorithm inspired in the behavior of the social-spider | *Expert Syst Appl*, 40(16):6374–6384 |
| Cuevas E, Echavarría A, Ramírez-Ortegón MA | 2014 | An optimization algorithm inspired by the states of matter that improves the balance between exploration and exploitation | *Appl Intell*, 40(2):256–272 |
| Cuevas E, González A, Zaldívar D et al | 2015 | An optimisation algorithm based on the behaviour of locust swarms | *International Journal of Bio-Inspired Computation*, 7(6):402–407 |
| Cuevas E, Gonzalez M, Zaldivar D, et al | 2012a | An algorithm for global optimization inspired by collective animal behavior | *Discrete Dynamics in Nature and Society*, 2012 |
| Cui X, Gao J, Potok TE | 2006 | A flocking based algorithm for document clustering analysis | *J Syst Architect*, 52(8–9):505–515 |
| Cui Y, Guo R, Guo D | 2010 | Lambda algorithm | *Journal of Uncertain Systems*, 4(1):22–33 |
| Cui Z, Cai X | 2011 | A new stochastic algorithm to solve lennard-jones clusters | *2011 International Conference of Soft Computing and Pattern Recognition*, IEEE, pp. 528–532 |
| Cui Y, Guo R, Rao R, et al | 2008 | Harmony element algorithm: A naive initial searching range | *International Conference on Advances in Mechanical Engineering*, pp. 1–6 |
| da Luz EFP, Becceneri JC, de Campos Velho HF | 2008 | A new multi-particle collision algorithm for optimization in a high performance environment | *Journal of Computational Interdisciplinary Sciences*, 1(1):3–10 |
| Dai C, Zhu Y, Chen W | 2006 | Seeker optimization algorithm | *International Conference on Computational and Information Science*, Springer, pp. 167–176 |
| Daliri A, Asghari A, Azgomi H, et al | 2022 | The water optimization algorithm: a novel metaheuristic for solving optimization problems | *Applied Intelligence*, pp. 1–40 |
| Dandy GC, Simpson AR, Murphy LJ | 1996 | An improved genetic algorithm for pipe network optimization | *Water Resour Res*, 32(2):449–458 |
| Das AK, Pratihar DK | 2019 | A new bonobo optimizer (bo) for real-parameter optimization | *2019 IEEE Region 10 Symposium (TENSYMP)*, IEEE, pp. 108–113 |
| Das S, Mullick SS, Suganthan PN | 2016 | Recent advances in differential evolution-an updated survey | *Swarm Evol Comput*, 27:1–30 |
| Das B, Mukherjee V, Das D | 2020 | Student psychology based optimization algorithm: a new population based optimization algorithm for solving optimization problems | *Adv Eng Softw*, 146(102):804 |
| Das S, Biswas A, Dasgupta S, et al | 2009 | Bacterial foraging optimization algorithm: theoretical foundations, analysis, and applications | *Foundations of computational intelligence volume 3*, Springer, pp. 23–55 |
| Daskin A, Kais S | 2011 | Group leaders optimization algorithm | *Mol Phys*, 109(5):761–772 |
| de Carvalho Filho AO, de Sampaio WB, Silva AC et al | 2014 | Automatic detection of solitary lung nodules using quality threshold clustering, genetic algorithm and diversity index | *Artif Intell Med*, 60(3):165–177 |
| De Castro LN, Von Zuben FJ | 2000 | The clonal selection algorithm with engineering applications | *Proceedings of GECCO*, pp. 36–39 |
| De Melo VV | 2014 | Kaizen programming | *Proceedings of the 2014 Annual Conference on Genetic and Evolutionary Computation*, pp. 895–902 |
| de Oliveira DR, Lopes HS, Parpinelli RS | 2011 | Bioluminescent swarm optimization algorithm | INTECH Open Access Publisher |
| Deb K, Jain H | 2013 | An evolutionary many-objective optimization algorithm using reference-point based nondominated sorting approach, part i: solving problems with box constraints | *IEEE Trans Evol Comput*, 18(4):577–601 |
| Deb K, Pratap A, Agarwal S et al | 2002 | A fast and elitist multiobjective genetic algorithm: Nsga-ii | *IEEE Trans Evol Comput*, 6(2):182–197 |
| Deb S, Fong S, Tian Z | 2015 | Elephant search algorithm for optimization problems | *2015 Tenth International Conference on Digital Information Management*, IEEE, pp. 2499–255 |
| Dehghani M, Samet H | 2020 | Momentum search algorithm: A new meta-heuristic optimization algorithm inspired by momentum conservation law | *SN Applied Sciences*, 2(10):1–15 |
| Dehghani M, Montazeri Z, Hubálovský Š | 2021 | Gmbo: Group mean-based optimizer for solving various optimization problems | *Mathematics*, 9(11):1190 |
| Dehghani M, Hubálovský Š, Trojovský P | 2022 | Tasmanian devil optimization: a new bio-inspired optimization algorithm for solving optimization algorithm | *IEEE Access*, 10:19,599–19,620 |
| Dehghani M, Trojovská E, Trojovský P | 2022 | A new human-based metaheuristic algorithm for solving optimization problems on the base of simulation of driving training process | *Sci Rep*, 12(1):1–21 |
| Dehghani M, Montazeri Z, Dehghani A, et al | 2017 | Spring search algorithm: A new meta-heuristic optimization algorithm inspired by hooke’s law | *2017 IEEE 4th International Conference on Knowledge Based Engineering and Innovation*, IEEE, pp. 0210–0214 |
| Del Ser J, Osaba E, Molina D et al | 2019 | Bio-inspired computation: Where we stand and what’s next | *Swarm Evol Comput*, 48:220–250 |
| Del Acebo E, de-la Rosa JL | 2008 | Introducing bar systems: a class of swarm intelligence optimization algorithms | *AISB 2008 Convention Communication, Interaction and Social Intelligence*, p. 18 |
| Delahaye D, Chaimatanan S, Mongeau M | 2019 | Simulated annealing: From basics to applications | *Handbook of metaheuristics*, Springer, pp. 1–35 |
| Deuri J, Sathya SS | 2018 | Cricket chirping algorithm: an efficient meta-heuristic for numerical function optimisation | *Int J Comput Sci Eng*, 16(2):162–172 |
| Dhal KG, Ray S, Das A et al | 2019 | A survey on nature-inspired optimization algorithms and their application in image enhancement domain | *Archives of Computational Methods in Engineering*, 26(5):1607–1638 |
| Dhiman G, Kumar V | 2017 | Spotted hyena optimizer: a novel bio-inspired based metaheuristic technique for engineering applications | *Adv Eng Softw*, 114:48–70 |
| Dhiman G, Kumar V | 2018 | Emperor penguin optimizer: A bio-inspired algorithm for engineering problems | *Knowl-Based Syst*, 159:20–50 |
| Djemame S, Batouche M, Oulhadj H et al | 2019 | Solving reverse emergence with quantum pso application to image processing | *Soft Comput*, 23(16):6921–6935 |
| Doğan B, Ölmez T | 2015 | A new metaheuristic for numerical function optimization: Vortex search algorithm | *Inf Sci*, 293:125–145 |
| Dong R, Wang S | 2020 | New optimization algorithm inspired by kernel tricks for the economic emission dispatch problem with valve point | *IEEE Access*, 8:16,584–16,594 |
| Dorigo M, Birattari M, Stutzle T | 2006 | Ant colony optimization | *IEEE Comput Intell Mag*, 1(4):28–39 |
| Dorigo M, Stützle T | 2019 | Ant colony optimization: overview and recent advances | *Handbook of metaheuristics*, pp. 311–351 |
| Doumari SA, Givi H, Dehghani M et al | 2021 | Ring toss game-based optimization algorithm for solving various optimization problems | *Int J Intell Eng Syst*, 14:545–554 |
| Duan H, Qiao P | 2014 | Pigeon-inspired optimization: a new swarm intelligence optimizer for air robot path planning | *International Journal of Intelligent Computing and Cybernetics*, 7(1):24–37 |
| Duan Q, Gupta VK, Sorooshian S | 1993 | Shuffled complex evolution approach for effective and efficient global minimization | *J Optim Theory Appl*, 76(3):501–521 |
| Dueck G | 1993 | New optimization heuristics: The great deluge algorithm and the record-to-record travel | *J Comput Phys*, 104(1):86–92 |
| Duman E, Uysal M, Alkaya AF | 2012 | Migrating birds optimization: A new metaheuristic approach and its performance on quadratic assignment problem | *Inf Sci*, 217:65–77 |
| Du H, Wu X, Zhuang J | 2006 | Small-world optimization algorithm for function optimization | *International Conference on Natural Computation*, Springer, pp. 264–273 |
| Eberhart R, Kennedy J | 1995 | A new optimizer using particle swarm theory | *MHS’95. Proceedings of the Sixth International Symposium on Micro Machine and Human Science*, IEEE, pp. 39–43 |
| Ebrahimi A, Khamehchi E | 2016 | Sperm whale algorithm: An effective metaheuristic algorithm for production optimization problems | *Journal of Natural Gas Science and Engineering*, 29:211–222 |
| Eesa AS, Brifcani AMA, Orman Z | 2013 | Cuttlefish algorithm-a novel bio-inspired optimization algorithm | *International Journal of Scientific & Engineering Research*, 4(9):1978–1986 |
| Ehsaeyan E, Zolghadrasli A | 2022 | Foa: fireworks optimization algorithm | *Multimedia Tools and Applications*, pp. 1–20 |
| Eita M, Fahmy M | 2014 | Group counseling optimization | *Appl Soft Comput*, 22:585–604 |
| El-Dosuky M, El-Bassiouny A, Hamza T, et al | 2012 | New hoopoe heuristic optimization | arXiv preprint arXiv:1211.6410 |
| Erol OK, Eksin I | 2006 | A new optimization method: big bang-big crunch | *Adv Eng Softw*, 37(2):106–111 |
| Eskandar H, Sadollah A, Bahreininejad A et al | 2012 | Water cycle algorithm-a novel metaheuristic optimization method for solving constrained engineering optimization problems | *Computers & Structures*, 110:151–166 |
| Eslami N, Yazdani S, Mirzaei M et al | 2022 | Aphid-ant mutualism: A novel nature-inspired metaheuristic algorithm for solving optimization problems | *Math Comput Simul*, 201:362–395 |
| Etminaniesfahani A, Ghanbarzadeh A, Marashi Z | 2018 | Fibonacci indicator algorithm: A novel tool for complex optimization problems | *Eng Appl Artif Intell*, 74:1–9 |
| Eusuff M, Lansey K, Pasha F | 2006 | Shuffled frog-leaping algorithm: a memetic meta-heuristic for discrete optimization | *Eng Optim*, 38(2):129–154 |
| Ezugwu AE, Agushaka JO, Abualigah L, et al | 2022 | Prairie dog optimization algorithm | *Neural Computing and Applications*, pp. 1–49 |
| Ezugwu AE, Shukla AK, Nath R, et al | 2021 | Metaheuristics: a comprehensive overview and classification along with bibliometric analysis | *Artificial Intelligence Review*, pp. 1–80 |
| Fadakar E, Ebrahimi M | 2016 | A new metaheuristic football game inspired algorithm | *2016 1st Conference on Swarm Intelligence and Evolutionary Computation (CSIEC)*, IEEE, pp. 6–11 |
| Fakhouri HN, Hamad F, Alawamrah A | 2021 | Success history intelligent optimizer | *The Journal of Supercomputing*, pp. 1–42 |
| Faramarzi A, Heidarinejad M, Mirjalili S et al | 2020 | Marine predators algorithm: A nature-inspired metaheuristic | *Expert Syst Appl*, 152(113):377 |
| Farasat A, Menhaj MB, Mansouri T et al | 2010 | Aro: A new model-free optimization algorithm inspired from asexual reproduction | *Appl Soft Comput*, 10(4):1284–1292 |
| Fard AF, Hajiaghaei-Keshteli M | 2016 | Red deer algorithm (rda); a new optimization algorithm inspired by red deer’s mating | *International Conference on Industrial Engineering*, IEEE, pp. 33–34 |
| Faris H, Aljarah I, Al-Betar MA et al | 2018 | Grey wolf optimizer: a review of recent variants and applications | *Neural Comput Appl*, 30(2):413–435 |
| Felipe D, Goldbarg EFG, Goldbarg MC | 2014 | Scientific algorithms for the car renter salesman problem | *2014 IEEE Congress on Evolutionary Computation*, IEEE, pp. 873–879 |
| Feng X, Ma M, Yu H | 2016 | Crystal energy optimization algorithm | *Comput Intell*, 32(2):284–322 |
| Feng Y, Wang GG, Deb S et al | 2017 | Solving 0–1 knapsack problem by a novel binary monarch butterfly optimization | *Neural Comput Appl*, 28(7):1619–1634 |
| Ferreira C | 2002 | Gene expression programming in problem solving | *Soft Computing and Industry*, Springer, pp. 635–653 |
| Findik O | 2015 | Bull optimization algorithm based on genetic operators for continuous optimization problems | *Turkish Journal of Electrical Engineering & Computer Sciences*, 23 |
| Fister Jr I, Yang XS, Fister I, et al | 2013 | A brief review of nature-inspired algorithms for optimization | arXiv preprint arXiv:1307.4186 |
| Flores JJ, López R, Barrera J | 2011 | Gravitational interactions optimization | *International Conference on Learning and Intelligent Optimization*, Springer, pp. 226–237 |
| Fogel LJ, McCulloch W, Ramsey-Klee D | 1970 | Natural automata and prosthetic devices | *Aids to Biological Communication: Prothesis and Synthesis*, 2:221–262 |
| Fong S, Deb S, Chaudhary A | 2015 | A review of metaheuristics in robotics | *Computers & Electrical Engineering*, 43:278–291 |
| Formato RA | 2008 | Central force optimization: a new nature inspired computational framework for multidimensional search and optimization | *Nature Inspired Cooperative Strategies for Optimization (NICSO 2007)*, Springer, pp. 221–238 |
| Gad AG | 2022 | Particle swarm optimization algorithm and its applications: A systematic review | *Archives of Computational Methods in Engineering*, 29:1–31 |
| Gandomi AH | 2014 | Interior search algorithm (isa): a novel approach for global optimization | *ISA Trans*, 53(4):1168–1183 |
| Gandomi AH, Alavi AH | 2012 | Krill herd: a new bio-inspired optimization algorithm | *Commun Nonlinear Sci Numer Simul*, 17(12):4831–4845 |
| Gao C, Hu Z, Tong W | 2021 | Linear prediction evolution algorithm: a simplest evolutionary optimizer | *Memetic Computing*, 13(3):319–339 |
| Gao ZM, Zhao J, Hu YR et al | 2021 | The challenge for the nature-inspired global optimization algorithms: Non-symmetric benchmark functions | *IEEE Access*, 9:106,317–106,339 |
| Gao-Wei Y, Zhanju H | 2012 | A novel atmosphere clouds model optimization algorithm | *2012 International Conference on Computing, Measurement, Control and Sensor Network*, IEEE, pp. 217–220 |
| Ghaemi M, Feizi-Derakhshi MR | 2014 | Forest optimization algorithm | *Expert Syst Appl*, 41(15):6676–6687 |
| Ghafil HN, Jármai K | 2020 | Dynamic differential annealed optimization: New metaheuristic optimization algorithm for engineering applications | *Appl Soft Comput*, 93(106):392 |
| Ghafil HN, Alsamia S, Jármai K | 2022 | Fertilization optimization algorithm on cec2015 and large scale problems | *Pollack Periodica*, 17(1):24–29 |
| Gharebaghi SA, Kaveh A, Ardalan Asl M | 2017 | A new meta-heuristic optimization algorithm using star graph | *Smart Struct Syst*, 20(1):99–114 |
| Gharebaghi S, Ardalan AM | 2017 | New meta-heuristic optimization algorithm using neuronal communication | *Iran University of Science & Technology*, 7(3):413–431 |
| Ghasemi M, Akbari MA, Jun C et al | 2022 | Circulatory system based optimization (csbo): An expert multilevel biologically inspired meta-heuristic algorithm | *Engineering Applications of Computational Fluid Mechanics*, 16(1):1483–1525 |
| Ghasemi-Marzbali A | 2020 | A novel nature-inspired meta-heuristic algorithm for optimization: bear smell search algorithm | *Soft Comput*, 24(17):13,003–13,035 |
| Gheraibia Y, Moussaoui A | 2013 | Penguins search optimization algorithm (pesoa) | *International Conference on Industrial, Engineering and Other Applications of Applied Intelligent Systems*, Springer, pp. 222–231 |
| Gholizadeh S, Danesh M, Gheyratmand C | 2020 | A new newton metaheuristic algorithm for discrete performance-based design optimization of steel moment frames | *Computers & Structures*, 234(106):250 |
| Ghorbani N, Babaei E, Sadikoglu F | 2017 | Exchange market algorithm for multi-objective economic emission dispatch and reliability | *Procedia Computer Science*, 120:633–640 |
| Glover F | 1977 | Heuristics for integer programming using surrogate constraints | *Decis Sci*, 8(1):156–166 |
| Glover F | 1989 | Tabu search-part i | *ORSA J Comput*, 1(3):190–206 |
| Goel U, Varshney S, Jain A et al | 2018 | Three dimensional path planning for uavs in dynamic environment using glow-worm swarm optimization | *Procedia Computer Science*, 133:230–239 |
| Golilarz NA, Gao H, Addeh A, et al | 2020 | Orca optimization algorithm: a new meta-heuristic tool for complex optimization problems | *2020 17th International Computer Conference on Wavelet Active Media Technology and Information Processing*, IEEE, pp. 198–204 |
| Gomes GF, da Cunha SS, Ancelotti AC | 2019 | A sunflower optimization (sfo) algorithm applied to damage identification on laminated composite plates | *Engineering with Computers*, 35(2):619–626 |
| Gonçalves MS, Lopez RH, Miguel LFF | 2015 | Search group algorithm: a new metaheuristic method for the optimization of truss structures | *Computers & Structures*, 153:165–184 |
| Gonzalez-Fernandez Y, Chen S | 2015 | Leaders and followers-a new metaheuristic to avoid the bias of accumulated information | *2015 IEEE Congress on Evolutionary Computation*, IEEE, pp. 776–783 |
| Goodarzimehr V, Shojaee S, Hamzehei-Javaran S et al | 2022 | Special relativity search: A novel metaheuristic method based on special relativity physics | *Knowl-Based Syst*, 257(109):484 |
| Goudhaman M | 2018 | Cheetah chase algorithm (cca): a nature-inspired metaheuristic algorithm | *International Journal of Engineering & Technology*, 7(3):1804–1811 |
| Greensmith J, Aickelin U, Cayzer S | 2005 | Introducing dendritic cells as a novel immune-inspired algorithm for anomaly detection | *International Conference on Artificial Immune Systems*, Springer, pp. 153–167 |
| Gupta S, Deep K | 2019 | A novel random walk grey wolf optimizer | *Swarm Evol Comput*, 44:101–112 |
| Gupta A, Ong YS, Feng L | 2015 | Multifactorial evolution: toward evolutionary multitasking | *IEEE Trans Evol Comput*, 20(3):343–357 |
| Gutin G, Punnen AP | 2006 | The traveling salesman problem and its variations | Vol. 12. Springer, New York |
| Häckel S, Dippold P | 2009 | The bee colony-inspired algorithm (bcia) a two-stage approach for solving the vehicle routing problem with time windows | *Proceedings of the 11th Annual Conference on Genetic and Evolutionary Computation*, pp. 25–32 |
| Haddad OB, Afshar A, Marino MA | 2006 | Honey-bees mating optimization (hbmo) algorithm: a new heuristic approach for water resources optimization | *Water Resour Manage*, 20(5):661–680 |
| Hajiaghaei-Keshteli M, Aminnayeri M | 2014 | Solving the integrated scheduling of production and rail transportation problem by keshtel algorithm | *Appl Soft Comput*, 25:184–203 |
| Halim AH, Ismail I | 2018 | Tree physiology optimization in constrained optimization problem | *Telkomnika*, 16(2):876–882 |
| Hansen N, Müller SD, Koumoutsakos P | 2003 | Reducing the time complexity of the derandomized evolution strategy with covariance matrix adaptation (cma-es) | *Evol Comput*, 11(1):1–18 |
| Harifi S, Khalilian M, Mohammadzadeh J et al | 2019 | Emperor penguins colony: a new metaheuristic algorithm for optimization | *Evol Intell*, 12(2):211–226 |
| Harifi S, Mohammadzadeh J, Khalilian M, et al | 2020 | Giza pyramids construction: an ancient-inspired metaheuristic algorithm for optimization | *Evol Intell*, pp. 1–19 |
| Hasançebi O, Azad SK | 2012 | An efficient metaheuristic algorithm for engineering optimization: Sopt | *Int J Optim Civil Eng*, 2(4):479–487 |
| Hashim FA, Hussien AG | 2022 | Snake optimizer: a novel meta-heuristic optimization algorithm | *Knowl-Based Syst*, 242(108):320 |
| Hashim FA, Houssein EH, Mabrouk MS et al | 2019 | Henry gas solubility optimization: a novel physics-based algorithm | *Future Gener Comput Syst*, 101:646–667 |
| Hashim FA, Hussain K, Houssein EH et al | 2021 | Archimedes optimization algorithm: a new metaheuristic algorithm for solving optimization problems | *Appl Intell*, 51(3):1531–1551 |
| Hashim FA, Houssein EH, Hussain K et al | 2022 | Honey badger algorithm: New metaheuristic algorithm for solving optimization problems | *Math Comput Simul*, 192:84–110 |
| Hatamlou A | 2013 | Black hole: A new heuristic optimization approach for data clustering | *Inf Sci*, 222:175–184 |
| Hatamlou A | 2014 | Heart: a novel optimization algorithm for cluster analysis | *Progress in Artificial Intelligence*, 2(2–3):167–173 |
| Havens TC, Spain CJ, Salmon NG, et al | 2008 | Roach infestation optimization | *2008 IEEE Swarm Intelligence Symposium*, IEEE, pp. 1–7 |
| He S, Wu QH, Saunders J | 2009 | Group search optimizer: an optimization algorithm inspired by animal searching behavior | *IEEE Trans Evol Comput*, 13(5):973–990 |
| Hedayatzadeh R, Salmassi FA, Keshtgari M, et al | 2010 | Termite colony optimization: A novel approach for optimizing continuous problems | *2010 18th Iranian Conference on Electrical Engineering*, IEEE, pp. 553–558 |
| Hegazy AE, Makhlouf M, El-Tawel GS | 2020 | Improved salp swarm algorithm for feature selection | *J King Saud Univ-Comput Inf Sci*, 32(3):335–344 |
| Heidari AA, Mirjalili S, Faris H et al | 2019 | Harris hawks optimization: Algorithm and applications | *Futur Gener Comput Syst*, 97:849–872 |
| Hernández H, Blum C | 2012 | Distributed graph coloring: an approach based on the calling behavior of japanese tree frogs | *Swarm Intell*, 6(2):117–150 |
| Hersovici M, Jacovi M, Maarek YS et al | 1998 | The shark-search algorithm: an application: tailored web site mapping | *Computer Networks and ISDN Systems*, 30(1):317–326 |
| Hertz A, Mittaz M | 2001 | A variable neighborhood descent algorithm for the undirected capacitated arc routing problem | *Transp Sci*, 35(4):425–434 |
| He X, Zhang S, Wang J | 2015 | A novel algorithm inspired by plant root growth with self-similarity propagation | *2015 1st International Conference on Industrial Networks and Intelligent Systems*, IEEE, pp. 157–162 |
| Holland J | 1991 | Adaptation in natural and artificial systems, 1975 | MIT Press |
| Horn J, Goldberg DE | 1995 | Genetic algorithm difficulty and the modality of fitness landscapes | *Foundations of genetic algorithms*, Vol. 3. Elsevier, p. 243–269 |
| Hosseini E | 2017 | Laying chicken algorithm: A new meta-heuristic approach to solve continuous programming problems | *J Appl Math Comput*, 6(344):2 |
| Hosseini E, Sadiq AS, Ghafoor KZ et al | 2021 | Volcano eruption algorithm for solving optimization problems | *Neural Comput Appl*, 33(7):2321–2337 |
| Houssein EH, Saad MR, Hashim FA et al | 2020 | Lévy flight distribution: A new metaheuristic algorithm for solving engineering optimization problems | *Eng Appl Artif Intell*, 94(103):731 |
| Hsiao YT, Chuang CL, Jiang JA, et al | 2005 | A novel optimization algorithm: space gravitational optimization | *2005 IEEE International Conference on Systems, Man and Cybernetics*, IEEE, pp. 2323–2328 |
| Hsinchun C, Yi-Ming C, Ramsey M et al | 1998 | An intelligent personal spider (agent) for dynamic internet/intranet searching | *Decis Support Syst*, 23(1):41–58 |
| Hu TC, Kahng AB, Tsao CWA | 1995 | Old bachelor acceptance: A new class of non-monotone threshold accepting methods | *ORSA J Comput*, 7(4):417–425 |
| Huan TT, Kulkarni AJ, Kanesan J et al | 2017 | Ideology algorithm: a socio-inspired optimization methodology | *Neural Comput Appl*, 28(1):845–876 |
| Huang G | 2016 | Artificial infectious disease optimization: A seiqr epidemic dynamic model-based function optimization algorithm | *Swarm Evol Comput*, 27:31–67 |
| Hudaib AA, Fakhouri HN | 2018 | Supernova optimizer: a novel natural inspired meta-heuristic | *Mod Appl Sci*, 12(1):32–50 |
| Ibrahim MK, Ali RS | 2016 | Novel optimization algorithm inspired by camel traveling behavior | *Iraqi Journal for Electrical and Electronic Engineering*, 12(2):167–177 |
| Irizarry R | 2004 | Lares: an artificial chemical process approach for optimization | *Evol Comput*, 12(4):435–459 |
| Jaderyan M, Khotanlou H | 2016 | Virulence optimization algorithm | *Appl Soft Comput*, 43:596–618 |
| Jafari M, Salajegheh E, Salajegheh J | 2021 | Elephant clan optimization: A nature-inspired metaheuristic algorithm for the optimal design of structures | *Appl Soft Comput*, 113(107):892 |
| Jahangiri M, Hadianfard MA, Najafgholipour MA et al | 2020 | Interactive autodidactic school: A new metaheuristic optimization algorithm for solving mathematical and structural design optimization problems | *Computers & Structures*, 235(106):268 |
| Jahani E, Chizari M | 2018 | Tackling global optimization problems with a novel algorithm-mouth brooding fish algorithm | *Appl Soft Comput*, 62:987–1002 |
| Jain M, Singh V, Rani A | 2019 | A novel nature-inspired algorithm for optimization: Squirrel search algorithm | *Swarm Evol Comput*, 44:148–175 |
| James J, Li VO | 2015 | A social spider algorithm for global optimization | *Appl Soft Comput*, 30:614–627 |
| Jamil M, Yang XS | 2013 | A literature survey of benchmark functions for global optimisation problems | *International Journal of Mathematical Modelling and Numerical Optimisation*, 4(2):150–194 |
| Javidy B, Hatamlou A, Mirjalili S | 2015 | Ions motion algorithm for solving optimization problems | *Appl Soft Comput*, 32:72–79 |
| Jia H, Peng X, Lang C | 2021 | Remora optimization algorithm | *Expert Syst Appl*, 185(115):665 |
| Jiang BLW | 1998 | Optimizing complex functions by chaos search | *Cybernetics & Systems*, 29(4):409–419 |
| Jiang Y, Hu T, Huang C et al | 2007 | An improved particle swarm optimization algorithm | *Appl Math Comput*, 193(1):231–239 |
| Jiang Q, Wang L, Hei X, et al | 2014 | Optimal approximation of stable linear systems with a novel and efficient optimization algorithm | *2014 IEEE Congress on Evolutionary Computation*, IEEE, pp. 840–844 |
| Jiang Y, Wu Q, Zhu S, et al | 2021 | Orca predation algorithm: A novel bio-inspired algorithm for global optimization problems | *Expert Systems with Applications*, p. 116026 |
| Jin GG, Tran TD | 2010 | A nature-inspired evolutionary algorithm based on spiral movements | *Proceedings of SICE Annual Conference 2010*, IEEE, pp. 1643–1647 |
| Jin X, Reynolds RG | 1999 | Using knowledge-based evolutionary computation to solve nonlinear constraint optimization problems: a cultural algorithm approach | *2008 IEEE Congress on Evolutionary Computation*, IEEE, pp. 1672–1678 |
| Jozefowiez N, Semet F, Talbi EG | 2008 | Multi-objective vehicle routing problems | *Eur J Oper Res*, 189(2):293–309 |
| Juarez JRC, Wang HJ, Lai YC, et al | 2009 | Virus optimization algorithm (voa): A novel metaheuristic for solving continuous optimization problems | *Proceedings of the 2009 Asia Pacific Industrial Engineering and Management Systems Conference (APIEMS 2009)*, pp. 2166–2174 |
| Jung SH | 2003 | Queen-bee evolution for genetic algorithms | *Electron Lett*, 39(6):575–576 |
| Kaboli SHA, Selvaraj J, Rahim N | 2017 | Rain-fall optimization algorithm: A population based algorithm for solving constrained optimization problems | *Journal of Computational Science*, 19:31–42 |
| Kadioglu S, Sellmann M | 2009 | Dialectic search | *International Conference on Principles and Practice of Constraint Programming*, Springer, pp. 486–500 |
| Kaedi M | 2017 | Fractal-based algorithm: a new metaheuristic method for continuous optimization | *Int J Artif Intell*, 15(1):76–92 |
| Kahrizi M, Kabudian S | 2020 | Projectiles optimization: A novel metaheuristic algorithm for global optimization | *Int J Eng*, 33(10):1924–1938 |
| Kallioras NA, Lagaros ND, Avtzis DN | 2018 | Pity beetle algorithm-a new metaheuristic inspired by the behavior of bark beetles | *Adv Eng Softw*, 121:147–166 |
| Karaboga D, Basturk B | 2007 | A powerful and efficient algorithm for numerical function optimization: artificial bee colony (abc) algorithm | *J Global Optim*, 39(3):459–471 |
| Karaboga D, Gorkemli B, Ozturk C et al | 2014 | A comprehensive survey: artificial bee colony (abc) algorithm and applications | *Artif Intell Rev*, 42(1):21–57 |
| Karami H, Anaraki MV, Farzin S et al | 2021 | Flow direction algorithm (fda): A novel optimization approach for solving optimization problems | *Computers & Industrial Engineering*, 156(107):224 |
| Karci A | 2007 | Theory of saplings growing up algorithm | *International Conference on Adaptive and Natural Computing Algorithms*, Springer, pp. 450–460 |
| Karci A | 2018 | A (3)-artificial atom algorithm: A new meta-heuristic computational intelligence algorithm inspired by chemical processes | *Applied and Computational Mathematics*, 17(2) |
| Karimkashi S, Kishk AA | 2010 | Invasive weed optimization and its features in electromagnetics | *IEEE Trans Antennas Propag*, 58(4):1269–1278 |
| Karimzadeh Parizi M, Keynia F, Khatibi Bardsiri A | 2020 | Woodpecker mating algorithm (wma): a nature inspired algorithm for solving optimization problems | *International Journal of Nonlinear Analysis and Applications*, 11(1):137–157 |
| Karpenko A, Kuzmina I | 2021 | Meta-heuristic algorithm for the global optimization: Intelligent ice fishing algorithm | *Inventive Systems and Control*, Springer, p. 147–160 |
| Kashan AH | 2014 | League championship algorithm (lca): An algorithm for global optimization inspired by sport championships | *Appl Soft Comput*, 16:171–200 |
| Kashan AH | 2015 | A new metaheuristic for optimization: optics inspired optimization (oio) | *Computers & Operations Research*, 55:99–125 |
| Kashan AH, Tavakkoli-Moghaddam R, Gen M | 2019 | Find-fix-finish-exploit-analyze (f3ea) meta-heuristic algorithm: An effective algorithm with new evolutionary operators for global optimization | *Computers & Industrial Engineering*, 128:192–218 |
| Katoch S, Chauhan SS, Kumar V | 2021 | A review on genetic algorithm: past, present, and future | *Multimedia Tools and Applications*, 80(5):8091–8126 |
| Kaur S, Awasthi LK, Sangal A et al | 2020 | Tunicate swarm algorithm: A new bio-inspired based metaheuristic paradigm for global optimization | *Eng Appl Artif Intell*, 90(103):541 |
| Kaur A, Kumar Y | 2021 | A new metaheuristic algorithm based on water wave optimization for data clustering | *Evolutionary Intelligence*, pp. 1–25 |
| Kaveh A, Bakhshpoori T | 2016 | Water evaporation optimization: a novel physically inspired optimization algorithm | *Computers & Structures*, 167:69–85 |
| Kaveh A, Dadras A | 2017 | A novel meta-heuristic optimization algorithm: thermal exchange optimization | *Adv Eng Softw*, 110:69–84 |
| Kaveh A, Farhoudi N | 2013 | A new optimization method: Dolphin echolocation | *Adv Eng Softw*, 59:53–70 |
| Kaveh A, Ghazaan MI | 2017 | Vibrating particles system algorithm for truss optimization with multiple natural frequency constraints | *Acta Mech*, 228(1):307–322 |
| Kaveh A, Khayatazad M | 2012 | A new meta-heuristic method: ray optimization | *Computers & Structures*, 112:283–294 |
| Kaveh A, Kooshkebaghi M | 2019 | Artificial coronary circulation system: A new bio-inspired metaheuristic algorithm | *Scientia Iranica*, 26(5):2731–2747 |
| Kaveh A, Mahdavi VR | 2014 | Colliding bodies optimization: a novel meta-heuristic method | *Computers & Structures*, 139:18–27 |
| Kaveh A, Talatahari S | 2010 | A novel heuristic optimization method: charged system search | *Acta Mech*, 213(3):267–289 |
| Kaveh A, Zolghadr A | 2016 | A novel meta-heuristic algorithm: tug of war optimization | *Iran University of Science & Technology*, 6(4):469–492 |
| Kaveh A, Zolghadr A | 2017 | Cyclical parthenogenesis algorithm: A new meta-heuristic algorithm | *Asian Journal of Civil Engineering*, 18:673–701 |
| Kaveh A, Share MAM, Moslehi M | 2013 | Magnetic charged system search: a new meta-heuristic algorithm for optimization | *Acta Mech*, 224(1):85–107 |
| Kaveh A, Seddighian M, Ghanadpour E | 2020 | Black hole mechanics optimization: a novel meta-heuristic algorithm | *Asian Journal of Civil Engineering*, 21(7):1129–1149 |
| Kaveh A, Akbari H, Hosseini SM | 2020a | Plasma generation optimization: a new physically-based metaheuristic algorithm for solving constrained optimization problems | *Engineering Computations* |
| Kaveh A, Eslamlou AD | 2020 | Water strider algorithm: A new metaheuristic and applications | *Structures*, Elsevier, pp. 520–541 |
| Kaveh A, Hosseini SM, Zaerreza A | 2022 | A physics-based metaheuristic algorithm based on doppler effect phenomenon and mean euclidian distance threshold | *Periodica Polytechnica Civil Engineering* |
| Kaveh A, Khanzadi M, Moghaddam MR | 2020b | Billiards-inspired optimization algorithm; a new metaheuristic method | *Structures*, Elsevier, pp. 1722–1739 |
| Kaveh A, Zaerreza A | 2020 | Shuffled shepherd optimization method: a new meta-heuristic algorithm | *Engineering Computations* |
| Kazikova A, Pluhacek M, Senkerik R, et al | 2017 | Proposal of a new swarm optimization method inspired in bison behavior | *23rd International Conference on Soft Computing*, Springer, pp. 146–156 |
| Kennedy J, Eberhart R | 1995 | Particle swarm optimization | *Proceedings of ICNN’95 - International Conference on Neural Networks*, pp. 1942–1948, doi:10.1109/ICNN.1995.488968 |
| Kennedy J, Mendes R | 2002 | Population structure and particle swarm performance | *2002 IEEE Congress on Evolutionary Computation*, IEEE, pp. 1671–1676 |
| Khalid AM, Hosny KM, Mirjalili S | 2022 | Covidoa: a novel evolutionary optimization algorithm based on coronavirus disease replication lifecycle | *Neural Computing and Applications*, pp. 1–28 |
| Khishe M, Mosavi MR | 2020 | Chimp optimization algorithm | *Expert Syst Appl*, 149(113):338 |
| Kiran MS | 2015 | Tsa: Tree-seed algorithm for continuous optimization | *Expert Syst Appl*, 42(19):6686–6698 |
| Kirkpatrick S, Gelatt CD, Vecchi MP | 1983 | Optimization by simulated annealing | *Science*, 220(4598):671–680 |
| Kivi ME, Majidnezhad V | 2022 | A novel swarm intelligence algorithm inspired by the grazing of sheep | *J Ambient Intell Humaniz Comput*, 13(2):1201–1213 |
| Klau GW, Ljubić I, Moser A, et al | 2004 | Combining a memetic algorithm with integer programming to solve the prize-collecting steiner tree problem | *Genetic and Evolutionary Computation Conference*, Springer, pp. 1304–1315 |
| Klein CE, dos Santos Coelho L | 2018 | Meerkats-inspired algorithm for global optimization problems | *ESANN* |
| Klein CE, Mariani VC, dos Santos Coelho L | 2018 | Cheetah based optimization algorithm: A novel swarm intelligence paradigm | *ESANN*, Bruges, Belgium, pp. 685–690 |
| Kong X, Chen YL, Xie W, et al | 2012 | A novel paddy field algorithm based on pattern search method | *2012 IEEE International Conference on Information and Automation*, IEEE, pp. 686–690 |
| Kononova AV, Corne DW, De Wilde P et al | 2015 | Structural bias in population-based algorithms | *Inf Sci*, 298:468–490 |
| Koohi SZ, Hamid NAWA, Othman M et al | 2018 | Raccoon optimization algorithm | *IEEE Access*, 7:5383–5399 |
| Koza JR et al | 1994 | Genetic programming II | Vol. 17. MIT Press, Cambridge |
| Koza T, Karaboga N, Koçkanat S | 2012 | Aort valve doppler signal noise elimination using iir filter designed with abc algorithm | *2012 International Symposium on Innovations in Intelligent Systems and Applications*, IEEE, pp. 1–5 |
| Kumar V, Chhabra JK, Kumar D | 2012 | Effect of harmony search parameters’ variation in clustering | *Procedia Technol*, 6:265–274 |
| Kumar N, Singh N, Vidyarthi DP | 2021 | Artificial lizard search optimization (also): a novel nature-inspired meta-heuristic algorithm | *Soft Comput*, 25(8):6179–6201 |
| Kumar A, Misra R, Singh D | 2015 | Butterfly optimizer | *2015 IEEE Workshop on Computational Intelligence: Theories, Applications and Future Directions (WCI)*, pp. 1–6 |
| Kundu S | 1999 | Gravitational clustering: a new approach based on the spatial distribution of the points | *Pattern Recogn*, 32(7):1149–1160 |
| Kuo RJ, Zulvia FE | 2015 | The gradient evolution algorithm: A new metaheuristic | *Inf Sci*, 316:246–265 |
| Kuyu YÇ, Vatansever F | 2022 | Gozde: A novel metaheuristic algorithm for global optimization | *Futur Gener Comput Syst*, 136:128–152 |
| Labbi Y, Attous DB, Gabbar HA et al | 2016 | A new rooted tree optimization algorithm for economic dispatch with valve-point effect | *International Journal of Electrical Power & Energy Systems*, 79:298–311 |
| Lamy JB | 2019 | Artificial feeding birds (afb): a new metaheuristic inspired by the behavior of pigeons | *Advances in Nature-Inspired Computing and Applications*, Springer, pp. 43–60 |
| Layeb A | 2021 | The tangent search algorithm for solving optimization problems | arXiv preprint arXiv:2104.02559 |
| Lee ZY | 2006 | Method of bilaterally bounded to solution blasius equation using particle swarm optimization | *Appl Math Comput*, 179(2):779–786 |
| Lee KS, Geem ZW | 2005 | A new meta-heuristic algorithm for continuous engineering optimization: harmony search theory and practice | *Comput Methods Appl Mech Eng*, 194(36–38):3902–3933 |
| Li X | 2003 | A new intelligent optimization-artificial fish swarm algorithm | Doctoral thesis, Zhejiang University, China |
| Li X, Zhang J, Yin M | 2014 | Animal migration optimization: an optimization algorithm inspired by animal migration behavior | *Neural Comput Appl*, 24(7–8):1867–1877 |
| Li L, Sun L, Kang W et al | 2016 | Fuzzy multilevel image thresholding based on modified discrete grey wolf optimizer and local information aggregation | *IEEE Access*, 4:6438–6450 |
| Li M, Zhao H, Weng X et al | 2016 | Cognitive behavior optimization algorithm for solving optimization problems | *Appl Soft Comput*, 39:199–222 |
| Li MD, Zhao H, Weng XW et al | 2016 | A novel nature-inspired algorithm for optimization: Virus colony search | *Adv Eng Softw*, 92:65–88 |
| Li X, Cai Z, Wang Y et al | 2020 | Tdsd: A new evolutionary algorithm based on triple distinct search dynamics | *IEEE Access*, 8:76,752–76,764 |
| Liang J, Qu B, Suganthan P et al | 2014 | Problem definitions and evaluation criteria for the cec 2015 competition on learning-based real-parameter single objective optimization | Technical Report 201411A, Zhengzhou Univ. & Nanyang Tech. Univ. |
| Li Z, Tam V | 2020 | A novel meta-heuristic optimization algorithm inspired by the spread of viruses | arXiv preprint arXiv:2006.06282 |
| Liu Y, Li R | 2020 | Psa: a photon search algorithm | *Journal of Information Processing Systems*, 16(2):478–493 |
| Liu C, Yan X, Liu C et al | 2011 | The wolf colony algorithm and its application | *Chin J Electron*, 20(2):212–216 |
| Liu Q, Wei W, Yuan H et al | 2016 | Topology selection for particle swarm optimization | *Inf Sci*, 363:154–173 |
| Liu R, Zhou N, Yao Y et al | 2022 | An aphid inspired metaheuristic optimization algorithm and its application to engineering | *Sci Rep*, 12(1):1–17 |
| Lucic P, Teodorovic D | 2002 | Transportation modeling: an artificial life approach | *14th IEEE International Conference on Tools with Artificial Intelligence*, IEEE, pp. 216–223 |
| Luo F, Zhao J, Dong ZY | 2016 | A new metaheuristic algorithm for real-parameter optimization: natural aggregation algorithm | *2016 IEEE Congress on Evolutionary Computation*, IEEE, pp. 94–103 |
| Mahdavi S, Shiri ME, Rahnamayan S | 2015 | Metaheuristics in large-scale global continuous optimization: A survey | *Inf Sci*, 295:407–428 |
| Mahmood M, Al-Khateeb B | 2019 | The blue monkey: A new nature inspired metaheuristic optimization algorithm | *Periodicals of Engineering and Natural Sciences*, 7(3):1054–1066 |
| Mahmoodabadi M, Rasekh M, Zohari T | 2018 | Tga: Team game algorithm | *Future Computing and Informatics Journal*, 3(2):191–199 |
| Maia RD, de Castro LN, Caminhas WM | 2013 | Optbees-a bee-inspired algorithm for solving continuous optimization problems | *2013 BRICS Congress on Computational Intelligence*, IEEE, pp. 142–151 |
| Malakooti B, Kim H, Sheikh S | 2012 | Bat intelligence search with application to multi-objective multiprocessor scheduling optimization | *The International Journal of Advanced Manufacturing Technology*, 60(9–12):1071–1086 |
| Mandal S | 2018 | Elephant swarm water search algorithm for global optimization | *Sādhanā*, 43(1):1–21 |
| Mann PS, Singh S | 2017 | Improved metaheuristic based energy-efficient clustering protocol for wireless sensor networks | *Eng Appl Artif Intell*, 57:142–152 |
| Marinakis Y, Marinaki M, Matsatsinis N | 2010 | A bumble bees mating optimization algorithm for global unconstrained optimization problems | *Nature Inspired Cooperative Strategies for Optimization (NICSO 2010)*, Springer, pp. 305–318 |
| Martinez-Soto R, Castillo O, Aguilar LT, et al | 2012 | Bio-inspired optimization of fuzzy logic controllers for autonomous mobile robots | *2012 Annual Meeting of the North American Fuzzy Information Processing Society*, IEEE, pp. 1–6 |
| Masoudi-Sobhanzadeh Y, Jafari B, Parvizpour S et al | 2021 | A novel multi-objective metaheuristic algorithm for protein-peptide docking and benchmarking on the leads-pep dataset | *Comput Biol Med*, 138(104):896 |
| McCaffrey JD | 2009 | Generation of pairwise test sets using a simulated bee colony algorithm | *2009 IEEE International Conference on Information Reuse & Integration*, IEEE, pp. 115–119 |
| Mehrabian AR, Lucas C | 2006 | A novel numerical optimization algorithm inspired from weed colonization | *Eco Inform*, 1(4):355–366 |
| Melin P, Astudillo L, Castillo O et al | 2013 | Optimal design of type-2 and type-1 fuzzy tracking controllers for autonomous mobile robots under perturbed torques using a new chemical optimization paradigm | *Expert Syst Appl*, 40(8):3185–3195 |
| Melvix JL | 2014 | Greedy politics optimization: Metaheuristic inspired by political strategies adopted during state assembly elections | *2014 IEEE International Advance Computing Conference (IACC)*, IEEE, pp. 1157–1162 |
| Menczer F, Pant G, Srinivasan P | 2004 | Topical web crawlers: Evaluating adaptive algorithms | *ACM Transactions on Internet Technology (TOIT)*, 4(4):378–419 |
| Meng XB, Gao XZ, Lu L et al | 2016 | A new bio-inspired optimisation algorithm: Bird swarm algorithm | *Journal of Experimental & Theoretical Artificial Intelligence*, 28(4):673–687 |
| Meng X, Liu Y, Gao X, et al | 2014 | A new bio-inspired algorithm: chicken swarm optimization | *International Conference in Swarm Intelligence*, Springer, pp. 86–94 |
| Merrikh-Bayat F | 2014 | A numerical optimization algorithm inspired by the strawberry plant | arXiv preprint arXiv:1407.7399 |
| Merrikh-Bayat F | 2015 | The runner-root algorithm: a metaheuristic for solving unimodal and multimodal optimization problems inspired by runners and roots of plants in nature | *Appl Soft Comput*, 33:292–303 |
| Milani A, Santucci V | 2012 | Community of scientist optimization: An autonomy oriented approach to distributed optimization | *AI Commun*, 25(2):157–172 |
| Minh HL, Sang-To T, Theraulaz G et al | 2022 | Termite life cycle optimizer | *Expert Syst Appl*, 213(119):211 |
| Min H, Wang Z | 2011 | Design and analysis of group escape behavior for distributed autonomous mobile robots | *2011 IEEE International Conference on Robotics and Automation*, IEEE, pp. 6128–6135 |
| Mirjalili S | 2015 | The ant lion optimizer | *Adv Eng Softw*, 83:80–98 |
| Mirjalili S | 2015 | Moth-flame optimization algorithm: A novel nature-inspired heuristic paradigm | *Knowl-Based Syst*, 89:228–249 |
| Mirjalili S | 2016 | Dragonfly algorithm: a new meta-heuristic optimization technique for solving single-objective, discrete, and multi-objective problems | *Neural Comput Appl*, 27(4):1053–1073 |
| Mirjalili S | 2016 | Sca: a sine cosine algorithm for solving optimization problems | *Knowl-Based Syst*, 96:120–133 |
| Mirjalili S, Lewis A | 2016 | The whale optimization algorithm | *Adv Eng Softw*, 95:51–67 |
| Mirjalili S, Mirjalili SM, Lewis A | 2014 | Grey wolf optimizer | *Adv Eng Softw*, 69:46–61 |
| Mirjalili S, Mirjalili SM, Hatamlou A | 2016 | Multi-verse optimizer: a nature-inspired algorithm for global optimization | *Neural Comput Appl*, 27(2):495–513 |
| Mirjalili S, Gandomi AH, Mirjalili SZ et al | 2017 | Salp swarm algorithm: A bio-inspired optimizer for engineering design problems | *Adv Eng Softw*, 114:163–191 |
| Mirjalili S, Lewis A | 2019 | Benchmark function generators for single-objective robust optimisation algorithms | *Decision Science in Action*, Springer, pp. 13–29 |
| Misra RK, Singh D, Kumar A | 2020 | Spherical search algorithm: A metaheuristic for bound-constrained optimization | *Indo-French Seminar on Optimization, Variational Analysis and Applications*, Springer, pp. 421–441 |
| Moazzeni AR, Khamehchi E | 2020 | Rain optimization algorithm (roa): A new metaheuristic method for drilling optimization solutions | *J Petrol Sci Eng*, 195(107):512 |
| Moein S, Logeswaran R | 2014 | Kgmo: A swarm optimization algorithm based on the kinetic energy of gas molecules | *Inf Sci*, 275:127–144 |
| Moez H, Kaveh A, Taghizadieh N | 2016 | Natural forest regeneration algorithm: A new meta-heuristic | *Iranian Journal of Science and Technology, Transactions of Civil Engineering*, 40(4):311–326 |
| Moghdani R, Salimifard K | 2018 | Volleyball premier league algorithm | *Appl Soft Comput*, 64:161–185 |
| Mohamed AW, Hadi AA, Mohamed AK | 2020 | Gaining-sharing knowledge based algorithm for solving optimization problems: a novel nature-inspired algorithm | *Int J Mach Learn Cybern*, 11(7):1501–1529 |
| Mohammadi-Balani A, Nayeri MD, Azar A et al | 2021 | Golden eagle optimizer: A nature-inspired metaheuristic algorithm | *Computers & Industrial Engineering*, 152(107):050 |

---

Here is the complete bibliography transcribed into a single Markdown table.

| Author(s) | Year | Title | Publication Source & Details |
| :--- | :--- | :--- | :--- |
| Meng X, Liu Y, Gao X, et al | 2014 | A new bio-inspired algorithm: chicken swarm optimization | In: International Conference in Swarm Intelligence, Springer, pp 86–94 |
| Merrikh-Bayat F | 2014 | A numerical optimization algorithm inspired by the strawberry plant | arXiv preprint arXiv:1407.7399 |
| Merrikh-Bayat F | 2015 | The runner-root algorithm: a metaheuristic for solving unimodal and multimodal optimization problems inspired by runners and roots of plants in nature | Appl Soft Comput 33:292–303 |
| Milani A, Santucci V | 2012 | Community of scientist optimization: An autonomy oriented approach to distributed optimization | AI Commun 25(2):157–172 |
| Minh HL, Sang-To T, Theraulaz G et al | 2022 | Termite life cycle optimizer | Expert Syst Appl 213(119):211 |
| Min H, Wang Z | 2011 | Design and analysis of group escape behavior for distributed autonomous mobile robots | In: 2011 IEEE International Conference on Robotics and Automation, IEEE, pp 6128–6135 |
| Mirjalili S | 2015 | The ant lion optimizer | Adv Eng Softw 83:80–98 |
| Mirjalili S | 2015 | Moth-flame optimization algorithm: A novel nature-inspired heuristic paradigm | Knowl-Based Syst 89:228–249 |
| Mirjalili S | 2016 | Dragonfly algorithm: a new meta-heuristic optimization technique for solving single-objective, discrete, and multi-objective problems | Neural Comput Appl 27(4):1053–1073 |
| Mirjalili S | 2016 | Sca: a sine cosine algorithm for solving optimization problems | Knowl-Based Syst 96:120–133 |
| Mirjalili S, Lewis A | 2016 | The whale optimization algorithm | Adv Eng Softw 95:51–67 |
| Mirjalili S, Mirjalili SM, Lewis A | 2014 | Grey wolf optimizer | Adv Eng Softw 69:46–61 |
| Mirjalili S, Mirjalili SM, Hatamlou A | 2016 | Multi-verse optimizer: a nature-inspired algorithm for global optimization | Neural Comput Appl 27(2):495–513 |
| Mirjalili S, Gandomi AH, Mirjalili SZ et al | 2017 | Salp swarm algorithm: A bio-inspired optimizer for engineering design problems | Adv Eng Softw 114:163–191 |
| Mirjalili S, Lewis A | 2019 | Benchmark function generators for single-objective robust optimisation algorithms | In: Decision Science in Action. Springer, p 13–29 |
| Misra RK, Singh D, Kumar A | 2020 | Spherical search algorithm: A metaheuristic for bound-constrained optimization | In: Indo-French Seminar on Optimization, Variational Analysis and Applications, Springer, pp 421–441 |
| Moazzeni AR, Khamehchi E | 2020 | Rain optimization algorithm (roa): A new metaheuristic method for drilling optimization solutions | J Petrol Sci Eng 195(107):512 |
| Moein S, Logeswaran R | 2014 | Kgmo: A swarm optimization algorithm based on the kinetic energy of gas molecules | Inf Sci 275:127–144 |
| Moez H, Kaveh A, Taghizadieh N | 2016 | Natural forest regeneration algorithm: A new meta-heuristic | Iranian Journal of Science and Technology, Transactions of Civil Engineering 40(4):311–326 |
| Moghdani R, Salimifard K | 2018 | Volleyball premier league algorithm | Appl Soft Comput 64:161–185 |
| Mohamed AW, Hadi AA, Mohamed AK | 2020 | Gaining-sharing knowledge based algorithm for solving optimization problems: a novel nature-inspired algorithm | Int J Mach Learn Cybern 11(7):1501–1529 |
| Mohammadi-Balani A, Nayeri MD, Azar A et al | 2021 | Golden eagle optimizer: A nature-inspired metaheuristic algorithm | Computers & Industrial Engineering 152(107):050 |
| Mohammed H, Rashid T | 2022 | Fox: a fox-inspired optimization algorithm | Applied Intelligence pp 1–21 |
| Molina D, Poyatos J, Ser JD et al | 2020 | Comprehensive taxonomies of nature-and bio-inspired optimization: Inspiration versus algorithmic behavior, critical analysis recommendations | Cogn Comput 12(5):897–939 |
| Monismith DR, Mayfield BE | 2008 | Slime mold as a model for numerical optimization | In: 2008 IEEE Swarm Intelligence Symposium, IEEE, pp 1–8 |
| Montiel O, Castillo O, Melin P et al | 2007 | Human evolutionary model: A new approach to optimization | Inf Sci 177(10):2075–2098 |
| Moosavi SHS, Bardsiri VK | 2017 | Satin bowerbird optimizer: A new optimization algorithm to optimize anfis for software development effort estimation | Eng Appl Artif Intell 60:1–15 |
| Moosavian N, Roodsari BK | 2014 | Soccer league competition algorithm: A novel meta-heuristic algorithm for optimal design of water distribution networks | Swarm Evol Comput 17:14–24 |
| Mora-Gutiérrez RA, Ramírez-Rodríguez J, Rincón-García EA | 2014 | An optimization algorithm inspired by musical composition | Artif Intell Rev 41(3):301–315 |
| Moscato P, et al | 1989 | On evolution, search, optimization, genetic algorithms and martial arts: Towards memetic algorithms | Caltech Concurrent Computation Program, C3P Report 826:1989 |
| Mousavirad SJ, Ebrahimpour H | 2017 | Human mental search: a new population-based metaheuristic optimization algorithm | Appl Intell 47(3):850–887 |
| Mo H, Xu L | 2013 | Magnetotactic bacteria optimization algorithm for multimodal optimization | In: 2013 IEEE Symposium on Swarm Intelligence (SIS), IEEE, pp 240–247 |
| Mozaffari A, Goudarzi AM, Fathi A et al | 2013 | Bio-inspired methods for fast and robust arrangement of thermoelectric modulus | International Journal of Bio-Inspired Computation 5(1):19–34 |
| Mucherino A, Seref O | 2007 | Monkey search: a novel metaheuristic search for global optimization | In: AIP conference proceedings, American Institute of Physics, pp 162–173 |
| Muller SD, Marchetto J, Airaghi S et al | 2002 | Optimization based on bacterial chemotaxis | IEEE Trans Evol Comput 6(1):16–29 |
| Munoz MA, López JA, Caicedo E | 2009 | An artificial beehive algorithm for continuous optimization | Int J Intell Syst 24(11):1080–1093 |
| Murase H | 2000 | Finite element inverse analysis using a photosynthetic algorithm | Comput Electron Agric 29(1–2):115–123 |
| Mutazono A, Sugano M, Murata M | 2009 | Frog call-inspired self-organizing anti-phase synchronization for wireless sensor networks | In: 2009 2nd International workshop on nonlinear dynamics and synchronization, IEEE, pp 81–88 |
| Muthiah-Nakarajan V, Noel MM | 2016 | Galactic swarm optimization: A new global optimization metaheuristic inspired by galactic motion | Appl Soft Comput 38:771–787 |
| Naderi B, Khalili M, Khamseh AA | 2014 | Mathematical models and a hunting search algorithm for the no-wait flowshop scheduling with parallel machines | Int J Prod Res 52(9):2667–2681 |
| Narang N, Dhillon J, Kothari D | 2014 | Scheduling short-term hydrothermal generation using predator prey optimization technique | Appl Soft Comput 21:298–308 |
| Nara K, Takeyama T, Kim H | 1999 | A new evolutionary algorithm based on sheep flocks heredity model and its application to scheduling problem | In: IEEE SMC’99 Conference Proceedings. 1999 IEEE International Conference on Systems, Man, and Cybernetics, IEEE, pp 503–508 |
| Nematollahi AF, Rahiminejad A, Vahidi B | 2017 | A novel physical based meta-heuristic optimization method known as lightning attachment procedure optimization | Appl Soft Comput 59:596–621 |
| Neshat M, Sepidnam G, Sargolzaei M | 2013 | Swallow swarm optimization algorithm: a new method to optimization | Neural Comput Appl 23(2):429–454 |
| Nguyen HT, Bhanu B | 2012 | Zombie survival optimization: A swarm intelligence algorithm inspired by zombie foraging | In: Proceedings of the 21st International Conference on Pattern Recognition, IEEE, pp 987–990 |
| Nguyen LB, Nguyen AV, Ling SH, et al | 2013 | Combining genetic algorithm and levenberg-marquardt algorithm in training neural network for hypoglycemia detection using eeg signals | In: 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, IEEE, pp 5386–5389 |
| Nishida TY | 2006 | Membrane algorithms: approximate algorithms for np-complete optimization problems | In: Applications of Membrane Computing. Springer, p 303–314 |
| Niu B, Wang H | 2012 | Bacterial colony optimization | Discrete Dynamics in Nature and Society 2012 |
| Noroozi M, Mohammadi H, Efatinasab E et al | 2022 | Golden search optimization algorithm | IEEE Access 10:37,515-37,532 |
| Numaoka C | 1996 | Bacterial evolution algorithm for rapid adaptation | In: European Workshop on Modelling Autonomous Agents in a Multi-Agent World, Springer, pp 139–148 |
| Odili JB, Kahar MNM, Anwar S | 2015 | African buffalo optimization: A swarm-intelligence technique | Procedia Computer Science 76:443–448 |
| Oftadeh R, Mahjoob M, Shariatpanahi M | 2010 | A novel meta-heuristic optimization algorithm inspired by group hunting of animals: Hunting search | Computers & Mathematics with Applications 60(7):2087–2098 |
| Ojugo A, Emudianughe J, Yoro R et al | 2013 | A hybrid artificial neural network gravitational search algorithm for rainfall runoffs modeling and simulation in hydrology | Prog Intell Comput Appl 2(1):22–33 |
| Omidvar R, Parvin H, Rad F | 2015 | Sspco optimization algorithm (see-see partridge chicks optimization) | In: 2015 Fourteenth Mexican International Conference on Artificial Intelligence (MICAI), IEEE, pp 101–106 |
| Osaba E, Diaz F, Onieva E | 2014 | Golden ball: a novel meta-heuristic to solve combinatorial optimization problems based on soccer concepts | Appl Intell 41(1):145–166 |
| Osaba E, Villar-Rodriguez E, Del Ser J, et al | 2021 | A tutorial on the design, experimentation and application of metaheuristic algorithms to real-world optimization problems | Swarm and Evolutionary Computation p 100888 |
| Oyelade ON, Ezugwu AE | 2021 | Ebola optimization search algorithm (eosa): A new metaheuristic algorithm based on the propagation model of ebola virus disease | arXiv preprint arXiv:2106.01416 |
| Pambudi D, Kawamura M | 2022 | Novel metaheuristic: Spy algorithm | IEICE Trans Inf Syst 105(2):309–319 |
| Pan WT | 2012 | A new fruit fly optimization algorithm: taking the financial distress model as an example | Knowl-Based Syst 26:69–74 |
| Pan JS, Zhang LG, Wang RB et al | 2022 | Gannet optimization algorithm: A new metaheuristic algorithm for solving engineering optimization problems | Math Comput Simul 202:343–373 |
| Panagant N, Bureerat S | 2014 | Solving partial differential equations using a new differential evolution algorithm | Mathematical Problems in Engineering 2014 |
| Panwar K, Deep K | 2021 | Discrete grey wolf optimizer for symmetric travelling salesman problem | Appl Soft Comput 105(107):298 |
| Parpinelli RS, Lopes HS | 2011 | An eco-inspired evolutionary algorithm applied to numerical optimization | In: 2011 Third World Congress on Nature and Biologically Inspired Computing, IEEE, pp 466–471 |
| Passino KM | 2002 | Biomimicry of bacterial foraging for distributed optimization and control | IEEE Control Syst Mag 22(3):52–67 |
| Patel VK, Savsani VJ | 2015 | Heat transfer search (hts): a novel optimization algorithm | Inf Sci 324:217–246 |
| Pattnaik SS, Bakwad KM, Sohi B et al | 2013 | Swine influenza models based optimization (simbo) | Appl Soft Comput 13(1):628–653 |
| Pham DT, Ghanbarzadeh A, Koç E, et al | 2006 | The bees algorithm-a novel tool for complex optimisation problems | In: Intelligent Production Machines and Systems. Elsevier, p 454–459 |
| Pierezan J, Maidl G, Yamao EM et al | 2019 | Cultural coyote optimization algorithm applied to a heavy duty gas turbine operation | Energy Convers Manage 199(111):932 |
| Pierezan J, Coelho LDS | 2018 | Coyote optimization algorithm: a new metaheuristic for global optimization problems | In: 2018 IEEE Congress on Evolutionary Computation, IEEE, pp 1–8 |
| Pijarski P, Kacejko P | 2019 | A new metaheuristic optimization method: the algorithm of the innovative gunner (aig) | Engineering Optimization |
| Pinto P, Runkler TA, Sousa JM | 2005 | Wasp swarm optimization of logistic systems | In: Adaptive and Natural Computing Algorithms. Springer, p 264–267 |
| Piotrowski AP, Napiorkowski JJ | 2018 | Some metaheuristics should be simplified | Inf Sci 427:32–62 |
| Piotrowski AP, Napiorkowski JJ, Rowinski PM | 2014 | How novel is the "novel" black hole optimization approach? | Inf Sci 267:191–200 |
| Pira E | 2022 | City councils evolution: a socio-inspired metaheuristic optimization algorithm | Journal of Ambient Intelligence and Humanized Computing pp 1–50 |
| Pitzer E, Affenzeller M, Beham A | 2010 | A closer look down the basins of attraction | In: 2010 UK Workshop on Computational Intelligence, IEEE, pp 1–6 |
| Polya G | 2004 | How to solve it: A new aspect of mathematical method | 246, Princeton university press |
| Prakasam A, Savarimuthu N | 2015 | Metaheuristic algorithms and polynomial turing reductions: A case study based on ant colony optimization | Procedia Computer Science 46:388–395 |
| Punnathanam V, Kotecha P | 2016 | Yin-yang-pair optimization: A novel lightweight optimization algorithm | Eng Appl Artif Intell 54:62–79 |
| Puris A, Bello R, Molina D et al | 2012 | Variable mesh optimization for continuous optimization problems | Soft Comput 16(3):511–525 |
| Purnomo HD | 2014 | Soccer game optimization: Fundamental concept | Jurnal Sistem Komputer 4(1):25–36 |
| Qais MH, Hasanien HM, Alghuwainem S | 2020 | Transient search optimization: a new meta-heuristic optimization algorithm | Appl Intell 50(11):3926–3941 |
| Qais MH, Hasanien HM, Turky RA et al | 2022 | Circle search algorithm: A geometry-based metaheuristic optimization algorithm | Mathematics 10(10):1626 |
| Qi X, Zhu Y, Zhang H | 2017 | A new meta-heuristic butterfly-inspired algorithm | Journal of Computational Science 23:226–239 |
| Quan H, Shi X | 2017 | A surface-simplex swarm evolution algorithm | Wuhan Univ J Nat Sci 22(1):38–50 |
| Quijano N, Passino KM | 2007 | Honey bee social foraging algorithms for resource allocation, part i: algorithm and theory | In: 2007 American Control Conference, IEEE, pp 3383–3388 |
| Rabanal P, Rodríguez I, Rubio F | 2007 | Using river formation dynamics to design heuristic algorithms | In: International Conference on Unconventional Computation, Springer, pp 163–177 |
| Rahkar Farshi T | 2021 | Battle royale optimization algorithm | Neural Comput Appl 33:1139–1157 |
| Rahmani AM, AliAbdi I | 2022 | Plant competition optimization: A novel metaheuristic algorithm | Expert Syst 39(6):e12,956 |
| Rahmani R, Yusof R | 2014 | A new simple, fast and efficient algorithm for global optimization over continuous search-space problems: radial movement optimization | Appl Math Comput 248:287–300 |
| Rahmanzadeh S, Pishvaee MS | 2020 | Electron radar search algorithm: a novel developed meta-heuristic algorithm | Soft Comput 24(11):8443–8465 |
| Raidl GR | 2006 | A unified view on hybrid metaheuristics | In: International Workshop on Hybrid Metaheuristics, Springer, pp 1–12 |
| Rajabioun R | 2011 | Cuckoo optimization algorithm | Appl Soft Comput 11(8):5508–5518 |
| Rajakumar B | 2012 | The lion's algorithm: a new nature-inspired search algorithm | Procedia Technol 6:126–135 |
| Rakhshani H, Rahati A | 2017 | Snap-drift cuckoo search: A novel cuckoo search optimization algorithm | Appl Soft Comput 52:771–794 |
| Rao R | 2016 | Jaya: A simple and new optimization algorithm for solving constrained and unconstrained optimization problems | Int J Ind Eng Comput 7(1):19–34 |
| Rao RV, Savsani VJ, Vakharia D | 2011 | Teaching-learning-based optimization: a novel method for constrained mechanical design optimization problems | Comput Aided Des 43(3):303–315 |
| Raouf OA, Hezam IM | 2017 | Sperm motility algorithm: a novel metaheuristic approach for global optimisation | International Journal of Operational Research 28(2):143–163 |
| Rashedi E, Nezamabadi-Pour H, Saryazdi S | 2009 | Gsa: a gravitational search algorithm | Inf Sci 179(13):2232–2248 |
| Rashid MFFA | 2020 | Tiki-taka algorithm: a novel metaheuristic inspired by football playing style | Eng Comput 38:313–343 |
| Ray T, Liew KM | 2003 | Society and civilization: an optimization algorithm based on the simulation of social behavior | IEEE Trans Evol Comput 7(4):386–396 |
| Razmjooy N, Khalilpour M, Ramezani M | 2016 | A new meta-heuristic optimization algorithm inspired by fifa world cup competitions: theory and its application in pid designing for avr system | Journal of Control, Automation and Electrical Systems 27(4):419–440 |
| Rbouh I, El Imrani AA | 2014 | Hurricane-based optimization algorithm | AASRI Procedia 6:26–33 |
| Reddy KS, Panwar L, Panigrahi B et al | 2019 | Binary whale optimization algorithm: a new metaheuristic approach for profit-based unit commitment problems in competitive electricity markets | Eng Optim 51(3):369–389 |
| Reynolds CW | 1987 | Flocks, herds and schools: A distributed behavioral model | In: Proceedings of the 14th Annual Conference on Computer Graphics and Interactive Techniques, pp 25–34 |
| Rodriguez L, Castillo O, Garcia M et al | 2021 | A new meta-heuristic optimization algorithm based on a paradigm from physics: string theory | Journal of Intelligent & Fuzzy Systems 41(1):1657–1675 |
| Rosenberg L, Willcox G | 2018 | Artificial swarms find social optima: (late breaking report) | In: 2018 IEEE Conference on Cognitive and Computational Aspects of Situation Management, IEEE, pp 174–178 |
| Saadi Y, Yanto ITR, Herawan T et al | 2016 | Ringed seal search for global optimization via a sensitive search model | PLoS ONE 11(1):e0144,371 |
| Sacco WF, Alves Filho H, De Oliveira C | 2007 | A populational particle collision algorithm applied to a nuclear reactor core design optimization | In: Joint International Topical Meeting on Mathematics and Computations for Supercomputing in Nuclear Applications, M&C+SNA 2007 (CD-ROM), pp 15–19 |
| Sadollah A, Bahreininejad A, Eskandar H et al | 2013 | Mine blast algorithm: A new population based algorithm for solving constrained engineering optimization problems | Appl Soft Comput 13(5):2592–2612 |
| Sadollah A, Choi Y, Kim JH et al | 2015 | Metaheuristic algorithms for approximate solution to ordinary differential equations of longitudinal fins having various profiles | Appl Soft Comput 33:360–379 |
| Saha A, Das P, Chakraborty AK | 2017 | Water evaporation algorithm: A new metaheuristic algorithm towards the solution of optimal power flow | Engineering Science and Technology, an International Journal 20(6):1540–1552 |
| Salcedo-Sanz S, Del Ser J, Landa-Torres I, et al | 2014 | The coral reefs optimization algorithm: a novel metaheuristic for efficiently solving optimization problems | The Scientific World Journal 2014 |
| Salehan A, Deldari A | 2022 | Corona virus optimization (cvo): A novel optimization algorithm inspired from the corona virus pandemic | J Supercomput 78(4):5712–5743 |
| Salgotra R, Singh U | 2019 | The naked mole-rat algorithm | Neural Comput Appl 31(12):8837–8857 |
| Salih SQ, Alsewari AA | 2020 | A new algorithm for normal and large-scale optimization problems: Nomadic people optimizer | Neural Comput Appl 32(14):10,359-10,386 |
| Salim A, Jummar WK, Jasim FM et al | 2022 | Eurasian oystercatcher optimiser: New meta-heuristic algorithm | J Intell Syst 31(1):332–344 |
| Salimi H | 2015 | Stochastic fractal search: a powerful metaheuristic algorithm | Knowl-Based Syst 75:1–18 |
| Samie Yousefi F, Karimian N, Ghodousian A | 2019 | Xerus optimization algorithm (xoa): a novel nature inspired metaheuristic algorithm for solving global optimization problems | Journal of Algorithms and Computation 51(2):111–126 |
| Saremi S, Mirjalili S, Lewis A | 2017 | Grasshopper optimisation algorithm: theory and application | Adv Eng Softw 105:30–47 |
| Sato T, Hagiwara M | 1998 | Bee system: finding solution by a concentrated search | IEEJ Transactions on Electronics, Information and Systems 118(5):721–726 |
| Sattar D, Salim R | 2021 | A smart metaheuristic algorithm for solving engineering problems | Engineering with Computers 37(3):2389–2417 |
| Savsani P, Savsani V | 2016 | Passing vehicle search (pvs): A novel metaheuristic algorithm | Appl Math Model 40(5–6):3951–3978 |
| Sayed GI, Solyman M, Hassanien AE | 2019 | A novel chaotic optimal foraging algorithm for unconstrained and constrained problems and its application in white blood cell segmentation | Neural Comput Appl 31(11):7633–7664 |
| Sayed GI, Tharwat A, Hassanien AE | 2019 | Chaotic dragonfly algorithm: an improved metaheuristic algorithm for feature selection | Appl Intell 49(1):188–205 |
| Shadravan S, Naji H, Bardsiri VK | 2019 | The sailfish optimizer: A novel nature-inspired metaheuristic algorithm for solving constrained engineering optimization problems | Eng Appl Artif Intell 80:20–34 |
| Shah-Hosseini H | 2009 | The intelligent water drops algorithm: a nature-inspired swarm-based optimization algorithm | International Journal of Bio-inspired Computation 1(1–2):71–79 |
| Shah-Hosseini H | 2011 | Principal components analysis by the galaxy-based search algorithm: a novel metaheuristic for continuous optimisation | Int J Comput Sci Eng 6(1–2):132–140 |
| Shahrouzi M, Kaveh A | 2022 | An efficient derivative-free optimization algorithm inspired by avian life-saving manoeuvres | Journal of Computational Science 57(101):483 |
| Shalamov V, Filchenkov A, Shalyto A | 2019 | Heuristic and metaheuristic solutions of pickup and delivery problem for self-driving taxi routing | Evol Syst 10(1):3–11 |
| Sharafi Y, Khanesar MA, Teshnehlab M | 2016 | Cooa: Competitive optimization algorithm | Swarm Evol Comput 30:39–63 |
| Shareef H, Ibrahim AA, Mutlag AH | 2015 | Lightning search algorithm | Appl Soft Comput 36:315–333 |
| Sharma A | 2010 | A new optimizing algorithm using reincarnation concept | In: 2010 11th International Symposium on Computational Intelligence and Informatics (CINTI), IEEE, pp 281–288 |
| Sharma S, Kumar V | 2022 | A comprehensive review on multi-objective optimization techniques: Past, present and future | Archives of Computational Methods in Engineering pp 1–29 |
| Shayanfar H, Gharehchopogh FS | 2018 | Farmland fertility: A new metaheuristic algorithm for solving continuous optimization problems | Appl Soft Comput 71:728–746 |
| Shehab M, Khader AT, Al-Betar MA | 2017 | A survey on applications and variants of the cuckoo search algorithm | Appl Soft Comput 61:1041–1059 |
| Shehadeh HA, Idna Idris MY, Ahmedy I et al | 2018 | The multi-objective optimization algorithm based on sperm fertilization procedure (mosfp) method for solving wireless sensor networks optimization problems in smart grid applications | Energies 11(1):97 |
| Shen J, Li J | 2010 | The principle analysis of light ray optimization algorithm | In: 2010 Second International Conference on Computational Intelligence and Natural Computing, IEEE, pp 154–157 |
| Shi Y | 2011 | Brain storm optimization algorithm | In: International Conference in Swarm Intelligence, Springer, pp 303–309 |
| Shiqin Y, Jianjun J, Guangxing Y | 2009 | A dolphin partner optimization | In: 2009 WRI global congress on intelligent systems, IEEE, pp 124–128 |
| Siddique N, Adeli H | 2015 | Nature inspired computing: an overview and some future directions | Cogn Comput 7(6):706–714 |
| Simon D | 2008 | Biogeography-based optimization | IEEE Trans Evol Comput 12(6):702–713 |
| Singh MK | 2013 | A new optimization method based on adaptive social behavior: Asbo | In: Proceedings of International Conference on Advances in Computing, Springer, pp 823–831 |
| Singh PR, Abd Elaziz M, Xiong S | 2019 | Ludo game-based metaheuristics for global and engineering optimization | Appl Soft Comput 84(105):723 |
| Skorin-Kapov J | 1990 | Tabu search applied to the quadratic assignment problem | ORSA J Comput 2(1):33–45 |
| Steer KC, Wirth A, Halgamuge SK | 2009 | The rationale behind seeking inspiration from nature | In: Nature-inspired algorithms for optimisation. Springer, p 51–76 |
| Storn R, Price K | 1997 | Differential evolution-a simple and efficient heuristic for global optimization over continuous spaces | J Global Optim 11(4):341–359 |
| Su MC, Su SY, Zhao YX | 2009 | A swarm-inspired projection algorithm | Pattern Recogn 42(11):2764–2786 |
| Subashini P, Dhivyaprabha T, Krishnaveni M | 2017 | Synergistic fibroblast optimization | In: Artificial Intelligence and Evolutionary Computations in Engineering Systems. Springer, p 285–294 |
| Subramanian C, Sekar A, Subramanian K | 2013 | A new engineering optimization method: African wild dog algorithm | Int J Soft Comput 8(3):163–170 |
| Suganthi M, Madheswaran M | 2012 | An improved medical decision support system to identify the breast cancer using mammogram | J Med Syst 36(1):79–91 |
| Sulaiman M, Salhi A | 2015 | A seed-based plant propagation algorithm: the feeding station model | The Scientific World Journal 2015 |
| Sulaiman M, Salhi A, Selamoglu BI, et al | 2014 | A plant propagation algorithm for constrained engineering optimisation problems | Mathematical Problems in Engineering 2014 |
| sulfur HP | 1977 | Numerical optimization of computer models using the evolution strategy: with a comparative introduction to the hill climbing and random strategy | Vol 1. Springer |
| Suman B, Kumar P | 2006 | A survey of simulated annealing as a tool for single and multiobjective optimization | Journal of the Operational Research Society 57(10):1143–1160 |
| Sur C, Sharma S, Shukla A | 2013 | Egyptian vulture optimization algorithm–a new nature inspired metaheuristics for knapsack problem | In: The 9th International Conference on Computing and Information Technology (IC2IT2013), Springer, pp 227–237 |
| Su S, Wang J, Fan W, et al | 2007 | Good lattice swarm algorithm for constrained engineering design optimization | In: 2007 International Conference on Wireless Communications, Networking and Mobile Computing, IEEE, pp 6421–6424 |
| Suyanto S, Ariyanto AA, Ariyanto AF | 2021 | Komodo mlipir algorithm | Applied Soft Computing p 108043 |
| Tahani M, Babayan N | 2019 | Flow regime algorithm (fra): a physics-based meta-heuristics algorithm | Knowl Inf Syst 60(2):1001–1038 |
| Taherdangkoo M, Shirzadi MH, Yazdi M et al | 2013 | A robust clustering method based on blind, naked mole-rats (bnmr) algorithm | Swarm Evol Comput 10:1–11 |
| Taherdangkoo M, Yazdi M, Bagheri MH | 2011 | Stem cells optimization algorithm | In: International Conference on Intelligent Computing, Springer, pp 394–403 |
| Taillard ÉD, Voss S | 2002 | Popmusic-partial optimization metaheuristic under special intensification conditions | In: Essays and surveys in metaheuristics. Springer, p 613–629 |
| Talatahari S, Azizi M | 2021 | Chaos game optimization: a novel metaheuristic algorithm | Artif Intell Rev 54(2):917–1004 |
| Talatahari S, Azizi M, Gandomi AH | 2021 | Material generation algorithm: A novel metaheuristic algorithm for optimization of engineering problems | Processes 9(5):859 |
| Talatahari S, Azizi M, Tolouei M et al | 2021 | Crystal structure algorithm (crystal): A metaheuristic optimization method | IEEE Access 9:71,244-71,261 |
| Talbi EG | 2009 | Metaheuristics: from design to implementation | Vol 74. Wiley, Hoboken |
| Tamura K, Yasuda K | 2011 | Primary study of spiral dynamics inspired optimization | IEEJ Trans Electr Electron Eng 6(S1):S98–S100 |
| Tan KC, Feng L, Jiang M | 2021 | Evolutionary transfer optimization-a new frontier in evolutionary computation research | IEEE Comput Intell Mag 16(1):22–33 |
| Tang D, Dong S, Jiang Y et al | 2015 | Itgo: Invasive tumor growth optimization algorithm | Appl Soft Comput 36:670–698 |
| Tang R, Fong S, Yang XS, et al | 2012 | Wolf search algorithm with ephemeral memory | In: Seventh International Conference on Digital Information Management (ICDIM 2012), IEEE, pp 165–172 |
| Tang W, Wu Q, Saunders J | 2007 | A bacterial swarming algorithm for global optimization | In: 2007 IEEE Congress on Evolutionary Computation, IEEE, pp 1207–1212 |
| Tanyildizi E, Demir G | 2017 | Golden sine algorithm: A novel math-inspired algorithm | Advances in Electrical and Computer Engineering 17(2):71–79 |
| Tan Y, Zhu Y | 2010 | Fireworks algorithm for optimization | In: International Conference in Swarm Intelligence, Springer, pp 355–364 |
| Taramasco C, Crawford B, Soto R et al | 2020 | A new metaheuristic based on vapor-liquid equilibrium for solving a new patient bed assignment problem | Expert Syst Appl 158(113):506 |
| Tayarani-N MH, Akbarzadeh-T M | 2008 | Magnetic optimization algorithms a new synthesis | In: 2008 IEEE Congress on Evolutionary Computation (IEEE World Congress on Computational Intelligence), IEEE, pp 2659–2664 |
| Tayeb FBS, Bessedik M, Benbouzid M et al | 2017 | Research on permutation flow-shop scheduling problem based on improved genetic immune algorithm with vaccinated offspring | Procedia Computer Science 112:427–436 |
| Teodorovic D, Dell’Orco M | 2005 | Bee colony optimization-a cooperative learning approach to complex transportation problems | Advanced OR and AI Methods in Transportation 51:60 |
| Thammano A, Moolwong J | 2010 | A new computational intelligence technique based on human group formation | Expert Syst Appl 37(2):1628–1634 |
| Tilahun SL, Ong HC | 2015 | Prey-predator algorithm: a new metaheuristic algorithm for optimization problems | International Journal of Information Technology & Decision Making 14(06):1331–1352 |
| Ting T, Man KL, Guan SU, et al | 2012 | Weightless swarm algorithm (wsa) for dynamic optimization problems | In: IFIP International Conference on Network and Parallel Computing, Springer, pp 508–515 |
| Torabi M, Yaghoobi H, Fereidoon A | 2012 | Application of differential transformation method and padé approximant for the glauert-jet problem | Recent Patents on Mechanical Engineering 5(2):150–155 |
| Tran TH, Ng KM | 2011 | A water-flow algorithm for flexible flow shop scheduling with intermediate buffers | J Sched 14(5):483–500 |
| Trojovská E, Dehghani M | 2022 | A new human-based metahurestic optimization method based on mimicking cooking training | Sci Rep 12(1):1–24 |
| Trojovskỳ P, Dehghani M | 2022 | A new optimization algorithm based on mimicking the voting process for leader selection | PeerJ Computer Science 8:e976 |
| Trojovskỳ P, Dehghani M | 2022 | Pelican optimization algorithm: A novel nature-inspired algorithm for engineering applications | Sensors 22(3):855 |
| Tsai HC, Lin YH | 2011 | Modification of the fish swarm algorithm with particle swarm optimization formulation and communication behavior | Appl Soft Comput 11(8):5367–5374 |
| Tsai CW, Cho HH, Shih TK et al | 2015 | Metaheuristics for the deployment of 5g | IEEE Wirel Commun 22(6):40–46 |
| Tychalas D, Karatza H | 2021 | Samw: a probabilistic meta-heuristic algorithm for job scheduling in heterogeneous distributed systems powered by microservices | Cluster Computing pp 1–25 |
| Tzanetos A, Dounias G | 2021 | Nature inspired optimization algorithms or simply variations of metaheuristics? | Artif Intell Rev 54(3):1841–1862 |
| Tzanetos A, Dounias G | 2017 | A new metaheuristic method for optimization: sonar inspired optimization | In: International Conference on Engineering Applications of Neural Networks, Springer, pp 417–428 |
| Uymaz SA, Tezel G, Yel E | 2015 | Artificial algae algorithm (aaa) for nonlinear global optimization | Appl Soft Comput 31:153–171 |
| Valsecchi A, Damas S, Santamaría J | 2012 | An image registration approach using genetic algorithms | In: 2012 IEEE Congress on Evolutionary Computation, IEEE, pp 1–8 |
| Veysari EF et al | 2022 | A new optimization algorithm inspired by the quest for the evolution of human society: human felicity algorithm | Expert Syst Appl 193(116):468 |
| Vicsek T, Czirók A, Ben-Jacob E et al | 1995 | Novel type of phase transition in a system of self-driven particles | Phys Rev Lett 75(6):1226 |
| Villalón CLC, Stützle T, Dorigo M | 2020 | Grey wolf, firefly and bat algorithms: Three widespread algorithms that do not contain any novelty | In: International Conference on Swarm Intelligence, Springer, pp 121–133 |
| Wagan AI, Shaikh MM et al | 2020 | A new metaheuristic optimization algorithm inspired by human dynasties with an application to the wind turbine micrositing problem | Appl Soft Comput 90(106):176 |
| Wang GG, Deb S, Coelho LdS | 2015 | Elephant herding optimization | In: 2015 3rd International Symposium on Computational and Business Intelligence (ISCBI), IEEE, pp 1–5 |
| Wang GG, Gao XZ, Zenger K, et al | 2018b | A novel metaheuristic algorithm inspired by rhino herd behavior | In: Proceedings of the 9th EUROSIM Congress on Modelling and Simulation, EUROSIM 2016, the 57th SIMS Conference on Simulation and Modelling SIMS 2016, Linköping University Electronic Press, pp 1026–1033 |
| Wang GG (2018) | 2018 | Moth search algorithm: a bio-inspired metaheuristic algorithm for global optimization problems | Memetic Computing 10(2):151–164 |
| Wang GG, Tan Y | 2017 | Improving metaheuristic algorithms with information feedback models | IEEE Transactions on Cybernetics 49(2):542–555 |
| Wang J, Wang D | 2008 | Particle swarm optimization with a leader and followers | Prog Nat Sci 18(11):1437–1443 |
| Wang TH, Chang YL, Peng HH et al | 2005 | Rapid detection of fetal aneuploidy using proteomics approaches on amniotic fluid supernatant | Prenatal Diagnosis: Published in Affiliation With the International Society for Prenatal Diagnosis 25(7):559–566 |
| Wang M, Li B, Zhang G et al | 2017 | Population evolvability: Dynamic fitness landscape analysis for population-based metaheuristic algorithms | IEEE Trans Evol Comput 22(4):550–563 |
| Wang GG, Deb S, Coelho LDS | 2018 | Earthworm optimisation algorithm: a bio-inspired metaheuristic algorithm for global optimisation problems | International Journal of Bio-Inspired Computation 12(1):1–22 |
| Wang L, Shen J, Yong J | 2012 | A survey on bio-inspired algorithms for web service composition | In: 2012 IEEE Conference on Computer Supported Cooperative Work in Design, IEEE, pp 569–574 |
| Wang T, Yang L | 2018 | Beetle swarm optimization algorithm: Theory and application | arXiv preprint arXiv:1808.00206 |
| Wang P, Zhu Z, Huang S | 2013 | Seven-spot ladybird optimization: a novel and efficient metaheuristic algorithm for numerical optimization | The Scientific World Journal 2013 |
| Wedde HF, Farooq M, Zhang Y | 2004 | Beehive: An efficient fault-tolerant routing algorithm inspired by honey bee behavior | In: International Workshop on Ant Colony Optimization and Swarm Intelligence, Springer, pp 83–94 |
| Wedyan A, Whalley J, Narayanan A | 2017 | Hydrological cycle algorithm for continuous optimization problems | Journal of Optimization 2017 |
| Weibo W, Quanyuan F, Yongkang Z | 2008 | A novel particle swarm optimization algorithm with stochastic focusing search for real-parameter optimization | In: 2008 11th IEEE Singapore International Conference on Communication Systems, IEEE, pp 583–587 |
| Wei Z, Cui Z, Zeng J | 2010 | Social cognitive optimization algorithm with reactive power optimization of power system | In: 2010 International Conference on Computational Aspects of Social Networks, IEEE, pp 11–14 |
| Weyland D | 2010 | A rigorous analysis of the harmony search algorithm: How the research community can be misled by a "novel" methodology | International Journal of Applied Metaheuristic Computing 1(2):50–60 |
| Wolpert DH, Macready WG | 1997 | No free lunch theorems for optimization | IEEE Trans Evol Comput 1(1):67–82 |
| Wu G | 2016 | Across neighborhood search for numerical optimization | Information Sciences 329:597 – 618. Special issue on Discovery Science |
| Wu SX, Banzhaf W | 2010 | A hierarchical cooperative evolutionary algorithm | In: Proceedings of the 12th Annual Conference on Genetic and Evolutionary Computation, pp 233–240 |
| Xavier AE, Xavier VL | 2016 | Flying elephants: a general method for solving non-differentiable problems | Journal of Heuristics 22(4):649–664 |
| Xie XF, Zhang WJ, Yang ZL | 2002 | Social cognitive optimization for nonlinear programming problems | In: Proceedings. International Conference on Machine Learning and Cybernetics, IEEE, pp 779–783 |
| Xie L, Han T, Zhou H, et al | 2021 | Tuna swarm optimization: A novel swarm-based metaheuristic algorithm for global optimization | Computational Intelligence and Neuroscience 2021 |
| Xie L, Zeng J, Cui Z | 2009 | General framework of artificial physics optimization algorithm | In: 2009 World Congress on Nature & Biologically Inspired Computing (NaBIC), IEEE, pp 1321–1326 |
| Xu J, Xu L | 2021 | Optimal stochastic process optimizer: A new metaheuristic algorithm with adaptive exploration-exploitation property | IEEE Access 9:108,640-108,664 |
| Xu X, Hu Z, Su Q et al | 2020 | Multivariable grey prediction evolution algorithm: a new metaheuristic | Appl Soft Comput 89(106):086 |
| Xu Y, Cui Z, Zeng J | 2010 | Social emotional optimization algorithm for nonlinear constrained optimization problems | In: International Conference on Swarm, Evolutionary, and Memetic Computing, Springer, pp 583–590 |
| Yadav A et al | 2019 | Aefa: Artificial electric field algorithm for global optimization | Swarm Evol Comput 48:93–108 |
| Yampolskiy RV, El-Barkouky A | 2011 | Wisdom of artificial crowds algorithm for solving np-hard problems | International Journal of Bio-Inspired Computation 3(6):358–369 |
| Yang XS, Deb S | 2009 | Cuckoo search via lévy flights | In: 2009 World Congress on Nature & Biologically Inspired Computing (NaBIC), IEEE, pp 210–214 |
| Yang XS, Deb S | 2010 | Eagle strategy using lévy walk and firefly algorithms for stochastic optimization | In: Nature Inspired Cooperative Strategies for Optimization. Springer, p 101–111 |
| Yang XS, Lees JM, Morley CT | 2006 | Application of virtual ant algorithms in the optimization of cfrp shear strengthened precracked structures | In: International Conference on Computational Science, Springer, pp 834–837 |
| Yang XS | 2005 | Engineering optimizations via nature-inspired virtual bee algorithms | In: International Work-Conference on the Interplay Between Natural and Artificial Computation, Springer, pp 317–323 |
| Yang XS | 2009 | Firefly algorithms for multimodal optimization | In: International symposium on stochastic algorithms, Springer, pp 169–178 |
| Yang XS | 2010b | A new metaheuristic bat-inspired algorithm | In: Nature Inspired Cooperative Strategies for Optimization. Springer, p 65–74 |
| Yang XS | 2012 | Flower pollination algorithm for global optimization | In: International Conference on Unconventional Computing and Natural Computation, Springer, pp 240–249 |
| Yang XS | 2018 | Mathematical analysis of nature-inspired algorithms | In: Nature-Inspired Algorithms and Applied Optimization. Springer, p 1–25 |
| Yang XS | 2010 | Engineering optimization: an introduction with metaheuristic applications | Wiley, Hoboken |
| Yang XS | 2020 | Nature-inspired optimization algorithms | Academic Press, Boca Raton |
| Yang XS, He X | 2013 | Bat algorithm: literature review and applications | International Journal of Bio-Inspired Computation 5(3):141–149 |
| Yang FC, Wang YP | 2007 | Water flow-like algorithm for object grouping problems | Journal of the Chinese Institute of Industrial Engineers 24(6):475–488 |
| Yang C, Tu X, Chen J | 2007 | Algorithm of marriage in honey bees optimization based on the wolf pack search | In: 2007 IEEE Conference on Intelligent Pervasive Computing, IEEE, pp 462–467 |
| Yapici H, Cetinkaya N | 2019 | A new meta-heuristic optimizer: pathfinder algorithm | Appl Soft Comput 78:545–568 |
| Yazdani M, Jolai F | 2016 | Lion optimization algorithm (loa): a nature-inspired metaheuristic algorithm | Journal of Computational Design and Engineering 3(1):24–36 |
| Zaeimi M, Ghoddosian A | 2020 | Color harmony algorithm: an art-inspired metaheuristic for mathematical function optimization | Soft Comput 24(16):12,027-12,066 |
| Zamani H, Nadimi-Shahraki MH, Gandomi AH | 2022 | Starling murmuration optimizer: A novel bio-inspired algorithm for global and engineering optimization | Comput Methods Appl Mech Eng 392(114):616 |
| Zarand G, Pazmandi F, Pál K et al | 2002 | Using hysteresis for optimization | Phys Rev Lett 89(15):150,201 |
| Zeidabadi FA, Dehghani M, Trojovskỳ P et al | 2022 | Archery algorithm: A novel stochastic optimization algorithm for solving optimization problems | Computers, Materials and Continua 72(1):399–416 |
| Zelinka I | 2004 | Soma-self-organizing migrating algorithm | In: New optimization techniques in engineering. Springer, p 167–217 |
| Zelinka I | 2015 | A survey on evolutionary algorithms dynamics and its complexity-mutual relations, past, present and future | Swarm Evol Comput 25:2–14 |
| Zhang LM, Dahlmann C, Zhang Y | 2009 | Human-inspired algorithms for continuous function optimization | In: 2009 IEEE International Conference on Intelligent Computing and Intelligent Systems, IEEE, pp 318–321 |
| Zhang Y, Jin Z | 2020 | Group teaching optimization algorithm: A novel metaheuristic method for solving global optimization problems | Expert Syst Appl 148(113):246 |
| Zhang Q, Li H | 2007 | Moea/d: A multiobjective evolutionary algorithm based on decomposition | IEEE Trans Evol Comput 11(6):712–731 |
| Zhang H, Liu S, Moraca S et al | 2017 | An effective use of hybrid metaheuristics algorithm for job shop scheduling problem | International Journal of Simulation Modelling 16(4):644–657 |
| Zhang Q, Wang R, Yang J et al | 2017 | Collective decision optimization algorithm: A new heuristic optimization method | Neurocomputing 221:123–137 |
| Zhang J, Xiao M, Gao L et al | 2018 | Queuing search algorithm: A novel metaheuristic algorithm for solving engineering optimization problems | Appl Math Model 63:464–490 |
| Zhang Q, Wang R, Yang J et al | 2019 | Biology migration algorithm: a new nature-inspired heuristic methodology for global optimization | Soft Comput 23(16):7333–7358 |
| Zhang J, Huang Y, Ma G et al | 2021 | Mixture optimization for environmental, economical and mechanical objectives in silica fume concrete: A novel frame-work based on machine learning and a new metaheuristic algorithm | Resour Conserv Recycl 167(105):395 |
| Zhang X, Chen W, Dai C | 2008 | Application of oriented search algorithm in reactive power optimization of power system | In: 2008 Third International Conference on Electric Utility Deregulation and Restructuring and Power Technologies, IEEE, pp 2856–2861 |
| Zhang X, Sun B, Mei T, et al | 2010 | Post-disaster restoration based on fuzzy preference relation and bean optimization algorithm | In: 2010 IEEE Youth Conference on Information, Computing and Telecommunications, IEEE, pp 271–274 |
| Zhao J, Tang D, Liu Z et al | 2020 | Spherical search optimizer: a simple yet efficient meta-heuristic approach | Neural Comput Appl 32(13):9777–9808 |
| Zhao W, Wang L, Zhang Z | 2020 | Artificial ecosystem-based optimization: a novel nature-inspired metaheuristic algorithm | Neural Comput Appl 32(13):9383–9425 |
| Zhao S, Zhang T, Ma S et al | 2022 | Dandelion optimizer: A nature-inspired metaheuristic algorithm for engineering applications | Eng Appl Artif Intell 114(105):075 |
| Zhao W, Wang L, Mirjalili S | 2022 | Artificial hummingbird algorithm: A new bio-inspired optimizer with its engineering applications | Comput Methods Appl Mech Eng 388(114):194 |
| Zhao Z, Cui Z, Zeng J, et al | 2011 | Artificial plant optimization algorithm for constrained optimization problems | In: 2011 Second International Conference on Innovations in Bio-Inspired Computing and Applications, IEEE, pp 120–123 |
| ZhaoHui C, HaiYan T | 2010 | Notice of retraction: cockroach swarm optimization | In: 2010 2nd International Conference on Computer Engineering and Technology, IEEE, pp V6–652 |
| Zheng YJ | 2015 | Water wave optimization: a new nature-inspired metaheuristic | Computers & Operations Research 55:1–11 |
| Zheng M, Gx L, Cg Z et al | 2010 | Gravitation field algorithm and its application in gene cluster | Algorithms for Molecular Biology 5(1):32 |
| Zheng YJ, Ling HF, Xue JY | 2014 | Ecogeography-based optimization: enhancing biogeography-based optimization with ecogeographic barriers and differentiations | Computers & Operations Research 50:115–127 |
| Zhong C, Li G, Meng Z | 2022 | Beluga whale optimization: A novel nature-inspired metaheuristic algorithm | Knowledge-Based Systems p 109215 |
| Zhou Y, Luo Q, Liu J | 2014 | Glowworm swarm optimization for dispatching system of public transit vehicles | Neural Process Lett 40(1):25–33 |
| Zhu C, Ni J | 2012 | Cloud model-based differential evolution algorithm for optimization problems | In: 2012 Sixth International Conference on Internet Computing for Science and Engineering, IEEE, pp 55–59 |
| Zitouni F, Harous S, Belkeram A, et al | 2021 | The archerfish hunting optimizer: a novel metaheuristic algorithm for global optimization | arXiv preprint arXiv:2102.02134 |
| Zong_yuan ZYM | 2003 | A new search algorithm for global optimization: Population migration algorithm | Journal of South China University of Technology (Natural Science) 3 |
| Zou F, Chen D, Liu H et al | 2022 | A survey of fitness landscape analysis for optimization | Neurocomputing 503:129–139 |
| Zungeru AM, Ang LM, Seng KP | 2012 | Termite-hill: Performance optimized swarm intelligence based routing algorithm for wireless sensor networks | J Netw Comput Appl 35(6):1901–1917 |