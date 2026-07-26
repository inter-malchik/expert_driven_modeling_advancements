"""Soft color palettes for individual commentaries."""

from __future__ import annotations

COMMENTARY_IDS = [f"n{i}" for i in range(1, 49)]


def _palette(hue: float) -> dict[str, str]:
    return {
        "accent": f"hsl({hue:.0f}, 30%, 40%)",
        "bg": f"hsl({hue:.0f}, 38%, 95%)",
        "border": f"hsl({hue:.0f}, 28%, 78%)",
        "highlight": f"hsl({hue:.0f}, 42%, 90%)",
        "highlight_border": f"hsl({hue:.0f}, 32%, 62%)",
    }


COMMENTARY_PALETTES: dict[str, dict[str, str]] = {
    commentary_id: _palette((index * 360 / len(COMMENTARY_IDS)) + 8)
    for index, commentary_id in enumerate(COMMENTARY_IDS)
}


def palette_for(commentary_id: str) -> dict[str, str]:
    return COMMENTARY_PALETTES.get(commentary_id, _palette(330))
