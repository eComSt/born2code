class BaseHuman:
    def __init__(self, name, age): # инициализатор класса
        self.name = name    # имя
        self.age = age      # возраст

    def introduce(self):    # вывод информацию об имени и возрасте
        print(f'Привет, меня зовут {self.name}!')
        print(f'Мой возраст: {self.age}')

# Создаем класс для моделирования программиста
class Programmer(BaseHuman): # Наследуемся от класса BaseHuman
    pass
human = BaseHuman(name='Миша', age=25)      # экземпляр класса
proger = Programmer(name='Дима', age=26)     # экземпляр класса 
human.introduce() # вызовы метода introduce()
proger.introduce()
