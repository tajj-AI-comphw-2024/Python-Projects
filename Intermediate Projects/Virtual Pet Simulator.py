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
    def __init__(self, name, health=0 , hunger= 0, happiness= 0, petType=None):
        print("VirtualPet class successfully called")
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        return self.name
    def checkStatus(self):
        print(f"Name: {self.name}, Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}")
'''
# If want to seperate variables used globally for a class will still have to take in variables 
'''
class Dog(virtualPet):
    print("Dog class successfully called")
    def __init__(self, name):
        super().__init__(name)
        print(f"Hi im {self.name}")
    
# class Cat(virtualPet):

# class Bird(virtualPet):

# class Fish(virtualPet):

# dog = Dog("Buddy", 14, 15, 60)

# print(dog.speak())
                   
dogs = ["Labrador", "Beagle", "Poodle"]
dogname = dogs[random.randint(0, len(dogs)-1)]
dog = Dog(dogname)
pettest = virtualPet()
print(pettest.__init__(name)