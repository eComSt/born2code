class Car:
        # инициализатор класса
        def __init__(self, color, model, speed):
            self.color = color  # цвет
            self.model = model  # модель
            self.speed = speed  # скорость

# создаем объект класса Car 
my_car = Car('Белый', 'Camry', 100)
print(my_car)           # выводим адрес объекта в терминал
print(my_car.__dict__)  # получаем локальные свойства объекта