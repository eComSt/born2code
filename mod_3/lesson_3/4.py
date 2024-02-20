class BaseHuman:
    def __init__(self, name, age): # инициализатор класса
        self.name = name    # имя
        self.age = age      # возраст

    def introduce(self):    # вывод информацию об имени и возрасте
        print(f'Привет, меня зовут {self.name}!')
        print(f'Мой возраст: {self.age}')
    def walk(self):         # информирование, что человек идет на прогулку
        print(f'{self.name} идет на прогулку.')
# Создаем класс для моделирования программиста
# Создаем класс для моделирования программиста 
class Cat:
    def sleep_cat(self):
        print('Z-z-z-z')
class Programmer(BaseHuman):		
    def __init__(self, name, age, language): 
        # self.name = name         # имя
        # self.age = age           # возраст  
        super().__init__(name, age)
        self.language = language # язык программирования
    def coding(self):
        print(f'Программист {self.name} сейчас пишет код на {self.language}!')
class BackendProgrammer(Programmer,Cat):
    pass
# экземпляр класса BackendProgrammer
backproger = BackendProgrammer(name='Иван', age=27, language='C++')
backproger.walk()
backproger.sleep_cat()
proger = Programmer(name='Дима', age=26, language='Python')
print(issubclass(BackendProgrammer, Programmer))
print(issubclass(BackendProgrammer, BaseHuman))
print(BackendProgrammer.__base__)
print(BaseHuman.__base__)
print(issubclass(Programmer, object))
print(issubclass(BackendProgrammer, object))
# проверяем, что proger является экземпляром класса Programmer
print(isinstance(proger, Programmer))
# проверяем, что proger является экземпляром класса BaseHuman
print(isinstance(proger, BaseHuman))
