class Solution:
    def sumOfDigits(self, nums):
        sum_of_digits = 0
        while nums > 0:
            sum_of_digits += nums % 10
            nums //= 10
        return sum_of_digits

numbers = 123
obj = Solution()
print(obj.sumOfDigits(numbers))


