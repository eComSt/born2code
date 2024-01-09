numbs = ['4', '23', '15', '8']
ans = []
for i in numbs:
    ans.append(int(i))
#формируем объект с целыми числами
int_numbs = list(map(int, numbs))
print(int_numbs)
lst = ['123','assdfsaf','sdfawrsehdfsaddfsdaf']
lll = list(map(len,lst))
print(lll)

base = [1, 2, 5, 6] #список с основаниями
exp = [2, 3, 4, 5] #список с показателями

#указываем списки, к которым применяем функции, порядок важен!
data = list(map(lambda x, y: x**y, base, exp))