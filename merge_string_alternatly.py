class Solution:
    def MergeAlternatly(self, word1, word2):
        merged = ""
        length = max(len(word1), len(word2))
        for i in range(length):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
        return merged
word1 = "abc"
word2 = "pqr"
obj = Solution()
print(obj.MergeAlternatly(word1, word2))