"""Soft color palettes for individual commentaries."""

from __future__ import annotations

import hashlib

from article.palette_utils import palette


def _hue_from_id(commentary_id: str) -> float:
    # Use a stable hash so colors do not change between Python processes.
    digest = hashlib.blake2s(commentary_id.encode("utf-8"), digest_size=4).digest()
    value = int.from_bytes(digest, "big")
    return (value % 3600) / 10.0


def palette_for(commentary_id: str) -> dict[str, str]:
    return palette(_hue_from_id(commentary_id))
