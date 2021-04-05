#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (50.05%)
# Likes:    2219
# Dislikes: 185
# Total Accepted:    325.7K
# Total Submissions: 620.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
# Example 1:
#
#
# Given input matrix =
# [
# ⁠ [1,2,3],          [7,4,1]
# ⁠ [4,5,6],          [8,5,6]
# ⁠ [7,8,9]           [9,2,3]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
#
#
# Example 2:
#
#
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
#
#
#

# @lc code=start


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.

        1. swap rows
        # [
        # ⁠ [1,2,3],      [7,8,9]          [7,4,1]
        # ⁠ [4,5,6],   -> [4,5,6]      ->  [8,5,6]
        # ⁠ [7,8,9]       [1,2,3]          [9,2,3]
        # ],
        """
        i = 0
        j = len(matrix) - 1

        # swap rows
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        # swap diagonally. only swap upper right triangle.
        # [7,8,9]              [7 8 9]
        # ⁠[4,5,6] swap only ->    5 6]
        # ⁠[1,2,3]                   3]
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # m = len(matrix)
        # n = len(matrix[0])

        # # transpose matrix
        # for i in range(m):
        #     for j in range(i, n):  # <------ key
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # print(matrix)
        # # swap colums
        # for i in range(m):
        #     for j in range(int(n / 2)):  # <----- key
        #         matrix[i][j], matrix[i][n -
        #                                 (j + 1)] = matrix[i][n - (
        #                                     j + 1)], matrix[i][j]
        #     # or matrix[i].reverse()
        # return matrix


print(Solution().rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

# print(Solution().rotate([
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]))


# @lc code=end
