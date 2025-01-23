# from fractions import Fraction

# def fraction_to_decimal(numerator, denominator):
#     result = Fraction(numerator, denominator)
#     decimal_representation = float(result)
    
#     # Check if the decimal representation has a repeating part
#     decimal_str = str(decimal_representation)
#     if '.' in decimal_str:
#         non_repeating_part, repeating_part = decimal_str.split('.')
#         if '(' in repeating_part:
#             repeating_part = repeating_part[repeating_part.index('(') + 1:repeating_part.index(')')]
#         decimal_str = f"{non_repeating_part}.{repeating_part}"
    
#     return decimal_representation, decimal_str

# # Example usage
# numerator = 1
# denominator = 3

# result, decimal_str = fraction_to_decimal(numerator, denominator)
# print(f"The decimal representation of {numerator}/{denominator} is: {result}")
# print(f"Decimal representation without parentheses: {decimal_str}")


from math import gcd

def fraction_to_decimal(numerator, denominator):
    # Handle the case of zero numerator
    if numerator == 0:
        return "0"

    # Handle the sign
    sign = "-" if numerator * denominator < 0 else ""
    numerator, denominator = abs(numerator), abs(denominator)

    # Calculate the integer part and the remainder
    integer_part, remainder = divmod(numerator, denominator)

    # Initialize the result with the integer part
    result = f"{sign}{integer_part}"

    # If there's a remainder, start calculating the decimal part
    if remainder > 0:
        result += "."

        # Use a dictionary to store the position of each remainder
        remainder_positions = {}
        recurring_part = ""
        position = 0

        while remainder > 0:
            if remainder in remainder_positions:
                # Repeating part detected, insert parentheses
                recurring_part = result[remainder_positions[remainder]:]
                result = result[:remainder_positions[remainder]] + f"({recurring_part})"
                break

            remainder_positions[remainder] = position
            position += 1

            remainder *= 10
            digit = remainder // denominator
            result += str(digit)
            remainder %= denominator

    return result

# Example usage:
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

result = fraction_to_decimal(numerator, denominator)
print(f"The decimal representation is: {result}")


# from fractions import Fraction

# def cal_fraction(numeretor, denominetor):
#     result = Fraction(numeretor, denominetor)
#     decimal_present = float(result)
#     return result, decimal_present

# #Example usages:
# numeretor = int(input("Enter the numeretor:"))
# denominetor = int(input("Enter the denominetor:"))
# result, decimal_present= cal_fraction(numeretor, denominetor)   
# print(f'The fraction representation of {numeretor} / {denominetor} is; {result}')  
# print(f'The decimal represent is: {decimal_present}')  



from fractions import Fraction
class Solution:
    def cal_fraction(self, numeretor, denominetor):
        result = Fraction(numeretor, denominetor)
        decimal_present = float(result)
        return result, decimal_present
numeretor = int(input("Enter the numeretor:"))
denominetor = int(input("Enter the denominetor:")) 
solution_instance = Solution()
result, decimal_present = solution_instance.cal_fraction(numeretor, denominator)   
print(f'The fraction representation of {numeretor} / {denominetor} is: {result}')  
print(f'The decimal represent is: {decimal_present}')


