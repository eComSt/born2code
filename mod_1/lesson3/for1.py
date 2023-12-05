# # from random import randint
# lst = ['bananas','apples','oranges']
# strg = 'abcdef'
# for i in strg:
#     print(i)
x = 2000
length = 0
for i in range(14):
    length = length + x
    x = x + 500
print(length)
x = 2000
length = 0
for i in range(2000, 9000, 500):
    length = length + i
print(length)