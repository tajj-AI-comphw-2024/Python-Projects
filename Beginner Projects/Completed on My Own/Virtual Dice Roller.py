# Virtual Dice Roller
# Skills Used: Random module, loops, functions.
# Create a dice-rolling simulation for a game. Let the user choose how many dice to roll and the number of sides on each die.
# Goal: Reinforce randomness and user input.

import random
# want a function to roll the dice
# a loop that will run numDice times and every side is the max value of sides so 1 side is 1, 2 sides is 2, etc.
def rollDice(numDice, sides):
    for i in range(numDice):
        print(f"Your rolled Dice #{i+15}, it landed on side {random.randint(1, sides)}")

userDice = int(input("How many dice do you want to roll? "))
userDiceSides = int(input("How many sides does each die have? "))
rollDice(userDice, userDiceSides)