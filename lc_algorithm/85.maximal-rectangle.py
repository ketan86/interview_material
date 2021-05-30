#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix) -> int:
        """
        https://www.xiaokangstudynotes.com/dynamic-programming-maximal-rectangle/
        """
        # if not matrix, return 0
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        # left = [0,0,0,0,0]
        left = [0] * n  # initialize left as the leftmost boundary possible
        # right = [5,5,5,5,5]
        right = [n] * n  # initialize right as the rightmost boundary possible
        # height = [0,0,0,0,0]
        height = [0] * n

        # max area so far
        max_area = 0

        for row in range(m):

            cur_left, cur_right = 0, n

            # update height
            for col in range(n):
                if matrix[row][col] == '1':
                    height[col] += 1

            # update left
            for col in range(n):
                if matrix[row][col] == '1':
                    left[col] = max(left[col], cur_left)
                else:
                    cur_left = col + 1

            # update right
            for col in range(n-1, -1, -1):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], cur_right)
                else:
                    cur_right = col

            # update the area
            for col in range(n):
                max_area = max(
                    max_area, height[col] * (right[col] - left[col]))

        return max_area


print(Solution().maximalRectangle(
    [
        ["0", "0", "1", "0"],
        ["0", "1", "1", "0"],
        ["0", "1", "1", "1"]
    ]))

# print(Solution().maximalRectangle(
#     [
#         ["1", "0", "1", "0", "0"],
#         ["1", "0", "1", "1", "1"],
#         ["1", "1", "1", "1", "1"],
#         ["1", "0", "0", "1", "0"]
#     ]))
# @lc code=end
