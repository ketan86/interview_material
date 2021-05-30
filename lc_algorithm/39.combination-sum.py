#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (50.16%)
# Likes:    3223
# Dislikes: 102
# Total Accepted:    490.4K
# Total Submissions: 907K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates, target):
        """
        In order to find combinations with repeated number, start with the list and extract all elements and find combination with
        all the elements starting from that element to n.

        When a sum of all elements is greater than target, break.
        When a sum of all the elements is equal to target, save it.
                                                                                        [2,3,5]
                                                /                                                                    \          \
                                            2 & [2,3,5],                                                            3 & [3,5], 5 &[5]
            /                                    |                                 \
    2,2 & [2,3,5],                          2,3 & [3,5],                        2,5 & [5]
    /               \           \                 /         \                       |
2,2,2 & [2,3,5], 2,2,3 & [3,5], 2,2,5 & [5]  2,3,3 & [3,5], 2,3,5 & [5]         2,5,5 & [5]
                                ...

        """
        # save the results
        results = []
        self.find_combinations(candidates, target, results)
        return results

    def find_combinations(self, candidates, target, results, index=0, combinations=None, sum_=0):
        if combinations is None:
            combinations = []
        # if sum is greater than target, return
        if sum_ > target:
            return
        # if sum is equal to target, append combinations
        if sum_ == target:
            results.append(combinations)
            return

        # loop from index till end to cover all the combinations including the current element due to
        # repeatability.
        for i in range(index, len(candidates)):
            # calculate new combinations. Note: combinations.append(candidate[i]) would change
            # the combinations value for the next iteration so add new list with candidate i.
            new_combinations = combinations + [candidates[i]]
            new_sum = sum_ + candidates[i]
            self.find_combinations(
                candidates, target, results, i, new_combinations, new_sum)


print(Solution().combinationSum([2, 3, 6, 7], 7))
# @lc code=end
