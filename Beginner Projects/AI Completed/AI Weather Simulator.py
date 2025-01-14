# Weather Simulator
# Skills Used: Random module, lists, if-else statements.
# Simulate a random weather forecast for a day using predefined conditions (e.g., sunny, rainy, snowy).
# Goal: Practice using randomness and conditionals to model real-world scenarios.

import random

def get_weather_forecast():
    weather_conditions = ["sunny", "rainy", "snowy"]
    weather_condition = random.choice(weather_conditions)
    
    if weather_condition == "sunny":
        return "It's a beautiful day with warm sunshine!"
    elif weather_condition == "rainy":
        return "It's raining heavily today, but you can still enjoy your day!"
    else:
        return "It's snowing, perfect for sledding!"
    
print(get_weather_forecast())