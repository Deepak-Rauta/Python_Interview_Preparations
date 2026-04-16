class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        # Initialize the two-pointers
        left = 0
        right = n - 1
        k = n - 1 # last index of result

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[k] = nums[left] ** 2
                left += 1
            else:
                result[k] = nums[right] ** 2
                right -= 1
            k -= 1
        
        return result
nums = [-4, -1, 0, 3, 10]
obj = Solution()
print(obj.sortedSquares(nums))

