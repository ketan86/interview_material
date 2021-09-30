# Design a data structure that will be initialized with a string array, and then
# it should answer queries of the shortest distance between two different
# strings from the array.

# Implement the WordDistance class:

# WordDistance(String[] wordsDict) initializes the object with the strings array
# wordsDict. int shortest(String word1, String word2) returns the shortest
# distance between word1 and word2 in the array wordsDict.

# Example 1:

# Input
# ["WordDistance", "shortest", "shortest"]
# [[["practice", "makes", "perfect", "coding", "makes"]],
#     ["coding", "practice"], ["makes", "coding"]]
# Output
# [null, 3, 1]

# Explanation
# WordDistance wordDistance = new WordDistance(
#           ["practice", "makes", "perfect", "coding", "makes"])
# wordDistance.shortest("coding", "practice")
# // return 3
# wordDistance.shortest("makes", "coding")
# // return 1


# Constraints:

# 1 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2
# At most 5000 calls will be made to shortest.

from collections import defaultdict


class WordDistance:

    def __init__(self, wordsDict):
        self.d = defaultdict(list)

        for i, w in enumerate(wordsDict):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:

        shortest_distance = float('inf')

        word1_indices = self.d[word1]
        word2_indices = self.d[word2]

        l1 = 0
        l2 = 0

        while l1 < len(word1_indices) and l2 < len(word2_indices):
            shortest_distance = min(shortest_distance, abs(
                word1_indices[l1] - word2_indices[l2]))
            # to find shorted distance, we need to move the one that is less
            # in index
            # [1,7,5], [3,4,6]
            #  ^        ^
            if word1_indices[l1] < word2_indices[l2]:
                l1 += 1
            else:
                l2 += 1

        return shortest_distance
