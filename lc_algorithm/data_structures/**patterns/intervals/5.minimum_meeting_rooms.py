"""
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.

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
    """
    NOTE: Keep meetings in the min_heap such that meeting are sorted based on
    their end time. (meeting that are ending first)

    For a new meeting, check and remove the meeting that are ended so far
    before adding new meeting in the heap.

    Meetings -> [1,2], [3,5], [4,6], [5,8]

    1. sort meeting by their start time and end time if start time is same.
    2. process meeting [1,2] and remove all the meeting from the heap that
       are ended. 
    3. add current meeting in the heap.
    4. calculate minimum meeting rooms by using
        max(prev_minimum_rooms, len(heap))

            min_meeting_rooms = 0

            1-2 
                -> no meeting rooms in heap so nothing to remove
                -> [1-2] goes in the min_heap
                    - min_heap -> [1-2]
                -> min_meeting_rooms = 1
            3-5
                -> meeting start time(3) > [1-2] end_time(2)
                    - meeting [1,2] has finished so remove from the min_heap
                -> [3-5] goes in the min_heap
                    - min_heap -> [3-5]
                -> min_meeting_rooms = 1
            4-6
                -> meeting start time(4) < [3-5] end_time(5)
                    - meeting [3-5] has not finished so keep it in the min_heap
                -> [4-6] goes in the min_heap
                    - min_heap -> [3-5], [4-6] (sorted by end time)
                -> min_meeting_rooms = 2
            5-8
                -> meeting start time(5) <= [3-5] end_time(5)
                    - meeting [3-5] has finished so remove from the min_heap
                    - meeting [4-6] has not finished so keep it in the min_heap
                -> [5-8] goes in the min_heap
                    - min_heap -> [4-6], [5-8] (sorted by end time)
                -> min_meeting_rooms = 2


    """
    # we are only keeping the running meeting in the heap so length of the
    # heap decides the number of rooms required.

    # sort meeting by start time and end time if start time is same.
    arr.sort()

    # min heap to maintain running meeting
    min_heap = []
    min_rooms = 0
    for interval in arr:
        # if there are meeting and current meeting start time is less than
        # other meetings end time, keep removing the ended meeting.
        while min_heap and interval[0] >= min_heap[0]:
            heapq.heappop(min_heap)
        # insert current meeting end time
        heapq.heappush(min_heap, interval[1])
        # calculate the min_rooms based on the heap elements.
        min_rooms = max(min_rooms, len(min_heap))
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
print('hi', minimum_meeting_rooms([[1, 2], [3, 5], [4, 6], [5, 8]]))

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
