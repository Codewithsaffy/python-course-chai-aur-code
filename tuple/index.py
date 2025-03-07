# Tuple operations

t = (1, 3, 5, 6, 7)
print(t[3])  # Output: 6 (Accessing an element)

# Tuples are immutable, so item assignment is not allowed
# t[3] = 4  # Uncommenting this line will raise TypeError

# Creating a new reference
t2 = t
print(t, t2)  # Output: (1, 3, 5, 6, 7) (1, 3, 5, 6, 7)

# Tuple with a single element must have a comma
t = ([2, 4, 6, 7],)
print(type(t))  # Output: <class 'tuple'>

# Accessing and modifying mutable elements within a tuple
t[0].append(33)
print(t)  # Output: ([2, 4, 6, 7, 33],)

# Copying reference
t2 = t
print(t2)  # Output: ([2, 4, 6, 7, 33],)

# Removing last element from the mutable list inside the tuple
t[0].pop()
print(t2)  # Output: ([2, 4, 6, 7],) (Change is reflected in both references)

# Tuple Methods
tuple1 = (1, 2, 3, 4, 2, 5, 2)
print(tuple1.count(2))  # Output: 3 (Counts occurrences of 2)
print(tuple1.index(3))  # Output: 2 (Returns index of first occurrence of 3)

# Possible Operations with Tuples
# Concatenation
tuple2 = (8, 9)
new_tuple = tuple1 + tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 2, 5, 2, 8, 9)

# Repeating
tuple3 = ('a',) * 5
print(tuple3)  # Output: ('a', 'a', 'a', 'a', 'a')

# Membership Test
print(3 in tuple1)  # Output: True (Checks if 3 is in the tuple)

# Length of tuple
print(len(tuple1))  # Output: 7

# Iterating over a tuple
for item in tuple1:
    print(item)  # Prints each element in the tuple
