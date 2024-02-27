class List(list):
    def __getitem__(self, item):
        item = item % len(self)
        return super().__getitem__(item)
a = List((1,2,3,4))
print(a[4])