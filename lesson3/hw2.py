num = 5
suggestion = int(input("Введите ваше предложение: "))
if num == suggestion:
    print("Вы угадали!")
elif num > suggestion:
    print("Мое число больше")
else:
    print("Мое число меньше")