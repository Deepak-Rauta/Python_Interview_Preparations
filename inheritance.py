# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def showDetails(self):
#         print(f'The name of employee: {self.id} is {self.name}')

# class programmer(Employee):
#     def showLanguage(self):
#       print('I love python!')        

# e1 = Employee('Deepak', 101)
# e1.showDetails()
# e2 = programmer('Bikash', 102)
# e2.showDetails()
# e2.showLanguage()

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f'The name of the employee is {self.name} and id is {self.id}')

# class programmer(Employee):
#     def showLanguage(self):
#         print('I love python')

# e = Employee('Deepak', 101)
# e.showDetails()

# e2 = programmer('Biaksh', 102)
# e2.showDetails()

# e2.showLanguage()

## Inheritance allows us to define a class that inherits all the methods and prioperties from another class


# Inheritance allows a class to inherit its properties and method from another class
# it also establish a parent child relationship between the code 

# class Employee:
#     def __init__(self, id, name):
        
#         self.id = id
#         self.name = name
#     def showDetails(self):
#         print(f"The employee id is {self.id} and name is {self.name}")

# class programmer(Employee):
#     def showLanguage(self):
#         print("The default language is python")

# class coder(programmer):
#     def showCode(self):
#         print("The default code is Inheritance")

# obj = Employee(101, "Deepak")
# obj.showDetails()

# obj1 = programmer(102, "Bikash")
# obj1.showDetails()
# obj1.showLanguage()

# obj2 = coder(103, "Roshan")
# obj2.showDetails()
# obj2.showCode()



class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def showDetails(self):
        print(f"The Employee id is: {self.id} and name is: {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("Python is a vary famouse Language")

class Coder(programmer):
    def showCode(self):
        print("Python have small amount of code")

obj = Employee(101, "Deepak")
obj.showDetails()

obj1 = programmer(102, "Bikash")
obj1.showDetails()
obj1.showLanguage()

obj2 = Coder(103, "Roshan")
obj2.showDetails()
obj2.showCode()





