#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (31.47%)
# Likes:    3244
# Dislikes: 111
# Total Accepted:    342.1K
# Total Submissions: 1M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different  and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
# pylint: skip-file
from collections import deque
# @lc code=start


class Solution:
    def failedSolutionCoinChange(self, coins, amount):
        """
        This soultion fails due to the reason that it does not cover all the
        usecases. While traversing over the denomination, keep substracting
        from the amount and if amount is not 0 at the end, we do not find the
        change.

        The problem with this approach is that only one scenario is considered.
        what if amount does not become 0 at the end. we have to try the same
        approach from the second last denomination.

        This solution also can't be fixed by making the multiple iteration.
        O(n^2) time complexity due to the reason the combinations could be
        not in the sequence.
        """
        coins.sort()
        i = len(coins) - 1
        num_of_coins = 0
        while i >= 0:
            if amount >= coins[i]:
                amount -= coins[i]
                num_of_coins += 1
            else:
                i -= 1
        if amount != 0:
            return -1
        return num_of_coins

    def failedSolutionCoinChange(self, coins, amount):
        """
        Above solution can be fixed by making the multiple iteration.
        O(n^2) time complexity.
        """
        coins.sort()
        i = j = len(coins) - 1
        num_of_coins = 0
        temp_amount = amount
        while i >= 0:
            print(i)
            while j >= 0:
                if temp_amount >= coins[j]:
                    temp_amount -= coins[j]
                    num_of_coins += 1
                else:
                    print('****')
                    j -= 1
                print(temp_amount)
            print('---')
            if temp_amount != 0:
                i -= 1
                j = i
                temp_amount = amount
            else:
                return num_of_coins
        return -1

    def dfsCoinChange(self, coins, amount):
        """We have to find all combinations and use min of all that combinations
        to find the min coins.

        just checking the first left soultion may not give minimum coins.

            [1,3,4,5] target -> 7

                [5,1,1] which is not min coins combination because [4,3] will
                be even smaller number of coins so we have to find all
                combinations and then find the min among them.

        """

    def bfsCoinChangeTimelimitExceeds(self, coins, amount):
        """
        Breath first search using queue. At any level, amount becomes 0,
        we find the minimum coins (equals to levels).

                                11, [5,2,1]
                        / 11-5  \ 11-2     \11-1
                    6 [5,2,1]  9[5,2,1]     10[5,2,1]
                     /  6-5       \ 9-5        ...
                    1 [5,2,1]     4[5,2,1]
                    / 1-1           \ 4-2
                 0 [5,2,2]         2 [5,2,1]
                 return 1             \ 2-2
                                    0 [5,2,1]
                                        return 1

        Timelimit Exceeds for [1,2,5] amount -> 100

        """
        num_of_coins = 0
        if amount < 1:
            return 0
        queue = deque()
        queue.append((amount, num_of_coins))
        while queue:
            current_amount, current_num_of_coins = queue.popleft()
            for coin in coins:
                if current_amount >= coin:
                    new_amount = current_amount - coin
                    if new_amount == 0:
                        return current_num_of_coins + 1
                    queue.append((new_amount, current_num_of_coins + 1))
        return -1

    def coinChange(self, coins, amount):
        """
        Runtime: 1348 ms, faster than 50.89%

        This problem can be solved by solving the subproblems. for ex,

        coins = [1,2,5], amount 6

        Algorithm:
            - set min_change(amount->0) to 0
            - for 1..amount,
                - for all coins,
                    - if amount >= coin,
                        - min_change(amount) = min(
                                    min_change(amount),
                                    1 + min_change(amount-coin)
                                )
        NOTE: 1 in min function represents the current coin that is included
        in the combination with all combinations excluding current coin.

        min_change = ['inf', 'inf', 'inf', 'inf', 'inf', 'inf']

        min_change(0) = 0

        min_change(1) = 1
            for coin from 1,2,5:
                amount(1) >= coin(1)
                    -> min_change(1) = min(min_change(1), 1 + min_change(1 - 1)
                                     = min('inf', 1 + min_change(0))
                                     = 1
                coin(2) - X

        min_change(2) = 1
            for coin from 1,2,5:
                amount(2) >= coin(1)
                    -> min_change(2) = min(min_change(2), 1 + min_change(2-1))
                                     = min('inf', 1 + min_change(1))
                                     = 2
                amount(2) >= coin(2)
                    -> min_change(2) = min(min_change(2), 1 + min_change(2-2))
                                     = min('inf', 1 + min_change(0))
                                     = 1
                coin(5) - X

        ...

        ...
        """
        # define an array with size = amount + 1 for [0..amount] with inf value.
        # inf means, any change will be less than inf else it will remain inf.
        dp = [float('inf')] * (amount + 1)
        # for amount 0, there wont be any change so min is 0.
        dp[0] = 0
        # go over all the amount starting from 1 to amount + 1.
        for i in range(1, amount + 1):
            # for each amount, go over all the coins.
            for j in range(len(coins)):
                # if amount is greater than the current coin value then
                # and then we can find the change. else skip that coin
                if i >= coins[j]:
                    # find the min of the inf or prev min.
                    # adding 1 to diff of amount and coin gives the min coins
                    # required for the change.
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])

        # return -1 if min coins are still inf else return the min coins
        # for the amount given.
        return -1 if dp[amount] == float('inf') else dp[amount]


print(Solution().coinChange([1, 7, 9], 1000))
# print(Solution().coinChange([2], 3))
# @lc code=end
