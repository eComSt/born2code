class MyHouse:
    rooms = 5
    material = 'wood'
    def __init__(self, s, color):
        self.__s  = s
        self.color = color
        self.price = self.__s*10000

a = MyHouse(123,'red')
a.__s = 142
print(a.__s)