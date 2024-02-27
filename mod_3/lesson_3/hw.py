class Animal: 
    def __init__(self, name, habitat): 
        self.name = name 
        self.habitat = habitat 
    def introduse(self): 
        print("ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ") 
        print(f"Привет, меня зовут {self.name}") 
        print(f'Моя среда обитания - {self.habitat}') 
        print("ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ") 
class Tiger(Animal): 
    def __init__(self, name, habitat, color): 
        super().__init__(name, habitat) 
        self._color = color 
    def show_color(self,): 
        print("ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ") 
        print(f"Окрас тигра по имени {self.name}: {self._color}") 
        print("ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ") 
class Elephant(Animal): 
    def __init__(self, name, habitat, tusk_length): 
        super().__init__(name, habitat) 
        self._tusk_length = tusk_length 
    def show_tusks(self):             
        print(f"У слона по имени {self.name} есть бивни длиной {self._tusk_length}") 
elephant = Elephant("Элли", "Саванна", 200)
elephant.show_tusks()