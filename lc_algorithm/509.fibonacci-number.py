#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.66%)
# Likes:    531
# Dislikes: 187
# Total Accepted:    179.6K
# Total Submissions: 268.2K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
#
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
#
#
# Given N, calculate F(N).
#
#
#
# Example 1:
#
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
# Example 2:
#
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
# Example 3:
#
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
#
# Note:
#
# 0 ≤ N ≤ 30.
#
#

# @lc code=start
class Solution:
    def fib(self, n):
        """ 0, 1, 1, 2, 3, 5 """
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)

    def fib(self, n):
        """Runtime: 32 ms, faster than 60.19% """
        if n == 0:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


print(Solution().fib(4))
# @lc code=end
