PAPER_CSS = """
section[data-testid="stSidebar"][aria-expanded="true"] {
    width: 15.5rem !important;
    min-width: 15.5rem !important;
}

section[data-testid="stSidebar"][aria-expanded="true"] > div {
    width: 15.5rem !important;
    min-width: 15.5rem !important;
}

section[data-testid="stSidebar"][aria-expanded="false"] {
    width: 0 !important;
    min-width: 0 !important;
    max-width: 0 !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"][aria-expanded="false"] > div {
    width: 0 !important;
    min-width: 0 !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    font-size: 0.68rem;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] li,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] strong,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a,
section[data-testid="stSidebar"] .stButton button {
    font-size: 0.68rem;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
section[data-testid="stSidebar"] [data-testid="stHeader"] {
    font-size: 0.82rem;
}

section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    font-size: 0.62rem;
}

.main .block-container,
[data-testid="stMainBlockContainer"] {
    max-width: none;
    width: 100%;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    padding-left: max(1.25rem, 2.5vw);
    padding-right: max(1.25rem, 2.5vw);
    container-type: inline-size;
    container-name: article-main;
}

section[data-testid="stMain"] > div {
    max-width: none;
}

[data-testid="stMarkdownContainer"] .paper-shell {
    width: 100%;
    max-width: none;
    font-family: "Times New Roman", Times, serif;
    color: #111;
    --paper-text: clamp(11pt, 1.05cqw + 8pt, 18pt);
    font-size: var(--paper-text) !important;
    line-height: 1.5;
}

.paper-shell {
    width: 100%;
    max-width: none;
    font-family: "Times New Roman", Times, serif;
    color: #111;
    --paper-text: clamp(11pt, 1.05cqw + 8pt, 18pt);
    font-size: var(--paper-text);
    line-height: 1.5;
}

@supports not (container-type: inline-size) {
    [data-testid="stMarkdownContainer"] .paper-shell,
    .paper-shell {
        --paper-text: clamp(11pt, 0.95vw + 7pt, 18pt);
    }
}

.paper-shell a {
    color: #2a7ae2;
    text-decoration: none;
}

.paper-shell a:hover {
    text-decoration: underline;
}

.paper-banner {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 0.5rem;
    font-size: 9pt;
    color: #444;
}

.paper-journal-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin: 0.25rem 0;
}

.paper-volume {
    font-size: 9pt;
    color: #444;
    text-align: right;
}

.paper-meta {
    color: #555;
    font-size: 9.5pt;
    margin-bottom: 0.25rem;
}

.paper-title {
    font-size: clamp(1.15em, 0.18vw + 1.05em, 1.32em);
    font-weight: 700;
    line-height: 1.3;
    margin: 1rem 0 0.75rem;
}

.paper-authors {
    font-size: 1em;
    line-height: 1.55;
    margin: 0.5rem 0;
}

.paper-affiliations {
    font-size: 9.5pt;
    line-height: 1.45;
    margin-bottom: 1rem;
}

.paper-footer-meta {
    border-top: 1px solid #ccc;
    margin-top: 1rem;
    padding-top: 0.75rem;
    font-size: 8.5pt;
    color: #444;
    line-height: 1.5;
}

.paper-rule {
    border: none;
    border-top: 1px solid #999;
    margin: 1rem 0;
}

.paper-columns {
    display: grid;
    grid-template-columns: 26% 1fr;
    gap: 2rem;
    margin: 0.5rem 0 1.25rem;
    align-items: start;
}

.paper-section-label {
    font-weight: 700;
    letter-spacing: 0.12em;
    font-size: 8pt;
    margin-bottom: 0.5rem;
}

.paper-keywords {
    font-size: 9.5pt;
    line-height: 1.45;
}

.paper-abstract {
    font-size: 0.9em;
    line-height: 1.5;
    text-align: justify;
}

.paper-body {
    column-count: 2;
    column-gap: clamp(28px, 3vw, 48px);
    text-align: justify;
    margin-top: 0.5rem;
    width: 100%;
}

.paper-body p,
.paper-body li {
    font-size: 1em;
}

.paper-body h2 {
    column-span: all;
    font-size: 1.04em;
    font-weight: 700;
    margin: 1.1rem 0 0.5rem;
    break-after: avoid;
}

.paper-body h3 {
    font-size: 1em;
    font-weight: 700;
    font-style: italic;
    margin: 0.85rem 0 0.35rem;
    break-after: avoid;
}

.paper-body p {
    margin: 0 0 0.55rem;
    text-indent: 0;
}

.paper-body ul,
.paper-body ol {
    margin: 0.25rem 0 0.55rem 1.1rem;
    padding: 0;
}

.paper-body li {
    margin-bottom: 0.25rem;
}

.paper-highlights {
    column-span: all;
    width: 100%;
    border-top: 1px solid #999;
    border-bottom: 1px solid #999;
    border-collapse: collapse;
    margin: 0.75rem 0 1rem;
    font-size: 0.76em;
}

.paper-highlights td {
    padding: 0.45rem 0.5rem;
    vertical-align: top;
    border-bottom: 1px solid #ddd;
}

.paper-highlights tr:last-child td {
    border-bottom: none;
}

.paper-highlights td:first-child {
    width: 28%;
    font-weight: 700;
}

.paper-table-wrap {
    column-span: all;
    margin: 0.75rem 0 1rem;
    break-inside: avoid;
}

.paper-table-title {
    font-weight: 700;
    font-size: 0.76em;
    margin-bottom: 0.15rem;
}

.paper-table-caption {
    font-size: 0.72em;
    margin-bottom: 0.35rem;
}

.paper-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.72em;
}

.paper-table th,
.paper-table td {
    padding: 0.3rem 0.45rem;
    text-align: left;
    vertical-align: top;
    border-top: 1px solid #999;
    border-bottom: 1px solid #999;
}

.paper-table thead th {
    font-weight: 700;
}

.paper-figure {
    column-span: all;
    margin: 0.75rem 0 1rem;
    break-inside: avoid;
}

.paper-figure-details {
    border: none;
    border-radius: 0;
    background: transparent;
    overflow: visible;
}

.paper-figure-summary {
    cursor: pointer;
    list-style: none;
    padding: 0.35rem 0 0.35rem 1.1rem;
    position: relative;
    user-select: none;
    background: transparent;
}

.paper-figure-summary::-webkit-details-marker {
    display: none;
}

.paper-figure-summary::before {
    content: "▸";
    position: absolute;
    left: 0;
    top: 0.42rem;
    font-size: 0.75rem;
    color: #666;
}

.paper-figure-details[open] .paper-figure-summary::before {
    content: "▾";
}

.paper-figure-summary:hover {
    background: transparent;
}

.paper-figure-show-label {
    display: block;
    font-family: "Times New Roman", Times, serif;
    font-size: 0.72em;
    font-weight: 400;
    font-style: italic;
    color: #555;
    margin-bottom: 0.2rem;
}

.paper-figure-caption {
    display: block;
    font-family: "Times New Roman", Times, serif;
    font-size: 0.72em;
    font-weight: 400;
    color: #111;
    text-align: left;
    line-height: 1.4;
}

.paper-figure-caption strong {
    font-weight: 700;
}

.paper-figure-image {
    padding: 0.35rem 0 0.5rem;
    border-top: none;
    text-align: center;
    background: transparent;
}

.paper-figure-image img {
    max-width: 100%;
    height: auto;
}

.paper-figure--half-width .paper-figure-image img {
    width: 50%;
    max-width: 50%;
    display: block;
    margin: 0 auto;
}

.paper-backmatter {
    column-span: all;
    margin-top: 1rem;
    font-size: 0.9em;
}

.paper-backmatter h2 {
    font-size: 0.84em;
    font-style: normal;
    margin: 0.85rem 0 0.35rem;
}

.paper-references {
    column-count: 2;
    column-gap: 28px;
    font-size: 0.82em;
    line-height: 1.4;
    margin-top: 0.75rem;
}

.paper-references h2 {
    column-span: all;
    font-size: 1.04em;
    margin-bottom: 0.5rem;
}

.paper-ref-entry {
    break-inside: avoid;
    margin-bottom: 0.45rem;
    padding-left: 1.2em;
    text-indent: -1.2em;
}

.paper-ref-entry em {
    font-style: italic;
}

.paper-section-block {
    column-span: all;
    break-inside: avoid;
    margin-bottom: 0.35rem;
}

.paper-commentary-group {
    column-span: all;
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
    margin: 0.5rem 0 0.75rem;
}

.paper-anchor {
    color: inherit;
    text-decoration: none;
    background: var(--anchor-highlight, #f3edf2);
    border-bottom: 1.5px dotted var(--anchor-border, #b8a0b0);
    padding: 0 0.1em 0.05em;
    border-radius: 2px;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
    scroll-margin-top: 1rem;
}

.paper-anchor:hover {
    background: color-mix(in srgb, var(--anchor-highlight, #f3edf2) 75%, var(--anchor-accent, #7a6578));
}

.paper-anchor-marker {
    font-family: "Times New Roman", Times, serif;
    font-weight: 600;
    font-size: 0.78em;
    color: var(--anchor-accent, #7a6578);
    margin-left: 0.1em;
    text-decoration: none;
}

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

.paper-commentary-label {
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--commentary-accent, #8a6d82);
}

.paper-commentary-category {
    font-size: 7.5pt;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--commentary-accent, #8a6d82);
    margin-left: auto;
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
    margin: 0 0 0.45rem;
    padding: 0.45rem 0 0;
    border-top: 1px solid var(--commentary-border, #d8c8d2);
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

.paper-commentary-tagline {
    font-size: 7.5pt !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--commentary-accent, #8a6d82) !important;
    margin: 0 !important;
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
