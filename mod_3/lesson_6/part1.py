from tkinter import *
window = Tk() # создаем объект главного окна
window.geometry('350x300') # задаем размеры окна
# создаем стандартную кнопку
# задаем сеточную конфигурацию окна
for c in range(2): window.columnconfigure(index=c, weight=1)
for r in range(2): window.rowconfigure(index=r, weight=1)
btn1 = Button(window, text='Кнопка 1', font=('Arial', 15))
# располагаем кнопку на окне с помощью метода grid()
btn1.grid(row=0, column=0)
btn2 = Button(window, text='Кнопка 2', font=('Arial', 15))
btn2.grid(row=0, column=1, rowspan=2)
btn3 = Button(window, text='Кнопка 3', font=('Arial', 15))
btn3.grid(row=1, column=0)
# запускаем цикл обработки событий
window.mainloop() 