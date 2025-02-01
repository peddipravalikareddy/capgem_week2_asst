#10
#Build a `SmartPhone` class inheriting from `MobileDevice`, 
# which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.


class Electronics:
    device_category = 'Electronics'
    def scope(self):
        print("All the electronic devices")
    def showCategory(self):
        print(f"Category is: {Electronics.device_category}")
class MobileDevice(Electronics):
    Electronics.device_category  = "Mobile Device"
    def scope(self):
        print("Electronic devices that are mobile phones")
class SmartPhone(MobileDevice):
    Electronics.device_category  = "Smart Phone"
    def scope(self):
        print("All the mobile phones that are smart phones")
sp = SmartPhone()
sp.scope()
sp.showCategory()