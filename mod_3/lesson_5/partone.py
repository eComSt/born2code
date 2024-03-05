from tkinter import *
if __name__ == "__main__":
    window = Tk() # создаем главное окно
    window.title('Добро пожаловать!') # задаем название окна
    window.geometry('300x400') #
    # создаем виджет для отображения однострочного текста
    label = Label(text='Hello', font=('Arial', 20))
    label.place(x=0, y=0)
    window.mainloop() # запускаем цикл обработки событий
    # n = 0
    # while True:
    #     window.update()
    #     n+=1
    #     if n>100: n =0
    #     window.title((n//10)*" "+'Добро!') # задаем название окна