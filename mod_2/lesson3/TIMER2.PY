import datetime, time
import customtkinter as ctk
from threading import Thread

def refresh():
    while True:
        now = datetime.datetime.now()
        NY = datetime.datetime(2024, 1 ,1)
        d = NY - now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        text.configure(text="До нового года осталось:\n{} дней {} часов {} минут {} секунд".format(d.days, hh, mm, ss))
        time.sleep(1)

Timer = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
Timer.title("Таймер до нового года")
Timer.geometry("500x100")
Timer.resizable(False, False)
text = ctk.CTkLabel(Timer, text="До нового года осталось:\n", font=('Minecraft Rus', 20), justify="center")
text.pack()
Thread(target=refresh, daemon=True).start()
Timer.mainloop()
