from abc import ABC, abstractmethod
class Figure(ABC): # класс, описывающий фигуру
    @abstractmethod
    def get_area(self): # метод для получения площади фигуры
        pass
    @abstractmethod
    def get_perimeter(self): # метод для получения площади фигуры
        pass