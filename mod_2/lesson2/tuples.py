objects_tuple = tuple()

objects_tuple = ()
objects_tuple = (1, 2, 3)
# print(objects_tuple)
objects_tuple = tuple([1, 2, 3])
# print(objects_tuple)
# print(type(objects_tuple))

objects_tuple = (1, 2, 3)
first_elem = objects_tuple[2]
# print(first_elem)

objects_tuple = (1, 2, 3)
# objects_tuple[0] = 5
# print(objects_tuple)
# len(objects_tuple)
# print(objects_tuple.count(1))
# print(objects_tuple.index(1))
objects_tuple = (1, 2, 3)
first, second, third = objects_tuple
# print(first, second)
# for i in objects_tuple:
#     print(i)
    
    
first_tuple = (1, 2, 3,4,5)
second_tuple = (3, 4, 5,6,7)
third_tuple =  second_tuple[1:4:2] + first_tuple[1:4:2]
# print(third_tuple)
# def func(a, b, c):
#     print(a, b, c)

# objects_tuple = (1, 2, 3)

# func(objects_tuple)
# func(objects_tuple[0], objects_tuple[1], objects_tuple[2])

def func(a, b, c):
    summa = a + b + c
    diff = a - b - c
    return summa, diff
objects_tuple = (1, 2, 3)
result = func(*objects_tuple)
result_summ,result_dif = func(*objects_tuple)
# print(result_summ,result_dif)

my_tuple =(1,2,4,5,3,2,42)
	
# if my_tuple:
#     print('Кортеж не пустой')
# else:
#     print('Кортеж пустой')
my_tuple = (1,)
# print(my_tuple)
tuple_with_lists = ([1, 2, 3], [4, 5, 6])
first = tuple_with_lists[0]
second = tuple_with_lists[1]
second.append(4242)
tuple_with_lists[0].append(42)
print(tuple_with_lists)

