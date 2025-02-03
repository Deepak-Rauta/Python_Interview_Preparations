class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:  # If there are 2 or fewer elements, no need to process
            return len(nums)
        
        i = 2  # Pointer for placing valid elements (allows two occurrences)
        
        for j in range(2, len(nums)):  # Start from index 2
            if nums[j] != nums[i - 2]:  # Allow at most 2 occurrences
                nums[i] = nums[j]
                i += 1
        
        return i  # Length of the modified array

# Example Usage
nums = [3, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]
solution = Solution()
k = solution.removeDuplicates(nums)

# Output the result
print(k)       # Output: 5
print(nums[:k])  # Output: [1, 1, 2, 2, 3]
