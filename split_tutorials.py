# Q1
sentence = "Hello, welcome to the world of Python"
# Expected output: ['Hello,', 'welcome', 'to', 'the', 'world', 'of', 'Python']
result = sentence.split()
print(result)

# Q2
filename = "example.txt"
# Expected output: "txt"
result = filename.split('.')[-1]
print(result)

# Q3
sentence = "Python is fun"
# Expected output after join: "Python-is-fun"
result = "-".join(sentence.split())
print(result)

# Q4
email = "user@example.com"
# Expected output: ['user', 'example.com']
results = email.split('@')
print(results)

# Q5
sentence = "Hello world"
# Expected output: "world Hello"
results = " ".join(sentence.split() [::-1])
print(results)

# After split "Hello world"---> ['Hello', 'world']
# after split it reverse the list using [::-1]
#result should be ['world', 'Hello']
# after join this, basically join() method join elements of a lsit into a single string

# Q6
# split and capitalize
sentence = "hello world python"
# Expected output: ['Hello', 'World', 'Python']
result = [word.capitalize() for word in sentence.split()]
print(result)

# Tricky Ques
sentence = "this is a tricky question and you have to solve it"
result = [word.capitalize() if i % 2 == 1 else word for i, word in enumerate(sentence.split())]
print(result)

# Tricky-2
sentence = "python programming is really fun to learn"
print(len(sentence))
# Expected output:
# ['Python', 'programming', 'is', 'really', 'fun', 'to', 'Learn']
# split the sentence into words
words = sentence.split()
# capitalize the first and last word while leaving the others unchanged
result = [words[i].capitalize() if i == 0 or i == len(words) -1 else words[i] for i in range(len(words))]
print(result)

############################
sentence = "python programming is fun"
words = sentence.split()
result = [words[i].capitalize() if i == 0 or i == len(words) - 1 else words[i] for i in range(len(words))]
print(result)

# Q7
# method 1
sentence = "This is a Python coding challenge"
# Expected output: 6
words = sentence.split()
count = 0
for i in range(len(words)):
    count = count + 1
print(count)
# method2
sentence = "This is a Python coding challenge"
words = sentence.split()
count = len(words)
print(count)

# Q8
# Split a String into Substrings of Equal Length
# Write a function that splits a string into substrings of equal length (e.g., length 3)
string = "abcdefghijklm"
print(len(string))
# Expected output for length 3: ['abc', 'def', 'ghi', 'jkl', 'm']
chunk_size = 3
result = [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]
print(result)

# Q9
# split based on delimeter
data = "apple;orange;banana;grapes"
# Expected output: ['apple', 'orange', 'banana', 'grapes']
result = data.split(';')
print(result)

# Q10
sentence = "apple orange apple banana apple"
word = "apple"
# Expected output: 3
words = sentence.split()
count = words.count(word)
print(count)

# Q11
# Split and Filter Numeric Strings
import re
string = "abc 123 xyz 456 789"
# Expected output: ['123', '456', '789']
numbers = re.findall(r'\d+', string)
print(numbers)

# r'\d+' -------> This is the regular expression pattern used to find sequence of digits
# \d ----> matches any digit
# + ----> means one or more of the preceding element

# Extracting user name and domain
email = "deepak@gmail.com"
# splitting at the '@' to extract user name and domain
parts = email.split('@')
print(f"username: {parts[0]}")
print(f"Domain: {parts[1]}")

# using indexing and slicing 
email = "deepak@gmail.com"
at_index = email.index('@') # it gives the position of '@'
# slice the string using the index of '@'
user_name = email[:at_index]
domain = email[at_index+1:] # every things after the '@'

print(f"usernames: {user_name}")
print(f"domains is: {domain}")

# Handling different emails with indexing 
email1 = "john.doe@company.org"
email2 = "admin@website.net"

# for emails1
at_index_1 = email1.index('@')
username1 = email1[:at_index_1]
domain1 = email1[at_index_1+1:]

# for emails2
at_index_2 = email2.index('@')
username2 = email2[:at_index_2]
domain2 = email2[at_index_2+1:]

print(f"The usename is: {username1} and the domain is {domain1}")
print(f"The username is: {username2} and the domain is {domain2}")


# from jupyter note book session 15
string1 = 'virat.kohli@rcb.com, Rohit.sharma@mi.co, Dhoni.mahendra@csk.co'
# split the string by comas and spaces to separate each email
email_list = string1.split(", ")
# Loop through each email in the list
for email in email_list:
    first_dot_index = email.index('.') # first dot
    second_dot_index = email.index('.',first_dot_index+1) # finds dot that comes after the first one 
    # second_dot_index = email.index('.',5+1) # after the first dot at position 6
    at_the_index = email.index('@') # find the '@' symbol to identify where the domain starts 

    # Extract first name, last name, and company name
    f_name = email[:first_dot_index]
    s_name = email[first_dot_index + 1:at_the_index]
    c_name = email[at_the_index + 1:second_dot_index]

    # print the result 
    print(f_name.capitalize(), s_name.capitalize(), c_name.upper())


string2 = "deepak.rauta.mca.2022@nist.edu"

first_dot_index = string2.index('.')
second_dot_index = string2.index('.', first_dot_index+1)
third_dot_index = string2.index('.', second_dot_index+1)
at_the_index = string2.index('@')
fourth_dot_index = string2.index('.', third_dot_index+1)

f_name = string2[:first_dot_index]
s_name = string2[first_dot_index+1 : second_dot_index]
t_name = string2[second_dot_index+1 : third_dot_index]
f1_name = string2[third_dot_index+1 : at_the_index]
l_name = string2[at_the_index+1:]

print(f_name,s_name,t_name,f1_name,l_name)


string2 = "deepak.rauta.mca.2022@nist.edu"

# Finding the positions of the dots and '@'
first_dot_index = string2.index('.')  
second_dot_index = string2.index('.', first_dot_index + 1)  
third_dot_index = string2.index('.', second_dot_index + 1)  
fourth_dot_index = string2.index('.', third_dot_index + 1)  
at_the_index = string2.index('@')

# Extracting the parts based on the dot and '@' positions
f_name = string2[:first_dot_index]
s_name = string2[first_dot_index + 1 : second_dot_index]
t_name = string2[second_dot_index + 1 : third_dot_index]
f1_name = string2[third_dot_index + 1 : at_the_index]
l_name = string2[at_the_index + 1: fourth_dot_index]  # Get everything after '@'
finsl_part = string2[fourth_dot_index +1:]
# Printing the extracted names
print(f_name, s_name, t_name, f1_name, l_name,finsl_part)

