#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (31.14%)
# Likes:    1624
# Dislikes: 475
# Total Accepted:    298.5K
# Total Submissions: 924.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#

# @lc code=start

class Solution:

    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result

        # create row and col start and end boundries
        row_start = 0
        row_end = len(matrix) - 1
        col_start = 0
        col_end = len(matrix[0]) - 1

        # direction variable to store the direction
        direction = 0

        # run loop until within the bound
        while row_start <= row_end and col_start <= col_end:
            # go right
            if direction == 0:
                # traverse column by keeping the row fixed.
                for i in range(col_start, col_end + 1):
                    result.append(matrix[row_start][i])
                row_start += 1
                direction += 1
            # go down
            elif direction == 1:
                # traverse row by keeping the col fixed.
                for i in range(row_start, row_end + 1):
                    result.append(matrix[i][col_end])
                col_end -= 1
                direction += 1
            # go left
            elif direction == 2:
                # traverse col in reverse by keping the row fixed.
                for i in reversed(range(col_start, col_end + 1)):
                    result.append(matrix[row_end][i])
                row_end -= 1
                direction += 1
            # go up
            elif direction == 3:
                # traverse row in reverse by keeping the col fixed.
                for i in reversed(range(row_start, row_end + 1)):
                    result.append(matrix[i][col_start])
                col_start += 1
                direction += 1
            else:
                # reset the direction
                direction = 0

        return result

    # def spiralOrder(self, matrix):
    #     result = []
    #     return self.traverse(matrix, result)

    # def traverse(self, matrix, result):
    #     if len(matrix) == 0:
    #         return result
    #     if matrix:
    #         self.print_row(matrix, 0, result)
    #         matrix = [[matrix[i][j] for j in range(len(matrix[0]))]
    #                   for i in range(1, len(matrix))]
    #     if matrix:
    #         self.print_col(matrix, len(matrix[0]) - 1, result)
    #         matrix = [[matrix[i][j] for j in range(len(matrix[0]) - 1)]
    #                   for i in range(0, len(matrix))]
    #     if matrix:
    #         self.print_row(matrix, len(matrix) - 1, result, backward=True, )
    #         matrix = [[matrix[i][j] for j in range(len(matrix[0]))]
    #                   for i in range(0, len(matrix) - 1)]
    #     if matrix:
    #         self.print_col(matrix, 0, result, backward=True)
    #         matrix = [[matrix[i][j] for j in range(1, len(matrix[0]))]
    #                   for i in range(0, len(matrix))]
    #     return self.traverse(matrix, result)

    # def print_row(self, matrix, row, result, backward=False):
    #     if not backward:
    #         if len(matrix) != 0:
    #             for col in range(len(matrix[0])):
    #                 result.append(matrix[row][col])
    #     else:
    #         if len(matrix) != 0:
    #             for col in reversed(range(len(matrix[0]))):
    #                 result.append(matrix[row][col])

    #     return result

    # def print_col(self, matrix, col, result, backward=False):
    #     if not backward:
    #         if len(matrix[0]) != 0:
    #             for row in range(len(matrix)):
    #                 result.append(matrix[row][col])
    #     else:
    #         if len(matrix[0]) != 0:
    #             for row in reversed(range(len(matrix))):
    #                 result.append(matrix[row][col])
    #     return result


# a = Solution().spiralOrder([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(a)

# @lc code=end
