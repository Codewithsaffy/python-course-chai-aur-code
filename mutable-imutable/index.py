x = 10
y = x
print(x, y)
x = 20
print(x, y) # When we assigned y to x, y got the value 10. When we changed x to 20, y remained 10 because in Python variables are references to objects. Initially both x and y referenced 10, but when x was changed to 20, only x's reference changed


# python varibles has no data types  value has data types

# python has garbage collector to remove unused  memory but it not remove number and string immediately because they are used so much 

l1 = [1, 2, 3] 
l2 = l1
print(l1, l2) # [1, 2, 3] [1, 2, 3]
l1[0] = 4
print(l1, l2) # [4, 2, 3] [4, 2, 3] # When we assigned l2 to l1, l2 got the reference to l1. When we changed l1, l2 also changed because both are references to the same object in memory

n1 = [1, 2, 3]
n2 = [1, 2, 3]
n1[0] = 4
print(n1, n2) # [4, 2, 3] [1, 2, 3] # When we assigned n2 to n1, n2 got the reference to n1. When we changed n1, n2 remained the same because n1 and n2 are references to different objects in

# check if two variables are referencing the same object
print(l1 is l2) # True
print(n1 is n2) # False

