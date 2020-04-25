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

# n^2 solution


def minimum_meeting_rooms(arr):
    arr.sort()
    max_overlap = 0
    n = len(arr)
    for i in range(n):
        overlaps = _find_overlaps(arr, i)
        max_overlap = max(max_overlap, overlaps)
    return max_overlap


def _find_overlaps(arr, index):
    overlaps = 1
    prev_index = index - 1
    # check all previous meetings for overlap.
    while prev_index >= 0:
        start = max(arr[prev_index][0], arr[index][0])
        end = min(arr[prev_index][1], arr[index][1])
        if end > start:
            overlaps += 1
        prev_index -= 1
    return overlaps

# O(nlogn) time and O(n) space with heap data structure.


def minimum_meeting_rooms_heap(arr):
    arr.sort()
    heap = []
    min_rooms = 0
    for interval in arr:
        # if there are meeting and current meeting start time is less than
        # other meetings end time, keep removing the ended meeting.
        while len(heap) > 0 and interval[0] >= heap[0]:
            heapq.heappop(heap)
        # insert current meeting end time
        heapq.heappush(heap, interval[1])
        # calculate the min_rooms based on the heap elements.
        min_rooms = max(min_rooms, len(heap))
    return min_rooms


print(minimum_meeting_rooms_heap([[1, 4], [2, 3], [3, 6]]))
