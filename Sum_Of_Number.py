# Sum of first N number
N = int(input("Enter the number:"))
total = 0
for i in range(1, N+1):
    total += i
print(f"The sum of {N} number is: {total}")

###############################################################

# Sum of Even Numbers up to N
N = int(input("Enter a number:"))
total = 0
for i in range(1, N+1):
    if i % 2 == 0:
        total += i
print(f"The sum of Even Number {N} is: {total}")

###############################################################
# Sum of Odd Numbers up to N
N = int(input("Enter a number:"))
total = 0
for i in range(1, N+1):
    if i % 2 != 0:
        total += i
print(f"The sum of Odd Number {N} is: {total}")

################################################################
# Sum of Squares up to N
N = int(input("Enter the number:"))
total = 0
for i in range(1, N+1):
    total += i * i
print(f"The Sum of Squares upto {N} is: {total}")

################################################################
# Sum of Cubes up to N
N = int(input("Enter the number:"))
total = 0
for i in range(1, N+1):
    total += i * i * i
print(f"The Sum of Cubes uo to {N} is: {total}")

# 🟡 Level 2: With Conditions
# Sum of Multiples of 3 or 5 up to N
N = int(input("Enter the number:"))
total = 0
for i in range(1, N+1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(f"The Sum of Multiplies of 3 or 5 up to {N} is: {total}")

# Advance practice
N = int(input("Enter the number: "))
total = 0
print("Numbers:", end=" ")
for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
        total += i

print()
print(f"The Sum of Multiples of 3 or 5 up to {N} is: {total}")

# Sum of Digits of N
num = int(input("Enter a number:"))
total = 0
while num > 0:
    digit = num % 10 # Get the last digit
    total += digit # Add it to sum
    num = num // 10 # Remove the last digit
print(f"The Sum of Digits:{total}")


# Using class and function
class Solution:
    def SumDigits(self, num):
        total = 0
        while num > 0:
            digit = num % 10 # get the last digit
            total += digit # Adding it to sum
            num = num // 10 # Remove the last digit
        return total
number = 1234
obj = Solution()
print(obj.SumDigits(number))


# 🔴 Level 3: Tricky
# Alternating Sum
# An alternating sum is just a sum where the sign (+ / -) keeps flipping with each term
# 👉 So when we say “alternating sum up to N”, we usually mean:
# 1−2+3−4+⋯±N

N = int(input("Enter a Number:"))
total = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        total -= i # even
    else:
        total += i

print(f"Alternating sum up to {N} is: {total}")

# Using class and object
class Solution:
    def AltNumber(self, num):
        total = 0
        for i in range(1, num + 1):
            if i % 2 == 0: 
                total -= i # Even 
            else:
                total += i # Odd
        return total
Number = 5
obj = Solution()
result = obj.AltNumber(Number)
print(f"The Alternating Sum of {Number} is: {result}")

