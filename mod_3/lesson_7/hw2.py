from customtkinter import *
from random import randint

# функция обработки нажатия на стандартную кнопку
def check_state():
    # делаем переменную rand_num глобальной
    global rand_num
    # получаем номер выбранной радиокнопки
    num_btn = selected.get()
    # если сгенерированный номер совпал с номером выбранной кнопки
    if num_btn == rand_num:
        # генерируем новый номер кнопки
        rand_num = randint(1, 3)
        # выводим на окно сообщение о верном выборе
        text.configure(text=f'Все верно! Теперь нажмите на кнопку {rand_num}')
    # если сгенерированный номер не совпал с номером выбранной кнопки
    else:
        # выводим на окно сообщение о неверном выборе
        text.configure(text=f'Неверно! Нажмите на кнопку {rand_num}')

# создаем и настраиваем экземпляр главного окна
window = CTk()
window.geometry('400x200')
# настраиваем сеточную систему окна (3 строки, 3 столбца)
window.grid_columnconfigure((0, 1, 2), weight=1)
window.grid_rowconfigure((0, 1, 2), weight=1)
# генерируем случайный номер кнопки от 1 до 3
rand_num = randint(1, 3)
# создаем текст с информацией о кнопке и размещаем его в верхней части окна
text = CTkLabel(window, text=f'Нажмите на кнопку {rand_num}')
text.grid(row=0, column=0, columnspan=3)
# создаем переменную для группировки радиокнопок
selected = IntVar()
# создаем и размещаем первую радиокнопку
rad1 = CTkRadioButton(window, text='Кнопка 1', value=1, variable=selected)
rad1.grid(row=1, column=0)
# создаем и размещаем вторую радиокнопку
rad2 = CTkRadioButton(window, text='Кнопка 2', value=2, variable=selected)
rad2.grid(row=1, column=1)
# создаем и размещаем третью радиокнопку
rad3 = CTkRadioButton(window, text='Кнопка 3', value=3, variable=selected)
rad3.grid(row=1, column=2)
# создаем и размещаем стандартную кнопку
btn_check = CTkButton(window, text='Проверить', command=check_state)
btn_check.grid(row=2, column=1)
# запускаем цикл обработки событий
window.mainloop()
