num = int(input("Enter the number:"))
if (num == 1):
    print("1 is not prime and not composite")
for i in range(2, num):
    if num%i == 0:
        print("It is not a prime number")
    else:
        print("Number is prime number")        


result = []