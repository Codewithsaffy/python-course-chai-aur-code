x = 10
y = x
print(x, y)
x = 20
print(x, y) # When we assigned y to x, y got the value 10. When we changed x to 20, y remained 10 because in Python variables are references to objects. Initially both x and y referenced 10, but when x was changed to 20, only x's reference changed