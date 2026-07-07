# [TODO] Persistence

Deferred work related to storing and editing expert commentaries on the paper viewer.

| File | Description |
|---|---|
| [`commentary-persistence-requirement.md`](commentary-persistence-requirement.md) | Requirements for UI-editable section commentaries with JSON persistence |
| [`forum_draft.py`](forum_draft.py) | Draft forum app with Redis / local JSON persistence (reference implementation) |

**Status:** Not implemented. Current commentaries live in `article/commentaries.py` (Python dict, read-only at runtime).
