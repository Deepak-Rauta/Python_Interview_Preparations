# def multi_string(string1, string2):
# # convert the string into integer
#     num1 = int(string1)
#     num2 = int(string2)  
# # perform the multiplication
#     result = num1 * num2
# # convert the result back to the string
#     result_string = str(result)
#     return result_string
# # Example uses
# string1 = input("Enter the first string:")
# string2 = input('Enter the second string:')
# try:
#     result = multi_string(string1, string2)
#     print(f'The product of {string1} and {string2} is {result}')
# except ValueError:
#     print('Invalid input. please enter valid integers as string') 

# class multiplication:
#     @staticmethod
#     def multi_string(string1, string2):
#         num1 = int(string1)
#         num2 = int(string2)

#         result = num1 * num2
#         result_string = str(result) #convert the result back to the string
#         return result_string
# multiplication_instance = multiplication() 
# string1 = input("Enter the first string:")
# string2 = input("Enter the second string:")
# #Example uses
# try:
#      result = multiplication_instance.multi_string(string1, string2)
#      print(f'The product of {string1} and {string2} is {result}')
# except ValueError:
#      print('Invalid input. please enter valid integers as string') 

# def multiplication(string1, string2):
#     #convert the string into integer
#     num1 = int(string1)
#     num2 = int(string2)

#     result = num1 * num2
#     result_string = str(result)
#     return result_string
# #Example usages
# string1 = int(input("Enter the first string:"))
# string2 = int(input("Enter the second string:"))
# try:
#     result = multiplication(string1, string2)
#     print(f'The product of {string1} and {string2} is {result}')
# except ValueError:
#     print('Invalid input, please enter a valid input')    


class Solution:
    @staticmethod
    def multiplication(string1, string2):
        #convert the string into integer
        num1 = int(string1)
        num2 = int(string2)

        result = num1 * num2
        result_str = str(result)
        return result_str
solution_instance = Solution()
string1 = input("Enter the first string:")
string2 = input("Enter the second string:")
try:
    result = solution_instance.multiplication(string1, string2)
    print(f'The product of {string1} and {string2} is {result}')
except ValueError:
    print("Invalid input please enter a valid input")        
