def somthing(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

# somthing(1,2,3,4,5,d=6,e=42)
class smthng:
    b=5
    def sm(self):
        print(self.b)
a = smthng()
print(a.sm())