class Solution:
    def RemoveElements(self, nums, val):
        i = 0 #→ This pointer keeps track of where the next valid element should go.

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
nums = [3, 2, 2, 3]
val = 3
solution_instance = Solution()
result = solution_instance.RemoveElements(nums, val)
print(result, nums[:result])


# Step-by-Step Execution
# j (Index)	nums[j]	nums[j] != val?	Action Taken	nums After Change	i After Change
# 0	3	❌ (3 == 3)	Skip	[3, 2, 2, 3]	0
# 1	2	✅ (2 != 3)	nums[i] = nums[j] → nums[0] = 2	[2, 2, 2, 3]	1
# 2	2	✅ (2 != 3)	nums[i] = nums[j] → nums[1] = 2	[2, 2, 2, 3]	2
# 3	3	❌ (3 == 3)	Skip	[2, 2, 2, 3]	2
