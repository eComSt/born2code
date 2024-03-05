import customtkinter as ctk
from threading import Thread
from time import sleep

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("300x400")
root.title("Clicker")
root.resizable(False, False)

class Player:
    def __init__(self, clk, mltp, coinspc):
        self.clk = clk
        self.mltp = mltp
        self.coinspc = coinspc
        self.coins = 0

        self.clkup = 10
        self.mltpup = 100
        self.coinspcup = 50

        self.clkup_changed = False
        self.mltpup_changed = False

    def total(self):
        return self.clk * self.mltp

class Enemy:
    def __init__(self, hp, user):
        self.hp = hp
        self.maxhp = hp
        self.user = user

    def destroy(self, coins):
        self.user.coins += self.user.coinspc
        coins.configure(text=f"Coins: {round(self.user.coins)}")
        if self.user.clkup_changed:
            newhp = self.maxhp * (1+self.user.mltp/10)/2
            self.user.clkup_changed = False
        elif self.user.mltpup_changed:
            newhp = 10
            self.user.mltpup_changed = False
        else:
            newhp = self.maxhp * (1+self.user.clk/10)

        e = Enemy(newhp, self.user)
        e.show(coins)

    def click(self, btn, coins):
        if self.hp > self.user.total():
            self.hp -= self.user.total()
            percent = int(self.hp / self.maxhp * 100)
            btn.configure(text=f"{percent}%", width=percent/100*150+100, height=percent/100*150+100, font=("Times New Roman", percent/100*45+25))
        else:
            btn.destroy()
            self.destroy(coins)

    def show(self, coins):
        percent = int(self.hp / self.maxhp * 100)
        btn = ctk.CTkButton(root, text=f"{percent}%", command=lambda: self.click(btn, coins), font=("Times New Roman", 70))
        btn.configure(width=250, height=250)
        btn.place(relx=0.5, rely=0.5, anchor="center")

p = Player(1, 1, 1)
e1 = Enemy(10, p)

coins = ctk.CTkLabel(root, text=f"Coins: {p.coins}", font=("Times New Roman", 25))
coins.place(relx=0.5, rely=0.1, anchor="center")

btn_bg = ctk.CTkFrame(root, width=260, height=260)
btn_bg.place(relx=0.5, rely=0.5, anchor="center")
def shop_f():
    global coins

    shop_btn.configure(state="disabled")

    def shop_close():
        shop_btn.configure(state="normal")
        shop.destroy()

    shop = ctk.CTkToplevel(root)

    shop.title("Shop")

    shop.geometry(f"500x180")
    shop.resizable(False, False)
    coins_p_c = ctk.CTkLabel(shop, text=f"Coins per click: {p.coinspc}", font=("Times New Roman", 18))
    clicks_p_c = ctk.CTkLabel(shop, text=f"Clicks per click: {p.clk}", font=("Times New Roman", 18))
    mult_p_c = ctk.CTkLabel(shop, text=f"Multiplier: {p.mltp}", font=("Times New Roman", 18))

    def cpc():
        if p.coins >= p.coinspcup:
            p.coinspc += 1
            p.coins -= p.coinspcup
            p.coinspcup *= 2
            coins_p_c.configure(text=f"Coins per click: {round(p.coinspc)}")
            coins_p_c_btn.configure(text=f"Upgrade ({round(p.coinspcup)} Coins)")
            coins.configure(text=f"Coins: {round(p.coins)}")
        else:
            pass

    def clk():
        if p.coins >= p.clkup:
            p.clk += 1
            p.coins -= p.clkup
            p.clkup *= 1.2
            p.clkup_changed = True
            clicks_p_c.configure(text=f"Clicks per click: {round(p.clk)}")
            clicks_p_c_btn.configure(text=f"Upgrade ({round(p.clkup)} Coins)")
            coins.configure(text=f"Coins: {round(p.coins)}")
        else:
            pass

    def mltp():
        if p.coins >= p.mltpup:
            p.mltp += 0.5
            p.coins -= p.mltpup
            p.mltpup **= 1.5
            p.mltpup_changed = True
            mult_p_c.configure(text=f"Multiplier: {round(p.mltp)}")
            mult_p_c_btn.configure(text=f"Upgrade ({round(p.mltpup)} Coins)")
            coins.configure(text=f"Coins: {round(p.coins)}")
        else:
            pass

    coins_p_c_btn = ctk.CTkButton(shop, text=f"Upgrade ({round(p.coinspcup)} Coins)", command=cpc, font=("Times New Roman", 18), width=180)
    clicks_p_c_btn = ctk.CTkButton(shop, text=f"Upgrade ({round(p.clkup)} Coins)", command=clk, font=("Times New Roman", 18), width=180)
    mult_p_c_btn = ctk.CTkButton(shop, text=f"Upgrade ({round(p.mltpup)} Coins)", command=mltp, font=("Times New Roman", 18), width=180)



    coins_p_c_btn.place(relx=0.8, rely=0.3, anchor="center")
    clicks_p_c_btn.place(relx=0.8, rely=0.5, anchor="center")
    mult_p_c_btn.place(relx=0.8, rely=0.7, anchor="center")

    coins_p_c.place(relx=0.4, rely=0.3, anchor="center")
    clicks_p_c.place(relx=0.4, rely=0.5, anchor="center")
    mult_p_c.place(relx=0.4, rely=0.7, anchor="center")

    shop.protocol("WM_DELETE_WINDOW", shop_close)

shop_btn = ctk.CTkButton(root, text="Shop", font=("Times New Roman", 25), width=220, command=shop_f)
shop_btn.place(relx=0.5, rely=0.9, anchor="center")

e1.show(coins)

def autoclick():
    while True:
        sleep(1)
        p.coins += p.clk * p.mltp
        coins.configure(text=f"Coins: {round(p.coins)}")

Thread(target=autoclick).start()

root.mainloop()