import random
from customtkinter import CTk, CTkLabel, CTkRadioButton, CTkButton
import tkinter as tk
from tkinter import IntVar

class Game:
    def __init__(self):
        self.secret_button_number = random.randint(1, 3)
        self.guesses = 0
    
    def check_button(self, button_number):
        self.guesses += 1
        if button_number == self.secret_button_number:
            self.secret_button_number = random.randint(1, 3)  # Генерируем новый случайный номер кнопки
            return f'Все верно! Теперь нажмите на кнопку {self.secret_button_number}'
        else:
            return f'Неверно! Нажмите на кнопку {self.secret_button_number}'

class GUI(CTk):
    def __init__(self):
        super().__init__("#000000")  # Цвет фона окна
        self.game = Game()
        self.create_widgets()

    def create_widgets(self):
        self.label = CTkLabel(self, text=f"Нажмите на кнопку {self.game.secret_button_number}")
        self.label.pack(pady=10)

        self.selected_button = IntVar()
        self.radio_button1 = CTkRadioButton(self, text="Кнопка 1", variable=self.selected_button, value=1)
        self.radio_button1.pack()

        self.radio_button2 = CTkRadioButton(self, text="Кнопка 2", variable=self.selected_button, value=2)
        self.radio_button2.pack()

        self.radio_button3 = CTkRadioButton(self, text="Кнопка 3", variable=self.selected_button, value=3)
        self.radio_button3.pack()

        self.check_button = CTkButton(self, text="Проверить", command=self.check_button)
        self.check_button.pack()

    def check_button(self):
        selected_button_number = self.selected_button.get()
        result = self.game.check_button(selected_button_number)
        self.label.configure(text=result)

app = GUI()
app.mainloop()