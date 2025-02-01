#16
#Create an interface `IShape` with an abstract method 
# `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC, abstractmethod
class IShape:
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        print(f"Area of rectangle is: {self.length*self.breadth}")
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        print(f"Area of circle is: {3.14*self.radius*self.radius}")
rect = Rectangle(15,6)
rect.calculate_area()
cir = Circle(2)
cir.calculate_area()
