"""
Write a program that takes infinite stream of random numbers and provides a
method to query the top K largest integers encountered so far


Question:
K = 2
    3,3,1 > 3,1 (distinct) -> map and min_heap
K = 2
    3,3,1 > 3,3 (duplicate) -> min_heap
K = 2
    3,1


1. K with distinct elements(orderedDict) vs K with duplicates (min_heap)
"""
import heapq


class Solution:  # distinct

    def __init__(self, k):
        self.k = k
        self.num_set = set()
        self.min_heap = []

    def add(self, num):
        if num not in self.num_set:
            if len(self.min_heap) >= self.k and self.min_heap[-1] < num:
                removed = heapq.heappop(self.min_heap)
                self.num_set.remove(removed)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, num)
            self.num_set.add(num)

    def find_largest(self):
        return heapq.nlargest(self.k, self.min_heap)


class Solution2:  # non-distinct

    def __init__(self, k):
        self.k = k
        self.min_heap = []

    def add(self, num):
        if len(self.min_heap) >= self.k and self.min_heap[-1] < num:
            heapq.heapreplace(self.min_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

    def find_largest(self):
        return heapq.nlargest(self.k, self.min_heap)


s = Solution(3)
s.add(1)
s.add(3)
s.add(4)
s.add(3)
s.add(1)
s.add(2)
print(s.find_largest())
s.add(5)
print(s.find_largest())
