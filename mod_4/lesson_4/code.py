# def my_function():
#     '''Это строка документации. Здесь можно описать назначение функции'''
#     return 'Hello, world!'

# print(my_function.__name__)
# print(my_function.__doc__)

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(price):
        '''Это строка документации декоратора'''
        return f"{func(price)} руб."
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

    # return lambda price:f"{func(price)} руб."
@decorator
def cost(price):
    '''Это строка документации. Здесь можно описать назначение функции'''
    return f'Стоимость товара: {price}'

print(cost(190))
print(cost.__doc__)
print(cost.__name__)