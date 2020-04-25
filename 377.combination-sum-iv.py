#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (43.82%)
# Likes:    1192
# Dislikes: 145
# Total Accepted:    112.9K
# Total Submissions: 253K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
#
# Example:
#
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
#
#

# @lc code=start


class Solution:
    def combinationSum4(self, nums, target):
        n = len(nums)
        memo = {}
        if n < 1:
            return 0

        def dfs(target):
            # if target results are stored in the map, return the results
            if target in memo:
                return memo[target]

            # if target is 0, we found one pair so return 1 so count can be
            # incremented by 1.
            if target == 0:
                return 1

            # if target is not 0, initialize the count to 0 and keeping
            # adding results to count. either 1 if we found the pair or 0.
            count = 0
            # iterate over the all numbers and if i <= target, run dfs to
            # find the pair with target - i.
            for i in nums:
                if i <= target:
                    count += dfs(target - i)

            # store target results to map.
            memo[target] = count

            # return count.
            return count

        return dfs(target)

    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        # target sum 0 has 1 combination which is 0
        dp[0] = 0
        dp[1] = 1
        # iterate over the all targets from 1
        for target in range(1, target + 1):
            # iterate over reach item in the nums array.
            for item in range(len(nums)):
                # if target value is greater than the item, combinations are
                # possible
                if target >= nums[item]:
                    # all combinations of the target which is less than the
                    # target - item are valid combinations for current target
                    # for ex, [1,2,3], 3 so dp[1, 1, 2, ?]
                    # combinations = ((0),(1), (1,1)(2), ?)
                    # for each item in [1,2,3],
                    # target (3) - 1 = 2
                        # so 2 has two combinations and we can add 1 to it to
                        # form all valid combinations for target 3.
                        # (1,1,1)(2,1) --> question where is (1,2)
                    # target (3) - 2 = 1
                        # so 1 has one combination and we can add 2 to it to
                        # form all valid combinations for target 3.
                        # (1,2) --> answer: we found (1,2) :)
                    # target (3) - 3 = 0
                        # so 0 has one combination and we can add 3 to it to
                        # form all valid combinations for target 3.
                        # (3) --> we don't consider 0.
                    dp[target] += dp[target - nums[item]]
        return dp[target]
        

print(Solution().combinationSum4([1, 2, 3], 3))
# @lc code=end
