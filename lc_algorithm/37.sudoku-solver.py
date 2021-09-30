#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        return board

    def solve(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    # fill board with 1 to 9 numbers
                    for num in range(1, len(board) + 1):
                        if self.sub_sudoku_valid(row, col, str(num), board):
                            board[row][col] = str(num)
                            if self.solve(board):
                                return True
                            board[row][col] = '.'
                    return False
        return True

    def sub_sudoku_valid(self, row, col, num, board):
        for i in range(len(board)):
            if board[i][col] == num:
                return False
            if board[row][i] == num:
                return False
            if board[3*(row//3)+i//3][3*(col//3) + i % 3] == num:
                return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().solveSudoku(board))
# @lc code=end
