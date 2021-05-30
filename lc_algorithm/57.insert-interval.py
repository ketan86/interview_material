#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.92%)
# Likes:    2075
# Dislikes: 210
# Total Accepted:    287.8K
# Total Submissions: 840.5K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
# Example 3:
#
#
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
#
#
# Example 4:
#
#
# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
#
#
# Example 5:
#
#
# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^5
# intervals is sorted by intervals[i][0] in ascending order.
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def insert(self, intervals, newInterval):
        """
        Runtime: 88 ms, faster than 29.57%

        NOTE: Instead of merging with last result's interval, new interval
        is merged with the current interval if necessary.

        **APPORCHES**

        There are 3 possible places where new interval can be inserted.
        1. before the current interval
            - This can be done without any problem
        2. after the current interval
            - This can be done but then we run into merge issues
        3. merge with current inteval
            - This merge could lead to further merge problems

        Instead,

        1. current interval comes before the new interval
            - push current interval to result
        2. new interval comes before the current interval
            - return by appending new interval to results followed by
              remaining intervals
        3. current and merge intervals merge
            - update new interval by merging current with new interval
        4. if we did not return, we have a new interval possibly merged with
           others or never merged (last interval). insert that into the
           result and return.
        """
        result = []
        for index, interval in enumerate(intervals):
            # if current interval comes before the new interval, insert
            # current interval into the result
            if newInterval[0] > interval[1]:
                result.append(interval)
            # if current interval comes after the new interval, return
            # result so far + new_interval + all remaining intervals
            elif interval[0] > newInterval[1]:
                return result + [newInterval] + intervals[index:]
            # if current interval and new interval merges, instead of
            # merging with result, merge current interval with
            # new interval.
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        # if we are done with looping and did not return so far, a new
        # interval should be appended in the result.
        result.append(newInterval)

        return result

    def insertNotOptimized(self, intervals, newInterval):
        # insert the new interval at it's right position
        result = []

        # if intervals are empty, return new intervals
        if not intervals:
            return [newInterval]

        # flag to insert new interval at right position
        appended = False

        # if start time of the new interval is less or equal to first
        # interval, insert new interval at start.
        if newInterval[0] <= intervals[0][0]:
            result.append(newInterval)
            appended = True

        # insert interval in between other intervals.
        for interval in intervals:
            # if current interval start time is less than equal to
            # new interval start time, current interval in added
            # into the list.
            if interval[0] <= newInterval[0]:
                result.append(interval)
            else:
                # if new interval is not added, insert
                if not appended:
                    result.append(newInterval)
                # insert the current interval also
                result.append(interval)
                appended = True

        # if interval is not inserted yet, insert at the end
        if not appended:
            result.append(newInterval)

        # merge if necessary
        new_result = []
        for interval in result:
            if not new_result:
                new_result.append(interval)
            else:
                if new_result[-1][1] >= interval[0]:
                    new_result[-1][1] = max(new_result[-1][1], interval[1])
                else:
                    new_result.append(interval)
        return new_result


# print(Solution().insert(
#     [[1, 3], [6, 9]],
#     [2, 5])
# )
# print(Solution().insert(
#     [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
#     [4, 8])
# )
# @lc code=end
