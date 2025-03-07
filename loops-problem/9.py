# check uniqueness

list = ["mangoo", "apple", "banana" ,"apple", "banana" ]

for i in list:
    if list.count(i) > 1:
        print(f"{i} is repeat")
        break