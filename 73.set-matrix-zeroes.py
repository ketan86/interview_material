#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (40.59%)
# Likes:    1483
# Dislikes: 248
# Total Accepted:    260.7K
# Total Submissions: 626.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
#
# Example 1:
#
#
# Input:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# Example 2:
#
#
# Input:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#

# @lc code=start


class Solution:
    # def setZeroes(self, matrix):
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     zero_indexes = []

    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == 0:
    #                 zero_indexes.append((i, j))

    #     for p, q in zero_indexes:
    #         for i in range(rows):
    #             matrix[i][q] = 0
    #         for j in range(cols):
    #             matrix[p][j] = 0

    #     return matrix

    def setZeroes(self, matrix):
        import pdb
        pdb.set_trace()
        rows = len(matrix)
        cols = len(matrix[0])

        first_col_zero = False
        first_row_zero = False

        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        if first_row_zero:
            for i in range(cols):
                matrix[0][i] = 0

        return matrix


print(Solution().setZeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]))

# @lc code=end
