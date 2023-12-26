numbs = ['4', '23', '15', '8'] #объявляем список 
max_str = '0' #контрзначение для максимального числа в виде строки
for num in numbs: #перебираем строки из списка numbs
    if int(num) > int(max_str): #если текущее «число» больше
        max_str = num #обновляем значение переменной для максимума
print(max_str) #печатаем на экран максимальное значение

numbs = ['4', '23', '15', '8']
#ищем максимальное значение через генератор списков
max_str = max([int(num) for num in numbs])
print(max_str)

numbs = ['4', '23', '15', '8']
#ищем максимальное значение через параметр key и lambda-функцию

max_str = max(numbs, key=lambda num: int(num))
print((max_str))
