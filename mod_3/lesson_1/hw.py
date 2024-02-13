class Dog:
    def __init__(self, name, happiness=0):
        self.__happiness = happiness
        self.__name = name

    def caress(self):
        self.__happiness += 10
        print("Гав-гав")

    def set_name(self, name):
        if name and name.isalpha():
            self.__name = name
            print(f"Теперь собаку зовут {self.__name}!")
        else:
            print("В имени собаки должны быть только буквы!")

    def get_name(self):
        print(f"Собаку зовут {self.__name}")

    def bring_item(self, item: str, distance: int):
        if self.__happiness >= 10 and distance <= 100:
            print(f"{self.__name} принес(ла) предмет: {item}")
        elif distance > 100:
            print(f"{item} находится слишком далеко!")
        elif self.__happiness < 10:
            print(f"{self.__name} нуждается в вашей заботе!")

Lucky = Dog("Шарик")
Lucky.caress()
Lucky.bring_item("палка", 20)
Lucky.set_name("Бобик")
