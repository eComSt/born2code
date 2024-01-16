summ,candys = 0, 0
with open('data.txt','r') as File: 
    for line in File:
        try: num = int(line.strip())
        except ValueError: candys += 1
        else: summ += num  
print(f"Сумма чисел: {summ},кол-во шоколадок = {candys}")

# sum_numbers = 0
# sum_chocolate_bars = 0
# with open('data.txt', 'r') as file:
#     for line in file:
#         line = line.strip() # удаляем лишние пробелы и табуляции
#         try:
#             number = int(line)
#             sum_numbers += number
#         except ValueError: 
#             sum_chocolate_bars += 1
# print(f'Сумма чисел: {sum_numbers}')
# print(f'Количество будущих шоколадных батончиков: {sum_chocolate_bars}')