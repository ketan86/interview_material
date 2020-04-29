#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (47.97%)
# Likes:    2975
# Dislikes: 137
# Total Accepted:    562.5K
# Total Submissions: 1.2M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
#

# @lc code=start
# pylint: skip-file

# O(n^2)  solution


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # go through the array and sort i + 1 to n elements
        # and find profit. nth - ith.
        max_profit = 0
        for i in range(len(prices) - 1):
            sell_prices = sorted(prices[i + 1:])
            # max profit = nth (sorted) - ith
            max_profit = max(max_profit, sell_prices[-1] - prices[i])
        return max_profit

# O(n)  solution


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices:
            return max_profit

        # move lowest_prev only when new lowest is found. otherwise
        # keep calculating the max profit against the prev lowest


        # the lowest left and highest right will give the max profit.
        # only move left when you find the lower left otherwise keep
	    # calculating max against last lowest.

        prev_lowest = prices[0]
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - prev_lowest)
            if prices[i] < prev_lowest:
                prev_lowest = prices[i]
        return max_profit
