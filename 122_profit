"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = False
        profit = 0
        for i in range(0,len(prices) - 1):
            if prices[i] < prices[i + 1]:
                buy = True
                profit = profit + prices[i + 1] - prices[i]
            elif prices[i] > prices[i + 1]:
                if buy:
                    buy = False
        return profit

            
