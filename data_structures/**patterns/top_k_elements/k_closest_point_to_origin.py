"""
Given an array of points in the a 2D2D plane, find ‘K’ closest points to
the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""
# pylint: skip-file
import heapq


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return -self.get_distance() < -other.get_distance()

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def get_distance(self):
        return (self.x * self.x) + (self.y * self.y)


def find_closest_points(points, k):
    # use max heap to store the distance from the origin
    max_heap = []
    for point in points:
        # till k points, store it in the max heap
        if len(max_heap) < k:
            heapq.heappush(max_heap, point)
        else:
            # if point is less than the max heap top, replace the top
            # element with current point.
            if max_heap[0] < point:
                heapq.heapreplace(max_heap, point)
    return max_heap


def main():

    result = find_closest_points(
        [Point(1, 3), Point(3, 4), Point(2, -1), Point(3, 2)], 3)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
