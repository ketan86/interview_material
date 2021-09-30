#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxPoints(self, points) -> int:
        """
        Runtime: 60 ms, faster than 56.95%

        naive O(n^2) time, check all points with all others points
        use the fact that the slope between points on the same line is the same for
        all points on that line.

        find slope of the line that contains two points (-3,2) and (4,1)

        slope = y2-y1/x2-x1
              = 1-2/4-(-3)
              = -1/7
                y
        (-3,2)* |
                |      *(4,1)
        --------|---------x
                |
                |

        (3,-2), (3,4)
                |
                |      *(3,4)
                |
        --------|---------x
                |
                |      *(3,-2)

        maintain the slope in a dict and use the max occurrance of the slope value
        to calculate the max length

        Time -> O(n^2)
        Space -> O(n)
        """
    
        if len(points) == 1:
            return 1

        largest = 0
        # for each point, calculate the angle between two points
        for i in range(len(points)):
            slope_map = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    p1, p2 = points[i], points[j]
                    x = float(p2[0] - p1[0])
                    y = float(p2[1] - p1[1])
                    # if x == 0, we get vertical line, represented with
                    # "inf" slope.
                    if x == 0:
                        # (3,-2), (3,4)
                        #         |
                        #         |      *(3,4)
                        #         |
                        # --------|---------x
                        #         |
                        #         |      *(3,-2)
                        slope = float('inf')
                    else:
                        # if x and y both are 0, we get horizontal line,
                        # represented with "0" slope
                        # else, find slope.
                        slope = y/x

                    slope_map[slope] += 1

            largest = max(largest, max(slope_map.values()))

        # slope would 1 less than the actual points so need to add 1 to answer.
        return largest + 1


print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
print(Solution().maxPoints([[0, 0], [0, 0], [0, 0]]))
print(Solution().maxPoints([[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17], [13, -3], [3, 7], [-11, 12], [7, 19], [19, -12], [20, -18], [-16, -15], [-10, -15], [-16, -18], [-14, -1], [18, 10], [-13, 8], [7, -5], [-4, -9], [-11, 2], [-9, -9], [-5, -16], [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5], [15, -11], [3, 11], [11, -10], [-1, -7], [16, 7], [1, -11], [-8, -3], [1, -6], [19, 7], [3, 6], [-1, -2], [7, -3], [-6, -8], [7, 1], [-15, 12], [-17, 9], [19, -9], [
      1, 0], [9, -10], [6, 20], [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9], [-15, 15], [-3, -15], [-5, 20], [15, -14], [9, -17], [10, -14], [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1], [-17, -5], [15, -2], [-12, 11], [19, -18], [8, 7], [-5, -3], [-17, -1], [-18, 13], [15, -3], [4, 18], [-14, -15], [15, 8], [-18, -12], [-15, 19], [-9, 16], [-9, 14], [-12, -14], [-2, -20], [-3, -13], [10, -7], [-2, -10], [9, 10], [-1, 7], [-17, -6], [-15, 20], [5, -17], [6, -6], [-11, -8]]))
# @lc code=end
