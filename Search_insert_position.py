# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1


class Solution:
    def Insert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
numbers = [1, 3, 5, 6]
target = 2
solution_instance = Solution()
print(solution_instance.Insert(numbers, target)) 


# Why Return left Instead of -1?
# If the target is found, return mid
# if the target is not found, left will be the position where thet target should be inserted in order.
# left always points to the correct insertion index when the loop exits.
