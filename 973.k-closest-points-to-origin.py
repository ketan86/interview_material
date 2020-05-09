#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (62.07%)
# Likes:    1389
# Dislikes: 107
# Total Accepted:    224.4K
# Total Submissions: 361.1K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#

# @lc code=start
# pylint:skip-file
import heapq

class Solution:
    def kClosest(self, points, K):
        if not points:
            return points

        # use max heap to store the K closest points
        max_heap = []

        for point in points:
            # only square of the points will be enough to decide if
            # it is closest to origin or not compare to other points.
            sq = (point[0] * point[0]) + (point[1] * point[1])

            # add first k points 
            if len(max_heap) < K:
                heapq.heappush(max_heap, (-sq, point))
            else:
                # peek top point and if current point is closest compare
                # to the the one at top, replace the element.
                last_sq = max_heap[0][0]
                if last_sq <= -sq:
                    heapq.heapreplace(max_heap, (-sq, point))
        
        # pop top k elements and return the result.
        result = []
        for _ in range(K):
            result.append(heapq.heappop(max_heap)[1])
        
        return result

# print(Solution().kClosest([[10000, 10000], [5, -1], [-2, 4]], K=2))

# @lc code=end

