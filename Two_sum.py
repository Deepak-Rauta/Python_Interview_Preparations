class Solution:
    def twosum(self, numbers, target):
        # Take two pointers
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < left:
                left += 1
            else:
                right -= 1
numbers = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twosum(numbers, target))


