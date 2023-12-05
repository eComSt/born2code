a = {1,2,3}
b = {2,3,4}
print(b.union(a))
print("union", a|b)
print("inter",a&b)
print(" diff",a-b)
print("sym_dif",a^b)
from random import randint
lst = []
for i in range(10):
    lst.append(randint(1,100))
print(lst)