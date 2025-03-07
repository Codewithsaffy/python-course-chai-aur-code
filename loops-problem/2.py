# sum the even no in n

n = 10

sum = 0
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, n+1):
    if (i%2 == 0):
        sum += i
print(sum)