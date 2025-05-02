"""
Create Pet Module
Created: April 5th, 2025
Finished: May 2nd, 2025

Description:
This module provides functionality to create a virtual pet by selecting its breed and attributes.

Skills Developed:
- User Input Handling
- Randomization
- Function Design

Libraries: None (pure Python)
"""

import random
from typing import List
from virtual_pet import VirtualPet, Dog, Cat, Bird, Fish

def create_pet(pet_class, breeds: List[str], health: int, hunger: int, happiness: int) -> VirtualPet:
    """
    Create a new pet instance based on user input.

    Args:
        pet_class (class): The class of the pet (e.g., Dog, Cat).
        breeds (List[str]): List of available breeds for the pet.
        health (int): Initial health of the pet.
        hunger (int): Initial hunger of the pet.
        happiness (int): Initial happiness of the pet.

    Returns:
        VirtualPet: An instance of the selected pet class.
    """
    while True:
        print("Select your breed type or enter your own:")
        print(f"1. {pet_class.__name__} Breeds: {breeds}")
        print("2. Enter my own")
        print("3. Random Breed")
        print("4. Back")
        print("5. Exit")
        userBreedChoice = input("Enter your breed choice: ").lower()
        if userBreedChoice in [breed.lower() for breed in breeds]:
            return pet_class(input("Enter your pet's name: "), health, hunger, happiness, userBreedChoice)
        elif userBreedChoice in ["2", "2.", "enter my own"]:
            return pet_class(input("Enter your pet's name: "), health, hunger, happiness, input("Enter your breed: "))
        elif userBreedChoice in ["3", "3.", "random breed"]:
            return pet_class(input("Enter your pet's name: "), health, hunger, happiness, random.choice(breeds))
        elif userBreedChoice in ["4", "4.", "back"]:
            return None  # Return None to indicate going back 
        elif userBreedChoice in ["5", "5.", "exit"]:
            print("Thanks for playing!")
            exit()  # Exit the program
        else:
            print("Invalid choice. Please try again.")