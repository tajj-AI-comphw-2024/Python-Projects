# Virtual Dice Roller
# Skills Used: Random module, loops, functions.
# Create a dice-rolling simulation for a game. Let the user choose how many dice to roll and the number of sides on each die.
# Goal: Reinforce randomness and user input.

import random

def roll_dice(num_dice, num_sides):
    total_roll = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        total_roll += roll
        print(f"You rolled a {roll}!")
    print(f"Your total is {total_roll}.")
    return total_roll

# Get user input for the number of dice and sides

num_dice = int(input("How many dice do you want to roll? "))
num_sides = int(input("How many sides does each die have? "))

# Call the function to roll the dice and get the total

roll_dice(num_dice, num_sides)
