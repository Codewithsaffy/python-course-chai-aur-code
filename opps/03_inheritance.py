class Car:
    
    def __init__(self, whicels, speed):
        self.whicels = whicels
        self.speed = speed
    def print(self):
        print(f"{self.speed} and {self.whicels}")

c  = Car(4, "200km/s")
c.print()

class ElectricCar(Car):
    def __init__(self,  whicels, speed, brand):
        super().__init__(whicels, speed)
        self.brand = brand
    

p = ElectricCar(4, "200km/s", "toyta")

p.print()
