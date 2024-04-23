def decorator(f):
    def wrapper():
        print('Начало работы функции')
        f()
        print('Конец работы функции')
    return wrapper

@decorator
def hello():  
    print('Приветствую в своей программе')

# decorated_hello = decorator(hello)
# decorated_decorated_hello = decorator(decorated_hello)
# decorated_decorated_hello()

hello()