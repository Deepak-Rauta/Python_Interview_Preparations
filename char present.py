# def char_is_present(input_string, target_char):
#     return target_char in input_string
# #Example usge
# user_input = input('Enter the string:')
# char_to_check = input('Enter a character to check:')
# if char_is_present(user_input, char_to_check):
#     print(f"The character'{char_to_check}' is present in the string")
# else:
#     print(f"The character'{char_to_check}' is not present in the string")    



def char_is_present(input_string, target_char):
    return target_char in input_string
# Example usages
user_input = input("Enter a string:")
char_to_check = input("Enter a character:")
if char_is_present(user_input, char_to_check):
    print(f'The character {char_to_check} is present in the string')
else:
    print(f'The character {char_to_check} is not present in the string')    


def is_character_present(input_string, search_character):
    for char in input_string:
        if char == search_character:
            return True
    return False

# Example Usage:
input_string = input("Enter a string: ")
search_char = input("Enter a character to check for: ")

if is_character_present(input_string, search_char):
    print(f"The character '{search_char}' is present in the string.")
else:
    print(f"The character '{search_char}' is not present in the string.")


