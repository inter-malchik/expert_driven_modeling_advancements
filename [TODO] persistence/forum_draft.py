import streamlit as st
import json
import os
import redis
from datetime import datetime

# Конфигурация
COMMENTS_FILE = "comments.json"
# Приоритеты хранилища: Redis -> Local JSON
USE_REDIS = "REDIS_URL" in st.secrets

@st.cache_data(ttl=60) # Кэшируем на 1 минуту для снижения нагрузки на Redis
def load_comments():
    if USE_REDIS:
        try:
            r = redis.from_url(st.secrets["REDIS_URL"], decode_responses=True)
            data = r.lrange("comments_list", 0, -1)
            return [json.loads(c) for c in data]
        except Exception as e:
            st.error(f"Ошибка при загрузке из Redis: {e}")
            return []
    
    # Локальный режим
    if os.path.exists(COMMENTS_FILE):
        try:
            with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_comments(comments_or_new_comment):
    success = False
    if USE_REDIS:
        try:
            r = redis.from_url(st.secrets["REDIS_URL"], decode_responses=True)
            if isinstance(comments_or_new_comment, list):
                new_data = comments_or_new_comment[-1]
            else:
                new_data = comments_or_new_comment
            
            r.rpush("comments_list", json.dumps(new_data, ensure_ascii=False))
            success = True
        except Exception as e:
            st.error(f"Ошибка при сохранении в Redis: {e}")
            success = False
    else:
        # Локальный режим
        try:
            comments = comments_or_new_comment if isinstance(comments_or_new_comment, list) else load_comments() + [comments_or_new_comment]
            with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
                json.dump(comments, f, ensure_ascii=False, indent=4)
            success = True
        except Exception as e:
            st.error(f"Ошибка при локальном сохранении: {e}")
            success = False
    
    if success:
        st.cache_data.clear() # Очищаем кэш после добавления нового комментария
    return success

st.set_page_config(
    page_title="Streamlit Forum",
    page_icon="💬",
    layout="wide",
)

st.title("💬 Живой форум на Streamlit")

# Загружаем комментарии
comments = load_comments()

# Боковая панель
st.sidebar.header("Настройки профиля")
user_name = st.sidebar.text_input("Ваше имя", "Гость")

# Информация о хранилище
if USE_REDIS:
    storage_type = "Render Redis 🚀"
else:
    storage_type = "Локальный JSON 📁"

st.sidebar.write(f"Хранилище: **{storage_type}**")

# Форма для нового комментария
st.header("📝 Оставить комментарий")
with st.form("comment_form", clear_on_submit=True):
    comment_text = st.text_area("Ваше сообщение", placeholder="Напишите что-нибудь...")
    submit_button = st.form_submit_button("Отправить")

    if submit_button:
        if comment_text.strip():
            new_comment = {
                "name": user_name,
                "text": comment_text,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # Атомарно сохраняем новый комментарий
            if save_comments(new_comment):
                st.success("Комментарий успешно добавлен!")
                st.rerun()
        else:
            st.error("Пожалуйста, введите текст сообщения.")

# Отображение комментариев
st.header("💬 Последние обсуждения")
if not comments:
    st.info("Пока нет ни одного комментария. Будьте первым!")
else:
    # Показываем последние комментарии сверху
    for c in reversed(comments):
        st.markdown(f"**{c.get('name', 'Аноним')}** `{c.get('date', '')}`")
        st.write(c.get('text', ''))
        st.divider()

# Дополнительный контент в сайдбаре
st.sidebar.markdown("---")
st.sidebar.info(
    "Это приложение поддерживает сохранение данных даже после передеплоя "
    "через Redis (Render) и использует кэширование для скорости."
)
