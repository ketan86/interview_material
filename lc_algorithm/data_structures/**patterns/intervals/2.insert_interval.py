"""
Problem Statement #

Given a list of non-overlapping intervals sorted by their
start time, insert a given interval at the correct position and merge all
necessary intervals to produce a list that has only mutually exclusive
intervals.

Example 1:

Input:
Intervals=[[1,3], [5,7], [8,12]],
New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7],
we merged them into one [4,7].

Example 2:

Input:
Intervals=[[1,3], [5,7], [8,12]],
New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] &
[8,12], we merged them into [4,12].

Example 3:

Input:
Intervals=[[2,3],[5,7]],
New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation:
After insertion, since [1,4] overlaps with [2,3], we merged them
into one [1,4].
"""


def insert_interval(intervals, newInterval):
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
    3. current and new interval merges
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


print(insert_interval([[2, 3], [5, 7]], [1, 4]))
