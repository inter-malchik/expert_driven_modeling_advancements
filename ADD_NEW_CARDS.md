# Как добавить новую карточку (commentary + analysis-страница)

Гайд описывает, что именно нужно сделать, чтобы в приложении появилась новая карточка-комментарий рядом с текстом статьи и связанная с ней полноценная страница сравнения (`?analysis=<slug>`).

Каждая карточка состоит из двух связанных сущностей:

1. **Commentary** — блок в боковой панели и в теле статьи (`<details>` с маркером, категорией, заголовком, кратким текстом).
2. **Analysis page** — отдельный markdown-файл в `article/analysis/`, открываемый по ссылке *«Read full comparison»*.

Связка между ними — поле `filenote` у commentary: его первая часть до `" — "` должна совпадать с именем markdown-файла в `article/analysis/` (см. `analysis_slug_from_filenote` в `article/analysis_index.py:16`).

---

## 1. Список файлов, которые нужно тронуть

| Файл | Что менять | Обязательно? |
|---|---|---|
| `article/analysis/NN_<slug>.md` | Создать новый файл со сравнением | Да |
| `article/commentaries.py` | Добавить объект в список `COMMENTARIES` | Да |
| `article/commentary_anchors.py` | Добавить запись в `ANCHOR_TEXTS` (точный фрагмент из `body_html.py`) | Да, если нужно подсветить якорный фрагмент в тексте статьи |
| `article/commentary_colors.py` | Расширить диапазон `COMMENTARY_IDS`, если добавляется 16-я и последующие | Да, при `n16+` |
| `article/commentary_links.py` | Добавить URL источника в `SOURCE_URLS`, если он не задан явно и не парсится из текста | Опционально |
| `article/sections.py` | Добавить цвет для новой `category` в `CATEGORY_COLORS` | Опционально (только если вводится новая категория) |
| `article/body_html.py` | Убедиться, что заголовок раздела `<h2>` / `<h3>` из поля `section` уже присутствует | Обязательно, иначе группа комментариев не будет вставлена |

Никаких изменений в `streamlit_app.py`, `analysis_view.py` или `analysis_index.py` для новой карточки не требуется — они уже подхватывают всё динамически.

---

## 2. Шаг 1 — создать analysis-файл

Путь: `article/analysis/NN_<slug>.md`, где `NN` — следующий свободный номер (сейчас существуют `01…15`).

Требования:

* Имя файла без пробелов, только буквы/цифры/подчёркивания/дефисы. Это же имя (без `.md`) будет использоваться как параметр `?analysis=<slug>` в URL.
* Первый заметный заголовок (первая строка вида `# …` / `## …` / `### …` / `#### …`) берётся как заголовок для `load_analysis` (`article/analysis_index.py:36`), поэтому он должен быть осмысленным.
* Можно **не** вставлять блок *«How to read this comparison»* — он будет автоматически добавлен функцией `prepare_comparison_markdown` (`article/comparison_prose.py:44`), если его нет в начале файла.
* Функция `clean_comparison_prose` (`article/comparison_prose.py:33`) автоматически:
  * убирает эпистемические теги вида `(Comparative inference…)`, `(Author-stated…)`, `(Empirically shown…)`, `(Speculative extension…)`;
  * убирает `**Self-report:**` и всё после него до конца файла;
  * переименовывает `## Direction …` → `## Proposed direction …`.
* Стиль верстки в приложении задан через `ANALYSIS_CSS` (`article/styles.py`) — доступны стандартные элементы markdown (заголовки, таблицы, цитаты, код), плюс блок `<div class="analysis-shell">`, оборачивающий всё содержимое.

Минимальный скелет:

```markdown
#### comparison with <краткое имя источника>

Paper A (Gindullina et al., …) — …

Paper B (<автор>, «<название>») — …

---

## 1. <тезис>

…

## Proposed direction

…
```

---

## 3. Шаг 2 — зарегистрировать commentary

Файл: `article/commentaries.py`. Добавить новый словарь в конец списка `COMMENTARIES` (соблюдая порядок нумерации `id`).

Все поля обязательные — тип описан в `Commentary` (`article/commentaries.py:14`):

| Поле | Значение | Заметки |
|---|---|---|
| `id` | `"n<N>"` (следующий за существующим `n15`) | Также используется как: якорь HTML (`#commentary-n16`), id подсвеченного фрагмента (`#anchor-n16`), ключ в `ANCHOR_TEXTS`, ключ палитры |
| `section` | Название раздела статьи | **Должно совпадать** с текстом заголовка `<h2>` или `<h3>` в `body_html.py`, иначе `_inject_commentaries` (`article/sections.py:193`) не вставит блок |
| `category` | Строковый ID категории | Используется в CSS-классах; известные значения: `reliability`, `architecture`, `alignment`, `formalization`, `evaluation`, `explanation`, `epixai` (см. `CATEGORY_COLORS`, `article/sections.py:111`) |
| `category_label` | Человекочитаемая метка категории | Показывается в шапке карточки |
| `marker` | Один типографский символ (`¶`, `‖`, `‡`, `§`, `*`, `†`, `⁂` и т. п.) | Показывается перед заголовком; также выводится как `<sup>` в тексте статьи над подсвеченным фрагментом |
| `title` | Короткий заголовок карточки | Отображается жирным в `<summary>` |
| `body` | Основной текст карточки | Экранируется через `html.escape`, двойные переносы строк превращаются в `<p>` |
| `filenote` | Имя markdown-файла в формате `NN_slug.md` или `NN_slug.md — комментарий` | Функция `analysis_slug_from_filenote` (`article/analysis_index.py:16`) отрезает всё после `" — "` и `.md`. Ссылка *«Read full comparison»* появляется, только если файл существует |
| `tagline` | Мини-подпись под телом | Обычно `"Literature comparison"` или `"Literature comparison (proposed extension)"` |
| `anchor_preview` | Одна короткая фраза | Показывается в цитатной рамке; если пусто — блок «Linked passage in text» тоже пропускается |
| `sources` | Список `CommentarySource` | Минимум один элемент вида `{"text": …, "url": …|None, "verified": bool}` |

Пример шаблона:

```python
{
    "id": "n16",
    "section": "3.3. Working with the framework",
    "category": "reliability",
    "category_label": "LLM Reliability",
    "marker": "◊",
    "title": "…",
    "body": "…",
    "filenote": "16_myauthor_2026_topic.md",
    "tagline": "Literature comparison",
    "anchor_preview": "…",
    "sources": [
        {
            "text": "Author (2026), Title — arXiv:2601.12345",
            "url": "https://arxiv.org/abs/2601.12345",
            "verified": True,
        },
    ],
},
```

---

## 4. Шаг 3 — привязать якорь в тексте статьи (опционально, но обычно нужен)

Файл: `article/commentary_anchors.py`.

Добавить запись в словарь `ANCHOR_TEXTS`:

```python
"n16": (
    "точный фрагмент, встречающийся в article/body_html.py"
),
```

Правила:

* Строка должна быть **подстрокой** HTML тела в `body_html.py` (учитываются варианты с типографскими кавычками/апострофами; см. `_normalize_apostrophes`, `article/anchor_highlights.py:13`).
* Если совпадение не найдено — приложение просто не подсветит фрагмент, но карточка всё равно появится в панели раздела.
* Разрешено включать HTML-теги (например, `<strong>...</strong>`), если они реально стоят в этом месте `body_html.py`.

Обёртка со стилями и `id="anchor-n16"` создаётся автоматически в `inject_anchor_highlights` (`article/anchor_highlights.py:44`).

---

## 5. Шаг 4 — палитра

`article/commentary_colors.py` перебирает `COMMENTARY_IDS = [f"n{i}" for i in range(1, 16)]` и раскладывает оттенки по кругу. Пока карточек 15, диапазон `1..16` (не включая 16) заполнен полностью.

Если добавляете 16-ю карточку и далее — увеличьте верхнюю границу диапазона:

```python
COMMENTARY_IDS = [f"n{i}" for i in range(1, 17)]  # для n16
```

Иначе `palette_for("n16")` вернёт fallback (розовый оттенок `hsl(330, …)`), и карточка будет визуально «выбиваться».

---

## 6. Шаг 5 — URL источника (если он не тривиален)

`article/commentary_links.py` авторезолвит ссылки следующим образом (см. `resolve_source_url`, строка 33):

1. Если у источника задан `url` — используется он.
2. Иначе ищется точное совпадение текста в `SOURCE_URLS`.
3. Иначе ищется `arXiv:NNNN.NNNNN` или `doi:XXX` прямо в тексте.
4. Иначе ссылки нет — карточка помечает источник как *pending*.

Правило:

* Если можете дать явный URL в `sources[i].url` — этого достаточно.
* Если хотите держать «канонические» URL централизованно (как для большинства текущих 15 карточек) — добавьте пару `text -> url` в `SOURCE_URLS`.

---

## 7. Шаг 6 — новая категория (опционально)

Если поле `category` в новой карточке — одно из существующих (`reliability`, `architecture`, `alignment`, `formalization`, `evaluation`, `explanation`, `epixai`) — делать ничего не нужно.

Если вводится новая категория:

1. Добавить цвет в `CATEGORY_COLORS` в `article/sections.py:111`.
2. Убедиться, что нигде в CSS (`article/styles.py`) нет жёстко захардкоженного списка категорий, ломающегося от неизвестного значения.

---

## 8. Шаг 7 — заголовок раздела в теле статьи

`_inject_commentaries` (`article/sections.py:193`) ищет в HTML тела ровно такой тег:

```html
<h2>{section}</h2>
```

или

```html
<h3>{section}</h3>
```

где `{section}` — точное значение поля `section` из commentary.

Проверьте `article/body_html.py`: если такой заголовок уже есть — всё готово. Если нет (например, вы делаете карточку для нового подраздела) — заголовок нужно предварительно добавить в HTML (или пересобрать `body_html.py` из markdown-источника командой `python scripts/build_body_html.py`, см. `article/source.md`).

---

## 9. Как это связывается в URL

* Ссылка *«Read full comparison»* формируется в `analysis_url` (`article/analysis_index.py:25`) как `/?analysis=<slug>&from=<commentary_id>`.
* `slug` — имя markdown-файла без `.md` (то есть `NN_<slug>` целиком).
* `streamlit_app.py:58` читает query-параметр `analysis` (алиас — `slug`) и параметр `from`, после чего `render_analysis` (`article/analysis_view.py:22`) грузит нужный файл и добавляет ссылку «← Back to commentary».
* Ссылка «Linked passage in text» ведёт на `#anchor-n<N>`, а якорь на карточке — `#commentary-n<N>`; оба id проставляются автоматически из `id` карточки.

---

## 10. Быстрая проверка

1. Запустить приложение: `streamlit run streamlit_app.py` (см. README, раздел «Запуск»).
2. В сайдбаре в разделе `section` должна появиться новая карточка `<marker> <title>`.
3. Кликнув по маркеру рядом с ней, попасть на подсвеченный фрагмент в тексте.
4. Развернуть карточку (`<details>`), нажать *«Read full comparison»* — открывается страница `?analysis=NN_<slug>&from=n<N>` с содержимым нового markdown-файла.
5. На странице сравнения работает *«← Back to paper»* и *«← Back to commentary»*, а под навигацией — блок *«Original article(s)»* со ссылкой на источник.

Если что-то из этого не работает — почти всегда причина в одном из трёх мест:

* Несовпадение `filenote` и имени файла → ссылка *«Read full comparison»* не появляется.
* Несовпадение `section` и заголовка в `body_html.py` → блок с карточкой не появляется в теле статьи (но сама карточка остаётся видна в сайдбаре).
* `ANCHOR_TEXTS[id]` — не подстрока `body_html.py` → фрагмент не подсвечен, но карточка на месте.
