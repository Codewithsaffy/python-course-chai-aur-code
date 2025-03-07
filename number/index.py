from decimal import Decimal
import random

# Floating-point precision issue due to binary representation
print(0.1 + 0.1 + 0.1)  # Output: 0.30000000000000004
print(0.1 + 0.1 + 0.1 - 0.3)  # Output: 5.551115123125783e-17

# Using Decimal to handle floating-point precision accurately
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Output: Decimal('0.3')

# Boolean values in Python behave like integers (True = 1, False = 0)
print(True == 1)  # Output: True
print(False == 0)  # Output: True

# 'is' checks identity, '==' checks equality
print(False is 0)  # Warning: "is" with int literal is not recommended and it is not same in memory
print(True is 1)  # Warning: "is" with int literal is not  recommended and it is not same in memory

# Generating a random integer between 1 and 20
print(random.randint(1, 20))  # Output: Random number between 1 and 20

# Shuffling a list randomly
fruit = ["mango", "apple", "banana"]
random.shuffle(fruit)  # Shuffles the list in-place
print(fruit)  # Output: Random order of fruits

# Checking available methods in the random module
print(dir(random))  # Lists all attributes and methods in the module

# shuffle() does not return a new list; it modifies in-place
print(random.shuffle(fruit))  # Output: None (because it modifies in-place)

# Verifying the shuffled list
print(fruit)  # Output: Fruits in a random order

# True acts like 1 in arithmetic operations
print(True + 1)  # Output: 2
