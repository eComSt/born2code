class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __len__(self):
        return self.x * self.x + self.y * self.y

if __name__ == '__main__':
    v1 = vector(1,2)
    v2 = vector(3,4)
    v3= v1 - v2
    print(v3)    
