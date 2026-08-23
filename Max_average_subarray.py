class Solution:
    def max_avg_subarray(self, nums, k):
        # Calculate first candidate window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            # First add the element
            window_sum += nums[right]
            # Then remove the element
            window_sum -= nums[right - k]
            # Calculate maximum sum
            max_sum= max(max_sum, window_sum)

        # Now return the average
        return max_sum / k
nums = [1,12,-5,-6,50,3]
k = 4
obj = Solution()
print(obj.max_avg_subarray(nums, k))