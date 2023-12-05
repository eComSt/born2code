# def F(n):
#     return 10 - F(n - 1)
# print(F(5))
# F(1) = 1
# F(n) = 10 - F(n - 1)
# F(1) = 1
def F(n):
    if n == 1:
        return 1
    else:
        return 10 - F(n - 1)
10 - (10 + (10 - (10 + 1) ))
print(F(5))