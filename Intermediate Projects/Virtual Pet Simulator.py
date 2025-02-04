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
    def __init__(self, name, health , hunger, happiness, petType):
        print("VirtualPet class successfully called")
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.petType = petType
    def checkStatus(self):
        print(f"Name: {self.name}, Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}")
'''
# If want to seperate variables used globally for a class will still have to take in variables 
'''
class Dog(virtualPet):
    print("Dog class successfully called")
    def __init__(self, name, health, hunger, happiness, petType):
        super().__init__(name, health, hunger, happiness, petType)
        print(f"Hi im {self.name}")

class Cat(virtualPet):
    print("Cat class successfully called")
    def __init__(self, name):
        super().__init__(name)
        print(f"Hi im {self.name}")

class Bird(virtualPet):
    print("Bird class successfully called")
    def __init__(self, name):
        super().__init__(name)
        print(f"Hi im {self.name}")

class Fish(virtualPet):
    print("Fish class successfully called")
    def __init__(self, name):
        super().__init__(name)
        print(f"Hi im {self.name}")
    

def startGame():
    dogs = ["Labrador", "Beagle", "Poodle"]
    selected_breed = random.choice(dogs)
    dog = Dog(dogname, random.randint(25, 90), random.randint(25, 90), random.randint(25, 90), "Dog")
    dog.checkStatus()

startGame()