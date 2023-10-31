number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
if number1.isnumeric() and number2.isnumeric():
    number1 = int(number1)
    number2 = int(number2)
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
    elif oper == '//':
        result = number1 // number2
        print(f"Div int: {result}")
    elif oper == '%':
        result = number1 % number2
        print("Mod: {result}")
    else:
        print("Unknown operation")
