# reverse a string without using built-in functions
def reverse_str(str):
    reversed_str = ''
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

s = 'python'
result = reverse_str(s)
print(result)


# Check pallindrome

# def is_palindrome(num):
#     # Convert the number to a string
#     num_str = str(num)
#     # Check if the string is equal to its reverse
#     return num_str == num_str[::-1]

# # Example usage
# number = input()

# if is_palindrome(number):
#     print(f"{number} is a palindrome")
# else:
#     print(f"{number} is not a palindrome")


# Most frequent character

def frequent_character(s):

    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    # Now find character with highest frequency
    most_frequency = max(frequency, key = frequency.get)
    return most_frequency
s = 'Deepak'
result = frequent_character(s)
print(result)


# capitalize the first and last character of each word in a string
def cap_first_last(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) > 1:
            word = word[0].upper()+word[1:-1]+word[-1].upper()
        else:
            word = word.upper()
        result.append(word)
    return ' '.join(result)
s = 'hello world'
result = cap_first_last(s)
print(result)

# Remove all the worldcup from a string, keeping only the first occurance of each word
def remove_duplicate(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)
s = 'hello world'
result = remove_duplicate(s)
print(result)

# num palindrome
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


# prime number
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




