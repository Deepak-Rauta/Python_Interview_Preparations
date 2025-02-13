class Solution:
    def TwoSum(self, arr, target):
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
array = [1,2,3,4,6,8,9]
target = 10
obj = Solution()
result = obj.TwoSum(array, target)
print(result)