# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:

#         max = 0
#         for i in range(len(prices)):

#             for j in range(i+1,len(prices)):
#                 val = prices[j] - prices[i]
#                 if val >= 0:
#                     if val > max:
#                         max = val
        
#         return max

"""
Gives the TLE Error

"""
                    


class Solution:
    def maxProfit(self, prices: list[int]) -> float:
        n = len(prices)
        if n < 2:
            return 0

        max_profit, minstock = float('-inf'), prices[0]
        for x in prices:
            max_profit = max(max_profit,x-minstock)
            minstock = min(minstock,x)
        
        return max_profit

"""
T.C -> O(n)
S.C -> O(1)

Approach: 
Keeping a track of the minimum stock price and,
The maximum profit, we should be to solve the problem in a single pass.

"""