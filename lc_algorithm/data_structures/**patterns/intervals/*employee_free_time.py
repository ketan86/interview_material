"""
For ‘K’ employees, we are given a list of intervals representing the working
hours of each employee. Our goal is to find out if there is a free interval that
is common to all employees. You can assume that each list of employee working
hours is sorted on the start time.

Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]] Output: [3,5]
Explanation: Both the employess are free between [3,5]. Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]] Output: [4,6],
[8,9] Explanation: All employess are free between [4,6] and [8,9]. Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]] Output: [5,7]
Explanation: All employess are free between [5,7].
"""

# simple solution

# put all intervals into one list, sort, merge and find the gap.


def find_employee_free_time(schedule):
    # S(n)
    results = []
    # T(n^2)
    for intervals in schedule:
        for interval in intervals:
            results.append(interval)
    # T(nlogn)
    results.sort()
    # T(n)
    results = _merge(results)
    # S(n)
    free_time = []
    i = 0
    j = 1
    # T(n)
    while j < len(results):
        free_time.append([results[i][1], results[j][0]])
        i += 1
        j += 1

    return free_time


def _merge(intervals):
    results = []
    for interval in intervals:
        if not results:
            results.append(interval)
        else:
            if results[-1][1] >= interval[0]:
                merged = [min(results[-1][0], interval[0]),
                          max(results[-1][0], interval[1])]
                results[-1] = merged
            else:
                results.append(interval)
    return results


#
print(find_employee_free_time([[[1, 3], [5, 6]], [[2, 3], [6, 8]]]))
print(find_employee_free_time([[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]]))
print(find_employee_free_time([[[1, 3]], [[2, 4]], [[3, 5], [7, 9]]]))
