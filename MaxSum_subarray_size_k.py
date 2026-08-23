class Solution:
    def max_sum_subarray(self, nums, k):
        # Initialize the data structure
        left = 0
        window_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # Now, add the element
            window_sum += nums[right]
            # Calculate window size
            if right - left + 1 == k:
                # Calculate maximum sum
                max_sum = max(max_sum, window_sum)
                # Now, remove the leaving element and add the entering element
                window_sum -= nums[left]
                left += 1

        return max_sum
nums = [2, 1, 5, 1, 3, 2]
k = 3
obj = Solution()
print(obj.max_sum_subarray(nums, k))