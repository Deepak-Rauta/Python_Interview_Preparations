class Solution:
    def HIndex(self, citations):
        # First sorted in descending order
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i+1:
                h = i+1
            else:
                break
        return h
    
citations= [3, 0, 6, 1, 5]
obj = Solution()
print(obj.HIndex(citations))
