from collections import Counter
class Solution:
    def FisrtNonRepeat(self, s):
        char_count = Counter(s)
        for char in s:
            if char_count[char] == 1:
                return char
        return None
character = "swiss"
obj = Solution()
print(obj.FisrtNonRepeat(character))
