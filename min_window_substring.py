class Solution:
    def Min_window(self, target, nums):
        left = 0
        min_length = float("inf")
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
        
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float("inf") else 0
target = 7
nums = [2, 3, 1, 2, 4, 3]
solution_instance = Solution()
print(solution_instance.Min_window(target, nums))

        