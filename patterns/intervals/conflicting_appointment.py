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
    arr.sort()
    i = 0
    j = i + 1
    while j < len(arr):
        start = max(arr[i][0], arr[j][0])
        end = min(arr[i][1], arr[j][1])
        if end > start:
            return False
        i += 1
        j += 1
    return True


print(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
