from customtkinter import *



# # создаем и настраиваем главное окно
# window = CTk()
# window.title('Мое окно')
# def switch_event():
#     print("switch toggled, current value:", switch_var.get())

# switch_var = StringVar(value="on")
# switch = CTkSwitch(window, text="CTkSwitch", command=switch_event,
#                                  variable=switch_var, onvalue="on", offvalue="off")
# switch.grid(row=0,column=0)
# window.mainloop()

import customtkinter
class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()