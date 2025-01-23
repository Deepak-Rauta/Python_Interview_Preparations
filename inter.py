# WAP reverse a string
# def is_reverse(s):
#     return s[::-1]
# input_string = input()
# reversed_string = is_reverse(input_string)
# print(f"The original string is {input_string}")
# print(f"The reverse string is {reversed_string}")





# def is_reverse(s):
#     return s[::-1]
# input_string = input()
# reversed_string = is_reverse(input_string)
# print(f"The original string is {input_string}")
# print(f"The reversed string is {reversed_string}")


## wap factorial of number

# def is_factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*is_factorial(n-1)
    
# n = int(input("Enter a number:"))
# print(f"factorial of a number is {is_factorial(n)}")


## prime number

# num = int(input("Enter the number:"))
# if num == 1:
#     print("1 is neither prime nor composite")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("The number is not a prime number")
            
#         else:
#             print("The number is prime number")

# num = int(input("Enter a number:"))
# if num == 1:
#     print("1 is not prime nor composite")
# else:
#     for i in range(2, num):
#         if num%i==0:
#             print(f"The {num} is prime number")
#         else:
#             print(f"The {num} is not a prime number")





def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
    
number = 24
if is_prime(number):
     print(f"{number} is a prime number")
else:
     print(f"{number} is not a prime number")



def is_fact(n):
    if n==0:
        return 1
    else:
        return n*is_fact(n-1)
number = 5
print(f"The factorial of the {number} is {is_fact(number)}")


def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage
number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")


# def is_pallindrome(num):
#     # convert the number to string
#     num_str = str(num)
#     # check if the string is equal to its reverse string or not
#     return num_str == num_str[::-1]

# number = int(input("Enter a number:"))
# if is_pallindrome(number):
#     print(f"{number} is a palindrome")
# else:
#     print(f"{number} is not a palindrome")


def is_pallindrome(num):
    original_num = num  ## it store the original number
    reversed_num = 0
    while num > 0:
        digit = num % 10  # extract the last digit
        reversed_num = reversed_num * 10 + digit
        num = num//10 # integer division by zero

    return original_num == reversed_num
number = int(input("Enter the number:"))
if is_pallindrome(number):
    print(f"The {number} is pallindrome")
else:
    print(f"The {number} is not pallindrome")


# my_list = [1,2,3,4]
# my_list.remove(3)
# print(my_list)


# my_list = [1, 2, 3, 4, 5]
# sub_list = my_list[2:5]  # [2, 3, 4]
# print(sub_list)

# list comprehension provide a concise way to create a list
# square = [x**2 for x in range(5)]
# print(square)

# my_dict = {"a": 1, "b": 2, "c": 3}
# my_dict.pop("b")        # {"a": 1, "c": 3}
# #del my_dict["a"]        # {"c": 3}
# print(my_dict)

# square = {x: x**2 for x in range(5)}
# print(square)

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#         return True
# n = 29
# if is_prime(n):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")


# Find the largest element in a list----->
def find_largest_element(lst):
    # check if the list is empty
    if not lst:
        return None
    # initialize the largest element as the first element of the list
    largest = lst[0]

    # Loop through the list to find the largest element
    for element in lst:
        if element > largest:
            largest = element
    return largest
my_list = [3,5,7,8,9,4,2,6]
largest_number = find_largest_element(my_list)
print(f"The largest number in the list is {largest_number}")

## Using enumerate------>

# def find_largest_element(lst):
#     if not lst:
#         return None
#     largest = lst[0]
#     for index, element in enumerate(lst):
#         if element > largest:
#             largest = element
#     return largest

# # Example usage
# numbers = [3, 5, 2, 9, 4, 10, 6]
# largest_number = find_largest_element(numbers)
# print("The largest element in the list is:", largest_number)


# using list sorting------>
# def find_largest(lst):
#     if not lst:
#         return None
#     lst.sort()  # sorting the list into ascending order
#     return lst[-1] # it return last number as the largest number
# my_list = [1,9,4,7,8,3,2]
# largest_number = find_largest(my_list)
# print(f"The largest number in the list is {largest_number}")

## using max built-in method

# def find_largest(lst):
#     if not lst:
#         return None
#     return max(lst)
# my_list = [1,10,4,7,8,3,2]
# largest_number = find_largest(my_list)
# print(f"The largest number in the list is {largest_number}")


# my_mark = [70,78,85,60,88]

# for index, element in enumerate(my_mark):
#     if my_mark == 88:
#         print("Good!")


# list compheresion------>

# numbers = [1,2,3,4,5,6]
# squares = [number ** 2 for number in numbers]
# print(squares)


# without enumerate----->
# lst = [10,20,30,40]
# n = len(lst)
# for i in range(n):
#     print(f"Index: {i}, Value: {lst[i]}")

# with enumerate ----->

# lst = [10,20,30,40]
# for index, value in enumerate(lst):
#     print(f"Index: {index}, Value: {value}")


# lst = [10, 20, 30, 40]
# for index, value in enumerate(lst):
#     print(f"Index: {index}, Value: {value}")


## Basic splitting----->
s = 'apple,banana,cherry'
l = s.split(',')
print(l)


# custom Delimeter---->
# s = 'dog#cat#mouse'
# o = s.split('#')
# print(o)


## Limiting the number of solits--->
# we split the string into 2 parts so...we use maxsplit function
# s = 'red,green,blue,yellow'
# result = s.split(',', maxsplit=2)
# print(result)
# after set maxsplit into 2 it split the string into 3 parts

## splitting on multiple delimeter---->
# to solve the split on multiple delimeter we use re.split() function
# re(regular expression)
# import re
# s = "hello:world;python-programming"
# result = re.split(r'[:;\-]',s)
# print(result)
# r[:;\-] basically match any of the delimeter like :;\-


## strip() basically removes the white spaces at the begining and at the end

# s = "   Hello, World!   "
# cleaned_s = s.strip()
# print(cleaned_s)

# # also removing specific cheracter
# s = "###Python###"
# cleaned_s = s.strip('#')
# print(cleaned_s)



##splitting a paragraph into sentence----->
# s = "This is a sentence. And this is another. yet another one"
# sentences = s.split('.')
# # remove any extra space or empty strings that might result from split
# sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
# print(sentences)




# s = "Various educators teach rules governing the length of paragraphs. They may say that a paragraph should be 100 to 200 words long"
# sentences = s.split('.')
# sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
# print(sentences)

## Extracting word fro sentence---->
# If you have a sentence s = "Python is fun!", how would you split the sentence into words using the split method and remove any punctuation?

# To split the sentence into words and remove punctuation, you can use a combination of split() and str.translate() with str.maketrans() to handle punctuation.

# import string

# s = "python is fun!"

# # Create a translation table to remove punctuation
# translator = str.maketrans('','',string.punctuation)

# # Remove punctuation from the string
# cleaned_s = s.translate(translator)

# # Split the cleaned string into words
# words = cleaned_s.split()

# print(words)

# str.maketrans()
## creates a mapping or translate table that tells python how to replace or
# remove specific cheracter in a string

# str.translate()
##What it does: Uses the translation table created by str.maketrans() to actually change the string according to 
# the rules you've set (replacing or removing characters).


#s = "apple!"

# Create a translation table: replace 'a' with 'x', and remove '!'
# table = str.maketrans('a', 'x', '!')

# # Apply the translation table to the string
# result = s.translate(table)

# print(result)  # Output: "xpple"


import string
s = "my name is Deepak!!"
translator = str.maketrans('','',string.punctuation)
cleaned_s = s.translate(translator)
words = cleaned_s.split()
print(words)


# s = "apple!"
# table = str.maketrans('a','x','!')
# words = s.translate(table)
# print(words)

## Splitting by new line characters:
# s = "Line1\nLine2\nLine3"
# # result = s.splitlines()
# # print(result)

# lines = s.split('\n')
# print(lines)

# splitlines():
# This method splits the string s wherever it finds a newline character (\n), or any line break sequence, and returns a list of individual lines.

## Handling extra space---->
# s = "  too many spaces "
# #result = s.strip()
# result = s.split()
# print(result)


## splitting a path
##Given a file path s = "/home/user/docs/file.txt", how can you split this path into individual directories and the file name?

# s = "/home/user/docs/file.txt"
# result = s.split('/')
# print(result)


## Splitting on a Specific Character and Keeping the Delimiter:
## If you have the string s = "word1-word2-word3", how can you split the string while keeping the delimiter - with each split part?
# import re
# s = "word1-word2-word3"
# result = re.split(r'(-)',s)
# print(result)


l1 = [1, 2, 3, 4, 5, 6, 7, 2, 8, 9, 2, 10]
# now find the first occurence of 2
i1 = l1.index(2) # now l1 will be assigned the value will be 1
# now find the second occurence of 2
i2 = l1.index(2,1+i1) # previously i1 = 1 now 1+1 = 2
# means the search for 2 strat at index 2
# removing the element at the second index
l1.pop(i2)
print(l1)

# remove duplicate from a list:
# To remove duplicate from a list in python, the most common method is to convert
# the list into a set and then back into a list.since sets autometically remove duplicates
# method using set():

my_list = [1,2,2,3,4,4,5,5,6,7]
my_list = list(set(my_list))
print(my_list)

def duplicate_lis(lst):
    return list(set(lst)) # It is a commom python idiom to remove duplicate from a list
#Example uses
original_lis = [1,2,2,3,4,4,5]
duplicate_list = duplicate_lis(original_lis)
print(duplicate_list)

#using a loop to maintain order------->

my_list = [1,2,3,1,3,2,4]
# Remove duplicates while maintaing orders
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(f"The unique list is: {unique_list}")



# def find_largest(lst):
#     if not lst:
#         return None
#     # Initialize the largest element as the firt element of the list
#     largest = lst[0]
#     for element in lst:
#         if element > largest:
#             largest = element
#     return largest
# my_list = [1,2,5,6,8,9]
# result = find_largest(my_list)
# print(f"The largest element in the list is: {result}")


def find_largest(lst):
    if not lst:
        return None
    lst.sort()
    return lst[-1]
my_list = [1,2,5,6,8,9]
result = find_largest(my_list)
print(f"The largest element in the list is: {result}")

