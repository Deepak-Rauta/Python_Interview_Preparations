# The main motive of this code is the min. jump require to reach the last index

class Solution:
    def JumpGame(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i+nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n-1:
                    break
        return jumps
numbers = [2,3,1,1,4]
Solution_instance = Solution()
print(Solution_instance.JumpGame(numbers))
