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


"""
Solution 1 (nlog(n)): Add number to a list and when findMedian is called, sort
the number and return the mid value of odd or sum(left+right)/2 from the
middle.

Solution 2 (log(n)): In order to find the median (both for odd and even count)
we need to somehow maintain numbers such that the one set contains numbers
in decresing and other in increasing order.

for ex, 1,3,5,7,2,4,8   -> sorted version 1,2,3,4,5,7,8
              ->--------------->-
             |  4                |
             |  3              5 |
             |  2              7 |
             |  1              8 |
           ->                     ->
            max_heap       min_heap

  if we make sure max and min heap contains equal or max heap one extra element
  at most, finding the median is picking the top element of the max heap
  when odd or average of the max and min heap top elements.

  How to we preserve data on max and min heap in this order. The simplest
  solution is to,
      1. put the element in the max_heap first
         - elements could remain on top or move down
      2. then move the top of the element to the min_heap
         - picking the top element could be the max of the max_heap and may
           not be the same element we inserted in the above step.
      3. them move it back to max_heap if min_heap elements are greater than
         max_heap.
         - same as step 2.

      Doing such operations ensures that the elements order in the heaps is
      maintained.
"""




import heapq
class MedianOfAStream:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # ** median of numbers can only be found when nums are sorted.
        # now if we think about sorted number, it's increasing from left to right
        #   and decreasing from right to left. [1,2,3,4,5,6,7]
        # if we store 1 to 4 in max_heap and 5 to 7 in min_heap, 4 at the top of the
        #   max_heap would be a median else (top of the min_heap + top of the max_heap) / 2.
        # we can simply do that by adding number to max_heap first (considering that
        #   max_heap contains one extra element) and then move top element to min_heap
        #   to allow number to sort and later if min_heap has extra element, move it to
        #   min_heap.

        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # push element to max heap.
        # NOTE: insert negative values to maintain the heap property.
        heapq.heappush(self.max_heap, -num)
        # move top element of the max heap to the min heap.
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # if min_heap elements are greater than the max_heap, move top element
        # of the min_heap to max_heap.
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # if heap sizes are same, median is average of the two elements in the
        # middle
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # else, max_heap top element is the median.
        return -self.max_heap[0]

# **ANOTHER SOLUTION** -> checks before pushing it to min or max heap.


class MedianOfAStreamSolution2:
    def __init__(self):
        self.min_heap = []
        # invert the sign of the integer and store them in min_heap like
        # structure.
        self.max_heap = []

    def addNum(self, num):
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

    def findMedian(self):
        # if max heap and min heap size is same, return median of the first
        # elements of both heap
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # else, max element of heap
        else:
            return - self.max_heap[0]


def main():
    median_of_stream = MedianOfAStream()
    median_of_stream.addNum(3)
    median_of_stream.addNum(1)
    print("The median is: " + str(median_of_stream.findMedian()))
    median_of_stream.addNum(5)
    print("The median is: " + str(median_of_stream.findMedian()))
    median_of_stream.addNum(4)
    print("The median is: " + str(median_of_stream.findMedian()))


main()
