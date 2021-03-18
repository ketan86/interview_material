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


def insert_interval(intervals, new_interval):
    results = []
    inserted = False
    # merge intervals.
    for interval in intervals:

        # insert new interval at appropriate position only once.
        if not inserted:
            if new_interval[0] < interval[0]:
                results.append(new_interval)
                inserted = True

        if not results:
            results.append(interval)
        else:
            if results[-1][1] > interval[0]:
                _merge_with(interval, results[-1])
            else:
                results.append(interval)

    return results


def _merge(i, j):
    return [min([i[0], j[0]]), max(i[1], j[1])]


def _merge_with(i, j):
    min_ = min([i[0], j[0]])
    max_ = max(i[1], j[1])
    j[0] = min_
    j[1] = max_


print(insert_interval([[2, 3], [5, 7]], [1, 4]))
