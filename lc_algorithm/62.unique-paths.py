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
        """
        Runtime: 28 ms, faster than 87.99%

        for 3x3 grid,

                     1step     2..n step
        [x 0 0]    [x 1 1]     [x 1 1]    [x 1 1]          [x 1 1]
        [0 0 0] -> [1 0 0]  -> [1 2 0] -> [1 2 3] -> .. -> [1 2 3]
        [0 0 0]    [1 0 0]     [1 0 0]    [1 0 0]          [1 3 6]

        1 step:
            we fill first row's columns and first column's rows with 1
            because we can only reach at those cells from one direction.
            because we can't come from bottom or right.

        2 step:
            starting from [1][1] .. [n][n], we keep summing ways from top
            and left to find the total paths to reach that cell.

            for ex, [1][1] -> [0][1](1) + [1][0](1) = 2 paths
                    [2][2] -> [1][2](3) + [2][1](3) = 6 paths
        """
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

        # Replaces above 3 steps:
        # matrix = [0] * m
        # for i in range(m):
        #     matrix[i] = [0] * n
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             matrix[i][j] = 1
        #         else:
        #             matrix[i][j] = 0

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
