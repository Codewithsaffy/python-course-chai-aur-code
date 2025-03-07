# check prime no or not

no = 29

prime_no = True

if no > 0:
    for n in range(2, 29):
        if(no % n == 0):
            prime_no = False
            break

print(prime_no)