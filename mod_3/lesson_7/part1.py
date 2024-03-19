from customtkinter import *
def button_click():
    global count_clicks
    count_clicks += 1
    clicks.configure(text=f'Количество нажатий: {count_clicks}')
# создаем и настраиваем главное окно
window = CTk()
window.title('Мое окно')
window.geometry('400x300')
window.grid_columnconfigure(index=(0), weight=1)
window.grid_rowconfigure(index=(0, 1, 2, 3), weight=1)
label = CTkLabel(window, text='Пример текста в CustomTkinter')
# меняем размер шрифта однострочного текста
label.cget('font').configure(size=20)
label.grid(row=0, column=0)
checkbox_frame = CTkFrame(window)
checkbox_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')
# создаем и размещаем чек-бокс
checkbox_1 = CTkCheckBox(checkbox_frame, text='Вариант 1')
checkbox_1.grid(row=0, column=0)
checkbox_2 = CTkCheckBox(checkbox_frame, text='Вариант 2')
checkbox_2.grid(row=1, column=0)
count_clicks = 0 # счетчик нажатий на кнопку
# однострочный текст для отображения количества нажатий на кнопку
clicks = CTkLabel(window, text=f'Количество нажатий: {count_clicks}')
clicks.grid(row=1, column=0)
button = CTkButton(window, text='Кнопка', fg_color='blue',command=button_click)
button.grid(row=2, column=0, padx=20, pady=20, sticky='we')
# запускаем цикл обработки событий
window.mainloop()
