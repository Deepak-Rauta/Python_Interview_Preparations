class Solution:
    def My_Array(self, nums, target):
        def Find_first(nums, target):
            left, right = 0, len(nums)-1
            first = -1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    first = mid
            return first
        def Find_last(nums, target):
            left, right = 0, len(nums)-1
            last = -1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    last = mid
            return last
        return [Find_first(nums, target), Find_last(nums, target)]
numbers = [5,7,7,8,8,10]
target = 8
solution_instance = Solution()
print(solution_instance.My_Array(numbers, target))