# Encasulation is like putting data and function in a box(class).
# so we can control what goes in or out of the box.
# it helps to hide the inner details and only shows whats needed.
# the main idea is to restrict direct access to the internal data and provide collected access through methods 

# class Person:
#     def __init__(self, name, age):
#         self.__name = name # private attributes
#         self.__age = age  # private attributes

#     def get_name(self):  # public method to modify private name
#         return self.__name 
    
#     def set_age(self, new_age): # Public method to modify private age
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             print("Age must be positive")
#     def get_age(self):
#         return self.__age
# # create an instance of Person
# p = Person('Deepak', 22)

# # access data using public methods (encapsulation in action)
# print(p.get_name())
# print(p.get_age())

# # Modify data using public method
# p.set_age(30)
# print(p.get_age())

# # Try setting a negative age (controlled by method)
# p.set_age(-5)        # Output: Age must be positive!



class Person:
    def __init__(self, name, age):
        self.__name = name # private attributes
        self.__age = age # private attributes
    def get_name(self):
        return self.__name
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("pls enter a valid age")
    def get_age(self):
        return self.__age
p = Person("Deepak", 22)
print(p.get_name())
print(p.get_age())

p.set_age(30)
print(p.get_age())



class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.__balance = initial_balance  # Private attribute
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance is {self.__balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def view_balance(self):
        print(f"The current balance is {self.__balance}.")
        
# Example usage:
my_account = BankAccount("John Doe", 500)

my_account.view_balance()  # View balance
my_account.deposit(200)    # Deposit money
my_account.withdraw(100)   # Withdraw money
my_account.view_balance()  # View balance again

# Trying to access the private attribute directly (this will raise an error)
# print(my_account.__balance)  # Uncommenting this line will throw an AttributeError
