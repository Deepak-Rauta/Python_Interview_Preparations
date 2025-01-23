# # # Decorator:
# # # it is a special type of function that modifies the behavior of another function
# # # Decorators allows you to wrap a function, adding extra functionallity before or after the main function runs without chanaging its code.

# # # Example without decorator

# # # def say_hello():
# # #     print("Hello!")
# # # say_hello()



# # # Adding decorator
# # def my_decorator(func):
# #     def wrapper():
# #         print("something is happening before the function is called")
# #         func() # call the original function
# #         print("something is happening afterthe function is called")
# #     return wrapper

# # # now use the decorator

# # @my_decorator
# # def say_hello():
# #     print("Hello!")
# # say_hello()



# ### Decorator ####

# # in single words, a decorators in python is a wrapper
# # A decorator is a function that modifies or extends the behavior of another function or method without chanaging its actual code.
# # it's wrap the original function 

# # Common Use Cases of Decorators:

# # Logging: Automatically log function calls.
# # Authentication: Restrict access to functions based on certain conditions.
# # Timing: Measure the execution time of a function.
# # Caching: Cache the results of expensive function calls.
# # Validation: Check input arguments for validity before executing a function.

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx
# @greet
# def hello(): # here it basically modifies the hello function
#     print("Hello world!")
# # Here greet is a decorator and it decorate the hello function 
# # before and after hello function it doing something 
# @greet
# def add(a, b):
#     print(a + b)#

# hello()
# add(1, 2)
# # *args and **kwargs --->
# # *args takes arguments as a tuple 
# # **kwargs takes an arguments as dictonary

# # Example
def simple_decorator(func): # its a function, it takes a function as an arguments and return a new function wraper that wrap around the original func.
    def wrapper(): # The inner function does two things  it prints a message before and after calling the original function
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper
# Apply decorator to a function
@simple_decorator
def say_hello():
    print("Hello world!")

# call the decorator function
say_hello()


def simple_decorator(func):
    def wrapper(): # this function basically does two things
        print("Something is happen before the function")
        func()
        print("Somthing is happen after the function")
    return wrapper
@simple_decorator
def say_hello():
    print("Hello world")
say_hello()    












# # *args and **kwargs
# # Define a decorator that can accept any number of arguments 
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Arguments passed to the function:", args, kwargs)
#         result = func(*args, **kwargs) # call the original function with the arguments
#         print("Function excecuted successfully")
#         return result
#     return wrapper

# # Apply the decorator to a function with arguments 
# @my_decorator
# def add(a, b):
#     return a + b
# # now call the function
# result = add(10, 20)
# print("Result:", result)



def value_info(*args, **kwargs):
    print(f"Positional arguments(args):", args)
    print(f"Keyword arguments(kwargs):", kwargs)
value_info(1,2,3, name = "Deepak", Age = 22)


def my_info(*args):
    return sum(args)
result = my_info(1,2,3)
print(result)

def my_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_values(name = "Deepak", Age = 22, City = "HYD")



result = [i ** 2 for i in range(1, 11)]
print(result)


number = [1,2,3,4]
square = []
for num in number:
    square.append(num ** 2)
print(square)