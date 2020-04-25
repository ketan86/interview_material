"""
We are given a list of Jobs. Each Job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

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


@total_ordering
class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.start < other.start


def max_cpu_load(jobs):
    # sort by start time
    jobs.sort()
    max_cpu_load = 0
    min_heap = []
    current_cpu_load = 0
    for job in jobs:
        #  remove all jobs ended so far.
        while (len(min_heap) > 0 and job.start >= min_heap[0].end):
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)
        # insert current job
        current_cpu_load += job.cpu_load
        heappush(min_heap, job)
        # calculate max cpu load using running avg
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load


print(max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]))
print(max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]))
print(max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]))
