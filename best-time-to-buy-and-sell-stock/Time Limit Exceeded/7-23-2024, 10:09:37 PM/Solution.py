// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        max_profit = float('inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[i] - prices[j]
                if profit < max_profit:
                    max_profit = profit
        return max(max_profit * -1, 0)