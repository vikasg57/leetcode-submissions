// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        brought_for = float('inf')
        profit = 0
        max_profit = 0
        for i in range(len(prices)):
            if brought_for > prices[i]:
                brought_for = prices[i]
            profit = brought_for - prices[i]
            if profit < max_profit:
                max_profit = profit
        return max_profit * -1
