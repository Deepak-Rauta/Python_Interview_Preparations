# def count_vowels_consonants(s):
#     vowels = "AEIOUaeiou"
#     vowel_count = sum(1 for char in s if char in vowels) #use a generetor expression with in the sum function count the number of vowels in the input string
#     consonant_count = len(s) - vowel_count
#     return vowel_count, consonant_count

# # Example usage:
# input_string = "Python is fun"
# v_count, c_count = count_vowels_consonants(input_string)
# print("Vowels:", v_count)
# print("Consonants:", c_count)

      
def pallindrome(str):
    s = str.lower()
    return s == s[::-1]
string = input("Enter the string:")
if pallindrome(string):
    print(f"The {string} is pallindorm")
else:
    print(f"The string is not a pallindome")

