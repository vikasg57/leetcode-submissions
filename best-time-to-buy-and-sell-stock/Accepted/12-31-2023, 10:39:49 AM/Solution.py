// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        max_number = float('inf')
        # profit = []
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[i] < prices[j]: 
        #             profit_num = prices[i] - prices[j]
        #             if profit_num < 0:
        #                 profit.append(profit_num)
        # for i in range(0, len(profit)):
        #     if profit[i] < max_number:
        #         max_number = profit[i]
        # if max_number < 0:
        #     return max_number * -1
        # return 0

        min_price = float('inf')
        max_profit = float('-inf')
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
            