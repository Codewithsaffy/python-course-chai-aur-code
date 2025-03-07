# Dictionary operations and methods

dist = {"name": "yousuf", "age": 19, "hight": "6ft"}
print(dist)  # Output: {'name': 'yousuf', 'age': 19, 'hight': '6ft'}

# Iterating through dictionary keys
for i in dist:
    print(i)  # Output: name, age, hight

# Iterating through dictionary values
for i in dist:
    print(dist[i])  # Output: yousuf, 19, 6ft

# Correct way to iterate through dictionary key-value pairs
for key, value in dist.items():  # 'items()' instead of 'item()'
    print(key, value)  # Output: name yousuf, age 19, hight 6ft

# Checking available dictionary methods
print(dir(dist))

# Removing an element using 'pop()'
dist.pop("name")  # Removes 'name' key and returns its value
print(dist)  # Output: {'age': 19, 'hight': '6ft'}

# Adding and updating dictionary values
dist["name"] = "tallal"
print(dist)  # Output: {'age': 19, 'hight': '6ft', 'name': 'tallal'}

dist["name"] = "yousuf"  # Updating an existing key
print(dist)  # Output: {'age': 19, 'hight': '6ft', 'name': 'yousuf'}

# Using 'fromkeys()' to create a dictionary with default values
keys = ["baber", "virat", "rizwan", "shaheen"]
default_value = "good"
new_obj = dict.fromkeys(keys, default_value)  # Correct way to use fromkeys()
print(new_obj)  # Output: {'baber': 'good', 'virat': 'good', 'rizwan': 'good', 'shaheen': 'good'}

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(6)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Additional Dictionary Methods

# 'clear()' - Removes all elements from dictionary
dist.clear()
print(dist)  # Output: {}

# Reinitializing dictionary for further operations
dist = {"name": "yousuf", "age": 19, "hight": "6ft"}

# 'copy()' - Returns a shallow copy of the dictionary
dist_copy = dist.copy()
print(dist_copy)  # Output: {'name': 'yousuf', 'age': 19, 'hight': '6ft'}

# 'get()' - Returns value of key, or None if key not found
print(dist.get("name"))  # Output: yousuf
print(dist.get("weight", "Not Found"))  # Output: Not Found

# 'keys()' - Returns all keys in the dictionary
print(dist.keys())  # Output: dict_keys(['name', 'age', 'hight'])

# 'values()' - Returns all values in the dictionary
print(dist.values())  # Output: dict_values(['yousuf', 19, '6ft'])

# 'items()' - Returns all key-value pairs as tuples
print(dist.items())  # Output: dict_items([('name', 'yousuf'), ('age', 19), ('hight', '6ft')])

# 'popitem()' - Removes and returns the last inserted key-value pair
dist.popitem()
print(dist)  # Output: {'name': 'yousuf', 'age': 19} (removes 'hight')

# 'setdefault()' - Returns value of key if exists, else inserts key with default value
print(dist.setdefault("age", 25))  # Output: 19 (key already exists)
print(dist.setdefault("weight", "70kg"))  # Output: 70kg (new key added)
print(dist)  # Output: {'name': 'yousuf', 'age': 19, 'weight': '70kg'}

# 'update()' - Updates dictionary with key-value pairs from another dictionary or iterable
dist.update({"city": "Karachi", "country": "Pakistan"})
print(dist)  # Output: {'name': 'yousuf', 'age': 19, 'weight': '70kg', 'city': 'Karachi', 'country': 'Pakistan'}
