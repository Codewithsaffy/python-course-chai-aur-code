def sum_many_no(*arg):# we can keep name of this parameter any thing but it is professional name thorugh this para we can get multiple parameters
    print(*arg)
    print(arg)
    return sum(arg)

print(sum_many_no(1, 3, 4, 5, 3))

