#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (32.08%)
# Likes:    2562
# Dislikes: 134
# Total Accepted:    368.9K
# Total Submissions: 1.1M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#

# @lc code=start


class Solution:

    def exist(self, board, word):
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] == word[0] and \
                        self.search(board, i, j, 0, word):
                    return True
        return False

    def search(self, board, i, j, count, word):
        # if all letters are visited
        if count == len(word):
            return True

        # if out of bound
        if i < 0 or j < 0 or i >= len(board) or \
                j >= len(board[i]):
            return False

        # if letter is not found
        if board[i][j] != word[count]:
            return False

        # do not search visited nodes
        temp = board[i][j]
        board[i][j] = ''

        # traverse all directions
        bottom = self.search(board, i + 1, j, count + 1, word)
        top = self.search(board, i - 1, j, count + 1, word)
        right = self.search(board, i, j + 1, count + 1, word)
        left = self.search(board, i, j - 1, count + 1, word)

        # print(left, right, top, bottom)

        # restore the node value
        board[i][j] = temp

        # if either direction found the letter, return True
        return right or left or bottom or top


if __name__ == '__main__':
    s = Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']], 'ABCC')
    print(s)

# @lc code=end
