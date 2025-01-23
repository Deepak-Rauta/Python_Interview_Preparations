
# Basic list comprehension---->
squares = [i**2 for i in range(1,11)]
print(squares)

# filtering with list comprehension---->
my_list = [1,2,3,4,5,6,7,8,9]
even_lst = [i % 2 == 0 for i in my_list]
print(even_lst)

# Nested list comprehension----->
# Q. Use list comprehension to flatten a 2D matrix into a 1D list.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flattened_list = [element for row in matrix for element in row]
print(flattened_list)

# Conditional list comprehension------>
# Given a list of integers, write a list comprehension to create a new list containing the absolute values of the negative numbers only. 
lst = [10,-20,30,-40,50,60,-70]
# absolute value: absolute value of a number is always non-negative, even if the number itself is negative.
result = [abs(num) for num in lst if num < 0]
print(result)
# Basically it gives the absolute values of the negetive numbers 

# List comprehesion with string manipulation------>
#Write a list comprehension to convert a list of words to uppercase, but only for words that have more than three letters.
    
string = ['python','was','fun']
result = [char.upper() for char in string if len(char) > 3]
print(result)

# Using function in lisrt comprehension----->
import re
words = ['Hey','how','are','you']
removal_v = [re.sub(r'[aeiouAEIOU]','',word)for word in words]
print(removal_v)


words = ["Hey","How","Are","You"]
vowels = "aeiouAEIOU"
translator = str.maketrans('','',vowels)
result = [word.translate(translator)for word in words]
print(result)

# Multiple if condition------>
result = [num for num in range(1,51) if num % 3 == 0 and num % 5 == 0]
print(result)

# List comprehension with enumerates------>
names = ["Sonu","Nita"]
result = [(index,name) for index,name in enumerate(names)]
print(result)

# Nested loop with list comprehension--------->
list_1 = [1,2,3]
list_2 = ['a','b','c']

pairs = [(i,j) for i in list_1 for j in list_2]
print(pairs)

# Dictonary to List Comprehension-------->
dict = {'Name': 'Deepak', 'Age': 21, 'City': 'Hyderabad'}
result = [f"{key}: {value}" for key,value in dict.items()]
print(result)

# here dict.item() return a views of dictonary items 
dict = {'Name':'Deepak', 'Age':21}
result = [f"{key}:{value}" for key,value in dict.items()]
print(result)

# if-else condition using list comprehension
# Q1
even_odd_list = ['Even' if num % 2 == 0 else 'odd' for num in range(1,11)]
print(even_odd_list)

# Q2 Given a list of integers, write a list comprehension to create a new list where each number is doubled if it is even, and tripled if it is odd.
# Basic step:--->
# we want to create a new list where:
     # Each even number is doubled
     # Each odd number is tripled

# for loop : [<output> <for loop>]
# for-if : [<output> <for loop> <if-condition>]
# for if else : [<if out> <if con> <else> <else output> <for loop>]
# for if elif else : There is no elif condotion in list comprehension


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [num * 2 if num % 2 == 0 else num * 3 for num in numbers]
print(new_list)

# Q3

generated_txt = ['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(1,16)]
print(generated_txt)

generate_txt = ['Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else 'FizzBuzz' if num % 3 == 0 and num % 5 == 0 else num for num  in range(1,16)]
print(generated_txt)

# Q4
my_lst = ['hey', 'how', 'are', 'you']
result = [''.join([char.upper() if char in 'aeiouAEIOU' else char.lower() for char in word]) for word in my_lst]
print(result)

#Given a list of strings, use list comprehension to create a new list where each string is converted to uppercase if it starts with a vowel, otherwise convert it to lowercase. pls give me the solution

strings = ['apple', 'Banana', 'orange', 'grape', 'umbrella', 'Peach']
result = [word.upper() if word[0].lower() in 'aeiou' else word.lower() for word in strings]
print(result)

# word[0].lower()---->
# Continuing the example above, word[0].lower() would take 'A' and convert it to 'a'.

# Q5
result = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(1,11)]
print(result)

# Q6
# convert list of temprature in celsius to fahrenhit for temp above 0c 
# for temp  0 or below 0c keep the temp as is
celsius_tmp = [10,0,-20,-30,50,60]
fahrenhit_tmp = [(temp * 9/5) + 32 if temp > 0 else temp for temp in celsius_tmp]
print(fahrenhit_tmp)


fahrenhit_temp = [60, 0, -20, -25, 40]
celcius_temp = [round((temp - 32) * 5/9, 2) if temp > 0 else temp for temp in fahrenhit_temp]
print(celcius_temp)

# Q7
str = ['Deepak','Bikash','omm','Roshan']
result = [i[:3] if len(i) > 5 else i for i in str]
print(result)





