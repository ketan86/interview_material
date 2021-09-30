"""
361. Bomb Enemy Medium

617

82

Add to List

Share Given an m x n matrix grid where each cell is either a wall 'W', an enemy
'E' or empty '0', return the maximum enemies you can kill using one bomb. You
can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point
until it hits the wall since it is too strong to be destroyed.

Example 1:


Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Example 2:


Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 'W', 'E', or '0'.
"""


class Solution:
    def maxKilledEnemies(self, grid):
        """
        Runtime: 960 ms, faster than 5.04%

        Time : O(width * height * (width + height))
        Space : O(width)
        """
        def dfs(row, col, count=0, direction=None):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == '-':
                return count

            # if found enemy increment the count but do not return as more
            # enemies can be found in the same direction
            if grid[row][col] == 'E':
                count += 1

            if grid[row][col] == 'W':
                return count

            temp = grid[row][col]
            grid[row][col] = '-'

            # if direction is None and same direction, then continue
            if not direction or direction == 'r':
                count = dfs(row+1, col, count, direction='r')

            if not direction or direction == 'l':
                count = dfs(row-1, col, count, direction='l')

            if not direction or direction == 'd':
                count = dfs(row, col+1, count, direction='d')

            if not direction or direction == 't':
                count = dfs(row, col-1, count, direction='t')

            grid[row][col] = temp

            return count

        max_enemies = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '0':
                    max_enemies = max(max_enemies, dfs(row, col))

        return max_enemies
