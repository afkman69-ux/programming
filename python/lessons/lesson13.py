num1 = float(input("num1:  \n"))
num2 = float(input("num2:  \n"))

a = input("+, -, *, /:  \n")

if a == "+":
    print(num1 + num2)
elif a == "-":
    print(num1 - num2)
elif a == "*":
    print(num1 * num2)
else:
    print(num1 / num2)