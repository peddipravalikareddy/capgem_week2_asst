#Create a `Product` class with attributes `name`, `price`, and `stock`.
#  Write a method `check_availability(quantity)` that returns whether the requested quantity
#  is available.

class Product:
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def check_availability(self, quantity):
        self.quantity = quantity
        if self.stock >= quantity:
            print(f"Requested quantity of {self.quantity} is available")
        else:
            print("Stock is not available!")
n = int(input("Enter no of products: "))
for i in range(n):
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    prod = Product(name, price, stock)
    quantity = int(input("Enter quantity: "))
    prod.check_availability(quantity)