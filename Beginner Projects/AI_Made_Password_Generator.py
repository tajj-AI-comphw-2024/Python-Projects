# Random Password Generator
# Skills Used: loops, functions, lists, random modules.
# Create a program that generates a random password of a specified length using a mix of letters, numbers, and symbols.
# Goal: Explore randomness and learn how to manipulate strings and lists.

import random

def generate_password(length):
    # Define the character sets for each type of character
    # ASCII values for lowercase letters: 97-122
    # ASCII values for uppercase letters: 65-90
    # ASCII values for numbers: 48-57
    # ASCII values for symbols: 33-47, 58-64, 91-96, 123-126
    
    # Create lists for each type of character set using list comprehension
    # chr() function converts ASCII values back to characters
    # ord() function converts characters back to ASCII values
    
    # List of lowercase letters
    # List of uppercase letters
    # List of numbers
    # List of symbols
    
    # Combine all character sets into one list
    # Shuffle the characters in the list to randomize the order
    # Convert the list back to a string using ''.join() function
    # Return the generated password as a string

    # Example usage:
    lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    numbers = [chr(i) for i in range(ord('0'), ord('9')+1)]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '?', '/', '\\']
    
    # Combine all character sets into one
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols
    
    # Generate a random password of the specified length
    # Add each character to the password list in a random order using random.choice() function
    # Convert the password list back to a string using ''.join() function
    # Return the generated password as a string

    # Example usage:
    # length = 10
    # password = generate_password(length)
    # print("Generated Password:", password)  # Output: Jh0g8P!5Z

    # Example usage:
    # length = 15
    # password = generate_password(length)
    # print("Generated Password:", password)  # Output: 69Y$%r0z!K[=2

    # Example usage:
    # length = 20
    # password = generate_password(length)
    # print("Generated Password:", password)  # Output: 8Z1x&wB56e#r7T!K%G[=3
    password = []
    for _ in range(length):
        password.append(random.choice(all_characters))
    
    # Shuffle the characters in the password to randomize the order
    random.shuffle(password)
    
    # Convert the password list back to a string
    password = ''.join(password)
    
    return password

# Example usage

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Password:", password)


