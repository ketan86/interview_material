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

    def setZeroesMostEfficient(self, matrix):
        """Runtime: 120 ms, faster than 97.21%"""
        rows = len(matrix)
        cols = len(matrix[0])

        first_col_zero = False
        first_row_zero = False

        # find if first row has 0
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        # find if first col has 0
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # loop from 2nd row, 2nd col till end
        for i in range(1, rows):
            for j in range(1, cols):
                # if number is 0, set 0th row and 0th col to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # loop from 2nd row and 2nd col till end
        for i in range(1, rows):
            for j in range(1, cols):
                # if first row and col value is zero, set current number to zero
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # if first col is 0, set all rows to zero
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        # if first row is 0, set all cols to zero
        if first_row_zero:
            for i in range(cols):
                matrix[0][i] = 0

        return matrix

    def setZeroesBitMask(self, matrix):
        """
        Runtime: 156 ms, faster than 18.46%
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix

        m = len(matrix)
        n = len(matrix[0])

        # Use two integers to store the mask of the row and columns that are
        # zero using 1.
        row_mask = 0
        col_mask = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if element is zero
                if matrix[i][j] == 0:
                    # set bit at ith and jth index of row and col respectively
                    row_mask |= 1 << (m - i - 1)
                    col_mask |= 1 << (n - j - 1)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if either row and column was set, set it to zero.
                if self.is_bit_set(row_mask, m-i-1) == 1 \
                        or self.is_bit_set(col_mask, n - j-1) == 1:
                    matrix[i][j] = 0

    def is_bit_set(self, mask, position):
        return (mask >> position) & 1

    def setZeroesSlightlyEfficient(self, matrix):
        """
        # 124 ms, faster than 90.51%
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # store all rows and cols where value is 0
        row_set = set()
        col_set = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        # loop over the matrix
        for i in range(rows):
            for j in range(cols):
                # if both i and j are 0
                if i in row_set or j in col_set:
                    matrix[i][j] = 0

        return matrix


print(Solution().setZeroesSlightlyEfficient([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]))

# @lc code=end
