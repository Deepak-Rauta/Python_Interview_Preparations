class Solution:
    def ReverseLast(self, s):
        words = s.strip().split()
        return len(words[-1])
string = "Hello World"
obj = Solution()
print(obj.ReverseLast(string))

