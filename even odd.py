def find_even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return"Odd"

number = int(input("Enter the number:"))
result = find_even_odd(number)
print(f"The number is:{result}")            