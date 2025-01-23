# def reverse_string(s):
#     return s[::-1]

# # Example usage:
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(reversed_string)


# def reverse_string(s):
#     return s[::-1]
# #Example uses
# original_string = 'hello world'
# reversed_string = reverse_string(original_string)
# print(f'{reversed_string}')


# def reverse(s):
#     result = " "
#     for i in s:
#         result = i + result
#         print(result)
#     return result  
# s = "Deepak"
# print(f'The original string is:{s}')
# print('The reversed string is:', reverse(s))



class Solution:
    def reverse_string(self, n):
        return n[::-1]
solution_instance = Solution()
original_string = "Deepak"
reversed_string = solution_instance.reverse_string(original_string) 
print(f'{reversed_string}')   