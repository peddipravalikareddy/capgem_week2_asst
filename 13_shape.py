#13
#Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes 
# that provide specific implementations for `area()`.

class Shape:
    def area(self):
        print("No information to find the area")
class Square(Shape):
    def _init_(self, side):
        self.side = side
    def area(self):
        print(f"Area of square is: {self.side*self.side}")
class Triangle(Shape):
    def _init_(self, breadth, height):
        self.breadth = breadth
        self.height = height
    def area(self):
        print(f"Area of triangle is: {0.5*self.breadth*self.height}")
square = Square(4)
square.area()
triangle = Triangle(4, 4)
triangle.area()
