# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def RoateRight(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
numbers = [1,2,3,4,5,6,7]
k = 3
solution_instance = Solution()
solution_instance.RoateRight(numbers, k)
print(numbers)



