# Simple Calculator in Python

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get the user's choice
choice = input("Enter the operation symbol (+, -, *, /): ")

# Perform the calculation
if choice == '+':
    result = num1 + num2
    operation = "Addition"
elif choice == '-':
    result = num1 - num2
    operation = "Subtraction"
elif choice == '*':
    result = num1 * num2
    operation = "Multiplication"
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        operation = "Division"
    else:
        result = "Error! Division by zero."
        operation = "Division"
else:
    result = "Invalid operation!"
    operation = "Unknown"

# Display the result
print(f"{operation} result: {result}")