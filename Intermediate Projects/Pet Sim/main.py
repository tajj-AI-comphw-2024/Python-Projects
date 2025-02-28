# main.py
import random
from create_pet import create_pet
from virtual_pet import Dog, Cat, Bird, Fish
from pet_actions import *

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

        
if __name__ == "__main__":
    startGame()