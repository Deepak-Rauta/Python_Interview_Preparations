class Solution:
    def TwoSum(self, num, target):
        left, right = 0, len(num)-1
        while left < right:
            total = num[left] + num[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1
Numbers = [2, 7, 11, 15]
Target = 9
obj = Solution()
print(obj.TwoSum(Numbers, Target))
