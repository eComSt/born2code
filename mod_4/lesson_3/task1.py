def repeat(func):
    def wrapper():
        for _ in range(10):
            func()
    return wrapper

@repeat # вызываем декоратор repeat
def message():
    print('Привет!')
message() # вызываем функцию message
