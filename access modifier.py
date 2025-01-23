## When we make a class in python by default their there variable are in public we also make it private.
## Three types of access modifier presents in python:- public, private, protected

## public access modifier:-
# class Student:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

# obj = Student(22, 'Deepak')
# print(obj.age)
# print(obj.name)  

# ## self.name and self.age are publically accessed

# ## private access modifier:-
# class Student:
#     def __init__(self, age, name):
#         self.__age = age  ##we can not access the variables
#         self.name = name

# obj = Student(22, 'Deepak')
# #print(obj.age)  ## cannot be access directly
# print(obj._Student__age) ## we can access the variables like this
# print(obj.name)

# print(obj.__dir__()) # means what are the method are available in this program all are shown by the dir method


# protected access modifier:-
# class Student:
#     def __init__(self):
#         self._name = "Deepak"

#     def _funName(self):
#         return "I love my parents"

# class subject(Student):
#     pass

# obj = Student()
# obj1 = subject()

# # calling by object of student class-
# print(obj._name)
# print(obj._funName())

# # calling by object of  subject class:-
# print(obj1._name)
# print(obj1._funName())


## if we use Double underscore(__) the in this case python magling it




# public access modifier
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# obj = Employee("Deepak", 22)
# print(obj.name)
# print(obj.age)

# Here self.name and self.age are publically protected

# private access modifier 

# class Employee:
#     def __init__(self):
#         self.__name = "Deepak"
        
# a = Employee()
# print(a.__name) # we can not be access
# print(a._Employee__name) # can be access in directly
# print(a.__dir__())



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Its my private attributes

    def __show_balance(self): # its my private methods
        print(f"Balance: {self.__balance}")

    def get_balance(self):
        self.__show_balance()  # can call the private methods witin the class

account = BankAccount(1000)
account.get_balance() # here the output is Balance 1000

# For making private attribute the basic syntax is .__attributes name
# For making private method we use def __mathod_name


