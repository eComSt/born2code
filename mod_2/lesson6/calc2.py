try:  # код, где потенциально может возникнуть ошибка
    num_1 = int(input())
    num_2 = int(input())
    result = num_1 / num_2
except ZeroDivisionError: # обработка ошибки деления на ноль
    print('Возникла ошибка на ноль делить нельзя')
except ValueError: # обработка ошибки неверного ввода
    print('Возникла ошибка ввода')
else:
    print(result)