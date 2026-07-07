# 🚀 Expert-Guided PINN Forecasting

Веб-приложение для демонстрации результатов исследования по прогнозированию заболеваемости ОРВИ с использованием нейронных сетей, информированных физикой (PINN), и больших языковых моделей (LLM).

## 📄 Текущее состояние
- На главной странице отображается статья в формате Elsevier: двухколоночная вёрстка, таблицы, рисунки и библиография.
- Исходные страницы PDF: `assets/paper/pages/`
- Вырезанные рисунки: `assets/figures/`
- Стили и разметка: `article/styles.py`, `article/sections.py`

## 🛠 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aleks/expert_driven_modeling_advancements.git
   cd expert_driven_modeling_advancements
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Запуск

Обычный запуск (после активации venv):
```bash
streamlit run streamlit_app.py
```

Запуск напрямую из виртуального окружения (без предварительной активации):
```bash
# macOS / Linux
./venv/bin/python -m streamlit run streamlit_app.py

# Windows
.\venv\Scripts\python -m streamlit run streamlit_app.py
```

## 📁 Структура
- `streamlit_app.py`: Основной код приложения.
- `requirements.txt`: Список необходимых библиотек.
- `.streamlit/config.toml`: Конфигурация Streamlit (тема, порты и т.д.).
- `.streamlit/secrets.toml`: Файл для хранения секретов (API-ключи, пароли и т.д.).
- `assets/`: Медиа-файлы (рисунки, страницы PDF).
- `article/`: Стили и разметка для отображения статьи.
