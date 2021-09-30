"""
759. Employee Free Time Hard

906

66

Add to List

Share We are given a list schedule of employees, which represents the working
time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are
in sorted order.

Return the list of finite intervals representing common, positive-length free
time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects
inside are Intervals, not lists or arrays. For example, schedule[0][0].start =
1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we
wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
Accepted
69,014
Submissions
100,025

"""
# Definition for an Interval.

import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedules):
        intervals = []

        # combine all intervals
        for schedule in schedules:
            for shift in schedule:
                intervals.append(shift)

        # sort intervals by time
        intervals.sort(key=lambda x: x.start)

        free_times = []

        # min_heap to store all the running shifts using the end time.
        min_heap = []

        # to find the prior end time
        prior_end = None

        for interval in intervals:
            # remove all finished intervals
            while min_heap and min_heap[0] <= interval.start:
                prior_end = heapq.heappop(min_heap)

            # if no runing shift and prior end and
            # not same as current interval start for ex, [94,94]
            if not min_heap and prior_end and prior_end != interval.start:
                free_times.append(Interval(prior_end, interval.start))

            # push new shift to min_heap by end time
            heapq.heappush(min_heap, interval.end)

        return free_times
