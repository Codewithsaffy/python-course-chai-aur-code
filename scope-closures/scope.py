x = 33
def add():
    x = 99
    print(x)
add()
print(x)


def add():
    global x # ir make this var globle
    x = 99
    print(x)

add()
print(x)
