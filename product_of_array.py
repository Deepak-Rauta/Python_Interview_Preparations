# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# A prefix product is the cumulative product of elements before the current index in an array.
# It means we compute the product of all elements before the current element.

# A suffix product is the cumulative product of elements after the current index in an array.
# It means we compute the product of all elements after the current element.

class Solution:
    def Array_Product(self, num):
        n = len(num)
        # Create a result array initialized with 1
        result = [1] * n
        # 01: Compute the prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= num[i]
        # 02: Compute the suffix product
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= num[i]
        return result
nums = [1, 2, 3, 4]
solution_instance = Solution()
print(solution_instance.Array_Product(nums))    