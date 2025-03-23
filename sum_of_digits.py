def SumDigits(n):
    sum_of_digit = 0
    while n > 0:
        sum_of_digit += n % 10 # Get the last digits
        n // 10 # Remove the last digits
    return sum_of_digit
print(SumDigits(123))
