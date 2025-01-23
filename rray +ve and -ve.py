# def create_alternating_array(length):
#     result = []
    
#     for i in range(1, length+1):
#         if i % 2 == 0:
#             result.append(-i)
#         else:
#             result.append(i)
    
#     return result

# # Example: Create an array of 10 alternating positive and negative numbers
# array_length = 10
# result_array = create_alternating_array(array_length)

# print("Alternating Array:", result_array)


class Solution:
    def alternate_arr(self,length):
        result = []
        for i in range(1, length+1):
            if i % 2 == 0:
                result.append(-i)
            else:
                result.append(i)
        return result         
arr_length = 10
solution_instance = Solution()    
result_arr = solution_instance.alternate_arr(arr_length)
print(f'Alternating array is:{result_arr}')


