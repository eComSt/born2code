# lst = [i for i in range(1,11)]
# lst = []
# for i in range(1,1000001):
#     lst.append(i)
# N = int(input())
# squares = [num**2 for num in range(1, N + 1)]
# print(squares)
# symbols = [sym for sym in input()]
# symbols = list(input())
# print(symbols)
numbers = [num for num in range(100, 1001) if not num % 7]
                                        
# print(numbers)
cities = ['Самара', 'Москва', 'Анапа', 'Новосибирск', 'Архангельск', 'Екатеринбург', 'Александровск']
new_cities = [city for city in cities if len(city) > 6 and city[0] == 'А']
# print(new_cities)
cities = ['Самара', 'Москва', 'Анапа', 'Новосибирск', 'Архангельск', 'Екатеринбург', 'Александровск']
uniq_cities = [city for city in cities if len(city) == len(set(city.lower()))]
# print(uniq_cities)
# print(set('Самара'))
square_roots = {}
# for num in range(1, 21):
#     square_roots[num] = num**0.5

# print(square_roots)

square_roots = {i:i**0.5 for i in range(1, 21)}
print(square_roots)


fruits = {
    'Персики': 150,
    'Яблоки': 100,
    'Бананы': 140,
    'Лимоны': 200,
    'Авокадо': 450
}
# fruits_new = {}
# for fruit, price in fruits.items():
#     fruits_new[fruit] = price*1.2
    # fruits_new[fruit] = price * 1.2
fruits_new = {fruit:price * 1.2 for fruit, price in fruits.items()}
print(fruits_new)

# N = int(input())              # вводим размерность таблицы умножения
# table = []                    # список для хранения таблицы   
# for i in range(1, N + 1):     # перебираем числа от 1 до N (строки таблицы)
#     line = []                 # список для хранения одной строки таблицы 
#     for j in range(1, N + 1): # перебираем числа от 1 до N (столбцы таблицы)
#         line.append(i * j)    # получаем очередное число, сохраняем в список
#     table.append(line)        # добавляем готовую строку в двумерный список

# for line in table:            # проходимся по итоговому двумерному списку
#     print(line)               # выводим очередную строку таблицы на экран


N = int(input())              # вводим размерность таблицы умножения
table = [[i * j for j in range(1, N + 1)] for i in range(1, N + 1)]                     

for line in table:            
    print(line)   
    
lst = ['Apple', 'Orange', 'Banana', 'Pear']
dct = {i:len(i) for i in lst}
print(dct)
    

