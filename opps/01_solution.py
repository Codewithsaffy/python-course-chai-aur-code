# create a Car class with arrtibute like brand model.Then create an instance of the class 

class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age


i  = Car("yousuf", 3)
print(i.age)