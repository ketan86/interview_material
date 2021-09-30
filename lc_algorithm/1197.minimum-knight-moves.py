# 1197. Minimum Knight Moves
# Medium

# 802

# 265

# Add to List

# Share
# In an infinite chess board with coordinates from -infinity to +infinity,
# you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is
# two squares in a cardinal direction, then one square in an orthogonal direction.



# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:

# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return 1 + min(
                    dfs(abs(x - 1), abs(y - 2)), 
                    dfs(abs(x - 2), abs(y - 1)))

        return dfs(abs(x), abs(y))