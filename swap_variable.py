# 1️⃣ Variables in Python
# What are Variables?

# A variable is a name that refers to a value stored in memory.
# Python is dynamically typed, so no need to declare the type explicitly.

# ✅ Declare a variable name and assign your name to it.
# ✅ Swap two variables without using a third variable.
# a, b = 10, 5
# a, b = b, a
# print(a, b)

# numbers = [1, 2, 3, 3, 4, 5]
# result = set(numbers)
# print(result)

# 🔹 Variables & Data Types Questions
# 1️⃣ Swap two numbers without using a third variable.

def swap_variable(a, b):
    return b, a  # Returning swapped values

a = 10
b = 5
a, b = swap_variable(a, b)  # Unpacking the returned values
print(a, b)  # Output: 5 10

# 2️⃣ Check if a given number is an integer or a float.
# using ininstance
def check_number_types(num):
    if isinstance(num, int):
        return "Integer"
    elif isinstance(num, float):
        return "Float"
    else:
        return "Neither integer or float"
number = 12.34
result = check_number_types(number)
print(result)

# using type():---->
def check_number_type(num):
    if type(num) == int:
        return "Integer"
    elif type(num) == float:
        return "Float"
    else:
        return "Neither Integer nor Float"

print(check_number_type(42))    # Output: Integer
print(check_number_type(3.14))  # Output: Float

# 4️⃣ Find the second largest number in a list.
def Second_largest(num):
    num = list(set(num))
    if len(num) < 2:
        return "No second largest elements"
    num.sort(reverse=True) # sort in descending order
    return num[1] # second elements in the second largest
print(Second_largest([10, 4, 5, 7, 9, 8, 1]))

# 5️⃣ Remove duplicates from a list while maintaining order.
def Remove_Duplicate(nums):
    unique_number = list(dict.fromkeys(nums))
    return unique_number
print(Remove_Duplicate([10, 3, 3, 4, 6, 4, 2, 1, 2]))

# Why Use fromkeys() to Remove Duplicates While Maintaining Order?
# The fromkeys() method is used because dictionaries in Python maintain insertion order (since Python 3.7+). 
# By using dict.fromkeys(), we can automatically remove duplicates while preserving the original order of elements.
# Insertion order means that elements are stored and retrieved in the same order they were added.
# Dictionary preserving insertion order
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)


# 🔹 Conditional Statements Questions
# prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
number = 12
if is_prime(number):
    print(f"{number} is Prime Number")
else:
    print(f"{number} is Not a Prime Number")

# Leap yaer
def LeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap yaer")
        
# Loop Questions
# 1️⃣1️⃣ Print all even numbers from 1 to 50.

# Even number
def IsPrime(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)
IsPrime(1, 10)

# Sum of digits
def sum_of_digits(n):
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10 # Get the last digit
        n //= 10
    return sum_of_digits
print(sum_of_digits(123))

# 2nd methods
def sum_of_digits(n):
    return sum(map(int, str(n)))

print(sum_of_digits(123))  # Output: 6

# Find factorial of a number
def Find_Factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial
print(Find_Factorial(5))

# Factorial using recusrssion:-
def Fact_Rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Fact_Rec(n-1)
print(Fact_Rec(5))


#factorial for non-negetive integer
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


# Fibonacci Series
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci_series(5)

print('\n')

# Second largest
def Sec_Largest(n):
    num = list(set(n))
    if len(num) < 2:
        "Return there is no second largest elements"
    num.sort(reverse=True) # Sort in descending order
    return num[1]
print(Sec_Largest([10, 6, 7, 9, 12, 15]))

# Methods-1
def Find_Largest(lst):
    largest = lst[0] # Initialize the first elements is the largets elements
    for elements in lst:
        if elements > largest:
            largest = elements
    return largest
list = [1, 2, 10, 4, 5]
print(Find_Largest(list))

# using list sorting------>
def find_largest(lst):
    if not lst:
        return None
    lst.sort()  # sorting the list into ascending order
    return lst[-1] # it return last number as the largest number
my_list = [1,9,4,7,8,3,2]
largest_number = find_largest(my_list)
print(f"The largest number in the list is {largest_number}")
