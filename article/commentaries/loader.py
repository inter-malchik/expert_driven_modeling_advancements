"""Load pilot commentary records from Markdown files with TOML front matter."""

from __future__ import annotations

import json
from pathlib import Path

from article.commentaries.schema import Commentary

RELEVANCE_PATH = Path(__file__).resolve().parents[1] / "context" / "commentary_relevance.json"


def _split_front_matter(text: str, path: Path) -> tuple[str, str]:
    if not text.startswith("+++\n"):
        raise ValueError(f"Missing TOML front matter in {path}")
    try:
        _, rest = text.split("+++\n", 1)
        front_matter, body = rest.split("\n+++\n", 1)
    except ValueError as exc:
        raise ValueError(f"Invalid front matter fence in {path}") from exc
    return front_matter, body.strip()


def _parse_string(value: str) -> str:
    if len(value) < 2 or not (value.startswith('"') and value.endswith('"')):
        raise ValueError(f"Expected quoted string, got: {value}")
    inner = value[1:-1]
    return inner.replace('\\"', '"').replace("\\\\", "\\")


def _parse_value(value: str) -> object:
    value = value.strip()
    if value in {"true", "false"}:
        return value == "true"
    return _parse_string(value)


def _parse_front_matter(front_matter: str, path: Path) -> dict[str, object]:
    data: dict[str, object] = {"sources": []}
    current_source: dict[str, object] | None = None

    for raw_line in front_matter.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line == "[[sources]]":
            current_source = {}
            sources = data.setdefault("sources", [])
            assert isinstance(sources, list)
            sources.append(current_source)
            continue
        if "=" not in line:
            raise ValueError(f"Invalid front matter line in {path}: {raw_line}")
        key, value = line.split("=", 1)
        key = key.strip()
        parsed_value = _parse_value(value)
        if current_source is not None:
            current_source[key] = parsed_value
        else:
            data[key] = parsed_value

    return data


def load_commentary_file(path: Path) -> Commentary:
    front_matter, body = _split_front_matter(path.read_text(encoding="utf-8"), path)
    data = _parse_front_matter(front_matter, path)
    data["body"] = body
    data.setdefault("sources", [])
    return data


def _load_relevance_data() -> dict[str, dict[str, int]]:
    if not RELEVANCE_PATH.exists():
        return {}
    raw = json.loads(RELEVANCE_PATH.read_text(encoding="utf-8"))
    items = raw.get("items", {})
    return {str(key): value for key, value in items.items() if isinstance(value, dict)}


def load_external_commentaries(root: Path) -> list[Commentary]:
    if not root.exists():
        return []

    relevance_by_id = _load_relevance_data()
    items = [load_commentary_file(path) for path in sorted(root.rglob("*.md"))]
    for item in items:
        item.update(relevance_by_id.get(item["id"], {}))
    ids = [item["id"] for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate commentary ids in commentaries_data")
    return items
