# jump game
# The goal of this code is to determine whether we can reach the last index of the given array nums, 
# starting from index 0, where each element in nums represents 
# the maximum number of steps we can jump forward from that position.

class Solution:
    def JumpGame(self, nums):
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+jump)
            if max_reach >= len(nums) - 1:
                return True
        return False
numbers = [2,3,1,1,4]
solution_instance = Solution()
print(solution_instance.JumpGame(numbers))
