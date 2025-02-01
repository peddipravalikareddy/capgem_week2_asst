#Implement a multi-level inheritance example where `Vehicle` is a base class, 
# `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
#  6


class Vehicle:
    name = 'Vehicle'
    def show(self):
        print("This is vehicle class method")
    def displayName(self):
        print(f"Vehicle name is: {self.name}")
class Car(Vehicle):
    def carMethod(self):
        print("This is car class method")
    def displayName(self):
        Vehicle.name = 'Car'
        print(f"Car name is: {Vehicle.name}")
class Bike(Vehicle):
    def bikeMethod(self):
        print("This is bike class method")
    def displayName(self):
        Vehicle.name = 'Bike'
        print(f"Vehicle name is: {Vehicle.name}")
class ElectricCar(Car):
    def electricCarMethod(self):
        print("This is electric car class method")
    def displayName(self):
        Vehicle.name = 'Electric Car'
        print(f"Vehicle name is: {Vehicle.name}")
ev = ElectricCar()
ev.displayName()
ev.carMethod()
ev.electricCarMethod()



