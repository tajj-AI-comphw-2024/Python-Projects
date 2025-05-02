"""
Pet Actions Module
Created: April 5th, 2025
Finished: May 2nd, 2025

Description:
This module contains functions to interact with virtual pets, such as feeding them, playing with them, and checking their health.

Skills Developed:
- Function Design
- Parameter Passing

Libraries: None (pure Python)
"""

def feed_pet(pet):
    """
    Feed the pet to reduce its hunger.

    Args:
        pet (VirtualPet): The pet to feed.
    """
    pet.hunger -= 10
    print(f"{pet.name} has been fed. Hunger is now {pet.hunger}.")

def play_with_pet(pet):
    """
    Play with the pet to increase its happiness.

    Args:
        pet (VirtualPet): The pet to play with.
    """
    pet.happiness += 10
    print(f"{pet.name} played and is now happier. Happiness is now {pet.happiness}.")

def check_health(pet):
    """
    Check the health of the pet.

    Args:
        pet (VirtualPet): The pet whose health to check.
    """
    print(f"{pet.name}'s health is {pet.health}.")