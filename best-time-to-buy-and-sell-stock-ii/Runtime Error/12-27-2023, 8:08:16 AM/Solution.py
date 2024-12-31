// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution(object):
    def maxProfit(self, prices):
        
        for i in range(0, len(prices)):
            max_price = prices[i]
            ind = 0
            for j in range(i+1, len(prices)):
                if max_price < prices[j]:
                    max_price = prices[j]
            print(max_price, prices[i])

            print(max_price - prices[i])

