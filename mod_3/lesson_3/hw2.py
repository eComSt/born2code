class Animal:
    def __init__(self, name, habitat):
        self._name = name
        self._habitat = habitat
    def introduce(self):
        print(f'Привет, меня зовут {self._name}')
        print(f'Моя среда обитания - {self._habitat}')

class Tiger(Animal):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self._color = color
    def show_color(self):
        print(f'Окрас тигра по имени {self._name} - {self._color}')

class Elephant(Animal):
    def __init__(self, name, habitat, tusk_length):
        super().__init__(name, habitat)
        self._tusk_length = tusk_length
    def show_tusks(self):
        print(f'У слона по имени {self._name} есть бивни длиной {self._tusk_length} см')