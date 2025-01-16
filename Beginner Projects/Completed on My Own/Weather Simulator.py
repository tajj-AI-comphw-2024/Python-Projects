# # Weather Simulator
# Skills Used: Random module, lists, if-else statements.
# Simulate a random weather forecast for a day using predefined conditions (e.g., sunny, rainy, snowy).
# Goal: Practice using randomness and conditionals to model real-world scenarios.

import random 

weatherConditions = ["sunny", "rainy", "snowy" "cloudy with a chance of meatballs"]
weatherChoice = random.choice(weatherConditions)

if weatherChoice == "sunny":
    print("Today is a beautiful day, with a warm sun and soft breeze.")
    print("You might enjoy a leisurely walk around the park.")
    print("Consider grabbing a cup of coffee or enjoying a hot beverage.")
    print("If you're feeling adventurous, you might try a scavenger hunt or a bike ride.")
    print("Have a great day!")
elif weatherChoice == "rainy":
    print("It's raining outside, so take your umbrella with you.")
    print("Pack a light jacket and bring a water bottle or an umbrella.")
    print("Dress appropriately for the weather and wear comfortable shoes.")
    print("If you're planning a trip, consider bringing a map and compass.")
    print("Stay hydrated and enjoy the fresh air.")
    print("If you're feeling adventurous, you might try a scavenger hunt or a bike ride.")
    print("Have a great day!")
elif weatherChoice == "snowy":
    print("It's snowing outside, so pack your winter clothes and bring an umbrella.")
    print("Dress appropriately for the weather and wear comfortable shoes.")
    print("If you're planning a trip, consider bringing a map and compass.")
    print("Stay hydrated and enjoy the fresh air.")
    print("If you're feeling adventurous, you might try a scavenger hunt or a bike ride.")
    print("Have a great day!")
else:
    print("It's a cloudy day, with a chance of meatballs. Stay hydrated and enjoy the fresh air.")
    print("If you're planning a trip, consider bringing a map and compass.")
    print("If you're feeling adventurous, you might try a scavenger hunt or a bike ride.")
    print("Have a great day!")