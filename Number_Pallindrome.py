class Solution:
    def isPallindrome(self, x):
        # Handling edge cases
        if x < 0:
            return False
        # Converting into the string
        s = str(x)
        return s == s[::-1]

x = 121
obj = Solution()
print(obj.isPallindrome(x))