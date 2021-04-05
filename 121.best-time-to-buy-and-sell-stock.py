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
    def maxProfit(self, prices):
        """Runtime: 972 ms, faster than 76.50%"""
        max_profit = 0
        if not prices:
            return max_profit

        # find a profit when min_price is less than current price.
        # when current price is less than min_price, we found the
        # next min_price so move current price. This is because,
        # the diff between the new min price and current price
        # will always be more than the previous min price and current price.
        # [7,1,5,3,6,4]
        #  when min price is 7, any value from 1 to 4 would always give lower
        # profit than price when min is 1.
        min_price = prices[0]
        for p in prices:
            if p <= min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)

        return max_profit
