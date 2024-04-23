def decorator(func):
    def wrapper():
        print('Начало работы функции')
        func()
        print('Конец работы функции')
    return wrapper

@decorator
def hello():  
    print('Приветствую в своей программе')

# hello = decorator(hello)
# decorated_decorated_hello = decorator(decorated_hello)
# decorated_decorated_hello()

hello()