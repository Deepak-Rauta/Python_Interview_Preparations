def increment_array(arr):
    # Using list comprehension to create a new array with incremented elements
    result_array = [element + 1 for element in arr]
    return result_array

# Example usage
input_array = [1, 2, 3, 4, 5]
output_array = increment_array(input_array)

print("Original Array:", input_array)
print("Array after incrementing each element by one:", output_array)

class Solution:
    def AddElement(self, arr):
        
# Using list comprehension to create a new array with incremented elements
        result_array = [element + 1 for element in arr]
        return result_array
# Example usages
my_arr = [1,2,3,4,5,6,7,8,9]
solution_instance = Solution()
output_array = solution_instance.AddElement(my_arr)
print(f'The original array is: {my_arr}') 
print(f'The array after pluse one is: {output_array}')               








def add_one(digits):  # The function add_one and pass a arguments digits
    carry = 1  # initialize to 1 as we are adding 1 to the given number
    result = []  # Empty list at will store the digits of the

    for i in range(len(digits) - 1, -1, -1): # for itereting through the digits in reverse order. three arguments is(start, stop, tsep)
        current_sum = digits[i] + carry  # for each digit sum of digit and carry is calculated
        result.insert(0, current_sum % 10) # The list significant of the current sum is added to the beginiing of the result list
        carry = current_sum // 10  # The carry of next iteration is calculated by dividing the current sum by 10

    if carry:
        result.insert(0, carry) # if there still a carry remaining it is add as the most significant digit in the result list

    return result

# Example usage
N = 3
arr = [1, 2, 4, 5]

result = add_one(arr)

print("Input:", arr)
print("Output:", result)

class Solution:
    def add_one(self, digits):
        carry = 1
        results = []
        for i in range(len(digits) -1, -1, -1):
            current_sum = digits[i] + carry
            results.insert(0, current_sum % 10)
            carry = current_sum // 10 

        if carry:
            results.insert(0, carry)
        return results
N = 3
arr = [1,2,3,4]
solution_instance = Solution()       
results = solution_instance.add_one(arr)
print("Input:", arr)
print("Output:", results)


