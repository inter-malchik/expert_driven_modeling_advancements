# CARDS_REORG_STATUS.md — полная передача контекста

Файл-хэндовер: всё, что нужно, чтобы другой агент продолжил работу без потери информации. Основная задача — расширить набор literature-карточек в приложении Expert-Guided PINN с 15 до 48 (15 оригиналов + 33 новых сравнения), встроив каждую в тело статьи как полноценный `<details>`-блок в сайдбаре, с якорем в тексте и связанной страницей `?analysis=<slug>`.

Смежные документы:
- [`ADD_NEW_CARDS.md`](./ADD_NEW_CARDS.md) — инструкция «как добавить карточку» (уже отредактирована пользователем, вводит категории `optimization`/`pathology` и маркеры `∆ Σ Ω ⊗`; см. п. «Что осталось» ниже — две мелкие правки).
- [`article/context/dinara_comprehensive_review.md`](./article/context/dinara_comprehensive_review.md) — обзор от эксперта, задающий приоритеты (что «ядро», что «второстепенное») и рамку рерайта карточек.
- Утверждённый план: `/Users/inter-malchik/.claude/plans/ai-chat-attachment-6895312849033851907-keen-aurora.md`.

---

## 1. Устройство приложения (минимум, чтобы не блуждать)

- `streamlit_app.py` — точка входа; если в URL есть `?analysis=<slug>`, рендерит страницу сравнения через `article/analysis_view.py`, иначе — статью (`render_header`/`render_body`/`render_references` из `article/sections.py`).
- `article/commentaries.py:COMMENTARIES` — **источник правды по карточкам**. Список dict-ов типа `Commentary` (см. TypedDict в `article/commentaries.py:14`).
- `article/commentary_anchors.py:ANCHOR_TEXTS` — карта `commentary_id → точный фрагмент в body_html.py`, который карточка комментирует. Подсветка и `<sup>marker</sup>` встраиваются функцией `inject_anchor_highlights` (`article/anchor_highlights.py:44`).
- `article/commentary_colors.py` — палитра, генерируется по кругу HSL для `COMMENTARY_IDS`.
- `article/commentary_links.py:SOURCE_URLS` — централизованный маппинг «текст источника → URL», используется только если у источника не задан явный `url`.
- `article/sections.py:CATEGORY_COLORS` (строка 111) — цвета категорий.
- `article/analysis/<slug>.md` — сравнения (48 файлов). Каждое — короткий (10-25 КБ) markdown в жанре «Paper A vs Paper B».
- `article/body_html.py:BODY_HTML` — HTML-тело статьи (генерируется). В нём есть `<h2>`/`<h3>`, к которым «пришпиливаются» карточки по совпадению строки `section` в commentary с текстом заголовка.

Связка commentary → analysis-файл: поле `filenote` в commentary; функция `analysis_slug_from_filenote` (`article/analysis_index.py:16`) отрезает всё после `" — "` и `.md`.

---

## 2. Что уже сделано

- **Удалены 28 «сырых» исходников** (`article/analysis/NN_YYYY <Title>.md`). Полный текст статей B в репозитории теперь не хранится — только `Paper B — live link` в заголовке каждого сравнения.
- **Сняты префиксы `NN_`** с 48 сравнений. Файлы теперь `<author>_<year>_<topic>.md` без номера.
- **`article/comparison_prose.py`**: добавлен `_SRC_LINK_LINE` (regex, отсекающий строку `> **Source in \`src/\`:**` при рендере). Это компенсирует битую ссылку внутри новых сравнений, которая осталась в файлах на диске, — файлы сами не редактируем.
- **`article/commentary_colors.py`**: `COMMENTARY_IDS = [f"n{i}" for i in range(1, 49)]`. Знаменатель `_palette` переведён на `len(COMMENTARY_IDS)` — палитра автоматически подстраивается под любое N.
- **`article/commentaries.py`**: у **всех 15 существующих** записей поле `filenote` очищено от `NN_` (проверено `grep`, коллизий нет).
- **`scripts/extract_card_drafts.py`**: скрипт-извлекатель. Читает 33 новых `.md`, пытается сматчить *первую* Гиндуллинскую цитату (`> **Quote (Gindullina et al.):** *"..."*`), а если она не совпадает как substring с `body_html.py` — перебирает все цитаты в файле и берёт первую, которая совпадает (с нормализацией «ёлочек»/апострофов). **Все 33 якоря найдены** — данные в `/tmp/card_drafts.json` (JSON list из 33 записей: `slug`, `paper_b_url`, `paper_b_label`, `paper_b_paren`, `thesis`, `anchor_text`, `inferred_section`, `all_quote_count`, `matched_quote_index`).
- **Обзор эксперта** сохранён в `article/context/dinara_comprehensive_review.md`.
- **`ADD_NEW_CARDS.md`** уже частично обновлён пользователем: введены категории `optimization`, `pathology` и маркеры `∆ Σ Ω ⊗`; в шаблоне-примере теперь Wei/DANTE.

---

## 3. Что осталось

### 3.1. #12 — Распределить категории, маркеры и разделы для 33 новых карточек

Задача — заполнить таблицу «slug → id, section, category, category_label, marker». Соответствие *category → marker* уже фиксировано в существующих 15 карточках:

| category | category_label | marker |
|---|---|---|
| `reliability` | LLM Reliability | `¶` |
| `architecture` | Agent Architecture | `‡` |
| `alignment` | Alignment / RLHF | `⁂` |
| `formalization` | Formalization & Ontology | `†` |
| `evaluation` | Evaluation Epistemics | `§` |
| `explanation` | Explanation Theory | `*` |
| `epixai` | Epi-XAI Pipeline | `‖` |

Новые (объявлены пользователем в `ADD_NEW_CARDS.md`):

| category | category_label | marker | подсказано ролью в обзоре |
|---|---|---|---|
| `optimization` | Active Optimization | `∆` | DANTE-кластер: Wei, Kerschke, Malek, eDSC, TRM (частично) |
| `pathology` | Loss Landscape Pathology | `Σ` (или `Ω`/`⊗`) | Malan-2021, Daza, Malan-gradient, Clark, Abell, weakEmergence, unpredictability |

Есть маркеры `Ω` и `⊗` — они пока не заняты; можно ввести ещё 1–2 категории при необходимости (например, `argumentation` для Amgoud/Cayrol/Dubois/Merhej/Potyka/Bisquert/Arioua — это плотный кластер).

**Список ядерных карточек по обзору (Roadmap Q1)** — им нужен более развёрнутый `body`:

| slug | роль в обзоре | предлагаемая category |
|---|---|---|
| `wei_2024_dante_active_optimization` | Roadmap step 2 (DANTE, surrogate pre-screen) | `optimization` |
| `zhang_2026_trm_complex_reasoning` | Roadmap step 1 (TRM/Bradley-Terry reward model) | `evaluation` или `alignment` |
| `eftimov_2019_edsc_statistical_comparison` | Блок 2.1 (Anderson-Darling + Bonferroni) | `evaluation` |
| `malan_2021_landscape_analysis_survey` | Блок 2.2 (loss-landscape pathology) | `pathology` |
| `daza_2016_basin_entropy` | Блок 2.2 (фрактальные бассейны аттракторов) | `pathology` |
| `noy_2001_ontology_development_101` | Блок 2.3 (formal ontology, competency Qs) | `formalization` |
| `halpern_pearl_2005_causes_and_explanations` | Кластер 12 (actual cause) | `explanation` |
| `miller_2020_contrastive_explanation` | Кластер 12 (contrastive foil) | `explanation` |
| `hidalgo_2018_glucose_grammatical_evolution` | Roadmap step 3 (DSL/grammar) | `formalization` |
| `malek_2009_multi_agent_collaboration` | Кластер 14 (MAS для Future Work) | `architecture` |
| `epstein_2008_why_model` | Roadmap step 4 (риторический фрейминг) | `evaluation` (или `explanation`) |

**Полная таблица «slug → inferred_section»** (из `/tmp/card_drafts.json`; в этом виде можно принять напрямую, но обзор может требовать сдвига некоторых карточек):

| slug | inferred_section |
|---|---|
| abell_landscape_features_under_noise | 2.3. PINN Customizer |
| amgoud_2015_undercutting | 2.2. Hierarchical text classifier |
| arioua_2015_explanatory_dialogues | 4. Limitations and Future work |
| bisquert_2015_dual_process_argument | 2.4. Evaluation Approach |
| cayrol_2015_bipolar_change | 2.1. Conversational Agent |
| clark_deconstructing_big_valley | 2.3. PINN Customizer |
| daza_2016_basin_entropy | 3.4. Framework performance |
| dubois_2015_possibilistic_inconsistency | 4. Limitations and Future work |
| eftimov_2019_edsc_statistical_comparison | 3.2. Code correctness |
| epstein_2008_why_model | 5. Conclusion |
| hadjimichael_1993_interactive_inductive | 1. Introduction |
| halpern_pearl_2005_causes_and_explanations | 1. Introduction |
| hayes_2017_policy_explanation | 4. Limitations and Future work |
| hidalgo_2018_glucose_grammatical_evolution | 4. Limitations and Future work |
| kerschke_2019_algorithm_selection_survey | 3.4. Framework performance |
| malan_2021_landscape_analysis_survey | 2. Methodology |
| malan_gradient_walk_nn_landscapes | 2. Methodology |
| malek_2009_multi_agent_collaboration | 4. Limitations and Future work |
| mehdi_2015_compositional_forecasting | 2.3. PINN Customizer |
| merhej_2015_asp_rules_of_thumb | 4. Limitations and Future work |
| miller_2020_contrastive_explanation | 4. Limitations and Future work |
| noy_2001_ontology_development_101 | 2.2. Hierarchical text classifier |
| omahony_icon_algorithm_selection_challenge | 2.4. Evaluation Approach |
| potyka_2015_priority_probabilistic_kb | 2.2. Hierarchical text classifier |
| skvorc_2020_ela_problem_space | 2.4. Evaluation Approach |
| steiner_2024_steering_wheel_crn | 4. Limitations and Future work |
| studer_1998_knowledge_engineering | 4. Limitations and Future work |
| tonda_2013_bnsl_interaction | 4. Limitations and Future work |
| unpredictabilityAndComputationalIrreducibility | 1. Introduction |
| walton_2010_dialogue_explanation | 3.3. Working with the framework |
| weakEmergence | 2. Methodology |
| wei_2024_dante_active_optimization | 3.3. Working with the framework |
| zhang_2026_trm_complex_reasoning | 4. Limitations and Future work |

**Id-нумерация:** после `n15` идут `n16…n48`; порядок в списке `COMMENTARIES` определяет **порядок в сайдбаре внутри одного раздела** (первый пришёл — первый показан). Разумно: сначала «ядерные», потом второстепенные для того же раздела.

**Совет:** результат этой задачи сохранить как таблицу в `article/context/card_assignments.md` — тогда таск #13 может опираться на неё, а не восстанавливать через контекст.

### 3.2. #13 — Черновики `title` / `body` / `anchor_preview` для 33 карточек · зависит от #12

Правила из существующих 15:
- `title` — ≤10 слов, ироничный/утвердительный тон (примеры: «A named risk, now with a taxonomy», «Naming the statistics already being done», «Single-shot is the baseline this architecture was built to beat»).
- `body` — 3–5 плотных предложений; конкретика (проценты, номера figures), не общие рассуждения.
- `anchor_preview` — одно предложение-хук; появляется цитатным блоком до тела.
- `tagline` — `"Literature comparison"` или `"Literature comparison (proposed extension)"` (второе — когда карточка предлагает изменение сверх того, что заявлено в статье).

Для **ядерных 11** тексты должны читаться как этапы Roadmap Q1 из обзора:
- Wei/DANTE → «Sampling + Surrogate Pre-screen поднимет compliance с 25% до 40–50%».
- Zhang/TRM → «Bradley-Terry разделяет следование инструкции и точность прогноза».
- Eftimov/eDSC → «Разница 27% vs 25% при n=20 — шум; нужны Anderson-Darling + Bonferroni».
- Malan-2021 + Daza — «Fig. 4b,c — не ошибки LLM, а фрактальные бассейны loss-ландшафта».
- Noy → «Ad hoc Table A.2 без competency questions хрупкая».
- Halpern-Pearl + Miller → «Was the edit the *cause* of the shift? Contrastive foil not asked».
- Hidalgo → «Templates as grammars, но не переусложнять — GE_Dir теряет разнообразие».
- Malek → «MAS с Generator + Adviser + Solution Pool — готовая архитектура Future Work».
- Epstein → «Prediction is one of 17 goals of modeling — переформулировать как discipline the dialogue».

Для остальных 22 — короткий тематический body без глубокого раскрытия, чтобы не перегружать сайдбар.

Черновой материал для body — `thesis` из `/tmp/card_drafts.json` (первый неквотный абзац файла); для anchor_preview — можно взять один из ключевых абзацев файла и сжать до предложения.

### 3.3. #14 — Дописать 33 записи в `article/commentaries.py` · зависит от #12, #13

Приложить 33 dict-а в конец списка `COMMENTARIES`. Шаблон:

```python
{
    "id": "n16",
    "section": "3.3. Working with the framework",
    "category": "optimization",
    "category_label": "Active Optimization",
    "marker": "∆",
    "title": "Best-of-N with a surrogate, not one-shot at T=1.0",
    "body": "…",
    "filenote": "wei_2024_dante_active_optimization.md",
    "tagline": "Literature comparison (proposed extension)",
    "anchor_preview": "…",
    "sources": [
        {
            "text": "Wei et al. (2024), DANTE: Deep active optimization for complex systems",
            "url": "https://doi.org/10.1038/s43588-025-00858-x",
            "verified": True,
        },
    ],
},
```

Для `sources[].text` рекомендую формат `<Author> (<Year>), <Title>` — так же, как в 15 существующих. URL берётся из `/tmp/card_drafts.json:paper_b_url`.

**Важно:** `section` в commentary должен быть **точной подстрокой** соответствующего `<h2>`/`<h3>` в `body_html.py`, иначе `_inject_commentaries` (`article/sections.py:193`) не встроит блок в тело (карточка останется в сайдбаре, но без анкера). Все `inferred_section` из таблицы выше уже проверены на существование заголовка.

### 3.4. #15 — Дописать 33 записи в `article/commentary_anchors.py` · зависит от #14

Формат:
```python
"n16": (
    "точный фрагмент из body_html.py"
),
```

Все 33 фрагмента уже готовы — в `/tmp/card_drafts.json:anchor_text`. Скрипт `scripts/extract_card_drafts.py` уже верифицировал substring-совпадение с нормализацией «ёлочек».

**Регенерация JSON** (если /tmp почистился):
```bash
cd /Users/inter-malchik/Downloads/expert_driven_modeling_advancements-main
python3 scripts/extract_card_drafts.py > /tmp/card_drafts.json
```

### 3.5. #16 — `SOURCE_URLS` в `commentary_links.py` · зависит от #14

Скорее всего **пропустить**: если `sources[].url` заполнен, `resolve_source_url` возьмёт его без обращения к `SOURCE_URLS`. Из 33 сравнений у 32 есть URL в блоке `Paper B — live link`; единственное исключение — `malek_2009_multi_agent_collaboration` (нет DOI в файле — придётся либо оставить без URL, либо найти вручную).

### 3.6. #17 — `CATEGORY_COLORS` в `article/sections.py` · зависит от #12

Файл `article/sections.py:111`. Текущий словарь:
```python
CATEGORY_COLORS = {
    "reliability": "#6B4271",
    "architecture": "#2E6E8E",
    "alignment": "#A6772C",
    "formalization": "#45527A",
    "evaluation": "#2F6B62",
    "explanation": "#6B6B2C",
    "epixai": "#8A5A3F",
}
```

Добавить как минимум:
- `optimization` — тёплый оттенок, отличимый от `alignment` (#A6772C) и `epixai` (#8A5A3F). Кандидат: `"#7A4A3F"` или `"#8E5E2E"`.
- `pathology` — контрастный, лучше «остывший». Кандидат: `"#5A3F6B"` или `"#3F4E6B"`.
- Если добавляется `argumentation` — что-то нейтральное; кандидат: `"#4E6B3F"`.

Точные HEX-ы стоит выбрать так, чтобы визуально не сливались с уже занятыми (7 существующих + новые).

### 3.7. #10 — Финальная правка `ADD_NEW_CARDS.md` · зависит от #17

Осталось два фрагмента:
- Строка **139**: `COMMENTARY_IDS = [f"n{i}" for i in range(1, 16)]` → надо переписать как «сейчас `range(1, 49)`; при добавлении n49 увеличить верхнюю границу до 50, и т. д.».
- Строка **139**: «Пока карточек 15» → «Сейчас карточек 48».
- Строка **144**: пример `range(1, 17)  # для n16` → лучше `range(1, N+1)  # для n<N>`.

Опционально пересмотреть Шаг 7 (заголовок раздела): у нас все секции покрыты, но упоминание `scripts/build_body_html.py` актуально.

### 3.8. #11 — Верификация · зависит от всего выше

Чек-лист:
1. `python3 -c "from article.commentaries import COMMENTARIES; print(len(COMMENTARIES))"` — должно быть 48.
2. `python3 -c "from article.commentary_anchors import ANCHOR_TEXTS; print(len(ANCHOR_TEXTS))"` — должно быть 48.
3. `streamlit run streamlit_app.py`.
4. В сайдбаре — 48 карточек, сгруппированных по разделам «1. Introduction / 2. Methodology / 2.1 / 2.2 / 2.3 / 2.4 / 3.2 / 3.3 / 3.4 / 4. Limitations / 5. Conclusion».
5. Клик по маркеру любой новой карточки — переход к подсвеченному фрагменту в тексте.
6. «Read full comparison» открывает `?analysis=<slug>&from=n<N>` c контентом. Строки `> **Source in \`src/\`:**` в рендере быть **не должно**.
7. Оригинальные 15 карточек работают по новым URL (`?analysis=kreikemeyer_2025_llm_reaction_networks` и т. д.).
8. Палитра — 48 визуально различимых оттенков.
9. `article/context/dinara_comprehensive_review.md` не подключён в приложение (это только контекст для агента) — проверить, что импорты не сломались.

---

## 4. Технические ограничения (не забыть)

1. **Anchor text ≠ regex**: `inject_anchor_highlights` делает `str.find` с нормализацией `’‘“”–` → ASCII (см. `article/anchor_highlights.py:13`). Если якорь содержит `\n`, HTML-теги или множественные пробелы — совпадение не найдётся. Скрипт `extract_card_drafts.py` уже подобрал безопасные варианты.
2. **Filenote — не путь**: только имя файла (`slug.md`), без `article/analysis/`. Функция `analysis_slug_from_filenote` (`article/analysis_index.py:16`) отрезает суффикс `.md` и всё после `" — "`.
3. **Section-match — точное string equality с текстом внутри тега** (см. `_inject_commentaries`, `article/sections.py:198`). Пробелы и точки значимы: `"2.2. Hierarchical text classifier"` — единственное правильное написание.
4. **Порядок в сайдбаре** = порядок в `COMMENTARIES`, сгруппированный по `section` (см. `commentaries_by_section`, `article/commentaries.py:327`).
5. **Первая строка карточки-сравнения** может содержать `> **Paper B — live link:** ...` — она остаётся в рендере. Строка `> **Source in \`src/\`:**` удаляется на лету регуляркой `_SRC_LINK_LINE` в `article/comparison_prose.py`, файлы на диске не редактируем.
6. **HTML статьи** (`article/body_html.py:BODY_HTML`) — генерируется скриптом `scripts/build_body_html.py` из markdown; редактировать руками разрешено (заголовки сохранятся), но лучше знать, что источник — `article/source.md` (пустой сейчас) → `body_html.py`.

---

## 5. Артефакты и пути

- Черновые данные (33 записи): `/tmp/card_drafts.json` — регенерируется командой ниже.
- Скрипт-извлекатель: `scripts/extract_card_drafts.py`.
- Контекст-обзор: `article/context/dinara_comprehensive_review.md`.
- Утверждённый план миграции: `~/.claude/plans/ai-chat-attachment-6895312849033851907-keen-aurora.md`.
- Гайд для будущих карточек: `ADD_NEW_CARDS.md` (в корне).

**Регенерация JSON**:
```bash
cd /Users/inter-malchik/Downloads/expert_driven_modeling_advancements-main
python3 scripts/extract_card_drafts.py > /tmp/card_drafts.json
```

**Быстрая проверка приложения без streamlit**:
```bash
python3 -c "
import sys; sys.path.insert(0, '.')
from article.commentaries import COMMENTARIES
from article.commentary_anchors import ANCHOR_TEXTS
from article.commentary_colors import COMMENTARY_IDS
print('COMMENTARIES:', len(COMMENTARIES))
print('ANCHOR_TEXTS:', len(ANCHOR_TEXTS))
print('COMMENTARY_IDS:', len(COMMENTARY_IDS))
# все id должны быть уникальны, filenotes ссылаться на существующие файлы
from pathlib import Path
ids = [c['id'] for c in COMMENTARIES]
assert len(set(ids)) == len(ids), 'duplicate id!'
files = {p.name for p in Path('article/analysis').glob('*.md')}
for c in COMMENTARIES:
    fn = c['filenote'].split(' — ')[0]
    assert fn in files, f'missing file: {fn}'
print('OK')
"
```

---

## 6. Ссылки на приоритеты обзора

Полный обзор в `article/context/dinara_comprehensive_review.md`. Короткая выжимка:

**Блок 2 — методологическая критика** называет 4 slot-а, куда должны попасть карточки:
1. Метрология (`zhang_2026_trm`, `eftimov_2019_edsc`) — обосновать субъективность «Compliance» и статистическую неразличимость 25 vs 27%.
2. Loss-landscape патология (`malan_2021`, `daza_2016`, + сопутствующие `abell`, `malan_gradient_walk`, `clark`, `weakEmergence`, `unpredictability`) — Fig. 4b,c это не ошибки LLM.
3. Экспертная система без экспертов (`noy_2001`, косвенно `hadjimichael_1993`, `studer_1998`) — Appendix A хрупкая без формальной онтологии.

**Блок 3 — литературные кластеры**:
- Кластер 1 (ЯДРО): `wei_2024_dante`.
- Кластер 12 (Actual Cause): `halpern_pearl_2005`, `miller_2020_contrastive`.
- Кластер 13 (Онтологии/DSL): `hidalgo_2018`, `noy_2001`.
- Кластер 14 (MAS): `malek_2009`.

**Блок 4 — Roadmap Q1** (4 шага):
1. Объективизация оценки → `zhang_2026_trm` — Bradley-Terry MQM (реф. модель).
2. Sampling + surrogate → `wei_2024_dante` — best-of-k + MQM pre-screen; ожидаемый рост compliance 25% → 40–50%.
3. Формализация правил → `hidalgo_2018` (grammar) + `noy_2001` (ontology).
4. Риторический фрейминг → `epstein_2008` — переформулировать как «дисциплинирование диалога», а не «прорицание».

Тон карточек должен показывать, что «неожиданности» статьи (нестабильность, субъективность) — не открытые проблемы, а решённые задачи в SOTA-литературе 2024–2026.

---

## 7. Что можно пропустить / сделать позже

- **`SOURCE_URLS`** — не нужно, если `sources[].url` заполнен (кроме `malek_2009`, где URL нет — можно оставить `None`).
- **Дополнительные категории сверх `optimization`/`pathology`** — опционально. Argumentation-кластер (Amgoud/Cayrol/Dubois и т.д.) можно распределить по `formalization` или `explanation`.
- **Правки `body_html.py`** — не нужны: все 33 `inferred_section` попадают в существующие заголовки.
- **Обновление `article/source.md`** — не нужно, там уже верная сборочная инструкция.

---

## 8. Порядок действий для агента-продолжателя

1. Прочитать `article/context/dinara_comprehensive_review.md`.
2. Открыть `/tmp/card_drafts.json` (или перегенерировать).
3. Выполнить #12 — таблица распределения. Сохранить в `article/context/card_assignments.md`.
4. Выполнить #17 — добавить категории в `CATEGORY_COLORS`.
5. Выполнить #13 — черновые тексты. Сохранить в `article/context/card_texts.md` (по одному блоку на слаг).
6. Выполнить #14 — сгенерировать/вставить 33 dict-а в `commentaries.py`.
7. Выполнить #15 — вставить 33 записи в `commentary_anchors.py`.
8. Выполнить #16 — при необходимости `SOURCE_URLS`.
9. Выполнить #10 — обновить строки 139/144 в `ADD_NEW_CARDS.md` под N=48.
10. Выполнить #11 — верификация (см. чек-лист).
