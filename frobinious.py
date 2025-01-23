# def frobenius_number(coins): # We define a function 
#     # coins refer to the set of positive integer
#     coins.sort() # is used to sort the list of coin denomination in ascending order
#     current = 1 # Initialize a veriable current 1

#     for coin in coins:
#         if coin > current:
#             break
#         current += coin

#     return current

# # Example usage:
# coins_list = [1, 2, 5]
# result = frobenius_number(coins_list)

# print(f"The smallest positive integer that cannot be represented as the sum is: {result}")



class Solution:
    
    def cal_frobinious(self, coins):
        
        coins.sort()
        current = 1
        for coin in coins:
            if coin > current:
                break
            current += coin
        return current    
coin_list = [1,2,5]
solution_instance = Solution()
result = solution_instance.cal_frobinious(coin_list)
print(f"The smallest positive integer that cannot be represented as the sum is: {result}")

           


