'''
Virtual Pet Simulator (Easy)
Skills Used/Developed: Classes, attributes, methods, inheritance
Description: This project involves creating a simple simulation of a virtual pet. The pet has various attributes like health, hunger, and happiness. Users can interact with the pet by feeding it, playing with it, or making it rest. The pet's stats change based on these interactions.
Goal: Learn how to model real-world objects and behaviors using Python classes and object-oriented programming (OOP).
Libraries: None (pure Python).
Example: Add more interaction options or extend the game by introducing a mini-game where the pet can play to improve its happiness.
'''

'''
# For classes:
# Want to create a Parent class for virutal pet to handle commonly shared attributes
# Seperate classes for pet types
# Functions that in that class that will dictate their behaviors and actions
# Oustide of the program, maybe use time libary and random later on
# Function that will keep the program running and end it 
'''
import random
class virtualPet:
    def __init__(self, name, health , hunger, happiness, breedType):
        print("VirtualPet class successfully called")
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.breedType = breedType
    def checkStatus(self):
        print(f"Name: {self.name}, Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}")
'''
# If want to seperate variables used globally for a class will still have to take in variables 
'''
class Dog(virtualPet):
    print("Dog class successfully called")
    def __init__(self, name, health, hunger, happiness, breedType):
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi im {self.name}")

class Cat(virtualPet):
    print("Cat class successfully called")
    def __init__(self, name, health, hunger, happiness, breedType):
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi im {self.name}")

class Bird(virtualPet):
    print("Bird class successfully called")
    def __init__(self, name, health, hunger, happiness, breedType):
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi im {self.name}")

class Fish(virtualPet):
    print("Fish class successfully called")
    def __init__(self, name, health, hunger, happiness, breedType):
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi im {self.name}")
    

def startGame():
    dogBreeds = ["Labrador", "Beagle", "Poodle"]
    catsBreeds = ["Siamese", "Persian", "Maine Coon"]
    birdBreeds = ["Cardinal", "Cockatiel", "Parrot"]
    fishBreeds = ["Goldfish", "Tuna", "Salmon"]
    
    
    print("Welcome to the Virtual Pet Simulator!")
    
    while True:
        # Print menu
        print("Select your pet type:")
        print("1. Dog")
        print("2. Cat")
        print("3. Bird")
        print("4. Fish")
        print("5. Random Pet")
        print("6. Exit")
        print("Inputs ex format: 1, 1., Dog, dog, DoG, DOG or etc")
        userChoice = input("Enter your choice: ").lower()

        # Decision Making Process
        if userChoice in ["1", "1.", "dog"]:
            while True:
                print("Select your breed type or enter your own:")
                print("1. Dog Breeds: "+str(dogBreeds))
                print("2. Enter my own")
                print("3. Random Breed")
                userBreedChoice = input("Enter your breed choice: ").lower()
                # Handles breed inputs
                if userBreedChoice in dogBreeds:
                    pet = (use)
        elif userChoice in ["2", "2.", "cat"]:
            pass
        elif userChoice in ["3", "3.", "bird"]:
            pass
        elif userChoice in ["4", "4.", "fish"]:
            pass
        elif userChoice in ["5", "5.", "random, random pet"]:
            pass
        elif userChoice in ["6", "6.", "exit"]:
            pass
            break
        else:
            print("Invalid choice. Please try again.")
                    

startGame()