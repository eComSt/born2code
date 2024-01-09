from functools import reduce #подключаем функцию reduce() 
numbers = [1, 2, 3, 4, 5,6,7,8,42] #задаем список с числами
#в переменной mult сохраняем произведение элементов списка numbers
mult = reduce(lambda x, y: x * y, numbers)
print(mult)