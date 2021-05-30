"""
Problem Statement #
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
 
"""
# pylint: skip-file


def can_attend_all_appointments(arr):
    """Find overlap to decide if all appointments can be attended or not"""
    # sort array by start time, sort by end time if start times are same
    arr.sort()
    # two pointers to compare meeting times
    i = 0
    j = i + 1

    # till j reaches end
    while j < len(arr):
        # find start and end time of the merged meeting
        start = max(arr[i][0], arr[j][0])
        end = min(arr[i][1], arr[j][1])
        # if both meetings are overlapping, end time will be greater than start,
        # return False
        if end > start:
            return False
        # move pointer by 1 for i and j
        i += 1
        j += 1
    return True


def can_attend_all_appointments(arr):
    """Find overlap to decide if all appointments can be attended or not"""
    # sort array by start time, sort by end time if start times are same
    arr.sort()
    # two pointers to compare meeting times
    i = 0
    j = i + 1

    # till j reaches end
    while j < len(arr):
        if arr[j][0] < arr[i][1]:
            return False
        i += 1
        j += 1

    return True


print(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
print(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))
print(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))
