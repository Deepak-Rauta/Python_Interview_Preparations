# Reverse a string 
def str_reverse(s):
    return s[::-1]
input_string = "Python"
result = str_reverse(input_string)
print(f"The original string is: {input_string}")
print(f"The reversed string id: {result}")


# prime number
def find_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
input_num = 24
if find_prime(input_num):
    print(f"The number {input_num} is prime number")
else:
    print(f"Thr number {input_num} is not a prime number")    

# factorial
def is_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * is_fact (n-1)
num = 7
print(f"The factorial of a number {num} is {is_fact(num)}")

# class Solution:
#     def __init__(self, num):
#         self.num = num
#     def is_pallindrome(self):
#         original_num = self.num
#         reversed_num = 0
#         num = self.num   # Copy the number to a local variable

#         while num > 0:
#             digit = num % 10 # check the last digit
#             reversed_num = reversed_num * 10 + digit  
#             num = num // 10 # zero division error
#         return original_num == reversed_num

# number = int(input("Enter the number:"))
# checker = Solution(number)
# if checker.is_pallindrome():
#     print(f"{number} is pallindrome")
# else:
#     print(f"The number is not pallindrome")


# anagram checker 
# def are_anagrams(str1, str2):
#     # remove spaces and convert it to lower case
#     str1 = str1.replace("","").lower() # This method remove all spaces 
#     str2 = str2.replace("","").lower()

#     # sort the character of both the string 
#     return sorted(str1) == sorted(str2)

# # example usage

# string1 = "listen"
# string2 = "silent"
# result = are_anagrams(string1, string2)
# if result:
#     print(f"{string1} and {string2} are anagrams")
# else:
#     print(f"{string1} and {string2} are not anagrams")


def are_anagrams(str1, str2):
    # remove spaces and convert it to lower cases
    str1 = str1.replace("","").lower()
    str2 = str2.replace("","").lower()
    # sorted the character of both the string
    return sorted(str1) == sorted(str2)
string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
if result:
    print(f"both {string1} and {string2} are anagrams")
else:
    print(f"Both {string1} and {string2} are not anagrams")


# fibonacci series
def fibonacci(n):
    # Define first two fibonacci number
    a, b = 0, 1
    fib_series = []

    for _ in range(n):
        fib_series.append(a) # append the current number to a list
        a,b = b, a+b
    return fib_series

# input the number of terms
num = int(input("Enter the number of series:"))
print(f"Fibonacci series:", fibonacci(num))

# sum of array
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [1,2,3,4,5,6]
print("The sum of array is:", sum_of_array(arr))

# Remove duplicate from a list
def remove_duplicate(lst):
    unique_element = set(lst)
    return list(unique_element)
# example uses
my_list = [1,2,4,6,6,8,9,3]
result = remove_duplicate(my_list)
print(result)

# count character frequency
def char_frequency(s):
    # Initialize a empty dictonary to store the character and frequency
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
my_string = "hello world"
result = char_frequency(my_string)
print(f"The frequency of the string is: {result}")

