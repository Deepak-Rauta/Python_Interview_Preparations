class Solution:
    def FindPeak(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
numbers = [1, 2, 3, 1]
solution_instance = Solution()
print(solution_instance.FindPeak(numbers))