#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord
# -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need
# to be in wordList.

# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return
# the number of words in the shortest transformation sequence from beginWord
# to endWord, or 0 if no such sequence exists.


# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


# @lc code=start
from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """Runtime: 492 ms, faster than 34.95%

        Time : O(M * N^2) where M is total words and N is length of the word

        Space : O(M * N) where M = number of words

                        hit
                         |
                        hot
                        /  \
                    dot    lot
                     |      |
                    dog    log
                     |
                    cog
        """

        # create set for quick search
        word_set = set(wordList)

        # initialize queue and put begin word
        queue = deque()
        queue.append((beginWord, 1))

        # if begin word is there in the word set, remove it
        if beginWord in word_set:
            word_set.remove(beginWord)

        while queue:
            levels = len(queue)
            for _ in range(levels):
                # get word from the queue and if it's end word,
                # search is complete
                word, level = queue.popleft()
                if word == endWord:
                    return level
                # generate all possible strings
                neighbors = self.find_neighbors(word, word_set)
                # iterate over each neighbors
                for n in neighbors:
                    # if neighbor is in word set, remove it and
                    # process it by adding it in the queue.
                    word_set.remove(n)
                    queue.append((n, level+1))
        # if no path found yet, return 0
        return 0

    def find_neighbors(self, word, word_set):
        # generate all neighbors of the current word by replacing each char
        # by a..z letters. only add neighbors that are in word set.
        result = []
        for index in range(len(word)):
            for letter in string.ascii_lowercase:
                new_word = word[:index] + letter + word[index+1:]
                if new_word in word_set:
                    result.append(new_word)
        return result


print(Solution().ladderLength('hit', 'cog', [
      "hot", "dot", "dog", "lot", "log", "cog"]))


print(Solution().ladderLength('hit', 'cog', [
      "hot", "dot", "dog", "lot", "log"]))


# @lc code=end
