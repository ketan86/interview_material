# Given an array of strings wordsDict and two different strings that already
# exist in the array word1 and word2, return the shortest distance between these
# two words in the list.

# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
#   word1 = "coding", word2 = "practice"
# Output: 3


# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
#   word1 = "makes", word2 = "coding"
# Output: 1

# Constraints:

# 1 <= wordsDict.length <= 3 * 104 1 <= wordsDict[i].length <= 10 wordsDict[i]
# consists of lowercase English letters. word1 and word2 are in wordsDict. word1
# != word2 Accepted 132, 601 Submissions 212, 327

from collections import defaultdict


class Solution:

    def shortestDistance(self, wordsDict, word1, word2):
        """
        Runtime: 64 ms, faster than 71.41%

        Time  -> O(n)
        Space -> O(1)
        """
        # set shorted distance to len of the word dict
        shortest_distance = len(wordsDict)
        # tuple to track prev word and it's index
        prev_word_index = ('', -1)
        for index, word in enumerate(wordsDict):
            # if word if one of the word1 and word2
            if word in (word1, word2):
                # if word1/word2 was found and new word is word2/word1
                if prev_word[0] and word != prev_word[0]:
                    # record the distance
                    shortest_distance = min(
                        shortest_distance, index - prev_word[1])
                # if same word1/word2 is found, discard the previous instance
                # and use latest word1/word2 instance.
                prev_word = (word, index)
        return shortest_distance

    def shortestDistance(self, wordsDict, word1, word2):
        """
        Runtime: 68 ms, faster than 44.20%

        Time  -> O(n)
        Space -> O(n)
        """
        shortest_distance = float('inf')
        if not wordsDict:
            return shortest_distance

        d = defaultdict(list)
        for index, word in enumerate(wordsDict):
            d[word].append(index)

        for index, word in enumerate(wordsDict):
            if word == word1:
                for i in d[word2]:
                    if index < i:
                        shortest_distance = min(i - index, shortest_distance)
            if word == word2:
                for i in d[word1]:
                    if index < i:
                        shortest_distance = min(i - index, shortest_distance)
        return shortest_distance
