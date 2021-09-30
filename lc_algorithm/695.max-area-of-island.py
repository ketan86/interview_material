#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
"""
Medium

3604

111

Add to List

Share
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
Accepted
283,325
Submissions
424,944
"""
# @lc code=start


class Solution:
    def maxAreaOfIsland(self, grid):
        """Runtime: 136 ms, faster than 83.75%"""
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self._find_area(grid, row, col))

        return max_area

    def _find_area(self, grid, row, col, islands=0):

        if row < 0 or col < 0 or row >= len(grid) or \
                col >= len(grid[row]) or grid[row][col] == 0:
            return islands

        islands += 1

        grid[row][col] = 0

        islands = self._find_area(grid, row-1, col, islands)
        islands = self._find_area(grid, row+1, col, islands)
        islands = self._find_area(grid, row, col-1, islands)
        islands = self._find_area(grid, row, col+1, islands)

        return islands
# @lc code=end
