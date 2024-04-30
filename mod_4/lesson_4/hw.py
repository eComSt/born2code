# def is_even_sum(f):
#     def wrapper(*args):
#         return f(*args) % 2 == 0
#     return wrapper


# @is_even_sum
# def get_sum(*args):
#     return sum(args)

# print(get_sum(1, 2, 3, 4, 5))
import time

from functools import lru_cache

# @lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(40))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")
# The execution time: 0.18129450 seconds