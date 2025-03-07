# find factorial of no with while loop
n = 5
i = 1
factorial = 1
# 5x4x3x2x1
while i < n:
    # print((n-i)+1)

    factorial = factorial * ((n-i)+1)
    i += 1
    print(factorial)
# print(factorial)