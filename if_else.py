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