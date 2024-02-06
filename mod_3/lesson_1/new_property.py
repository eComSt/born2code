
class MyClass:
    def __init__(self):
        self._value = 42 
    @property
    def value1(self):
        """This is 'value' property."""
        print("1")
        return self._value
    @value1.setter
    def value(self, value):
        print("2")
        self._value = value
    @value1.deleter
    def value(self):
        print("3")
        del self._value
a = MyClass()
print(a.value1)
