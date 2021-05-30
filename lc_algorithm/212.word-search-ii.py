#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (32.82%)
# Likes:    2880
# Dislikes: 124
# Total Accepted:    234.4K
# Total Submissions: 666.1K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
'["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
#
#
# Example:
#
#
# Input:
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
#
#
# Note:
#
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
#
#
#

# @lc code=start


class TrieNode:
    def __init__(self, char, end_word=False):
        self.char = char
        self.end_word = end_word
        self.child = [None] * 26


class SolutionTimeLimitExceed:
    """
    # because even if word is not present in the dict, we iterate over the
    # board to find all possible substrings.
    """

    def findWords(self, board, words):
        word_dict = set(words)
        result = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.dfs(board, row, col, '', word_dict, result)
        return result

    def dfs(self, board, row, col, sub_string, word_dict, result):

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]) or board[row][col] == '-':
            return

        sub_string += board[row][col]

        # because even if word is not present in the dict, we iterate over the
        # board to find all possible substrings.
        if sub_string not in result and sub_string in word_dict:
            result.append(sub_string)

        temp = board[row][col]
        board[row][col] = '-'

        self.dfs(board, row + 1, col, sub_string, word_dict, result)
        self.dfs(board, row - 1, col, sub_string, word_dict, result)
        self.dfs(board, row, col + 1, sub_string, word_dict, result)
        self.dfs(board, row, col - 1, sub_string, word_dict, result)

        board[row][col] = temp


class Solution:
    """Runtime: 9536 ms, faster than 5.02%"""

    def __init__(self):
        # trie data structure to make search efficient.
        self.trie = TrieNode(None)

    def getIndex(self, char):
        return ord(char) - ord('a')

    def insertWord(self, word):
        # insert words into the trie
        levels = len(word)
        curr = self.trie
        for i in range(levels):
            index = self.getIndex(word[i])
            if not curr.child[index]:
                curr.child[index] = TrieNode(word[i])
            curr = curr.child[index]
        curr.end_word = True

    def findWords(self, board, words):
        # result list to store the words found in board that
        # matches the word from the dict.
        result = []

        # insert words into trie
        for word in words:
            self.insertWord(word)

        # iterate over the board 1 index at a time.
        for i in range(len(board)):
            for j in range(len(board[i])):
                # traverse all direction
                self.traverse(
                    board, i, j, substring='', result=result, trie=self.trie)
        # return result
        return result

    def traverse(self, board, i, j, substring, result, trie):
        """Traverse the board starting from the ith and jth position.

        ⁠ ['o','a','a','n'],
        ⁠ ['e','t','a','e'],
        ⁠ ['i','h','k','r'],
        ⁠ ['i','f','l','v']

        substring starts from empty '' string and builds during traversal.
        for ex, if i and j are at the position where 'k' is,
            substring will be 'k' and for each direction, it will become
                - 'kh'
                - 'kr'
                - 'ka'
                - 'kl'

        while traversing, update the trie pointer and if trie node is none,
        for the given char, the word forming beyond that substring wont be
        present in the trie so return. if trie node is there, check if it's
        a end_word and if yes, add current substring to a result.
        """

        # if out of bound or board[i][j] is equal to '-', return
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) \
                or board[i][j] == '-':
            return

        # add new char to a substring
        substring += board[i][j]

        # advance the trie node
        trie = trie.child[self.getIndex(board[i][j])]

        # if trie node is none, substring is not present so no need to traverse.
        if not trie:
            return

        # if trie node is not none and if word is complete, add it to result.
        if trie.end_word:
            result.append(substring)
            # we can un-mark that word to avoid duplicates in results.
            # NOTE: if aleration to trie is not accepted, check if substring
            # is present in the result before adding.
            trie.end_word = False

        # save the curr char to temp
        curr_char = board[i][j]
        # mark the curr char to '-' or any other char than a-z to avoid
        # infinite traversal
        board[i][j] = '-'

        # traverse in all direction
        self.traverse(board, i - 1, j, substring, result, trie)
        self.traverse(board, i + 1, j, substring, result, trie)
        self.traverse(board, i, j - 1, substring, result, trie)
        self.traverse(board, i, j + 1, substring, result, trie)

        # reset the char
        board[i][j] = curr_char


print(Solution().findWords(
    [["o", "a", "a", "n"], ["e", "t", "a", "e"], [
        "i", "h", "k", "r"], ["i", "f", "l", "v"]],
    ["oath", "pea", "eat", "rain"]
))
# @lc code=end
