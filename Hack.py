# def leap_year(year):
#     if year % 400 == 0:
#         print("It is a leap year!")
#     elif year % 100 == 0:
#         print("Not a leap year")    
#     elif year % 4 == 0:
#         print("It is a leap year")  
#     else:
#         print("Not a leap year")  
        
# leap_year(2002)


# import random
# def leap_year(year):
#     if year % 400 == 0:
#         print("It is a leap year!")
#     elif year % 100 == 0:
#         print("Not a leap year")    
#     elif year % 4 == 0:
#         print("It is a leap year")  
#     else:
#         print("Not a leap year")  
        
# leap_year(random.randint(2000, 2024))

# # using logical opeartor:-->
# def is_leap_year(year):
#     return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# # Example usage
# year = 2021
# if is_leap_year(year):
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year.")

# using ternary operator-->
def is_leap_year(year):
    return "It is a leap year!" if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else "Not a leap year"

# Example usage
print(is_leap_year(2021))


