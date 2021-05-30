#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (45.11%)
# Likes:    2358
# Dislikes: 40
# Total Accepted:    264.7K
# Total Submissions: 586.8K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start
# pylint: skip-file

import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """
        Runtime: 84 ms, faster than 20.87%

        Maintain running meeting in the min_heap. Min_heap maintains the meeting
        ending first to last. If current meeting start time is greater than
        min_heap meeting end time, remove element from heap and continue
        removing until we find a meeting that is still active.
        """
        # sort intervals by start time
        intervals.sort()
        # use min_heap to store meeting end time
        min_heap = []
        # store minimum rooms
        min_rooms = 0
        for interval in intervals:
            # if min_heap and current meeting start time is >= last meeting
            # end time, remove the last ended meeting, keep removing until
            # there are no meeting ending before current time.
            while min_heap and interval[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            # insert the new meeting by end time
            heapq.heappush(min_heap, interval[1])
            # min_rooms will be a max of min_rooms and all meeting in the heap
            min_rooms = max(min_rooms, len(min_heap))

        return min_rooms

# @lc code=end
