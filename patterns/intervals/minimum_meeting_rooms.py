"""
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.
Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
hold all the meetings.
 
"""

# pylint: skip-file
import heapq
import time
# n^2 solution


def minimum_meeting_rooms(arr):
    # for every meeting, find all previous meeting, that are overlapping with
    # current meeting.
    arr.sort()
    max_overlap = 0
    n = len(arr)
    for i in range(n):
        # check how many previous meeting are not yet ended ?
        overlaps = _find_overlaps(arr, i)
        # find max
        max_overlap = max(max_overlap, overlaps)
    return max_overlap


def _find_overlaps(arr, index):
    # for each meeting, at least one overlap is itself
    overlaps = 1
    prev_index = index - 1
    # check all previous meetings for overlap.
    while prev_index >= 0:
        # if previous meeting end time is greater than current meeting end time,
        # there is a overlap.
        if arr[prev_index][1] > arr[index][0]:
            overlaps += 1
        prev_index -= 1
    return overlaps

# O(nlogn) time and O(n) space with heap data structure.


def minimum_meeting_rooms_heap(arr):
    # we are keeping the meeting end time in

    # we are only keeping the running meeting in the heap so length of the
    # heap decides the number of rooms required.
    arr.sort()
    heap = []
    min_rooms = 0
    for interval in arr:
        # if there are meeting and current meeting start time is less than
        # other meetings end time, keep removing the ended meeting.
        while heap and interval[0] >= heap[0]:
            heapq.heappop(heap)
        # insert current meeting end time
        heapq.heappush(heap, interval[1])
        # calculate the min_rooms based on the heap elements.
        min_rooms = max(min_rooms, len(heap))
    return min_rooms


def WILL_NOT_WORK_minimum_meeting_rooms_no_heap(arr):
    # merged based approach does not work since it does not consider the
    # start and end time of the job.
    # [[1,8],[6,20],[9,16],[13,17]]

    # sort meetings by start time
    arr.sort()
    min_rooms = 0
    # store last meeting
    last_overlapped_meeting = None
    # total rooms that are currently overlapped due to meetings.
    total_overlapped_rooms = 0
    for interval in arr:
        if not last_overlapped_meeting:
            last_overlapped_meeting = interval
            total_overlapped_rooms = 1
        else:
            print(last_overlapped_meeting)
            if last_overlapped_meeting[1] > interval[0]:
                last_overlapped_meeting = [
                    max(last_overlapped_meeting[0], interval[0]),
                    min(last_overlapped_meeting[1], interval[1])
                ]
                total_overlapped_rooms += 1
            else:
                total_overlapped_rooms = 1
                last_overlapped_meeting = interval

        min_rooms = max(min_rooms, total_overlapped_rooms)
    return min_rooms


print(minimum_meeting_rooms([[1, 8], [6, 20], [9, 16], [13, 17]]))
print(minimum_meeting_rooms([[1, 4], [2, 3], [3, 6]]))
print(minimum_meeting_rooms([[5, 9], [2, 3], [3, 6], [4, 6], [6, 12]]))
print(minimum_meeting_rooms([]))
print(minimum_meeting_rooms([[1, 4]]))

print('----------')
print(minimum_meeting_rooms_heap([[1, 8], [6, 20], [9, 16], [13, 17]]))
print(minimum_meeting_rooms_heap([[1, 4], [2, 3], [3, 6]]))
print(minimum_meeting_rooms_heap([[5, 9], [2, 3], [3, 6], [4, 6], [6, 12]]))
print(minimum_meeting_rooms_heap([]))
print(minimum_meeting_rooms_heap([[1, 4]]))


# print(WILL_NOT_WORK_minimum_meeting_rooms_no_heap([[1,8],[6,20],[9,16],[13,17]]))
# print(WILL_NOT_WORK_minimum_meeting_rooms_no_heap([[1, 4], [2, 3], [3, 6]]))
# print(WILL_NOT_WORK_minimum_meeting_rooms_no_heap([]))
# print(WILL_NOT_WORK_minimum_meeting_rooms_no_heap([[5, 9], [2, 3], [3, 6], [4,6], [6,12]]))
# print(WILL_NOT_WORK_minimum_meeting_rooms_no_heap([[1, 4]]))
