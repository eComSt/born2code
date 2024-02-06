class Car: #создаем класс для моделирования автомобиля
    def __init__(self, color, model, speed=0): #инициализатор класс
        self.color = color #публичное поле
        self._speed = speed #защищенное поле
        self.__model = model #приватное поле

    def show_info(self): #метод для вывода информации о полях на экран
        print(f'Цвет:{self.color}')
        print(f'Текущая скорость:{self._speed}')
        print(f'Модель:{self.__model}')
        
    def get_model(self): #геттер для получения значения __model
        return self.__model
    
    def set_speed(self, new_speed):#сеттер для обновления значения _speed
        if new_speed >= 0 and new_speed <300:
            self._speed = new_speed
        else:
            print('неверное значение скорости')
    def get_speed(self):#геттер для получения значения _speed
        return self._speed
    
my_car = Car(color='Синий', speed=10, model='Skyline')#создаем объект класса Car
my_car.set_speed(123)
print(my_car.get_speed())

# my_car.show_info()