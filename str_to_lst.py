# Problem 1: Convert a comma-separated string to a list
# Problem:
# Write a program to convert the string "apple,banana,cherry" into a list of fruits.

string = "apple, banana, cherry"
fruit_lst = string.split(',')
print(fruit_lst)

# Convert the string "Python" into a list of individual characters.
string = "python"
char_lst = list(string)
print(char_lst)

# Convert the sentence "Python is fun" into a list of words.
string = "python is fun"
char_lst = string.split()
print(char_lst) 

# Given the string "1 2 3 4 5", convert it to a list of integers
string = "1 2 3 4 5"
number_lst = list(map(int, string.split()))
print(number_lst)

## map(): 
# The map() function in Python is commonly used to apply a specific function to each item in an iterable (like a list, tuple, or string) to transform its elements into a different data type or representation.
# syntax:---->
# map(function, iterable)

# Convert the sentence "Hello, world! How are you?" into a list of words without punctuations.
# punctuations like , ! and ?

# string.punctuation
# # Output: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

import string
sentence = "Hello, world! How are you?"
# Remove punctuations with str.translate()
word_list = sentence.translate(str.maketrans('', '', string.punctuation)).split()
# The str.maketrans() function creates a translation table for replacing or removing characters.
# The first '' is for characters to replace (none in this case).
# The second '' is for characters to insert (none in this case).
# The third string.punctuation is for characters to remove.
# translate () method applies the translation table to the string
print(word_list)

# Given the string "red-blue-green-yellow", convert it to a list of colors.

string = "red-blue-green-yellow"
colors_list = string.split("-")
print(colors_list)  # Output: ['red', 'blue', 'green', 'yellow']


# Convert the string "Line1\nLine2\nLine3" into a list of lines
string = "Line1\nLine2\nLine3"
str_lst = string.splitlines()
print(str_lst)

# Convert the string "apple,,banana,,,cherry" to a list and remove the empty strings.
string = "apple,,banana,,,cherry"
fruits_lst = [item for item in string.split(",") if item]
print(fruits_lst)

# Convert the string "ABC" into a list of ASCII values of each character.
string = "ABC"
ascii_list = [ord(char) for char in string]
print(ascii_list)  # Output: [65, 66, 67]

# Convert "abcdef" into a list of every alternate character.
string = "abcdefghij"
alternate_list = list(string[::2])
print(alternate_list)

# string[start:stop:step]