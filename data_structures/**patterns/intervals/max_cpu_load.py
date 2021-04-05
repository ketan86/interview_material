"""
We are given a list of Jobs. Each Job has a Start time, an End time, and a CPU
load when it is running. Our goal is to find the maximum CPU load at any time
if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the
jobs are running at the same time i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any Job which is 15.
Example 3:

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
"""

# pylint: skip-file
from heapq import heappop, heappush
from functools import total_ordering
import time


@total_ordering
class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end

    def __repr__(self):
        return 'start: {}, end: {}'.format(self.start, self.end)

    __str__ = __repr__


def max_cpu_load(jobs):
    """
    jobs -> [Job(1, 8, 2), Job(6, 20, 1), Job(9, 16, 5), Job(13,17,3)]

    1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
    ----------------------
              1-8
                   ------------------------------------------------------
                                        6-20
                            -----------------------------
                                        9-16
                                            ----------------
                                                  13-17

    Min Heap -> Maintain job that is ending first


        max_cpu = 3 + 5 + 1 = max(9,6) -> [9]

    13-----17(end)  -> start_time 13 >= end_time 16 -> remove job ending with 8
    9-----16(end)
    6-----20(end)

        max_cpu = 5 + 1 -> max(6,3) -> 6
        min_heap (by end_time)

    9-----16(end)  -> start_time 9 >= end_time 8 -> remove job ending with 8
    1------8(end)
    6-----20(end)

        max_cpu = 2 + 1 -> max(3,0) -> 3
        min_heap (by end_time) - job ending at 20 moves down

    6-----20(end)  -> start_time 6 >= end_time 8
    1------8(end)

    """
    # sort by start time. here we explicitely mention the key because, __lt__
    # func of the Job class uses end time to store jobs in min_heap.
    jobs.sort(key=lambda x: x.start)

    # capture max cpu time.
    max_cpu_load = 0

    # min_heap to maintain job that ends
    min_heap = []
    for job in jobs:
        #  remove all jobs ended so far.
        while min_heap and job.start >= min_heap[0].end:
            heappop(min_heap)
        # push current job
        heappush(min_heap, job)
        # calculate max cpu load by summing the cpu load of all the jobs
        # that are running.
        max_cpu_load = max(max_cpu_load, sum(
            [job.cpu_load for job in min_heap]))
    return max_cpu_load


def WONT_WORK_max_cpu_load_no_heap(jobs):
    # merged based approach does not work since it does not consider the
    # start and end time of the job.
    # [Job(1, 8, 2), Job(6, 20, 1), Job(9, 16, 5), Job(13,17,3)]

    # sort by start time.
    jobs.sort()
    # instead of saving all merged items, we can only save the last item to
    # find out the max cpu load.
    # since max_cpu_load is calculated after every job, we can reset the
    # merged_job to current job if it is not mergable.
    merged_job = None
    max_cpu_load = 0
    # s_time = time.time()
    for job in jobs:
        # if merged job end time is greater than current job start time,
        # we can merge.
        if merged_job and merged_job.end > job.start:
            # merge job and add the current job cpu load
            merged_job = Job(
                max(merged_job.start, job.start),
                min(merged_job.end, job.end),
                merged_job.cpu_load + job.cpu_load
            )
        else:
            merged_job = job
        # calculate the max cpu load so far.
        max_cpu_load = max(max_cpu_load, merged_job.cpu_load)

    # print('total time without heap: {}'.format(time.time() - s_time))
    return max_cpu_load


# print(max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]))
# print(max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]))
# print(max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]))
# print(max_cpu_load(
#     [Job(1, 8, 2), Job(6, 20, 1), Job(9, 12, 5), Job(13, 17, 3)]))
print(max_cpu_load(
    [Job(1, 8, 2), Job(6, 20, 1), Job(9, 16, 5), Job(13, 17, 3)]))

# print(WILL_NOT_WORK_max_cpu_load_no_heap([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]))
# print(WILL_NOT_WORK_max_cpu_load_no_heap([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]))
# print(WILL_NOT_WORK_max_cpu_load_no_heap([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]))
# print(WILL_NOT_WORK_max_cpu_load_no_heap([Job(1, 8, 2), Job(6, 20, 1), Job(9, 16, 5), Job(13,17,3)]))
