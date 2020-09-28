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
                        self.searchOptimized(board, i, j, 0, word):
                    return True
        return False

    def searchTimeLimitExceed(self, board, i, j, count, word):
        # Time Limit Exceeded
        # 87/89 cases passed (N/A)
        # Testcase
        # [["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b"]]
        # ' +
        #   '"baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

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

        # NOTE: if word is found in either direction and if we still search
        # rest of the directions, it is not going to be efficient and will
        # exceed the time.

        # It can be optimized by checking if any of the direction finds word
        # and if, returns right away.

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

    def searchOptimized(self, board, i, j, count, word):
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

        # NOTE: if word is found in either direction and if we still search
        # rest of the directions, it is not going to be efficient and will
        # exceed the time.

        # It can be optimized by checking if any of the direction finds word
        # and if, returns right away.

        # traverse all directions
        if self.searchOptimized(board, i + 1, j, count + 1, word) or \
                self.searchOptimized(board, i - 1, j, count + 1, word) or \
                self.searchOptimized(board, i, j + 1, count + 1, word) or \
                self.searchOptimized(board, i, j - 1, count + 1, word):
            return True

        # restore the node value
        board[i][j] = temp

        # if word is not found in all direction, return False
        return False


class Solution1:
    def exist(self, board, word):

        # iterate over board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # dfs to traverse in all direction and building the word
                # if word is found, return right away instead of searching
                # further.
                if self.search(board, i, j, '', word):
                    return True
        return False

    def search(self, board, i, j, substring, word):
        # if i or j out of bound or current word is already visited, return
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] == '-':
            return

        #
        substring += board[i][j]

        if substring == word:
            return True

        if not word.startswith(substring):
            return False

        # do not search visited nodes
        temp = board[i][j]
        board[i][j] = '-'

        # NOTE: THIS IS IMPORTANT.
        # traverse all directions and if word is found in first, return and
        # do not continue search in all direction.
        if self.search(board, i + 1, j, substring, word) or \
                self.search(board, i - 1, j, substring, word) or \
                self.search(board, i, j + 1, substring, word) or \
                self.search(board, i, j - 1, substring, word):
            return True

        # restore the node value
        board[i][j] = temp

        # if word is not found in all directions, return False
        return False


if __name__ == '__main__':
    s = Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']], 'ABCC')
    print(s)

# @lc code=end
