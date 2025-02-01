#8
#Design a system where a base class `Animal` has a method `speak()`, 
# and subclasses `Dog` and `Cat` override it.	

class Animal:
    def sound(self):
        print("Animals make various sounds")
    def speak(self):
        print("Animal says Hi!")
class Dog(Animal):
    def sound(self):
        print("Dogs says bow bow")
    def speak(self):
        print("Dog says Hello!")
class Cat(Animal):
    def sound(self):
        print("Cat says meow")
    def speak(self):
        print("Cat says Hai!")
dog = Dog()
dog.speak()
cat = Cat()
cat.speak()

