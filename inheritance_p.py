class Employee:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the age is {self.age}")
class Programmer(Employee):
    def showLanguage(self):
        print("Python is a vary famous language")
class Coder(Programmer):
    def showCode(self):
        print("Python code is very easy")
obj = Employee("Deepak", 22)
obj.showDetails()

obj1 = Programmer("Bikash", 23)
obj1.showDetails()
obj1.showLanguage()