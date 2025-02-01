#7
# #Create a multi-level class structure with `Person` → `Employee` → `Manager`,
#  where `Manager` has an additional method `approve_leave()`.

class Person:
    occupation = 'Free guy'
    def personMethod(self):
        print(f"{Person.occupation}")
class Employee(Person):
    Person.occupation = 'Employee in ABC Company'
    def employeeMethod(self):
        print(f"Employee method with occupation: {Person.occupation}")
class Manager(Employee):
    Employee.occupation = 'Manager in ABC company'
    def managerMethod(self):
        print(f"{Employee.occupation}")
    def approve_leave(self):
        print("Leave approved!")
emp = Employee()
emp.employeeMethod()
m = Manager()
m.personMethod()
m.managerMethod()
m.approve_leave()
