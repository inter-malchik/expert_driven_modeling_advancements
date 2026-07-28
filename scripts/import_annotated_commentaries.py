"""Import margin notes from expert_guided_pinn_annotated.html into article/commentaries_data/."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.annotated_importer import parse_annotated_html, write_commentary_data

DEFAULT_HTML = Path.home() / "Downloads" / "expert_guided_pinn_annotated.html"


def main() -> None:
    html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_HTML
    if not html_path.exists():
        raise SystemExit(f"Annotated HTML not found: {html_path}")

    commentaries = parse_annotated_html(html_path)
    output = ROOT / "article" / "commentaries_data"
    write_commentary_data(output, commentaries)
    print(f"Imported {len(commentaries)} commentaries into {output}")


if __name__ == "__main__":
    main()
