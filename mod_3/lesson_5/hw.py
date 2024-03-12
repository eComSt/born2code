import tkinter as tk
import random

def change_color_and_move():
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    button.config(bg=random_color)
    x = random.randint(0, 250)
    y = random.randint(0, 250)
    button.place(x=x, y=y)

window = tk.Tk()
window.title("Кликер")
window.geometry("750x750")

button = tk.Button(window, text="Нажми меня", command=change_color_and_move)
button.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()