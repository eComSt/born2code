data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9],
    [7, 8, 9],
    [7, 8, 9],
]
# print(data[0][0])
summa = 0
for line in data:
    print(line)
for line in data:
    summa += sum(line)
print(summa)