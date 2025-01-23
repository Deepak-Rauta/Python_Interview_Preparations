# # for num in range(1,101):
# #     if num>1:
# #         for i in range(2,num):
# #             if num%i==0:
# #              break
# #         else:
# #            print(num, "is prime number")    



# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#         return True
    
# number = 12
# if is_prime(number):
#      print(f"{number} is a prime number")
# else:
#      print(f"{number} is not a prime number")


# # Factorial
# def is_fact(n):
#     if n==0 or n == 1:
#         return 1
#     else:
#         return n*is_fact(n-1)
# number = 5
# print(f"The factorial of the {number} is {is_fact(number)}")


# # String palindrome
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]
# string = 'MADAM'
# if is_palindrome(string):
#     print(f'The character {string} is palindrome')
# else:
#     print(f'The character {string} is not palindrome')


# # number palindrome

# def is_pallindrome(num):
#     original_num = num  ## it store the original number
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10  # extract the last digit
#         reversed_num = reversed_num * 10 + digit
#         num = num//10 # integer division by zero

#     return original_num == reversed_num
# number = int(input("Enter the number:"))
# if is_pallindrome(number):
#     print(f"The {number} is pallindrome")
# else:
#     print(f"The {number} is not pallindrome")


# # Find the largest elements in a list

# def find_largest_element(lst):
#     # check if the list is empty
#     if not lst:
#         return None
#     # initialize the largest element as the first element of the list
#     largest = lst[0]

#     # Loop through the list to find the largest element
#     for element in lst:
#         if element > largest:
#             largest = element
#     return largest
# my_list = [3,5,7,8,9,4,2,6]
# largest_number = find_largest_element(my_list)
# print(f"The largest number in the list is {largest_number}")


# Right angle traingle pattern
n = 5
for i in range(1, n+1):
    print('*' * i)

print('\n')

# Inverted right angle triangle pattern

n = 5
for i in range(n, 0, -1):
    print('*' * i)

# pyramid pattern
n = 5
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

# [' ' * (n-i)] :- This part create leading space for each row
# no. of spaces decreses as i increase bcz n - i becomes smaller
# ['*' * (2 * i - 1)]:- This part print the stars increases as i increases

# For example:
# When i = 1, 2 * i - 1 = 1, so it prints 1 star.
# When i = 2, 2 * i - 1 = 3, so it prints 3 stars.
# When i = 3, 2 * i - 1 = 5, so it prints 5 stars, and so on.

n = 5
for i in range(1, n+1):
    print(' ' * (n - 1) + '*' * (2 * i - 1))