# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.

class Solution:
    def Candy(self, ratings):
        n = len(ratings)
        candies = [1] * n # Ensure that each children get atleast one candy
        # Left to Right pass
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # Right to Left pass
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        return sum(candies)
ratings = [1, 0, 2]
solution_instance = Solution()
print(solution_instance.Candy(ratings))
