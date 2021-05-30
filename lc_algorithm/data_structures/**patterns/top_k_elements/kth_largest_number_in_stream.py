"""
Design a class to efficiently find the Kth largest element in a stream of
numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing
initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the
given number and return the Kth largest number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
 
"""
# pylint : skip-file
import heapq


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.min_heap = []
        self.k = k
        # add numbers to a heap
        for num in nums:
            self.add(num)

    def add(self, num):
        heapq.heappush(self.min_heap, num)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


def main():

    kth_largest = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kth_largest.add(6)))
    print("4th largest number is: " + str(kth_largest.add(13)))
    print("4th largest number is: " + str(kth_largest.add(4)))


main()
