// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):

        max_number = float('inf')

        profit = []
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                profit_num = prices[i] - prices[j]
                if profit_num < 0:
                    profit.append(profit_num)
        for i in range(0, len(profit)):
            if profit[i] < max_number:
                max_number = profit[i]
        if max_number < 0:
            return max_number * -1
        return 0
