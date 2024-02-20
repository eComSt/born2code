class BaseHuman:
    def __init__(self, name, age): # инициализатор класса
        self.name = name    # имя
        self.age = age      # возраст

    def introduce(self):    # вывод информацию об имени и возрасте
        print(f'Привет, меня зовут {self.name}!')
        print(f'Мой возраст: {self.age}')

# Создаем класс для моделирования программиста
# Создаем класс для моделирования программиста 

class Programmer(BaseHuman):		
    def __init__(self, name, age, language): 
        # self.name = name         # имя
        # self.age = age           # возраст  
        super().__init__(name, age)
        self.language = language # язык программирования
    def coding(self):
        print(f'Программист {self.name} сейчас пишет код на {self.language}!')


human = BaseHuman(name='Миша', age=25) 
proger = Programmer(name='Дима', age=26, language='Python') 
proger.coding() 
