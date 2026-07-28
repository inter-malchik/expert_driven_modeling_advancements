"""Export commentary records into Markdown data files with TOML front matter."""

from __future__ import annotations

import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = ROOT / "article" / "commentaries_data"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from article.commentaries.loader import load_external_commentaries
from scripts.recover_commentaries_data import main as recover_commentaries_data


def _slugify(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "misc"


def _escape_toml(value: str) -> str:
    return _normalize_text(value).replace("\\", "\\\\").replace('"', '\\"')


def _normalize_text(value: str) -> str:
    replacements = {
        "\x00": r"\0",
        "\x07": r"\a",
        "\x08": r"\b",
        "\x0b": r"\v",
        "\x0c": r"\f",
    }
    return "".join(replacements.get(char, char) for char in value)


def _dump_commentary(item: dict) -> str:
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
        lines.append(f'{key} = "{_escape_toml(item[key])}"')
    for key in ("proposed_update", "update_details"):
        if key in item:
            lines.append(f'{key} = "{_escape_toml(item[key])}"')
    for source in item.get("sources", []):
        lines.append("")
        lines.append("[[sources]]")
        lines.append(f'text = "{_escape_toml(source["text"])}"')
        if source.get("url") is not None:
            lines.append(f'url = "{_escape_toml(source["url"])}"')
        lines.append(f'verified = {"true" if source.get("verified", False) else "false"}')
    lines.append("+++")
    lines.append(_normalize_text(item["body"]))
    lines.append("")
    return "\n".join(lines)


def main(overwrite: bool = False) -> None:
    try:
        commentaries = load_external_commentaries(DATA_ROOT)
    except Exception:
        recover_commentaries_data()
        commentaries = load_external_commentaries(DATA_ROOT)

    created = 0
    skipped = 0
    for item in commentaries:
        section_dir = DATA_ROOT / _slugify(item["section"])
        file_path = section_dir / f'{item["id"]}.md'
        if file_path.exists() and not overwrite:
            skipped += 1
            continue
        section_dir.mkdir(parents=True, exist_ok=True)
        file_path.write_text(_dump_commentary(item), encoding="utf-8")
        created += 1
    print(f"Created {created} commentary data files; skipped {skipped} existing files.")


if __name__ == "__main__":
    main(overwrite="--overwrite" in sys.argv)
