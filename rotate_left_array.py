class Solution:
    def left(self, k, nums):
        k = k % len(nums)
        nums[:] = nums[k:] + nums[:k]
number=[1,2,3,4,5,6]
k=2
obj=Solution()
obj.left(k, number)
print(number)