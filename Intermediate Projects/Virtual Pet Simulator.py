import random
from typing import List

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

def create_pet(pet_class, breeds: List[str], health: int, hunger: int, happiness: int) -> VirtualPet:
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
            startGame()
            break
        elif userBreedChoice in ["5", "5.", "exit"]:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def startGame() -> None:
    dogBreeds = ["Labrador", "Beagle", "Poodle"]
    catBreeds = ["Siamese", "Persian", "Maine Coon"]
    birdBreeds = ["Cardinal", "Cockatiel", "Parrot"]
    fishBreeds = ["Goldfish", "Tuna", "Salmon"]
    
    health = random.randint(20, 100)
    hunger = random.randint(20, 100)
    happiness = random.randint(20, 100)

    print("Welcome to the Virtual Pet Simulator!")
    running = True

    while running:
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
            pet = create_pet(Dog, dogBreeds, health, hunger, happiness)
            pet.checkStatus()
            running = False
        elif userChoice in ["2", "2.", "cat"]:
            pet = create_pet(Cat, catBreeds, health, hunger, happiness)
            pet.checkStatus()
            running = False
        elif userChoice in ["3", "3.", "bird"]:
            pet = create_pet(Bird, birdBreeds, health, hunger, happiness)
            pet.checkStatus()
            running = False
        elif userChoice in ["4", "4.", "fish"]:
            pet = create_pet(Fish, fishBreeds, health, hunger, happiness)
            pet.checkStatus()
            running = False
        elif userChoice in ["5", "5.", "random", "random pet"]:
            # Randomly select a pet class (Dog, Cat, Bird, or Fish)
            pet_class = random.choice([Dog, Cat, Bird, Fish])
            
            # Create a dictionary that maps each pet class to its corresponding list of breeds
            breeds = {
                Dog: dogBreeds,
                Cat: catBreeds,
                Bird: birdBreeds,
                Fish: fishBreeds
            }[pet_class]  # Access the list of breeds corresponding to the randomly selected pet class
            
            # Create a new pet using the selected pet class and breed list
            pet = create_pet(pet_class, breeds, health, hunger, happiness)
            
            # Check the status of the newly created pet
            pet.checkStatus()
            
            # Set running to False to exit the main loop
            running = False
        elif userChoice in ["6", "6.", "exit"]:
            print("Thanks for playing!")
            running = False
        else:
            print("Invalid choice. Please try again.")

startGame()