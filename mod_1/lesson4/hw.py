squares = []
for _ in range(5):
    squares.append(int(input('Введите число: ')) ** 2)
print(sorted(squares, reverse=True))

# print(sorted([int(input(': ')) ** 2 for _ in range(5)], reverse=True))


# print(sorted([int(input())**2,int(input())**2,
#         int(input())**2,int(input())**2,
#         int(input())**2], reverse=True))