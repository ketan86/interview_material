#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#

# @lc code=start
import heapq


class Interval:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        if self.left == -1:
            self.distance = self.right
        elif self.right == n:
            self.distance = n - 1 - left
        else:
            self.distance = abs(left - right) // 2

    def __lt__(self, other):
        if self.distance == other.distance:
            return self.left < other.left
        else:
            return self.distance >= other.distance


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.max_heap = []
        heapq.heappush(
            self.max_heap, Interval(-1, self.n, self.n))

    def seat(self) -> int:
        seat = 0
        interval = heapq.heappop()
        if interval.left == -1:
            seat = 0
        elif interval.right == self.n:
            seat = self.n - 1
        else:
            seat = interval.left + interval.right // 2

        heapq.heappush(self.max_heap, Interval(interval.left, seat, self.n))
        heapq.heappush(self.max_heap, Interval(seat, interval.right, self.n))

        return seat

    def leave(self, p: int) -> None:
        head, tail = None, None
        for interval in self.max_heap:
            if interval.left == p:
                head = interval
            elif interval.right == p:
                tail = interval
            if head != None and tail != None:
                break

        self.max_heap.remove(head)
        self.max_heap.remove(tail)

        self.heap.append(Interval(tail.left, head.right, self.n))
        heapq.heapify(self.max_heap)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end
