#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.

# Example 1:

# Input: matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Output: [
#   [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9]
# ]
# Example 2:

# Input: matrix = [[1, 2, 3], [4, 5, 6]]
# Output: [[1, 4], [2, 5], [3, 6]]

# Example 3:

# Input: matrix = [
#      0   1   2   3
#   0 [1,  2,  3,  4 ],
#   1 [5,  6,  7,  8 ],
#   2 [9,  10, 11  12],
#   3 [13, 14, 15, 16],
# ]
# Output: [
#   [1, 5, 9,  13],
#   [2, 6, 10, 14],
#   [3, 7, 11, 15],
#   [4, 8, 12, 16]
# ]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# -109 <= matrix[i][j] <= 109

# @lc code=start
class Solution:
    def FAILED_transpose(self, matrix):
        # does not handle mxn where m and n sizes are different
        for row in range(len(matrix)):
            for col in range(row, len(matrix[row])):
                matrix[row][col], matrix[col][row] = \
                    matrix[col][row], matrix[row][col]
        return matrix

    def transpose(self, matrix):
        # result list
        result = []
        # go over the col and put them as row in result
        for col in range(len(matrix[0])):
            temp = []
            # go over the row one by one and create temp
            # list
            for row in range(len(matrix)):
                temp.append(matrix[row][col])

            # put temp list in result
            result.append(temp)
        return result

    def transpose(self, matrix):
        row, col = len(matrix), len(matrix[0])

        # create transposed list
        result = [[None] * row for _ in range(col)]

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                result[j][i] = col

        return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11,  12],
    [13, 14, 15, 16],
]
matrix3 = [
    [1, 2, 3],
    [4, 5, 6]
]

print(Solution().transpose(matrix))
print(Solution().transpose(matrix2))
print(Solution().transpose(matrix3))
# @lc code=end
