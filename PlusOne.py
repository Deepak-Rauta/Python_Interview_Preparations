class Solution:
    def Plusone(self, digits):
        num = int("".join(map(str, digits)))
        num += 1
        return [int(digit) for digit in str(num)]
Digit = [1, 2, 3]
obj = Solution()
print(obj.Plusone(Digit))