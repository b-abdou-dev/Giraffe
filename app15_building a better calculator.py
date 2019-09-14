
print(" Calculator with the following valid operator: +, -, *, / \n")
num1 = float(input(" Enter the first number: \n"))
op = input("Enter the operator:\n")
num2 = float(input("Enter the second number: \n"))

if (op == "+"):
    print(num1 + num2)
elif (op == "-"):
    print(num1 - num2)
elif (op == "*"):
    print(num1 * num2)
elif (op == "/"):
    print(num1 / num2)
else :
    print("Invalid operator \n")

