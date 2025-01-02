# Python Calculator

try:
    operator = input("Enter an operator (+ - * /): ")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

if operator == "+":
    result = num1 + num2
    print(round(result,5))
elif operator == "-":
    result = num1 - num2
    print(round(result,5))
elif operator == "*":
    result = num1 * num2
    print(round(result,5))
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(round(result,5))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(f"Please enter a valid operator, {operator} is not a valid operator.")