"""Operational helpers for cropping paper figures."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from scripts.figure_crop_data import CROPS, FIGURES_DIR, PAGE_ALIASES, PAGES_DIR


def resolve_page(alias: str) -> Path:
    return PAGES_DIR / PAGE_ALIASES[alias]


def crop_all_figures() -> list[str]:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    saved = []
    for output_name, (page_alias, box) in CROPS.items():
        page_path = resolve_page(page_alias)
        image = Image.open(page_path)
        cropped = image.crop(box)
        output_path = FIGURES_DIR / output_name
        cropped.save(output_path)
        saved.append(f"Saved {output_path} ({cropped.size[0]}x{cropped.size[1]})")
    return saved
