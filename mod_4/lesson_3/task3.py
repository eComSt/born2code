def access(func):
    def wrapper(*args, **kwargs):
        # Проверка уровня доступа из kwargs
        if kwargs.get('password') == '12345qwerty':
            return f"Доступ разрешён. {func(*args, **kwargs)}"
        else:
            return "Доступ запрещён. Введен неверный пароль."
    return wrapper
@access
def send_message(message, **kwargs):
    return f"Сообщение: {message}"
user_password = input("Введение пароль:")
result = send_message("Очень важная информация!", password=user_password)
print(result)