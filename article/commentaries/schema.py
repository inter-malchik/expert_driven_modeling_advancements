"""Shared types for commentary records."""

from __future__ import annotations

from typing import NotRequired, TypedDict


class CommentarySource(TypedDict, total=False):
    text: str
    url: str | None
    verified: bool


class Commentary(TypedDict):
    id: str
    section: str
    category: str
    category_label: str
    marker: str
    title: str
    body: str
    filenote: str
    tagline: str
    anchor_preview: str
    sources: list[CommentarySource]
    proposed_update: NotRequired[str]
    update_details: NotRequired[str]
    relevance_score: NotRequired[int]
    relevance_method_fit: NotRequired[int]
    relevance_transferability: NotRequired[int]
    relevance_actionability: NotRequired[int]
    relevance_expansion_value: NotRequired[int]
