import customtkinter as ctk
import random

# Укажите цвета, которые будут использоваться для квадратиков
colors = ["red", "blue", "green", "yellow", "purple", "orange", "lightblue", "lightgreen"]

# Укажите количество квадратиков
squares = 100

# Размеры окна
winx = 1280
winy = 720

# Примечание: Если квадратиков больше цветов, то цвета будут повторяться;
# Если squares = 0, то будет учитываться все цвета (кол-во)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DragableLabel(ctk.CTkLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)
        self.random_size = random.randint(round((root.winfo_height()+root.winfo_width())/2/8), round((root.winfo_height()+root.winfo_width())/2/4))
        self.random_color = random.choice(colors)
        self.rand_x = random.randint(0, root.winfo_width() - self.random_size)
        self.rand_y = random.randint(0, root.winfo_height() - self.random_size)

    def drag_start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drag_motion(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        self.place(x=x, y=y)
        if x < 0: self.place(x=0)
        elif x > root.winfo_width()-self.random_size: self.place(x=root.winfo_width()-self.random_size)
        if y < 0: self.place(y=0)
        elif y > root.winfo_height()-self.random_size: self.place(y=root.winfo_height()-self.random_size)

root = ctk.CTk()
root.geometry(f"{winx}x{winy}")
root.title("Sorting Center")
root.resizable(False, False)

if squares == 0:
    for i in range(len(colors)):
        label = DragableLabel(root, text="")
        label.configure(width=label.random_size, height=label.random_size, fg_color=label.random_color)
        colors.remove(label.random_color)
        label.place(x=label.rand_x, y=label.rand_y, anchor="nw")
elif squares > len(colors):
    for i in range(squares):
        label = DragableLabel(root, text="")
        label.configure(width=label.random_size, height=label.random_size, fg_color=label.random_color)
        label.place(x=label.rand_x, y=label.rand_y, anchor="nw")
else:
    for i in range(squares):
        label = DragableLabel(root, text="")
        label.configure(width=label.random_size, height=label.random_size, fg_color=label.random_color)
        colors.remove(label.random_color)
        label.place(x=label.rand_x, y=label.rand_y, anchor="nw")

root.mainloop()
