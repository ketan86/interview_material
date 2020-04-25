"""
Problem Statement # Given a list of intervals, merge all the overlapping
intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap,
we merged them into one [1,5]. svg

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap,
we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.

"""
# pylint: skip-file


def merge_intervals(arr):
    # sort the array so only adjacent intervals need merging.
    arr.sort()
    results = []
    for interval in arr:
        # add first interval in results.
        if not results:
            results.append(interval)
        # if not the first one, check if intervals overlap using first inext.
        # if yes, pop the most recent interval from the results array
        # and merge with current one. push merged interval to results array.
        else:
            if results[-1][1] > interval[0]:
                last_interval = results.pop()
                results.append(_merge_intervals(last_interval, interval))
            else:
                # if current interval is not overlapping, put that in results
                # array
                results.append(interval)
    return results


def _merge_intervals(i, j):
    return [min(i[0], j[0]), max(i[1], j[1])]


print(merge_intervals([[1, 4], [2, 5], [7, 9]]))
