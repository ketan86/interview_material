#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (46.71%)
# Likes:    1497
# Dislikes: 123
# Total Accepted:    142.5K
# Total Submissions: 284.2K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
#
# Example 1:
#
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
#
#
#
# Example 2:
#
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
#
#
#
# Follow up:
#
# Try to solve it in O(n log k) time and O(n) extra space.
#
#
#

# @lc code=start
# pylint: skip-file

from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, words, k):
        # max heap to store all max elements. here we could have used min_heap
        # with only k elements but that would not accommodate the case when
        # freq is same. when freq is same, we have to pop the last element
        # which is higher in alphabetical order. so we have to store all the
        # elements in the heap and since we need top k, we use max_heap
        max_heap = []

        # create a freq map
        freq_map = defaultdict(int)
        for word in words:
            freq_map[word] += 1

        # add all words into heap based on the freq in max_heap
        for word, freq in freq_map.items():
            heapq.heappush(max_heap, (-freq, word))

        # read top k elements and return the results.
        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result

    def WILL_NOT_WORK_topKFrequent(self, words, k):
        min_heap = []
        freq_map = defaultdict(int)
        for word in words:
            freq_map[word] += 1

        for word, freq in freq_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, word))
                print(min_heap)
            else:
                top_element_freq = min_heap[0][0]
                if freq > top_element_freq:
                    heapq.heapreplace(min_heap, (freq, word))
                elif freq == top_element_freq:
                    # NOTE: : : prob is here where same elements are stored
                    # in lower to higher in alphabetical order when
                    # freq is same so we end up poping word with
                    # lower in alphabetical order if we do heap replace top
                    # element. even if we push current word, pop first two
                    # words and push second word, the reverse of the final
                    # heap messes up the order.
                    heapq.heappush(min_heap, (freq, word))
                    first = heapq.heappop(min_heap)
                    second = heapq.heappop(min_heap)
                    heapq.heappush(min_heap, first)
        return [item[1] for item in reversed(min_heap)]


print(Solution().topKFrequent(
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
print(Solution().topKFrequent(
    ["i", "love", "leetcode", "i", "love", "coding"], k=2))
# @lc code=end
