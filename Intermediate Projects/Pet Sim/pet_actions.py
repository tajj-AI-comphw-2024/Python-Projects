# pet_actions.py

def feed_pet(pet):
    pet.hunger -= 10
    print(f"{pet.name} has been fed. Hunger is now {pet.hunger}.")

def play_with_pet(pet):
    pet.happiness += 10
    print(f"{pet.name} played and is now happier. Happiness is now {pet.happiness}.")

def check_health(pet):
    print(f"{pet.name}'s health is {pet.health}.")