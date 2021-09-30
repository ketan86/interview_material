"""
Problem:
1. An odd chess board with size (0,0) and (max,max) has single knight.
2. The knight can move to following neighboring fields
  (-2,-1), (-1,-2), (2,-1), (1,-2), (-1,2), (-2,1), (1,2) (2,1)


Q: find path for the minimum num of moves.
Q: Space/Time Complexity

Clarify:
1. what if path is not found.

"""
from collections import deque


class Solution:

    def is_valid(self, point, min_bound, max_bound):
        return min_bound[0] <= point[0] <= max_bound[0] and \
            min_bound[1] <= point[1] <= max_bound[1]

    def are_same(self, point1, point2):
        return point1[0] == point2[0] and point1[1] == point2[1]

    def min_move(self, start, end, min_bound, max_bound):

        # check if start and end is inside the boundary
        if not self.is_valid(start, min_bound, max_bound) or \
                not self.is_valid(end, min_bound, max_bound):
            return []

        queue = deque()

        # (start_x, start_y, number_of_moves)
        queue.append((start[0], start[1], 0))

        # store neighbors
        neighbors = [(-2, -1), (-1, -2), (2, -1), (1, -2),
                     (-1, 2), (-2, 1), (1, 2), (2, 1), (1, 1)]

        while queue:
            point = queue.popleft()

            if self.are_same(point, end):
                return point[2]

            for neighbor in neighbors:

                next_point = (point[0] + neighbor[0],
                              point[1] + neighbor[1], point[2] + 1)

                if self.is_valid(next_point, min_bound, max_bound):
                    queue.append(next_point)

        return -1

    def min_move_with_path(self, start, end, min_bound, max_bound):

        # check if start and end is inside the boundary
        if not self.is_valid(start, min_bound, max_bound) or \
                not self.is_valid(end, min_bound, max_bound):
            return []

        queue = deque()

        # (start_x, start_y, number_of_moves, parent)
        queue.append((start[0], start[1], 0, None))

        # store neighbors
        neighbors = [(-2, -1), (-1, -2), (2, -1), (1, -2),
                     (-1, 2), (-2, 1), (1, 2), (2, 1)]

        # store path
        path = []

        while queue:
            point = queue.popleft()

            if self.are_same(point, end):
                path.append(end)
                parent = point[3]

                while parent:
                    path.append((parent[0], parent[1]))
                    parent = parent[3]

                path.reverse()

                return len(path)

            for neighbor in neighbors:

                next_point = (point[0] + neighbor[0],
                              point[1] + neighbors[1], point[2] + 1, point)

                if self.is_valid(next_point):
                    queue.append(next_point)

        return -1


print(
    Solution().min_move((1, 1), (2, 2), (0, 0), (3, 3)))
