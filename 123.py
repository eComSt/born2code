lst = input().split()
for i,j in enumerate(lst):
    lst[i] = int(j)
print(sum(lst)/len(lst))