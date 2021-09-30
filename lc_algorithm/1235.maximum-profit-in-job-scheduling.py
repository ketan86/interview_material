#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
"""
1235. Maximum Profit in Job Scheduling Hard

1548

16

Add to List

Share We have n jobs, where every job is scheduled to be done from startTime[i]
to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit
you can take such that there are no two jobs in the subset with overlapping time
range.

If you choose a job that ends at time X you will be able to start another job
that starts at time X.

Example 1:


Input: startTime = [1, 2, 3, 3], endTime = [3, 4, 5, 6], profit = [50, 10, 40, 70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range[1-3]+[3-6], we get profit of 120 = 50 + 70.
Example 2:


Input: startTime = [1, 2, 3, 4, 6], endTime = [3, 5, 10, 6, 9], 
    profit = [20, 20, 100, 70, 60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:


Input: startTime = [1, 1, 1], endTime = [2, 3, 4], profit = [5, 6, 4]
Output: 6


Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104


"""
# @lc code=start
import heapq


class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        """
        Runtime: 612 ms, faster than 50.61%

        if heap is not empty, pop each element and find max among them

        # heapify
        [5, 40+50 = 90]
        [7, 70+50 = 120]

        [7, 70+50 = 120]
        [5, 40+50 = 90]
        pop entry with end time 3. - max_profit = 50

        # heapify
        [3, 50+0 = 50]
        [4, 10+0 = 10]

        [4, 10+0 = 10]
        [3, 50+0 = 50]
        end_time, profit   max_profit = 0
        """
        # zip start,end, profit and sort by start time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])

        min_heap = []  # end_time, max_profit
        max_profit = 0

        # iterate over the job
        for start, end, profit in jobs:
            # delete all the jobs that have finished
            while min_heap and min_heap[0][0] <= start:
                top = heapq.heappop(min_heap)
                # find the max profit from ended jobs.
                max_profit = max(max_profit, top[1])

            # add current job and by adding current profit to max_profit
            heapq.heappush(min_heap, (end, profit + max_profit))

        # if head is not empty
        while min_heap:
            top = heapq.heappop(min_heap)
            max_profit = max(max_profit, top[1])

        return max_profit


print(Solution().jobScheduling(startTime=[1, 2, 3, 3], endTime=[
      3, 4, 5, 6], profit=[50, 10, 40, 70]))
# @lc code=end
