# Represents a sequence of numbers.
num_range: range = range(1, 10, 2) # range(start, stop, step)
# print(type(num_range), " num_range = ", num_range.step, " ", num_range.start, " ", num_range.stop, num_range)  # <class 'range'>")  # <class 'range'>


# a. Set (set)
# Mutable, unordered, and contains unique values.

my_set: set = {1, 2, 33, 4, 4, 5}
# print(my_set)
# my_set.add("33")
# print(my_set)
# print(dir(my_set))
# print(type(my_set), "my_set = ", my_set)  # <class 'set'>


# b. Frozen Set (frozenset)
# Immutable version of a set.

frozen_set = frozenset([11, 2, 3, 4, 4, 5])
frozen_set = frozenset(my_set)

print(type(frozen_set), " frozen_set = ", frozen_set)  # <class 'frozenset'>


# Byte array
byte_array = bytearray([66, 23, 24])
print(type(byte_array), " byte_array = ", byte_array)  # <class 'bytearray'>
print(chr(byte_array[0]))

# What is UTF-8?
# UTF-8 (8-bit Unicode Transformation Format) is a variable-length character encoding that can represent every character in the Unicode standard. It is designed for efficiency and compatibility:

byte_array: bytearray = bytearray([65, 66, 67, 69])
# Converting the entire bytearray to a string using decode()
print("Decoded string: ", byte_array.decode('utf-8'))  # Output: ABCE