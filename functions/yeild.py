def generate_nu(n):
    for i in range(1, n+1):
        return i # it will retunr one number 

print(generate_nu(4))

for i in generate_nu(4):
    print(i) # it give error 

def generate_n(n):
    for i in range(1, n+1):
        yield i  

for i in generate_n(4):
    print(i) # i will pront all number

