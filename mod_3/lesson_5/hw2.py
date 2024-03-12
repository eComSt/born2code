import tkinter as tk    
import random

def change_color_and_position():
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    new_color = random.choice(colors)
    button.config(bg=new_color)
    
    new_x = random.randint(0, 400) # случайное положение по оси X
    new_y = random.randint(0, 300) # случайное положение по оси Y
    button.place(x=new_x, y=new_y)

window = tk.Tk()
window.title("Кликер")

button = tk.Button(window, text="Нажми меня", command=change_color_and_position, bg='blue', fg='white', font=('Arial', 12))
button.place(x=150, y=100)

window.geometry("400x300")
window.mainloop()