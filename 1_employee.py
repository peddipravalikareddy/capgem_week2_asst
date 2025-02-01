#1.Create a class `Employee` with properties `name`, 
# `id`, and `department`. Instantiate an object and assign values dynamically.

class Employee:
    def Details(self,name,id,department):
        self.employeeName=name
        self.id=id
        self.department=department
    def get_employee_info(self):
        print (f'Name: {self.employeeName} \nId: {self.id} \nDepartment: {self.department}')
        print() 
a=input("enter the name of employee ")
b=input("enter the employee_id ")
c=input("enter the department ")

A=Employee()
A.Details(a,b,c)
A.get_employee_info()


    
