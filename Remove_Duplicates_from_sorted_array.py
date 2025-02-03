class Solution:
    def RemoveElements(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
numbers = [1,1,2]
solution_instance = Solution()
k = solution_instance.RemoveElements(numbers)  # k stores the number of unique elements
# Printing the number of unique elements and the modified list
print(f"Unique count: {k}")  
print(f"Modified array: {numbers[:k]}")  # Print only the first k elements
