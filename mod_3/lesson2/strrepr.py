class Car:
        # инициализатор класса
        def __init__(self, model):
            self.model = model  # модель

        # отображения информации об объекте в понятном для пользователя виде
        def __repr__(self):
            return f'Car({self.model})'
        def __str__(self):
            return f'Модель машины1 - {self.model}'
        

my_car = Car('Camry') # создаем объект класса Car 
# print(my_car) # выводим информацию об объекте в терминал 
print(repr(my_car))