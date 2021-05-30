#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of
# intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval[a, b](with a < b) denotes the set of real numbers x with a
# <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of[1, 3] and [2, 4] is [2, 3].

# Input: firstList = [[0, 2], [5, 10], [13, 23], [24, 25]], secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
# Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
# Example 2:

# Input: firstList = [[1, 3], [5, 9]], secondList = []
# Output: []
# Example 3:

# Input: firstList = [], secondList = [[4, 8], [10, 12]]
# Output: []
# Example 4:

# Input: firstList = [[1, 7]], secondList = [[3, 10]]
# Output: [[3, 7]]


# Constraints:

# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109
# endj < startj+1

# @lc code=start


class Solution:
    def intervalIntersection(self, firstList, secondList):
        """
        Runtime: 152 ms, faster than 43.18%

              0  1  2  3  4  5  8  10  11   12  13  15  23  24  25  26
            A -------        --------           ----------  ------
                0-2            5-10                12-23    24-25
            B   -------------   -------------       ----------  ------
                     1-5             8-12              15-24     25-26

        """
        i = 0
        j = 0
        results = []
        # loop over the two arrays and stop when one of them finishes. no need
        # to continue if either one is done.
        while i < len(firstList) and j < len(secondList):
            # NOTE: We can not check if start of the secondList is greater
            # than the end time of the firstList because both lists are sorted
            # not sorted together.
            # intersection is max of first interval and min of second interval.
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # if end is GE to start, we find the intersection, record the results.
            # NOTE: for usecase where secondList [8, 12] and firstList [13, 23], intersection
            # is not possible because start of the one array is greater than end of
            # another.
            if end >= start:
                results.append([start, end])
            # move the index for which end interval is lesser.
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return results
# @lc code=end
