# Interactive Chatbot
# Skills Used: variables, if-else statements, functions, dictionaries.
# Build a simple chatbot that can answer a set of predefined questions or provide random responses based on user input.
# Example: The user inputs, "What's your favorite movie?" and the bot replies, "The Godfather is a classic!"
# Goal: Familiarize yourself with basic decision-making and user input/output handling.

import time

# Print greeting message character by character
greetings = [char for char in "Hi I'm a chatbot! \nI am programmed to inform you about my favorite movies, foods, drinks, hobbies, and sports and more! \nRegular conversation are out of scope for this chatbot!"]
for char in greetings:
    print(char, end="", flush=True)
    time.sleep(0.05)
time.sleep(1)

def chatbot(user_input):
    # Predefined answers and interests of the chatbot
    movies = ["The Godfather", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings"]
    foods = ["Pizza", "Burger", "Pasta", "Sushi", "Steak"]
    drinks = ["Water", "Coffee", "Tea", "Beer", "Wine"]
    hobbies = ["Reading", "Writing", "Drawing", "Cooking", "Gardening"]
    sports = ["Football", "Basketball", "Tennis", "Golf", "Cricket"]
    
    chatbot_response = [char for char in "\n\nWhat would you like to know about me? \n1. My favorite movies \n2. My favorite foods \n3. My favorite drinks \n4. My hobbies \n5. My favorite sports \n6. Exit \n\nPlease input the number or question exactly.\nExample: 1., 1, or \"My favorite movies\". No extra space at the end."]
    for char in chatbot_response:
        print(char, end="", flush=True)
        time.sleep(0.05)

    if user_input == "My favorite movies" or user_input == "1" or user_input == "1.":
        print("\nMy favorite movies are:")
        for movie in movies:
            print(movie)
    elif user_input == "My favorite foods" or user_input == "2" or user_input == "2.":
        print("\nMy favorite foods are:")
        for food in foods:
            print(food)
    elif user_input == "My favorite drinks" or user_input == "3" or user_input == "3.":
        print("\nMy favorite drinks are:")
        for drink in drinks:
            print(drink)
    elif user_input == "My hobbies" or user_input == "4" or user_input == "4.":
        print("\nMy hobbies are:")
        for hobby in hobbies:
            print(hobby)
    elif user_input == "My favorite sports" or user_input == "5" or user_input == "5.":
        print("\nMy favorite sports are:")
        for sport in sports:
            print(sport)
    elif user_input == "Exit" or user_input == "6" or user_input == "6.":
        print("\nGoodbye!")
        return False
    else:
        print("\nI don't understand that question.")
    return True

# Start the chatbot interaction loop

    