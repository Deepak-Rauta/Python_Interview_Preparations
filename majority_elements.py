class Solution:
    def FindMajority(self, nums):
        count_dict = {}
        n = len(nums)//2 # Majority conditions
        for num in  nums:
            count_dict[num] = count_dict.get(num, 0)+1
            if count_dict[num] > n:
                return num
# Example usages
numbers = [2,2,1,1,1,2,2]
solution_instance = Solution()
result = solution_instance.FindMajority(numbers)
print(result)
