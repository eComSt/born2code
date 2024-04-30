# fib(1) = 1
# fib(2) = 1
# fib(3) = fib(1)+fib(2) = 2
# fib(4) = 3
# fib(5) = 5
# fib(n) = fib(n-2)+fib(n-1)
from time import time
from functools import lru_cache
# def cache(func):
#     data = {}
#     def wrapper(n):
#         if n not in data: data[n] = func(n)
#         return data[n]
#     return wrapper 

# @cache
@lru_cache(maxsize=None)
def fib(n):
    return 1 if n<3 else fib(n-2)+fib(n-1)

start = time()
print(fib(35))
end = time()
print('Время выполнения: {} секунд.'.format(end-start))