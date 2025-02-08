# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

class Solution():
    def MaxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
price = [7,1,5,3,6,4]
solution_instance = Solution()
print(solution_instance.MaxProfit(price))
