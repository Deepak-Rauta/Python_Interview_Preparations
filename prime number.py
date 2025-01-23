# num = int(input("Enter the number:"))
# if num == 1:
#     print("1 is neither prime nor composite")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("The number is not a prime number")
            
#         else:
#             print("The number is prime number")



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def is_classify(number):
    if is_prime(number):
        print(f'{number} is prime number')
    else:
        print(f'{number} is a composite number')

#Example usages:
user_input = int(input("Enter the number:")) 
is_classify(user_input)                     


