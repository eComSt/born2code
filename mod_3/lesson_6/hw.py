from random import randint
from tkinter import *
class Game:
    def __init__(self):
        self.random_number = randint(1,100)
    def check_answer(self, ans):
        try:
            ans  = int(ans)
            if 1 <= ans <= 100:
                st = f"Ваше число {ans}. "
                if self.random_number == ans:
                    return st + "Угадали!"
                elif self.random_number < ans:
                    return st + "Мое число меньше!"
                else:
                    return st + "Мое число больше!"
            else:
                return "Введите число от 1 до 100"
        except ValueError:
            return "Введите корректное число"
        
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x300')
        self.window.title('Угадай число')
        self.game = Game()          # экземпляр класса Game
        self.startUI(self.window)   # наполнение окна виджетами

        self.window.mainloop() 

    def startUI(self, window):
        # задаем вес для рядов и колонок
        for c in range(3): window.columnconfigure(index=c, weight=1)
        for r in range(4): window.rowconfigure(index=r, weight=1)
        # создаем и размещаем подпись "Угадайте число от 1 до 100:"
        self.guess_label = Label(window, text="Угадайте число от 1 до 100:", font=("Arial", 12))
        self.guess_label.grid(row=0, column=1)
        # создаем и размещаем поле для ввода числа
        self.guess_entry = Entry(window, font=("Arial", 12), width=10)
        self.guess_entry.grid(row=1, column=1)
        # создаем и размещаем кнопку для проверки числа
        self.submit_button = Button(window, text="Проверить", font=("Arial", 12), command=self.button_click)
        self.submit_button.grid(row=2, column=1)
        # создаем и размещаем многострочный текст для вывода результата проверки числа
        self.result_message = Message(window, font=("Arial", 12), width=300)
        self.result_message.grid(row=3, column=1)
    
    # метод для обработки нажатия на кнопку
    def button_click(self):
        # получаем число, введенное пользователем
        guess_numb = self.guess_entry.get()
        print(guess_numb)
        # вызываем метод check_answer(), получаем результат проверки числа и размещаего его на окне
        self.result_message['text'] = self.game.check_answer(guess_numb)

# создаем экземпляр класса GUI
app = GUI()
