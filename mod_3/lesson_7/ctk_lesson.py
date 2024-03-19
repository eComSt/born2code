# Работа с Custom Tkinter I

from customtkinter import *

def button_click():
    global count_clicks
    count_clicks += 1
    clicks.configure(text=f'Количество нажатий: {count_clicks}')

# создаем и настраиваем главное окно
window = CTk()
window.title('Мое окно')
window.geometry('400x300')

# задаем сеточную конфигурацию окна
window.grid_columnconfigure(index=(0), weight=1)
window.grid_rowconfigure(index=(0, 1, 2, 3), weight=1)

# создаем и размещаем однострочный текст
label = CTkLabel(window, text='Пример текста в CustomTkinter')
label.grid(row=0, column=0)
# меняем размер шрифта однострочного текста
label.cget('font').configure(size=20)

# счетчик нажатий на кнопку
count_clicks = 0
# однострочный текст для отображения количества нажатий на кнопку
clicks = CTkLabel(window, text=f'Количество нажатий: {count_clicks}')
clicks.grid(row=1, column=0)

# создаем и размещаем стандартную кнопку
button = CTkButton(window, text='Кнопка', fg_color='blue', command= button_click)
button.grid(row=2, column=0, padx=20, pady=20, sticky='we')

# Фрейм - дополнительная область внутри окна для структурирования виджетов
# Создаем и размещаем фрейм для группировки чек-боксов
checkbox_frame = CTkFrame(window)
checkbox_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')
# задаем сеточную конфигурацию для фрейма
checkbox_frame.grid_columnconfigure((0), weight=1)
checkbox_frame.grid_rowconfigure((0, 1), weight=1)
# создаем и размещаем 2 чек-бокса
checkbox_1 = CTkCheckBox(checkbox_frame, text='Вариант 1')
checkbox_1.grid(row=0, column=0)
checkbox_2 = CTkCheckBox(checkbox_frame, text='Вариант 2')
checkbox_2.grid(row=1, column=0)

# запускаем цикл обработки событий
window.mainloop()



