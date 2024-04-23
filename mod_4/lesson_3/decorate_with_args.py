def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(10):
            func(*args, **kwargs) # вызываем функцию с передачей аргументов
    return wrapper
@repeat # указываем, какая функции будет обертывать message
def message(name):
    print(f'Привет, {name}!')

@repeat
def message2():
    print(f'Привет!')

message2()
message("dfdfdsf")