# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# class Solution:
#     def RoateRight(self, nums, k):
#         k = k % len(nums)
#         nums[:] = nums[-k:] + nums[:-k]
# numbers = [1,2,3,4,5,6,7]
# k = 3
# solution_instance = Solution()
# solution_instance.RoateRight(numbers, k)
# print(numbers)





def rotate(nums, k):
    k = k % len(nums)
    new_nums = nums[-k:] + nums[:-k]  # Creating a new list
    return new_nums  # Returning new list instead of modifying nums

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate(nums, 3)  # Reassigning to a new list
print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]


