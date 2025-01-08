# Random Password Generator
# Skills Used: loops, functions, lists, random modules.
# Create a program that generates a random password of a specified length using a mix of letters, numbers, and symbols.
# Goal: Explore randomness and learn how to manipulate strings and lists.

import random

def generate_password(length):
    # Defines the character sets for each type of character
    lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p ", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '?', '/', '\\']
    
    password_generated = ""

    for i in range(length):
        random_list = random.randint(1, 4)
        if random_list == 1:
            password_generated += lowercase_letters[random.randint(1, len(lowercase_letters)-1)]
        elif random_list == 2:
            password_generated += uppercase_letters[random.randint(1, len(uppercase_letters)-1)]
        elif random_list == 3:
            password_generated += str(numbers[random.randint(1, len(numbers)-1)])
        else:
            password_generated += symbols[random.randint(1, len(symbols)-1)]
    
    return password_generated

# Get the desired length from the user

password_length = int(input("Enter the desired length of the password: "))

# Generate and print the password

generated_password = generate_password(password_length)
print("Generated Password:", generated_password)