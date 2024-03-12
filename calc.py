from tkinter import * 
from tkinter import ttk
import math
#------раздел функций-------------
#Чекбокс
def chk_b_changed():
    if enabled.get() == 1:
        return 1
    else:
        return 0
    
#проверка корректности ввода чисел
def is_valid():
    f2 = number.get().isdigit() and number2.get().isdigit()
    if not f2:
        return 0
    if number.get()=='' or number2.get()=='':
        return 0
    return 1

def f_NOD(): 
    if is_valid()==0:
        return 0
    n1=int(number.get())
    n2=int(number2.get())
    while n2!=0:
        n1,n2=n2,n1%n2
    answer["text"] = str(n1)
    listbox["text"] ='Нахождение наибольшего общего делителя двух чисел \nwhile n2!=0:\n    n1, n2 = n2, n1%n2'

def f_NOK():
    if is_valid()==0:
        return 0
    n1=int(number.get())
    n2=int(number2.get())
    greater=max(n1,n2)
    while True:
        if((greater % n1 == 0) and (greater % n2 == 0)):
            lcm = greater
            break
        greater += 1
    answer["text"] = str(lcm)
    listbox["text"] ='Нахождение наименьшего общего кратного двух чисел \nwhile True:\n    if((greater % n1 == 0) and (greater % n2 == 0)):\n        lcm = greater\n        break\n    greater += 1'

def SMP():
    n1=int(number.get())
    k = 0
    for i in range(2, n1 // 2+1):
        if (n1 % i == 0):
            k = k+1
    if k <= 0:
        x="YES"
    else:
        x="NO"
    answer["text"] = x
    listbox["text"] ='Нахождение простого числа \nfor i in range(2, n1 // 2+1):\n    if (n1 % i == 0):\n        k = k+1\n   if k <= 0:\n        x="YES"\n   else:\n        x="NO"'

def f_KOLVO():
    n1=int(number.get())
    count=n1
    num=1
    kolvo=0
    while count!=0:
        if n1%num==0:
            kolvo+=1
            num+=1
        else:
            num+=1
        count-=1
           
    answer["text"] = str(kolvo)
    listbox["text"] ='Нахождение количества делителей числа \ncount=n1\nnum=1\nkolvo=0\nwhile count!=0:\n    if n1%num==0:\n        kolvo+=1\n        num+=1\n    else:\n        num+=1\n    count-=1'
    
def FIB():
    n1=int(number.get())
    a, b = 0, 1
    i = 1
    while a+b <= n1:
        a, b = b, a+b
        i += 1
    if n1 == b:
      answer["text"] = "Yes"
      listbox["text"] ="Входит ли число в последовательность чисел Фибоначчи \na, b = 0, 1\ni = 1\nwhile a+b <= n1:\n    a, b = b, a+b\n     i += 1"
    else:
      answer["text"] = "No"
      listbox["text"] ="Входит ли число в последовательность чисел Фибоначчи \na, b = 0, 1\ni = 1\nwhile a+b <= n1:\n    a, b = b, a+b\n     i += 1"

def fact(n):
    if n == 0 :
        answer["text"] = "число слишком большое"
        return 1
    else:
        return n * fact(n-1)

def KAT():
    i = int(number.get())
    if i>45:
        return 0
    x = fact(i*2)/(fact(i)*fact(i+1))
    answer["text"] = str(int(x))
    listbox["text"] ="Нахождение числа Каталана \na, b = 0, 1\ni = 1\nwhile a+b <= n1:\n    a, b = b, a+b\n     i += 1"
def ARM():
    n1=int(number.get())
    d=n1
    c=len(str(n1))
    b=[]
    while n1 > 0:
        b.append(n1%10)
        n1//=10
    b = b[::-1]
    for i in range(len(b)):
        b[i]**=c
    y=sum(b)
    if y==d:
        q="YES"
    else:
        q="NO"
    answer["text"] = q
    listbox["text"] ='Нахождение числа Армстронга \nd=n1\nc=len(str(n1))\nb=[]\nwhile n1 > 0:\n    b.append(a%10)\n   n1//=10\nb = b[::-1]\nfor i in range(len(b)):\n    b[i]**=c\ny=sum(b)\nif y==d:\n    print("YES")\nelse:\n    print("NO")'
def L_CRL():
    n1=int(number.get())
    p = 2 * math.pi * n1
    answer["text"] = str(p)
    listbox["text"] ='Нахождение длины круга \nimport math\np = 2 * math.pi * r\ns = math.pi * math.pow(r, 2)'

def S_CRL():
    n1=int(number.get())
    area = n1** 2 * math.pi 
    answer["text"] = str(area)
    listbox["text"] ='Нахождение площади круга \nimport math\narea = n1** 2 * math.pi\n'

def V_CRL():
    n1=int(number.get())
    V = (4 * math.pi * n1**3) / 3
    answer["text"] = str(V)
    listbox["text"] ='Нахождение объёма шара \nimport math\nV = (4 * math.pi * n1**3) / 3\n'
def ART():
    n1=int(number.get())
    primes = [i for i in range(n1 + 1)]
    primes[1] = 0
    i = 2
    while i <= n1:
        if primes[i] != 0:
            j = i + i
            while j <= n1:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0]
    answer["text"] = primes
    listbox["text"] ='Нахождение решето эратосфена \nprimes = [i for i in range(n1 + 1)]\nprimes[1] = 0\ni = 2\nwhile i <= n1:\n    if primes[i] != 0:\n        j = i + i\n        while j <= n1:\n            primes[j] = 0\n            j = j + i\n    i += 1\n    primes = [i for i in primes if i != 0]'

def LUKE():
    n1=int(number.get())
    if n1 <= 1:
        s = False
    if n1 == 2:
        s = True
    if n1 % 2 == 0:
        s = False
    for i in range(3, int(n1**0.5) + 1, 2):
        if n1 % i == 0:
            s = False
    s = True
    answer["text"] = str(s)
    listbox["text"] ="Нахождение числа Люка \nif n1 <= 1:\n    s = False\nif n1 == 2:\n    s = True\nif n1 % 2 == 0:\n    s = False\nfor i in range(3, int(n1**0.5) + 1, 2):\n    if n1 % i == 0:\n        s = False\ns = True"
def f_S_TRIANGLE():
    if is_valid()==0:
        return 0
    n1=int(number.get())
    n2=int(number2.get())
    S=n1*n2/2
    if S%1==0:
        S=int(S)
        answer["text"] = str(S)
        listbox["text"] ="Нахождение площади треугольника \nS=n1*n2/2"
    else:
        answer["text"] = str(S)
        listbox["text"] ="Нахождение площади треугольника \nS=n1*n2/2"

def count_Mersen(p):
    n=((2**p)-1)
    return n
def MERSEN():
    p=int(number.get())
    answer["text"] = str(count_Mersen(p))
    listbox["text"] ="Нахождение числа мерсена \nn = ((2**n1)-1)"

def V_SQ():
    n1=int(number.get())
    s = round((4/3) * math.pi * n1 ** 3)
    answer["text"] = str(s)
    listbox["text"] ="Нахождение объёиа куба мерсена \ns = round((4/3) * math.pi * n1 ** 3)"

#очищение полей
def f_CLR():
    number.delete(0, END)
    number2.delete(0, END)
    answer["text"]="Ответ"
    listbox["text"]=""

#создание окна 
root = Tk()
root.geometry("650x650")
root.resizable(False, False)
root.title('Калькулятор алгоритмов')
check = (root.register(is_valid), "%P") #инициализация проверки ввода

#------раздел кнопок--------------
#кнопка НОД
btn_NOD = ttk.Button(text="НОД",command=f_NOD)
btn_NOD.place(x=40,y=80,width=109,height=40)
#кнопка НОК
btn_NOD = ttk.Button(text="НОК",command=f_NOK)
btn_NOD.place(x=160,y=80,width=109,height=40)
#кнопка проверка на простоту
btn_NOD = ttk.Button(text="ПРОСТ",command=SMP)
btn_NOD.place(x=280,y=80,width=109,height=40)
#кнопка кол-во делителей числа
btn_NOD = ttk.Button(text="КОЛ-ВО ДЕЛ",command=f_KOLVO)
btn_NOD.place(x=400,y=80,width=109,height=40)
#кнопка ФИБОНАЧЧИ
btn_NOD = ttk.Button(text="ФИБОНАЧЧИ",command=FIB)
btn_NOD.place(x=520,y=80,width=109,height=40)
#кнопка числа Каталана
btn_NOD = ttk.Button(text="КАТАЛАН",command=KAT)
btn_NOD.place(x=40,y=140,width=109,height=40)
#кнопка числа Армстронга
btn_NOD = ttk.Button(text="АРМСТРОНГ",command=ARM)
btn_NOD.place(x=160,y=140,width=109,height=40)
# кнопка длины окружности
btn_NOD = ttk.Button(text="ДЛИНА ОКРУЖ",command=L_CRL)
btn_NOD.place(x=280,y=140,width=109,height=40)
# кнопка площади круга
btn_NOD = ttk.Button(text="ПЛОЩАДЬ КРУГА",command=S_CRL)
btn_NOD.place(x=400,y=140,width=109,height=40)

# кнопка объёма шара
btn_NOD = ttk.Button(text="ОБЪЁМ ШАРА",command=V_CRL)
btn_NOD.place(x=520,y=140,width=109,height=40)

# кнопка решето эратосфена
btn_NOD = ttk.Button(text="ЭРАТОСФЕН",command=ART)
btn_NOD.place(x=40,y=200,width=109,height=40)

# кнопка числа Люка
btn_NOD = ttk.Button(text="ЧИСЛО ЛЮКА",command=LUKE)
btn_NOD.place(x=160,y=200,width=109,height=40)

# кнопка площади треугольника
btn_NOD = ttk.Button(text="ПЛОЩАДЬ ТРЕУГОЛЬНИКА",command=f_S_TRIANGLE)
btn_NOD.place(x=280,y=200,width=109,height=40)

# кнопка числа Мерсена
btn_NOD = ttk.Button(text="ЧИСЛО МЕРСЕНА",command=MERSEN)
btn_NOD.place(x=400,y=200,width=109,height=40)

# кнопка объёма куба
btn_NOD = ttk.Button(text="ОБЪЁМ КУБА",command=V_SQ)
btn_NOD.place(x=520,y=200,width=109,height=40)

#кнопка очищения полей
btn_CLR = ttk.Button(text="Очистить",command=f_CLR)
btn_CLR.place(x=40,y=580,width=109,height=40)
 
#------раздел меток--------------
answer = ttk.Label(font=("Arial", 14),text="Ответ",borderwidth=2, relief="ridge", padding=8)
answer.place(x=300,y=20,width=320,height=40)
listbox = ttk.Label(font=("Arial", 14), anchor=NW, borderwidth=2, relief="ridge", padding=8, wraplength=480)
listbox.place(x=40,y=300,width=550,height=250)

#------раздел полей--------------
number = ttk.Entry(font=("Arial", 14))
number.place(x=40,y=20,width=109,height=40)
number2 = ttk.Entry(font=("Arial", 14))
number2.place(x=170,y=20,width=109,height=40)

#----------раздел чекбокса-----------
#enabled = IntVar()
#chk_b = ttk.Checkbutton(text="Показать алгоритм", variable=enabled)
#chk_b.place(x=420,y=20,width=400,height=40)
root.mainloop()
