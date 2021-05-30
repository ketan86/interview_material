#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

# A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right
# direction until reaching the matrix's end. For example, the matrix diagonal
# starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells
# mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
# order and return the resulting matrix.


# Example 1:


# Input: mat = [
#   [3, 3, 1, 1],
#   [2, 2, 1, 2],
#   [1, 1, 1, 2]
# ]
# Output: [
#   [1, 1, 1, 1],
#   [1, 2, 2, 2],
#   [1, 2, 3, 3]
# ]

# Example 2:

# Input: mat = [
#   [11, 25, 66, 1, 69, 7],
#   [23, 55, 17, 45, 15, 52],
#   [75, 31, 36, 44, 58, 8],
#   [22, 27, 33, 25, 68, 4],
#   [84, 28, 14, 11, 5, 50]
# ]
#
# Output: [
#   [5, 17, 4, 1, 52, 7],
#   [11, 11, 25, 45, 8, 69],
#   [14, 23, 25, 44, 58, 15],
#   [22, 27, 31, 36, 50, 66],
#   [84, 28, 75, 33, 55, 68]
# ]


# Constraints:

# m == mat.length n == mat[i].length 1 <= m, n <= 100 1 <= mat[i][j] <= 100


# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def diagonalSort(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # diagonal map with min_heap
        diagonal_map = defaultdict(list)

        # iterate over matrix and push diagonal elements into respective
        # map

        # NOTE: key here is to find a key that is same for each diagonal
        # elements. subtracting col from row yields same key for diagonal.
        #       0        1        2        3   4   5
        #   0  [11(0-0), 25,      66,      1,  69, 7],
        #   1  [23{1-0}, 55(1-1), 17,      45, 15, 52],
        #   2  [75,      31{2-1}, 36(2-2), 44, 58, 8],
        #   3  [22,      27,      33,      25, 68, 4],
        #   4  [84,      28,      14,      11, 5,  50]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                heapq.heappush(
                    diagonal_map[row - col], matrix[row][col])

        # iterate over matrix and replace elements in sorted order
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = heapq.heappop(diagonal_map[row - col])

        return matrix


matrix = [
    [11, 25, 66, 1, 69, 7],
    [23, 55, 17, 45, 15, 52],
    [75, 31, 36, 44, 58, 8],
    [22, 27, 33, 25, 68, 4],
    [84, 28, 14, 11, 5, 50]
]

print(Solution().diagonalSort(matrix))
# @lc code=end
