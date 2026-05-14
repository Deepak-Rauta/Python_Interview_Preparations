"""You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise."""

# Method:-01
class Solution:
    def JumpGame(self, nums):
        max_reach = 0
        # Find the last index
        last_index = len(nums) - 1
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= last_index:
                return True
        return False

numbers = [2, 3, 1, 1, 4]
obj = Solution()
print(obj.JumpGame(numbers))


# Jump Game:-
# Each value in the array tells us from this postion how many maximum steps can i jump forward!
# Method:-02
class Solution:
    def canJump(self, nums):
        # Our goal is can i continue moving forward without getting stuck!
        # Initialize the max_reach
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True

nums = [2, 3, 1, 1, 4]
obj = Solution()
print(obj.canJump(nums))