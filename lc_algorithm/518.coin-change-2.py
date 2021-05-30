#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (47.06%)
# Likes:    2298
# Dislikes: 67
# Total Accepted:    149K
# Total Submissions: 294.6K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of
# coin.
#
#
#
#
#
#
# Example 1:
#
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# Example 2:
#
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
#
# Example 3:
#
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
#
#
# Note:
#
# You can assume that
#
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
#
#
#

# @lc code=start
class Solution:

    def change(self, amount, coins):
        """
                                 [1,2,5], 5
                                /     \
                       1 / 5-1=4    2 \ 5-2=3
                    [1,2,5],4        [2,5],3
                      1 /               2 \ 3-2

        """

        # dict to store solutions of the subproblem.
        memo = {}
        # dfs to find all combinations (order does not matter)
        # so (1,2,2) is same as (2,1,2)
        return self.dfs(coins, amount, 0, memo)

    def dfs(self, coins, amount, index, memo):
        # if amount becomes 0, we found the valid denomination
        if amount == 0:
            return 1

        # if the current amount and index in the dict, return the total
        # combinations stored.
        # for ex, [1,2,3], 4
        #          ^  <- 0
        # if we have the answer found for index 0 and amount 4, we don't
        # have to recompute.
        if (amount, index) in memo:
            return memo[(amount, index)]

        # find total combinations
        total_combinations = 0
        # to avoid duplicates (because we need combinations), we shrink coins
        # array index.
        for i in range(index, len(coins)):
            # find the remaining amount after removing the current coin amount
            new_amount = amount - coins[i]
            # if new amount >= 0, then only we can find the combination.
            if new_amount >= 0:
                # dfs to find the combinations on with new amount.

                # NOTE: we sum up all the combinations that we have found
                # traversing index to len(coins) for the current amount.
                total_combinations += self.dfs(coins, new_amount, i, memo)

        # save results in the memo
        memo[(amount, index)] = total_combinations

        # return the combinations.
        return total_combinations

    def change(self, amount, coins):
        """
        For each coin, find out if it can contribute to total ways,

        For ex,
            coin 1 -> can contribute to all amount from 1..5
            coin 2 -> can contribute to only amount 2..5
            coin 5 -> can contribute to 5


            dp ->    [1,0,0,0,0,0]
            coin 1   [1,1,1,1,1,1]
            coin 2   [1,1,2,2,3,3]
            coin 5   [1,1,2,2,3,4]

            dp[-1] -> 4

        [1,2,5], 5
                       0 1 2 3 4 5 
        dp[amount] -> [0,0,0,0,0,0]
        dp[0]         [1,0,0,0,0,0]
        for coin in range(1,2,5):
            for 1..5:
                dp[1] += dp[1-1] = 1
                dp[2] += dp[2-1] = 1
                dp[3] += dp[3-1] = ..
        """
        # total ways for each amount is 0
        dp = [0] * (amount + 1)
        # for amount 0, there is one way which is 0 way
        dp[0] = 1
        # for each coin, find out if amount can be formed
        for coin in coins:
            # from coin to final amount, add ways of dp[amount - coin]
            # to current amount.
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]


print(Solution().change(5, [1, 2, 5]))
# @lc code=end
