# This program classifies the wind status based on the input wind speed.
# this is a basic if-else statement example in Python.

wind = int(input()) # Don't change this line
status = "unset"
# Type your code below
if wind < 8:
    status = "Calm" 
elif wind >= 8 and wind <=31 :
    status = "Breeze"
elif wind >= 32 and wind <=63 :
    status = "Gale"
else :
    status = "Storm"

# Don't change the line below
print(f"status = {status}")

# This program classifies the wind status based on the input wind speed.
# this is a basic if-else statement example in Python.

temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below
if temperature < 0:
    weather = "Freezing"
elif temperature >= 0 and temperature <= 15:
     weather = "Cold"
elif temperature >= 16 and temperature <= 25:
    weather = "Mild"
else :
    weather = "Hot"


# Don't change the line below
print(f"weather = {weather}")


# Nested if-else statement example in Python.

level = int(input()) # Don't change this line
has_training = input() == "True" # Don't change this line
level_message = "None" # Don't change this line

# Write your code below
if level <= 0:
    level_message = "Invalid level"
elif level <= 5:
    level_message = "Basic weapons only"
elif level <= 10:
    if has_training:
        level_message = "Access to advanced weapons granted"
    else:
        level_message = "Need weapon training first"
else:
    level_message = "Access to all weapons granted"


# Don't change below this line
print(level_message)