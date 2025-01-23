# user_input = input("Enter the words:")
# vowels = 'aeiouAEIOU'
# vowels_found = False
# for char in user_input:
#     if char in vowels:
#         vowels_found = True
#         break
# if vowels_found:
#     print("The string contain vowels")
# else:
#     print("The string does not contain any vowels")


# number = int(input("Enter the number:"))

# is_prime = True

# if number < 2:
#     is_prime = False
# else:
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Enter the number:"))
if is_prime(number):
    print(f"The {number} is prime number")
else:
    print(f"The {number} is not a prime number")