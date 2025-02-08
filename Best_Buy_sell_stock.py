# Best time to Buy and sell stock

class Solution:
    def maxprofit(self, prices):
        min_prices = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_prices:
                min_prices = price
            else:
                max_profit = max(max_profit, price - min_prices)
        return max_profit
Amount = [7,1,5,3,6,4]
solution_instance = Solution()
print(solution_instance.maxprofit(Amount))




