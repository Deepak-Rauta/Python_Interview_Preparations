class Solution:
    def moveZeros(self, nums):
        j = 0 # pointers to place the next non-zero elemnt
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
numbers = [0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeros(numbers))