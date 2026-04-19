# This is a simple calculator program in Python.

n1 = int(input("Enter the first number: ")) # Don't change this line
n2 = int(input("Enter the second number: ")) # Don't change this line
op = input("Enter the operator (+, -, *, /): ") # Don't change this line

result = 0
if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    result = n1 / n2
elif op == '*':
    result = n1 * n2

# Don't change the line below
print(f"result = {result}")