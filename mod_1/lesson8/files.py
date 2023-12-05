file = open('readme.txt', 'r')
data = file.read()
# print(data)
file.close()
file = open('readme.txt', 'r')
data = file.readline()
# print(data)
file.close()
file = open('readme.txt', 'r',encoding='utf-8')
data = file.readlines()
# print(data)
file.close()

file = open('readme.txt', 'r', encoding='utf-8')
summ = 0
for line in file:
    summ += int(line)
# print(sum)
file.close()
file = open('readme.txt', 'r', encoding='utf-8')
lst = []
for line in file:
    lst.append(int(line))
# print(lst)
# print(sum(lst))
file.close()

# with open('file2.txt', 'w') as file:
#     file.write('Hello, World!')
    
file = open('file2.txt', 'a')
file.write('Are hear mi???!!!!!!\n')
file.close()
#file: nums.txt записать туда целые числа от 1 до 20 включительно
# каждое число с новой строки
from time import sleep

# for i in range(1, 21):
#     file = open('nums.txt', 'w')
#     file.write(f'{i}\n')
#     file.close()
#     sleep(1)


from random import randint
N = randint(10,100)
file = open('rand_nums.txt', 'w+')
for i in range(N):
    digit = randint(0, 100)
    file.write(f'{digit}\n')
file.seek(0)
num = []
for line in file:
    num.append(int(line))
# print(max(num),min(num),sum(num))
file.close()

# def f(x,z = 3):
#     y = x*x+z*2
#     return y

# ans = f(5)
# print(ans)
dct = {"a":5,"b":6,"c":7}
for i in dct.items():
    print(i)
    print(i[0])
    print(i[1])