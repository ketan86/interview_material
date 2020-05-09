#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (62.44%)
# Likes:    2419
# Dislikes: 71
# Total Accepted:    140.2K
# Total Submissions: 224.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
#
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
#
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#
#

# @lc code=start
# pylint: skip-file


class Solution:
    def dailyTemperatures(self, T):
        # initialize the result array with 0 days
        result = [0] * len(T)
        # use stack to find the next warmmer day
        # NOTE:: we put current temperature and day index
        # in the stack to find the number of days.
        stack = []
        for index, temp in enumerate(T):
            if not stack:
                stack.append((temp, index))
            else:
                while stack:
                    # if current temprature is higher than prev,
                    # pop the item, use the index difference to
                    # find the days and update the result at stored
                    # index.
                    if temp > stack[-1][0]:
                        _, prev_index = stack.pop()
                        result[prev_index] = index - prev_index
                    else:
                        # if temp is not greater, break
                        break
                # store the current temperature.
                stack.append((temp, index))
        return result


# print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# @lc code=end
