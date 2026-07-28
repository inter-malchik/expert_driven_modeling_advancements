"""Commentary, responsive, and analysis CSS fragments."""

from __future__ import annotations

PAPER_COMMENTARY_CSS = """
.paper-commentary {
    column-span: all;
    background: var(--commentary-bg, #f7f2f5);
    border: 1px solid var(--commentary-border, #d8c8d2);
    border-left: 4px solid var(--commentary-accent, #8a6d82);
    border-radius: 4px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 9.5pt;
    line-height: 1.45;
    color: #3f3438;
    overflow: hidden;
}

.paper-commentary-summary {
    cursor: pointer;
    list-style: none;
    padding: 0.55rem 0.8rem 0.55rem 1.6rem;
    position: relative;
    user-select: none;
}

.paper-commentary-summary::-webkit-details-marker {
    display: none;
}

.paper-commentary-summary::before {
    content: "▸";
    position: absolute;
    left: 0.55rem;
    top: 0.62rem;
    font-size: 0.85rem;
    color: var(--commentary-accent, #8a6d82);
    transition: transform 0.15s ease;
}

.paper-commentary[open] .paper-commentary-summary::before {
    content: "▾";
}

.paper-commentary-summary:hover {
    background: var(--commentary-highlight, #efe6ec);
}

.paper-commentary-body {
    padding: 0 0.8rem 0.65rem;
    border-top: 1px solid var(--commentary-border, #d8c8d2);
    overflow-x: clip;
    overflow-wrap: anywhere;
}

.paper-commentary-body,
.paper-commentary-body * {
    box-sizing: border-box;
    max-width: 100%;
}

.paper-commentary-body [data-testid="stMarkdownContainer"] p {
    margin: 0 0 0.45rem !important;
    text-align: left;
    text-indent: 0;
    font-size: 9.5pt;
    line-height: 1.4;
}

.paper-commentary-body [data-testid="stMarkdownContainer"] {
    width: 100%;
}

.paper-commentary-body h1,
.paper-commentary-body h2,
.paper-commentary-body h3,
.paper-commentary-body h4,
.paper-commentary-body h5,
.paper-commentary-body h6 {
    margin: 0.8rem 0 0.4rem;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 10pt;
    line-height: 1.3;
    color: #3f3438;
}

.paper-commentary-body ul,
.paper-commentary-body ol {
    margin: 0 0 0.55rem 1.15rem;
    padding-left: 0.85rem;
}

.paper-commentary-body li {
    margin: 0 0 0.3rem;
    line-height: 1.45;
}

.paper-commentary-body blockquote {
    margin: 0.35rem 0 0.45rem 0.35rem;
    padding: 0.15rem 0 0.15rem 0.75rem;
    border-left: 2px solid var(--commentary-border, #d8c8d2);
    color: #5a4d52;
}

.paper-commentary-body blockquote p {
    margin: 0 !important;
}

.paper-commentary-body code {
    white-space: break-spaces;
    overflow-wrap: anywhere;
    background: rgba(255, 255, 255, 0.65);
    border-radius: 3px;
    padding: 0.05rem 0.25rem;
    font-size: 0.92em;
}

.paper-commentary-math {
    font-family: "Times New Roman", Times, serif;
}

.paper-commentary-head {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    margin-bottom: 0.2rem;
    flex-wrap: wrap;
}

.paper-commentary-marker {
    font-family: "Times New Roman", Times, serif;
    font-weight: 700;
    font-size: 1.05rem;
    color: var(--commentary-accent, #8a6d82);
}

.paper-commentary-type {
    font-size: 0.95rem;
    line-height: 1;
    display: inline-flex;
    align-items: center;
}

.paper-commentary-label {
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--commentary-accent, #8a6d82);
}

.paper-commentary-relevance-summary {
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 0.03em;
    color: var(--commentary-accent, #8a6d82);
    white-space: nowrap;
}

.paper-commentary-category {
    font-size: 7.5pt;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--commentary-accent, #8a6d82);
    margin-left: auto;
}

.paper-commentary-id {
    font-size: 0.7rem;
    font-weight: 400;
    opacity: 0.7;
    margin-left: 0.35rem;
    text-transform: none;
    letter-spacing: normal;
}

.paper-commentary-hidden-toggle {
    background: none;
    border: 1px solid var(--commentary-border, #d8c8d2);
    border-radius: 3px;
    color: var(--commentary-accent, #8a6d82);
    cursor: pointer;
    font-size: 7.5pt;
    padding: 0 3px;
    height: 18px;
    min-width: 18px;
    line-height: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    margin-left: 0.5rem;
}

.paper-commentary-hidden-toggle:hover {
    background: var(--commentary-accent, #8a6d82);
    color: white;
}

.paper-commentary.is-hidden {
    opacity: 0.4;
}

.paper-commentary.is-hidden[open] {
    opacity: 0.6;
}

.paper-commentary-title {
    margin: 0;
    font-size: 10pt;
    text-align: left;
    text-indent: 0;
}

.paper-commentary-quote {
    margin: 0 0 0.45rem;
    font-style: italic;
    color: #5a4d52;
    text-align: left;
    text-indent: 0;
}

.paper-commentary-anchor-link {
    margin: 0 0 0.45rem !important;
    font-size: 8.5pt;
    text-align: left;
    text-indent: 0;
}

.paper-commentary-anchor-link a {
    color: var(--commentary-accent, #8a6d82);
    text-decoration: none;
    font-weight: 600;
}

.paper-commentary-anchor-link a:hover {
    text-decoration: underline;
}

.paper-commentary p {
    margin: 0 0 0.45rem;
    text-align: left;
    text-indent: 0;
}

.paper-commentary-filenote {
    font-family: "Courier New", monospace;
    font-size: 8pt;
    color: #8b4a67;
    margin: 0 0 0.35rem !important;
}

.paper-commentary-analysis-link {
    margin: 0 0 0.45rem !important;
    text-align: left;
    text-indent: 0;
}

.paper-commentary-analysis-link a {
    color: #2a7ae2;
    font-weight: 600;
    text-decoration: none;
}

.paper-commentary-analysis-link a:hover {
    text-decoration: underline;
}

.paper-commentary-sources {
    list-style: none;
    margin: 0;
    padding: 0.45rem 0 0;
}

.paper-commentary-sources-details {
    margin-top: 0.45rem;
    padding-top: 0.45rem;
    border-top: 1px solid var(--commentary-border, #d8c8d2);
}

.paper-commentary-sources-panel {
    padding-top: 0.15rem;
}

.paper-commentary-sources-summary {
    font-size: 8.5pt;
    font-weight: 600;
    color: var(--commentary-accent, #8a6d82);
    cursor: pointer;
    list-style: none;
    display: flex;
    align-items: center;
}

.paper-commentary-sources-summary::-webkit-details-marker {
    display: none;
}

.paper-commentary-sources-summary::before {
    content: "▶";
    font-size: 7pt;
    margin-right: 0.4rem;
    transition: transform 0.2s;
}

.paper-commentary-sources-details[open] .paper-commentary-sources-summary::before {
    transform: rotate(90deg);
}

.paper-commentary-sources li {
    font-size: 8.5pt;
    line-height: 1.4;
    margin-bottom: 0.3rem;
    padding-left: 1rem;
    position: relative;
    color: #4a4044;
}

.paper-commentary-sources li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.45em;
    width: 0.45em;
    height: 0.45em;
    border-radius: 50%;
}

.paper-commentary-sources li.verified::before {
    background: #2F6B62;
}

.paper-commentary-sources li.pending::before {
    border: 1.5px solid var(--commentary-accent, #8a6d82);
    background: transparent;
}

.paper-commentary-source-link {
    color: #2a7ae2;
    text-decoration: none;
}

.paper-commentary-source-link:hover {
    text-decoration: underline;
}

.paper-commentary-sources-markdown {
    margin-top: 0.45rem;
}

.paper-commentary-sources-markdown > :first-child {
    margin-top: 0;
}

.paper-commentary-sources-markdown h1,
.paper-commentary-sources-markdown h2,
.paper-commentary-sources-markdown h3,
.paper-commentary-sources-markdown h4,
.paper-commentary-sources-markdown h5,
.paper-commentary-sources-markdown h6 {
    font-size: 9pt;
}

.paper-commentary-relevance-box {
    margin-top: 0.7rem;
    padding-top: 0.55rem;
    border-top: 1px dashed var(--commentary-border, #d8c8d2);
}

.paper-commentary-relevance-heading {
    margin: 0 0 0.3rem !important;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--commentary-accent, #8a6d82) !important;
}

.paper-commentary-relevance-overall {
    margin: 0 0 0.35rem !important;
    font-size: 8.75pt;
}

.paper-commentary-relevance-basis {
    color: #6b5f64;
}

.paper-commentary-relevance-metrics {
    margin: 0 0 0.45rem !important;
}

.paper-commentary-relevance-item {
    margin: 0 0 0.2rem !important;
    font-size: 8.75pt;
    padding-left: 0;
}

.paper-commentary-relevance-text {
    margin: 0 0 0.3rem !important;
    font-size: 8.75pt;
}

.paper-commentary-update-box {
    margin-top: 0.65rem;
    padding-top: 0.55rem;
    border-top: 1px dashed var(--commentary-border, #d8c8d2);
    font-size: 8.5pt;
}

.paper-commentary-update-label {
    font-weight: 700;
    color: var(--commentary-accent, #8a6d82);
    margin-right: 0.3rem;
}

.paper-commentary-update-text {
    color: #333;
}

.paper-commentary-update-details {
    color: #5a4d52;
}

.paper-body h2,
.paper-body h3 {
    scroll-margin-top: 1rem;
}

@media (max-width: 900px) {
    .paper-body,
    .paper-references {
        column-count: 1;
    }

    .paper-columns {
        grid-template-columns: 1fr;
    }
}

.stApp:has(#sidebar-state-hidden) section[data-testid="stSidebar"] {
    display: none !important;
    width: 0 !important;
    min-width: 0 !important;
    max-width: 0 !important;
}

.stApp:has(#sidebar-state-hidden) [data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

.stApp:has(#sidebar-state-hidden) section[data-testid="stMain"],
section[data-testid="stSidebar"][aria-expanded="false"] ~ section[data-testid="stMain"] {
    flex: 1 1 auto !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
}

.stApp:has(#sidebar-state-hidden) [data-testid="stMainBlockContainer"],
section[data-testid="stSidebar"][aria-expanded="false"] ~ section[data-testid="stMain"] [data-testid="stMainBlockContainer"] {
    max-width: none !important;
    width: 100% !important;
}

.sidebar-show-bar {
    margin: 0 0 0.75rem;
}

.sidebar-show-bar button {
    font-size: 0.78rem !important;
    padding: 0.2rem 0.65rem !important;
    min-height: 0 !important;
}
"""

ANALYSIS_CSS = """
.analysis-shell {
    width: 100%;
    max-width: none;
    margin: 0;
    padding: 1.25rem 0 2.5rem;
    font-family: "Times New Roman", Times, serif;
    color: #1a1a1a;
    line-height: 1.55;
}
.analysis-shell h1,
.analysis-shell h2,
.analysis-shell h3,
.analysis-shell h4 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #2b2b2b;
    margin-top: 1.4rem;
    margin-bottom: 0.6rem;
}
.analysis-shell p,
.analysis-shell li {
    font-size: 11pt;
}
.analysis-shell table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    font-size: 10pt;
}
.analysis-shell th,
.analysis-shell td {
    border: 1px solid #ccc;
    padding: 0.45rem 0.55rem;
    vertical-align: top;
}
.analysis-shell blockquote {
    border-left: 3px solid #d4739a;
    margin: 0.8rem 0;
    padding: 0.2rem 0 0.2rem 0.9rem;
    color: #444;
}

.analysis-shell blockquote:first-of-type {
    border-left-color: #9a8a92;
    background: #faf8f9;
    padding: 0.65rem 0.9rem;
    border-radius: 4px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 9.5pt;
    line-height: 1.5;
}
.analysis-nav {
    margin-bottom: 1rem;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 10pt;
}
.analysis-nav a {
    color: #2a7ae2;
    text-decoration: none;
}
.analysis-nav a:hover {
    text-decoration: underline;
}

.analysis-sources-wrap {
    margin: 0 0 1.25rem;
    padding: 0.75rem 0.9rem;
    border: 1px solid #d8d0d4;
    border-radius: 4px;
    background: #faf8f9;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.analysis-sources-label {
    margin: 0 0 0.45rem;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #6a5d63;
}

.analysis-sources {
    list-style: none;
    margin: 0;
    padding: 0;
}

.analysis-sources li {
    font-size: 9.5pt;
    line-height: 1.45;
    margin-bottom: 0.35rem;
    padding-left: 1rem;
    position: relative;
    color: #3f3438;
}

.analysis-sources li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.45em;
    width: 0.45em;
    height: 0.45em;
    border-radius: 50%;
    background: #5f8f78;
}

.analysis-sources li.pending::before {
    background: transparent;
    border: 1.5px solid #9a8a92;
}

.analysis-source-link {
    color: #2a7ae2;
    text-decoration: none;
}

.analysis-source-link:hover {
    text-decoration: underline;
}
"""
