# def find_natural_number(n):
#     count = 0
#     num = 1

#     while True:
#         # Check if the number contains the digit 9
#         if '9' not in str(num):  #we convert the num into string because we find the 9 as a character
#             count += 1

#         # If count reaches N, return the result
#         if count == n:
#             return num

#         # Move to the next natural number
#         num += 1

# # Example usage:
# N = int(input("Enter the value of N: "))
# result = find_natural_number(N)
# print(f"The {N}th natural number after removing numbers containing digit 9 is: {result}")

# class Solution:
#     @staticmethod
#     def cal_natural_number(n):
#         count = 0
#         num = 1
#         while True:
#           if '8' not in str(num): 
#              count+=1
#           if count == n:
#              return num
#           num+=1
# #Example usages:
# Solution_instance = Solution()
# N = int(input("Enter the number:"))
# result = Solution_instance.cal_natural_number(N)
# print(f"The {N}th natural number after removing numbers containing digit 8 is: {result}")  

class Solution:
    @staticmethod
    def cal_natural_number(n):
        count = 0
        num = 1
        while True:
            if '5' not in str(num):
                count==1
            # if count reaches N then return result    
            if count == n:
                return num    
#Example usages
solution_instance = Solution()
N = int(input("Enter the number:"))
result = solution_instance.cal_natural_number(N)
print(f'The {N}th natural number after removing number containig digit 8 is: {result}')                                                