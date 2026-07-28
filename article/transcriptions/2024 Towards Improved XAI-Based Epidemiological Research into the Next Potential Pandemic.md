# Towards Improved XAI-Based Epidemiological Research into the Next Potential Pandemic

*Systematic Review*

## Towards Improved XAI-Based Epidemiological Research into the Next Potential Pandemic

**Hamed Khalili** * and **Maria A. Wimmer**

Research Group E-Government, Faculty of Computer Science, University of Koblenz, D-56070 Koblenz, Germany;  
wimmer@uni-koblenz.de  
\* Correspondence: hamedkhalili@uni-koblenz.de

**Abstract:** By applying AI techniques to a variety of pandemic-relevant data, artificial intelligence (AI) has substantially supported the control of the spread of the SARS-CoV-2 virus. Along with this, epidemiological machine learning studies of SARS-CoV-2 have been frequently published. While these models can be perceived as precise and policy-relevant to guide governments towards optimal containment policies, their black box nature can hamper building trust and relying confidently on the prescriptions proposed. This paper focuses on interpretable AI-based epidemiological models in the context of the recent SARS-CoV-2 pandemic. We systematically review existing studies, which jointly incorporate AI, SARS-CoV-2 epidemiology, and explainable AI approaches (XAI). First, we propose a conceptual framework by synthesizing the main methodological features of the existing AI pipelines of SARS-CoV-2. Upon the proposed conceptual framework and by analyzing the selected epidemiological studies, we reflect on current research gaps in epidemiological AI toolboxes and how to fill these gaps to generate enhanced policy support in the next potential pandemic.

**Keywords:** AI; SARS-CoV-2; epidemiology; interpretable machine learning; explainable machine learning; interpretable deep learning; explainable deep learning; non-pharmaceutical interventions

**Citation:** Khalili, H.; Wimmer, M.A. Towards Improved XAI-Based Epidemiological Research into the Next Potential Pandemic. *Life* **2024**, *14*, 783. https://doi.org/10.3390/life14070783

Academic Editors: Antonio Caputi and Jaroslaw Walory

Received: 25 May 2024  
Revised: 16 June 2024  
Accepted: 19 June 2024  
Published: 21 June 2024

**Copyright:** © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

---

## 1. Introduction

The application of artificial intelligence (AI), especially machine learning and deep learning models, has been evidenced in a variety of research areas such as computer vision, robotics, epidemiology, medical imaging, etc., as one of the most powerful approaches to contain the spread of the SARS-CoV-2 pandemic [1]. While the excellence of AI models in terms of their accuracy and performances is broadly admitted, the results and prescriptions made based on these models are not always as transparent as required [2]. In other words, despite being highly accurate, AI models are not sufficiently interpretable (or explainable). Miller defines interpretability as “the degree to which a human can understand the cause of a decision” [2]. The terms explainability and interpretability are often used interchangeably. Explainability is also referred to in the literature as interpretability, intelligibility, causability, or understandability [3].

In recent research, explainable artificial intelligence (XAI) has received high attention to address interpretability. The goal of XAI is to understand and explain the corresponding processes behind the algorithms, which lead to the generated predictions of the AI models [3–8].

In AI studies of the SARS-CoV-2 pandemic, XAI remains one of the main concerns, especially with regard to medical AI systems [9], as AI-based medical diagnoses are directly linked to human lives. While the significance of XAI in healthcare systems is self-evident, the substantial role XAI may play in AI-based and data-driven generation of government policies in pandemic circumstances is a noticeable subject as well [10].

Figure 1 shows an example of a basic AI-powered recommendation system to contain the SARS-CoV-2 pandemic, researched within the “AI and COVID project”. The system uses three types of databases: (a) Publicly available information on the global status of the pandemic and historical data on measures and their impacts (primary pandemic data), (b) region-specific information on population and demographic characteristics (secondary pandemic data), and (c) information about the current status of available healthcare personnel and resources (internal data). By developing AI-supported methods and taking into account the current knowledge base, recommendations for actions are developed and communicated to the key pandemic-relevant target groups, including political decision-makers, health authorities, and citizens. The impact of the proposed policy measures, e.g., pharmaceutical interventions (PIs) and non-pharmaceutical interventions (NPIs), behavioral changes, and knowledge gained are then stored back into the primary pandemic databases for use in the next phase of the pandemic.

## Figure 1

**Figure 1.** Motivation of applying XAI to influence the understandability of AI at policy level along the overall AI and COVID approach (https://covid-ai.uni-koblenz.de/, accessed on 20 June 2024).

### PlantUML approximation

```plantuml
@startuml
top to bottom direction

rectangle "Data Sources" {
  database "Primary data" as primary
  database "Secondary data" as secondary
  database "Internal data" as internal
}

rectangle "AI Methods" as aim {
  circle "Machine\nLearning" as ml
  circle "Feature\nEmbedding" as fe
  circle "Data\nAnalytics" as da
  rectangle "XAI-supported\nAction Recommendation" as xai
  database "Knowledge\nBasis" as kb
}

rectangle "Stakeholders" {
  actor "People" as people
  actor "Policy makers" as policy
  actor "Health-care actors" as health
}

primary --> aim
secondary --> aim
internal --> aim

ml --> xai
fe --> xai
da --> xai
kb <--> xai

xai --> people
xai --> policy
xai --> health

people ..> primary : Effects of measures\nand behavioral changes\nas well as knowledge gained
@enduml
```

XAI makes it possible to transparently present the significance and magnitude of the recommended measures for the target actors mentioned above. In particular, in the presence of XAI, the policy level can see the evidence of the results achieved at the level of AI development and trust the proposed policies.

In addition, system developers can also benefit from the use of XAI at the AI development level. XAI enables system developers to take a look at the internal workings of AI-based algorithms and helps them eliminate potential pitfalls (e.g., misunderstandings of semantics and syntax errors) that arise at the AI development level and correct the corresponding errors [11].

Identifying the main methodological gaps in the AI pipelines of epidemiology remains important to develop enhanced epidemiological XAI toolboxes for the next potential epidemics. In order to develop a comprehensive understanding, our objective in this paper is to systematically review the existing literature in the field and to figure out the main research gaps on XAI and AI-based epidemiological pipelines of the recent SARS-CoV-2 pandemic. The insights obtained from our review serve as a guide for expanding the methodological toolbox in AI-based epidemiology. The following research questions (RQs) drive this study:

- **RQ 1:** What is the current state of research on XAI applied to the recent pandemic, and what research gaps exist?
- **RQ 2:** What would be a suitable conceptual framework to systematically analyze the main methodological features of interpretable machine learning pipelines on SARS-CoV-2 data?
- **RQ 3:** What further research is required to boost the development of explainable AI models of epidemiology?

To answer these RQs, the study conducts a systematic literature review by adapting the Preferred Reporting Items for Systematic Reviews and Meta-Analysis (PRISMA) approach [12,13].

The remainder of the paper is as follows. Section 2 details the methodology for the systematic literature reviews in the subsequent Sections 3 and 4. In Section 3, a literature analysis is conducted with the focus of conceptualizing a decent framework of interpretable machine learning pipelines in the context of SARS-CoV-2. Based on the conceptual framework, in Section 4, we focus on the epidemiological AI approaches of SARS-CoV-2 and analyze the set of selected epidemiological papers. Section 5 concludes the paper with a discussion and reflection of future research needs derived from the gaps identified.

---

## 2. Research Methodology

Our study applies the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) approach for literature identification [12]. The process employs four sequential phases: Identification, screening, eligibility, and inclusion. The identification phase is carried out by filtering titles and content in the Google Scholar database. Thereby, we opted for broad coverage by using the search term “COVID” in the title as well as one of the semantically exchangeable search terms “interpretable machine learning”, “interpretable deep learning”, “explainable machine learning” and “explainable deep learning” in the body text (accessed on 10 January 2024). We opted for setting a generally defined search term in the database without primarily specifying any keywords with relation to the “epidemiological” target of our review. This was conducted to minimize the risk of bias in the selection of the final included studies in favor of specified words such as epidemiology, government policy, non-pharmaceutical interventions, etc. The search of the aforementioned four search combinations resulted in a total of 1503 studies. As among the collected papers, 218 studies were duplicates due to coexistence in more than one of the four aforementioned search combinations, the duplicated papers were filtered, and we moved on with 1285 papers in the screening phase.

In the screening phase, an Excel sheet was used to mark each paper with regard to the specific research area (with respect to the methods and results) it belongs to. For the development of the reference framework for interpretable machine learning pipelines on SARS-CoV-2 data, the 1285 papers were the basis. We particularly scanned the studies for the main methods of data processing and ML processing pipelines. This resulted in 325 papers that deal with different methodological features. Through tabular evaluation, we analyzed these papers to synthesize the information with regard to the six steps for our conceptual framework. A tabular representation of the papers is presented in the paper’s Supplementary Material. The results of the synthesis are described in Section 3 along with the conceptualized reference framework of the pipeline. This reference framework was applied to identify both the potentials and limitations of the narrowed scope of epidemiological AI research in the SARS-CoV-2 context elaborated in Section 4.

To narrow the vast amount of literature for Section 4, more than seven research areas were identified to group the studies. A subset of identified papers included 328 papers related to X-ray and CT imaging classification methods. 196 papers addressed SARS-CoV-2 diagnosis approaches based on clinical markers (i.e., blood tests, patient symptoms etc.). 62 papers tackled psychology and language understanding. Further 611 papers were grouped into the miscellaneous area. While, within this miscellaneous group, we identified 188 articles that conducted reviews of literature in the scope of AI research and SARS-CoV-2 epidemiology from different perspectives, none of these studies have focused on the same objective as our study, i.e., jointly incorporating AI, SARS-CoV-2 epidemiology, and XAI. We therefore did not include these papers in our further consideration for the latter analysis of epidemiological AI research with XAI. 88 studies were assigned to the epidemiological category to be further considered in our targeted group of relevant studies in Section 4.

Next, we further screened the eligibility of the 88 epidemiological studies as the main study target with the following three inclusion rules: (a) Being a peer-reviewed journal paper, (b) using at least one ML model rather than statistical regression models in the paper, and (c) that the paper applies XAI in the pipeline. By stepwise filtering based on the three inclusion rules, we finally included 26 papers, which are further categorized and explored in more detail in Section 4 of this paper. Figure 2 presents the flowchart for selecting the papers for the epidemiological AI research in Section 4 based on the PRISMA 2020 flow diagram for new systematic reviews [12,13].

## Figure 2

**Figure 2.** Study search and selection process for literature on epidemiological AI research based on the PRISMA template [13]. The dashed lines and dashed squares are added to elucidate the selection process of included studies reviewed in Section 3.

### PlantUML approximation

```plantuml
@startuml
top to bottom direction
skinparam shadowing false

rectangle "Identification of studies via databases and registers" as title

rectangle "Records identified from Google Scholar :\nintitle:covid intext:\"interpretable machine learning\" (n =459)\nintitle:covid intext:\"explainable machine learning\" (n =354)\nintitle:covid intext:\"interpretable deep learning\" (n=144)\nintitle:covid intext:\"explainable deep learning\" (n=564)" as r1

rectangle "Records removed before screening:\nDuplicate records removed (n =218)" as r2

rectangle "Records screened\n(n =1285)" as r3

rectangle "Records excluded to be reviewed in section 4:\nX-ray imaging (n =227)\nClinical markers (n =196)\nCT imaging (n=101)\nPsychology (n=32)\nLanguage understanding (n=30)\nMiscellaneous (n=611)" as r4

rectangle "Records sought for retrieval\n(n =88)" as r5
rectangle "Records not retrieved\n(n =0)" as r6
rectangle "Records assessed for eligibility\n(n =88)" as r7

rectangle "Records excluded:\nNot peer reviewed paper (n =33)\nNot Machine learning approach (n =18)\nNot XAI approach(n =11)" as r8

rectangle "Studies included in review in section 4\n(n =26)" as r9

rectangle "Studies included in review in section 3\n(n =325)" as r10
rectangle "Records excluded:\nMiscellaneous (n=611)\nNot methodological relevant (n=349)" as r11

title --> r1
r1 --> r2
r1 --> r3
r3 --> r4
r3 --> r5
r5 --> r6
r5 --> r7
r7 --> r8
r7 --> r9
r11 ..> r10
r4 ..> r11
@enduml
```

---

## 3. Literature Review on XAI Pipelines of SARS-CoV-2 and Reference Framework for the Subsequent Epidemiological Study

In this section, we review the existing literature with regard to XAI applied in the identified SARS-CoV-2 literature. The objective is to conceptualize a reference framework for studying XAI pipelines of SARS-CoV-2 for synthesizing the main methodological features in Section 4. The proposed reference framework (Figure 3) entails the main steps of Severn et al.’s approach, i.e., process data, build prediction models, and explain prediction model sub-pipelines for explainable machine learning models [14]. However, we followed a more fine-grained and adjusted set of steps as shown in Figure 3: Data preprocessing, feature engineering, parameter tuning, model training, model evaluation, and model explanation (XAI). This more detailed pipeline is extracted from the literature analysis and is described below along the individual steps.

## Figure 3

**Figure 3.** A conceptual reference framework of ML pipelines in the context of SARS-CoV-2.

### PlantUML

```plantuml
@startuml
left to right direction

rectangle "Data Preprocessing\n• Missing data\n• Unbalanced data\n• Sparse data" as dp
rectangle "Feature Engineering\n• Feature selection\n• Feature extraction" as fe
rectangle "Parameter Tuning\n• Exhaustive search\n• Non exhaustive search" as pt

rectangle "Model Training\n• Basic model\n• Hybrid model\n• Ensemble model" as mt
rectangle "Model Evaluation\n• Continuous output\n• Classification output" as me
rectangle "Model Explanation\n• Model agnostic\n• Model specific" as mx

dp --> fe
fe --> pt
pt --> mt
mt --> me
me --> mx
@enduml
```

### 3.1. Data Preprocessing

The Data Preprocessing step handles missing, unbalanced and sparse data.

#### 3.1.1. Missing Data

Missing data can cause concerns not only to the model’s precision but, furthermore, to the interpretation of the achieved output. While missing data values are inherently handled by some techniques, e.g., gradient-boosting predictors [15], these remain a basic problem on top of the pipeline in numerous studies. The lack of enough data hampers the prediction accuracy of SARS-CoV-2 cases, while having larger datasets can lead to improved results [16]. As the amount of data increases, the epistemic uncertainty related to the model decreases [17]. In contrast, the problem of lacking data is amplified when facing problems with a large number of inputs. Docquier et al. show how the inclusion of extra parameters (to incorporate day-specific effects—i.e., 366 day-specific time dummies) in their models deteriorates the predictive power of the ML model. The authors conclude that, given a dataset, the gains from adding information are indeed outbalanced by the costs linked to the inflated dimensionality of the AI computation problem [18]. Hinns et al. study XAI generated by various predictors on a dataset and show how inconsistent model interpretations emerge among a set of random data sub-sets when using little data, and that by increasing the size of the data, interpretations of the random data subsets converge towards each other [19]. Andonov, Ulm, and Graessner show how a sudden shift in the input data impacts the performances of AI models as well as the explanation of the models [20].

To combat missing data, in the context of SARS-CoV-2 studies, the k-nearest-neighbor algorithm (KNN) is frequently used [21] to impute the missing values in the dataset. By trying to compare an unlabeled data point to the training dataset, the KNN finds the K most related data points. Thereby, a metric that measures distance, such as Euclidean or Manhattan distance, is utilized to determine proximity. This technique then assigns the given data point to the most familiar class [22]. Another possible imputation approach is the usage of generative adversarial neural networks (GANN), which learn to generate “missing” data with the same distribution as the training set. This is performed by training a “generative” network, which generates possible imputed values and proposes them to a “discriminative” network, which is trained to accept only those generated values that properly fill the missing ones according to the underlying data distribution [23].

#### 3.1.2. Unbalanced Data

Unbalanced data can lead the model’s performance to be biased in favor of the classes or ranges of outputs, which are overrepresented. The unbalanced data is often handled by the Synthetic Minority Oversampling Technique algorithm (SMOTE) [24]. SMOTE works based on identifying the k-nearest neighbors’ principle and deploys the principles of interpolation [25]. It creates synthetic data that is close to the minority class to oversample the minority class in the feature space [26,27]. To handle the problem of unbalanced data, other alternatives exist, such as data partitioning (i.e., utilizing dichotomous variables). Discretizing the variable spaces will not necessarily worsen the model performance in all circumstances to a large extent. For instance, Wendland et al. show that models using only dichotomous features perform only slightly worse than models based on a complex combination of numerical input values [28]. Another way of managing unbalanced data is during the training step. In [29], during the fitting procedure, the unbalancing issue is tackled by penalizing the misclassification of the minority class with a multiplicative factor inversely proportional to the class frequencies. Hu et al. propose a novel self-adaptive auxiliary loss to help the training with imbalanced data [30]. The self-adaptive factor reflects the feature distribution and emphasizes the minority class. Also, other data imputation methods are used in the SARS-CoV-2 literature based on decision trees, e.g., isolation forest [31], miss forest [32], and random forest [33]. The range of possible data imputation techniques is not restricted to those frequently used. For example, predictive mean matching to impute numeric features, logistic regression to impute binary variables, and Bayesian polytomous regression to impute factor features are used in [34]. In addition, Abbasimehr, Paki, and Bahrini present a time series augmentation technique to create new time series with the same temporal dependencies that exist in the original time series data [35].

#### 3.1.3. Sparse Data

To resolve the generic problem of sparse training data, generative networks (GANs) are applied in studies to generate ample synthetic training data [36–38]. With limited data in the SARS-CoV-2 context, synthetic data is generated using the auto encoder (AE) methods [39–41]. AEs belong to the realm of unsupervised learning, as they do not need labeled data for their training. The process consists of providing labeled sample data to the encoder, which captures the distribution of the deep feature, and the decoder, which generates data from the deep feature by decompressing the latent space.

### 3.2. Feature Engineering

Feature engineering generally covers feature extraction and feature selection [42]. Whereas feature extraction creates new features, feature selection is about selecting a subset of the original feature set [43]. For feature extraction, two types of methods are distinguished: pre-trained feature extracting and reduced dimensional feature extracting.

#### 3.2.1. Pre-Trained Feature Extracting

As most ML models require inputs in the form of numerical vectors, some feature extraction techniques aim at translating features such as vocabulary [44], images [45], or parts of speech into numerical representations. This is performed in most image recognition studies [46] as well as natural language processing studies [44] by means of pre-trained deep learning models. The pre-trained model acts as an early feature extractor, usually followed by a fine-tuning step [47]. Subsequently, a downstream classification step is executed in many cases [48].

The upstream part of an ML pipeline can comprise the translation of, e.g., text and image in both directions to extract desired features. For example, Shang et al. utilize a text-guided visual feature generator to generate visual features from the news text as well as an image-guided textual feature decoder to generate the corresponding textual features from the news image [49].

#### 3.2.2. Reduced Dimensional Feature Extraction

Feature extraction techniques can also aim at learning the reduced structure of the data by finding a low-dimensional embedding representation that preserves the essential structure of the data. For this, a variety of algorithms are applied in the context of the SARS-CoV-2 literature, as summarized in Table 1.

## Table 1

**Table 1.** Overview and short explanation of dimensionality reduction algorithms used in SARS-CoV-2 literature context.

| Method [Source] | Explanation |
|---|---|
| K-Means [50,51] | Clustering algorithms that can detect complex patterns based on a partition system to group data into several clusters |
| PCA—principal component analysis [26,51–53] | A statistical procedure, which relies on linear transformation for reducing the dimensionality of datasets while preserving crucial information |
| AE—auto encoders [40] | Perform dimensionality reduction similar to PCA. However, unlike PCA, which relies on linear transformation, AEs carry out non-linear transformation using deep neural networks |
| SOM—self-organizing maps [54,55] | Is an unsupervised machine learning technique to cluster the high-dimensional data into low-dimensional outputs consisting of a similar structure like artificial neural networks (ANNs), with the difference that the organizing maps in SOM use competitive learning whereas the ANNs use error correction learning such as back-propagation with gradient descent |
| LDA—Latent Dirichlet Allocation [56] | Is a Bayesian unsupervised clustering method that is often employed to cluster topics of a set of documents in each cluster |
| t-SNE—t-stochastic neighborhood embedding [57] | Is a kind of unsupervised non-linear embedding dimensionality reduction: It embeds the points from a higher dimension to a lower dimension trying to preserve the local structure of data |
| UMAP—uniform manifold approximation and projection [58,59] | Is a flexible non-linear dimension reduction algorithm based on Riemannian geometry and algebraic topology to learn the manifold structure of the data and find a low dimensional embedding that preserves the essential topological structure of that manifold |
| RFF—Random Fourier Features [60] | An approximate kernel method, which maps the given data to a low dimensional randomized feature space based on Euclidean inner product space |

Docquier, Golenvaux, and Nijssen use a PCA analysis to reduce the dimensionality of the origin- and destination-specific containment measures, extract the first two components of the PCA, and propose that the first PCA component can be interpreted as an average index of the stringency of containment measures, and the second component captures testing and tracing policies [18]. Trajanoska, Trajanov, and Eftimov cluster countries with similarly balanced diets using SOM. In addition to presenting the SOM clusters, the authors present an explainable decision map corresponding to the SOM clusters, with squares representing the most dominant feature leading to the decision to cluster the countries [61].

Beside the previously mentioned methods, knowledge graph embedding techniques to encode the entities and relations in a knowledge graph as dense and low-dimensional vector representations are utilized in the literature of SARS-CoV-2 [62,63]. In addition, functional data analysis following the principle of “breaking up the whole into pieces” of big data analysis to transfer discrete and high-frequency sequences of data to continuous smooth functions, treating the whole functions as a single entity with an internal unified structure, is used in the literature [64].

While the above-mentioned techniques for reducing the number of variables can eliminate redundant and irrelevant features, de Paiva, Pereira, and de Andrade argue that it is not always clear whether these methods result in improvements in the predictive power of ML models [65]. Furthermore, as these methods project the features to a new dimension and the features in the new dimension become mixed features, these new features might not necessarily provide a strong explanatory basis [66]. Despite that, some of the aforementioned studies have provided XAI along with the corresponding AI algorithms. For example, [58] constructs discriminative decision rules that identify and differentiate the clusters, forming the explanations of subgroups. Moreover, features with the strongest impact on clustering can be examined by assessing their importance to each emerging cluster through supervised machine learning models and subsequent application of XAI techniques [67].

#### 3.2.3. Feature Selection

Feature selection aims at eliminating irrelevant and redundant features. Irrelevant and redundant features not only increase the computational complexity of a model but also increase the probability of overfitting [68].

Statistical correlation analysis is the first milestone to observe if, e.g., there is a high degree of correlation between multiple independent variables. Finding high correlations between two variables, e.g., the share of the population with cancer and the share of the elderly, is conceivable. After the correlation analysis, such variables can be reduced to continue the investigation with a lower number of representing variables [69]. The factor analysis technique is an alternative statistical method that extracts the maximum common variance from all variables and puts them into a common score. This contributes to identifying latent composite variables, for example, between gross domestic product (GDP) per capita and other development metrics, such as access to electricity [70].

Various statistical methods can contribute to evaluating the association between independent variables and the dependent variables (leading to sorting the priority of influential variables and eliminating the irrelevant ones), including H-statistics [71], Pearson’s correlation analysis [72], chi-square [73], T-test [74], U-test [51], univariate logistic regression [75], etc. While statistical methods can indicate the overall interaction strength of each feature with the other features, they do not convey what the interactions look like. That is what XAI is for.

Next to the statistical approaches, the selection of the feature selection model is often based on training an ML model. This ML model could be identical to the training model at the upcoming stage of the pipeline or not. Various approaches undertake a kind of stepwise wrapping feature selection by removing (or adding) features one by one from (to) a set of features and evaluating the model error (or statistical significance of the added factor) through training the model at the upcoming stage of the pipeline (forward feature addition and backward feature elimination) [69,76].

Alternatively, the selection of the feature selection model can be carried out based on training an ML model and computing the significance of each feature through the subsequent XAI corresponding to the chosen ML model [77,78]. For example, a number of studies utilize the SHAPley value-based explanations (SHAP) concept (see Section 3.6 below on model interpretation) to undertake the task of feature selection in their pipeline [52,79–81].

Beside the above-mentioned categories (i.e., statistical analysis, error-based, and XAI-based feature selection methods) different evolutionary techniques are utilized in the context of SARS-CoV-2 literature for feature selection. Examples are artificial bee colony, ant colony optimization, butterfly optimization algorithm, elephant herding optimization, genetic algorithm, and particle swarm optimization [40,82,83].

An alternative kind of explainable feature selection is proposed by [84] by initializing a weighted graph to comprise features with Pearson similarity criteria for the feature similarities calculation as well as the integration of Fisher score (FS) and the node centrality to determine the score of each feature. That way, the feature selection approach considers not only feature importance but also feature similarity.

Figure 4 portrays an overview of the methods presented in Section 3.2.

## Figure 4

**Figure 4.** Overview of the feature engineering approaches resulted from the SARS-CoV-2 research studied in Section 3.2.

### PlantUML approximation

```plantuml
@startuml
left to right direction

rectangle "Feature Engineering" as FE

rectangle "Feature Selection" as FS
rectangle "Feature Extraction" as FX

FE --> FS
FE --> FX

rectangle "Training Identical or\nSurrogate ML Model" as TISM
rectangle "Graph-based\nFeature Selection" as GFS
rectangle "Evolutionary\nFeature Selection" as EFS
rectangle "Statistical\nCorrelation Analysis" as SCA

FS --> TISM
FS --> GFS
FS --> EFS
FS --> SCA

rectangle "Model XAI" as MXAI
rectangle "Model Error\nEvaluation" as MEE
TISM --> MXAI
TISM --> MEE

rectangle "Feature Importance" as FI
rectangle "Wrapping Method" as WM
MXAI --> FI
MEE --> WM

rectangle "Forward Feature\nAddition" as FFA
rectangle "Backward Feature\nReduction" as BFR
WM --> FFA
WM --> BFR

rectangle "Artificial Bee Colony,\nAnt Colony,\nButterfly Optimization,\nElephant Herding Optimization,\nParticle Swarm Optimization" as EVO
EFS --> EVO

rectangle "Continuous Features" as CF
rectangle "Discrete Features" as DF
SCA --> CF
SCA --> DF

rectangle "T-Test, U-Test" as TU
rectangle "Fisher, Chi-Square" as FC
CF --> TU
DF --> FC

rectangle "Pre-trained\nTransformer-based" as PTT
rectangle "Reduced-\ndimensionality" as RD
rectangle "Graph-based\nFeature Extraction" as GFE
FX --> PTT
FX --> RD
FX --> GFE

rectangle "PCA, SOM, LDA,\nt-SNE, RFF,\nFunctional Data Analysis, AE" as RED
RD --> RED

rectangle "Knowledge\nEmbedding Graph" as KEG
GFE --> KEG
@enduml
```

### 3.3. Model Parameter Tuning

To achieve highly precise results through ML algorithms, various approaches are used to fine-tune the models’ hyper-parameters. The hyper-parameters of DL (deep learning) models, which must be tuned, consist of the number of layers, number of neurons, activation function, learning rate, etc. [72]. For example, Vernikou, Lyras, and Kanavos show that the Bert Tokenizer long short-term memory network (LSTM) model responds better with a very low learning rate [85]. The hyper-parameters to tune in decision tree-based models would comprise the maximum depths of trees and the maximum number of features used in each split. Hyper-parameter tuning is conducted in most pipelines with a grid search algorithm. The grid search algorithm tests all combinations of hyper-parameters and narrows the model parameters to the optimal ones [25,86,87].

Due to the computational costs of information processing in grid search strategies, evolutionary and swarm intelligence-based optimization algorithms are also applied [88,89]. In addition, the search for hyper-parameters is carried out frequently using a Bayesian search [90–92].

### 3.4. Model Training

Model training approaches are based on different categories consisting of statistical regression models, pre-trained DL (deep learning) models, ML basic models, DL basic models, graph models, ensemble models, and hybrid models. A complete list of detailed training (as well as interpretation) methods used in the identification phase of the literature in our paper is provided in the Supplementary Material to this paper. Among statistical regression models, the logistic regression (LR) model is frequently used to take on either classification or regression tasks in various studies [93–95]. Model training in the context of natural language processing and medical imaging is often elaborated through pre-trained models, such as Bert [44], ResNet [96], etc. Among the basic ML models, the extreme gradient boosting algorithm (XGB) is elaborated on in a variety of classification or regression tasks in the context of the SARS-CoV-2 literature. XGB itself is an ensemble model encompassing multiple weak tree-based models, which work together [97] based on the boosting approach. Boosting is a sequential ensemble method that iteratively adjusts the weight of observation as per the last model output. Long short-term memory networks (LSTM) and convolutional neural networks (CNN) are prominent examples of basic DL models applied frequently in the context of SARS-CoV-2 studies. LSTM excels at capturing time data dependencies, making it ideal for sequence prediction tasks [98]. CNN is specifically used for image classification and tasks that consider the processing of spatial dimensions of data [99]. While CNNs are primarily used for computer vision applications, they work on different time series problems, too [100]. Ensemble models incorporate a number of basic ML or DL models to achieve higher degrees of accuracy. Four main alternatives to creating ensembles, comprising bagging, boosting, stacking, and mixture of experts, are addressed in [93]. Hybrid models concatenate different combinations of ML and DL models at different model architecture levels [96,101,102]. Graph models reflect the underlying logical connection of the model components in a graphical style [103,104]. Graph neural networks (GNNs) are novel graph models that comprise input variables as graph components, e.g., nodes and edges. The graph components get updated through machine learning models, e.g., based on the feature networks of the nodes’ neighbors and the edges connecting them [105]. Figure 5 provides an overview of the methods presented in Section 3.4.

## Figure 5

**Figure 5.** Overview of the model training approaches resulted from the SARS-CoV-2 research studied in Section 3.3.

### PlantUML approximation

```plantuml
@startuml
left to right direction

rectangle "Model Training" as MT

rectangle "Basic" as Basic
rectangle "Hybrid" as Hybrid
rectangle "Graphical" as Graphical
rectangle "Ensemble" as Ensemble

MT --> Basic
MT --> Hybrid
MT --> Graphical
MT --> Ensemble

rectangle "Statistical" as Statistical
rectangle "ML" as ML
rectangle "DL" as DL
rectangle "Pre-Trained" as PT

Basic --> Statistical
Basic --> ML
Basic --> DL
Basic --> PT

rectangle "Bagging" as Bagging
rectangle "Boosting" as Boosting
rectangle "Stacking" as Stacking
rectangle "Mixture" as Mixture

Ensemble --> Bagging
Ensemble --> Boosting
Ensemble --> Stacking
Ensemble --> Mixture
@enduml
```

### 3.5. Model Evaluation

The evaluation of the performance of an ML or DL model depends on the model outputs. For pipelines with classification output types, the evaluation criteria are often AUC (area under receiver operating characteristic curve), precision, recall, F1-score, and accuracy [106]. The aforementioned criteria can be further elucidated based on the notions of the receiver operating characteristic (ROC) curve [107] as well as the precision and recall (PR) curve [108]. To evaluate the performance of pipelines with continuous outputs, mean absolute error (MAE), mean square error (MSE), root mean squared error (RMSE), and goodness-of-fit (R2 score) are used [90]. Furthermore, instead of evaluating the performance of a model on a single validation dataset, multiple random splits (k-fold validation) are utilized (as the performance of a model can change depending on the choice of split) [109]. For the time series ML models, a sliding window can be applied to the dataset to alter the test data that is set in a non-random (subsequent) manner from a time point to the next time point onward. Thus, if, e.g., for the first split, the test set covers 20% of the earliest data records from a certain time point on, the test set of the last split corresponds to the most recent 20% of the data records [77].

### 3.6. Model Interpretation

ML and DL models can be grouped into two categories of interpretability: Intrinsically interpretable and non-intrinsically interpretable [3]. A complete list of detailed interpretations (as well as training methods) used in the identification phase of the literature study can be found in the Supplementary Material.

#### 3.6.1. Intrinsically Interpretable Models

Statistical regression models, e.g., a logistic regression (LR) model, are examples of intrinsically interpretable models. In these models, a coefficient or odds ratio summarizes the positive or negative strength of the association between exposure and an event. Moreover, the coefficients from the LR model can be utilized to build a nomogram predicting the model outcome [110]. Regressions remain one of the simplest and most explainable models with a clear formulation. Despite this, they may not precisely accommodate the non-linear and non-monotonic patterns in the data. The literature of SARS-CoV-2 studies has proposed a range of intrinsically interpretable methods rather than statistical models. Table 2 summarizes a list of intrinsically interpretable methods identified throughout the literature analysis.

## Table 2

**Table 2.** Overview of intrinsically interpretable ML methods used in SARS-CoV-2 literature context.

| Method [Source] | Description of Method |
|---|---|
| J48 [111] | Machine learning decision tree classification algorithm based on Iterative Dichotomies. |
| RIPPER [112,113] | Rule-based ML algorithm, in which rules are learned from the data directly. |
| pyFUME [112] | Can create rules based on fuzzy logic. |
| GAMs [114] | Used as non-linear regression tools that allow for non-parametric fittings of complex dependencies of responses. |
| GNAMs [115] | A hybrid ML-DL, which belongs to the GAMs family and learns a linear combination of multi-layer perceptron models. |
| EBM [116] | Explainable boosting machine is constructed with multiple hierarchically organized simple classifiers consisting of sequences of binary decisions and tree-based decision system. |
| JRip [109] | Rule-based classifier, which creates propositional rules that can be used to classify elements. |
| Quantum Lattice [25] | Inspired by the Richard Feynman path, which creates multiple possible graphical models composed of different mathematical operations. On selection of the best model, a Q-graph is created to provide the rationale behind a prediction. Further, a simplified equation for the model is obtained that provides insights into the mapping of inputs to outputs. |
| Bayesian networks [117] | Probabilistic graphical model for representing knowledge about an uncertain domain. |

#### 3.6.2. Non-Intrinsically Interpretable Models

The non-intrinsically interpretable models are analyzed in two alternative ways in the literature: Model-agnostic approaches and model-specific approaches [3–8]. Model-agnostic approaches presume ML models as a black box and try to convey XAI based on surrogate models, either by means of employing intrinsically interpretable meta-explaining models or by means of employing perturbation mechanisms. Model-specific approaches, conversely, try to embed XAI into the specific model to observe the feature influences during the training procedure. Among model-agnostic approaches, SHAP is frequently elaborated on in a variety of model interpretation tasks in the context of the SARS-CoV-2 literature. The SHAP is a perturbation-based concept. Perturbation-based approaches aim at analyzing the importance of each input on the model outcome by systematically modifying the input of the model and observing the changes in the output. If the permutation of a specific part of the input, considerably alters the model output, then the specified part is considered to be important. SHAP computes the average marginal contribution of a feature to the output predicted by the ML model, considering all possible combinations of features [118]. The SHAP computation time increases exponentially with the number of features.

Local interpretable model-agnostic explanation (LIME) is another most frequently applied interpretation model-agnostic method that is based on perturbation and meta-modeling. LIME tunes the values of the features of a selected predicted instance and generates new samples based on the proximity to the instance being picked [119]. It then optimizes a line based on all generated samples and gives a local interpretable explanation of the instance being picked.

Likewise, a number of studies in the context of the SARS-CoV-2 literature have utilized other surrogate meta-models, which are intrinsically interpretable, to explain the logic behind decisions made by an original black-box model. Examples of such approaches include:

- using formal concept analysis (FCA) to create a set of association rules with different confidence intervals [120];
- applying a Bayesian network to visualize the effect of the potential influencers on decision making [24];
- proposing a single associated decision tree (DT) to represent a random forest (RF) model [68];
- applying the anchors method to help explain predictions by decision rules [23];
- utilizing a probabilistic graphical model (PGM-Explainer) as a simpler interpretable Bayesian network in order to interpret GNNs [121];
- applying the symbolic meta modeling approach, which integrates various simple parameterized functions to obtain a closed-form and interpretable expression for the meta model [122].

Despite a wide range of practical applications of model-agnostic models, these approaches are not ideal XAI approaches, representing the original training procedures behind the model they explain. Model-agnostic methods are indeed surrogates, which first presume an ML model as a black box, then derive their interpretations (after the model training is finished) from a different modeling perspective with priors that are not necessarily in line with the internal procedures of the original model [123]. Model-specific approaches try to fill this gap by trying to provide information regarding the actual reasoning process within the specific model through the training. Model-specific approaches are built based on incorporating weights, gradients, or attention from DL model-specific layers. Figure 6 visualizes the mechanisms behind the XAI approaches reviewed in this section.

## Figure 6

**Figure 6.** Overview of the mechanisms of XAI approaches used in the SARS-CoV-2 context: intrinsically interpretable methods, model-agnostic methods, weight-based methods, gradient-based methods, and attention-based methods.

### PlantUML approximation

```plantuml
@startuml
left to right direction

package "Intrinsically Interpretable methods" {
  database "Input" as i1
  rectangle "White box" as w1
  circle "Output" as o1
  i1 --> w1 --> o1
}

package "Model-agnostic methods" {
  database "Input" as i2
  rectangle "Black box" as b2
  circle "Output" as o2
  database "Input\nperturbed" as ip2
  rectangle "Black box" as bp2
  circle "Altered\nOutput" as ao2

  i2 --> b2 --> o2
  ip2 --> bp2 --> ao2
}

package "Weight-based methods" {
  database "Input" as i3
  circle "Neurons" as n3
  circle "Output" as o3
  i3 --> n3 --> o3 : Weights connection
}

package "Gradient-based methods" {
  database "Input" as i4
  circle "Neurons" as n4
  circle "Output" as o4
  i4 --> n4 --> o4
  o4 --> n4 : Output backpropagation
}

package "Attention-based methods" {
  database "Input" as i5
  circle "Neurons" as n5
  rectangle "Attention\nweights" as aw5
  circle "Output" as o5
  i5 --> n5 --> o5
  aw5 --> o5
}
@enduml
```

Weight-based techniques utilize the product of final weights based on the connections from input neurons to the output neurons [72,124]. Gradient-based techniques back-propagate outputs onto a particular feature map (the output of one filter applied to the previous layer). Usually, the feature map is chosen to be the final convolutional layer in CNNs. Class activation map (CAM) and Grad-CAM explanation methods are frequently applied examples of weight-based and gradient-based approaches in the literature [125]. CAM uses the notion of global average pooling (GAP) and learns weights from the output of the GAP layer onto the output classes. Grad-CAM generates a localization map that shows the critical features by using gradients from the target class, which are settled in the final convolutional layer in the CNN network [125]. Integrated gradients (IG) method is another gradient-based alternative. IG methods examine the inputs of a deep learning model and their importance for the output by integrating the gradients of the output with respect to the input along an arbitrary path from the baseline to the input data point [98].

In addition, attention mechanisms have gained a lot of attention in the SARS-CoV-2 literature [126]. The attention approaches are inspired by human attention visual mechanisms, which use limited attention to quickly screen high value information from a large amount of information. This not only contributes to increase the prediction performance but is also efficient in gaining insight into information that is more critical to the model outputs instead of learning non-useful information [37,127,128].

---

## 4. Literature Analysis of Epidemiological AI Research

In this section, we focus on the 26 papers that fulfill the inclusion criteria of our study. A detailed tabular representation of the 26 papers (comprising research question, data, pipeline, and significant results per paper) is presented in the paper’s Supplementary Materials.

The models in the papers are designed to analyze different epidemiologic aspects of SARS-CoV-2 in different geographical scopes. A subset of papers incorporated data of multiple countries, including analyzing NPIs in 176 countries [129], analyzing the evolution of cross-border movements of people during the SARS-CoV-2 in Europe [18], studying the influence of NPIs, PIs, virus variants etc. on SARS-CoV-2 spread in Europe [130], investigating the role of booster vaccine in 32 countries [131], focusing on the role of dietary imbalances in 154 countries [61], assessing the role of NPIs against SARS-CoV-2 at containing seasonal influenza transmission in 33 countries [92], forecasting confirmed cases prediction in 8 countries [102], assessing the effect of non-countermeasure factors (e.g., cultural factors) to classify countries into those more and less prone to the fast spread of SARS-CoV-2 [51], and explaining a variety of socio-temporal variables on SARS-CoV-2 prevalence and mortality at a global scale [72].

The rest of the papers, e.g., [98,127,132], mostly utilize the data of one country or region, especially from the US. The analyzed studies focus on different research objectives. Depending on the focus, they generate different explanations on the significance of different influential factors on the spread of the pandemic, such as compliance with interventions [133], population density [134], population movement and gathering [76,78,92], lock down effects [18,120], labor and unemployment effects [72,81], closure and regulation of schools [129,135], vaccination [130–132], spatial effects [74,136], weather conditions [127,137,138], country dietary and cultural effects [51,61], virus variants [98], and health infrastructural impacts [139].

The data preprocessing stage encompasses, in most studies, a data imputation step. In rare cases, the unbalanced data issue is handled, e.g., by SMOT in [138] and by excluding those NPIs that were used in less than 20 countries [129]. Data discretization is carried out by means of a relevant algorithm due to the necessity of discretization of feature values in Bayesian network analysis (but not for the sake of handling data unbalance) [136].

Feature extraction techniques are applied in three studies, comprising: PCA analysis in [18], SOM in [61], and K-means in [51]. The feature selection step is performed in most of the studies. It consists, e.g., of statistical analysis in [72,133], and stepwise wrapping methods based on k-fold validation [61,76,92,136,137,139].

SHAP-based feature selection methods [61,78,92] and feature selection based on alternative ML methods [51,92] are applied as well. Data preprocessing and data engineering steps are not explicit parts of the pipeline in [74]. The authors use the inherent advantage of XGB to cope with correlations between the covariates and to deal with data imputation.

Parameter tuning and model evaluation stages are in most models performed based on a grid search algorithm and by evaluation metrics as introduced in Sections 3.3 and 3.5, respectively.

Figures 7 and 8 depict the main ML and XAI approaches and their corresponding application frequencies within the selected epidemiological XAI research. A list of method abbreviations existing in Figures 7 and 8 is presented in Abbreviations.

Figures 7 and 8 visualize a dominance of XGB (using ML in the training step) and SHAP (using XAI in the interpretation step), as well as their joint application in the literature studied. Zopluoglu argues that this results from XGB’s speed and performance based on parallelization, tree pruning, and hardware optimization [140]. Molnar argues for the first time that this may be grounded in the solid game-theoretical basis of SHAP [141]. At the same time, the higher proportion of the XGB- and SHAP-based pipelines (beside the prevalence of other tree-based ML and model-agnostic XAI techniques) indicates a lower presence of deep learning as well as the corresponding model-specific XAI techniques in the context of epidemiological AI studies of SARS-CoV-2. This is despite the fact that deep learning approaches (the corresponding XAI techniques) are a rapidly growing area of computer science.

Table 3 illustrates further modeling aspects employed in the different XAI-based epidemiological studies analyzed.

SEIR-based ML models combine compartmental models with machine learning models to replace the fixed parameters of the former with time-varying parameters that are fitted using machine learning methods. Figure 9 illustrates the estimation of SEIR parameters based on AI-based approaches.

## Figure 7

**Figure 7.** ML approaches used in the epidemiological context, and frequency of use in the studies.

### Figure description

Pie chart of ML approaches used in the epidemiological context and relative frequency. Visible labels include:

- XGB
- ENR
- KNN
- SVM
- GB
- CONV-LSTM
- BI-LSTM
- RNN
- LGB
- ANN
- ADAB
- ENSEMBLE RF-XGB-LGB
- NN
- LOG-R
- BAYESIAN REGRESSION
- CATB
- HYBRID SEIR-GAMS-XGB
- BN
- MLP
- LR
- RF
- DT
- HYBRID AR-LSTM
- LSTM
- HYBRID SEIR-ML

## Figure 8

**Figure 8.** XAI approaches used in the epidemiological context, and frequency of use in the studies.

### Figure description

Pie chart of XAI approaches used in the epidemiological context and relative frequency. Visible labels include:

- SHAP
- PDP
- FEATURE ABLATION
- XGB FEATURE IMPORTANCE
- INTEGRATED GRADIENTS
- ATTENTION WEIGHTS
- GARSON
- VB
- MLEK
- LEK
- MS
- MCW
- CW
- WRAPPER
- RULE-LEARNER
- GAMS MODEL
- RF FEATURE IMPORTANCE
- PFI
- ALE
- REGRESSION MODEL
- FCA
- GRAPH-SHAP
- PGM
- ICE

## Table 3

**Table 3.** Overview of modelling aspects in the XAI epidemiological studies.

| Modelling Aspect | SEIR Based ML | Time Explicitness | Dynamic Time | Graphical Model | Rule Creating XAI | Model-Specific XAI |
|---|---|---|---|---|---|---|
| [Source] | [135,142] | [18,81,92,98,102,120,127,129,132,135,138,139,142] | [98,102,120,127,135,138,139,142] | [136,142,143] | [51,120] | [72,98,127,138] |

## Figure 9

**Figure 9.** Hybrid SEIR-Deep learning approach in epidemiological pipelines.

### PlantUML approximation

```plantuml
@startuml
top to bottom direction

rectangle "Epidemic Data" as ED

rectangle "Time series Data:\n- Government Measures (NPIs)\n- Virus variant percentages\n- Populated vaccination percentages\n- Daily infection number" as TS

rectangle "Static Data:\n- Healthcare system data\n- Economic system data\n- ...\n- system data\n- Demographic data" as SD

rectangle "Estimate SEIR Transition Rates based on XAI\n\n- Rate at which people transition from susceptible to exposed\n- Rate at which people transition from exposed to infected\n- Rate at which people transition from infected to recovered\n- ..." as EST

state "Susceptible" as S
state "Exposed" as E
state "Infected" as I
state "Recovered" as R

rectangle "Transformer Models" as TM
rectangle "Graphical Models" as GM
rectangle "..." as OM
rectangle "Bayesian Models" as BM

ED --> TS
ED --> SD
TS --> EST
SD --> EST

S --> E
E --> I
I --> R

TM --> EST
GM --> EST
OM --> EST
BM --> EST
@enduml
```

Time series data (Figure 9) includes the main epidemiological factors such as daily government non-pharmaceutical measures (NPIs), the percentages of different virus variants, as well as the proportion of vaccinated people. Static data include factors such as country-specific parameters of the healthcare system as well as its demographic and economic characteristics. The transition rates at which people move from one state of the SEIR model to another state can be calculated based on deep learning models fed with time series and static epidemic data. The deep learning models applied can be of different natures (e.g., pre-trained transformer-based, graphical, Bayesian, etc.).

Vega et al. [142] use a simplified probabilistic graph model (PGM) (e.g., probabilistic version of linear regression) to update the SEIR model parameters based on past information and estimated parameters in a previous iteration. Ref. [135] adopts a generalized additive model for each variable to be added to the SEIR model to represent the transmission rates.

A subset of studies is not designed to be used as real-time forecasting tools. Indeed, most of the studies employ fitted models to enhance the overall understanding regarding the effect of various influential features on pandemic progression, mortality rates, etc. Hence, they do not explicitly model the factor time. In contrast, a subset of studies (listed in the third column of Table 3) has explicitly modeled the factor time. These studies can be divided into two distinct categories: (a) Studies, which utilize dynamic time series models (i.e., RNN, LSTM, or CNN) to systematically incorporate the dependencies between consequent time points (listed in the fourth column in Table 3); and (b) studies, which treat each variable at each time point as a distinct input to the model (listed in the third column but not listed in the fourth column in Table 3). For example, Ref. [129] represents a combination of each NPI variable with how long the corresponding NPI has been in place as a distinct variable. Ref. [92] used, for each NPI, the lagged day with the largest Spearman correlation coefficient to generate the explanatory variables. Nonetheless, Ref. [127] uses a multi-stage (4-stage) LSTM, which, at each stage, forecasts a chosen target variable for one week ahead. The model elaborates on the initial first stage prediction to forecast an additional week, and it continues to implement this iterative approach, one stage at a time, to predict further into the future.

Graphical causal structure of the data is used in the studies presented in Table 3, not only for the sake of intrinsically interpretable model training [136,142], but also for incorporating prior knowledge into the resulting SHAP values [143]. In addition, creating associative rules as interpretable model-agnostic models is applied in [51,120].

The explanations provided by models in the sixth column of Table 3 are model-specific explanation types replicating an ML model’s internal mechanism. Such XAIs can better reflect the corresponding decision making of the models rather than explanations produced by model-agnostic methods. These XAI methods reflect:

- the internal connected neurons’ weights in [72];
- attention weights (to determine which input features should be given more attention over others, and the weight of importance for each historical temporal step) in [127]
- integrated gradient in [98];
- the XGB feature is important in [138], representing the percentage of trees that use a variable in the ensemble tree model.

Although the presented studies incorporate important data processing, training, and explanation tools, there is still room to reflect on enhancing the reviewed AI pipelines based on the existing scope of literature.

---

## 5. Discussion and Conclusions

The overall aim of this paper is to systematically figure out the main research gaps with regard to the methodological aspects of the epidemiological interpretable machine learning models of SARS-CoV-2. In Section 3, we developed a conceptual framework for the methodical pipeline of AI-based model development. The conceptual framework serves as a guideline for the analysis of epidemiological AI research in Section 4. Subsequently, we summarize the main existing research gaps in XAI-based epidemiological models of SARS-CoV-2 as data, modeling, explanation, uncertainty, and generation. Figure 10 visualizes the summarization of the main research needs related to each of the aforementioned research gaps.

## Figure 10

**Figure 10.** Main existing research needs in XAI-based epidemiological models of SARS-CoV-2.

### PlantUML approximation

```plantuml
@startuml
left to right direction

rectangle "Maximize available data\nutilization" as A
rectangle "Boost deep learning\nutilization in\nEpidemiological modeling" as B
rectangle "Generate Best Policies\nsubject to status of the\npandemic" as C

ellipse "Incorporate\nuncertainty" as U
ellipse "Incorporate\nModel/Case\nspecific\nExplanation" as E

A --> B --> C
U ..> B
U ..> C
E ..> B
E ..> C
@enduml
```

More detailed research necessities are elaborated in the following subsections.

### 5.1. Data

Currently, the problem of missing, unbalanced, and sparse data is handled to a limited extent, especially by applying oversampling techniques such as SMOTE. SMOTE works based on the k-nearest neighbors’ principle and the principles of interpolation. However, such models can lead to the generation of poor, new, or unseen data. Upcoming epidemiological research needs to explore using more complex methods based on the variety of techniques mentioned in Section 3.1, especially generative approaches, e.g., AEs and GANs, to come up with a data scarcity issue.

In addition, while the datasets used in the recent epidemiological AI research are scattered and diverse, assessing the impact of different applied data sources in the analyzed literature in Section 4 on the corresponding results in a comparative way is crucial. A variety of influencing factors are used to generate results. Key data used in the reviewed epidemiological studies in our study are aggregated in Table 4.

## Table 4

**Table 4.** Overview of selected key data used in XAI-based epidemiological studies of SARS-CoV-2.

| Paper | Selected Key Data |
|---|---|
| [133] | Compliance with NPIs, mobility patterns, work–life conflicts. |
| [134] | Income per capita, Population density. |
| [142] | Regional government policies. |
| [76] | Travel data, population density, medical endowments, environmental policy. |
| [143] | Socioeconomic disparities. |
| [120] | New cases, seasons, national lockdown, population vaccination number. |
| [102] | Population data, positive and total tests, number of cases and deaths, population vaccination number. |
| [81] | Population density, educational data, income data, household and housing data. |
| [129] | NPIs and how long which NPI has been in place. |
| [18] | Data on international travel bans, stringency of countries containment policies, Facebook users’ mobility data. |
| [130] | NPIs, different virus variants, average daily temperature, population characteristics, health expenditures, cultural participation data. |
| [135] | Confirmed case and deaths, Google mobility reports, government restrictions, demographic data. |
| [136] | Geographic data, e.g., proximity to major health facilities, churches, shopping centers and supermarkets, Average annual traffic density. |
| [131] | Health services indexes, GDP, behavioral risk factors. |
| [78] | Demographic data, economic data, health care data, unemployment, education, emissions. |
| [137] | Air pollution, proximity to industrial facilities, neighborhood and housing characteristics, age, poverty rate. |
| [61] | Dietary habits, past comorbidity prevalence, environmental policy factors such as seasonally averaged temperature geolocation, development indices. |
| [74] | Sex, age, ethnicity, comorbidities, socioeconomic data. |
| [92] | NPIs, influenza virology surveillance. |
| [132] | Vaccination data, wearing masks, mobility, government interventions. |
| [51] | Weather, culture, travel, health, economical data, development data. |
| [72] | Unemployment data, population density, air and rail transportation, urban population, gross national income per capita. |
| [127] | Demographic, public health data, population density, transportation, pollution, sex ratio. |
| [98] | Mobility, climate data, demographic data, virus variant frequencies. |
| [138] | Weather situation in the location of the infected person, medRxiv, and bioRxiv SARS-CoV-2 literature databases. |
| [139] | Mobility data, death number, patients in ICU, hospitalization by region. |

Investigating the feasibility of integrating the above-mentioned data sources into comprehensive pipelines is a research need. This approach can lead to the creation of pre-trained epidemiological models based on the combination of existing large SARS-CoV-2 data sets. The resulting models can then be used for the next possible pandemic through transformer-based approaches based on the specific nature of new epidemic diseases or the corresponding specific spatial dimensions. The conceptual framework presented in Section 3 represents a starting point for tackling this research.

### 5.2. Modelling

Although the need to use deep learning models to address the spatial and temporal features of epidemics in epidemiological pipelines is urgent, we have found (in Section 4) that deep learning-based (as well as corresponding XAI) methods are not widely considered. The SEIR approaches can be enriched by using state-of-the art DL models. Currently, the time-dependent parameters of the applied SEIR models are often updated based on classic time series approaches or simplified probabilistic graph models [142]. Hybrid CNN-LSTM architectures as well as novel GNN approaches (presented in Section 3.4) are archetypal alternative approaches that can represent the time-varying character of SEIR model parameters in a robust and explainable manner.

The usage of CNN-based architecture approaches in the context of clinical studies is practiced [144]. However, the potential of CNN-based models has so far not been substantially exploited in XAI-based epidemiological studies. CNNs can be combined with the time-dependency-based architecture of existing LSTM models (mentioned in Section 4) to present multi-dimensional spatial-temporal representations of the pandemic. CNNs perform convolution operations in the upstream layers of the network, where the filters extract the most critical features to generate a feature map. The extracted features can not only be of spatial or temporal nature but also be used to recognize a range of government policies, including PIs and NPIs in a certain spatial context (cf. Figure 9). Further research is needed to explore these options.

In addition, other feature extraction methods mentioned in Section 3.2.2, such as knowledge embedding graphs, functional data analysis, and RFFs, have not been examined in epidemiological studies. By encoding the explanatory factors into dense and low-dimensional vectors, these methods can potentially boost the predictive power of AI models. Whether the inclusion of these methods enhances (or decreases) the explanation power of the models needs to be further studied. However, as mentioned in Section 3, through utilizing further AI and XAI techniques, it is possible to shed light on the features with the strongest impact on feature extraction methods. In addition, applying explainable graphical approaches to selecting the relevant features (noted in Section 3.2.3) has not yet been considered in epidemiological research.

Physics-informed neural networks (PINNs) [145] and neural ordinary differential equations (Neural ODEs) [146] are further noticeable modeling approaches that are not identified within the searched scope in Sections 3 and 4, but need to be considered more in future XAI-based epidemiologic research. PINNs comprise neural networks that can add the SEIR models and the corresponding constraints as a regularization term in the loss function. The regularization term penalizes the training when SEIR models and the corresponding constraints are disturbed [147,148]. Neural ODEs combine the notions of ordinary differential equations (ODEs) and deep learning by parameterizing the derivative of the hidden state in the neural network. Given that the SEIR model can be expressed by an intractable system of ordinary differential equations, neural ODEs can devise a representing system that approximates the output of the model [149]. Future research shall demonstrate the added value of such approaches within future XAI-based epidemiologic research.

### 5.3. Explanation

The set of applied XAI methods shown in Section 4 is currently led by model-agnostic interpretation methods, especially SHAP-based approaches (see Figure 8 above).

Other model-agnostic interpretation methods, i.e., surrogate meta-models introduced in Section 3.6.2, such as symbolic meta modeling, FCA, and anchors are not well known in the epidemiological context. In addition, while the high-performance degree of intrinsically interpretable approaches (especially the high performance of EBMs compared to non-intrinsically interpretable models) is indicated in the corresponding literature (cf. Table 2), such approaches are still not well known in the field of epidemiology. Moreover, the potential of model-specific interpretation methods (mentioned in Section 3.6.2) is, to date, not effectively utilized. Model-specific explanations can better replicate the ML models’ corresponding decision making than explanations created using model-agnostic methods. Model-specific CNN XAI approaches, such as gradient- and CAM-based methods, are proposed in papers belonging to the group of X-ray and CT imaging methods. The Grad-CAM interpretation method uses the gradients of the target class flowing into the final convolutional layer and, hence, can be used to produce visual explanations for any CNN-based model. It can be applied to the spatial-temporal epidemiological pipelines, too, indicating further research is needed in this area.

Case-based reasoning (CBR) techniques are another decent technique that can be adopted from the broad context of the literature in epidemiological XAI research. In the evidence-based medical domain, cases are the most specialized form of knowledge representation, consisting of both general understanding and human experiences, taking into consideration differences between the current case and typical or known exceptional cases [150]. Prototyping for the explanation of decision making within the training networks in the clinical and imaging-based studies of SARS-CoV-2 has been explored through CBR-based approaches [123,151,152]. However, this area of research has not yet been explored in an XAI-based epidemiological context.

Furthermore, comparing the explaining power and suitability of different XAI methods to epidemiological problems based on reliable criteria has not been elaborated in the existing literature. While some research, e.g., [153,154], has proposed guidelines for evaluating and scoring XAI methods from a human understanding point of view in medical image applications, neither a global evaluation schema nor specific evaluation metrics have been proposed as standard evaluation schemes so far. This needs to be further addressed in the medical AI literature as well as within the related epidemiological research. The relevant evaluation criteria must enable the epidemiological research to choose XAI methods, which not only efficiently convey the significance and magnitude of the effects of each pandemic explanatory factor in the spread of a pandemic but also efficiently explain the required time gaps, which could have been necessary to unfold the effect of each explanatory factor. This research can also possibly be extended to examine the fusion and hybridization of the existing XAI models.

### 5.4. Uncertainty

At the onset of pandemic phases, where the available data are scarce, not only the task of forecasting but also the task of explaining and generating suitable epidemiological policies are required to be inherently of a non-deterministic nature. The effect of data scarcity, both on model training and on model interpretation, is argued in Section 3.1 [19]. Scarce data necessitates the incorporation of uncertainty in the model training as well as in the model interpretation [17]. Incorporating uncertainty in model training and model interpretation level is practiced in computer vision literature. For example, [17] introduces ensemble models of pre-trained CNNs with large changes in CNN weights and applied uncertain-CAM approaches to their model explanation. In the epidemiological context, uncertainty is rarely performed based on Bayesian approaches [137]. Elaborating more on different non-deterministic approaches, including ensemble models (to best synthesize the predictions of multiple basic models) [93] and Bayesian neural networks (to infer distributions over the models’ weights and outputs) [155], can enhance future epidemiological pipelines.

### 5.5. Generation

The important role generative DL models can play within the scope of epidemiological studies is not elaborated on in the range of the reviewed SARS-CoV-2 literature studied in Section 4. Currently, most generative AI models are performed in the field of computer vision as well as in medical studies. A comprehensive study on the role of GANs in addressing the challenges related to SARS-CoV-2 data scarcity and diagnosis is presented in [156]. The use of GANs in the context of SARS-CoV-2 diagnosis is further studied in [38,157]. Generative epidemiological pipelines can create government policies along with different counter-factual scenarios as the pandemic spreads beyond the forecasting models. However, further research is needed to develop reliable and accurate results with GANs.

---

## Supplementary Materials

The following supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/life14070783/s1.

## Author Contributions

Conceptualization, M.A.W. and H.K.; methodology, H.K.; software, H.K.; validation, M.A.W.; formal analysis, M.A.W.; investigation, H.K.; resources, M.A.W.; data curation, H.K.; writing—original draft preparation, H.K.; writing—review and editing, M.A.W.; visualization, H.K.; supervision, M.A.W.; project administration, M.A.W.; funding acquisition, M.A.W. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by Ministry of Science and Health of Rhineland-Palatinate, Germany, grant number 7208-0008#2021/0003-1501 15401 and the APC was funded by Ministry of Science and Health of Rhineland-Palatinate, Germany. URL: https://covid-ai.uni-koblenz.de/, accessed on 20 June 2024.

## Acknowledgments

We acknowledge the fruitful discussion along presentations of the work in our joint workshops of the four research groups at the University of Koblenz.

## Conflicts of Interest

No conflicts of interest exist for the authors.

---

## Abbreviations

### ML abbreviations

- ADAB — adaptive boosting model
- ANN — artificial neural network
- AR — autoregressive model
- BI-LSTM — bidirectional long short-term memory network
- BN — Bayesian network model
- CATB — categorical boosting model
- CBR — case-based reasoning
- CONV-LSTM — convolutional long short term memory network
- DT — decision tree
- EBM — explainable boosting machine
- ENR — elastic net regularization regression
- GAMS — generalized additive model
- GAN — generative network
- GB — gradient boosting model
- KNN — k-nearest neighbors model
- LGB — light gradient boosting model
- LOG-R — logistic regression
- LR — linear regression
- LSTM — long short-term memory network
- MLP — multi-layer perception network
- NN — neural network
- ODEs — ordinary differential equations
- PINNs — physics-informed neural networks
- RF — random forest
- RNN — recurrent neural network
- SEIR — susceptible exposed infected recovered model
- SVM — support vector machine
- XGB — extreme gradient boosting model

### XAI abbreviations

- ALE — accumulated local effects
- CW — connection weights
- FCA — formal concept analysis
- ICE — individual conditional expectation
- IG — integrated gradients
- LIME — local interpretable model-agnostic explanation
- MCW — modified connection weights
- MS — most squares
- SHAP — Shapley value-based explanation
- PDP — partial dependence plot
- PFI — permutation feature importance
- PGM — probabilistic graphical model
- VB — Variance-based model

---

## References

1. Vinod, D.N.; Prabaharan, S.R.S. COVID-19-The Role of Artificial Intelligence, Machine Learning, and Deep Learning: A Newfangled. *Arch. Comput. Methods Eng.* **2023**, *30*, 2667–2682.  
2. Miller, T. Explanation in artificial intelligence: Insights from the social sciences. *Artif. Intell.* **2019**, *267*, 1–38.  
3. Allgaier, J.; Mulansky, L.; Draelos, R.L.; Pryss, R. How does the model make predictions? A systematic literature review on the explainability power of machine learning in healthcare. *Artif. Intell. Med.* **2023**, *143*, 102616.  
4. Lu, S.; Swisher, C.L.; Chung, C.; Jaffray, D.; Sidey-Gibbons, C. On the importance of interpretable machine learning predictions to inform clinical decision making in oncology. *Front. Oncol.* **2023**, *13*, 1129380.  
5. Confalonieri, R.; Coba, L.; Wagner, B.; Besold, T.R. A historical perspective of explainable Artificial Intelligence. *WIREs Data Min. Knowl. Discov.* **2021**, *11*, e1391.  
6. Angelov, P.P.; Soares, E.A.; Jiang, R.; Arnold, N.I.; Atkinson, P.M. Explainable artificial intelligence: An analytical review. *Wiley Interdiscip. Rev. Data Min. Knowl. Discov.* **2021**, *11*, e1424.  
7. Vilone, G.; Longo, L. Notions of explainability and evaluation approaches for explainable artificial intelligence. *Inf. Fusion* **2021**, *76*, 89–106.  
8. Tjoa, E.; Guan, C. A Survey on Explainable Artificial Intelligence (XAI): Toward Medical XAI. *IEEE Trans. Neural Netw. Learn. Syst.* **2021**, *32*, 4793–4813.  
9. Abiodun, K.M.; Awotunde, J.B.; Aremu, D.R.; Adeniyi, E.A. Explainable AI for Fighting COVID-19 Pandemic: Opportunities, Challenges, and Future Prospects. In *Computational Intelligence for COVID-19 and Future Pandemics. Disruptive Technologies and Digital Transformations for Society 5.0*; Kose, U., Watada, J., Deperlioglu, O., Marmolejo Saucedo, J.A., Eds.; Springer: Singapore, 2022.  
10. Janssen, M.; Hartog, M.; Matheus, R.; Yi Ding, A.; Kuk, G. Will Algorithms Blind People? The Effect of Explainable AI and Decision-Makers’ Experience on AI-supported Decision-Making in Government. *Soc. Sci. Comput. Rev.* **2022**, *40*, 478–493.  
11. Sun, J.; Shi, W.; Giuste, F.O. Improving explainable AI with patch perturbation-based evaluation pipeline: A COVID-19 X-ray image analysis case study. *Sci. Rep.* **2023**, *13*, 19488.  
12. Moher, D.; Liberati, A.; Tetzlaff, J.; Altman, D.G. The PRISMA Group Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement. *PLoS Med.* **2009**, *6*, e1000097.  
13. Page, M.J.; McKenzie, J.E.; Bossuyt, P.M.; Boutron, I.; Hoffmann, T.C.; Mulrow, C.D. The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ* **2021**, *372*, n71.  
14. Severn, C.; Suresh, K.; Görg, C.; Choi, Y.S.; Jain, R.; Ghosh, D. A Pipeline for the Implementation and Visualization of Explainable Machine Learning for Medical Imaging Using Radiomics Features. *Sensors* **2022**, *22*, 5205.  
15. Zoabi, Y.; Deri-Rozov, S.; Shomron, N. Machine learning-based prediction of COVID-19 diagnosis based on symptoms. *NPJ Digit. Med.* **2021**, *4*, 3.  
16. Jayanthi, P.; MuraliKrishna, I. ARIMA and Predicted Geospatial Distribution of COVID-19 in India. In *Interpretable Cognitive Internet of Things for Healthcare. Internet of Things*; Kose, U., Gupta, D., Khanna, A., Rodrigues, J.J.P.C., Eds.; Springer: Cham, Switzerland, 2023.  
17. Aldhahi, W.; Sull, S. Uncertain-CAM: Uncertainty-Based Ensemble Machine Voting for Improved COVID-19 CXR Classification and Explainability. *Diagnostics* **2023**, *13*, 441.  
18. Docquier, F.; Golenvaux, N.; Nijssen, S. Cross-border mobility responses to COVID-19 in Europe: New evidence from facebook data. *Glob. Health* **2022**, *18*, 41.  
19. Hinns, J.; Fan, X.; Liu, S.; Raghava Reddy Kovvuri, V.; Yalcin, M.O.; Roggenbach, M. An Initial Study of Machine Learning Underspecification Using Feature Attribution Explainable AI Algorithms: A COVID-19 Virus Transmission Case Study. In *PRICAI 2021: Trends in Artificial Intelligence*; Pham, D.N., Theeramunkong, T., Governatori, G., Liu, F., Eds.; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2021; Volume 13031.  
20. Andonov, D.I.; Ulm, B.; Graessner, M. Impact of the COVID-19 pandemic on the performance of machine learning algorithms for predicting perioperative mortality. *BMC Med. Inf. Decis. Mak.* **2023**, *23*, 67.  
21. Cabitza, F.; Campagner, A.; Ferrari, D.; Di Resta, C.; Ceriotti, D.; Sabetta, E.; Colombini, A.; De Vecchi, E.; Banfi, G.; Locatelli, M.; et al. Development, evaluation, and validation of machine learning models for COVID-19 detection based on routine blood tests. *Clin. Chem. Lab. Med. (CCLM)* **2021**, *59*, 421–431.  
22. Chadaga, K.; Chakraborty, C.; Prabhu, S. Clinical and Laboratory Approach to Diagnose COVID-19 Using Machine Learning. *Interdiscip. Sci. Comput. Life Sci.* **2022**, *14*, 452–470.  
23. Casiraghi, E.; Malchiodi, D.; Trucco, G.; Frasca, M.; Cappelletti, L.; Fontana, T.; Esposito, A.A.; Avola, E.; Jachetti, A.; Reese, J.; et al. Explainable Machine Learning for Early Assessment of COVID-19 Risk Prediction in Emergency Departments. *IEEE Access* **2020**, *8*, 196299–196325.  
24. Alle, S.; Kanakan, A.; Siddiqui, S.; Garg, A.; Karthikeyan, A. COVID-19 Risk Stratification and Mortality Prediction in Hospitalized Indian Patients: Harnessing clinical data for public health benefits. *PLoS ONE* **2022**, *17*, e0264785.  
25. Khanna, V.V.; Chadaga, K.; Sampathila, N.; Prabhu, S.; Chadaga, R. A machine learning and explainable artificial intelligence triage-prediction system for COVID-19. *Decis. Anal. J.* **2023**, *7*, 100246.  
26. Adeoye, E.A.; Rozenfeld, Y.; Beam, J. Who was at risk for COVID-19 late in the US pandemic? Insights from a population health machine learning model. *Med. Biol. Eng. Comput.* **2022**, *60*, 2039–2049.  
27. Rezapour, M.; Elmsheuser, S.K. Artificial intelligence-based analytics for impacts of COVID-19 and online learning on college students’ mental health. *PLoS ONE* **2022**, *17*, e0276767.  
28. Wendland, P.; Schmitt, V.; Zimmermann, J.; Häger, L.; Göpel, S.; Schenkel-Häger, C.; Kschischo, M. Machine learning models for predicting severe COVID-19 outcomes in hospitals. *Inform. Med. Unlocked* **2023**, *37*, 101188.  
29. Croci, S.; Venneri, M.A.; Mantovani, S.; Fallerini, C.; Benetti, E.; Picchotti, N.; Campolo, F.; Imperatore, F.; Palmieri, M.; Daga, S.; et al. The polymorphism L412F in TLR3 inhibits autophagy and is a marker of severe COVID-19 in males. *Autophagy* **2022**, *18*, 1662–1672.  
30. Hu, K.; Huang, Y.; Huang, W.; Tan, H.; Chen, Z.; Zhong, Z.; Li, X.; Zhang, Y.; Gao, X. Deep supervised learning using self-adaptive auxiliary loss for COVID-19 diagnosis from imbalanced CT images. *Neurocomputing* **2021**, *458*, 232–245.  
31. AlJame, M.; Ahmad, I.; Imtiaz, A.; Mohammed, A. Ensemble learning model for diagnosing COVID-19 from routine blood tests. *Inform. Med. Unlocked* **2020**, *21*, 100449.  
32. Cortes, M.P.; Schultz, C.S.; Sinclair, S.I.J.E.; Bhakta, S.; Kunze, K.L.; Johnson, P.W.; Cowart, J.B.; Carter, R.E.; Franco, P.M.; Sanghavi, D.K.; et al. The Pitfalls of Mining for QuantiFERON Gold in Severely Ill Patients with COVID-19. *Mayo Clinic Proceedings: Innovations, Quality, Outcomes* **2022**, *6*, 409–419.  
33. Esposito, A.; Casiraghi, E.; Chiaraviglio, F.; Scarabelli, A.; Stellato, E.; Plensich, G.; Lastella, G.; Di Meglio, L.; Fusco, S.; Avola, E.; et al. Artificial Intelligence in Predicting Clinical Outcome in COVID-19 Patients from Clinical, Biochemical and a Qualitative Chest X-Ray Scoring System. *Rep. Med. Imaging* **2021**, *14*, 27–39.  
34. Liang, W.; Yao, J.; Chen, A. Early triage of critically ill COVID-19 patients using deep learning. *Nat. Commun.* **2020**, *11*, 3543.  
35. Abbasimehr, H.; Paki, R.; Bahrini, A. A novel approach based on combining deep learning models with statistical methods for COVID-19 time series forecasting. *Neural Comput. Applic.* **2022**, *34*, 3135–3149.  
36. Amin, J.; Sharif, M.; Gul, N. Quantum Machine Learning Architecture for COVID-19 Classification Based on Synthetic Data Generation Using Conditional Adversarial Neural Network. *Cogn. Comput.* **2022**, *14*, 1677–1688.  
37. Singh, R.K.; Pandey, R.; Babu, R.N. COVIDScreen: Explainable deep learning framework for differential diagnosis of COVID-19 using chest X-rays. *Neural Comput. Applic.* **2021**, *33*, 8871–8892.  
38. Rangarajan, A.K.; Ramachandran, H.K. A preliminary analysis of AI based smartphone application for diagnosis of COVID-19 using chest X-ray images. *Expert Syst. Appl.* **2021**, *183*, 115401.  
39. Laatifi, M.; Douzi, S.; Ezzine, H. Explanatory predictive model for COVID-19 severity risk employing machine learning, SHAPley addition, and LIME. *Sci. Rep.* **2023**, *13*, 5481.  
40. Khozeimeh, F.; Sharifrazi, D.; Izadi, N.H. Combining a convolutional neural network with autoencoders to predict the survival chance of COVID-19 patients. *Sci. Rep.* **2021**, *11*, 15343.  
41. Khobahi, S.; Agarwal, C.; Soltanalian, M. CoroNet: A Deep Network Architecture for Semi-Supervised Task-Based Identification of COVID-19 from Chest X-ray Images; Cold Spring Harbor Laboratory Press: New York, NY, USA, 2020.  
42. Ntakolia, C.; Priftis, D.; Charakopoulou-Travlou, M.; Rannou, I.; Magklara, K.; Giannopoulou, I.; Kotsis, K.; Serdari, A.; Tsalamanios, E.; Grigoriadou, A. An Explainable Machine Learning Approach for COVID-19’s Impact on Mood States of Children and Adolescents during the First Lockdown in Greece. *Healthcare* **2022**, *10*, 149.  
43. Sulaiman, S.; Salam, N.; Nisha, U.B.; Abdullah, R.Y. COVID-19 Risk Prediction with Regularized Discriminant Analysis and Lasso Regression Using Booster Tree. In *Information and Communication Technology for Competitive Strategies (ICTCS 2021)*; Kaiser, M.S., Xie, J., Rathore, V.S., Eds.; Lecture Notes in Networks and Systems; Springer: Singapore, 2023; Volume 401.  
44. Beranová, L.; Joachimciak, M.P.; Kliegr, T. Why was this cited? Explainable machine learning applied to COVID-19 research literature. *Scientometrics* **2022**, *127*, 2313–2349.  
45. De Falco, I.; De Pietro, G.; Sannino, G. Classification of Covid-19 chest X-ray images by means of an interpretable evolutionary rule-based approach. *Neural Comput. Applic.* **2023**, *35*, 16061–16071.  
46. Gomes, D.P.S.; Horry, M.J.; Ulhaq, A.; Paul, M.; Chakraborty, S.; Saha, M.; Debnath, T.; Motiur Rahaman, D.M. MAVIDH Score: A COVID-19 Severity Scoring using Chest X-ray Pathology Features. *arXiv* **2021**, arXiv:2011.14983.  
47. Nguyen, X.V.; Dikici, E.; Candemir, S.; Ball, R.L.; Prevedello, L.M. Mortality Prediction Analysis among COVID-19 Inpatients Using Clinical Variables and Deep Learning Chest Radiography Imaging Features. *Tomography* **2022**, *8*, 1791–1803.  
48. Chamberlin, J.H.; Aquino, G.; Nance, S. Automated diagnosis and prognosis of COVID-19 pneumonia from initial ER chest X-rays using deep learning. *BMC Infect. Dis.* **2022**, *22*, 637.  
49. Shang, L.; Kou, Z.; Zhang, Y.; Wang, D. A Duo-Generative Approach to Explainable Multimodal COVID-19 Misinformation Detection; Association for Computing Machinery: New York, NY, USA, 2022.  
50. Thenata, A.; Suryadi, M. Machine Learning Prediction of Anxiety Levels in the Society of Academicians during the COVID-19 Pandemic. *J. Varian* **2022**, *6*, 81–88.  
51. Janko, V.; Slapničar, G.; Dovgan, E.; Resčič, N.; Kolenik, T.; Gjoreski, M.; Smerkol, M.; Gams, M.; Luštrek, M. Machine Learning for Analyzing Non-Countermeasure Factors Affecting Early Spread of COVID-19. *Int. J. Environ. Res. Public Health* **2021**, *18*, 6750.  
52. Chieregato, M.; Frangiamore, F.; Morassi, M. A hybrid machine learning/deep learning COVID-19 severity predictive model from CT images and clinical data. *Sci. Rep.* **2022**, *12*, 4329.  
53. Hueniken, K.; Somé, N.H.; Abdelhack, M.; Taylor, G.; Elton Marshall, T.; Wickens, C.M.; Hamilton, H.A.; Wells, S.; Felsky, D. Machine Learning–Based Predictive Modeling of Anxiety and Depressive Symptoms during 8 Months of the COVID-19 Global Pandemic: Repeated Cross-sectional Survey Study. *JMIR Ment. Health* **2021**, *8*, e32876.  
54. Yu, Z.; Sohail, A.; Nofal, T.; Tavares, J.O.; Manuel, R.S. Explainability of neural network clustering in interpreting the COVID-19 emergency data. *Fractals* **2022**, *30*, 2240122.  
55. Souza, A.A.d.; Almeida, D.C.d.; Barcelos, T.S. Simple hemogram to support the decision-making of COVID-19 diagnosis using clusters analysis with self-organizing maps neural network. *Soft Comput.* **2023**, *27*, 3295–3306.  
56. Lannou, E.L.; Post, B.; Haar, S.; Brett, S.J.; Kardarivelu, B.; Faisal, A.A. Clustering of Patient Comorbidities within Electronic Medical Records Enables High-Precision COVID-19 Mortality Prediction; Cold Spring Harbor Laboratory Press: New York, NY, USA, 2021.  
57. Higaki, A.; Okayama, H.; Homma, Y. Predictive value of neutrophil-to-lymphocyte ratio for the fatality of COVID-19 patients complicated with cardiovascular diseases and/or risk factors. *Sci. Rep.* **2022**, *12*, 13606.  
58. Cooper, A.; Doyle, O.; Bourke, A. Supervised Clustering for Subgroup Discovery: An Application to COVID-19 Symptomatology. In *Machine Learning and Principles and Practice of Knowledge Discovery in Databases*; Kamp, M., Koprinska, I., Bibal, A., Bouadi, T., Frenay, B., Galarraga, L., Oramas, J., Adilova, L., Krishnamurthy, Y., Kang, B., et al., Eds.; ECML PKDD 2021; Communications in Computer and Information Science; Springer: Cham, Switzerland, 2021; Volume 1525.  
59. Lande, J.; Pillay, A.; Chandra, R. Deep learning for COVID-19 topic modelling via Twitter: Alpha, Delta and Omicron. *arXiv* **2023**, arXiv:2303.00135.  
60. Ali, S.; Zhou, Y.; Patterson, M. Efficient analysis of COVID-19 clinical data using machine learning models. *Med. Biol. Eng. Comput.* **2022**, *60*, 1881–1896.  
61. Trajanoska, M.; Trajanov, R.; Eftimov, T. Dietary, comorbidity, and geo-economic data fusion for explainable COVID-19 mortality prediction. *Expert Syst. Appl.* **2022**, *209*, 118377.  
62. Li, S.; Wong, K.W.; Zhu, D. Drug-CoV: A drug-origin knowledge graph discovering drug repurposing targeting COVID-19. *Knowl. Inf. Syst.* **2023**, *65*, 5289–5308.  
63. Ma, J.; Li, B.; Li, Q.; Fan, C.; Mostafavi, A. Attributed Network Embedding Model for Exposing COVID-19 Spread Trajectory Archetypes. *arXiv* **2022**, arXiv:2209.09448.  
64. Zhu, J.; Weng, F.; Zhuang, M.; Lu, X.; Tan, X.; Lin, S.; Zhang, R. Revealing Public Opinion towards the COVID-19 Vaccine with Weibo Data in China: BertFDA-Based Model. *Int. J. Environ. Res. Public Health* **2022**, *19*, 13248.  
65. de Paiva, B.B.M.; Pereira, P.D.; de Andrade, C.M.V. Potential and limitations of machine meta-learning (ensemble) methods for predicting COVID-19 mortality in a large inhospital Brazilian dataset. *Sci. Rep.* **2023**, *13*, 3463.  
66. Cao, Y.; Duan, X.; Hou, S.; Xing, W.; Yang, M.; Ma, Y.; Wang, Z.; Li, W.; Li, Q.; He, C.; et al. *Intelligent Classification of B-Line and White Lung from COVID-19 Pneumonia Ultrasound Images Using Radiomics Analysis*; Association for Computing Machinery: New York, NY, USA, 2022.  
67. Lingelbach, K.; Gado, S.; Janssen, D.; Piechnik, D.; Eichler, M.; Knopf, D.; Hentschel, L.; Schuler, M.; Sernatinger, D.; Peissner, M. Identifying the Effects of COVID-19 on Psychological Well-Being Through Unsupervised Clustering for Mixed Data. In *Proceedings of Sixth International Congress on Information and Communication Technology*; Yang, X.S., Sherratt, S., Dey, N., Joshi, A., Eds.; Lecture Notes in Networks and Systems; Springer: Singapore, 2022; Volume 235.  
68. Rostami, M.; Oussalah, M.A. Novel explainable COVID-19 diagnosis method by integration of feature selection with random forest. *Inform. Med. Unlocked* **2022**, *30*, 100941.  
69. Cui, S.; Jiang, Y.; Shi, Q.Z.L.; Kong, D.; Qian, M.; Chu, J. Impact of COVID-19 on Anxiety, Stress, and Coping Styles in Nurses in Emergency Departments and Fever Clinics: A Cross-Sectional Survey. *Risk Manag. Healthc. Policy* **2021**, *14*, 585–594.  
70. Hegde, S.J.; Ng, M.T.M.; Rios, M.; Mahmassani, H.S.; Chen, Y.; Smilowitz, K. Capacity Analysis and Determinants of the Global COVID-19 Vaccine Distribution Process. *Preprint* **2023**.  
71. Youha, S.A.; Alkhamis, M.; Al Mazeedi, S. Using Machine Learning to Unveil Demographic and Clinical Features of COVID-19 Symptomatic and Asymptomatic Patients. *Preprint* **2020**.  
72. Kianfar, N.; Mesgari, M.S.; Mollalo, A.; Kaveh, M. Spatio-temporal modeling of COVID-19 prevalence and mortality using artificial neural network algorithms. *Spat. Spatio-Temporal Epidemiol.* **2022**, *40*, 100471.  
73. Harmouche-Karaki, M.; Mahfouz, M.; Salameh, P.; El Helou, N. Physical Activity Levels and Predictors during COVID-19 Lockdown among Lebanese Adults: The Impacts of Sociodemographic Factors, Type of Physical Activity and Work Location. *Healthcare* **2023**, *11*, 2080.  
74. Baqui, P.; Marra, V.; Alaa, A.M. Comparing COVID-19 risk factors in Brazil using machine learning: The importance of socioeconomic, demographic and structural factors. *Sci. Rep.* **2021**, *11*, 15591.  
75. Sun, S.; Annadi, R.R.; Chaudhri, I.; Munir, K.; Hajagos, J.; Saltz, J.; Hoai, M.; Mallipattu, S.K.; Moffitt, R.; Koraishy, F.M. Short- and Long-Term Recovery after Moderate/Severe AKI in Patients with and without COVID-19. *Kidney360* **2021**, *3*, 242–257.  
76. Cao, Z.; Tang, F.; Chen, C.; Zhang, C.; Guo, Y.; Lin, R.; Huang, Z.; Teng, Y.; Xie, T.; Xu, Y.; et al. Impact of Systematic Factors on the Outbreak Outcomes of the Novel COVID-19 Disease in China: Factor Analysis Study. *J. Med. Internet Res.* **2020**, *22*, e23853.  
77. Rinderknecht, M.D.; Klopfenstein, Y. Predicting critical state after COVID-19 diagnosis: Model development using a large US electronic health record dataset. *NPJ Digit. Med.* **2021**, *4*, 113.  
78. Doblhammer, G.; Kreft, D.; Reinke, C. Regional Characteristics of the Second Wave of SARS-CoV-2 Infections and COVID-19 Deaths in Germany. *Int. J. Environ. Res. Public Health* **2021**, *18*, 10663.  
79. Abbaspour, S.; Robbins, G.K.; Blumenthal, K.G.; Hashimoto, D.; Hopcia, K.; Mukerji, S.S.; Shenoy, E.S.; Wang, W.; Klerman, E.B. Identifying Modifiable Predictors of COVID-19 Vaccine Side Effects: A Machine Learning Approach. *Vaccines* **2022**, *10*, 1747.  
80. Nguyen, H.V.; Byeon, H. Predicting Depression during the COVID-19 Pandemic Using Interpretable TabNet: A Case Study in South Korea. *Mathematics* **2023**, *11*, 3145.  
81. Jiang, Z.; Yin, J.; Han, P.; Chen, N.; Kang, Q.; Qiu, Y.; Li, Y.; Lao, Q.; Sun, M.; Yang, D.; et al. Wavelet transformation can enhance computed tomography texture features: A multicenter radiomics study for grade assessment of COVID-19 pulmonary lesions. *Quant. Imaging Med. Surg.* **2022**, *12*, 4758–4770.  
82. Chadaga, K.; Prabhu, S.; Bhat, V.; Sampathila, N.; Umakanth, S.; Chadaga, R. Artificial intelligence for diagnosis of mild–moderate COVID-19 using haematological markers. *Ann. Med.* **2023**, *55*, 1.  
83. Hu, J.; Han, Z.; Heidari, A.A.; Shou, Y.; Ye, H.; Wang, L.; Huang, X.; Chen, H.; Chen, Y.; Wu, P. Detection of COVID-19 severity using blood gas analysis parameters and Harris hawks optimized extreme learning machine. *Comput. Biol. Med.* **2022**, *142*, 105166.  
84. Kalustian, K.; Ruth, N. Evacuate the Dancefloor: Exploring and classifying Spotify music listening before and during the COVID-19 pandemic in DACH countries. *Jahrb. Musikpsychol.* **2021**, *30*, e95.  
85. Vernikou, S.; Lyras, A.; Kanavos, A. Multiclass sentiment analysis on COVID-19-related tweets using deep learning models. *Neural Comput. Applic.* **2022**, *34*, 19615–19627.  
86. Taye, A.D.; Borga, L.G.; Greiff, S. A machine learning approach to predict self-protecting behaviors during the early wave of the COVID-19 pandemic. *Sci. Rep.* **2023**, *13*, 6121.  
87. Maitre, J.; Bergeron-Leclerc, C.; Maltais, D.; Gaboury, S. *Exploring Anxiety of Qubec University Community during COVID-19 Pandemic via Machine Learning*; Association for Computing Machinery: New York, NY, USA, 2022.  
88. Kareem, A.; Olufemi, A.; Lawal, N. Development of a COVID-19 Patients’ Fatality Prediction System Using Swarm Intelligent Convolution Neural Network. *Asian J. Res. Comput. Sci.* **2023**, *16*, 12–35.  
89. Najaran, M.H.T. A probabilistic meta-heuristic optimisation algorithm for image multi-level thresholding. *Genet. Program Evolvable Mach.* **2023**, *24*, 14.  
90. Mora-Garcia, R.T.; Cespedes-Lopez, M.F.; Perez-Sanchez, V.R. Housing Price Prediction Using Machine Learning Algorithms in COVID-19 Times. *Land* **2022**, *11*, 2100.  
91. Shade, J.; Doshi, A.; Sung, E. Real-Time Prediction of Mortality, Cardiac Arrest, and Thromboembolic Complications in Hospitalized Patients with COVID-19. *JACC Adv.* **2022**, *1*, 100043.  
92. Qiu, Z.; Cao, Z.; Zou, M. The effectiveness of governmental nonpharmaceutical interventions against COVID-19 at controlling seasonal influenza transmission: An ecological study. *BMC Infect. Dis.* **2022**, *22*, 331.  
93. Hasan, M.; Bath, P.A.; Marincowitz, C.; Sutton, L.; Pilbery, R.; Hopfgartner, F.; Mazumdar, S.; Campbell, R.; Stone, T.; Thomas, B.; et al. Pre-hospital prediction of adverse outcomes in patients with suspected COVID-19: Development, application and comparison of machine learning and deep learning methods. *Comput. Biol. Med.* **2022**, *151 (Part A)*, 106024.  
94. Shiri, I.; Mostafaei, S.; Haddadi Avval, A. High-dimensional multinomial multiclass severity scoring of COVID-19 pneumonia using CT radiomics features and machine learning algorithms. *Sci. Rep.* **2022**, *12*, 14817.  
95. Thimoteo, L.M.; Vellasco, M.M.; Amaral, J. Explainable Artificial Intelligence for COVID-19 Diagnosis Through Blood Test Variables. *J. Control Autom. Electr. Syst.* **2022**, *33*, 625–644.  
96. Xu, M.; Ouyang, L.; Han, L.; Sun, K.; Yu, T.; Li, Q.; Tian, H.; Safarnejad, L.; Zhang, H.; Gao, Y.; et al. Accurately Differentiating Between Patients with COVID-19, Patients with Other Viral Infections, and Healthy Individuals: Multimodal Late Fusion Learning Approach. *J. Med. Internet Res.* **2021**, *23*, e25535.  
97. Yagin, F.H.; Cicek, I.B.; Alkhateeb, A.; Yagin, B.; Colak, C.; Azzeh, M.; Akbulut, S. Explainable artificial intelligence model for identifying COVID-19 gene biomarkers. *Comput. Biol. Med.* **2023**, *154*, 106619.  
98. Du, H.; Dong, E.; Badr, H.S.; Petrone, M.E.; Grubaugh, N.D.; Gardner, L.M. Incorporating variant frequencies data into short-term forecasting for COVID-19 cases and deaths in the USA: A deep learning approach. *eBioMedicine* **2023**, *89*.  
99. Cardoso, M.; Cavalheiro, A.; Borges, A.; Duarte, A.F.; Soares, A.; Pereira, M.; Nunes, N.J.; Azevedo, L.; Oliveira, A. *Modeling the Geospatial Evolution of COVID-19 Using Spatio-Temporal Convolutional Sequence-to-Sequence Neural Networks*; Association for Computing Machinery: New York, NY, USA, 2022.  
100. Sengupta, S.; Loomba, J.; Sharma, S.; Brown, D.E.; Thorpe, L.; Haendel, M.A. Analyzing historical diagnosis code data from NIH N3C and RECOVER Programs using deep learning to determine risk factors for Long Covid. In *Proceedings of the 2022 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*, Las Vegas, NV, USA, 6–8 December 2022; pp. 2797–2802.  
101. Li, A.; Yadav, N. An Adaptable LSTM Network Predicting COVID-19 Occurrence Using Time Series Data. In *Proceedings of the 2021 IEEE International Conference on Digital Health (ICDH)*, Chicago, IL, USA, 5–10 September 2021; pp. 172–177.  
102. Zhang, Y.; Tang, S.; Yu, G. An interpretable hybrid predictive model of COVID-19 cases using autoregressive model and LSTM. *Sci. Rep.* **2023**, *13*, 6708.  
103. Segovia-Dominguez, I.; Zhen, Z.; Wagh, R.; Lee, H.; Gel, Y.R. Tlife-LSTM: Forecasting Future COVID-19 Progression with Topological Signatures of Atmospheric Conditions. In *Advances in Knowledge Discovery and Data Mining*; Karlapalem, K., Cheng, H., Ramakrishnan, N., Agrawal, R.K., Reddy, P.K., Srivastava, J., Chakraborty, T., Eds.; PAKDD 2021; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2021; Volume 12712.  
104. Alqaissi, E.; Alotaibi, F.; Ramzan, M.S. Graph data science and machine learning for the detection of COVID-19 infection from symptoms. *PeerJ Comput. Sci.* **2023**, *9*, e1333.  
105. Fritz, C.; Dorigatti, E.; Rügamer, D. Combining Graph Neural Networks and Spatio-temporal Disease Models to Predict COVID-19 Cases in Germany. *arXiv* **2021**, arXiv:2101.00661.  
106. Karthikeyan, A.; Garg, A.; Vinod, P.K.; Deva Priyakumar, U. Machine Learning Based Clinical Decision Support System for Early COVID-19 Mortality Prediction. *Front. Public Health* **2021**, *9*, 626697.  
107. Fawcett, T. An Introduction to ROC Analysis. *Pattern Recognit. Lett.* **2006**, *27*, 861–874.  
108. Powers, D.M.W. Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation. *J. Mach. Learn. Technol.* **2011**, *2*, 37–63.  
109. Bottrighi, A.; Pennisi, M.; Roveta, A. A machine learning approach for predicting high risk hospitalized patients with COVID-19 SARS-CoV-2. *BMC Med. Inform. Decis. Mak.* **2022**, *22*, 340.  
110. Hong, W.; Zhou, X.; Jin, S.; Lu, Y.; Pan, J.; Lin, Q.; Yang, S.; Xu, T.; Basharat, Z.; Zippi, M.; et al. A Comparison of XGBoost, Random Forest, and Nomogram for the Prediction of Disease Severity in Patients with COVID-19 Pneumonia: Implications of Cytokine and Immune Cell Profile. *Front. Cell. Infect. Microbiol.* **2022**, *12*, 819267.  
111. Nopour, R.; Kazemi-Arpanahi, H.; Shanbehzadeh, M.; Azizifar, A. Performance analysis of data mining algorithms for diagnosing COVID-19. *J. Educ. Health Promot.* **2021**, *10*, 405.  
112. Onari, M.A.; Nobile, M.S.; Grau, I.; Fuchs, C.; Zhang, Y.; Boer, A.; Scharnhorst, V. Comparing Interpretable AI Approaches for the Clinical Environment: An Application to COVID-19. In *Proceedings of the 2022 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB)*, Ottawa, ON, Canada, 15–17 August 2022; pp. 1–8.  
113. Schiesser, L.; Witschel, H.F.; De La Harpe, A. Uncovering Cross-Platform Spreading Patterns of Fake News about COVID-19. In *Proceedings of Society 5.0 Conference*; EasyChair: Stockport, UK, 2023.  
114. Seguel, R.J.; Gallardo, L.; Osses, M.; Rojas, N.Y.; Nogueira, T.; Menares, C.; Andrade, M.; Belalcázar, L.C.; Carrasco, P. Photochemical sensitivity to emissions and local meteorology in Bogotá, Santiago, and São Paulo: An analysis of the initial COVID-19 lockdowns. *Elem. Sci. Anth.* **2022**, *10*, 00044.  
115. Moslehi, S.; Mahjub, H.; Farhadian, M. Interpretable generalized neural additive models for mortality prediction of COVID-19 hospitalized patients in Hamadan, Iran. *BMC Med. Res. Methodol.* **2022**, *22*, 339.  
116. Zhou, J.; Tse, G.; Lee, S.; Liu, T.; Wu, W.K.K.; Cao, Z.; Zeng, D.D.; Chi Kei Wong, I.; Zhang, Q.; Yung Cheung, B.M. *Identifying Main and Interaction Effects of Risk Factors to Predict Intensive Care Admission in Patients Hospitalized with COVID-19: A Retrospective Cohort Study in Hong Kong*; Cold Spring Harbor Laboratory Press: New York, NY, USA, 2020.  
117. Derevitskii, I.V.; Mramorov, N.D.; Usoltsev, S.D.; Kovalchuk, S.V. Hybrid Bayesian Network-Based Modeling: COVID-19-Pneumonia Case. *J. Pers. Med.* **2022**, *12*, 1325.  
118. Fan, Y.; Liu, M.; Sun, G. An interpretable machine learning framework for diagnosis and prognosis of COVID-19. *PLoS ONE* **2023**, *18*, e0291961.  
119. Rabby, G.; Berka, P. Multi-class classification of COVID-19 documents using machine learning algorithms. *J. Intell. Inf. Syst.* **2023**, *60*, 571–591.  
120. Saleh, N.I.; Ghani, H.A.; Jilani, Z. Defining factors in hospital admissions during COVID-19 using LSTM-FCA explainable model. *Artif. Intell. Med.* **2022**, *132*, 102394.  
121. Alharbi, R.; Chan-Olmsted, S.; Chen, H.; Thai, M.T. Cultural-aware Machine Learning based Analysis of COVID-19 Vaccine Hesitancy. *arXiv* **2023**, arXiv:2304.06953.  
122. Jana, A.; Minacapelli, C.D.; Rustgi, V.; Metaxas, D. Global and local interpretation of black-box machine learning models to determine prognostic factors from early COVID-19 data. In *Proceedings of the SPIE 12088, 17th International Symposium on Medical Information Processing and Analysis*, Campinas, Brazil, 17–19 November 2021; p. 120880A.  
123. Gao, X.W.; Gao, A. COVID-CBR: A Deep Learning Architecture Featuring Case-Based Reasoning for Classification of COVID-19 from Chest X-Ray Images. In *Proceedings of the 2021 20th IEEE International Conference on Machine Learning and Applications (ICMLA)*, Pasadena, CA, USA, 13–16 December 2021; pp. 1319–1324.  
124. Mahmoudi, S.A.; Stassin, S.; Daho, M.E.H.; Lessage, X.; Mahmoudi, S. Explainable Deep Learning for Covid-19 Detection Using Chest X-ray and CT-Scan Images. In *Healthcare Informatics for Fighting COVID-19 and Future Epidemics. EAI/Springer Innovations in Communication and Computing*; Garg, L., Chakraborty, C., Mahmoudi, S., Sohmen, V.S., Eds.; Springer: Cham, Switzerland, 2022.  
125. Suri, J.S.; Agarwal, S.; Chabert, G.L.; Carriero, A.; Paschè, A.; Danna, P.S.C.; Saba, L.; Mehmedović, A.; Faa, G.; Singh, I.M.; et al. COVLIAS 2.0-cXAI: Cloud-Based Explainable Deep Learning System for COVID-19 Lesion Localization in Computed Tomography Scans. *Diagnostics* **2022**, *12*, 1482.  
126. Islam, M.K.; Zhu, D.; Liu, Y.; Erkelens, A.; Daniello, N.; Fox, J. Interpreting County Level COVID-19 Infection and Feature Sensitivity using Deep Learning Time Series Models. *arXiv* **2022**, arXiv:2210.03258.  
127. Jing, N.; Shi, Z.; Hu, Y. Cross-sectional analysis and data-driven forecasting of confirmed COVID-19 cases. *Appl. Intell.* **2022**, *52*, 3303–3318.  
128. Nazir, A.; Ampadu, H.K. Interpretable deep learning for the prediction of ICU admission likelihood and mortality of COVID-19 patients. *PeerJ Comput. Sci.* **2022**, *8*, e889.  
129. Nader, I.W.; Zeilinger, E.L.; Jomar, D. Onset of effects of non-pharmaceutical interventions on COVID-19 infection rates in 176 countries. *BMC Public Health* **2021**, *21*, 1472.  
130. Balogh, A.; Harman, A.; Kreuter, F. Real-Time Analysis of Predictors of COVID-19 Infection Spread in Countries in the European Union through a New Tool. *Int. J. Public Health* **2022**, *67*, 1604974.  
131. Zhou, C.; Wheelock, A.M.; Zhang, C.; Ma, J.; Dong, K.; Pan, J.; Li, Z.; Liang, W.; Gao, J.; Xu, L. The role of booster vaccination in decreasing COVID-19 age-adjusted case fatality rate: Evidence from 32 countries. *Front. Public Health* **2023**, *11*, 1150095.  
132. Zheng, H.L.; An, S.Y.; Qiao, B.J. A data-driven interpretable ensemble framework based on tree models for forecasting the occurrence of COVID-19 in the USA. *Environ. Sci. Pollut. Res.* **2023**, *30*, 13648–13659.  
133. Bakkeli, N.Z. Predicting COVID-19 exposure risk perception using machine learning. *BMC Public Health* **2023**, *23*, 1377.  
134. Paul, A.; Englert, P.; Varga, M. Socio-economic disparities and COVID-19 in the USA. *J. Phys. Complex.* **2021**, *2*, 035017.  
135. Arik, S.Ö.; Shor, J.; Sinha, R. A prospective evaluation of AI-augmented epidemiology to forecast COVID-19 in the USA and Japan. *NPJ Digit. Med.* **2021**, *4*, 146.  
136. Dlamini, W.M.D.; Simelane, S.P.; Nhlabatsi, N.M. Bayesian network-based spatial predictive modelling reveals COVID-19 transmission dynamics in Eswatini. *Spat. Inf. Res.* **2022**, *30*, 183–194.  
137. Ren, X.; Mi, Z.; Georgopoulos, P.G. Socioexposomics of COVID-19 across New Jersey: A comparison of geostatistical and machine learning approaches. *J. Expo. Sci. Environ. Epidemiol.* **2023**, *34*, 197–207.  
138. Zeng, W.; Gautam, A.; Huson, D.H. On the Application of Advanced Machine Learning Methods to Analyze Enhanced, Multimodal Data from Persons Infected with COVID-19. *Computation* **2021**, *9*, 4.  
139. Flores, C.; Taramasco, C.; Lagos, M.E.; Rimassa, C.; Figueroa, R. A Feature-Based Analysis for Time-Series Classification of COVID-19 Incidence in Chile: A Case Study. *Appl. Sci.* **2021**, *11*, 7080.  
140. Zopluoglu, C. Detecting Examinees With Item Preknowledge in Large-Scale Testing Using Extreme Gradient Boosting (XGBoost). *Educ. Psychol. Meas.* **2019**, *79*, 931–961.  
141. Molnar, C. *Interpretable Machine Learning.* Leanpub: Victoria, BC, Canada, 2020; Available online: https://leanpub.com/interpretable-machine-learning (accessed on 18 June 2024).  
142. Vega, R.; Flores, L.; Greiner, R. SIMLR: Machine Learning inside the SIR Model for COVID-19 Forecasting. *Forecasting* **2022**, *4*, 72–94.  
143. Banerjee, T.; Paul, A.; Srikanth, V. Causal connections between socioeconomic disparities and COVID-19 in the USA. *Sci. Rep.* **2022**, *12*, 15827.  
144. Solayman, S.; Aumi, S.A.; Mery, C.S.; Mubassir, M.; Khan, R. Automatic COVID-19 prediction using explainable machine learning techniques. *Int. J. Cogn. Comput. Eng.* **2023**, *4*, 36–46.  
145. Raissi, M.; Perdikaris, P.; Karniadakis, G.E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *J. Comput. Phys.* **2019**, *378*, 686–707.  
146. Ricky, T.; Chen, Q.; Rubanova, Y.; Bettencourt, J.; Duvenaud, D. Neural Ordinary Differential Equations. *arXiv* **2019**, arXiv:1806.07366.  
147. Schiassi, E.; De Florio, M.; D’Ambrosio, A.; Mortari, D.; Furfaro, R. Physics-Informed Neural Networks and Functional Interpolation for Data-Driven Parameters Discovery of Epidemiological Compartmental Models. *Mathematics* **2021**, *9*, 2069.  
148. Hu, H.; Kennedy, C.M.; Kevrekidis, P.G.; Zhang, H.-K. A Modified PINN Approach for Identifiable Compartmental Models in Epidemiology with Application to COVID-19. *Viruses* **2022**, *14*, 2464.  
149. Kosma, C.; Nikolentzos, G.; Panagopoulos, G.; Steyaert, J.-M.; Vazirgiannis, M. Neural Ordinary Differential Equations for Modeling Epidemic Spreading. *Trans. Mach. Learn. Res.* **2023**. Available online: https://openreview.net/forum?id=yrkJGne0vN (accessed on 18 June 2024).  
150. Brunese, L.; Mercaldo, F.; Reginelli, A.; Santone, A. Explainable Deep Learning for Pulmonary Disease and Coronavirus COVID-19 Detection from X-rays. *Comput. Methods Programs Biomed.* **2020**, *196*, 105608.  
151. Olaide, N.; Absalom, E. A case-based reasoning framework for early detection and diagnosis of novel coronavirus. *Inform. Med. Unlocked* **2020**, *20*, 100395.  
152. Rawat, D.; Sharma, S.; Bhadula, S. Case based Reasoning Technique in Digital Diagnostic System for Lung Cancer Detection. In *Proceedings of the 2023 8th International Conference on Communication and Electronics Systems (ICCES)*, Coimbatore, India, 1–3 June 2023; pp. 1355–1361.  
153. Phongthit, N.; Taeprasartsit, P. Prediction Performance and Explainability of COVID-19 Classification Models. In *Proceedings of the 2021 25th International Computer Science and Engineering Conference (ICSEC)*, Chiang Rai, Thailand, 18–20 November 2021; pp. 383–387.  
154. Zhou, J.; Gandomi, A.H.; Chen, F. Evaluating the quality of machine learning explanations: A survey on methods and metrics. *Electronics* **2021**, *10*, 593.  
155. MacKay, D.J. A practical Bayesian framework for backpropagation networks. *Neural Comput.* **1992**, *4*, 448–472.  
156. Ali, H.; Shah, Z. Combating COVID-19 Using Generative Adversarial Networks and Artificial Intelligence for Medical Images: Scoping Review. *JMIR Med. Inform.* **2022**, *10*, e37365.  
157. Li, Z.; Zhang, J.; Li, B.; Gu, X.; Luo, X. COVID-19 diagnosis on CT scan images using a generative adversarial network and concatenated feature pyramid network with an attention mechanism. *Med. Phys.* **2021**, *48*, 4334–4349.  

---

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
