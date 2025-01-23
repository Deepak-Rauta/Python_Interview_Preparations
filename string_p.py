# reverse a srtring
def is_reverse(s):
    return s[::-1]
original_string = "Deepak"
reversed_string = is_reverse(original_string)
print(f"The original string is: {original_string}")
print(f"The reverse string is: {reversed_string}")

#Q2
# check palindrome

def check_pal(n):
    # first convert the number into string
    str_num = str(n)
    # now check if the string equals to its reverse or not
    return str_num == str_num[::-1]
my_string = "madam"
if check_pal(my_string):
    print(f"The {my_string} is palindrome")
else:
    print(f"The {my_string} is not a palindrome")

# Q3
# count vowels and consonant:--->

str = 'hey how are you'
count = 0
vowels = 'aeiou'
for i in str:
    if i in vowels:
        count = count + 1
print(f"The no. of vowels is {count}")

def count_vowel_consonants(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    cons_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        # check if the cheracter is a consonant (ignoring non alphabetic cheracter)
        elif char.isalpha():
            cons_count +=1
    return vowel_count, cons_count

input_string = 'Hello world!'
vowels, consonants = count_vowel_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")

# Q4
# Given a string find the non-repeating character in it.
# Example 'swiss' the first non-repeating character is 'w'
string = 'swiss'
str1 = ''

for i in string:
    # check if the character appears only once in the string
    if string.count(i) == 1:
        str1 = i
        break
if str1:
    print(f"The first non-repeating character is: {str1}")
else:
    print("There is no non-repeating character")

def first_non(input_string):
    str1 = ''
    for i in input_string:
        if input_string.count(i) == 1:
            str1 = i
            break
    return str1
input_string = 'swiss'
non_repeated = first_non(input_string)
print(f"The first non repeating cheracter is: {non_repeated}")

# Q5
# Anagram check------->
# write a function to check if two given strings are anagram of each others
# they contain the same character in a different order

def are_anagrams(str1, str2):
    # remove spaces and convert it to lower case
    str1 = str1.replace("","").lower() # This method remove all spaces 
    str2 = str2.replace("","").lower()

    # sort the character of both the string 
    return sorted(str1) == sorted(str2)

# example usage

string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
if result:
    print(f"{string1} and {string2} are anagrams")
else:
    print(f"{string1} and {string2} are not anagrams")

# Q6
# string compression----->
# Normal code----->

string = "aaabbcc"
count_a = 0
count_b = 0
count_c = 0
for i in string:
    if i == 'a':
        count_a = count_a + 1
    elif i == 'b':
        count_b = count_b + 1
    elif i == 'c':
        count_c = count_c + 1
print(f"No. of 'a' count is: {count_a}")
print(f"No. of 'b' count is: {count_b}")
print(f"No. of 'c' count is: {count_c}")

# Actual code---->
del str
def compress_string(s):
    compressed = "" # this string will store the final compressed version
    count = 1

    # Loop through the string
    # The loop starts from index 1(the second character) bcz we compare each character to the privious one
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count = count + 1
        else:
            # append the character and its count to the result
            compressed += s[i - 1] + str(count)
            count = 1 # reset the count for the new character

    # append the last character and its count 
    compressed += s[-1] + str(count)
    return compressed

# Example usage:
string = "aaabbcc"
compressed_string = compress_string(string)
print(f"The compressed string is: {compressed_string}")

# First Iteration (i = 1):

# s[1] is 'a', s[0] is 'a'
# Since they are the same, count is incremented to 2.
# Second Iteration (i = 2):

# s[2] is 'a', s[1] is 'a'
# Again, they are the same, so count is incremented to 3.
# Third Iteration (i = 3):

# s[3] is 'b', s[2] is 'a'
# so.... now it goes to the else part

# Q7
# Longest sub string without repeating character------>
def longest_unique_substring(s):
    start = 0 # starting index 
    max_length = 0 # we will keep track of the longest substring without repeating its character
    char_set = set() # set to store the characters in the current window
    # we will take set here bcz set autometically handles the duplicatesmens each characters in the set is unique
    for end in range(len(s)):
        # if the characters is already in the set, remove characters from the start until it's not
        while s[end] in char_set:
            char_set.remove(s[start])
            start+=1
        # Add the current character to the end
        char_set.add(s[end])
        # update the max length if the current window is larger
        max_length = max(max_length, end - start +1)
    return max_length

# Example usages
input_string = "abcabcbb"
length = longest_unique_substring(input_string)
print(f"The length of the longest substring without repeating characters is: {length}")

# Q8
# Remove Duplicates
# write a function to remove duplicate character from a string while mantaining the order of character

def find_duplicate(input_string):
    seen = set() # keep track of the character that have already been encounterd in the string
    result = []

    for char in input_string:
        if char not in seen:
            seen.add(char) # Add the character to the set if it's not a duplicate
            result.append(char) # Append it to the result list
    return ''.join(result)
input_string = "swiss"
output_string = find_duplicate(input_string)
print(f"string after removing duplicates: {output_string}")

# Q9
# Generating all posssible permutations of a string 
# for this we can also use itertools.permutations function to achieve this

import itertools

def generate_permutation(input_string):
    # generate all permutation
    permutations = itertools.permutations(input_string)

    # convert each permutation from tuple to string and store in a list
    permutation_list = [''.join(p) for p in permutations]
    return permutation_list
input_string = "abc"
permutations = generate_permutation(input_string)
print(f"All possible permutations of '{input_string}' are: {permutations}") 

# Q10
# check if two string are rotation of each other
# examples 'abcd' and 'dabc' are rotation each other
# key ideas:
# if string s2 is a rotation of string s1,then s2 must be substring of s1 + s1
# s1 = 'abcd', s2 = 'dabc' s1+s1 = 'abcdabcd' and 'dabc' is a substring of 'abcdabcd'

# if the length of the strings are the same and neither is empty
def is_rotations(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    # concatenate  s1 with itself
    combined = s1 + s1
    # check if s2 is a substring of the combined strng 
    return s2 in combined

s1 = "abcd"
s2 = "dabc"
result = is_rotations(s1, s2)
print(f"Is '{s2}' is a rotation of '{s1}'? {result}")

# Q11
# lengest common prefix------>

def check_logest_prefix(strs):
    if not strs:
        return ""
    
    # set a initial prefix
    prefix = strs[0]
    # now iterate each string
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
input_string = ["flower", "flow", "flight"]
longest_prefix = check_logest_prefix(input_string)
print(f"The logest common prefix starts with: {longest_prefix}")


# Q12
# substring search----->

def find_substring(main_string, sub_string):
    # find out the length of them
    len_main = len(main_string)
    len_sub = len(sub_string)

    # first compare if the length of len_sub is greater or less
    if len_sub > len_main:
        return False

    # iterate using loop
    for i in range(len_main - len_sub + 1):
        match = True
        # take the inner loop---->
        for j in range(len_sub):
            if main_string[i + j] != sub_string[j]:
                match = False
                break
        # if it is matching 
        if match:
            return True
    return False
main_string = "hello world"
sub_string = "world"
result = find_substring(main_string, sub_string)
print(f"Does the substring exist?:{result}")


# Q13
# write a function to count the number of times a given substring appears in a string 
def count_substring(main_string, sub_string):
    count = 0
    sub_len = len(sub_string)

    # loop through the main string
    for i in range(len(main_string) - sub_len + 1):
        # ckeck if the substring matches the current slice of the main string 
        if main_string[i:i + sub_len] == sub_string:
            count += 1
    return count

main_string = "abababab"
sub_string = "ab"
result = count_substring(main_string, sub_string)
print(f"The substring '{sub_string}' appears {result} times in the string")

# check for balanced parenthesis---->
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid (i.e., the parentheses are balanced

# def is_valid_parenthesis(s: str) -> bool: This syntax is known as type hinting or type annotation in python
# (s: str) ----> s to be of type str(string)
# it is telling anyone reading the code, or tools like linters and IDEs that the input s should be a string 
# -> bool: it indicate that return types of the function 
# that the function is expected to return a boolean value (True or False)

def is_valid_parenthesis(s: str) -> bool:
    # Dictonary to match closing brackets with their corresponding opening brackets
    matching_brackets = {')' : '(', '}' : '{', ']' : '['}


    # stack to keep track of opening brackets
    stack = []

    # iterate over the characters in the string
    for char in s:
        # if it is a closing brackets
        if char in matching_brackets:
            # pop the stack if not empty, else assign a dumy value
            top_element = stack.pop() if stack else '#'
            # ckeck of the poped element matches the coresponding opening brackets
            if matching_brackets[char] != top_element:
                return False
        else:
            stack.append(char)
           
    # at the end, the stack should be empty if the paranthesis are balanced
    return not stack
# Example usage
input_string = "{[()()]}"
print(is_valid_parenthesis(input_string))

input_string2 = "{[(])}"
print(is_valid_parenthesis(input_string2))

# Convert a String to an Integer (atoi):
# Write a function to convert a string into an integer, handling edge cases like leading/trailing spaces, negative numbers, and invalid characters.


# ===========================================================================================================
class Solution:
    def find_substring(self, main_string, sub_string):
        main_len = len(main_string)
        sub_len = len(sub_string)

        if sub_len > main_len:
            return False
        for i in range(main_len - sub_len + 1):
            match = True
            for j in range(sub_len):
                if main_string[i + j] != sub_string[j]:
                    match = False
                    break
            if match:
                return True
        return False
main_string = "Hello world"
sub_string = "world"
solution_instance = Solution()
result = solution_instance.find_substring(main_string, sub_string)
print(f"Does the substring exists? {result}")

# Q14
# longest palindromic substring------>
# Example "babad", the output is "bab" or "aba"

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        # odd length palindrome 
        temp = expand_around_center(s,i,i)
        if len(temp) > len(res):
            res = temp
        # Even length palindrome
        temp = expand_around_center(s, i, i+1)
        if len(temp) > len(res):
            res = temp
    return res
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left +1 : right]
input_string = "babad"
print(f"Longest palindrome substring is:", longest_palindrome(input_string))
