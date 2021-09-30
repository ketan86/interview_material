#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """Runtime: 112 ms, faster than 82.00%"""

    def construct(self, grid):
        # dfs with root node
        return self.dfs(
            grid, 0, 0, len(grid), len(grid[0]), self.create_node())

    def create_node(self):
        # helper method to initialize node
        return Node(0, False, None, None, None, None)

    def dfs(self, grid, s_row, s_col, e_row, e_col, node):
        # if elements are same, set it's value and isLeft to True
        if self.is_same(grid, s_row, s_col, e_row, e_col):
            node.val = grid[s_row][s_col]
            node.isLeaf = True
        else:

            # divide the grid in 4 section
            row_half = (e_row + s_row) // 2
            col_half = (e_col + s_col) // 2

            # set current node's child
            node.topLeft = self.dfs(
                grid, s_row, s_col, row_half, col_half, self.create_node())
            node.topRight = self.dfs(
                grid, s_row, col_half, row_half, e_col, self.create_node())
            node.bottomLeft = self.dfs(
                grid, row_half, s_col, e_row, col_half, self.create_node())
            node.bottomRight = self.dfs(
                grid, row_half, col_half, e_row, e_col, self.create_node())

        return node

    def is_same(self, grid, s_row, s_col, e_row, e_col):
        # check if values are same or not
        value = grid[s_row][s_col]
        for row in range(s_row, e_row):
            for col in range(s_col, e_col):
                if grid[row][col] != value:
                    return False
        return True


# print(Solution().construct([[0,1],[1,0]]))
print(Solution().construct(
    [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]
    ]))


# @lc code=end
