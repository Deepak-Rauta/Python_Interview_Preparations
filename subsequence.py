class Solution:
    def Sequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
s = "abc"
t = "ahbgdc"
obj = Solution()
print(obj.Sequence(s, t))