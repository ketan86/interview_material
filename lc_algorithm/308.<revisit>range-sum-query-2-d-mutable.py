#
# @lc app=leetcode id=308 lang=python3
#
# [308] Range Sum Query 2D - Mutable
#
# https://leetcode.com/problems/range-sum-query-2d-mutable/description/
#
# algorithms
# Hard (34.75%)
# Likes:    384
# Dislikes: 53
# Total Accepted:    44.7K
# Total Submissions: 128.3K
# Testcase Example:  '["NumMatrix","sumRegion","update","sumRegion"]\n' +
#  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],
#  [3,2,2],[2,1,4,3]]'
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
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
#
#
#
# Note:
#
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is
# distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
#
#
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix):
        """Runtime: 132 ms, faster than 85.31%

        This solution could also work when shape is not rectangle or square.
        Even when region is triangle, this algorithm can find the sum.

                1 2 3 4 5 6 7
                    8 9 1
                      5 
        """
        self.matrix = matrix

        # 2-D dp matrix to store the current sum start from row 0 till column
        # NOTE: we have to use one extra colum to store the sum of all the col
        # values.
        # for ex, [1,2,3] -> [0,1,3,6]
        self.dp = [[0] * (len(self.matrix[0]) + 1)
                   for row in range(len(self.matrix))]

        # populate dp with sum values
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                # store sum of the current element with previous sum to next
                # column.
                self.dp[i][j+1] = self.dp[i][j] + self.matrix[i][j]

    def update(self, row: int, col: int, val: int) -> None:
        # subtract current value from the dp sum and add new value
        for i in range(col, len(self.matrix[row])):
            self.dp[row][i+1] = self.dp[row][i+1] - self.matrix[row][col] + val
        # update matrix with new value
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        # in order to find the sum of the row of the given region, we have to
        # look at the end col of the row and subtract sum that is at row1 to
        # find the sum of that row.
        # for ex,
        # [0,1,3,6] -> sum
        # [1,2,3] -> row 0
        # to find sum from row 1 to 2 we have to ->
        # dp[row0][col3] - dp[row0][col1]
        for i in range(row1, row2+1):
            sum_ += self.dp[i][col2+1] - self.dp[i][col1]
        return sum_

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
