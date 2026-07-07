# Requirement: Editable Section Commentaries with Persistence

## Context

The paper viewer (`streamlit_app.py`) can show expert commentaries above annotated sections (e.g. *"Please more details about complex system"* on **1. Introduction**). Today these are defined statically in `article/commentaries.py` and require a code change to add or edit.

A draft forum with persistence patterns already exists in [`forum_draft.py`](forum_draft.py) (Redis with local JSON fallback). This requirement describes extending the commentary feature using similar ideas, without implementing it yet.

## Goal

Allow reviewers to add, edit, and remove section-level commentaries from the Streamlit UI, with changes persisted across app restarts.

## Functional requirements

### FR-1 Section targeting

- Each commentary is bound to a **section heading** that matches an `<h2>` or `<h3>` title in `article/body_html.py` (e.g. `"1. Introduction"`, `"2.3. PINN Customizer"`).
- The UI must offer a picker or autocomplete of valid section headings so reviewers cannot attach comments to non-existent sections.
- Commentaries render in the same position as today: a full-width **Expert commentary** box immediately above the target section.

### FR-2 CRUD in the UI

- **Create:** add a commentary for a selected section (one commentary per section; adding again updates the existing entry).
- **Read:** load and display all saved commentaries when "Show expert commentaries" is enabled.
- **Update:** edit commentary text in the sidebar or a dedicated review panel.
- **Delete:** remove a commentary for a section.

### FR-3 Persistence

- Primary store: **JSON file** (e.g. `data/section_commentaries.json`).
- Schema (minimum):

```json
{
  "commentaries": {
    "1. Introduction": {
      "text": "Please more details about complex system.",
      "author": "Reviewer name",
      "updated_at": "2026-07-07T16:00:00"
    }
  }
}
```

- On startup: load JSON if present; otherwise fall back to defaults from `article/commentaries.py` (or an empty dict).
- On save: write JSON atomically (write temp file, then rename).
- Optional later: Redis backend using the same pattern as `forum_draft.py` (`REDIS_URL` in Streamlit secrets) for multi-user / deployed environments.

### FR-4 Review workflow

- Sidebar **Review** panel (already exists for toggle + section links) should grow to include:
  - list of annotated sections with edit/delete actions;
  - form to add a new section commentary;
  - optional reviewer name (session or profile field).
- Toggle **Show expert commentaries** continues to control visibility without deleting stored data.

### FR-5 Permissions (minimal v1)

- No auth required for v1 (same as `forum_draft.py`).
- Document that production deployments should restrict write access (e.g. `?review=true` + deployment-level protection, or auth in a later iteration).

## Non-functional requirements

- **NFR-1:** No breaking change to current read-only mode — app works with only `article/commentaries.py` if JSON is missing.
- **NFR-2:** Keep rendering logic in `article/sections.py`; persistence logic in a separate module (e.g. `article/commentary_store.py`).
- **NFR-3:** JSON file path configurable via env var or Streamlit secrets (default: `data/section_commentaries.json`).
- **NFR-4:** Reuse caching patterns from `forum_draft.py` where appropriate; invalidate cache after writes.

## Out of scope (v1)

- Threaded replies per commentary.
- Inline comments on arbitrary paragraphs (only section-level).
- Real-time sync between multiple concurrent editors.
- Version history / audit log.

## Acceptance criteria

1. Reviewer can add a commentary on **1. Introduction** from the UI without editing Python source.
2. After restarting the app, the commentary still appears above **1. Introduction**.
3. Reviewer can edit and delete that commentary from the UI; changes persist in JSON.
4. With commentaries toggle off, stored data remains but boxes are hidden.
5. `article/commentaries.py` remains a valid fallback seed for default commentaries.

## Implementation notes (for future work)

- Extract `load_commentaries()` / `save_commentaries()` mirroring `forum_draft.py`.
- Replace direct import of `SECTION_COMMENTARIES` in `streamlit_app.py` with store-backed loading.
- Add `data/.gitkeep` and document whether `section_commentaries.json` is gitignored (likely yes for local review data).
- Run with: `streamlit run streamlit_app.py` (main app); `streamlit run "[TODO] persistence/forum_draft.py"` for the standalone forum prototype.

## References

- Current commentary injection: `article/sections.py` → `_inject_commentaries()`
- Current static data: `article/commentaries.py`
- Persistence prototype: [`forum_draft.py`](forum_draft.py)
