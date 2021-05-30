"""
Problem Statement #
Given an array of numbers and a number ‘k’, find the median of all
the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
 ----
[1, 2, -1, 3, 5] -> median is 0.5
    -----
[1, 2, -1, 3, 5] -> median is 1.0
       -----
[1, 2, -1, 3, 5] -> median is 4.0
           ----
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

# time complexity : 0(n*k log(k))
# space complexity : 0(k)


class SlidingWindowMedian:

    def find_sliding_window_median(self, arr, k):
        # define a result
        result = []
        n = len(arr)
        # loop over the array till 0 to n - (k-1) times to find the window
        for i in range(n - (k - 1)):
            result.append(self._find_median_sub_array(arr[i:i + k]))
        return result

    def _find_median_sub_array(self, arr):
        # use min and max heap to maintain the heap property
        min_heap = []
        max_heap = []
        # insert data into heap
        for num in arr:
            # move number to max heap
            heapq.heappush(max_heap, -num)
            # move top element of max heap to min heap
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

            # if min heap length is greater than max, move top
            # element of min heap to max heap
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # ANOTHER SOLUTION
            # if not max_heap or num <= -max_heap[0]:
            #     heapq.heappush(max_heap, -num)
            # else:
            #     heapq.heappush(min_heap, num)

            # if len(max_heap) > len(min_heap) + 1:
            #     heapq.heappush(min_heap, -heapq.heappop(max_heap))
            # elif len(min_heap) > len(max_heap):
            #     heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # return results
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2
        else:
            return -max_heap[0]
# Improve the above version by not creating a new array for finding
# the median. we can use the indexes.


class SlidingWindowMedianImprovedSolution:

    def find_sliding_window_median(self, arr, k):
        # define a result
        result = []
        n = len(arr)
        # loop over the array till 0 to n - (k-1) times to find the window
        for i in range(n - (k - 1)):
            result.append(self._find_median_sub_array(arr, i, i+k))
        return result

    def _find_median_sub_array(self, arr, start, end):
        # use min and max heap to maintain the heap property
        min_heap = []
        max_heap = []
        # insert data into heap. since k is added to i, end index is already
        # one step ahead.
        # for ex, [1,2], i-> 0 and k=2 so start=0, end=2
        for i in range(start, end):
            # move number to max heap
            heapq.heappush(max_heap, -arr[i])
            # move top element of max heap to min heap
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

            # if min heap length is greater than max, move top
            # element of min heap to max heap
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # return results
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

    # ------------------
    sliding_window_median = SlidingWindowMedianImprovedSolution()
    result = sliding_window_median.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    sliding_window_median = SlidingWindowMedianImprovedSolution()
    result = sliding_window_median.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
