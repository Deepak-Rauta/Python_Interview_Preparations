# def product_puzzle(arr):
#     n = len(arr)
    
#     # Initialize left and right product arrays
#     left_product = [1] * n
#     right_product = [1] * n
    
#     # Calculate left products
#     left_prod = 1
#     for i in range(1, n):
#         left_prod *= arr[i - 1]
#         left_product[i] = left_prod
    
#     # Calculate right products
#     right_prod = 1
#     for i in range(n - 2, -1, -1):
#         right_prod *= arr[i + 1]
#         right_product[i] = right_prod
    
#     # Calculate final product array
#     result = [left_product[i] * right_product[i] for i in range(n)]
    
#     return result

# # Example usage
# arr = [1, 2, 3, 4, 5]
# result_array = product_puzzle(arr)

# # Print the result
# print("Original Array:", arr)
# print("Product Puzzle Solution:", result_array)

class Solution:
    def product_puzzle(self, arr):
       
        n = len(arr)
        left_product = [1] * n
        right_product = [1] * n
        # calculate left product
        left_pro = 1
        for i in range(1, n):
            left_pro *= arr[i-1]
            left_product[i] = left_pro

        #calculate right product
        right_pro = 1
        for i in range(n-2, -1, -1):
            right_pro *= arr[i+1]  
            right_product[i] = right_pro

        result = [left_product[i] * right_product[i] for i in range(n)]  
        return result

arr = [1,2,3,4,5]
solution_instance = Solution()
result_array =  solution_instance.product_puzzle(arr)
print(f'The original array is:{arr}')
print(f'The rsult array is:{result_array}')           

     
    
