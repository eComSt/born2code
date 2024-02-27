class Rectangle: # класс, описывающий прямоугольник
    def __init__(self, lenght, width): # инициализатор класса
        self._lenght = lenght  # длина
        self._width = width           # ширина
    def get_area(self): # метод для получения площади прямоугольника
        return self._lenght * self._width
    def get_perimeter(self):# метод для получения периметра квадрата
                return (self._lenght + self._width) * 2
class Triangle:                 # класс, описывающий треугольник 
    def __init__(self, side1, side2, side3): # инициализатор класса
        self._side1 = side1     # первая сторона треугольника
        self._side2 = side2     # вторая сторона треугольника
        self._side3 = side3     # третья сторона треугольника
    def get_perimeter(self):    # метод для получения периметра квадрата
        return self._side1 + self._side2 + self._side3    
    def get_area(self):# получение площади треугольника по трем сторонам
        p = self.get_perimeter()/2 # полупериметр
        return (p * (p - self._side1) * (p - self._side2) * (p - self._side3))**0.5
# def area(obj):
#     return obj.get_area()
area = lambda obj: obj.get_area()
rect1 = Rectangle(4, 5)         # экземпляры класса Rectangle и Triangle
rect2 = Rectangle(8, 10)
trian1 = Triangle(7, 9,4)
trian2 = Triangle(3, 5,4)
# print(rect1.get_rectangle_area(), rect2.get_rectangle_area())
# print(trian1.get_triangle_area(), trian2.get_triangle_area())
figures = [rect1, rect2, trian1, trian2] # список с фигурами
for fig in figures:             # перебираем фигуры в списке
    # выводим на экран площадь и периметр каждой фигуры
    print(f'Площадь фигуры: {fig.get_perimeter()}')
    print(f'Периметр фигуры: {area(fig)}')