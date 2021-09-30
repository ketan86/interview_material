#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        # make freq map
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1

        # unique set to store the unique frequencies
        unique = set()
        # store the minimum deletion
        minimum_deletion = 0

        for char, freq in freq_map.items():
            # if freq is unique, add it to set
            # else, reduce the current char feq and
            # count the deletion
            while freq > 0 and freq in unique:
                freq -= 1
                minimum_deletion += 1
            unique.add(freq)

        return minimum_deletion
# @lc code=end
