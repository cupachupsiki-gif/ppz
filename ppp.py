import streamlit as st

# Настройки страницы
st.set_page_config(
    page_title="Мой сайт",
    layout="wide"
)

# Заголовок
st.title("Мой сайт")

# Текст
st.write("Добро пожаловать на сайт!")

# Поле ввода
name = st.text_input("Введите ваше имя")

# Кнопка
if st.button("Отправить"):
    if name:
        st.success(f"Привет, {name}!")
    else:
        st.warning("Введите имя.")

# Разделитель
st.divider()

# Дополнительная информация
st.subheader("О сайте")
st.write("Это базовый шаблон сайта на Streamlit.")
