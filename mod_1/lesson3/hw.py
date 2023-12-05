number = int(input())
factorial = number

for i in range(2, number):
    factorial *= i

print(factorial)