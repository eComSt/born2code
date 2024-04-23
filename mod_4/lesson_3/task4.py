def up(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
def warning(func):
    def wrapper(*args, **kwargs):
        return f'Вы получили сообщение: {func(*args, **kwargs)}'
    return wrapper 


@warning
@up
def send_message(gift):
    return f'Мне на день рождения подарили {gift}'

print(send_message('NICHEGO'))