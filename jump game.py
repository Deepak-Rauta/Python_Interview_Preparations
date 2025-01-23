# def can_jump(nums):
#     max_reach = 0
#     last_index = len(nums) - 1

#     for i in range(len(nums)):
#         # If the current index is unreachable
#         if i > max_reach:
#             return False

#         # Update the maximum reachable index
#         max_reach = max(max_reach, i + nums[i])

#         # If the last index is reachable
#         if max_reach >= last_index:
#             return True

#     return False

# # Example usage:
# nums1 = [2, 3, 1, 1, 4]  # Can jump to the last index
# nums2 = [3, 2, 1, 0, 4]  # Cannot jump to the last index

# print(can_jump(nums1))  # Output: True
# print(can_jump(nums2))  # Output: False



#Explanation
# N = 6
# A[] = {1, 2, 0, 3, 0, 0} 
# Output:
# 1
# Explanation:
# Jump 1 step from first index to
# second index. Then jump 2 steps to reach 
# 4th index, and now jump 2 steps to reach
# the end.



class Solution:
    def jump_game(self, nums):
        max_reach = 0
        last_index = len(nums) - 1  # Fix: Calculate last_index correctly

        for i in range(len(nums)):  # Fix: Correct the range
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= last_index:
                return True

        return False  # Fix: Correct the indentation

# Example usage:
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

solution_instance = Solution()
result1 = solution_instance.jump_game(nums1)
result2 = solution_instance.jump_game(nums2)

print(nums1, result1)
print(nums2, result2)
