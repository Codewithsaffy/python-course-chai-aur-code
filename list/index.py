# List operations and slicing
l1 = ["ball", "tap", "bat"] 

# Inserting a string at index 1 using slicing
# Since strings are iterable, "glove" is treated as a list of characters
l1[1:1] = "glove"  # This inserts each character separately
print(l1)  # Output: ['ball', 'g', 'l', 'o', 'v', 'e', 'tap', 'bat']

# Checking available list methods
print(dir(l1))

# Removing an element from the list
l1.remove("ball")
print(l1)  # Output: ['g', 'l', 'o', 'v', 'e', 'tap', 'bat']

# Removing characters of "glove" one by one
for i in "glove":
    l1.remove(i)
print(l1)  # Output: ['tap', 'bat']

# Inserting an element at a specific index
l1.insert(1, "ball")
print(l1)  # Output: ['tap', 'ball', 'bat']

# Correct way to insert a single element using slicing
l1[1:1] = ["glove"]  # This inserts "glove" as a single list element
print(l1)  # Output: ['tap', 'glove', 'ball', 'bat']

# Replacing multiple elements using slicing
l1[1:3] = ["guard"]  # Replaces "glove" and "ball" with "guard"
print(l1)  # Output: ['tap', 'guard', 'bat']

# List comprehension examples

# Generating squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Adding 2 to each number in range(10)
added_two = [x+2 for x in range(10)]
print(added_two)  # Output: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Incorrect list comprehension due to an undefined variable
# [y/2 for x in range(10)]  # This causes NameError because 'y' is not defined

# Corrected list comprehension using the correct variable
halves = [y/2 for y in range(10)]
print(halves)  # Output: [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

