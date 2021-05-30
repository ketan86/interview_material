#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#

# @lc code=start
class Solution:
    def cherryPickup(self, grid):
        f_cherry = self.forward_trip(
            grid, 0, 0)

        b_cherry = self.backword_trip(
                grid, len(grid)-1, len(grid[0])-1)

        return f_cherry + b_cherry
        
    def forward_trip(self, grid, row, col, max_cherry=0):
        if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == -1:
            return max_cherry

        if grid[row][col] == 1:
            grid[row][col] = 0
            max_cherry += 1

        max_cherry += max(
            self.forward_trip(grid, row, col+1),
            self.forward_trip(grid, row+1, col)
        )

        return max_cherry


    def backword_trip(self, grid, row, col, max_cherry=0):
        if row < 0 or col < 0 or grid[row][col] == -1:
            return max_cherry

        if grid[row][col] == 1:
            grid[row][col] = 0
            max_cherry += 1

        max_cherry += max(
            self.forward_trip(grid, row, col-1), 
            self.forward_trip(grid, row-1, col)
        )

        return max_cherry

print(Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))
# @lc code=end




            #         s

            #    1 r       1 d
                         
            #      d     r     1 d
 
            #   1  d    1 d     1 r

            #   1  r    1 r     1 r 