from tkinter import *
def check():
    # получение и вывод информации из виджетов с помощью метода get()
    print(name.get(), selected.get(), age.get(), check_state.get())
    # меняем значение атрибута text 
    label.configure(text=f'Спасибо, {name.get()}')
# создаем и настраиваем главное окно
window = Tk()
window.geometry('700x500')
window.title('Анкета')
# создаем и размещаем надпись "Расскажите о себе"
label = Label(text='Расскажите о себе', font=('Arial', 20))
label.place(x=200, y=10)
about = Message(text='''Мы рады приветствовать вас в нашей анкете 
дружбы! Пожалуйста, отвечайте на вопросы честно, вся информация 
останется между нами.''', font=('Arial', 14), width=680)
about.configure(justify=CENTER)
about.place(x=5, y=70)
check_state = IntVar()                                         
check_bnt = Checkbutton(text='Запомнить меня', variable=check_state) 
check_bnt.place(x=10, y=350)      
# создаем и размещаем поле для ввода ФИО
name = Entry(width=30)
name.place(x=70, y=155)
# создаем и размещаем подпись для поля ввода
label_name = Label(text='ФИО: ', font=('Arial', 15))
label_name.place(x=5, y=150)
selected = IntVar()
# создаем и размещаем радиокнопки для возможности указания пола 
rad1 = Radiobutton(text='Мужской', value=1, variable=selected) 
rad2 = Radiobutton(text='Женский', value=2, variable=selected)
rad1.place(x=10, y=200)
rad2.place(x=100, y=200) 

# создаем и размещаем подпись с текстом "Сколько вам лет?"
label_age = Label(text='Сколько вам лет? ', font=('Arial', 15))
label_age.place(x=5, y=250)
# создаем и размещаем виджет для указания возраста
age = Spinbox(from_=0, to=100, width=20)
age.place(x=10, y=300)
check_state = IntVar()    
# IntVar() для создания группы из одного чек-бокса
                                
btn = Button(text='Отправить', 
             font=('Arial', 10), bg='green', command=check)                                            
btn.place(x=100, y=400)
# запускаем цикл обработки событий
window.mainloop() 