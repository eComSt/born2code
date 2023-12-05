import os
import random
import time



"""
try:
    data = open('gamedata.txt', 'x')
except FileExistsError as e:
    print('Данный файл существует')
else:
    with data:
        print('Такого файла нет')
        data = open('gamedata.txt', 'w')
        data.write('\n0')
        data.write('\n0')
        data.write('\n0')
        data.close()
"""

try:
    from msvcrt import getch
except ImportError:
    import sys
    import tty, termios
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def stop(symbol, message):
    while True:
        print(message)
        if getch() == symbol:
            break

os.system('cls')

start = input('Добро пожаловать!\nДля входа введите "1", для регистрации введите "2" >> ')

start = int(start)

if start == 1:
    os.system('cls')
    print('Вход')
    print()

    while True:
        dataname = input('Введите ваш логин >> ')
        try:
            data = open(dataname + '.txt', 'r')
        except FileNotFoundError as e:
            print('Аккаунт не найден. Попробуйте ещё раз')
            time.sleep(1)
            os.system('cls')
            continue
        else:
            with data:
                print('Логин принят\n')
                datapass = input('Введите ваш пароль >> ')
                data = open(dataname + '.txt', 'r')
                check = data.readline()
                data.close()
                check = check[:-1]
                if check == datapass:
                    print('Данные приняты, приятного пользования!')
                    time.sleep(1)
                    os.system('cls')
                    save = open(dataname + '.txt', 'r')
                    break
                elif check != datapass:
                    print('Пароли не совпадают, данные отклонены!')
                    time.sleep(1)
                    continue

elif start == 2:
    os.system('cls')
    print('Регистрация')
    print()

    while True:
        dataname = input('Введите ваш логин >> ')
        try:
            data = open(dataname + '.txt', 'x')
        except FileExistsError as e:
            print('Логин занят, попробуйте ещё раз.')
            time.sleep(1)
            os.system('cls')
            continue
        else:
            with data:
                print('Логин принят\n')
                datapass = input('Введите ваш пароль (Для сохранности данных вводите только английские буквы и цифры) >> ')
                data.write(datapass)
                data.write('\n0\n0\n0\nX')
                data.close()
                print('Аккаунт создан, проверка данных...')
                data = open(dataname + '.txt', 'r')
                check = data.readline()
                data.close()
                check = check[:-1]
                if check == datapass:
                    print('Данные приняты и сохранены.')
                    time.sleep(1)
                    os.system('cls')
                    save = open(dataname + '.txt', 'r')
                    break
                else:
                    print(len(check), len(datapass))

skip = save.readline()
win = save.readline()
lose = save.readline()
draw = save.readline()
a1 = save.readline()
save.close()

#Достижения
a1 = str(a1)

print(skip, win, lose, draw , a1)

win = int(win)
lose = int(lose)
draw = int(draw)

os.system('cls')
while True:
    os.system('cls')
    menu = input('(1) Начать игру\n(2) Перейти в меню достижений\n(3) Сохранить данные и выйти из программы\n>>> ')
    menu = int(menu)
    if menu == 1:
        while menu == 1:
            os.system('cls')
            print('Добро пожаловать в игру "Камень, Ножницы, Бумага!"')

            print('')

            print('Пожалуйста сделайте выбор: Камень (1), Ножницы (2) или Бумага (3)?')

            plr = input('Ваш выбор >> ')
            plr = int(plr)

            print('')

            if plr == 1:
                print('Вы выбрали Камень!')
            elif plr == 2:
                print('Вы выбрали Ножницы!')
            elif plr == 3:
                print('Вы выбрали Бумагу!')
            elif plr != (1 or 2 or 3):
                print('Ответ не принят. Доступные ответы: 1, 2, 3!')
                break

            rnd = random.randint(1, 3)
            rnd = int(rnd)

            print('Система также сделала свой выбор!')

            print('')

            print('Камень, Ножницы, Бумага...')
            time.sleep(0.2)
            print('Раз...')
            time.sleep(0.2)
            print('Два...')
            time.sleep(0.2)
            print('Три..!')

            print('')

            if plr == rnd:
                draw += 1
            elif plr == 1 and rnd == 2:
                win += 1
            elif plr == 1 and rnd == 3:
                lose += 1
            elif plr == 2 and rnd == 1:
                lose += 1
            elif plr == 2 and rnd == 3:
                win += 1
            elif plr == 3 and rnd == 1:
                win += 1
            elif plr == 3 and rnd == 2:
                lose += 1

            print('')

            if win >= 1 and a1 != 'V':
                print('Получено новое достижение!')
                win10toast.ToastNotifier().show_toast('Получено достижение', '"Первая победа!"')
                a1 = 'V'

            os.system('cls')

            print('Результат:')

            if plr == rnd:
                print('Система сделала тот же выбор, что и вы! \nНичья!')
            elif plr == 1 and rnd == 2:
                print('Система выбрала Ножницы! Камень сломал Ножницы. \nВы победили!')
            elif plr == 1 and rnd == 3:
                print('Система выбрала Бумагу! Бумага накрыла Камень. \nВы проиграли!')
            elif plr == 2 and rnd == 1:
                print('Система выбрала Камень! Камень сломал Ножницы. \nВы проиграли!')
            elif plr == 2 and rnd == 3:
                print('Система выбрала Бумагу! Ножницы разрезали Бумагу. \nВы победили!')
            elif plr == 3 and rnd == 1:
                print('Система выбрала Камень! Бумага накрыла Камень. \nВы победили!')
            elif plr == 3 and rnd == 2:
                print('Система выбрала Бумагу! Ножницы разрезали Бумагу. \nВы проиграли!')

            print('')

            print(f'На данный момент у вас: \n{win} побед \n{lose} поражений \n{draw} ничей\n')

            ge = input('Желаете повторить? (д/н) >> ')
            if ge == 'д':
                os.system('cls')
                continue
            elif ge == 'н':
                break
            elif ge == 'cmd':
                os.system('cls')
                admpass = input('Введите пароль >> ')
                admacc = True
                if admpass == 'ItsuneADM':
                    print('Доступ разрешён.')
                    while admacc == True:
                        admint = input('cmd >> ')
                        if admint == 'cd':
                            win = 0
                            lose = 0
                            draw = 0
                        elif admint == 'win 5':
                            win += 5
                        elif admint == 'lose 5':
                            lose += 5
                        elif admint == 'draw 5':
                            draw += 5
                        elif admint == 'win -5':
                            if win < 5:
                                win = 0
                            else:
                                win -= 5
                        elif admint == 'lose -5':
                            if lose < 5:
                                lose = 0
                            else:
                                lose -= 5
                        elif admint == 'draw -5':
                            if draw < 5:
                                draw = 0
                            else:
                                draw -= 5
                        elif admint == 'stop':
                            admacc = False
                    break
                else:
                    print('Доступ закрыт.')
            elif ge != ('д' or 'н' or 'cmd'):
                print('Ответ не принят. Доступные ответы: д, н!')
                break
    elif menu == 2:
        while menu == 2:
            os.system('cls')
            print('Добро пожаловать в меню достижений!')
            print('"V" - достижение открыто, "X" - достижение заблокировано.\n')
            print('Первая победа! - ' + a1 + '\n (Победите 1 раз)')
            emenu = input('Для выхода в меню нажмите Enter ')
            if emenu == '':
                break
            elif emenu != '':
                continue
    elif menu == 3:
        break
    elif menu != (1 or 2 or 3 or 4):
        continue

os.system('cls')

savew = open(dataname + '.txt', 'w')
savew.write(datapass)
savew.write('\n' + str(win) + '\n' + str(lose) + '\n' + str(draw) + '\n'+ a1)
savew.close()

stop(b'\r', 'Нажмите Enter, чтобы закрыть консоль!') # Первым параметром нужный вам символ
