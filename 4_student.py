# Implement a student class with a constructor that initializes name and roll number.
# Write a method to return Student Details.

class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    def studentDetails(self):
        print(f"Student Name: {self.name}\nStudent Roll No: {self.roll_number}")

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    stu = Student(name, roll)
    stu.studentDetails()