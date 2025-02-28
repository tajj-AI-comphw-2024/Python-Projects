# virtual_pet.py
class VirtualPet:
    def __init__(self, name: str, health: int, hunger: int, happiness: int, breedType: str) -> None:
        print("VirtualPet class successfully called")
        self.name = name
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.breedType = breedType

    def checkStatus(self) -> None:
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