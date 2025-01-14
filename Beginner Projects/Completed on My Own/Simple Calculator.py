#  Simple Calculator
# Concept: Create a basic calculator that can perform addition, subtraction, multiplication, and division.
# Implementation:
# Use input() to get two numbers from the user.
# Use if-elif-else statements to determine the operation the user wants to perform (e.g., "+", "-", "*", "/").
# Perform the calculation and print the result.
# Learning Points:
# Input/Output
# Basic arithmetic operations
# Conditional statements

import time
for char in [char for char in "Welcome to the Simple Calculator!"]:
    print(char, end = "", flush = True)
    time.sleep(0.05)
time.sleep(1)
print()
userNum1 = input(float("Enter the first number: "))
userNum1 = input(float("Eter the second number:"))
userOperation = input("Enter the operation (+, -, *, /): ")
                 

