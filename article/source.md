# Article markdown source

The rendered article HTML lives in:

- `article/body_html.py` — main body (auto-generated)
- `article/references_html.py` — bibliography (auto-generated)

To rebuild HTML from markdown, restore the full article markdown here and run:

```bash
python scripts/build_body_html.py
```

To refresh figure crops from PDF page images:

```bash
python scripts/crop_figures.py
```
