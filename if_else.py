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