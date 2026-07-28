"""Section slug helpers shared across paper rendering modules."""

from __future__ import annotations

import re


def slugify_heading(heading: str) -> str:
    slug = heading.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def section_slug(heading: str) -> str:
    return slugify_heading(heading)
