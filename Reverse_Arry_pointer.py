# Two pointer Techniques
class Solution:
    def ReverseArray(self, nums):
        # Takes Two pointer
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
nums = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.ReverseArray(nums))

