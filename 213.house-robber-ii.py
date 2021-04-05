#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.52%)
# Likes:    1453
# Dislikes: 45
# Total Accepted:    157.8K
# Total Submissions: 437.4K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#

# @lc code=start
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        max_money_robbed = 0
        for i in range(n):
            max_money_robbed = max(max_money_robbed, self._dfs(
                nums, start_index=i, current_index=i,
                money_robbed=0, max_money_robbed=0))
        return max_money_robbed

    def _dfs(self, nums, start_index, current_index,
             money_robbed, max_money_robbed):

        if start_index == 0 and current_index == len(nums) - 1:
            return money_robbed

        if current_index >= len(nums):
            return money_robbed

        money_robbed += nums[current_index]

        for i in range(current_index, len(nums)):
            max_money_robbed = max(
                max_money_robbed, self._dfs(
                    nums, start_index, i + 2, money_robbed, max_money_robbed))

        return max_money_robbed

    def rob(self, nums):
        """Runtime: 20 ms, faster than 98.93%"""
        if not nums:
            return 0
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

    def rob_helper(self, nums):
        # dp to store money collected at house index.
        dp = [0] * (len(nums) + 1)

        dp[0] = 0
        dp[1] = nums[0]

        # start from the 3rd house to end
        for i in range(2, len(nums) + 1):
            # if last house or odd number of houses, remove the first house
            # profit.
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[len(nums)]


# print(Solution().rob([2, 7, 3, 6, 9]))
print(Solution().rob([2, 1, 1, 2]))
# # @lc code=end
