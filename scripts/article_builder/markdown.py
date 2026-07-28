"""Markdown-to-HTML conversion for the legacy paper source."""

from __future__ import annotations

import re

from scripts.article_builder.constants import (
    HIGHLIGHTS_TABLE,
    TABLE1,
    TABLE_A2,
    figure_html,
)


def inline_format(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def convert_markdown_block(text: str) -> str:
    lines = text.strip().splitlines()
    html_parts: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_ordered = False
    in_blockquote = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            html_parts.append(f"<p>{inline_format(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items, list_ordered
        if list_items:
            tag = "ol" if list_ordered else "ul"
            items = "".join(f"<li>{inline_format(item)}</li>" for item in list_items)
            html_parts.append(f"<{tag}>{items}</{tag}>")
            list_items = []
            list_ordered = False

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            flush_list()
            in_blockquote = False
            i += 1
            continue

        if stripped.startswith("> "):
            in_blockquote = True
            i += 1
            continue

        if in_blockquote:
            i += 1
            continue

        if stripped == "---":
            flush_paragraph()
            flush_list()
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            flush_list()
            html_parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            flush_list()
            html_parts.append(f"<h3>{inline_format(stripped[4:])}</h3>")
            i += 1
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            flush_paragraph()
            flush_list()
            if stripped.startswith("| |"):
                html_parts.append(HIGHLIGHTS_TABLE)
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                i += 1
            continue

        if stripped == "**Table 1**":
            flush_paragraph()
            flush_list()
            html_parts.append(TABLE1)
            i += 1
            while i < len(lines) and (
                lines[i].strip().startswith("Hierarchical")
                or lines[i].strip().startswith("|")
            ):
                i += 1
            continue

        if stripped == "**Table A.2**":
            flush_paragraph()
            flush_list()
            html_parts.append(TABLE_A2)
            i += 1
            while i < len(lines) and (
                lines[i].strip().startswith("Rules for")
                or lines[i].strip().startswith("|")
            ):
                i += 1
            continue

        if stripped == "**Fig. 1.** Schematic of Expert-Guided PINN. The expert enters a comment that will help them correctly structure the conversational agent. Next, a class and subclass are defined for the comment, for which rules for generating modifications to the current loss function will be defined. After generating the loss function and checking its compilability, the PINN training process begins. The user then receives a new prediction, which they can then decide whether it satisfies their comment or not.":
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG1"))
            i += 1
            continue

        if stripped.startswith("**Fig. 2.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG2"))
            i += 1
            continue

        if stripped.startswith("**Fig. 3.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG3"))
            i += 1
            continue

        if stripped.startswith("**Fig. 4.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG4"))
            i += 1
            continue

        if stripped.startswith("**Fig. 5.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIG5"))
            i += 1
            continue

        if stripped.startswith("**Fig. A.6.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIGA6"))
            i += 1
            continue

        if stripped.startswith("**Fig. A.7.**"):
            flush_paragraph()
            flush_list()
            html_parts.append(figure_html("FIGA7"))
            i += 1
            continue

        if stripped.startswith("**CRediT authorship contribution statement**"):
            flush_paragraph()
            flush_list()
            html_parts.append('<div class="paper-backmatter">')
            html_parts.append("<p><strong>CRediT authorship contribution statement</strong></p>")
            i += 1
            continue

        if stripped == "## Appendix A. Classification of expert comments":
            flush_paragraph()
            flush_list()
            html_parts.append("</div>")
            html_parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
            i += 1
            continue

        if stripped.startswith("## References"):
            flush_paragraph()
            flush_list()
            break

        ordered_match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        bullet_match = re.match(r"^[\*\-]\s+(.*)$", stripped)

        if ordered_match:
            flush_paragraph()
            if not list_ordered and list_items:
                flush_list()
            list_ordered = True
            list_items.append(ordered_match.group(2))
            i += 1
            continue

        if bullet_match:
            flush_paragraph()
            if list_ordered and list_items:
                flush_list()
            list_items.append(bullet_match.group(1))
            i += 1
            continue

        flush_list()
        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    flush_list()
    return "\n".join(html_parts)
