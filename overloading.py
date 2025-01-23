# Python does not directly support the method overloading we can achive it by using 
# Default arguments
# variable arguments(*args, **kwargs)

# Using default arguments

class calculator:
    def add(self, a, b=0, c=0): # Default values for b and c
        return a+b+c
    
cal = calculator()
print(cal.add(5)) # for one parameters
print(cal.add(5, 10)) # for two parameters
print(cal.add(5, 10, 15)) # for three parameters
 

# using variable arguments
class Calculator:
    def add(self, *args):  # Accepts any number of arguments
        return sum(args)

calc = Calculator()
print(calc.add(5))          # Output: 5
print(calc.add(5, 10))      # Output: 15
print(calc.add(5, 10, 15))  # Output: 30
