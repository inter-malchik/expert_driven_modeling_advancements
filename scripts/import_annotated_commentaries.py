"""Import margin notes from expert_guided_pinn_annotated.html into article/commentaries.py."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HTML = Path.home() / "Downloads" / "expert_guided_pinn_annotated.html"

SECTION_HEAD_MAP = {
    "1 · Introduction": "1. Introduction",
    "2 · Methodology": "2. Methodology",
    "3 · Results and Discussion": "3. Results and Discussion",
    "4 · Limitations and Future Work": "4. Limitations and Future work",
}

SUBLOC_MAP = {
    "§2.2 Hierarchical Text Classifier": "2.2. Hierarchical text classifier",
    "§2.3 PINN Customizer": "2.3. PINN Customizer",
    "§2.4 Evaluation Approach": "2.4. Evaluation Approach",
    "§3.3 Working with the framework": "3.3. Working with the framework",
}

CATEGORY_MARKERS = {
    "reliability": "¶",
    "architecture": "‡",
    "alignment": "⁂",
    "formalization": "†",
    "evaluation": "§",
    "explanation": "*",
    "epixai": "‖",
}


def _strip_tags(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def _extract_sources(note_body: str) -> list[dict[str, str | None]]:
    sources: list[dict[str, str | None]] = []
    for block in re.findall(r"<ul class=\"sources\">(.*?)</ul>", note_body, re.S):
        for item in re.findall(r"<li class=\"([^\"]*)\">(.*?)</li>", block, re.S):
            status, inner = item
            link = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', inner, re.S)
            if link:
                sources.append(
                    {
                        "text": _strip_tags(link.group(2)),
                        "url": link.group(1),
                        "verified": "verified" in status,
                    }
                )
            else:
                sources.append(
                    {
                        "text": _strip_tags(inner),
                        "url": None,
                        "verified": "verified" in status,
                    }
                )
    return sources


def parse_annotated_html(path: Path) -> list[dict]:
    content = path.read_text(encoding="utf-8")
    main = re.search(r"<main>(.*)</main>", content, re.S)
    if not main:
        raise RuntimeError("Could not find <main> in annotated HTML")

    current_section = "1. Introduction"
    commentaries: list[dict] = []

    for chunk in re.split(r"(<p class=\"section-head\">.*?</p>|<p class=\"subloc\">.*?</p>|<section class=\"entry\".*?</section>)", main.group(1), flags=re.S):
        chunk = chunk.strip()
        if not chunk:
            continue

        head = re.match(r'<p class="section-head">(.*?)</p>', chunk, re.S)
        if head:
            label = _strip_tags(head.group(1))
            current_section = SECTION_HEAD_MAP.get(label, current_section)
            continue

        subloc = re.match(r'<p class="subloc">(.*?)</p>', chunk, re.S)
        if subloc:
            label = _strip_tags(subloc.group(1))
            current_section = SUBLOC_MAP.get(label, current_section)
            continue

        entry = re.match(r'<section class="entry" data-cat="([^"]+)"[^>]*>(.*)</section>', chunk, re.S)
        if not entry:
            continue

        category = entry.group(1)
        inner = entry.group(2)

        note_id_match = re.search(r'<div class="note" id="([^"]+)"', inner)
        if not note_id_match:
            continue
        note_id = note_id_match.group(1)

        title_match = re.search(r'class="note-title">(.*?)</span>', inner, re.S)
        cat_match = re.search(r'class="note-cat">(.*?)</span>', inner, re.S)
        if not title_match or not cat_match:
            continue

        title = _strip_tags(title_match.group(1))
        cat_label = _strip_tags(cat_match.group(1))

        body_match = re.search(
            r'<div class="note-body">(.*)</div>\s*</div>\s*</aside>',
            inner,
            re.S,
        )
        body_html = body_match.group(1) if body_match else ""

        filenote_match = re.search(r'<p class="filenote">(.*?)</p>', body_html, re.S)
        filenote = _strip_tags(filenote_match.group(1)) if filenote_match else ""

        body_parts: list[str] = []
        for attrs, content in re.findall(r"<p([^>]*)>(.*?)</p>", body_html, re.S):
            if "filenote" in attrs or "tagline" in attrs:
                continue
            text = _strip_tags(content)
            if text:
                body_parts.append(text)
        body = "\n\n".join(body_parts)

        tagline_match = re.search(r'<p class="tagline">(.*?)</p>', body_html, re.S)
        tagline = _strip_tags(tagline_match.group(1)) if tagline_match else "Literature comparison"

        anchor_match = re.search(r'data-preview="([^"]*)"', inner)
        anchor_preview = html.unescape(anchor_match.group(1)) if anchor_match else ""

        commentaries.append(
            {
                "id": note_id,
                "section": current_section,
                "category": category,
                "category_label": cat_label,
                "marker": CATEGORY_MARKERS.get(category, "•"),
                "title": title,
                "body": body,
                "filenote": filenote,
                "tagline": tagline,
                "anchor_preview": anchor_preview,
                "sources": _extract_sources(body_html),
            }
        )

    return commentaries


def render_commentaries_py(commentaries: list[dict]) -> str:
    lines = [
        '"""Literature commentaries imported from expert_guided_pinn_annotated.html."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import TypedDict",
        "",
        "",
        "class CommentarySource(TypedDict, total=False):",
        "    text: str",
        "    url: str | None",
        "    verified: bool",
        "",
        "",
        "class Commentary(TypedDict):",
        "    id: str",
        "    section: str",
        "    category: str",
        "    category_label: str",
        "    marker: str",
        "    title: str",
        "    body: str",
        "    filenote: str",
        "    tagline: str",
        "    anchor_preview: str",
        "    sources: list[CommentarySource]",
        "",
        "",
        "COMMENTARIES: list[Commentary] = [",
    ]

    for item in commentaries:
        lines.append("    {")
        for key in (
            "id",
            "section",
            "category",
            "category_label",
            "marker",
            "title",
            "body",
            "filenote",
            "tagline",
            "anchor_preview",
        ):
            lines.append(f"        {key!r}: {item[key]!r},")
        lines.append("        \"sources\": [")
        for source in item["sources"]:
            lines.append("            {")
            lines.append(f"                \"text\": {source['text']!r},")
            lines.append(f"                \"url\": {source['url']!r},")
            lines.append(f"                \"verified\": {source['verified']!r},")
            lines.append("            },")
        lines.append("        ],")
        lines.append("    },")

    lines.append("]")
    lines.append("")
    lines.append("")
    lines.append("def commentaries_by_section() -> dict[str, list[Commentary]]:")
    lines.append("    grouped: dict[str, list[Commentary]] = {}")
    lines.append("    for commentary in COMMENTARIES:")
    lines.append("        grouped.setdefault(commentary[\"section\"], []).append(commentary)")
    lines.append("    return grouped")
    lines.append("")
    lines.append("")
    lines.append("ANNOTATED_SECTIONS: list[str] = list(commentaries_by_section().keys())")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_HTML
    if not html_path.exists():
        raise SystemExit(f"Annotated HTML not found: {html_path}")

    commentaries = parse_annotated_html(html_path)
    output = ROOT / "article" / "commentaries.py"
    output.write_text(render_commentaries_py(commentaries), encoding="utf-8")
    print(f"Imported {len(commentaries)} commentaries into {output}")


if __name__ == "__main__":
    main()
