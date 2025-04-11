import math
class Solution:
    def FindGcd(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]
str1 = "ABCABC"
str2 = "ABC"
obj = Solution()
print(obj.FindGcd(str1, str2))