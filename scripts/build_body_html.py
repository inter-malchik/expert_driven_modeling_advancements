"""Generate article/body_html.py from legacy markdown content."""

from __future__ import annotations

from scripts.article_builder.io import (
    extract_article_content,
    split_body_and_references,
    write_generated_modules,
)
from scripts.article_builder.markdown import convert_markdown_block


def main() -> None:
    body_html = convert_markdown_block(extract_article_content())
    body_part, refs_part = split_body_and_references(body_html)
    body_output, refs_output = write_generated_modules(body_part, refs_part)
    print(f"Wrote {body_output} ({len(body_part)} chars)")
    print(f"Wrote {refs_output} ({len(refs_part)} chars)")


if __name__ == "__main__":
    main()
