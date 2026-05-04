# Concept Name: Inheritance (Single, Multilevel, and Multiple) and the super() function.

"""Simple Explaation: Inheritance allow us to create a new class (the child or sub class) that takes on all the attributes and methods of an existing class (the parent or superclass). Instead of copying and pasting code, the child simply "inherits" everything from the parent, and can then add its own unique features or override existing ones."""

"""Single Inheritance: One child inherits from one parent.

Multilevel Inheritance: A child inherits from a parent, and then another child inherits from that child (like Grandparent ➔ Parent ➔ Child).

Multiple Inheritance: One child inherits from two or more parents at the same time (unique to languages like Python!)."""


# 1. The parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Methods
    def work(self):
        print(f"{self.name} is working hard!")

# 2. The child class (single inheritance)
# We put the parent class in paranthesses to inherit from it
class Manager(Employee):
    def __init__(self, name, salary, department):
        # super() calls the parent's __init__ so we don't repat the code.
        super().__init__(name, salary)
        self.department = department

    # The manager has a unique method the regular employee don't have
    def hold_meeting(self):
        print(f"{self.name} is holding a meeting for the {self.department} department")

# 3. Testing it out
emp = Employee("Deepak", 50000)
mgr = Manager("Bob", 90000, "IT")

# Deepak can work but cannot hold meetings
emp.work()

# Bob can hold meetings, AND he inherited the ability to work!
mgr.hold_meeting()
mgr.work()
       
