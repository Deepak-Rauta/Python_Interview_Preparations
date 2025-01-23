# def is_rotated_by_two_places(string1, string2):
#     # Check if the lengths of the strings are the same
#     if len(string1) != len(string2):
#         return False

#     # Concatenate the first string with itself
#     concatenated_string = string1 + string1

#     # Check if the second string is a substring at the specified positions
#     rotated_string1 = concatenated_string[2:len(string1) + 2]
#     if string2 in rotated_string1:
#         return True
#     else:
#         return False

# # Example usage:
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# if is_rotated_by_two_places(string1, string2):
#     print(f"{string1} is rotated by two places to become {string2}.")
# else:
#     print(f"{string1} is not rotated by two places to become {string2}.")

def cal_roated_string(string1, string2):
    if len(string1)!= len(string2):
        return False
    
    concateneted_string = string1 + string1
    # check if the second string is a sub string at the specified position
    roated_string1 = concateneted_string[2:len(string1) + 2]
    if string2 in roated_string1:
        return True
    else:
        return False
# Example usages
string1 = input("Enter the first string:")
string2 = input("Enter the second string:")
if cal_roated_string(string1, string2):
    print(f'{string1} is roated by two place to became {string2}')
else:
    print(f'{string1} is not rotated by two places to become {string2}')            







