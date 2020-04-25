#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (48.74%)
# Likes:    2208
# Dislikes: 161
# Total Accepted:    370.3K
# Total Submissions: 733.3K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#

# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # no unique distance if m or n is 0.
        if m == 0 or n == 0:
            return 0

        # construct mxn grid using list of list.
        paths = [[0 for j in range(n)] for i in range(m)]

        # set all distances to 1 for vertical cells.
        for i in range(m):
            paths[i][0] = 1

        # set all distances to 1 for horizontal cells.
        for j in range(n):
            paths[0][j] = 1

        # for rest of the cells starting from 1,1, find the distance
        # top and left cell distance addition
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i][j - 1] + paths[i - 1][j]

        # return the desired cell distance
        return paths[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution().uniquePaths(3, 3)
    print(s)

# @lc code=end
