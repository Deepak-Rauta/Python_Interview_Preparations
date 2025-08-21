class Solution:
    def TwoSum_Solution(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
Numbers = [10, 2, 11, 7]
target = 9
obj = Solution()
print(obj.TwoSum_Solution(Numbers, target))
