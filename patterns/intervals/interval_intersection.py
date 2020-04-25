"""
Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: output list contains the common intervals between the two lists.

Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: output list contains the common intervals between the two lists.
"""

# pylint: skip-file


def interval_intersection(arr1, arr2):
    i = 0
    j = 0
    results = []
    # loop over the two arrays and stop when one of them finishes. no need
    # to continue if either one is done.
    while i < len(arr1) and j < len(arr2):
        # intersection is max of first interval and min of second interval.
        start = max(arr1[i][0], arr2[j][0])
        end = min(arr1[i][1], arr2[j][1])
        # if end is GE to start, we find the intersection, record the results.
        if end >= start:
            results.append([start, end])
        # move the index for which end interval is lesser.
        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1
    return results


print(interval_intersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
