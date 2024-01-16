class SportCar:
    mark = ""
    color = ""
    model = "" 
    max_speed = ""
cars = []
for _ in range (3):
      car = SportCar()
      car.mark = input()
      car.color = input()
      car.model = input ()
      car.max_speed = input (int())
      cars.append(car)
      print('-------------------')
print('Машины в автопарке')
for car in cars:
    print(f'Марка: {car.mark}, цвет: {car.color}, модель: {car.model}, максимальная скорость: {car.max_speed}')