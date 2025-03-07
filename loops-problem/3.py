# multiplication and skip fifth 

n = int(input("Enter no >>"))

for i in range(1, 11):
    if(i == 5):
        continue
    print(f"{i} x n = {i*n}")