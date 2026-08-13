class Solution:
    def max_sum_subarray(self, nums, k):
        # 01. Initialize the variables
        window_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # 02. Now, add the lement
            window_sum += nums[right]
            if right >= k - 1:
                max_sum = max(max_sum, window_sum)
                # 0. Now remove the element
                window_sum -= nums[right - k + 1]
        return max_sum

numbers = [2, 1, 5, 1, 3, 2]
k = 3
obj = Solution()
print(obj.max_sum_subarray(numbers, k))