# *args:------->
# args allows you to pass a variable number of positional arguments to a function
# *args passed arguments as a tuple

# Example 
def greet(*args):
    for name in args:
        print(f"Hello {name}")
greet("Biaksh", "Roshan", "Deepak")


# **kwargs:-------------->

# kwargs allows you to pass a varibale number of keywords arguments (key-value pairs) to a function
# it takes arguments as a dictonary

def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
output = introduce(name = "Deepak", age = 22, salary = 40000)


