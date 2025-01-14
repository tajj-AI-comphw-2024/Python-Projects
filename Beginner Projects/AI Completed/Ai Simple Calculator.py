# Simple Calculator
# Concept: Create a basic calculator that can perform addition, subtraction, multiplication, and division.
# Implementation:
# Use input() to get two numbers from the user.
# Use if-elif-else statements to determine the operation the user wants to perform (e.g., "+", "-", "*", "/").
# Perform the calculation and print the result.
# Learning Points:
# Input/Output
# Basic arithmetic operations
# Conditional statements

# Get two numbers from the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operation from the user

operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation and print the result

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        result = None
else:
    print("Error: Invalid operation.")
    result = None

if result is not None:
    print("The result is:", result)

# Test the calculator with some sample inputs
# num1 = 10
# num2 = 5
# operation = "-"
# print(f"The result is: {num1} {operation} {num2} = {num1 - num2}")