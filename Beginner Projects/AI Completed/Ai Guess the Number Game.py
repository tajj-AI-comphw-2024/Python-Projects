# "Guess the Number" Game
# Skills Used: Random module, loops, if-else statements.
# Generate a random number and let the user guess it. Provide hints like "Too high!" or "Too low!"
# Goal: Develop logic for user interaction and feedback.

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Set the maximum number of attempts
    max_attempts = 10
    
    # Loop until the user guesses the correct number or runs out of attempts
    for attempt in range(max_attempts):
        print(f"Attempt {attempt+1}/{max_attempts}")
        
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    
    # If the user did not guess the number within the maximum attempts, reveal the secret number
    if guess != secret_number:
        print(f"Sorry, but the number I was thinking of was {secret_number}.")

guess_the_number()

