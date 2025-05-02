"""
Virtual Pet Simulator
Created: April 5th, 2025
Finished: May 2nd, 2025

Description:
This project is a simple simulation of a virtual pet. 
Users can interact with the pet by feeding it, playing with it, or making it rest. 
The pet's stats (health, hunger, and happiness) change based on these interactions. 
The project demonstrates the use of Python classes, attributes, methods, and inheritance.

Skills Developed:
- Object-Oriented Programming (OOP)
- Classes and Inheritance
- Attributes and Methods

Libraries: None (pure Python)
"""

class VirtualPet:
    def __init__(self, name: str, health: int, hunger: int, happiness: int, breedType: str) -> None:
        """
        Initialize a VirtualPet instance.

        Args:
            name (str): The name of the pet.
            health (int): The health level of the pet.
            hunger (int): The hunger level of the pet.
            happiness (int): The happiness level of the pet.
            breedType (str): The breed type of the pet.
        """
        print("VirtualPet class successfully called")
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.breedType = breedType

    def checkStatus(self) -> None:
        """
        Print the current status of the pet.
        """
        print(f"Name: {self.name}, Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}")

class Dog(VirtualPet):
    def __init__(self, name: str, health: int, hunger: int, happiness: int, breedType: str) -> None:
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi, I'm {self.name}")

class Cat(VirtualPet):
    def __init__(self, name: str, health: int, hunger: int, happiness: int, breedType: str) -> None:
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi, I'm {self.name}")

class Bird(VirtualPet):
    def __init__(self, name: str, health: int, hunger: int, happiness: int, breedType: str) -> None:
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi, I'm {self.name}")

class Fish(VirtualPet):
    def __init__(self, name: str, health: int, hunger: int, happiness: int, breedType: str) -> None:
        super().__init__(name, health, hunger, happiness, breedType)
        print(f"Hi, I'm {self.name}")