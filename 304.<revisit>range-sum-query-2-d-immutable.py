#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (37.07%)
# Likes:    842
# Dislikes: 166
# Total Accepted:    105.6K
# Total Submissions: 284K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
#  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
#
#
#
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
#
#
# Example:
#
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
#
#
# Note:
#
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
#
#
#

# @lc code=start
# pylint: skip-file


class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.memo = {}

    def pre_process(self):
        if not self.matrix:
            return
        dp = [matr]

    def sumRegion(self, row1, col1, row2, col2):
        sum_ = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                sum_ += self.matrix[row][col]
        return sum_


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
# @lc code=end
