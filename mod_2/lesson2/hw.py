original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
number_to_remove = int(input("Введите число для удаления из кортежа: "))
new_tuple = ()
for x in original_tuple:
    new_tuple += (x,) if x != number_to_remove else ()
print("Кортеж без указанного числа:", new_tuple)