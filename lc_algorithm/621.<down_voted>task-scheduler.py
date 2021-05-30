#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (46.09%)
# Likes:    1851
# Dislikes: 321
# Total Accepted:    98.1K
# Total Submissions: 212.9K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks. Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
#
#
#
# Example:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#
#
#
# Note:
#
#
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
#
#
#

# @lc code=start
# pylint: skip-file

from collections import defaultdict
import heapq


class Solution:
    def NOT_WORKING_leastInterval(self, tasks, n):
        """
        tasks : number of tasks
        n     : number of different task must run before the same task can be
                scheduled.

        A A A, n = 2
        A I I A I I A -> use as many idle as you want to to make sure two
            same tasks are not running without n intervals.

        A B C A B C, n = 2
        A B C A B C -> here we dont need any idle interval since same tasks
            are running n intervals apart.
        """
        task_freq_map = defaultdict(int)

        for task in tasks:
            task_freq_map[task] += 1

        # use max heap to store tasks that are frequent, the reason being,
        # running the more frequent tasks first would reduce the amount of
        # idle time
        # for ex, A B B A A A > n=2
        # B A I B A I I A I I A = 11 (where less frequent task is chosen first)
        # A B I A B I A I I A = 10 (by chossing more frequent task, we reduce
        # the idle time)
        # hence, max_heap is a right data structure. max_heap with freq also
        # known as priority queue.
        max_heap = []

        for task, freq in task_freq_map.items():
            heapq.heappush(max_heap, (-freq, task))

        total_intervals = 0

        while max_heap:
            i = 0
            tasks = set()
            while i <= n:
                if max_heap:
                    freq, task = heapq.heappop(max_heap)
                    if freq < 0:
                        tasks.add((freq + 1, task))
                    else:
                        heapq.heappop(max_heap)

                total_intervals += 1

                if not max_heap and not tasks:
                    break

                i += 1

            for task in tasks:
                heapq.heappush(max_heap, task)

        return total_intervals


print(Solution().leastInterval(["A", "B", "C", "D"], 2))
print(Solution().leastInterval(
    ["G", "A", "C", "B", "F", "C", "D", "A", "B"], 2))
# @lc code=end
