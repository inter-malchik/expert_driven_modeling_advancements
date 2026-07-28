**Personal View**  
**eBioMedicine** 2026;126: 106207  
Published Online 12 March 2026  
DOI: https://doi.org/10.1016/j.ebiom.2026.106207  

---

# Integrating explainable AI and One Health: a new frontier in combating infectious diseases

**Yanni Cao<sup>a</sup>, Emma Lancaster<sup>a</sup>, Jiyoung Lee<sup>a,b,c</sup>, and Jianyong Wu<sup>a,*</sup>**

<sup>a</sup> Division of Environmental Health Sciences, College of Public Health, The Ohio State University, Columbus, OH, 43210, USA  
<sup>b</sup> Infectious Diseases Institute, The Ohio State University, Columbus, OH, 43210, USA  
<sup>c</sup> Department of Food Science & Technology, The Ohio State University, Columbus, OH, 43210, USA  

*\*Corresponding author.*  
*E-mail address:* wu.6255@osu.edu (J. Wu).

---

> ### Summary
> Infectious diseases (IDs) remain a major threat to global health and societal stability. Because most emerging IDs in humans are zoonotic in origin and shaped by environmental contexts, effective prevention and control call for a One Health approach. Machine learning is widely used for ID modelling and forecasting but often lacks interpretability to explain predictions or guide public health action. Explainable AI (XAI) makes complex models interpretable, enabling attribution of predictions and identification of key outbreak drivers. In this Personal View, we argue that embedding XAI within a One Health framework offers a new organising principle for ID intelligence. We highlight emerging applications in surveillance and forecasting, zoonotic spillover, antimicrobial resistance monitoring and optimisation of resource allocation. We also outline key challenges, including data harmonisation, governance, privacy protection and equitable distribution of risks and benefits. Advancing XAI-enabled One Health systems will require collaboration across sectors and methodological innovation.
>
> **Copyright © 2026 The Author(s).** Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
>
> **Keywords:** Explainable artificial intelligence (XAI); One Health; Infectious diseases; Predictive modelling

---

## Introduction

Infectious diseases (IDs) remain one of the most pressing threats to global health and societal well-being.<sup>1</sup> The COVID-19 pandemic alone had caused more than 7.1 million reported deaths worldwide as of November 9, 2025.<sup>2</sup> It also led to the largest global economic contraction since World War II.<sup>3</sup> These outcomes have highlighted the importance of ID prediction, prevention and more proactive preparedness. Research indicates that over 60% of human IDs are zoonotic, stemming from pathogens transmitted between humans and wild or domestic animals,<sup>4,5</sup> while the risk of zoonotic spillover is closely linked to human activities, including habitat destruction.<sup>6</sup> This underscores the importance of systematically integrating humans, animals, and the environment in ID prevention. In response, the One Health framework has been proposed. The World Health Organization (WHO) defines One Health as ‘an integrated, unifying approach to balance and optimise the health of people, animals, and the environment’.<sup>7</sup> Essentially, the central concept is that all these three domains are inherently interconnected, with each domain directly or indirectly influencing the others.<sup>8</sup> In recent years, there has been a growing consensus around the One Health framework for global health and sustainable development.<sup>9,10</sup> In the context of IDs, more studies advocate the One Health framework for prevention and control,<sup>11–13</sup> including COVID-19<sup>14</sup> and bartonellosis.<sup>15</sup> The value of One Health for the prevention and early detection of disease threats had been recognised globally, leading to its inclusion as an important component of the Global Health Security Agenda.<sup>16</sup>

Against this backdrop, practice-oriented efforts to operationalise One Health for ID surveillance, forecasting, and prevention are accelerating, spanning integrated surveillance platforms that link human, animal, and environmental data streams (e.g., USAID’s PREDICT program<sup>17</sup>); systems-thinking frameworks and interdisciplinary systems perspectives;<sup>18</sup> and big data and AI technologies for multisource data fusion and situational awareness.<sup>19,20</sup> In parallel, cross-sector data are expanding in volume, velocity, and variety, with new modalities (e.g., audio and video, mobile app and sensor data) and faster refresh cycles, creating an urgent need for near-real-time data integration and processing. Conventional statistical approaches and black-box machine learning models often fail to provide transparent, decision-oriented rationales. This gap motivates methods that combine performance with interpretability. In this context, explainable artificial intelligence (XAI) offers a powerful tool to enhance understanding, transparency, and trust in complex modelling processes. XAI comprises a growing set of tools that help make machine learning models transparent and interpretable to human users.<sup>21</sup> Unlike traditional black-box algorithms, XAI methods clarify which factors drive outcomes and why.<sup>22</sup> Far beyond a technical enhancement, XAI represents a strategic frontier for operationalising One Health in ID contexts, as it makes predictions and responses more interpretable, coordinated, and responsive to real-world complexity.

Recent reviews highlight AI’s promise for ID modelling from disease surveillance to epidemic forecasting and spillover prediction, but they largely emphasise accuracy and data integration rather than how model outputs can be made interpretable and actionable for decision-makers across One Health.<sup>23,24</sup> We argue that XAI fills this operational gap by translating complex predictions into transparent rationales, enabling shared interpretation, accountability, and coordinated action across sectors. Embedding XAI in One Health goes beyond data integration by enabling mechanism-informed action, shared cross-disciplinary interpretation, and transparent, accountable decision-making.<sup>25–27</sup> In this sense, XAI functions as an implementation layer that operationalizes One Health rather than a technical add-on. In this article, we (i) address that integrating XAI with One Health is essential for combating IDs; then (ii) summarise current applications and illustrative cases of XAI in One Health; thereafter (iii) discuss current challenges and practical considerations; and finally (iv) propose future directions.

---

## The need for integration

### Complexity of infectious diseases
Despite decades of progress in ID control, a persistent burden of long-standing, emerging, and re-emerging infections remains. For example, tuberculosis continues to pose a major global health threat,<sup>28</sup> while cholera,<sup>29</sup> Mpox,<sup>30</sup> and measles<sup>31</sup> have re-emerged in multiple regions. Additionally, new human infections of highly pathogenic avian influenza (HPAI)<sup>32</sup> and dengue virus<sup>33</sup> are increasingly reported. These recurring crises highlight that IDs are not merely clinical concerns but are deeply intertwined with the stability, resilience, and welfare of societies.<sup>34,35</sup> In an era shaped by accelerating globalisation, climate instability, ecological disruption, and social inequity, the landscape of ID threats is becoming increasingly dynamic and difficult to manage.<sup>36</sup> This underscores the importance of addressing the broader systemic forces that drive disease vulnerability. Rather than stemming from a single cause, IDs arise from a complex web of interacting drivers. These include land-use change, intensified livestock production, global travel and trade, urban crowding, climate variability and vulnerability, inadequate sanitation, antimicrobial resistance (AMR), vector-borne transmission, and zoonotic spillover.<sup>1,37,38</sup> These drivers do not operate in isolation; instead, they intersect and can amplify one another across human, animal, and environmental systems.

### One Health as a foundational framework for infectious disease prediction
Originating in the early 2000s in response to growing concern over pandemic-prone IDs, One Health has since evolved into a coherent conceptual framework for cross-sectoral action.<sup>39</sup> This framework encourages a collaborative, transdisciplinary strategy that integrates local, national, and global efforts to achieve optimal health for humans, animals, and the environment,<sup>40</sup> which is critical for preventing, anticipating, and responding to global health threats, as it fosters innovative solutions that address root causes within and across domains.<sup>41</sup> Using dengue forecasting as an example, one study argues for assessing dengue risk more comprehensively from a One Health perspective.<sup>42</sup> Here, the animal pillar encompasses vector ecology, the human pillar covers individual and social factors, (e.g., health, socioeconomic status, education, behaviour and demographics), and the environmental pillar includes climatic and geographical factors. This supports cross-sectoral strategies to anticipate, prevent and manage threats across disciplinary and borders. Ultimately, One Health provides a proactive, ecosystem-based approach to interconnected ID risks and long-term health.

### Limitations of existing ID forecasting models
Drawing on prior studies, ID forecasting approaches are commonly grouped into traditional compartmental, statistical, and machine learning models. Traditional compartmental models, such as Susceptible–Infectious–Recovered (SIR) models, have long provided the foundation for ID modelling and remain essential for understanding transmission dynamics because of their transparency and mechanistic clarity.<sup>43</sup> However, these models often struggle to accommodate the high-dimensional, real-time, and unstructured data sources, and are typically inflexible when additional compartments or pathways are needed.<sup>44</sup> Besides, the increasing complexity of disease drivers, including climate variables, human mobility, land use, and socio-economic indicators, challenges traditional frameworks that rely on predefined compartments and assumptions. As a result, conventional models may fall short in detecting subtle patterns, adapting to rapidly changing conditions, or capturing cross–sectoral interactions.<sup>45</sup> Statistical models, such as time-series approaches and regression models, also have limitations, including weak out-of-sample generalisability and poor suitability for multimodal data such as video, mobility, and remote-sensing data.<sup>24,46,47</sup> Generalisability limitations also apply to complex AI models, which may capture highly local associations that do not readily transfer across different One Health settings. Explainability can help identify such context dependence by revealing reliance on local drivers, supporting responsible model adaptation rather than uncritical generalisation.

In response to the growing volume, dimensionality, and heterogeneity of data on ID drivers, alongside stringent timeliness requirements, machine learning methods are increasingly being employed,<sup>46</sup> and have been widely used to forecast ID outbreaks<sup>45,48</sup> as well as anticipate zoonotic spillover events.<sup>49,50</sup> Common approaches include supervised learning (e.g., random forests, deep neural networks), semi-supervised learning, unsupervised learning (e.g., clustering and association rule mining), and reinforcement learning.<sup>45,48–51</sup> Despite advances in modelling heterogeneous data, black-box machine learning systems often fail to provide decision-relevant explanations that link diverse predictors to outcomes, limiting scientific understanding and their operational values.

### Importance of XAI
This lack of interpretability in AI models poses serious challenges in One Health, where public health professionals, veterinarians, ecologists, and policymakers must collaboratively respond to emerging threats. In such interdisciplinary contexts, the rationale behind predictions must be clear, accountable, and actionable in the sense that model outputs can be traced and justified in real-world decision making, not just accurate. Evidence from health and public-sector decision-support settings indicates that transparent and explainable models are more likely to foster stakeholder trust, facilitate cross-sector coordination, and support timely and targeted responses.<sup>22,26,52,53</sup>

XAI makes complex models more transparent by identifying key drivers of predictions and how their influence varies across contexts, bridging the gap between predictive performance and operational use. Techniques such as SHapley Additive exPlanations (SHAP) and Local Interpretable Model-Agnostic Explanations (LIME) exemplify how model outputs can be broken down into human-understandable components.<sup>54</sup> SHAP identifies the most influential contributors to a model’s prediction,<sup>25</sup> while LIME explains the drivers behind individual predictions in specific contexts.<sup>26</sup> Together, these tools turn opaque algorithms into transparent decision-support systems aligned with the goals of One Health. To illustrate these advantages, we present several use cases of XAI-integrated models and highlight their advantages over conventional statistical models (**Table 1**).

---

### Table 1: Comparative advantages of XAI-integrated models over conventional statistical approaches in recent infectious disease studies.

| Disease and research area | Data in One Health framework | Conventional statistical model (Reference) | Optimal machine learning model | XAI approach | Gain from XAI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dengue, Bangladesh**<sup>55</sup> | **Human:** Poverty. Population density, GDP.<br>**Environment:** temperature, humidity, rain, wind, vector habitat. | Generalised linear model with the AUC of 0.84 | XGBoost with the AUC of 0.89. | Global driver identification with SHAP;<br>Local prediction explanations with LIME. | LIME revealed complex, non-linear thresholds, providing actionable targets that linear coefficients miss. |
| **West Nile Virus, Europe**<sup>56</sup> | **Animal:** *Passeriformes* birds.<br>**Vector:** *Culex* spp. Abundance.<br>**Environment:** bioclimatic, Water, etc. | Time-Series/Regression | XGBoost with the AUC ranging from 0.93 to 0.97. | SHAP for Ranking biotic/abiotic drivers and visualising contributions. | SHAP disentangled complex lagged effects. |
| **Malaria, Kenya**<sup>57</sup> | **Human:** Symptoms (Nausea, Fever).<br>**Parasite:** *Plasmodium* spp.<br>**Environment:** Rain, temperature. | Linear clinical methods | Random Forest with the accuracy of 98%. | SHAP & DALEX for visualising decision paths for individual patients. | DALEX/SHAP provided instance-level explanations, which mimics clinical reasoning, fostering trust that black box models lack. |

**GDP:** Gross Domestic Product, **AUC:** Area under the receiver operating characteristic curve.

---

## Applications of XAI in One Health

### Disease surveillance and prediction
Interconnected human, animal, and environmental systems drives ID emergence and spread through complex interactions, such as wildlife movements and human activities.<sup>27</sup> Growing recognition of these links has underscored the importance of effective cross-sector disease surveillance within One Health frameworks.<sup>17,58</sup> In this context, XAI provides a promising approach to addressing the complexity and opacity of disease risk prediction.<sup>47</sup> By integrating diverse input data, such as health records, wildlife monitoring, and environmental observations, XAI-based models can detect subtle, non-linear ecological precursors, such as specific climatic thresholds or complex vector–habitat interactions, and generate clear, interpretable forecasts.<sup>47,59</sup> Incorporating animal health indicators, such as wildlife density or livestock infection rates, further enhances these models’ ability to capture cross-species transmission dynamics central to the One Health framework. **Fig. 1** summarises the end-to-end XAI workflow designed for disease surveillance, from integrating multi-source data to producing localised interpretations.

```
+------------------------------------+       +------------------------------------+
| INPUT DATA                         |       | EXAMPLES                           |
| • Health records                   |       | • Dengue early warning             |
| • Wildlife data                    |       | • West Nile virus prediction       |
| • Environmental data               |       | • Highly pathogenic avian          |
|                                    |       |   influenza (HPAI) outbreak        |
|                                    |       |   prediction [EXAMPLE]             |
+------------------------------------+       +------------------------------------+
                  |                                             ^
                  v                                             |
+------------------------------------+       +------------------------------------+
| XAI MODELING                       | ----> | RISK FORECAST                      |
| • Combine diverse data             |       | • Highlight key drivers            |
| • Find hidden risk signals         |       | • Assign area risk scores          |
| • Produce clear results            |       | • Give scenario insights           |
|                [XAI Modeling]      |       |                [Risk Forecast]     |
+------------------------------------+       +------------------------------------+

                          =================================
                            XAI Analysis & Prediction Flow
                          =================================
```

***Fig. 1:** XAI analysis and prediction workflow for multi-source infectious disease surveillance.*

Recent studies illustrate the practical value of this approach. For example, an XAI-enhanced framework in Bangladesh combined climatic, socio-demographic, and land-use data to predict dengue outbreaks and clarify the main factors driving risk.<sup>55</sup> While this system primarily integrated human and environmental information, SHAP analyses quantified the relative importance of key variables, highlighting the central role of rainfall, population density, and minimum temperature in shaping transmission dynamics. LIME was then used to generate local explanations, showing how these features influenced specific predictions across different regions and time periods. In Europe, a similar XAI approach was applied to West Nile virus prediction.<sup>56</sup> SHAP values were used to rank the predictors contributing most to outbreak forecasts, identifying preceding-year summer temperatures, seasonal spring temperature anomalies, and *Culex* mosquito abundance as the most influential drivers. Importantly, explainability allowed the model to distinguish the broader eco-climatic factors underlying endemic risk from the specific conditions that triggered the extraordinary 2018 outbreak. Moreover, an XGBoost model interpreted with SHAP was developed to predict HPAI outbreaks at the NUTS-3 level.<sup>60</sup> The analysis identified poultry density, climatic conditions and environmental indices, together with wild bird distributions, as the main drivers of outbreak risk. These insights informed sentinel surveillance and early warning systems that explicitly incorporate climate patterns, migratory bird ecology and reinfection dynamics, illustrating how XAI can operationalise One Health principles in routine outbreak prediction. Together, these examples demonstrate that XAI can enhance disease surveillance systems by clarifying predictive mechanisms, strengthening actionable interpretation and enabling more responsive, locally informed public health decisions.

### Zoonotic spillover and vector–host–environment interfaces
Unlike population-level ID surveillance, tracking zoonotic spillover requires attention to ecological interfaces where pathogens move between wildlife, livestock, vectors, and humans.<sup>23</sup> Monitoring these spillover pathways remains a profound challenge because it demands integrating diverse signals from wildlife ecology, livestock management, human behaviours, and environmental change. Subtle shifts, including habitat fragmentation, altered animal movement or microbial contamination of water and soil, often precede zoonotic emergence but frequently go undetected in conventional surveillance systems. In this context, XAI offers a way to transform complex datasets into interpretable risk assessments and actionable insights.

XAI-based models can help detect incipient environmental signals by capturing subtle changes in climate, water quality, soil conditions, wildlife habitats and other environmental factors that precede pathogen spillover. One XAI-based study compared multiple algorithms to predict *Cryptosporidium* and *Giardia* presence in surface water. SHAP showed that low temperatures (<20 °C) and high turbidity drove *Cryptosporidium* contamination, while *Escherichia (E.) coli* counts and turbidity were the main predictors of *Giardia*.<sup>59</sup> Beyond early detection, these models also excel at predicting localised hotspots and revealing fine-scale spatiotemporal risk patterns that often elude conventional surveillance systems. In Malaysia, a deep neural network combined with LIME was applied to forecast leptospirosis outbreaks, identifying weekly hotspots linked to acidic soils and extensive rubber plantations, and enabling targeted interventions in high-risk communities.<sup>61</sup>

At a broader scale, XAI frameworks are well-suited to quantifying the large-scale drivers of zoonotic spillover and supporting high-resolution decision-making. For example, an integrated machine learning approach linked human modification, livestock density, and cropping intensity to higher spillover risk, while SHAP highlighted crop cover and livestock headcounts as mediators.<sup>62</sup> In Peninsular Malaysia, human *Plasmodium knowlesi* risk was modelled using an XGBoost ecological niche model with multiple environmental covariates. The model outperformed alternatives, and SHAP highlighted distance to the coastline, elevation, tree cover, historical precipitation, historical tree loss, and distance to forest as dominant predictors, supporting risk mapping for targeted control.<sup>63</sup> Taken together, these examples illustrate XAI’s transformative potential for zoonotic disease tracking from traditional approaches. As One Health surveillance systems evolve, embedding XAI within predictive frameworks offers a unique opportunity to bridge disciplinary divides, strengthen accountability and deliver more precise interventions.

### Monitoring and predicting antimicrobial resistance
Antimicrobial Resistance (AMR) crisis has been recognised as one of the leading global health threats.<sup>64</sup> While AMR has traditionally been studied in clinical and healthcare settings, increasing research highlights the role of the environment in shaping resistant microbes.<sup>65</sup> Resistant bacteria and antibiotic resistance genes (ARGs) can evolve, spread, and persist across human, animal, and environmental sectors, making AMR a complex One Health issue.<sup>66</sup> Although antibiotic resistance is widely monitored in clinical settings, its functions, transmission risks, and broader ecological impacts remain poorly understood, especially in the environment. To address these challenges, XAI can help integrate diverse One Health data to track and explain AMR trends. By combining clinical, prescribing, livestock, and environmental ARG datasets, XAI clarifies cross–domain interactions, explains resistance patterns, and identifies key sources and pathways. XAI can help characterise key antimicrobial mechanisms, including mode-of-action and gene transfer dynamics that link resistance across species and domains. For example, it has been applied to predict antimicrobial mechanisms-of-action from transcriptome data, providing interpretable insights into the features driving resistance patterns and supporting the discovery of novel antibiotics.<sup>67</sup>

The food supply chain is a critical yet under-recognised pathway for AMR transmission, particularly via contamination and cross–sector interactions.<sup>68</sup> Changes in the supply chain can increase food-safety risks for both humans and animals by increasing exposure to resistant microbes in contaminated food or feed, which may lead to drug-resistant infections. In this context, one study compared SHAP, LIME, and the What-If Tool (WIT) for food fraud and safety evaluation based on speed, explanation scope, and usability.<sup>69</sup> In light of these emerging applications and the persistent knowledge gaps in AMR surveillance, explainable techniques hold great potential for advancing public health strategies. Accordingly, further exploration of XAI techniques in AMR surveillance is encouraged, as such efforts could enhance public health protection, ensure food safety, and promote sustainable agriculture. Such insights can support more proactive global AMR governance, including surveillance prioritisation and risk communication.

### Optimising intervention strategies and resource allocation
Beyond surveillance and predictive modelling, XAI also plays a critical role in designing proactive strategies. By informing how, where, and why interventions are needed, XAI supports the optimisation of One Health responses across domains. Specifically, it enables interpretable disease surveillance by identifying which variables (e.g., land use, vector density, temperature, precipitation) drive outbreaks and how interactions between human and animal health indicators elevate such risk. This transparency enhances early warning systems that stakeholders can trust and act upon with greater confidence. Guiding intervention strategies is often difficult due to limited resources, including vaccination campaigns, vector control, safe water and sanitation, habitat protection, and wildlife monitoring. To overcome these limitations, particularly in resource-constrained settings, explainability is essential. Given the collaborative nature of One Health, XAI can provide transparent rationales to align decision-making across environmental, animal, and human health sectors. Consequently, XAI can provide effective justification of resource distribution by showing why a particular region, species, or population is prioritised over others. For example, when implementing vaccination campaigns, XAI models can identify high-risk populations and explain why particular communities are prioritised, whether they have higher mobility, recent outbreak history, or low immunity. Such transparency facilitates greater community engagement and public acceptance of interventions.

Unsustainable human practices such as deforestation, urbanisation, water overuse, and air pollution disrupt ecosystems, increase human–animal interactions, and elevate the risk of zoonotic disease transmission.<sup>70</sup> XAI can promote effective resource management, which are critical for controlling disease spread, ensuring food and water security, and supporting overall well-being across all domains.<sup>71,72</sup> One recent study applied a XAI-driven method to investigate the connections among eight universal water quality indicators in Indian river bodies, delivering an interpretable tool for estimation and management.<sup>73</sup> Another study applied XAI models to uncover how climate extremes and land cover jointly shape wildfire smoke–related $\text{PM}_{2.5}$, an emerging contaminant of concern for both human and environmental health.<sup>74</sup> XAI also allows decision-makers to understand the key factors that drive both our renewable and non-renewable resources, such as air, water, plants, soil, minerals, and fossil fuels. For example, wildlife fisheries can extract the key water quality parameters that are directly influencing fish health and productivity to plan fishing schedules, optimise locations, and reduce the risks of fish mortality.<sup>73</sup> Additionally, natural ecosystems, such as forests and wetlands, play a crucial role in mitigating climate change, which in turn affects the distribution and severity of many IDs.<sup>72</sup> XAI-based modelling of natural and managed resources can guide their safe use while helping prevent pathogen contamination. Sustainable management of these resources, in turn, strengthens the resilience of health systems and promotes long-term public and environmental health.

### Meeting stakeholders’ needs
Stakeholders across human, animal, and environmental health increasingly view interpretability as essential for deploying AI in practice. In endemic settings, malaria forecasts are of limited value if their rationale is opaque. XAI addresses this by explaining predictions and identifying key risk drivers. For example, an XAI-enhanced malaria model in Kenya used SHAP and descriptive machine learning explanations (DALEX) to pinpoint the factors most strongly influencing malaria risk scores.<sup>57</sup> These included clinical symptoms like fever and muscle aches, parasite species identification, and environmental variables such as rainfall and temperature. By making these contributions transparent, XAI-enabled models allowed public health teams to determine not only where risk was the highest but also *why*, supporting more targeted and accountable interventions. This transparency is not merely a technical benefit. It strengthens confidence in AI tools, improves coordination among sectors, and enables faster, evidence-based responses. Over time, this clarity reinforces trust and supports sustained adoption of predictive systems, creating a continuous cycle in which explainability meets stakeholder needs and drives more effective collaboration, as illustrated in **Fig. 2**.

```
+------------------------------------------+        +------------------------------------------+
| STAKEHOLDER NEEDS                        |        | IMPACT                                   |
| • Sectors need clear, explainable        |        | • Builds trust in AI tools               |
|   predictions                            |        | • Improves coordination across sectors   |
| • Knowing "why" builds trust             |        | • Enables faster action                  |
+------------------------------------------+        +------------------------------------------+
       |                                                         ^
       | Satisfies the need for clarity                          | Enables targeted action
       v                                                         |
+------------------------------------------+        +------------------------------------------+
| XAI INTERPRETABILITY                     |        | ILLUSTRATIVE SCENARIO                    |
| • Shows key drivers of risk              | ---->  | • Malaria warning with XAI               |
| • Explains factors behind predictions    |        |   explanations                           |
+------------------------------------------+        +------------------------------------------+
                                     Demonstrates
                                     application

                    ====================================================
                              XAI-Supported Action Cycle
                    ====================================================
```

***Fig. 2:** XAI interpretability–action–trust cycle.*

---

## Challenges and considerations

XAI plays a critical role not only in surveillance and intervention, but also in building resilience through feedback and adaptation. Its inherent capacity for continual learning allows for iterative improvements in One Health decision-making. Despite these advantages of integrating XAI and One Health in combating IDs, several challenges persist.

A key limitation is that explainability does not inherently imply causal understanding. Many widely used XAI approaches rely on post hoc explanations of complex models, which may be sensitive to data perturbations, modelling choices, or the selection of explanation methods, potentially creating false reassurance if interpreted uncritically in high-stakes health contexts.<sup>52,53</sup> These concerns highlight the need to view XAI as a complementary tool rather than a substitute for external validation, domain expertise, and inherently interpretable models. In One Health contexts, especially in highly complex systems, some predictions may arise from non-linear interactions that remain only partially explainable. In these cases, XAI results should be interpreted with biological and ecological plausibility in mind and supported by domain expertise, rather than treated as evidence of mechanistic interactions or causal relationships without further validation.<sup>52,53</sup>

One of the biggest challenges is integrating heterogeneous data across human, animal, and environmental domains. These datasets often differ in structure, format (e.g., text, imaging, numerical data), spatial and temporal resolution, quality, and accessibility, making standardisation difficult. Such fragmentation constrains the potential of XAI models by reducing interpretability. To support transparent and robust outputs, developing data harmonisation protocols, intersectoral data infrastructure and multimodal XAI frameworks are essential.

Alongside technical challenges, ethical and privacy concerns arise when deploying AI in cross-sectoral health contexts. Sensitive information from medical records, zoonotic surveillance systems, and environmental monitoring must be protected. Because the nature of One Health is interdisciplinary, managing data governance, privacy, and compliance with government regulations can be challenging. Explainability serves as an ethical safeguard by exposing biases and unintended consequences in model reasoning. Biases in data and model outputs can lead to the stigmatisation of communities, unequal health interventions, and underrepresented wildlife populations. Thus, ethical considerations must be taken to ensure accountability and fairness across animal, human, and environmental health. While explainability methods such as SHAP and LIME enhance transparency at model level, system-level transparency is equally vital for real-world adoption. This broader dimension includes clear communication of model outputs, rationale for interventions, data governance, and mechanisms for public accountability.

Despite growing interest and promising applications, XAI remains a developing field that requires further refinement. Most existing explainability methods were initially designed for general-purpose, non-spatial tasks and are not optimised for the complex, multi-scale data environments typical of One Health applications. However, recent studies have shown that XAI-enhanced models can capture spatial patterns in ways comparable to conventional approaches.<sup>75</sup> These applications, however, require further validation across longitudinal and cross-sectoral contexts, particularly given the trade-off between model interpretability and predictive performance.

---

## Future directions

Unlocking XAI’s potential in One Health demands coordinated investment and integration; otherwise, it will remain underused. Here, “investment” includes interoperable data infrastructure, analytic capacity, workforce training, decision-support tools, and governance frameworks for privacy, fairness, and auditability. Many stakeholders, including local public health practitioners, veterinary officers, and policy analysts, lack training or resources to interpret model outputs. Educational programs and dashboards tailored to user needs can help democratise access to XAI tools.

Deeper interdisciplinary collaboration is essential. Algorithmic performance alone is insufficient without integrating expertise from epidemiology, veterinary science, ecology and environmental health with data and computer science. AI developers should co-design models with One Health practitioners to reflect real-world constraints and priorities. Robust policy and governance frameworks are also essential to ensure that XAI is deployed ethically and equitably. National and global agencies should develop guidelines that incorporate responsible AI principles, such as transparency, fairness, and accountability, into One Health systems. These standards should include validation procedures, reporting requirements, and equity-focused assessments.

Finally, future research must address persistent technical gaps. These include the need for scalable XAI methods that can handle spatiotemporal data, support domain adaptation, and function across complex, multimodal datasets. Key priorities include enhancing explainability for graph neural networks, real-time surveillance models, and multi-level causal frameworks. As these innovations mature, they can shift XAI from retrospective interpretation toward prospective guidance, improving timeliness and precision in cross-sectoral responses. Moving forward, efforts must be collaborative, ethically grounded, and driven by both scientific innovation and operational feasibility, ensuring that XAI becomes a reliable and trusted tool for ID surveillance, forecasting, and management across species and systems.

---

## Conclusion

Integrating XAI into the One Health framework offers a transformative opportunity to improve the prediction, prevention, preparedness, and control of IDs. By making complex models interpretable, XAI enables targeted interventions and supports cross-sector decision-making in dynamic systems. As illustrated here, XAI not only enhances technical transparency but also promotes trust and equity, empowering stakeholders across human, animal, plant, and environmental domains to act on shared health insights. Realising this potential will require sustained efforts to embed transparency in AI systems, strengthen interdisciplinary collaboration, and advance innovation in explainability methods adapted to One Health contexts. We call on researchers, practitioners, and policymakers to jointly pursue ethical, effective, and scalable applications of XAI that support resilient, equitable, and sustainable health outcomes across species and sectors.

---

> ### Search strategy and selection criteria
> We searched literature from PubMed and Google Scholar up to January 25, 2026. Queries combined One Health and infectious disease concepts (e.g., “One Health,” “infectious diseases,” “zoonotic,” “spillover,” and “forecasting/surveillance”) with AI and explainability-related terms (e.g., “explainable artificial intelligence (XAI),” “model interpretability,” SHAP, and LIME). Terms related to common modelling approaches (e.g., compartmental and statistical/time-series models), AMR/ARG terminology, and disease-specific keywords (e.g., influenza/H5N1 and dengue) were added as needed. Searches used Boolean operators (e.g., AND/OR) where appropriate. We included peer-reviewed English-language articles, prioritising studies from the past five years. Conference abstracts, meeting reports, and non-peer-reviewed supplements were excluded; authoritative sources (e.g., WHO) were cited when needed. Only a small number of peer-reviewed conference papers were included when they were relevant. References were selected based on relevance and the quality.

> ### Outstanding questions
> A key outstanding question is how XAI can be integrated into One Health to enable coordinated decision-making across human, animal, and environmental systems. Related questions include how XAI can be operationalised in real-time cross-sector surveillance, what data streams are required to build reliable and explainable models that generalise across domains, and how XAI can support causal reasoning rather than correlation-driven interpretation in ID modelling.

---

### Contributors
YC and JW conceptualised the study. YC, EL and JW wrote the original draft. YC, EL, JL and JW reviewed and edited the manuscript. All the authors have read and approved the final manuscript.

### Declaration of interests
We declare no competing interests.

### Acknowledgements
We acknowledge the support of the OSU Health Sciences Library for assistance with access to the literature. The authors used ChatGPT (OpenAI) to assist with language editing and improve clarity. All scientific content, interpretations, and conclusions remain the responsibility of the authors.

---

## References

1. Baker RE, Mahmud AS, Miller IF, et al. Infectious disease in an era of global change. *Nat Rev Microbiol*. 2022;20(4):193–205.
2. World Health Organization. *Number of COVID-19 Deaths Reported to WHO (cumulative total)*; 2025. https://data.who.int/dashboards/covid19/deaths?n=c&m49=001. Accessed November 27, 2025.
3. Naseer S, Khalid S, Parveen S, Abbass K, Song H, Achim MV. COVID-19 outbreak: impact on global economy. *Front Public Health*. 2022;10:1009393.
4. Karesh WB, Dobson A, Lloyd-Smith JO, et al. Ecology of zoonoses: natural and unnatural histories. *Lancet*. 2012;380(9857):1936–1945.
5. Taylor LH, Latham SM, Woolhouse ME. Risk factors for human disease emergence. *Philos Trans R Soc B Biol Sci*. 2001;356(1411):983–989.
6. Barbier EB. Habitat loss and the risk of disease outbreak. *J Environ Econ Manag*. 2021;108:102451.
7. World Health Organization. *One Health*; 2017. https://www.who.int/news-room/questions-and-answers/item/one-health. Accessed July 17, 2025.
8. Cao Y, Martins R, Lee J, Wu J. Navigating one health impacts of rugged terrain: challenges and opportunities. *BioScience*. 2025;biaf126.
9. Sinclair JR. Importance of a one health approach in advancing global health security and the sustainable development goals. *Rev Sci Tech*. 2019;38(1):145–154.
10. One Health High-Level Expert Panel OHHLEP, Adisasmito WB, Almuhairi S, et al. One health: a new definition for a sustainable and healthy future. *PLoS Pathog*. 2022;18(6):e1010537.
11. McClymont H, Bambrick H, Si X, Vardoulakis S, Hu W. Future perspectives of emerging infectious diseases control: a one health approach. *One Health*. 2022;14:100371.
12. Sikkema RS, Koopmans M. Viral emergence and pandemic preparedness in a one health framework. *Nat Rev Microbiol*. 2025;24:29–44.
13. Li T, Zhou X-N, Tanner M. One health: enabler of effective prevention, control and elimination of emerging and re-emerging infectious diseases. *Infect Dis Poverty*. 2025;14(1):77.
14. Wu Q, Li Q, Lu J. A one Health strategy for emerging infectious diseases based on the COVID-19 outbreak. *J Biosaf Biosecur*. 2022;4(1):5–11.
15. Breitschwerdt EB. Bartonellosis: one health perspectives for an emerging infectious disease. *ILAR J*. 2014;55(1):46–58.
16. Gronvall G, Boddie C, Knutsson R, Colby M. One health security: an important component of the global health security agenda. *Biosecur Bioterror*. 2014;12(5):221–224.
17. Kelly TR, Machalaba C, Karesh WB, et al. Implementing One Health approaches to confront emerging and re-emerging zoonotic disease threats: lessons from PREDICT. *One Health Outlook*. 2020;2:1–7.
18. Wang C-X, Xiu L-S, Hu Q-Q, et al. Advancing early warning and surveillance for zoonotic diseases under climate change: interdisciplinary systematic perspectives. *Adv Clim Change Res*. 2023;14(6):814–826.
19. Judijanto L, Hermansyah H, Ningsih KP, Anurogo D, Firdaus M. The role of big data technology in predicting and managing the spread of infectious diseases. *J World Future Med Health Nurs*. 2024;2(2):216–227.
20. Isiaka AB, Anakwenze VN, Ilodinso CR, et al. Harnessing artificial intelligence for early detection and management of infectious disease outbreaks. *Int J Innov Res Dev*. 2024;13(2):52–65.
21. Minh D, Wang HX, Li YF, Nguyen TN. Explainable artificial intelligence: a comprehensive review. *Artif Intell Rev*. 2022;55(5):3503–3568.
22. Barredo Arrieta A, Díaz-Rodríguez N, Del Ser J, et al. Explainable Artificial Intelligence (XAI): concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion*. 2020;58:82–115.
23. Koopmans M, Csabai I, Remondini D, Snary E, Aarestrup F. Artificial intelligence and one health: potential for spillover prediction? *Lancet Infect Dis*. 2025;26(3):219–220.
24. Kraemer MUG, Tsui JL, Chang SY, et al. Artificial intelligence for modelling infectious disease epidemics. *Nature*. 2025;638(8051):623–635.
25. Lundberg SM, Lee S-I. A unified approach to interpreting model predictions. *Adv Neural Inf Process Syst*. 2017;30.
26. Ribeiro MT, Singh S, Guestrin C. “Why should i trust you?” explaining the predictions of any classifier. In: *Proceedings of the 22nd ACM SIGKDD international conference on Knowledge Discovery and Data Mining*. 2016:1135–1144.
27. Singh S, Sharma P, Pal N, Sarma DK, Tiwari R, Kumar M. Holistic one health surveillance framework: synergizing environmental, animal, and human determinants for enhanced infectious disease management. *ACS Infect Dis*. 2024;10(3):808–826.
28. Gulumbe BH, Abdulrahim A, Ahmad SK, Lawan KA, Danlami MB. WHO report signals tuberculosis resurgence: addressing systemic failures and revamping control strategies. *Decod Infect Transm*. 2025;3:100044.
29. Moore S, Worku Demlie Y, Muluneh D, et al. Spatiotemporal dynamics of cholera epidemics in Ethiopia: 2015–2021. *Sci Rep*. 2024;14(1):7170.
30. Adepoju P. Mpox declared a public health emergency. *Lancet*. 2024;404(10454):e1–e2.
31. Durrheim DN, Andrus JK, Tabassum S, Bashour H, Githanga D, Pfaff G. A dangerous measles future looms beyond the COVID-19 pandemic. *Nat Med*. 2021;27(3):360–361.
32. Krammer F, Hermann E, Rasmussen AL. Highly pathogenic avian influenza H5N1: history, current situation, and outlook. *J Virol*. 2025;99(4):e0220924–e0222224.
33. Wu T, Wu Z, Li YP. Dengue fever and dengue virus in the People’s Republic of China. *Rev Med Virol*. 2022;32(1):e2245.
34. Choi YK. Emerging and re-emerging fatal viral diseases. *Exp Mol Med*. 2021;53(5):711–712.
35. Bloom DE, Cadarette D. Infectious disease threats in the twenty-first century: strengthening the global response. *Front Immunol*. 2019;10:549.
36. Nova N, Athni TS, Childs ML, Mandle L, Mordecai EA. Global change and emerging infectious diseases. *Annu Rev Resour Econ*. 2022;14(1):333–354.
37. Horby PW, Hoa NT, Pfeiffer DU, Wertheim HF. Drivers of Emerging Zoonotic Infectious Diseases. *Confronting Emerging Zoonoses: The One Health Paradigm*. Tokyo: Springer; 2014:13–26.
38. Mahon MB, Sack A, Aleuy OA, et al. A meta-analysis on global change drivers and the risk of infectious disease. *Nature*. 2024;629(8013):830–836.
39. Riley MF. One health pandemic prevention and mitigation. *Food Drug Law J*. 2021;76(2):200–234.
40. Mackenzie JS, Jeggo M. *The One Health Approach—Why is it so Important?* MDPI; 2019:88.
41. Mumford EL, Martinez DJ, Tyance-Hassell K, et al. Evolution and expansion of the one health approach to promote sustainable and resilient health and well-being: a call to action. *Front Public Health*. 2022;10:1056459.
42. Cabrera M, Leake J, Naranjo-Torres J, Valero N, Cabrera JC, Rodríguez-Morales AJ. Dengue prediction in Latin America using machine learning and the one health perspective: a literature review. *Trop Med Infect Dis*. 2022;7(10):322.
43. Huang J, Morris JS. Infectious disease modeling. *Annu Rev Stat Appl*. 2025;12:19–44.
44. Moein S, Nickaeen N, Roointan A, et al. Inefficiency of SIR models in forecasting COVID-19 epidemic: a case study of Isfahan. *Sci Rep*. 2021;11(1):4725.
45. Adegoke BO, Odugbose T, Adeyemi C. Data analytics for predicting disease outbreaks: a review of models and tools. *Int J Life Sci Res Upd*. 2024;2(2):1–9.
46. Santangelo OE, Gentile V, Pizzo S, Giordano D, Cedrone F. Machine learning and prediction of infectious diseases: a systematic review. *Mach Learn Knowl Extr*. 2023;5(1):175–198.
47. Villanueva-Miranda I, Xiao G, Xie Y. Artificial intelligence in early warning systems for infectious disease surveillance: a systematic review. *Front Public Health*. 2025;13:1609615.
48. Zhao AP, Li S, Cao Z, et al. AI for science: predicting infectious diseases. *J Saf Sci Resil*. 2024;5(2):130–146.
49. Telford CT, Amman BR, Towner JS, Montgomery JM, Lessler J, Shoemaker T. Predictive model for estimating annual ebolavirus spillover potential. *Emerg Infect Dis*. 2025;31(4):689–698.
50. Becker DJ, Albery GF, Sjodin AR, et al. Optimising predictive models to prioritise viral discovery in zoonotic reservoirs. *Lancet Microbe*. 2022;3(8):e625–e637.
51. Kim J, Ahn I. Infectious disease outbreak prediction using media articles with machine learning models. *Sci Rep*. 2021;11(1):4413.
52. Ghassemi M, Oakden-Rayner L, Beam AL. The false hope of current approaches to explainable artificial intelligence in health care. *Lancet Digit Health*. 2021;3(11):e745–e750.
53. Rudin C. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nat Mach Intell*. 2019;1(5):206–215.
54. Salih AM, Raisi-Estabragh Z, Galazzo IB, et al. A perspective on explainable artificial intelligence methods: SHAP and LIME. *Adv Intell Syst*. 2025;7(1):2400304.
55. Rahman MS, Shiddik MAB. Explainable artificial intelligence for predicting dengue outbreaks in Bangladesh using eco-climatic triggers. *Glob Epidemiol*. 2025;10:100210.
56. Farooq Z, Rocklöv J, Wallin J, et al. Artificial intelligence to predict West Nile virus outbreaks with eco-climatic drivers. *Lancet Reg Health Eur*. 2022;17:100370.
57. Muriithi DK, Lumumba VW, Awe OO, Muriithi DM. An explainable artificial intelligence models for predicting malaria risk in Kenya. *Eur J Artif Intell Mach Learn*. 2025;4(1):1–8.
58. Schnepf A, Hille K, van Mark G, et al. Basis for a one health approach—inventory of routine data collections on zoonotic diseases in lower Saxony, Germany. *Zoonotic Dis*. 2024;4(1):57–73.
59. Ligda P, Mittas N, Kyzas GZ, Claerebout E, Sotiraki S. Machine learning and explainable artificial intelligence for the prevention of waterborne cryptosporidiosis and giardiosis. *Water Res*. 2024;262:122110.
60. Opata MR, Lavarello-Schettini A, Semenza JC, Rocklöv J. Predictiveness and drivers of highly pathogenic avian influenza outbreaks in Europe. *Sci Rep*. 2025;15(1):20286.
61. Rahmat F, Zulkafli Z, Ishak AJ, et al. Interpretable spatio-temporal prediction using deep neural network-local interpretable model-agnostic explanations: a case study on leptospirosis outbreaks in Malaysia. *Eng Appl Artif Intell*. 2025;151:110665.
62. Zhang Y, Wang J, Wang L, et al. An integrated machine learning framework to understand zoonotic spillover emergence across anthropogenically modified landscapes. *Environ Health Perspect*. 2025.
63. Phang WK, Hamid MHBA, Jelip J, et al. Predicting *Plasmodium knowlesi* transmission risk across Peninsular Malaysia using machine learning-based ecological niche modeling approaches. *Front Microbiol*. 2023;14:1126418.
64. Murray CJ, Ikuta KS, Sharara F, et al. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. *Lancet*. 2022;399(10325):629–655.
65. Mills MC, Lee J. The threat of carbapenem-resistant bacteria in the environment: evidence of widespread contamination of reservoirs at a global scale. *Environ Pollut*. 2019;255:113143.
66. Robinson TP, Bu D, Carrique-Mas J, et al. Antibiotic resistance is the quintessential one health issue. *Trans R Soc Trop Med Hyg*. 2016;110(7):377–380.
67. Espinoza JL, Dupont CL, O’Rourke A, et al. Predicting antimicrobial mechanism-of-action from transcriptomes: a generalizable explainable artificial intelligence approach. *PLoS Comput Biol*. 2021;17(3):e1008857.
68. Samtiya M, Matthews KR, Dhewa T, Puniya AK. Antimicrobial resistance in the food chain: trends, mechanisms, pathways, and possible regulation strategies. *Foods*. 2022;11(19):2966.
69. Buyuktepe O, Catal C, Kar G, Bouzembrak Y, Marvin H, Gavai A. Food fraud detection using explainable artificial intelligence. *Expert Systems*. 2025;42(1):e13387.
70. Esposito MM, Turku S, Lehrfield L, Shoman A. The impact of human activities on zoonotic infection transmissions. *Animals*. 2023;13(10):1646.
71. Chen F, Jiang F, Ma J, Alghamdi MA, Zhu Y, Yong JWH. Intersecting planetary health: exploring the impacts of environmental stressors on wildlife and human health. *Ecotoxicol Environ Saf*. 2024;283:116848.
72. Pfenning-Butterworth A, Buckley LB, Drake JM, et al. Interconnecting global threats: climate change, biodiversity loss, and infectious diseases. *Lancet Planet Health*. 2024;8(4):e270–e283.
73. Kundu S, Datta P, Pal P, Ghosh K, Das A, Das BK. Unveiling the hidden connections: using explainable artificial intelligence to assess water quality criteria in nine giant rivers. *J Clean Prod*. 2025;492:144861.
74. Liu Y, Cao Y, Chen Q, Wu J. Uncovering the influence of land cover and climate extremes on wildfire smoke PM(2.5) in the United States using explainable artificial intelligence. *Environ Sci Technol*. 2025;59(46):24874–24887.
75. Li Z. Extracting spatial effects from machine learning model using local interpretation method: an example of SHAP and XGBoost. *Comput Environ Urban Syst*. 2022;96:101845.
