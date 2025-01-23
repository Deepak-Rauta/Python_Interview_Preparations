# def is_palindrome(s):
#     return s == s[::-1]

# # Example usage:
# test_string = "level"
# if is_palindrome(test_string):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# # s = str(input("Enter the word"))
# # def is_pallindrome(self):
# #     return self == self[::-1]
# # if is_pallindrome(s):
# #     print("The word is pallindrome")
# # else:
# #     print('The word is not a pallindrome')    




class Solution:
    def is_pallindrome(self, s):
        return s == s[::-1]

# Example usases:

solution_instance = Solution()
test_string = "level"
if solution_instance.is_pallindrome(test_string):
    print("pallindrome")
else:
    print("not a palindrome")    
