class Car:
        # def __new__(cls, *args, **kwargs): 
        #     print(f'Работает метод __new__() для класса {cls}')
        #     print(args)
        #     print(kwargs)
        #     # возвращаем новый, неинициализированный объект
        #     return super().__new__(cls) 
        def __init__(self, color, model, speed):
            self.color = color  # цвет
            self.model = model  # модель
            self.speed = speed  # скорость

# создаем объект класса Car 
my_car = Car('Белый', 'Camry', 100)
#  создаем объект класса Car с именованными аргументами
my_car = Car('Белый', model='Camry', speed=100) 
print(my_car)               # выводим адрес объекта в терминал