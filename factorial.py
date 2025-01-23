# num = int(input("Enter the number"))
# factorial = 1
# for i in range(1, num+1):
#     factorial *= i
# print(factorial)    

# def factorial(n):
#     if n==0 or n==1:
#      return 1
#     else:
#        return n*factorial(n-1)
# number = int(input("Enter the number:")) 
# result = factorial(number)  
# print(f'The factorial of {number} is {result}')  


# #factorial for non-negetive integer
# def factorial(n):
#     """Calculate the factorial of a non-negative integer."""
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

# # Example usage:
# number = int(input("Enter a non-negative integer: "))
# result = factorial(number)

# print(f"The factorial of {number} is: {result}")

# #using class
# class Factorial:
#     def __init__(self, n):
#         self. n = n
#     def calculate(self,n):
#         if n == 0 or n ==1:
#             return 1
#         else:
#             return n * self.calculate(n-1) 
# #Example usages

# number = int(input("Enter a positive number to check the factorial:"))
# factorial_calulate = Factorial(number)
# result = factorial_calulate.calculate(number) 
# print(f'The factorial of {number} is {result}')                  

# class Factorial:
#     def __init__(self, n):
#         self.n = n
#     def calculate(self, n):
#         if n == 0 or n == 1:
#             return 1
#         else:
#             return n * self.calculate(n-1)
# #Example uses
# number = int(input("Enter a positive number to check the factorial:"))
# factorial_calculator = Factorial(number)
# result = factorial_calculator.calculate(number)
# print(f'The factorial of {number} is {result}')   


class Factorial:
    def __init__(self, n):
        self.n = n
    def calculate(self, n):
        if n==0 or n==1:
            return 1
        else:
            return n * self.calculate(n-1)
#Example usages
number = int(input("Enter the positive number to check the factorial number:"))
class_instance = Factorial(number)
result = class_instance.calculate(number)
print(f'The factorial {number} is {result}')                





