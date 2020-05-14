#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (45.80%)
# Likes:    4949
# Dislikes: 187
# Total Accepted:    669.9K
# Total Submissions: 1.5M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
# pylint: skip-file
class Solution:
    def numIslands(self, grid):
        """
        when we land on the island, we explore the island till we find the
        water and then return 1 to represent that island.
        for ex,
            11110
            11010
            11000
            00000
        at index [0][0], if is 1, we start exploring the island on all
        sides. before exploring all sides, we mark the current index `0`
        to indicate that it has been visited. During the exploration, we
        will either cover all grid cells if all of them are 1 or the land
        that is attached to index[0][0]. once we find water (0's) on all
        the directions, we stop and consider the whole exploration a 1 island.

        we expolore all indexes and all the land around each index if it is
        a land.

        all these islands are summed together to find total islands.
        """
        # store the count of islands 
        islands = 0

        # edge condition check
        if not grid:
            return islands

        def dfs(i, j):
            # if we are out of bound, return 0
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return 0
            
            # if we find the water, return 0
            if grid[i][j] == '0':
                return 0

            # NOTE: Above base conditions are only used when i and j that are
            # out of bound.

            # mark the current index '0' and explore all directions from
            # current index.
            grid[i][j] = '0'
            
            # dfs on all the directions.
            # NOTE: here the returned value of the dfs call is not used
            # for anything.
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

            # if we explored all the directions and returned, we are done
            # covering the island (or we reached water on all the sides)
            # at index[i][j]. return 1 to indicate we found one island.
            return 1

        # traverse each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # if current cell value is 1, we are interested knowing
                # if all side of current cell is 0.
                if grid[i][j] == '1':
                    islands += dfs(i, j)
        return islands

# @lc code=end

