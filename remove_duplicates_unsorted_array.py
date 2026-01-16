class Solution:
    def removeDuplicatesUnsorted(self, nums):
        seen = set()
        i = 0

        for j in range(len(nums)):
            # check if we have seen this number before
            if nums[j] not in seen:
                seen.add(nums[j])
                nums[i] = nums[j]
                i += 1
        return i
numbers = [2, 4, 1]
obj = Solution()
print(obj.removeDuplicatesUnsorted(numbers))