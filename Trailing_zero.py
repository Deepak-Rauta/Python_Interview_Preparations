class Solution:
    def TrailiningZeros(self, n):
        count = 0
        while n >= 5:
            n //=5
            count += n
        return count
number = 5
obj = Solution()
print(obj.TrailiningZeros(number))