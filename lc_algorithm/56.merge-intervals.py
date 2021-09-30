#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.36%)
# Likes:    2415
# Dislikes: 187
# Total Accepted:    389.3K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start


class Solution:
    def merge(self, intervals):
        """Runtime: 80 ms, faster than 91.78% """
        # sort intervals so we can merge it without checking if
        # next interval's start time is less or greater than current.
        intervals.sort()
        result = []
        for interval in intervals:
            # since intervals are sorted, check if the last interval
            # end time is >= current internal start time.
            if result and result[-1][1] >= interval[0]:
                # since intervals are sorted by start time, we don't have
                # to update the start time using the min function.
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # if can't be merged, append it to result.
                result.append(interval)
        return result

# @lc code=end
