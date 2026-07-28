# Что Не Хватило Для Полного Завершения Работы С Карточками

Этот файл фиксирует не то, что осталось вовсе не сделанным, а именно те дефициты исходных материалов и инфраструктуры, которые помешали довести все карточки до полностью единообразного и максимально строгого стандарта `Sources & Evidence`.

## Общий Итог

- Разделы `Sources & Evidence` были добавлены в карточки.
- Однако не все карточки удалось закрыть в одинаковом качестве источников.
- Основная причина: для части cited works в репозитории отсутствуют локальные полные транскрипции в `article/transcriptions/`.
- В этих случаях пришлось опираться на первичные abstract-страницы по ссылкам из front matter, а не на локальный полнотекстовый transcription workflow.

## Главный Дефицит

- Не для всех работ, уже перечисленных в `[[sources]]` карточек, есть соответствующие локальные файлы в `article/transcriptions/`.
- Из-за этого часть карточек оформлена по ослабленному стандарту:
  - claim-level evidence есть,
  - прямые цитаты есть,
  - но цитаты взяты только из abstract / landing page статьи, а не из полной локальной транскрипции.

## Конкретно Чего Не Хватило

### 1. Отсутствовали локальные транскрипции для `n52`

Карточка:
- `article/commentaries_data/2_4_evaluation_approach/n52.md`

Не хватило полных локальных транскрипций для работ:
- `Akazan et al. (2025), RRaPINNs: Residual Risk-Aware Physics Informed Neural Networks`
- `Han et al. (2022), Residual-Quantile Adjustment for Adaptive Training of Physics-informed Neural Network`

Что пришлось сделать вместо этого:
- использовать цитаты из первичных abstract-страниц по source links;
- оформить `Sources & Evidence` по abstract-level evidence.

Что желательно для полного закрытия:
- добавить полные локальные транскрипции обеих работ в `article/transcriptions/`;
- после этого переписать `n52.md` так, чтобы evidence опирался не только на abstract, а на полноценные sections / formulations / experimental claims.

### 2. Отсутствовали локальные транскрипции для `n50`

Карточка:
- `article/commentaries_data/4_limitations_and_future_work/n50.md`

Не хватило полных локальных транскрипций для работ:
- `Eshkofti et al. (2025), Vanishing Stacked-Residual PINN for State Reconstruction of Hyperbolic Systems`
- `Chiu et al. (2026), Scale-PINN: Learning Efficient Physics-Informed Neural Networks Through Sequential Correction`

Что пришлось сделать вместо этого:
- использовать цитаты из первичных abstract-страниц;
- оформить evidence только на уровне abstract claims.
# CARD COMPLETION GAPS

Что желательно для полного закрытия:
- добавить обе статьи в `article/transcriptions/`;
- затем расширить `Sources & Evidence` по архитектурным деталям:
  - staged residual correction,
  - viscosity schedule / refinement logic,
  - sequential correction inside loss construction,
  - experimental stability / convergence claims.
Назначение: зафиксировать недостающие материалы и контентные пробелы, которые мешают полностью закончить оформление карточек (в формате с жёсткой трассировкой claim → source → verbatim quotes из локальных транскрипций).

## Что Ещё Было Ограничением
Обновление на дату: 2026‑07‑28

### 3. Не везде можно было дать section-level locators внутри локальной базы
## 1) Отсутствующие локальные транскрипции (нужны для замены цитат из абстрактов/ссылок)

- Для карточек, где источник был только через abstract, невозможно было дать locator вида `Section X`, `Figure Y`, `Equation Z`.
- Пришлось ограничиться пометкой `abstract`.
- n52 — article/commentaries_data/2_4_evaluation_approach/n52.md (Risk‑aware Optimization)
  - Akazan et al. (2025), “RRaPINNs: Residual Risk‑Aware Physics Informed Neural Networks” — нет локального файла в article/transcriptions.
  - Han et al. (2022), “Residual‑Quantile Adjustment for Adaptive Training of PINN” — нет локального файла в article/transcriptions.
  - Действие: добавить оба транскрипта в `article/transcriptions/` и заменить абстракт‑цитаты на verbatim фрагменты с Section/Equation/lines.

Это касается:
- `n52`
- `n50`
- n50 — article/commentaries_data/4_limitations_and_future_work/n50.md (Stacked‑Residual / Sequential‑Correction)
  - Eshkofti et al. (2025), “Vanishing Stacked‑Residual PINN…” — нет локального транскрипта.
  - Chiu et al. (2026), “Scale‑PINN: Sequential Correction…” — нет локального транскрипта.
  - Действие: добавить транскрипты и заменить абстракт‑цитаты на verbatim.

### 4. Не все analysis-файлы подкреплены полнотекстовыми первичными источниками в репозитории
- n15 — article/commentaries_data/4_limitations_and_future_work/n15.md (People‑centred XAI)
  - Longo, “How the Future Depends on the Past and Rare Events in Systems of Life” — локального транскрипта не найдено (точные выходные данные/глава требуются).
  - Действие: добавить корректную библиографию (глава/издание) и локальный транскрипт для включения 1–2 ключевых цитат.

- Для некоторых карточек analysis уже есть и хорошо раскрывает смысл paper-to-paper comparison.
- Но analysis-файл не заменяет `article/transcriptions/*` как первичную evidence-базу.
- Там, где transcription отсутствовал, analysis помогал понять логику карточки, но не мог считаться полноценной заменой доказательной базы.
## 2) Карточки с оформленным S&E, но полезно усилить точными локаторами (страницы)

## Чего НЕ Не Хватило
Следующие карточки уже содержат “Sources & Evidence” из локальных транскрипций, однако для идеальной воспроизводимости желательно указать номера страниц (где применимо), т.к. сейчас в ряде мест стоят только секции/фигуры/строки:

Ниже перечислены вещи, которые не являлись блокерами:
- n30 — Kerschke et al. (2019): §1/§2 покрыты; страницы приветствуются.
- n14 — Pillay (2010): Abstract/Intro процитированы; можно дополнить страницами/рисунками, если есть в PDF.
- n15 — Miller (2017); Broekens (2010): добавить номера страниц для процитированных мест.
- n18 — Arioua & Croitoru (2015): Definitions 4–5 и интеграция с ARG — добавить номера страниц.

- Формат самих карточек `nXX.md` был достаточным.
- Структура front matter в целом была достаточной.
- Для большинства карточек нужные локальные транскрипции уже были в репозитории.
- Для карточек, закрытых через локальные `article/transcriptions/*.md`, evidence удалось оформить в полном рабочем стандарте.
## 3) Проверка наличия опорных транскриптов, задействованных в других карточках (на случай будущих правок)

## Что Нужно Сделать Для Идеального Финала
- Noy & McGuinness (2001) “Ontology Development 101” — убедиться, что локальный транскрипт присутствует (для n7/n37).
- Gruber (1993) “A Translation Approach to Portable Ontology Specifications” — проверить наличие (n7).
- Chakraborti et al. (2017) “Plan Explanations as Model Reconciliation” — проверить наличие (n10/n7).
- W3C PROV‑DM (для traceability) — при необходимости добавить выдержки.
- Semantic Versioning 2.0.0 — добавить выдержки правил (MAJOR.MINOR.PATCH) при расширении n7.
- Yu et al. (2025) “Spec2RTL‑Agent” — убедиться в наличии локального транскрипта (используется в n5/n12 при доработках).

Чтобы довести весь корпус карточек до полностью единообразного стандарта, нужен такой минимальный добор материалов:
## 4) Известные ограничения/договорённости

1. Добавить в `article/transcriptions/` полные локальные транскрипции четырёх работ:
- Akazan et al. (2025)
- Han et al. (2022)
- Eshkofti et al. (2025)
- Chiu et al. (2026)
- Скриншоты/изображения не вставляются по договорённости; вместо этого указывать Figure/Table/Equation/Section/lines.
- Все новые цитаты — строго англоязычные verbatim из локальных транскриптов.

2. После этого обновить две карточки:
- `article/commentaries_data/2_4_evaluation_approach/n52.md`
- `article/commentaries_data/4_limitations_and_future_work/n50.md`
## 5) Резюме действий для полного закрытия

3. Для них заменить abstract-level evidence на full-text evidence:
- с более точными locators,
- с section-specific claims,
- с более сильной опорой на методы / результаты / ограничения самих papers.
1. Добавить недостающие транскрипты (Akazan 2025; Han 2022; Eshkofti 2025; Chiu 2026; Longо — точную ссылку подтвердить).
2. В n50 и n52 заменить абстракт‑цитаты на verbatim фрагменты из локальных транскриптов.
3. Проставить номера страниц к уже вставленным цитатам в n30, n14, n15, n18.
4. Пройти быстрый контроль на консистентность “Sources & Evidence” (единый стиль, отсутствие дубликатов секций, корректные локаторы).

## Практический Вывод

- Карточки как рабочий корпус сейчас закрыты.
- Но полностью строгий и единообразный стандарт достигнут не на 100%, а на уровне:
  - почти все карточки опираются на локальные полнотекстовые транскрипции;
  - `n52` и `n50` пока опираются только на abstract-level первичные источники.
- Именно отсутствие этих четырёх полнотекстовых статей было главным недостающим элементом для полного завершения работы без оговорок.
После выполнения пунктов 1–4 база карточек будет полностью закрыта по методологическим требованиям (источники → цитаты → утверждения, воспроизводимость и трассируемость).


