"""Palette generation helpers for commentary theming."""

from __future__ import annotations


def palette(hue: float) -> dict[str, str]:
    return {
        "accent": f"hsl({hue:.0f}, 25%, 55%)",
        "bg": f"hsl({hue:.0f}, 25%, 97%)",
        "border": f"hsl({hue:.0f}, 20%, 85%)",
        "highlight": f"hsl({hue:.0f}, 30%, 93%)",
        "highlight_border": f"hsl({hue:.0f}, 25%, 75%)",
    }
