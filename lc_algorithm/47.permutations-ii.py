#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        """Runtime: 72 ms, faster than 42.35%"""
        results = []
        freq_map = Counter(nums)

        def backtrack(comb, freq_map):
            """
            [1, 1, 2]
            Counter({1: 2, 2: 1}) []
            Counter({1: 1, 2: 1}) [1]
            Counter({2: 1, 1: 0}) [1, 1]
            Counter({1: 0, 2: 0}) [1, 1, 2]
            Counter({1: 1, 2: 0}) [1, 2]
            Counter({1: 0, 2: 0}) [1, 2, 1]
            Counter({1: 2, 2: 0}) [2]
            Counter({1: 1, 2: 0}) [2, 1]
            Counter({1: 0, 2: 0}) [2, 1, 1]
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

            """
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(comb[:])
            else:
                for num in freq_map:
                    if freq_map[num] > 0:
                        # add this number into the current combination
                        comb.append(num)
                        freq_map[num] -= 1
                        # continue the exploration
                        backtrack(comb, freq_map)
                        # revert the choice for the next exploration
                        comb.pop()
                        freq_map[num] += 1

        backtrack([], freq_map)

        return results


print(Solution().permuteUnique([1, 1, 2]))
# @lc code=end
