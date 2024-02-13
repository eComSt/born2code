class Captain:
        __cap = None    # ссылка на экземпляр класса Captain
        # метод __new__(), итоговая версия
        def __new__(cls, *args, **kwargs):
            if cls.__cap is None:  # если объекта класса Captain еще нет в программе
                cls.__cap = super().__new__(cls) # создаем объект класса Captain
            return cls.__cap                     # возвращаем созданный объект

        # инициализатор класса
        def __init__(self, name, age, height, weight):
            self.name = name        # имя
            self.age = age          # возраст
            self.height = height    # рост
            self.weight = weight    # масса
        def __str__(self):
            return f"{self.name},{self.age}"
# создаем экземпляр класса Captain
cap = Captain(name='Дима', age=26, height=179, weight=75)
# пытаемся создать новый экземпляр класса Captain
new_cap = Captain(name='Миша', age=25, height=189, weight=82)

# выводим адреса созданных объектов на экран (они совпадают)
print(cap)
print(new_cap)
