"""Helpers for importing commentaries from the annotated HTML source."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

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


def strip_tags(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def extract_sources(note_body: str) -> list[dict[str, str | None]]:
    sources: list[dict[str, str | None]] = []
    for block in re.findall(r"<ul class=\"sources\">(.*?)</ul>", note_body, re.S):
        for item in re.findall(r"<li class=\"([^\"]*)\">(.*?)</li>", block, re.S):
            status, inner = item
            link = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', inner, re.S)
            if link:
                sources.append(
                    {
                        "text": strip_tags(link.group(2)),
                        "url": link.group(1),
                        "verified": "verified" in status,
                    }
                )
            else:
                sources.append(
                    {
                        "text": strip_tags(inner),
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

    chunks = re.split(
        r"(<p class=\"section-head\">.*?</p>|<p class=\"subloc\">.*?</p>|<section class=\"entry\".*?</section>)",
        main.group(1),
        flags=re.S,
    )
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        head = re.match(r'<p class="section-head">(.*?)</p>', chunk, re.S)
        if head:
            label = strip_tags(head.group(1))
            current_section = SECTION_HEAD_MAP.get(label, current_section)
            continue

        subloc = re.match(r'<p class="subloc">(.*?)</p>', chunk, re.S)
        if subloc:
            label = strip_tags(subloc.group(1))
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

        title = strip_tags(title_match.group(1))
        cat_label = strip_tags(cat_match.group(1))

        body_match = re.search(
            r'<div class="note-body">(.*)</div>\s*</div>\s*</aside>',
            inner,
            re.S,
        )
        body_html = body_match.group(1) if body_match else ""

        filenote_match = re.search(r'<p class="filenote">(.*?)</p>', body_html, re.S)
        filenote = strip_tags(filenote_match.group(1)) if filenote_match else ""

        body_parts: list[str] = []
        for attrs, content in re.findall(r"<p([^>]*)>(.*?)</p>", body_html, re.S):
            if "filenote" in attrs or "tagline" in attrs:
                continue
            text = strip_tags(content)
            if text:
                body_parts.append(text)
        body = "\n\n".join(body_parts)

        tagline_match = re.search(r'<p class="tagline">(.*?)</p>', body_html, re.S)
        tagline = strip_tags(tagline_match.group(1)) if tagline_match else "Literature comparison"

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
                "sources": extract_sources(body_html),
            }
        )

    return commentaries


def _slugify_section(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "misc"


def _normalize_text(value: str) -> str:
    replacements = {
        "\x00": r"\0",
        "\x07": r"\a",
        "\x08": r"\b",
        "\x0b": r"\v",
        "\x0c": r"\f",
    }
    return "".join(replacements.get(char, char) for char in value)


def _escape_data_text(value: str) -> str:
    return _normalize_text(value).replace("\\", "\\\\").replace('"', '\\"')


def _render_data_file(commentary: dict) -> str:
    lines = ["+++"]
    for key in (
        "id",
        "section",
        "category",
        "category_label",
        "marker",
        "title",
        "filenote",
        "tagline",
        "anchor_preview",
    ):
        lines.append(f'{key} = "{_escape_data_text(commentary[key])}"')
    for key in ("proposed_update", "update_details"):
        if key in commentary:
            lines.append(f'{key} = "{_escape_data_text(commentary[key])}"')
    for source in commentary.get("sources", []):
        lines.append("")
        lines.append("[[sources]]")
        lines.append(f'text = "{_escape_data_text(source["text"])}"')
        if source.get("url") is not None:
            lines.append(f'url = "{_escape_data_text(source["url"])}"')
        lines.append(f'verified = {"true" if source.get("verified", False) else "false"}')
    lines.append("+++")
    lines.append(_normalize_text(commentary["body"]))
    lines.append("")
    return "\n".join(lines)


def write_commentary_data(data_root: Path, commentaries: list[dict]) -> None:
    temp_dir = data_root.with_name(f"{data_root.name}_tmp")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir(parents=True, exist_ok=True)

    for commentary in commentaries:
        section_dir = temp_dir / _slugify_section(commentary["section"])
        section_dir.mkdir(parents=True, exist_ok=True)
        file_path = section_dir / f'{commentary["id"]}.md'
        file_path.write_text(_render_data_file(commentary), encoding="utf-8")

    if data_root.exists():
        shutil.rmtree(data_root)
    temp_dir.rename(data_root)
