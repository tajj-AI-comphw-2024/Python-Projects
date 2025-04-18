"""
Automated Calculator (Easy-Intermediate)
Skills Used/Developed: Exception handling, match/case, input validation
Description: Build a scientific calculator that supports basic arithmetic (addition, subtraction, multiplication, division) 
and more advanced operations like exponentiation, square roots, and trigonometric functions.
Goal: Practice working with functions, conditional statements, error handling, and validating user input.
Libraries: math
Example: Expand the calculator by adding a graphical user interface (GUI) or implementing a history feature that stores recent calculations.
"""
import math
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))
        entry.delete(0, tk.END)

def clear():
    entry.delete(0, tk.END)

def add():
    entry.insert(tk.END, "+")
    entry.icursor(tk.END)

def subtract():
    entry.insert(tk.END, "-")
    entry.icursor(tk.END)

def multiply():
    entry.insert(tk.END, "*")
    entry.icursor(tk.END)

def divide():
    entry.insert(tk.END, "/")
    entry.icursor(tk.END)

def exponentiation():
    entry.insert(tk.END, "**")
    entry.icursor(tk.END)

def square_root():
    entry.insert(tk.END, "math.sqrt(")
    entry.icursor(tk.END)

def sin():
    entry.insert(tk.END, "math.sin(")
    entry.icursor(tk.END)

def cos():
    entry.insert(tk.END, "math.cos(")
    entry.icursor(tk.END)

def tan():
    entry.insert(tk.END, "math.tan(")
    entry.icursor(tk.END)

# Create the main window
root = tk.Tk()
root.title("Automated Calculator")

# Create the entry widget for input
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('^', 5, 1), ('√', 5, 2), ('sin', 5, 3),
    ('cos', 6, 0), ('tan', 6, 1)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, command=clear)
    elif text == '+':
        button = tk.Button(root, text=text, padx=20, pady=20, command=add)
    elif text == '-':
        button = tk.Button(root, text=text, padx=20, pady=20, command=subtract)
    elif text == '*':
        button = tk.Button(root, text=text, padx=20, pady=20, command=multiply)
    elif text == '/':
        button = tk.Button(root, text=text, padx=20, pady=20, command=divide)
    elif text == '^':
        button = tk.Button(root, text=text, padx=20, pady=20, command=exponentiation)
    elif text == '√':
        button = tk.Button(root, text=text, padx=20, pady=20, command=square_root)
    elif text == 'sin':
        button = tk.Button(root, text=text, padx=20, pady=20, command=sin)
    elif text == 'cos':
        button = tk.Button(root, text=text, padx=20, pady=20, command=cos)
    elif text == 'tan':
        button = tk.Button(root, text=text, padx=20, pady=20, command=tan)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col)

# Run the main loop
root.mainloop()
