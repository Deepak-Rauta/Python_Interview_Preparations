# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     result_string = "".join(char for char in input_string if char not in vowels)
#     return result_string

# # Get input from the user
# user_input = input("Enter a string: ")

# # Remove vowels from the input string
# result = remove_vowels(user_input)

# # Display the result
# print("Original String:", user_input)
# print("String without vowels:", result)





def remove_vowel(input_string):
    vowels = 'aeiouAEIOU'
    result_string = "".join(char for char in input_string if char not in vowels)
    return result_string

#get input from the user
user_input = input("Enter the string")

# Remove vowels from the input string
result = remove_vowel
(user_input)

# Display the result
print("Original String:", user_input)
print("String without vowels:", result)

