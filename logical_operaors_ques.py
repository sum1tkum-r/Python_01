# Initialize variables
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Calculate conditions
can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18
cannot_go_outside = not is_sunny or temperature < 10 or wind_speed > 30

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)

# logical Operators Question 1:

# Initialize variables
has_license = True
has_space = True
has_experience = False

# Calculate conditions
can_sell_regular_pet = (has_license or has_experience) and has_space
can_sell_exotic_pet = (has_experience or has_experience) and has_space 
cannot_sell_any_pet = (not has_license or not has_experience) and not has_space

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)

# logical Operators Question 2:

# Initialize variables
has_license = True
has_space = True
has_experience = False

# Calculate conditions
can_sell_regular_pet = (has_license or has_experience) and has_space
can_sell_exotic_pet = (has_experience or has_experience) and has_space 
cannot_sell_any_pet = (not has_license or not has_experience) and not has_space

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)