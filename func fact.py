def find_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*find_factorial(n-1)
number = int(input("Enter the number:"))
result = find_factorial(number)
print(f"The factorial of {number} is:{result}")    