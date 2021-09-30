#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
"""
36. Valid Sudoku Medium

2695

571

Add to List

Share Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
be validated according to the following rules:

Each row must contain the digits 1-9 without repetition. Each column must
contain the digits 1-9 without repetition. Each of the nine 3 x 3 sub-boxes of
the grid must contain the digits 1-9 without repetition. Note:

A Sudoku board (partially filled) could be valid but is not necessarily
solvable. Only the filled cells need to be validated according to the mentioned
rules.

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
Accepted
490,544
Submissions
955,184
"""
# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_set = set()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != '.':

                    # formula to find the sub-sudoku
                    box = (row // 3) * 3 + (col // 3)

                    row_string = f'row+{row}+{board[row][col]}'
                    col_string = f'col+{col}+{board[row][col]}'
                    box_string = f'box+{box}+{board[row][col]}'

                    if row_string in seen_set or col_string in seen_set or box_string in seen_set:
                        return False

                    else:
                        seen_set.add(row_string)
                        seen_set.add(col_string)
                        seen_set.add(box_string)
        return True


# @lc code=end
