# n = int(input("Enter the number of term:"))
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(2,n):
#     c = a+ b
#     print(c)
#     a = b 
#     b = c


#fibonacci series using recursion
# class Fibonacci:
#     def __init__(self):   #__init__ method initialize the instance of the class
#             self.memo = {} # Emptey dictonary it will store the previously calculated fibonacci number

#     def calculate(self, n):
#         """Calculate the nth Fibonacci number using recursion."""
#         if n <= 0:
#             return "Please enter a positive integer for the Fibonacci sequence."
#         elif n == 1:
#             return 0
#         elif n == 2:
#             return 1
#         elif n in self.memo:
#             return self.memo[n]
#         else:
#             result = self.calculate(n - 1) + self.calculate(n - 2)
#             self.memo[n] = result
#             return result

# # Example usage:
# fibonacci_calculator = Fibonacci()  #instance of the class
# try:
#     term = int(input("Enter the position of the Fibonacci term you want to calculate: "))
#     result = fibonacci_calculator.calculate(term)
#     print(f"The Fibonacci number at position {term} is: {result}")
# except ValueError:
#     print("Please enter a valid integer.")



# class Fibonacci:
#     def __init__(self):
#         self.memo = {}
#     def calculate(self, n):
#             """calculate the nth fibonacci number using recuression"""
#             if n <= 0:
#                 return """please enter a positive integer"""
#             elif n == 1:
#                 return 0
#             elif n == 2:
#                 return 1
#             elif n in self.memo:
#                 return self.memo[n]
#             else:
#                 result = self.calculate(n-1) + self.calculate(n-2)
#                 self.memo[n] = result
#                 return result
# fibonacci_calculator = Fibonacci()
# try:
#     term = int(input("Enter the no. of term:"))
#     result = fibonacci_calculator.calculate(term)
#     print(f'The fibonacci number at position {term} is {result}')   
# except ValueError:
#     print('please enter a valid number')             




# def fibonacci_series(n):
#     """Function to print Fibonacci series up to n terms."""
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# # Main code
# if __name__ == "__main__":
#     n = int(input("Enter the number of terms: "))
#     fibonacci_series(n)

def fibonacci_math(n):
    a, b = 1, 1  # Fibonacci starts from 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

print(fibonacci_math(5))  # Output: 5






           
