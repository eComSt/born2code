def separator(sym = '', count = 0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # print(sym * count)
            # result = func(*args, **kwargs)
            # return result
            return f'{sym * count}\n{func(*args, **kwargs)}'
        return wrapper
    return decorator

@separator('-', 20)
def say_hello(name):
    return f'Добрый день, {name}'
# say_hello = separator('-', 20)(say_hello)

@separator('+', 30)
def say_bye(name):
    return f'До свидания, {name}'

print(say_hello('Дима'))
print(say_bye('Дима'))