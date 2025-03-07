# -----------------------------
# 1. Opening a file (an Iterator)
# -----------------------------
# In Python, open() returns a file object that is both an Iterable and an Iterator.
# That means you can directly call next() on it, or use it in a for loop.

f = open("file.py")  # returns a file object
print(f.readline())  # reads the first line
print(f.readline())  # reads the second line
print(f.readline())  # reads the third line
print(f.readline())  # reads the fourth line (or empty string if fewer lines exist)

# If we call readline() again and there's nothing left, it returns an empty string.
# Notice that you won't get StopIteration with readline(); you just get '' (empty string).

# -----------------------------
# 2. File objects are Iterators
# -----------------------------
# You can confirm that iter(f) is f, meaning the file is its own iterator.

print("Is iter(f) the same object as f? ->", iter(f) is f)
f.close()  # Always good practice to close the file when done.

# -----------------------------
# 3. Lists are Iterables, but NOT Iterators
# -----------------------------
# A list is an "Iterable" because it has an __iter__() method that returns an iterator.
# But the list itself is not an iterator. Calling iter(list) returns a separate object.

my_list = [1, 2, 3]
print("Is iter(my_list) the same object as my_list? ->", iter(my_list) is my_list)

# -----------------------------
# 4. Getting an Iterator from a List
# -----------------------------
# Once you do iter(my_list), you get an iterator (let's store it in a variable i).
# That iterator has a __next__() method which you can call to get elements one by one.

i = iter(my_list)
print("First element ->", i.__next__())  # 1
print("Second element ->", i.__next__()) # 2
print("Third element ->", i.__next__())  # 3

# If you try to call __next__() again, you'll get StopIteration, 
# which signals there are no more items left.
try:
    print("Fourth element ->", i.__next__())
except StopIteration:
    print("StopIteration raised: No more items in the iterator.")

# -----------------------------
# 5. How a for loop uses Iterators
# -----------------------------
# Under the hood, a for loop does something like this:
# 
# for item in my_list:
#     print(item)
#
# is essentially:

print("\nSimulation of for loop with while + next:")
i2 = iter(my_list)  # get a new iterator from the list
while True:
    try:
        item = next(i2)  # same as i2.__next__()
        print(item)
    except StopIteration:
        break

# The for loop automatically calls iter() on the iterable, then repeatedly calls next()
# on the iterator until StopIteration is raised.

# -----------------------------
# 6. Summary of the Diagram
# -----------------------------
# - "Iterable Objects" (like lists, dicts, files) can be passed to iter() to produce an "Iterator".
# - An "Iterator" is an object that has a __next__() method, which returns the next item or raises StopIteration.
# - The built-in functions (like for loops, comprehensions, etc.) automatically call iter() and next() behind the scenes.
# - A file object in Python (from open()) is already its own iterator, so iter(f) is f.
# - A list is just an iterable, so iter(my_list) creates a separate iterator object.

# This script and comments should help remind you how iteration flows in Python:
# Iterable -> iter() -> Iterator -> next() -> item (until StopIteration).
