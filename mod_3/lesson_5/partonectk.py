# Библиотека
from customtkinter import * # pip install customtkinter

# Тема окна
set_appearance_mode("dark") # Тема
set_default_color_theme("dark-blue") # Цвет темы

# Окно
if __name__ == "__main__": # Проверка на основной файл программы
    root = CTk() # Главное окно

    # Функции окна
    def close_window(event): # Закрытие окна
        root.destroy() # Уничтожение окна

    # Свойства окна
    root.geometry("300x200") # Размер окна
    root.resizable(False, False) # Возможность менять размер
    root.title("Библиотека customtkinter") # Название окна
    root.attributes("-topmost", True) # Окно поверх всех
    root.overrideredirect(True) # Окно без рамки

    # Виджеты
    CTkLabel(root, text="Привет, мир!").pack() # Текст
    CTkButton(root, text="Закрыть окно", command=lambda: close_window(None)).pack() # Кнопка

    # Команды-бинды окна
    root.bind("<Escape>", close_window) # Закрытие окна при нажатии Escape

    root.mainloop() # Запуск окна