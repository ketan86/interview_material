#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.23%)
# Likes:    4081
# Dislikes: 124
# Total Accepted:    467.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#

# @lc code=start

import math


class Solution:
    def rob(self, nums):
        n = len(nums)

        if n < 1:
            return 0

        # find the maximum of all the paths starting from each index.
        # for ex. [1,2,3,1]
        # starting of 0 money, robber can rob 1,2,3 or 4th house.
        # find the max of all the money robbed among all options.
        max_money = 0
        for i in range(n):
            # if robber robs 1'st house, he could rob either 3rd or 4th house
            # if robber robs 2'nd house, he could rob 4th house
            # if robber robs 3'rd or 4th house, he can't rob any other house
            max_money = max(max_money, self._dfs(nums, i, 0, 0, memo={}))

        return max_money

    def _dfs(self, nums, index, money_robbed, max_money_robbed, memo):

        if index in memo:
            return memo[index] + money_robbed

        # if index is equal or greater than lengh, we are done and return the
        # current money.
        if index >= len(nums):
            return money_robbed

        # increment the current money with current house value.
        money_robbed += nums[index]

        # start from the current index and go to the last index. for each
        # index find the max of all the paths.
        for i in range(index, len(nums)):
            max_money_robbed = max(
                max_money_robbed, self._dfs(
                    nums, i + 2, money_robbed, max_money_robbed, memo))

        memo[index] = max_money_robbed - money_robbed

        # return the max of all the path.
        return max_money_robbed

    def rob(self, nums):
        # initialize array to hold the max money collected at given house.
        dp = [0] * (len(nums) + 1)
        # at house 0, there is 0 money collected
        dp[0] = 0
        # at house 1, its first value of the house
        dp[1] = nums[0]
        # from house 2 to n+1 (since we have 0th house)
        for i in range(2, len(nums) + 1):
            # at i'th house, the maximum money robbed is equal to
            # max of (third last house + current house) or (second last house).
            # in other words: at any house, robber would have come with
            # the all money collected from a house 1 house away + money from
            # the current house. if this is less than the money collected
            # then the previous house, we take that value. for second house
            # we take max(2 (0+2), 1).
            # for ex, [1,2,3,4]
            # dp[0,1,2,4,6]
            # [
            #   0,
            #   1,
            #   max(dp[0]=0 + 2, d[1]=1)=2,
            #   max(dp[1]=1+3, dp[2]=1)=4,
            #   max(dp[2]=2+4, dp[3]=3)=6
            # ]

            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums)]


print(Solution().rob([4, 1, 2, 7, 5, 3, 1]))
print(Solution().rob([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]))
print(Solution().rob([1, 2, 3, 4]))
# @lc code=end
