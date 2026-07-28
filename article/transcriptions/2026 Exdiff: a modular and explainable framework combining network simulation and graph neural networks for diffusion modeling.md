**Social Network Analysis and Mining (2026) 16:3**  
https://doi.org/10.1007/s13278-025-01556-2

**ORIGINAL ARTICLE**

# Exdiff: a modular and explainable framework combining network simulation and graph neural networks for diffusion modelling

**Annamaria Defilippo¹ · Ugo Lomoio¹ · Barbara Puccio¹ · Pierangelo Veltri² · Pietro Hiram Guzzi¹**

Annamaria Defilippo, Ugo Lomoio and Barbara Puccio have contributed equally to this work.  
Extended author information available on the last page of the article.

Received: 20 August 2025 / Revised: 16 October 2025 / Accepted: 7 November 2025  
© The Author(s) 2025

---

### Abstract
Understanding and modelling diffusion processes in complex networks is critical across disciplines, including epidemiology, sociology, and information science. Despite considerable progress, existing approaches often struggle to balance predictive accuracy with interpretability, constraining their applicability in real-world decision-making. ExDiff is introduced as an interactive and modular computational framework that integrates network simulation, Graph Neural Networks (GNNs), and eXplainable Artificial Intelligence (XAI) to both model and elucidate diffusion dynamics. By combining classical compartmental models with deep learning architectures, ExDiff captures the structural and temporal features of diffusion across heterogeneous network topologies. The framework includes modules designed for network analysis, neural modelling, simulation, and interpretability. Its effectiveness is demonstrated through applications to epidemic modelling, including simulation of disease spread, evaluation of intervention strategies, and identification of structural drivers of contagion via XAI techniques. The framework is available in the following GitHub repository: [https://github.com/hguzzi/ExDiff.git](https://github.com/hguzzi/ExDiff.git).

### Graphical Abstract
![Graphical Abstract](https://placeholder.link/graphical_abstract)
*Diagram breakdown: Complex network & Compartmental model (S, I, R, V, D) $\rightarrow$ Graph Neural Network & Captum XAI methods $\rightarrow$ Targeted interventions*

**Keywords:** Network simulation · Diffusion modelling · Graph theory · Explainable artificial intelligence · Stochastic processes

Published online: 24 December 2025

---

## 1 Introduction

Understanding, predicting and controlling complex systems is a key scientific challenge, and computational models serve as crucial bridges between theory and practice by enabling the simulation of dynamic phenomena across domains (Zitnik et al. 2024; Shahrabi et al. 2025; Vespignani 2012).

Diffusion processes on networks underpin a wide array of real-world phenomena, from information propagation in digital ecosystems to pathogen transmission in biological populations (Guzzi et al. 2022b, a; Fortunato and Castellano 2012). In technological systems, such models are crucial for tracing innovation spread and identifying vulnerabilities in interconnected infrastructures (Petrizzelli et al. 2022). In ecological and environmental sciences, diffusion modelling sheds light on species interactions and ecosystem resilience (De Domenico et al. 2016). Simulating these processes through compact, tractable models allows emergent behaviours to be replicated and system responses to perturbations anticipated, providing a quantitative foundation for evidence-based interventions (Humphreys 2002).

Classical compartmental models provide analytical simplicity in modelling diffusion phenomena such as disease spread (Zitnik et al. 2024), but they overlook the heterogeneous, networked nature of real interactions (Petrizzelli et al. 2022; Guzzi and Milenković 2018). The COVID-19 pandemic has highlighted these limitations, motivating the development of contact-based models that combine compartmental dynamics with network theory for more realistic representations of diffusion processes (Alguliyev et al. 2021; Bryant and Elofsson 2020; Karaivanov 2020; Zaplotnik et al. 2020; Patil et al. 2021; Chow et al. 2021). Recent studies have integrated mobility data and social behaviour into epidemic forecasting. For instance, deep learning models optimised through evolutionary algorithms have been applied to quantify the impact of social distancing on epidemic dynamics, showing improved predictive accuracy and reduced computational cost (Liu et al. 2022). Similarly, mobility-informed frameworks demonstrate how heterogeneous movement patterns shape epidemic trajectories and intervention outcomes (Lu et al. 2025a). Additionally, the emergence of data-centric pipelines has consolidated multimodal and hybrid approaches (Rodriguez et al. 2024). Finally, outbreak detection methods based on interpretable machine learning have proven effective in anticipating epidemic waves, providing standards for early-warning systems (Cho et al. 2023). Despite these advances, a critical gap remains: many existing tools lack accessibility for non-expert users and fall short in offering the interpretability, flexibility, and analytical depth required for contemporary network analysis. While platforms such as NDLib (Rossetti et al. 2018) offer useful web-based interfaces, they provide limited support for embedding-based inference, node-level classification, and explainable outputs (Fig. 1).

![Fig. 1 Visual Abstract](https://placeholder.link/fig1)  
**Fig. 1 Visual Abstract:** ExDiff is an integrated system combining network simulations, modelling, and GNN analysis, using explainable AI to interpret diffusion dynamics across complex networks. It simulates disease progression with the SIRVD model and identifies contagion determinants, providing researchers with a powerful framework for exploring diffusion processes through both predictive and interpretable perspectives, enabling targeted interventions.

To address these limitations, this study introduces ExDiff (Explainable Graph Neural Network Framework for Diffusion Processes Modelling), a unified and accessible platform for simulating and analysing diffusion dynamics in complex networks. Unlike existing tools, ExDiff is not a mere aggregation of components but an end-to-end architecture that combines: (i) a modular framework bridging classical diffusion dynamics with interpretable machine learning; (ii) a novel explanation layer that quantifies feature influence at each diffusion step, ensuring transparency of predictions; and (iii) a standardized evaluation protocol for explainability in generative epidemic models. ExDiff integrates classical compartmental modelling with explainable Graph Neural Networks (GNNs) (Scarselli et al. 2009), enabling interpretable and scalable predictions across heterogeneous network topologies. Designed for broad applicability, ExDiff supports the simulation of diverse diffusion phenomena, such as information spread, epidemic contagion, and behavioural adoption, across structurally complex systems. The framework delivers actionable insights for domains including epidemiology, marketing, and cybersecurity. By embedding advanced deep learning techniques (Leskovec et al. 2010; Guzzi and Zitnik 2022; Cho et al. 2013), ExDiff enables node embedding, classification, and the identification of structurally influential nodes or edges, facilitating the design of targeted intervention strategies. Beyond its modular architecture, ExDiff demonstrates its versatility through real-world applications. In epidemic modelling, for example, it has been employed to simulate disease spread, assess intervention strategies, and identify key structural drivers of contagion using explainable AI techniques.

---

## 2 Background and related work

This section discusses the main related concepts such as compartmental models, GNNs, and eXplainable Artificial Intelligence (XAI). A comparison with state-of-the-art computational frameworks is also provided to highlight the contributions of ExDiff.

### 2.1 Compartmental models
Compartmental models are theoretical framework for simulating the diffusion of an agent into a population. The population is subdivided into different classes (or compartments) and the *homogeneous mixing* hypothesis is hold, i.e. each individual has the same probability of contact with anyone. Examples of compartmental models used in epidemiology are the Susceptible-Infectious-Susceptible (SIS), in which population is subdivided in two groups, the Susceptible-Infectious-Recovered (SIR) (Kermack and McKendrick 1927), that use three compartments, that has been extended to consider also vaccinated in the Susceptible-Infectious-Recovered-Vaccinated (SIRV) model.

A main limitation of classical compartmental models lies in their assumption of homogeneous mixing, where individuals interact with equal probability. In contrast, *contact-based models* incorporate network structures that capture the heterogeneity of real-world interactions, representing individuals as nodes and their relationships as edges (Guzzi et al. 2022c).

A defining feature of these models is the integration of diffusion dynamics, typically derived from classical compartmental frameworks, with contact patterns encoded in temporal networks. In these networks, nodes represent individuals and edges denote time-resolved contacts between them (Ajelli et al. 2010). Each node is assigned a label corresponding to its epidemiological state (e.g., susceptible, infected, recovered), allowing the system’s evolution to reflect both the structure of interpersonal interactions and the probabilistic transitions dictated by the compartmental model. Transitions between states are governed by the model parameters and the occurrence of effective contacts, thereby linking diffusion dynamics directly to the underlying network topology (Liu et al. 2018). Beyond epidemiological applications, diffusion processes are central to understanding the propagation of information, behaviour, and influence in digital ecosystems. A particular focus has been placed on identifying high-impact nodes, or *super-spreaders*, whose structural position enables disproportionate influence on diffusion dynamics (Pastor-Satorras and Vespignani 2001).

### 2.2 Graph neural networks and explainable artificial intelligence
GNNs (Scarselli et al. 2008) have emerged as state-of-the-art tools for learning from graph-structured data by leveraging message-passing mechanisms to propagate and aggregate information across node neighbourhoods (Defilippo et al. 2024a). These architectures have demonstrated strong performance in tasks such as node classification, link prediction, and community detection, effectively capturing both local and global topological patterns (Defilippo et al. 2024b).

XAI encompasses methods designed to enhance the transparency and interpretability of Artificial Intelligence (AI) models (Adadi and Berrada 2018). With the increasing adoption of GNNs in applications requiring accountability, XAI techniques for graph data have advanced rapidly. These methods provide insights into how structural and feature-level patterns influence model outputs, supporting applications ranging from molecular analysis to social network dynamics and epidemiological forecasting. Captum (Kokhlikyan et al. 2020), an open-source library within the PyTorch ecosystem, offers a comprehensive suite of interpretability techniques, including Integrated Gradients and Saliency Maps. Such tools enable quantification of the contributions of features, nodes, and edges to model predictions, facilitating the alignment of predictive performance with human interpretability in graph-based learning.

### 2.3 State-of-the-art computational frameworks
A diverse range of computational frameworks has been developed to model diffusion processes in complex networks, each tailored to specific research needs. Table 1 provides a comparative overview of leading tools. NDLib (Rossetti et al. 2018), built on NetworkX, offers an accessible interface for simulating epidemic and opinion dynamics, supporting reproducible experimentation. Other specialised tools include *GLEaMviz* (Broeck et al. 2011) for large-scale epidemic simulations, *GEMF-sim* (Sahneh et al. 2017) for multi-platform stochastic simulations, and *EpiModel* (Jenness et al. 2018), an R-based environment for dynamic network modelling. Moreover, recent advances in data-centric pipelines proposed the integration of explainable AI with epidemic forecasting, where multimodal data sources such as mobility, policy interventions, and genomic surveillance are combined to enhance predictive performance (Rodriguez et al. 2024). Graph-based deep learning has also been proposed to model diffusion under sparse or noisy mobility data, facilitating the identification of high-risk areas and structurally influential nodes (Lu et al. 2025b). As summarised in Table 1, existing platforms typically lack integrated support for node embeddings, classification tasks, and interpretability features. Addressing these limitations, ExDiff introduces a unified framework that combines epidemic simulation with GNN architectures and XAI methods, enabling scalable, interpretable analysis of diffusion dynamics in complex networks.

Therefore, taken together, the integration of advanced GNN architectures with epidemiological diffusion models, particularly within multiplex and temporal network frameworks, offers a powerful toolkit for analysing complex systems. These hybrid approaches enable researchers to move beyond static, homogeneous assumptions, illuminating how structural and temporal variability jointly shape diffusion trajectories. Such insights hold promise for guiding effective interventions across diverse domains, including healthcare, communication, and infrastructure resilience.

**Table 1** Qualitative comparison of network diffusion-related frameworks for simulating diffusion processes on complex networks

| Framework | Visualisation tools | Dynamic network support | Experiment server | Visual interface | Extensible | GNN analysis | XAI methods |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| NDlib (Rossetti et al. 2018) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| Epigrass (Coelho et al. 2008) | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| GEMF-sim (Sahneh et al. 2017) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Nepidemix (Ahrenberg et al. 2016) | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| EoN (Miller and Ting 2020) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| EpiModel (Jenness et al. 2018) | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| GLEaMviz (Broeck et al. 2011) | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| NEXT-Net (Cure et al. 2024) | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| EpiPredict (Suer et al. 2024) | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| CyNetDiff (Robson et al. 2024) | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| Epydemic¹ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Nxsim² | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| RECON³ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Sisspread⁴ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **ExDiff** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |

¹ Epydemic: https://goo.gl/PrPHh4  
² Nxsim: https://goo.gl/U2rDvv  
³ RECON: https://goo.gl/eYMDqh  
⁴ Sisspread: https://goo.gl/LSWsUh  

---

## 3 System architecture

The architecture of ExDiff consists of five modular components, each responsible for a distinct stage in the modelling and analysis of diffusion processes:

I. Network Analysis Module,  
II. Simulation Module,  
III. Graph Neural Network (GNN) Analysis Module,  
IV. eXplainable Artificial Intelligence (XAI) Module,  
V. XAI-Guided Interventions Module.  

Rather than operating in isolation, these modules are designed as an interconnected pipeline: the output of each stage serves as the input for the next, ensuring a coherent flow from structural network characterization to simulation, predictive modelling, interpretability, and ultimately intervention design. This integration provides a unified framework that supports the configuration and execution of experiments as well as the transparent interpretation of their outcomes (Fig. 2). To facilitate usability and accessibility, the framework features an interactive interface implemented in Google Colab. This interface streamlines the entire workflow, from network generation and simulation setup to GNN training, evaluation, and interpretation.

![Fig. 2 Framework Overview](https://placeholder.link/fig2)  
**Fig. 2 Overview of the modular framework for network-based epidemic modelling and intervention analysis.** The system integrates five interconnected modules: I. the Network Analysis Module, built on NetworkX, provides generation, manipulation, and structural assessment of contact networks; II. the Simulation Module implements customizable compartmental models and supports scenario-based simulations including targeted or random vaccination strategies; III. the Graph Neural Network (GNN) Analysis Module uses PyTorch Geometric to perform node classification and embedding extraction from evolving diffusion graphs; IV. the Explainable AI (XAI) Module, powered by Captum, applies techniques such as Integrated Gradients and Saliency Maps to interpret the model’s predictions and quantify node or edge relevance; V. the XAI-Guided Interventions Module enables the structural reconfiguration of the network based on attribution scores to design and test containment strategies. All these modules are available in an intuitive Graphical User Interface (GUI) hosted in Google Colab, which guides users through the full modelling pipeline, including parameter configuration, visualisation, and export of simulation results. Together, these components enable dynamic, interpretable, and reproducible simulations for epidemic forecasting and decision support in biomedical contexts.

Users can configure model parameters, initiate simulations, and visualise results in a guided, notebook-based environment that requires no prior software installation. This design lowers the barrier to entry for non-specialists while maintaining the flexibility needed by advanced users. To ensure reproducibility, traceability, and integration with broader computational pipelines, the system supports persistent storage via Google Drive and uses standardized data formats. Simulation configurations are saved in *JSON*, network structures in *GraphML*, and graphical outputs in *PNG*. These export options facilitate cross-platform compatibility, collaborative research, and long-term archiving of simulation experiments. Furthermore, this modular design enables easy reloading and extension of previous runs, promoting iterative refinement and comparative analyses.

### 3.1 Network analysis module
Built upon the widely adopted NetworkX library ([https://networkx.org/](https://networkx.org/)), this module provides comprehensive support for the construction, analysis, and manipulation of graph-based representations. Users can generate a variety of synthetic network models, including Erdös-Rényi, Barabási-Albert, Watts–Strogatz, Random Geometric, and Stochastic Block Models, to simulate different types of social structures. The module offers an extensive suite of analytical tools for computing structural metrics such as clustering coefficients, and shortest path length. In addition, basic visualisation capabilities facilitate the exploration and inspection of network topology. This foundational module is essential for initializing the simulation environment and for preparing input graphs for downstream learning and intervention tasks.

### 3.2 Simulation module
Using the previously generated graph as input, this component functions as a versatile engine for simulating the spread of infectious diseases across dynamic and heterogeneous contact networks. Designed for modularity and extensibility, it supports user-defined compartmental models (e.g., SIR, SIRV, SIRVD), transition rules, and behavioural adaptations such as vaccine uptake or quarantine. The module enables node updates and accommodates temporal dynamics, making it suitable for simulating real-world epidemic processes. One of its defining features is the ability to implement and compare various immunisation strategies, including no vaccination, uniform random vaccination, and targeted vaccination schemes based on node centrality or model-derived relevance scores. Such structural interventions, along with optional edge or node removal, allow users to assess the efficacy of different containment policies under diverse epidemiological and topological conditions.

### 3.3 Graph neural network (GNN) analysis module
Implemented using *PyTorch* and the *PyTorch Geometric* framework, this module facilitates deep learning on graph-structured data, enabling both node-level classification and the extraction of low-dimensional node embeddings.

The default architecture is based on Graph Convolutional Networks (GCNs) (Kipf and Welling 2017), incorporating convolutional layers followed by non-linear activations and a softmax output for classification. Users can fine-tune architectural and training parameters such as the number of layers, hidden units, learning rate, and training epochs. To support interpretability and downstream tasks, learned node embeddings can be visualized using dimensionality reduction methods like UMAP or t-SNE. This module serves as a bridge between raw network topology and predictive analytics, enhancing the system’s capacity for pattern recognition and inference.

Each simulation instance is represented as a graph $G = (V, E)$, constructed from the contact network generated in previous modules, where nodes correspond to individuals and edges represent potential contacts or transmission pathways. For each node $v_i \in V$, a feature vector $x_i$ is derived from the previous simulation state $(t - 1)$ and local neighborhood statistics. The GCN learns latent node representations through stacked graph convolutions and nonlinear transformations. The adopted architecture consists of:

* Two `GraphConv` layers with ReLU activations, performing message passing and aggregation across the network;
* A fully connected (linear) layer projecting the hidden representations into a lower-dimensional latent space;
* A final classification layer producing softmax-normalized class probabilities.

The parameters controlling the number of hidden channels, output embedding dimension, learning rate, and training epochs are user-configurable. Specifically, for synthetic datasets, multiple architectural configurations were systematically tested to evaluate model robustness across different network structures. For real-world datasets, the configuration achieving the most stable performance was adopted, with hidden dimension set to 32, output embedding dimension to 16, and a learning rate of 0.002. Training is performed using the *Adam* optimizer and a weighted cross-entropy loss, where class weights are computed dynamically based on label frequencies to address class imbalance. A 70/30 node-level train/test split is applied, using stratified sampling when class distributions permit.

### 3.4 Explainable artificial intelligence (XAI) module
Model evaluation and interpretability were conducted through a dedicated analysis module implemented in Python, leveraging standard libraries such as *Captum*, a state-of-the-art library for interpretability in PyTorch-based neural networks. This component enables both quantitative performance assessment and qualitative visualization of model behaviour. This module applies attribution techniques such as Integrated Gradients and Saliency Maps to quantify the contribution of individual nodes and edges to the network’s predictive output. These insights provide a principled understanding of the factors influencing model decisions, helping identify structurally important nodes (e.g., potential super-spreaders) or vulnerable communities. In doing so, the XAI module enables researchers and practitioners to move beyond black-box predictions toward interpretable, data-informed interventions. Both explanation methods are accessible through a user-configurable interface. The *Integrated Gradients* method (Sundararajan et al. 2017) was chosen as the default approach for real-world datasets due to its greater stability and reduced sensitivity to local noise compared to gradient-based saliency techniques. Integrated Gradients compute attributions by integrating gradients along a continuous path from a baseline input to the actual input, resulting in smoother and more interpretable relevance maps. This approach is particularly suitable for epidemiological and graph-structured data, where small local perturbations should not significantly alter global interpretability patterns. Graph-level explanations are visualised using *NetworkX*, where nodes represent individuals and edges encode potential transmission pathways. Edge thickness reflects the magnitude of edge-level attributions, node size scales with degree centrality, and colour corresponds to the predicted epidemiological class. These visualisations provide an interpretable summary of the GCN’s decision process, highlighting key transmission pathways or influential substructures within the network. Outputs can optionally be exported as high-resolution figures for further qualitative analysis.

### 3.5 XAI-guided interventions module
Extending the capabilities of the XAI component, this module translates interpretability insights into actionable intervention strategies. By leveraging node- or edge-level attribution scores, users can selectively remove critical links or vaccinate high-risk individuals identified by the model.

For edge-based interventions, the module ranks edges according to their contribution to the predicted epidemiological outcome (e.g., infection spread) using attribution values obtained from *Integrated Gradients* or *Saliency Maps*. The top-ranked edges are selectively removed from the contact network, and the modified network is used in the simulation. This direct integration enables real-time evaluation of the impact of disrupting critical transmission pathways while maintaining the network’s overall connectivity. Key epidemiological metrics, such as peak infection, total deaths, and epidemic duration, are recorded to quantify intervention efficacy.

For node-based interventions, edge-level attributions are aggregated to compute per-node influence scores, identifying high-risk individuals or potential super-spreaders. The top $K\%$ most influential nodes are then vaccinated, updating their state within the simulation engine while leaving other nodes unchanged. This enables the system to simulate targeted control strategies in real time, assessing their effects on disease dynamics over multiple stochastic realisations. By embedding actionable interventions directly into the simulation workflow, the XAI-Guided Interventions Module forms the operational core of the framework. It allows researchers and policymakers to move beyond passive interpretation, systematically testing and comparing intervention strategies, and generating evidence-driven insights for network-informed epidemiological control. In this way, interpretability is seamlessly coupled with actionable decision-making, closing the loop between model explanation and practical intervention.

---

## 4 Synthetic case studies

The simulations were executed on the Google Colab platform (Bisong 2019), leveraging its accessibility for interactive experimentation and reproducibility. The primary objectives of the case studies included evaluating the framework’s runtime performance, analysing node classification capabilities, and investigating explainability features that illuminate the underlying diffusion dynamics. Model parameters were configured to simulate a realistic outbreak scenario, with customizable options available via the Colab-based interface. Node classification was performed using the GCN model integrated into ExDiff, trained to predict the compartmental state of each node at a given timestep. The classification was tailored to match the states defined by the selected compartmental model, ensuring consistency across various simulations.

As detailed in the case study subsections, the model demonstrated the ability to learn meaningful latent representations of the nodes, effectively distinguishing them by class within the embedded latent space. These results indicate that the neural architecture successfully captures both structural and state-based features of the network across all considered scenarios. To enrich the classification analysis, the explainability module was applied to interpret predictions using methods such as Integrated Gradients and Saliency Map. These tools highlighted key nodes and edges that contribute to infection spread.

Epidemic control generally targets the most "central" nodes (representing individuals) based on measures such as degree, betweenness, and eigenvector centrality to determine the order of vaccination or isolation. The use of GNNs and XAI techniques enhances the detection of super-spreaders and reveals their network connectivity, integrating both structural and contextual insights. For each compartmental model considered, a representative case is described in the following subsections. The presentation of each case follows a consistent structure:

* Simulations using the selected compartmental model, run for 400 steps.
* A final embedding generated by the GNN based on a randomly chosen simulation timestep.
* Visualisation of the applied XAI method insights.
* Results of XAI-guided intervention strategies.

### 4.1 Network generation
Users can select their preferred network model from the list of supported options.

* **Erdös-Rényi (ER) Model** (Zitnik et al. 2024): A random graph where each of the $n$ node pairs is connected with probability $p$. It produces binomial/Poisson degree distributions, lacks clustering, and is used to study phase transitions, such as the emergence of giant components.
* **Barabási-Albert (BA) Model** (Zitnik et al. 2024): A scale-free network generated through preferential attachment. Each new node connects to existing ones with a probability proportional to their degree, forming $m$ edges. This results in hubs and a power-law degree distribution.
* **Watts-Strogatz (WS) Model** (Zitnik et al. 2024): A small-world network created by rewiring edges in a ring lattice of $n$ nodes, each connected to $k_n$ neighbors. Rewiring occurs with probability $p$, balancing clustering and short paths.
* **Random Geometric (RG) Model** (Zitnik et al. 2024): Nodes are randomly placed in a metric space (e.g., unit square) and are connected if the distance is $< r$. This model produces spatial networks with clustering and locality, influenced by the space dimension ($dim$).
* **Stochastic Block (SB) Model** (Zitnik et al. 2024): Divides $n$ nodes into $k$ blocks. Edges form based on a $k \times k$ matrix of probabilities, capturing modular structure and modelling intra-group ($d_{in}$) and inter-group ($d_{out}$) connectivity.

Figure 3 illustrates the key topological differences among the graph models, constructed with 300 nodes as an example, highlighting the networks generated for subsequent simulations. Additionally, Table 2 presents the selected generation parameters and the resulting network characteristics.

![Fig. 3 Synthetic Graph Models](https://placeholder.link/fig3)  
**Fig. 3 Visual comparison of synthetic network models used in the experiments:** (a) Erdos-Rényi (ER) Model, (b) Barabási-Albert (BA) Model, (c) Stochastic Block (SB) Model, (d) Watts-Strogatz (WS) Model, (e) Random Geometric (RG) Model.

These analyses underpin the subsequent learning and simulation tasks by characterising key structural features of the network.

**Table 2** Network statistics and generation parameters for each graph model

| Network model | Nodes | Edges | Clustering coefficient | Shortest path length | Parameters |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Erdos-Rényi | 300 | 4475 | 0.1014 | 1.945 | $p = 0.1$ |
| Barabási-Albert | 300 | 596 | 0.0906 | 3.4318 | $m = 2$ |
| Watts-Strogatz | 300 | 900 | 0.5146 | 5.8116 | $k_n = 6, p = 0.06$ |
| Random geometric | 300 | 2672 | 0.6366 | 4.5801 | $r = 0.15, dim = 2$ |
| Stochastic block | 300 | 8280 | 0.2168 | 1.8155 | $k=3^{(1)}; d_{in} = 0.35, d_{out} = 0.10$ |

*(1) 100 nodes for each community*

### 4.2 SIRVD model
For comprehensive SIRVD simulations, two main objectives are addressed: (I) identify and disrupt super-spreader pathways to reduce infection, (II) evaluate the effectiveness of targeted vaccination strategies informed by the model explainability. In the first case, the simulation compares the outcomes of three immunisation strategies (*no vaccination*, *random vaccination*, and *targeted vaccination*) alongside XAI-based edge removal. It tracks the evolution of infected (“Ih”) and deceased (“Dh”) populations over time. The second scenario implements an XAI-driven vaccination protocol by determining node-level influence. Edge importance scores are aggregated per node, and the top $K\%$ of influential nodes (e.g., top 50%) are identified and vaccinated before simulation begins, in the synthetic case studies. A new run is executed under identical conditions and the results of XAI-guided interventions are benchmarked against the three initial alternatives: no vaccination, random vaccination, and betweenness-centrality-based targeted vaccination.

![Fig. 4 SIRVD Comparative Analysis](https://placeholder.link/fig4)  
**Fig. 4 Comparative analysis of SIRVD model simulations on an Erdös–Rényi (ER) network under three distinct vaccination strategies.** The figure presents the evolution of infected (Ih) and deceased (Dh) individuals over time as simulated on an ER network. Three immunisation strategies are evaluated: **a** No vaccination, which serves as a baseline to observe unmitigated epidemic spread; **b** Random vaccination, where a proportion of nodes is immunized without regard to their position or importance within the network; **c** Targeted vaccination, where high-centrality nodes are selected based on their betweenness centrality scores, representing key individuals in terms of information or disease flow within the network. The comparison highlights how topologically informed interventions (i.e., targeting nodes with high structural influence) can significantly alter epidemic dynamics by lowering infection peaks and reducing cumulative deaths, even within networks with low clustering and no apparent community structure. This demonstrates the relevance of integrating network analysis into public health planning, even when dealing with seemingly homogeneous populations.

For example, the Erdös–Rényi (ER) network was chosen for SIRVD simulations and the subsequent ExDiff-based experiments. Figure 4 presents the results of the three simulation settings applied on the ER network, showing the proportion of subjects in each state across all steps: Susceptible (Sh), Infectious (Ih), Recovered (Rh), Vaccinated (Vh), and Dead (Dh).

The GNN model is applied to the graph representing the system’s state in a random simulation step, resulting in a latent embedding that captures key structural and topological features (see Fig. 5).

![Fig. 5 Node Embedding ER](https://placeholder.link/fig5)  
**Fig. 5 Node embedding for ER network in SIRVD model setting:** This scatter plot illustrates the spatial distribution of node embeddings derived from an Erdös-Rényi (ER) network under the SIRVD simulation framework. Each node is color-coded based on its final epidemiological state. Overall, the embedding visually encapsulates how disease propagation influences structural dynamics and node evolution within synthetic random networks.

Model interpretability was addressed using Saliency Maps that highlighted the most influential edges contributing to the classification of infectious nodes (Ih), as shown in Fig. 6. As explained, XAI-guided interventions included:

* An XAI-based edge removal strategy, which involves removing the most important edges according XAI method,
* An XAI-based vaccination approach, aimed at vaccinating 'super-spreader' nodes, defined as those with high scores based on the most important edges (identified by XAI).

![Fig. 6 Saliency Map ER](https://placeholder.link/fig6)  
**Fig. 6 Saliency map analysis of node-level importance within the Erdös–Rényi (ER) network under the SIRVD epidemic model.** This figure illustrates the application of saliency mapping techniques to identify nodes that most influence the progression of the epidemic in a homogeneous random graph structure. Using a trained Graph Neural Network (GNN), the saliency scores quantify the contribution of each node to the model’s predictive outcome, specifically, the likelihood of transitioning between compartments (e.g., from susceptible to infected). In the ER network, where connections are randomly distributed and clustering is minimal, the saliency map provides insight into which nodes, despite the lack of prominent hubs, emerge as influential due to their position in the spreading process. These highlighted nodes represent potential targets for intervention strategies, demonstrating how model interpretability can uncover critical structures even in networks with limited inherent hierarchy or modularity.

Fig. 7 shows the effect of the XAI-based edge removal strategy, which eliminated the top 50% of the most important edges, on infection (Ih) and death (Dh) rates over time.

Figure 8 illustrates the effect of the XAI-guided targeted vaccination strategy, which involved preemptively vaccinating the top 50% of the most influential nodes identified by aggregated edge importance scores, by tracking infection (Ih) and death (Dh) rates over time.

Both strategies improved infection rates compared to previous strategies and resulted in a moderate reduction in deaths.

![Fig. 7 Edge Removal Effect ER](https://placeholder.link/fig7)  
**Fig. 7 Effect of XAI-based edge removal (top 50%) on infected (Ih) and dead (Dh) over time.** This figure presents the temporal evolution of infected (Ih) and deceased (Dh) populations under a targeted intervention strategy in an Erdös-Rényi (ER) network, guided by explainable artificial intelligence (XAI). This approach leverages attribution scores from a trained Graph Neural Network (GNN) to identify and eliminate the top 50% most influential edges–those most responsible for disease transmission pathways. By preemptively removing these high-impact edges before the simulated outbreak, the strategy disrupts key routes of viral propagation while preserving overall network integrity. This edge-centric strategy exemplifies how XAI can guide structural interventions, offering a scalable tool for optimizing outbreak containment in dynamic networks.

![Fig. 8 Targeted Vaccination ER](https://placeholder.link/fig8)  
**Fig. 8 Impact of explainable AI (XAI)-driven targeted vaccination on epidemic dynamics in the Erdös-Rényi (ER) network.** This figure presents the temporal evolution of the infected (Ih) and deceased (Dh) populations under a targeted immunisation strategy guided by explainable artificial intelligence. The approach leverages attribution scores derived from a trained Graph Neural Network (GNN), identifying the top 50% most influential nodes in terms of their contribution to disease spread. By vaccinating these high-impact individuals prior to the onset of the simulated outbreak, the intervention achieves a marked suppression of infection peaks and a substantial reduction in overall mortality compared to untargeted approaches. The results highlight the potential of XAI-guided strategies to optimize resource allocation in epidemic response, demonstrating that selectively immunizing a relatively small portion of the population, chosen based on learned model insights rather than heuristic centrality, can yield significant epidemiological benefits.

### 4.3 SIS model
In the SIS and SIR simulation settings, explainable artificial intelligence (XAI) techniques were employed to identify and disrupt the super-spreader connections that critically influence contagion dynamics. Leveraging methods such as Saliency Maps and Integrated Gradients, the framework computes an edge attribution mask based on the GNN’s prediction of a target class, typically infected individuals ("Ih"). Edges are ranked according to their influence scores, and the top-ranked connections (e.g., the top 25%) are selectively removed from the network.

Following this XAI-guided intervention, a new simulation is executed under the same initial conditions and parameter settings, enabling a direct comparison between baseline and modified scenarios. This process highlights the tangible impact of structural interventions derived from model interpretability. The framework quantitatively evaluates the difference in infection trajectories, particularly in terms of the proportion of infected individuals over time.

As previously described, the platform supports multiple parameter configurations for infection and recovery probabilities, allowing the simulation of different scenarios, providing a comprehensive view of how XAI-informed structural modifications perform across different epidemic intensities.

Simulating high infection cases, XAI-guided interventions demonstrate their effectiveness in containing the diffusion process, even in this scenario.

Figure 9 presents the results of the simulation setting, simulating a high infection scenario, applied using SIS model on the Watts-Strogatz (WS) graph. It shows the proportion of subjects in each state across all steps.

![Fig. 9 High Infection SIS WS](https://placeholder.link/fig9)  
**Fig. 9 High infection using SIS simulation on a WS network**

The latent embedding of the GNN application is shown in Fig. 10, highlighting key structural and topological features.

![Fig. 10 Node Embedding WS SIS](https://placeholder.link/fig10)  
**Fig. 10 Node embedding for WS network in SIS model setting**

Model interpretability was addressed using integrated gradient that highlighted the most influential edges contributing to the classification of infectious nodes, as shown in Fig. 11.

![Fig. 11 Integrated Gradients WS SIS](https://placeholder.link/fig11)  
**Fig. 11 Integrated Gradient Insights for WS network in SIS model setting**

To assess the impact of explainability-guided interventions on epidemic dynamics, two modified network scenarios were simulated. Figure 12 shows the results after removing the most influential 25% and 75% of the edges based on the learnt attributions of the model.

![Fig. 12 SIS Interventions WS](https://placeholder.link/fig12)  
**Fig. 12 SIS simulations under two XAI-guided intervention scenarios on an WS network.** In each case, the most influential edges, determined by XAI attributions, were removed to simulate targeted epidemic control. The first intervention removed the top 25% of edges, while the second removed 75%: (a) XAI-guided edge removal: top 25% of edges, (b) XAI-guided edge removal: top 75% of edges.

### 4.4 SIR model
In the SIR model experiments, the Random Geometric (RG) network was selected to further explore diffusion dynamics, following the same experimental configuration described in the preceding subsection. As in previous cases, the simulations were conducted under high-transmission conditions to emphasise the network’s role in shaping epidemic progression and to provide a stringent test for intervention strategies.

Figure 13 presents the results of the simulation setting, simulating a high infection scenario, applied using SIR model on the RG graph. It shows the proportion of subjects in each state across all steps.

![Fig. 13 High Infection SIR RG](https://placeholder.link/fig13)  
**Fig. 13 High infection using SIR simulation on a RG network**

The latent embedding of the GNN application is shown in Fig. 14, highlighting key structural and topological features.

![Fig. 14 Node Embedding RG SIR](https://placeholder.link/fig14)  
**Fig. 14 Node embedding for RG network in SIR model setting**

Model interpretability was addressed using saliency maps that highlighted the most influential edges contributing to the classification of infectious nodes, as shown in Fig. 15.

![Fig. 15 Saliency Map RG SIR](https://placeholder.link/fig15)  
**Fig. 15 Saliency Map for RG network in SIR model setting**

Finally, to assess the impact of explainability-guided interventions on epidemic dynamics, two modified network scenarios were simulated. Figure 16 shows the results after removing the most influential 20% and 65% of edges, based on the model’s learned attributions.

![Fig. 16 SIR Intervention RG](https://placeholder.link/fig16)  
**Fig. 16 SIR simulations under two XAI-guided intervention scenarios on an RG network.** In each case, the most influential edges, determined by explainable AI attributions, were removed to simulate targeted epidemic control. The first intervention removed the top 20% of edges, while the second removed 65%: (a) XAI-guided removal: top 20% of edges, (b) XAI-guided removal: top 65% of edges.

### 4.5 Results
Results of first experiments are illustrated in Figs. 7, 12 and 16 and Tables 3, 4 and 5. In both SIS and SIR model, the analysis of the infection rate shows that the peak is significantly lower with the application of XAI guided-edge removal. In the SIS model, Table 3 indicates a reduction in performance from 90.67% to 75.33% after removing 75% of the most important edges. In the SIR model, as shown in Table 4, performance decreases from 67.67% to 59.67% after removing 65% of the most significant edges.

In SIRVD model, the analysis of the infected humans (Ih) (Fig. 7a) reveals that the peak infected proportion remained high across all scenarios, while still showing a slight reduction attributable to the application of XAI. Table 5 reports that No Vaccination reached 99.67%, Targeted Vaccination reached 98.33%, and the XAI-based Edge Removal strategy recorded the lowest peak of 98.00%. In terms of mortality (Dh) (Fig. 7b), as detailed in Table 5, the No Vaccination scenario resulted in 16.67% total deaths. The XAI-based Edge Removal (14.00%) showed an improvement over Random Vaccination (14.67%), while the Targeted Vaccination strategy achieved the lowest mortality rate at 12.33%.

The results of XAI-driver vaccination protocol, which involved vaccinating the top 50% of the most influential nodes (150 nodes), are reported in Fig. 8 and Table 5. The analysis of infection dynamics (Fig. 8a) reveals measurable differences recorded for each strategy. The No Vaccination established a peak infected proportion of 99.67%. While all interventions were applied, the infection peak remained high overall. Random Vaccination resulted in a peak of 98.67%, and the Targeted Vaccination achieved a peak of 98.33%. The XAI Targeted Vaccination strategy yielded the best performance, recording the lowest peak infection rate at 96.00%. In terms of mortality rate (Dh) (Fig. 8b), the XAI Targeted Vaccination strategy resulted in the most significant reduction, achieving a final rate of 11.67%. This marks an improvement over both the Targeted Vaccination (12.33%) and Random Vaccination (14.67%) benchmarks, and a notable decrease from the 16.67% mortality rate observed in the No Vaccination scenario.

**Table 3** SIS XAI-based edge removal of 75% of most critical removal in WS network

| Strategy | Peak of infections | Duration (steps) | Edges removed |
| :--- | :---: | :---: | :---: |
| SIS - High infection | 90.67% | 400 | – |
| XAI - Top 75% edge removal | 75.33% | 400 | 625 |

**Table 4** SIR XAI-based edge removal of 65% of most critical removal in RG network

| Strategy | Peak of infections | Duration (steps) | Edges removed |
| :--- | :---: | :---: | :---: |
| SIR - High infection | 67.67% | 112 | – |
| XAI - Top 65% edge removal | 59.67% | 85 | 1736 |

**Table 5** SIRVD XAI-based interventions in ER network

| Strategy | Peak infected | Total dead | Duration | Interventions |
| :--- | :---: | :---: | :---: | :--- |
| No vaccination | 99.67% | 16.67% | 400 | – |
| Random vaccination | 98.67% | 14.67% | 400 | – |
| Targeted vaccination | 98.33% | 12.33% | 339 | – |
| XAI edge removal (50%) | 98% | 14.00% | 238 | 3404 edges removed |
| XAI vaccination (50%) | 96.00% | 11.67% | 400 | 150 vaccinated nodes |

---

## 5 Real case studies

To further assess the robustness and practical applicability of the proposed methodology, simulations were performed on a real contact network as a case study for each epidemiological model (SIS, SIR, SIRVD). Unlike synthetic scenarios, the simulations spanned approximately 15 weeks (103 days), with each step corresponding to one day, thereby capturing realistic temporal dynamics of an epidemic. Two phases of the Covid-19 pandemic were considered: the early stage, characterised by uncontrolled spread, and the late stage, in which the epidemic was partially controlled due to lockdown measures. The corresponding epidemiological parameters were estimated as reported in (Calafiore et al. 2020).

For each model (SIS, SIR, SIRVD), the spreading dynamics were simulated on the real contact network for both phases, after which the proposed XAI-guided interventions were applied. Table 6 summarizes the characteristics of the real network, which represents contact and friendship relations among students at a high school in Marseille, France, in December 2013 (Mastrandrea et al. 2015). This network served as the substrate for simulating the early and late stages of Covid-19 spreading and for evaluating the impact of the XAI-guided interventions.

In these real-world case studies, the framework operates in discrete time, considering the time steps as unit time, as in the synthetic case studies. However, in this real application, each step corresponds to one day of epidemic spreading. Although formally discrete, this setup can be regarded as pseudo-continuous, since the temporal resolution is aligned with the natural reporting interval of epidemiological data. This perspective is consistent with prior studies that highlight the importance of continuous-time formulations for accurately capturing spreading dynamics on networks (Gleeson 2011; Ran et al. 2020; Gleeson 2013).

**Table 6** Real contact network details

| Network model | Nodes | Edges | Clustering Coefficient | Shortest Path Length | Parameters |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Real network⁽¹⁾ | 134 | 406 | 0.5383 | –⁽²⁾ | –⁽³⁾ |

*(1) Friendship contact network (Mastrandrea et al. 2015); (2) Graph not connected - cannot compute average shortest path length; (3) No parameters to set*

### 5.1 SIRVD model
As in synthetic case studies, using the same mechanism, super-spreader pathways were identified and disrupted to reduce infection. Moreover, the effectiveness of targeted vaccination strategies informed by model explainability was evaluated. This second scenario implements an XAI-driven vaccination protocol by determining node-level influence (aggregating edge importance scores as previously described). However, in these real-world applications, nodes are vaccinated with the same probability as in other strategies to demonstrate the robustness of the proposed solution in identifying edges of fundamental importance for the spread of the epidemic. Additionally, to compare more than two vaccination strategies with the real experiments, the XAI-guided interventions were compared with the initial baseline strategies, incorporating an additional vaccination strategy, the *degree-based vaccination* method. This method involves vaccinating nodes with a higher degree, using the same probability as in the betweennesses-guided vaccination case, but with a different approach to identifying important nodes to vaccinate.

#### 5.1.1 Early stage
Simulating the first phase (*early stage*) of Covid-19 spread, the application of the proposed methodology is illustrated starting from the node-embedding representation (Fig. 17). Integrated Gradients was employed as the XAI method to estimate edge importance (Fig. 18). Figure 19a shows that removing 60% of the most important edges identified by XAI (243 edges removed) reduces the infection peak to 25.22% (see Table 7), which is lower than the best result obtained with the baseline. Additionally, Fig. 19b highlights the significant improvement achieved by vaccinating 20% of the most important nodes selected through the GNN-based XAI method (26 vaccinated nodes): as reported in Table 7, the infection peak decreases to 5.67%, and the epidemic concludes in 92 days instead of 103.

![Fig. 17 Node Embedding Early SIRVD](https://placeholder.link/fig17)  
**Fig. 17 Node embedding for a real contact network in SIRVD model setting with early stage Covid-19 parameters:** (a) No vaccination, (b) Betweennesses-based vaccination

![Fig. 18 Integrated Gradients Early SIRVD](https://placeholder.link/fig18)  
**Fig. 18 Integrated gradient applied to a real contact network in SIRVD model setting with early stage Covid-19 parameters:** (a) No vaccination, (b) Betweennesses-based vaccination

![Fig. 19 SIRVD Interventions Early](https://placeholder.link/fig19)  
**Fig. 19 SIRVD simulations under two XAI-guided intervention scenarios on a real contact network with early stage Covid-19 parameters:** (a) XAI-guided edge removal, (b) XAI-guided vaccination

**Table 7** SIRVD XAI-based interventions in the real contact network with early stage Covid-19 parameters

| Strategy | Peak infected | Total dead | Duration (days) |
| :--- | :---: | :---: | :---: |
| No vaccination | 62.84% | 80.60% | 103 |
| Random vaccination | 43.58% | 76.12% | 103 |
| Targeted vaccination | 29.40% | 72.84% | 103 |
| Degree vaccination | 30.75% | 76.42% | 103 |
| XAI edge removal (60%) | 25.22% | 73.28% | 103 |
| XAI targeted vaccination (20%) | 5.67% | 66.87% | 92 |

#### 5.1.2 Late stage
Similarly to the previous case, the second phase (*late stage*) of Covid-19 spread illustrates the application of the proposed methodology, starting from the node-embedding representation (Fig. 20). Integrated Gradients was employed as the XAI method to estimate edge importance (Fig. 21). Figure 22a shows that removing only 35% of the most important edges identified by XAI (142 edges removed) reduces the infection peak to 9.7% (see Table 8), which is slightly lower than the best result obtained with the baseline. Conversely, Fig. 22b highlights the significant improvement achieved by vaccinating 10% of the most important nodes selected through the GNN-based XAI method (13 vaccinated nodes): as reported in Table 8, the infection peak decreases to 0.90%, and the epidemic concludes in only 18 days instead of 103.

![Fig. 20 Node Embedding Late SIRVD](https://placeholder.link/fig20)  
**Fig. 20 Node embedding for a real contact network in SIRVD model setting with late stage Covid-19 parameters:** (a) No vaccination, (b) Degree-based vaccination

![Fig. 21 Integrated Gradients Late SIRVD](https://placeholder.link/fig21)  
**Fig. 21 Integrated gradient applied to a real contact network in SIRVD model setting with late stage Covid-19 parameters:** (a) No vaccination, (b) Degree-based vaccination

![Fig. 22 SIRVD Interventions Late](https://placeholder.link/fig22)  
**Fig. 22 SIRVD simulations under two XAI-guided intervention scenarios on a real contact network with late stage Covid-19 parameters:** (a) XAI-guided edge removal, (b) XAI-guided vaccination

**Table 8** SIRVD XAI-based interventions in the real contact network with late stage Covid-19 parameters

| Strategy | Peak infected | Total dead | Duration (days) |
| :--- | :---: | :---: | :---: |
| No vaccination | 11.19% | 71.04% | 103 |
| Random vaccination | 10.45% | 66.27% | 103 |
| Targeted vaccination | 10.15% | 70.90% | 103 |
| Degree vaccination | 10.00% | 63.58% | 88 |
| XAI edge removal (35%) | 9.70% | 67.76% | 87 |
| XAI targeted vaccination (10%) | 0.90% | 67.91% | 18 |

### 5.2 SIS model
In the SIS and SIR simulation settings, as in the synthetic case studies, XAI-guided techniques were employed to identify and disrupt the superspreader connections that critically influence contagion dynamics. Edges are ranked according to their influence scores, and the top-ranked connections are removed from the network, then to perform a new simulation under the same initial conditions and parameter settings (Table 9).

#### 5.2.1 Early stage
As illustrated in Fig. 23, removing 70% of the most important edges identified by the Integrated Gradient method (284 edges removed) has nearly halved the infection peak (see Table 9).

![Fig. 23 Real Contact SIS Early](https://placeholder.link/fig23)  
**Fig. 23 Node embedding, Integrated gradient and XAI-guided intervention for a real contact network in SIS model setting with early stage Covid-19 parameters:** (a) Node embedding, (b) Integrated Gradient, (c) XAI-guided intervention

**Table 9** SIS XAI-based edge removal (70%) in the real contact network with early stage Covid-19 parameters

| Strategy | Peak of infections | Duration (days) |
| :--- | :---: | :---: |
| SIS | 92.69% | 103 |
| XAI edge removal (70%) | 55.97% | 103 |

#### 5.2.2 Late stage
Using late stage parameter setting showed the complete end of the spreading (in 4 days), as illustrated in Fig. 24c. In fact, removing 45% of the most important edges identified by the Integrated Gradient method (182 edges removed) has reduced the infection peak to 0.75% (see Table 10).

![Fig. 24 Real Contact SIS Late](https://placeholder.link/fig24)  
**Fig. 24 Node embedding, Integrated gradient and XAI-guided intervention for a real contact network in SIS model setting with late stage Covid-19 parameters:** (a) Node embedding, (b) Integrated Gradient, (c) XAI-guided intervention

**Table 10** SIS XAI-based edge removal (45%) in the real contact network with late stage Covid-19 parameters

| Strategy | Peak of infections | Duration (days) |
| :--- | :---: | :---: |
| SIS | 7.46% | 103 |
| XAI edge removal (45%) | 0.75% | 4 |

### 5.3 SIR model
#### 5.3.1 Early stage
Figure 25c illustrates how the removal of 40% of the most important edges identified by the Integrated Gradient method (162 edges removed) has reduced the infection peak to 2.24% (see Table 11), already in the early stage of simulating the SIR model (Fig. 25).

![Fig. 25 Real Contact SIR Early](https://placeholder.link/fig25)  
**Fig. 25 Node embedding, Integrated gradient and XAI-guided intervention for a real contact network in SIR model setting with early stage Covid-19 parameters:** (a) Node embedding, (b) Integrated Gradient, (c) XAI-guided intervention

**Table 11** SIR XAI-based edge removal (40%) in the real contact network with early stage Covid-19 parameters

| Strategy | Peak of Infections | Duration (days) |
| :--- | :---: | :---: |
| SIR | 41.04% | 103 |
| XAI edge removal (40%) | 2.24% | 103 |

#### 5.3.2 Late stage
In the late-stage parameter setting, the SIR simulation demonstrated the complete end of the spread (in 8 days), as illustrated in Fig. 26c. In fact, removing 20% of the most important edges identified by the Integrated Gradient method (81 edges removed) reduced the infection peak to 0.75%, even though the peak was already very low (see Table 12).

![Fig. 26 Real Contact SIR Late](https://placeholder.link/fig26)  
**Fig. 26 Node embedding, Integrated gradient and XAI-guided intervention for a real contact network in SIR model setting with late stage Covid-19 parameters:** (a) Node embedding, (b) Integrated Gradient, (c) XAI-guided intervention

**Table 12** SIR XAI-based edge removal (20%) in the real contact network with late stage Covid-19 parameters

| Strategy | Peak of infections | Duration (days) |
| :--- | :---: | :---: |
| SIR | 3.73% | 103 |
| XAI edge removal (20%) | 0.75% | 8 |

---

## 6 Discussion

This study investigates the potential of explainability to guide epidemic control interventions. The efficacy of an XAI-driven approach is first validated in the SIS and SIR models before being applied to evaluate intervention strategies within the more comprehensive SIRVD model. The central hypothesis suggests that XAI can identify key elements of a network, allowing more effective interventions than those based on topology or untargeted approaches. The first strategy simulates a structural network intervention aimed at disrupting contagion by identifying and removing "super-spreader" connections. An edge importance mask was computed using either Saliency or Integrated Gradients to score each connection’s role in propagating the infection (’Ih’ class). A predefined percentage of the highest-scoring edges was then removed from the graph. The epidemiological impact of this structural modification was assessed by running a new simulation on the altered graph using the same initial conditions and simulation parameters to compare the evolution of the infected (’Ih’) in SIS and SIR models and both infected (’Ih’) and deceased (’Dh’) individuals in SIRVD model. In the SIRVD scenario, the outcomes of three immunisation strategies (no vaccination, random vaccination, and targeted vaccination) are compared with XAI-based edge removal applied to the targeted vaccination case. In contrast, in the SIS and SIR scenarios, the outcome of the high infection case is compared with the XAI-based edge removal applied to it. The second strategy, applied only in SIRVD scenario, implements an XAI-driver vaccination protocol by determining node-level influence. Instead of removing network components, this approach focus on calculating a composite score for each node by aggregating edge importance scores of all its connected edges. The top K% of nodes, ranked by this score, are preemptively vaccinated at the start of the simulation. A new run is conducted under identical conditions, comparing the results to three alternatives: no vaccination, random vaccination, and targeted vaccination based on betweenness centrality (Table 12).

To demonstrate the efficacy and real-world applicability of the proposed framework, parallel experiments were conducted on a contact network representing real interactions between people. As shown in synthetic scenarios, the XAI-guided interventions are highly effective in containing such spread, similar to the early and late phases of Covid-19 simulated in these experiments.

Despite the strengths demonstrated by ExDiff, two key limitations should be acknowledged:

* The random choice of the initial infected node injects run-to-run variability into both the simulated epidemic curves and the learnt GNN parameters.
* The interpretability and predictive performance of the GNN depend on the particular time step used for training. Selecting an optimal step remains somewhat heuristic and can bias the identified structural drivers of contagion.

These limitations underscore the need for cautious interpretation and robust experimental design when applying ExDiff to complex diffusion phenomena.

---

## 7 Conclusion

In conclusion, this work presents *ExDiff*, a Python-based simulation framework that integrates graph-theoretic modelling with explainability tools. ExDiff enables accessible, reproducible experimentation with potential applications in public health, social networks, and computational science. By combining classical compartmental models with deep learning and explainable AI techniques, the framework captures both structural and temporal aspects of diffusion in complex networks. The framework incorporates dedicated modules for network generation, neural modelling, simulation, and interpretability, all accessible through an intuitive Google Colab interface designed to support interactive analysis and practical implementation. Through extensive experimentation with SIS, SIR and SIRVD models, ExDiff demonstrates its capacity to simulate epidemic spread, assess intervention strategies, predict node-level infection states, and uncover the latent structural drivers of diffusion using saliency-based or integrated-gradient-based XAI methods. Importantly, the incorporation of XAI-guided interventions, such as targeted edge removal and vaccination strategies, highlights the framework’s potential to inform decision-making with interpretable insights in real contexts, as demonstrated by Covid-19 case studies. In summary, ExDiff provides a versatile and extensible platform that empowers researchers to explore, simulate, and explain complex contagion dynamics with potential real-world applications in networked systems.

---

**Acknowledgements** We acknowledge the support of the PNRR project FAIR - Future AI Research (PE00000013), Spoke 9 - Green-aware AI, under the NRRP MUR program funded by the NextGenerationEU.

**Author contributions** UL, BP, AD and PHG conceived main ideas of this paper, wrote and reviewed the manuscript. UL, BP and AD implemented the software modules and performed the experiments. PHG and PV contributed to the discussion of the results and to the revision of the first draft. All authors approved the manuscript.

**Funding** Open access funding provided by Università degli studi "Magna Graecia" di Catanzaro within the CRUI-CARE Agreement. U. Lomoio and B. Puccio PhD fellows are partially funded by Relatech S.p.a.

**Data availability** The ExDiff framework, including source code and simulation modules, is freely available at [https://github.com/hguzzi/ExDiff.git](https://github.com/hguzzi/ExDiff.git). All data used in this study were synthetically generated using standard network models (e.g., Erdos-Rényi, Barabàsi-Albert, Watts-Strogatz), and can be reproduced using the generation scripts included in the repository. No real-world or human subject data were used.

### Declarations

**Conflict of interest** No Conflict of interest is declared.

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

---

## References

* Adadi A, Berrada M (2018) Peeking inside the black-box: a survey on explainable artificial intelligence (XAI). IEEE Access 6:52138–52160
* Ahrenberg L, Kok S, Vasarhelyi K, et al (2016) Nepidemix. Technical report
* Ajelli M, Gonçalves B, Balcan D et al (2010) Comparing large-scale computational approaches to epidemic modeling: agent-based versus structured metapopulation models. BMC Infect Dis 10(1):1–13
* Alguliyev R, Aliguliyev R, Yusifov F (2021) Graph modelling for tracking the COVID-19 pandemic spread. Infect Dis Model 6:112–122
* Bisong E (2019) Google colaboratory. Building machine learning and deep learning models on google cloud platform: a comprehensive guide for beginners. Springer, pp 59–64
* Broeck WV, Gioannini C, Gonçalves B et al (2011) The gleamviz computational tool, a publicly available software to explore realistic epidemic spreading scenarios at the global scale. BMC Infect Dis 11(1):37
* Bryant P, Elofsson A (2020) Modelling the dispersion of sars-cov-2 on a dynamic network graph. medRxiv
* Calafiore GC, Novara C, Possieri C (2020) A time-varying SIRD model for the COVID-19 contagion in Italy. Annu Rev Control 50:361–372
* Cho G, Park JR, Choi Y et al (2023) Detection of COVID-19 epidemic outbreak using machine learning. Front Public Health 11:1252357
* Cho YR, Mina M, Lu Y et al (2013) M-finder: Uncovering functionally associated proteins from interactome data integrated with go annotations. Proteome science 11:1–12
* Chow K, Sarkar A, Elhesha R et al (2021) ANCA: Alignment-Based Network Construction Algorithm. IEEE ACM Trans Comput Biol Bioinform 18(2):512–524
* Coelho FC, Cruz OG, Codeço CT (2008) Epigrass: a tool to study disease spread in complex networks. Source Code Biol Med 3(1):3
* Cure S, Pflug FG, Pigolotti S (2024) Fast and exact simulations of stochastic epidemics on static and temporal networks. arXiv preprint [arXiv:2412.07095](https://arxiv.org/abs/2412.07095)
* De Domenico M, Granell C, Porter MA et al (2016) The physics of spreading processes in multilayer networks. Nat Phys 12(10):901–906
* Defilippo A, Giorgi FM, Veltri P et al (2024) Understanding complex systems through differential causal networks. Sci Rep 14(1):27431
* Defilippo A, Veltri P, Lió P et al (2024) Leveraging graph neural networks for supporting automatic triage of patients. Sci Rep 14(1):12548
* Fortunato S, Castellano C (2012) Community structure in graphs. Computational complexity. Springer, pp 490–512
* Gleeson JP (2011) High-accuracy approximation of binary-state dynamics on networks. Phys Rev Lett 107(6):068701
* Gleeson JP (2013) Binary-state dynamics on complex networks: pair approximation and beyond. Phys Rev X 3(2):021004
* Guzzi PH, Milenković T (2018) Survey of local and global biological network alignment: the need to reconcile the two sides of the same coin. Brief Bioinform 19(3):472–481
* Guzzi PH, Zitnik M (2022) Editorial deep learning and graph embeddings for network biology. IEEE ACM Trans Comput Biol Bioinform 19(2):653–654
* Guzzi PH, Di Paola L, Giuliani A et al (2022) Pcn-miner: an open-source extensible tool for the analysis of protein contact networks. Bioinformatics 38(17):4235–4237
* Guzzi PH, Petrizzelli F, Mazza T (2022b) Disease spreading modeling and analysis: a survey. Briefings Bioinform 23(4):bbac230
* Guzzi PH, Petrizzelli F, Mazza T (2022) Disease spreading modeling and analysis: a survey. Brief Bioinform. https://doi.org/10.1093/bib/bbac230
* Humphreys P (2002) Computational models. Philos Sci 69(S3):S1–S11
* Jenness SM, Goodreau SM, Morris M (2018) Epimodel: an R package for mathematical modeling of infectious disease over networks. J Stat Softw 84:1–47
* Karaivanov A (2020) A social network model of COVID-19. PLoS One 15(10):e0240878
* Kermack WO, McKendrick AG (1927) A contribution to the mathematical theory of epidemics. Proc R Soc London Ser Contain Pap Math Phys Charact 115(772):700–721
* Kipf TN, Welling M (2017) Semi-supervised classification with graph convolutional networks. In: International conference on learning representations, [https://openreview.net/forum?id=SJU4ayYgl](https://openreview.net/forum?id=SJU4ayYgl)
* Kokhlikyan N, Miglani V, Martin M, et al (2020) Captum: a unified and generic model interpretability library for pytorch. [arXiv:2009.07896](https://arxiv.org/abs/2009.07896)
* Leskovec J, Lang KJ, Mahoney M (2010) Empirical comparison of algorithms for network community detection. In: Proceedings of the 19th international conference on World wide web, ACM, pp 631–640
* Liu D, Ding W, Dong ZS et al (2022) Optimizing deep neural networks to predict the effect of social distancing on COVID-19 spread. Comput Ind Eng 166:107970
* Liu QH, Ajelli M, Aleta A et al (2018) Measurability of the epidemic reproduction number in data-driven contact networks. Proc Natl Acad Sci USA 115(50):12680–12685
* Lu X, Feng J, Lai S, et al (2025a) Human mobility in epidemic modeling. arXiv preprint [arXiv:2507.22799](https://arxiv.org/abs/2507.22799)
* Lu X, Feng J, Tan S (2025) Perspectives on modelling epidemics with human mobility. Europhys Lett 149(4):41002
* Mastrandrea R, Fournet J, Barrat A (2015) Contact patterns in a high school: a comparison between data collected using wearable sensors, contact diaries and friendship surveys. PLoS One 10(9):e0136497
* Miller JC, Ting T (2020) Eon (epidemics on networks): a fast, flexible python package for simulation, analytic approximation, and analysis of epidemics on networks. arXiv preprint [arXiv:2001.02436](https://arxiv.org/abs/2001.02436)
* Pastor-Satorras R, Vespignani A (2001) Epidemic spreading in scale-free networks. Phys Rev Lett 86(14):3200
* Patil R, Dave R, Patel H et al (2021) Assessing the interplay between travel patterns and SARS-CoV-2 outbreak in realistic urban setting. Appl Netw Sci 6(1):1–19
* Petrizzelli F, Guzzi PH, Mazza T (2022) Beyond covid-19 pandemic: topology-aware optimization of vaccination strategy for minimizing virus spreading. Comput Struct Biotechnol J. https://doi.org/10.1016/j.csbj.2022.05.040
* Ran Y, Deng X, Wang X et al (2020) A generalized linear threshold model for an improved description of the spreading dynamics. Chaos. https://doi.org/10.1063/5.0011658
* Robson EW, Reddy D, Umrawal AK (2024) Cynetdiff: a python library for accelerated implementation of network diffusion models. Proc VLDB Endow 17(12):4409–4412. https://doi.org/10.14778/3685800.3685887
* Rodriguez A, Kamarthi H, Agarwal P et al (2024) Machine learning for data-centric epidemic forecasting. Nat Mach Intell 6(10):1122–1131
* Rossetti G, Milli L, Rinzivillo S (2018) Ndlib: a python library to model and analyze diffusion processes over complex networks. Companion Proc The Web Conf 2018:183–186
* Sahneh FD, Vajdi A, Shakeri H et al (2017) Gemfsim: a stochastic simulator for the generalized epidemic modeling framework. J Comput Sci 22:36–44
* Scarselli F, Gori M, Tsoi AC et al (2008) The graph neural network model. IEEE Trans Neural Networks 20(1):61–80
* Scarselli F, Gori M, Tsoi AC et al (2009) The graph neural network model. IEEE Trans Neural Networks 20(1):61–80. https://doi.org/10.1109/TNN.2008.2005605
* Shahrabi A, Nikpanjeh F, Hamounian A et al (2025) Data-driven stability analysis of complex systems with higher-order interactions. Commun Phys 8(1):239
* Suer J, Ponge J, Hellingrath B (2024) Epipredict: agent-based modeling of infectious diseases. KI-Künstliche Intelligenz 38(3):177–181
* Sundararajan M, Taly A, Yan Q (2017) Axiomatic attribution for deep networks. In: International conference on machine learning, PMLR, pp 3319–3328
* Vespignani A (2012) Modelling dynamical processes in complex socio-technical systems. Nat Phys 8(1):32–39
* Zaplotnik Ž, Gavrić A, Medic L (2020) Simulation of the covid-19 epidemic on the social network of Slovenia: estimating the intrinsic forecast uncertainty. PLoS One 15(8):e0238090
* Zitnik M, Li MM, Wells A et al (2024) Current and future directions in network biology. Bioinformatics Adv 4(1):vbae099

---

### Authors and Affiliations

**Annamaria Defilippo¹ · Ugo Lomoio¹ · Barbara Puccio¹ · Pierangelo Veltri² · Pietro Hiram Guzzi¹**

✉ **Annamaria Defilippo**  
[annamaria.defilippo@unicz.it](mailto:annamaria.defilippo@unicz.it)

**Ugo Lomoio**  
[ugo.lomoio@unicz.it](mailto:ugo.lomoio@unicz.it)

**Barbara Puccio**  
[barbara.puccio@unicz.it](mailto:barbara.puccio@unicz.it)

**Pierangelo Veltri**  
[pierangelo.veltri@dimes.unical.it](mailto:pierangelo.veltri@dimes.unical.it)

**Pietro Hiram Guzzi**  
[hguzzi@unicz.it](mailto:hguzzi@unicz.it)

¹ Department of Surgical and Medical Sciences, Magna Graecia University of Catanzaro, 88100 Catanzaro, CZ, Italy  
² Department of Computer Engineering, Modelling, Electronics and Systems (DIMES), University of Calabria, 87036 Arcavacata, CS, Italy

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.