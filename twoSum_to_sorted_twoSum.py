class Solution:
    def two_sum_sorted(self, nums, target):
        arr = [(num, i) for i, num in enumerate(nums) ]
        # Sort the array
        arr.sort()
        # Initialize the pointers
        left = 0
        right = len(arr)-1
        while left < right:
            total = arr[left][0] + arr[right][0]
            if total == target:
                return [arr[left][1], arr[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1
numbers = [ 3, 2, 4]
target= 6
obj = Solution()
print(obj.two_sum_sorted(numbers, target))
