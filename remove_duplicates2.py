class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:  # If there are 2 or fewer elements, no need to process
            return len(nums)
        
        i = 2  # Pointer for placing valid elements (allows two occurrences)
        
        for j in range(2, len(nums)):  # Start from index 2 bcz the first two elements are always allowed, no matter what.
            # Think of the rule again:- Each number can appers at most 2 times
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

# ✅ Why do we write i = 2?
# Because the rule is:
# ➤ Each number can appear at most TWICE.
# So:
# The first 2 elements are always allowed.
# Only from the 3rd element onward we need to check if duplicates should be removed.

print("---------------------------------------------------------------")

"""🚀 General Problem

👉 Allow each number to appear at most K times
👉 Instead of checking 2 positions back, we check k positions back"""

class Solution:
    def removeDuplicates(self, nums, k):
        if len(nums) <= k:
            return len(nums)
        
        i = k # First k elements are always valid

        for j in range(k, len(nums)):
            if nums[j] != nums[i - k]:
                nums[i] = nums[j]
                i += 1
        
        return i

nums = [1, 1, 1, 1, 2, 2, 2, 3]
k = 2
obj = Solution()
result = obj.removeDuplicates(nums, k)

print(result)
print(nums[:result])
