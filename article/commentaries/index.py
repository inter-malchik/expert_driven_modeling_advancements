"""Indexes and loading helpers for commentary records."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from functools import lru_cache
from pathlib import Path
from typing import Any

from article.commentaries.loader import load_external_commentaries
from article.commentaries.schema import Commentary

DATA_ROOT = Path(__file__).resolve().parents[1] / "commentaries_data"


@lru_cache(maxsize=1)
def _load_external_commentaries() -> tuple[Commentary, ...]:
    return tuple(load_external_commentaries(DATA_ROOT))


def _safe_external_commentaries() -> list[Commentary]:
    try:
        return list(_load_external_commentaries())
    except Exception:
        # Do not crash module import when one external card is malformed.
        return []


class LazyCommentaryList(Sequence[Commentary]):
    def _items(self) -> list[Commentary]:
        return _safe_external_commentaries()

    def __getitem__(self, index: int | slice) -> Commentary | list[Commentary]:
        return self._items()[index]

    def __len__(self) -> int:
        return len(self._items())

    def __iter__(self) -> Iterator[Commentary]:
        return iter(self._items())

    def __bool__(self) -> bool:
        return bool(self._items())

    def __repr__(self) -> str:
        return repr(self._items())

    def __eq__(self, other: Any) -> bool:
        return self._items() == other


EXTERNAL_COMMENTARIES: Sequence[Commentary] = LazyCommentaryList()
BASE_COMMENTARIES: list[Commentary] = []
COMMENTARIES: Sequence[Commentary] = EXTERNAL_COMMENTARIES


def commentaries_by_section() -> dict[str, list[Commentary]]:
    grouped: dict[str, list[Commentary]] = {}
    for commentary in _safe_external_commentaries():
        grouped.setdefault(commentary["section"], []).append(commentary)
    return grouped


def commentaries_by_category() -> dict[str, list[Commentary]]:
    grouped: dict[str, list[Commentary]] = {}
    for commentary in _safe_external_commentaries():
        grouped.setdefault(commentary["category"], []).append(commentary)
    return grouped


def commentary_by_id(commentary_id: str) -> Commentary | None:
    for commentary in _safe_external_commentaries():
        if commentary["id"] == commentary_id:
            return commentary
    return None


ANNOTATED_SECTIONS: list[str] = list(commentaries_by_section())
