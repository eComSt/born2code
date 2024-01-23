class Car:   # создаем класс Car
    number_of_wheels = 4
    # метод для вывода информации о свойствах класса
    def __init__(self,mark,model,color,speed = 0):
        self.mark = mark
        self.model = model
        self.color = color
        if speed<0:
            speed = 0
        self.speed = speed         # скорость
    def __del__(self):
        print("Машина уничтожена")
    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self.speed}')
    def set_power_engine(self,power_engine = 0):
        self.power_engine = power_engine # устанавливаем мощность двигателя      
        # метод для возвращения значений свойств класса
    def get_params(self):
        return (self.mark, self.model, self.color, self.speed)  
# создаем два экземпляра класса Car  
my_car_1 = Car('Mercedes', 'E200', 'black',-42)
# my_car_1.show_info()
my_car_2 = Car('Toyota', 'Corolla', 'blue')
my_car_2 = 3
# my_car_2.show_info()
# my_car_2 = Car()
# # my_car_1.power_engine = 122
# my_car_1.set_power_engine(42)
# print(my_car_1.power_engine)
# my_car_1.color = "white"
# print(my_car_1.get_params())
