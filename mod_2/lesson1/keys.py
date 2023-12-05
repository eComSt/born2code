lst = [1,2,1,2,4,5,6,6,7,4,3,2,2]
set_temp = set(lst)
while len(set_temp)>0:
    i = set_temp.pop()
#     print(i)
# print("DONE")
str1 = 'i l o v e c a t s'
str2 = 's c a a a a a a a a a a a t'
set1 = set(str1)
set2 = set(str2)
print(set1)
print(set2)
print(set2.issubset(set1))