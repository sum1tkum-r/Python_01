# Logical Operators Part 1

print(True and True)   # True
print(True and False)  # False
print(False and False) # False
print(True or True)    # True
print(True or False)   # True
print(False or False)  # False
print(not True)        # False
print(not False)       # True

# Question 1:
age = 20
has_license = True

result = age >= 18 and has_license

# Don't change the line below
print("Eligible to drive:", result)

# Question 2:

# Replace the values with numbers
b1 = 2
b2 = 3

# This line checks if b1 * b2 is greater than b1 + b2
b3 = (b1 * b2) > (b1 + b2)

# Don't change the line below
print(f"b3 = {b3}")

# Question 3:

# Replace the values with booleans
a = True
b = False
c = False

# This line checks if (a or b) and not c is True
result = (a or b) and not c

# Don't change the line below
print(f"result = {result}")