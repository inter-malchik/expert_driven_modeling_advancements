"""Extract draft data for new commentary cards from the analysis files."""

from __future__ import annotations

from scripts.card_draft_extractors import dump_card_drafts_json


def main() -> None:
    print(dump_card_drafts_json())


if __name__ == "__main__":
    main()
