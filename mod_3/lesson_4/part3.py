from figure2 import Figure
class Rectangle(Figure): # класс, описывающий прямоугольник
    def __init__(self, lenght, width): # инициализатор класса
        self._lenght = lenght  # длина
        self._width = width           # ширина
    def get_area(self): # метод для получения площади прямоугольника
        return self._lenght * self._width
    def get_perimeter(self):# метод для получения периметра квадрата
                return (self._lenght + self._width) * 2
class Triangle(Figure):                 # класс, описывающий треугольник 
    def __init__(self, side1, side2, side3): # инициализатор класса
        self._side1 = side1     # первая сторона треугольника
        self._side2 = side2     # вторая сторона треугольника
        self._side3 = side3     # третья сторона треугольника
    def get_perimeter(self):    # метод для получения периметра квадрата
        return self._side1 + self._side2 + self._side3    
    def get_area(self):# получение площади треугольника по трем сторонам
        p = self.get_perimeter()/2 # полупериметр
        return (p * (p - self._side1) * (p - self._side2) * (p - self._side3))**0.5
class Circle(Figure):
    def __init__(self, radius): # инициализатор класса
        self._radius = radius   # радиус
circ = Circle(8) # экземпляр класса Circle
#3000 строк кода
print(circ.get_area()) # выводим на экран площадь круга
print(circ.get_perimeter())# выводим на экран периметр фигуры

