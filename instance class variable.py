

# Instance variables are not associated with class
class Employee:
    companyName = "Deloitte"   # after making it companyname is associated with class
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 # for this it will create a instance 
        Employee.noOfEmployee += 1
    def showDetails(self):
        print(f"The name of the employee is: {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

emp = Employee("Deepak")
emp.raise_amount = 0.04  # it is associated with instance 
emp.name = "Roshan"
emp.companyName = "Deloitte India"
emp.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)
# we also directly change the raise_amount of a perticular employee

emp1 = Employee("Bikash")
emp1.companyName = "Amazon"
emp1.showDetails()
#Employee.showDetails(emp)

# in above both emp.showdetails and employee.showdetails are equal 
# when we write emp.showdetails() it convert to Employee.showDetails()
# def showDetails(self): in this method if we remove self then we getting the error 
# The error is showDetails take 1 positional arguments but zero is given
# if we write Employee.showDetails(emp) it takes a one argumets 
# but in the def showDetails() there will be zero arguments but one are given 
# By default it takes self

# It coluld be very lengthy method to make separate raise_amount or different features of different employee
# instead of doing this we make a variable that is associated with class

# Here companyName is associated with class 
# emp.raise_amount is instance variable 

# first of all it check is there instance variable present if it is present then it shown the instance vaeriable 
# Otherwise it goes to the class variable 



# Example 2

class Car:
    # class variable (shared by all instances)
    wheels = 4

    def __init__(self, brand, color):
        # Instance variables unique to all instances
        self.brand = brand
        self.color = color
# creating instance objects for the class car
car = Car("Toyota", "Black")
car1 = Car("TATA", "Red")

# Accessing instance variables
print(car.brand)
print(car1.color)

# Accessing the class variables
print(car.wheels)
print(car1.wheels)

#modifying the instance variable of car
car.color = "white"
print(car.color)
print(car1.color)

# Modifying the class variable 
Car.wheels = 7
print(Car.wheels)
print(car.wheels)
print(car1.wheels)