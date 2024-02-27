class Rectangle: # класс, описывающий прямоугольник
    def __init__(self, lenght, width): # инициализатор класса
        self._lenght = lenght  # длина
        self._width = width           # ширина
    def get_area(self): # метод для получения площади прямоугольника
        return self._lenght * self._width 
class Triangle:                 # класс, описывающий треугольник 
    def __init__(self, base, height):  # инициализатор класса
        self._base = base       # основание
        self._height = height        # высота
    def get_area(self):#  метод для получения площади треугольника
        return 0.5 * self._base * self._height
# def area(obj):
#     return obj.get_area()
area = lambda obj: obj.get_area()
rect1 = Rectangle(4, 5)         # экземпляры класса Rectangle и Triangle
rect2 = Rectangle(8, 10)
trian1 = Triangle(7, 9)
trian2 = Triangle(3, 5)
# print(rect1.get_rectangle_area(), rect2.get_rectangle_area())
# print(trian1.get_triangle_area(), trian2.get_triangle_area())
figures = [rect1, rect2, trian1, trian2] # список с фигурами
for fig in figures:             # перебираем фигуры в списке
    # выводим на экран площадь каждой фигуры
    print(f'Площадь фигуры: {fig.get_area()}')
    print(f'Площадь фигуры: {area(fig)}')