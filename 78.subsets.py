#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.47%)
# Likes:    2226
# Dislikes: 54
# Total Accepted:    401.4K
# Total Submissions: 736.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start


class Solution:
    def subsets(self, nums):
        result = []
        return self.find(nums, [], 0, result)

    def find(self, nums, temp, index, result):
        if index == len(nums):
            result.append(temp)
            return temp

        self.find(nums, list(temp), index + 1, result)
        temp.append(nums[index])
        self.find(nums, list(temp), index + 1, result)

        return result


# print(Solution().subsets([1, 2, 3, 4, 5, 6, 7]))

# @lc code=end
