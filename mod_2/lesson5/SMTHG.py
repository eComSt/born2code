from itertools import zip_longest, cycle,repeat
x = [1,2,3,4,5,1,2,4,5,6,7]
y = [5,6,7,8,9,10,42]
z = [1,3,1,5,6,7,8,9,10,42]
# for i in range(min(len(x),len(y))):
#     print((x[i],y[i]))
for i in zip(x,y,z):
    print(i)
for i in zip_longest(x,y,z):
    print(i)
    
for i,j in enumerate(x):
    print(f'{i}:{j}')
    
for i in repeat(x,5):
    print(i)

#chain('ABC', 'DEF') --> A B C D E F
#accumulate([1,2,3,4,5]) --> 1 3 6 10 15