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
    while i < len(arr1) and j < len(arr2):
        # NOTE: We can not check if start of the secondList is greater
        # than the end time of the firstList because both lists are sorted
        # not sorted together.
        # intersection is max of first interval and min of second interval.
        start = max(arr1[i][0], arr2[j][0])
        end = min(arr1[i][1], arr2[j][1])

        # if end >= start, we find the intersection, record the results.
        # NOTE: for usecase where arr2 [8, 12] and arr1 [13, 23], intersection
        # is not possible because start of the one array is greater than end of
        # another.
        if end >= start:
            results.append([start, end])
        # move the index for which end interval is lesser.
        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1
    return results


print(interval_intersection(
    [[0, 2], [1, 3], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
