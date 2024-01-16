# ООП в Python  

# создаем класс "Автомобиль"
class Car:
    # описываем свойства класса
    mark = 'Toyota'     # марка
    model = 'Corolla'   # модель
    color = 'blue'      # цвет
    speed = 0           # скорость  

# создаем экземпляр класса Car
my_car_1 = Car()
# выводим информацию об экземпляре 
print(my_car_1)
# выводим тип экземпляра класса
print(type(my_car_1))
# выводим значение свойства model
print(f'Модель автомобиля: {my_car_1.model}')

# выводим на экран все свойства объекта my_car_1
print(f'Марка автомобиля: {my_car_1.mark}')
print(f'Модель автомобиля: {my_car_1.model}')
print(f'Цвет автомобиля: {my_car_1.color}')
print(f'Текущая скорость автомобиля: {my_car_1.speed}')

# меняем значение свойства сolor
my_car_1.color = 'red'

# создаем еще один экземпляр класса Car
my_car_2 = Car()

# выводим на экран все свойства объекта my_car_2
print(f'Марка автомобиля: {my_car_2.mark}')
print(f'Модель автомобиля: {my_car_2.model}')
print(f'Цвет автомобиля: {my_car_2.color}')
print(f'Текущая скорость автомобиля: {my_car_2.speed}')

# меняем значение свойства model 
my_car_2.model = 'Tundra'

# ---------------------------------------------------------------

# Задача "Автопарк спортивных машин"

# Создаем класс SportCar
class SportCar:
    mark = ''           # марка
    model = ''          # модель
    engine_power = 0    # мощность двигателя
    max_speed = 0       # максимальная скорость

# создаем список cars для хранения объектов класс SportCar
cars = []

# цикл для создания трех экземпляр класса Car
for _ in range(3):
    # создаем экземпляр класса Car
    car = SportCar()
    # задаем значени свойств объекта
    car.mark = input('Введите марку:')
    car.model = input('Введите модель:')
    car.engine_power = int(input('Введите мощность двигателя:'))
    car.max_speed = int(input('Введите макс. скорость:'))
    # добавляем экземпляр класса Car в список
    cars.append(car)
    print('--------------------------')

# выводим на экран информацию о свойствах всех машин
print('Машины в автопарке:')
print(cars)
for car in cars:
    print(f'Марка: {car.mark}')
    print(f'Модель: {car.model}')
    print(f'Мощность двигателя: {car.engine_power}')
    print(f'Макс. скорость: {car.max_speed}')
    print('--------------------------')
