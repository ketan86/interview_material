#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (44.82%)
# Likes:    3622
# Dislikes: 119
# Total Accepted:    604.1K
# Total Submissions: 1.3M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#

# @lc code=start


class Solution:
    def climbStairs(self, n):
        """
        Runtime: 52 ms, faster than 5.14%

        There are two possible ways to climb a stair. 1 step or 2 steps.

        or ex,
                        2  (stairs)
                1 step / \ 2 steps
                      1   0(return)
              1 step / \ 2 steps
                    0    x(not possible)
                (return)

        There are two ways you could finish climbing the stairs.
        """
        total_ways = 0
        # map to store the possible ways so it could be reused.
        memo = {}
        if n == 0:
            return total_ways

        return self._find_ways(n, total_ways, memo)

    def _find_ways(self, n, total_ways, memo):
        # if n is in the map, return the total number of ways one could climb
        # stairs from n.
        if n in memo:
            # add all the ways one could climb stairs from n to total ways
            # if we did not have this map, we would have to go all the way
            # to top(0) to find if one could climb all stairs.
            return total_ways + memo[n]

        # if we reach the top(0), increment total ways by 1.
        if n == 0:
            return total_ways + 1

        # if we have one or more stairs, one could climb one stair.
        if n >= 1:
            total_ways = self._find_ways(n - 1, total_ways, memo)

        # if we have two or more stairs, one could climb two stairs.
        if n >= 2:
            total_ways = self._find_ways(n - 2, total_ways, memo)

        # store total ways one could climb n stairs in the map.
        memo[n] = total_ways

        # return the total ways.
        return total_ways

    def climbStairsTabulation(self, n):
        # Runtime: 28 ms, faster than 82.58%

        dp = [0] * (n + 1)
        # number of ways one can climb 0 step is 0.
        dp[0] = 0
        # number of ways one can climb one step is only 1 way
        dp[1] = 1
        # number of ways one can climb 2 steps is 2 ways
        dp[2] = 2

        for i in range(3, n + 1):
            """
            Question: Why dp[i - 1] + dp[i - 2]
            Answer  : if we are at the step 3, we could have come from either
            step 1 (with 2 step) or step 2(with 1 step). we have to make 1 step
            from dp[i-2] and 2 step from dp[i-1] to reach dp[i] step but since
            we are calculating a ways, it is just a sum of total number of
            ways.
            """
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


print(Solution().climbStairs(3))
print(Solution().climbStairsTabulation(3))
# @lc code=end
