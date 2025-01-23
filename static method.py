# # static method in python is a method that belongs to a class, not its method
# class Math:
#     def __init__(self, num):
#         self.num = num

#     def addTonum(self, n):
#         self.num = self.num + n
#     @staticmethod
#     def add(a,b):  # it is a utility method. utility method basically design to perform common and reusable task
#         return a+b

# a = Math(5)
# print(a.num)    
# a.addTonum(6)
# print(a.num) 
# # result = Math.add(4,2)
# # print(result)
# print(a.add(2,4))
# print(Math.add(2,4))  # we also call in class name

#There is no need to require self arguments when we make a method in class we can also use the static method

class Math:
    def __init__(self, num):
        self.num = num
    def addtwo(self, n): # Instance method
       self.num = self.num + n 

    @staticmethod  # It is doesn't associated with class 
    def add(a, b): # It is a static method it doesn't connect with any instance method
        return a+b

result = Math.add(1,2)
print(result)
a = Math(5)
print(a.num)
a.addtwo(6)
print(a.num)

# print(a.add(3,4)) it is a ststic method but we also call it by using object and method name and also class.method name
# I need to build a utility method inside a class bcz sometimes i need to perform some complex problems 
# The effective concept of ststaic method is when we define a static method then there will no need to call the instance we can call it directly
# we use self bcz we refrence the object 

# print(add(3,7)) we also accessed this by this type but first we make the method outside the class 
# If we use static method then there will no need to pass the self arguments

class Employee:
    def __init__(self, num):
        self.num = num
    def addNumber(self, n):
        self.num = self.num + n
    @staticmethod
    def add(a, b):
        return a + b
obj = Employee(5)
print(obj.num)

obj.addNumber(3)
print(obj.num)





