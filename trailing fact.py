def count_trailing_zeroes_in_factorial(n):
    # Initialize the count of trailing zeroes
    trailing_zeroes = 0

    # Keep dividing n by powers of 5 and update the count
    power_of_five = 5
    while n // power_of_five > 0:
        trailing_zeroes += n // power_of_five
        power_of_five *= 5

    return trailing_zeroes

# Example usage:
number = int(input("Enter a number to find the trailing zeroes in its factorial: "))
result = count_trailing_zeroes_in_factorial(number)
print(f"The number of trailing zeroes in {number} factorial is: {result}")



