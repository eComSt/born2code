digital_M = 7
digital_K = int(input('Введи число: '))
count_try = 1
while digital_M != digital_K:
     digital_K = int(input('Неверно веди друое число: '))
     count_try += 1
print('Затраченно попыток:', count_try)
