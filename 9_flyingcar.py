#9
#Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. 
# Handle potential conflicts in the `move()` method.

class Car:
    def move(self):
        print("Car moves on road.")
class Airplane:
    def move(self):
        print("Plane goes over clouds.")
class FlyingCar(Car, Airplane):
    def move(self):
        super().move()
        print("Flying Car can travel on road as well as air")
fc = FlyingCar()
fc.move()
