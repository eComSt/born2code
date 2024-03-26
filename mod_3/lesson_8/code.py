from customtkinter import *
# класс для главного окна
class MainWindow(CTk):
    # инициализатор класса
    def __init__(self):
        # вызываем инициализатор из родительского класса
        super().__init__()
        # задаем название и размеры главного окна
        self.title('Цвета и фигуры')
        self.geometry('400x300')
        # задаем сеточную конфигурацию 
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # создаем и размещаем стандартную кнопку
        self.button = CTkButton(self, text='Отправить', command=self.show_info)
        self.button.grid(row=1, padx=10, pady=10, sticky='ew', columnspan=2)
        # создаем и размещаем лейбл с данными из чекбоксов и радиокнопок
        self.text = CTkLabel(self, text='')
        self.text.grid(row=2, padx=10, pady=10, sticky='ew', columnspan=2)
        
        self.checkbox_frame = MyCheckboxFrame(self, title='Выбери цвет', values=('Красный', 'Синий', 'Зеленый'))
        self.checkbox_frame.grid(row=0, column=0,  padx=10, pady=10, sticky='nsew')
        # создаем и размещаем фрейм с радиокнопками
        self.radiobutton_frame = MyRadiobuttonFrame(self, title='Выбери фигуру', values=('Круг', 'Квадрат'))
        self.radiobutton_frame.grid(row=0, column=1,  padx=10, pady=10, sticky='nsew')
    def show_info(self):
        pass

class MyCheckboxFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.checkboxes = []
        self.title = CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        for i in range(len(values)):
            checkbox = CTkCheckBox(self, text=values[i])
            checkbox.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")
            self.checkboxes.append(checkbox)

class MyRadiobuttonFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
    def get(self):
        pass

root = MainWindow()
root.mainloop()