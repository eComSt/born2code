def show_info(data:list):
    print(f'сумма: {sum(data)}')
    print(f'Средняя арифм: {sum(data) / len(data)}')
    print(f'Маскимальное значение: {max(data)}')
    print(f'Минимальное значение {min(data)}')
    print(f"Количество значений: {len(data)}")
show_info([7,2,4,2,3,4,8,3,6,42])
