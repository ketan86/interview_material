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

import heapq


class Solution:
    def dailyTemperatures(self, T):
        """
        Runtime: 596 ms, faster than 14.37%

        This soultion uses min heap, and sorts items hence, performs poor.
        """
        # create result with distance 0
        result = [0] * len(T)
        # min heap to store all the prev temp
        min_heap = []

        # loop over the temp list
        for index, temp in enumerate(T):
            # if min heap is not empty and top element of the min heap temp
            # is less than current temp, curr temp is warmer so pop all
            # items with temp lesser than current.
            while min_heap and min_heap[0][0] < temp:
                _, prev_index = heapq.heappop(min_heap)
                # store index diff using the index stored for each day
                result[prev_index] = index - prev_index

            # push current temp into min heap
            heapq.heappush(min_heap, (temp, index))

        return result

    def dailyTemperatures(self, T):
        """
        Runtime: 508 ms, faster than 67.66%


        NOTE: Because we remove all smaller elements when bigger element is
        found, elements in the stack will always be in decreasing order and
        hence, no need to use heap like data structure to maintain the lower
        elements on top (in stack they will be in decreasing order).

        Stack:
            []
            [(73, 0)]
            [(74, 1)]
            [(75, 2)]
            [(75, 2), (71, 3)]
            [(75, 2), (71, 3), (69, 4)]
            [(75, 2), (72, 5)]
            [(76, 6)]

        Stack to find the next warmer temperature. For ex,

        [73,74,75,71,69,72,76,73]

        73 in the stack
            74 > 73 -> 1 day diff
        73 out of stack
        74 in the stack
            75 < 74 -> 1 day diff
        74 out of stack
        75 in the stack
        71 in the stack
        69 in the stack
            72 > 69 -> 1 day diff
        69 out of stack
            72 > 71 -> 2 days diff
        71 out of stack
        72 in the stack
            76 > 72 -> 1 day diff
        72 out of stack
            76 > 75 -> 4 days diff
        75 out of stack
        76 in the stack  -> 0 day diff
        73 in the stack  -> 0 day diff

        """
        # initialize the result array with 0 days
        result = [0] * len(T)
        # use stack to find the next warmmer day
        # NOTE:: we put current temperature and day index
        # in the stack to find the number of days.
        stack = []
        for index, temperature in enumerate(T):
            while stack and temperature > stack[-1][0]:
                # if current temperature is higher than prev,
                # pop the item, use the index difference to
                # find the days and update the result at stored
                # index.
                _, prev_index = stack.pop()
                result[prev_index] = index - prev_index
            # store the current temperature.
            stack.append((temperature, index))

        # NOTE: we do not have to check if stack is empty of not because, all
        # the remaining temperatures are having 0 days diff and it's
        # by default 0 days in the results set.

        return result


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# @lc code=end
