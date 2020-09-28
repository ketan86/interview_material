#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (42.44%)
# Likes:    3006
# Dislikes: 58
# Total Accepted:    225.9K
# Total Submissions: 503.1K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
'[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
#
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
#
#
#
#
# Example:
#
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
#
#
#
# Follow up:
#
#
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
#
#
#

# @lc code=start
import heapq


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


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
