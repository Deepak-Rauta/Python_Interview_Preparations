class Solution:
    def RoatedSortedArray(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            # Sorted the left half
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # sorted the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1
numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0
obj = Solution()
print(obj.RoatedSortedArray(numbers, target))