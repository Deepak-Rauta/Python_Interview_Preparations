class Solution:
    def Reverse(self, nums, k):
        # Find the length of the number
        n = len(nums)
        # rotate the array based on the first k element
        k = k % n
        # Now reverse the array
        nums.reverse()
        # Now reverse the first k element
        nums[:k] = reversed(nums[:k])
        # Now reverse the rest of the elements
        nums[k:] = reversed(nums[k:])

        return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
obj = Solution()
result = obj.Reverse(nums, k)
print(result)