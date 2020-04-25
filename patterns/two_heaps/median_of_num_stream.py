"""
Median is the middle value of a set of data. To determine the median
value in a sequence of numbers, the numbers must first be arranged in
ascending order.

- If there is an odd amount of numbers, the median value is the number
that is in the middle, with the same amount of numbers below and above.

- If there is an even amount of numbers in the list, the median is the
average of the two middle values.

---|

Design a class to calculate the median of a number stream.
The class should have the following two methods:

insertNum(int num)  : stores the number in the class
findMedian()        : returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will
be the average of the middle two numbers.

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
"""
# pylint: skip-file

import heapq


class MedianOfAStream:
    def __init__(self):
        self.min_heap = []
        # invert the sign of the integer and store them in min_heap like
        # structure.
        self.max_heap = []

    def insert_num(self, num):
        # if max heap is empty or num is less than equal to max_heap first
        # element, pust it to max heap, else to min_heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # balance heap when diff is greater than 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # this condition to always keep one element extra only in max heap
        # so when median has to be found for odd elements, we look up the
        # max heap.
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        print('min_heap', self.min_heap)
        print('max_heap', self.max_heap)

    def find_median(self):
        # if max heap and min heap size is same, return median of the first
        # elements of both heap
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # else, max element of heap
        else:
            return - self.max_heap[0]


def main():
    median_of_stream = MedianOfAStream()
    median_of_stream.insert_num(3)
    median_of_stream.insert_num(1)
    print("The median is: " + str(median_of_stream.find_median()))
    median_of_stream.insert_num(5)
    print("The median is: " + str(median_of_stream.find_median()))
    median_of_stream.insert_num(4)
    print("The median is: " + str(median_of_stream.find_median()))


main()
