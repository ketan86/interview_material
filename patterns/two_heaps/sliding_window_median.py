"""
Problem Statement #
Given an array of numbers and a number ‘k’, find the median of all
the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
"""
# pylint: skip-file
import heapq


class SlidingWindowMedian:

    def find_sliding_window_median(self, arr, k):
        result = []
        n = len(arr)
        # loop over the array till 0 to n - (k-1) times
        for i in range(n - (k - 1)):
            result.append(self._find_median_sub_array(arr[i:i + k]))
        return result

    def _find_median_sub_array(self, arr):
        min_heap = []
        max_heap = []
        # insert data into heap
        for num in arr:
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2
        else:
            return -max_heap[0]


def main():

    sliding_window_median = SlidingWindowMedian()
    result = sliding_window_median.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    sliding_window_median = SlidingWindowMedian()
    result = sliding_window_median.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
