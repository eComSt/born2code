def check_age(min_age):
    def decorator(func):
        def wrapper(age, *args, **kwargs):
            if age < min_age:
                return f'Извините, посещение аттракциона разрешено с {min_age} лет.'
            return func(age, *args, **kwargs)
        return wrapper
    return decorator

@check_age(16) # указываем минимальный возраст - 16 лет
def go_attraction(age, attraction):
    '''Пожелание приятного посещения аттракциона'''
    return f'Приятного посещения аттракциона: {attraction}!'

age_user = int(input('Введите ваш возраст:'))
print(go_attraction(age_user, 'Воздушный экспресс')) 