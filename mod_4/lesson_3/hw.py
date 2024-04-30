# def is_even_sum(func):
#     def wrapper(*args): 
#         return func(*args) % 2 == 0
#     return wrapper
# def is_even_sum(func):
    # return lambda *args: f(*args)  % 2 == 0
is_even_sum  = lambda f: lambda *args: f(*args)  % 2 == 0

@is_even_sum
def get_sum(*args):
    return sum(args)
print(get_sum(1, 2, 3, 4))
