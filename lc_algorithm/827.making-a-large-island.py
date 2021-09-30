#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid) -> int:
        """Runtime: 4276 ms, faster than 31.41% """

        # input -> [[1,0],[0,1]]
        # create area map {'index' : area}
        area = {}
        # we are setting index on the grid during dfs to mark that area with
        # unique index and it's area size.
        # area -> {2:1, 3:1}
        index = 2
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    area[index] = self.dfs(row, col, grid, index)
                    index += 1

        # grid -> [[2, 0], [0, 3]]

        # we can't rely on max value because we have to go through all places
        # where it's 0. find neighboring cells where value is greater than
        # 1 and sum all connected areas + 1 (current 0 to mark 1) and keep
        # calculating the max ans.
        ans = max(area.values() or [0])

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    # find all connected neighbors where value is gerater
                    # than 1.
                    n_areas = set()
                    for n_row, n_col in self.neighbors(row, col, grid):
                        if grid[n_row][n_col] > 1:
                            n_areas.add(grid[n_row][n_col])
                    ans = max(ans, 1 + sum(area[i] for i in n_areas))

        return ans

    def dfs(self, row, col, grid, index):
        ans = 1
        grid[row][col] = index
        for n_row, n_col in self.neighbors(row, col, grid):
            if grid[n_row][n_col] == 1:
                ans += self.dfs(n_row, n_col, grid, index)

        return ans

    def neighbors(self, row, col, grid):
        for n_row, n_col in ((row-1, col), (row+1, col), (row, col-1), (row, col + 1)):
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid):
                yield n_row, n_col

# @lc code=end
