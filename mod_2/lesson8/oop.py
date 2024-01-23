class Car:   # создаем класс Car
    mark = 'BMW'   # марка
    model = 'x5' # модель
    color = 'blue'    # цвет
    speed = 0         # скорость
    # метод для вывода информации о свойствах класса
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
my_car_1 = Car()
my_car_2 = Car()
# my_car_1.power_engine = 122
my_car_1.set_power_engine(42)
print(my_car_1.power_engine)
my_car_1.color = "white"
print(int.__dict__)
