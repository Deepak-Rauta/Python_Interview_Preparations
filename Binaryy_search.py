class Solution:
    def BinarySearch(self, arr, target):
        left, right = 0, len(arr)-1

        while left <= right:
            mid = left + (right - left) // 2 # find middle indfex
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 23
obj = Solution()
print(obj.BinarySearch(array, target))