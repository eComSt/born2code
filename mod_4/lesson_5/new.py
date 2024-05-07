# from functools import wraps

# def decorator(func):
#     @wraps(func)
#     def wrapper(price):
#         '''Это строка документации декоратора'''
#         return f"{func(price)} руб."
#     return wrapper

# @decorator
# def cost(price):
#     '''Это строка документации. Здесь можно описать назначение функции'''
#     return f'Стоимость товара: {price}'

# print(decorator)
# # print(cost(190))
# # print(cost.__doc__)
# # print(cost.__name__)

def abc(i):
    j = i+1
    return "Hello, world!"

print(abc(5))
print(j)