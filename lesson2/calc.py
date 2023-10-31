number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
oper = input("Enter operation: ")
if oper == '+':
    result = number1 + number2
    print("Sum: " + str(result))
elif oper == '-':
    result = number1 - number2
    print("Sub: ", str(result))
elif oper == '*':
    result = number1 * number2
    print("Mul: " + str(result))
elif oper == '/':
    result = number1 / number2
    print(f"Div: {result}")
else:
    print("Unknown operation")
summ = number1 + number2
diff = number1 - number2
mulpt = number1 * number2
div1 = number1 / number2
div2 = number2 // number1
div3 = number1 % number2
print(summ)
print(diff)
print(mulpt)
print(div1)
print(div2)
print(div3)
print(type(diff))