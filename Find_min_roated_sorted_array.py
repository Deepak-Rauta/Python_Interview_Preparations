class Solution:
    def Min_Array(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
numbers = [4, 5, 6, 7, 0, 1, 2]
solution_instance = Solution()
print(solution_instance.Min_Array(numbers))