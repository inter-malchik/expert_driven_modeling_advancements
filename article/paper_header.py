"""Static header rendering for the paper view."""

from __future__ import annotations

import streamlit as st


def render_header() -> None:
    st.markdown(
        """
<div class="paper-shell">
<div class="paper-banner">
  <div>
    <p class="paper-meta"><strong>Contents lists available at ScienceDirect</strong></p>
    <p class="paper-journal-title">Expert Systems With Applications</p>
    <p class="paper-meta"><strong>journal homepage:</strong> <a href="https://www.elsevier.com/locate/eswa">www.elsevier.com/locate/eswa</a></p>
  </div>
  <div class="paper-volume">Expert Systems With Applications 315 (2026) 131730</div>
</div>

<p class="paper-title">Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models</p>

<p class="paper-authors">
<strong>Dinara Gindullina</strong><sup>a</sup>,
<strong>Mark Lazutov</strong><sup>a</sup>,
<strong>Kirill Stolyarov</strong><sup>b</sup>,
<strong>Daria Danilenko</strong><sup>b</sup>,
<strong>Vasiliy Leonenko</strong><sup>a,b,*</sup>
</p>

<p class="paper-affiliations">
<sup>a</sup> <em>ITMO University, Kronverksky Pr. 49, Saint Petersburg, 197101, Russia</em><br>
<sup>b</sup> <em>Smorodintsev Research Institute for Influenza, St. Prof. Popova 15/17, Saint Petersburg, 197022, Russia</em>
</p>

<hr class="paper-rule" />

<div class="paper-columns">
<div>
<p class="paper-section-label">ARTICLE INFO</p>
<p class="paper-keywords"><em>Keywords:</em><br>
influenza<br>
SARS-CoV-2<br>
predictive modeling<br>
LLM<br>
PINN
</p>
</div>
<div>
<p class="paper-section-label">ABSTRACT</p>
<p class="paper-abstract">
This paper presents an agent-based AI system that uses large-scale language models (LLMs) to dynamically adapt physically-informed neural networks (PINNs) based on high-quality expert judgment. Our system enables interactive refinement of epidemiological forecasts by translating unstructured expert feedback into structured modifications of the loss function, eliminating the need for prior mathematical formalization. Experimental results confirm the fundamental feasibility of this approach, demonstrating a success rate of 25-27% for the best models and providing a compelling proof-of-concept for using LLMs as core components of interactive decision support systems. This work represents a step toward building robust expert-led forecasting systems for public health problems, while simultaneously highlighting the need to develop more rigorous control mechanisms to ensure full robustness. The code of our system is available at <a href="https://github.com/vnleonenko/Epi_PINN_LLM">https://github.com/vnleonenko/Epi_PINN_LLM</a>.
</p>
</div>
</div>

<hr class="paper-rule" />

<div class="paper-footer-meta">
<p><strong>Corresponding author.</strong> Smorodintsev Research Institute for Influenza, St. Prof. Popova 15/17, Saint Petersburg, 197022, Russia.</p>
<p>E-mail addresses: <a href="mailto:mark.lazutov@gmail.com">mark.lazutov@gmail.com</a> (M. Lazutov), <a href="mailto:vasiliy.leonenko@gmail.com">vasiliy.leonenko@gmail.com</a> (V. Leonenko).</p>
<p>Received 12 December 2025; Received in revised form 2 March 2026; Accepted 3 March 2026</p>
<p>Available online 4 March 2026</p>
<p><a href="https://doi.org/10.1016/j.eswa.2026.131730">https://doi.org/10.1016/j.eswa.2026.131730</a></p>
<p>0957-4174/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.</p>
</div>
</div>
        """,
        unsafe_allow_html=True,
    )
