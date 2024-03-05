import customtkinter as ctk
import random

# Укажите цвета, которые будут использоваться для квадратиков
colors = ["red", "blue", "green", "yellow", "purple", "orange", "lightblue", "lightgreen"]

# Размеры окна
winx = 1280
winy = 720

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def near_obj_check(x, y):
    for obj in root.winfo_children():
        if obj.winfo_x() <= x <= obj.winfo_x() + obj.winfo_width() and obj.winfo_y() <= y <= obj.winfo_y() + obj.winfo_height():
            return obj

class DragableLabel(ctk.CTkLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)
        self.bind("<Button-3>", self.delete)
        self.random_size = 100
        self.random_color = random.choice(colors)
        self.rand_x = random.randint(0, root.winfo_width() - self.random_size)
        self.rand_y = random.randint(0, root.winfo_height() - self.random_size)

        self.right_side = self.winfo_x() + self.winfo_width()
        self.bottom_side = self.winfo_y() + self.winfo_height()
        self.left_side = self.winfo_x()
        self.top_side = self.winfo_y()

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

    def delete(self, event):
        self.destroy()

class InInventoryLabel(ctk.CTkLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)
        self.width = 100
        self.height = 100
        self.fg_color = random.choice(colors)
        self.__new_object = None
        self.start_x = self.winfo_x()
        self.start_y = self.winfo_y()

    def drag_start(self, event):
        self.__new_object = DragableLabel(root, text="", width=self.width, height=self.height, fg_color=self.fg_color)
        self.__new_object.place(x=self.winfo_x(), y=self.winfo_y())
        self.start_x = event.x
        self.start_y = event.y

    def drag_motion(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y

        self.__new_object.place(x=x, y=y)

        if x < 0: self.__new_object.place(x=0)
        elif x > root.winfo_width()-100: self.__new_object.place(x=root.winfo_width()-100)
        if y < 0: self.__new_object.place(y=0)
        elif y > root.winfo_height()-100: self.__new_object.place(y=root.winfo_height()-100)

root = ctk.CTk()
root.geometry(f"{winx}x{winy}")
root.title("Sorting Center")
root.resizable(False, False)

for i in range(0, 7):
    InInvD = InInventoryLabel(root, text="")
    InInvD.configure(width=InInvD.width, height=InInvD.height, fg_color=InInvD.fg_color)
    InInvD.place(x=100*i+50*i, y=50, anchor="nw")
    colors.remove(InInvD.fg_color)

root.mainloop()