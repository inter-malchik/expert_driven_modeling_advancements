"""Static crop coordinates and page aliases for figure extraction."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "assets" / "paper" / "pages"
FIGURES_DIR = ROOT / "assets" / "figures"

# Coordinates as (left, top, right, bottom) on 768x1024 page images.
CROPS = {
    "fig1.png": ("page-03.png", (18, 40, 750, 400)),
    "fig2.png": ("page-04.png", (12, 40, 756, 580)),
    "fig3.png": ("page-06.png", (18, 40, 750, 275)),
    "fig4.png": ("page-06.png", (18, 283, 750, 520)),
    "fig5.png": ("page-07.png", (18, 40, 750, 300)),
    "figA6.png": ("page-08.png", (24, 530, 744, 900)),
    "figA7.png": ("page-09.png", (20, 405, 748, 855)),
}

PAGE_ALIASES = {
    "page-01.png": "1-s2.0-S0957417426006433-main-01-c900370f-b6af-43bf-9ae8-22b4904426bf.png",
    "page-02.png": "1-s2.0-S0957417426006433-main-02-80fb03e5-82f1-4f77-8b6f-6030262b7e58.png",
    "page-03.png": "1-s2.0-S0957417426006433-main-03-098692ce-a9bb-44c4-85cd-8d23b7241259.png",
    "page-04.png": "1-s2.0-S0957417426006433-main-04-028739f5-3a1f-4459-b272-b209dafa6a76.png",
    "page-05.png": "1-s2.0-S0957417426006433-main-05-4db55eb3-b55a-4c0b-aa19-caa008ead632.png",
    "page-06.png": "1-s2.0-S0957417426006433-main-06-84905f86-9b81-4314-8c5f-6af180178d1b.png",
    "page-07.png": "1-s2.0-S0957417426006433-main-07-1a4923c7-5d3c-4b4f-a7fb-67b6a6e1ffc5.png",
    "page-08.png": "1-s2.0-S0957417426006433-main-08-158c5152-c8f2-4a29-a6db-7fb6683aa881.png",
    "page-09.png": "1-s2.0-S0957417426006433-main-09-13e19a8a-23f9-43f9-9d9f-5e87d58fd11c.png",
    "page-10.png": "1-s2.0-S0957417426006433-main-10-a3009fc2-f563-46cf-9ff6-51e1ef1bb926.png",
}
