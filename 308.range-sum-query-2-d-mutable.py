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
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]'
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

    def __init__(self, matrix: List[List[int]]):
        

    def update(self, row: int, col: int, val: int) -> None:
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

