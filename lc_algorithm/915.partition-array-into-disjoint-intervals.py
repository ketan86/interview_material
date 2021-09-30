#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums) -> int:

        # create min right array
        min_from_right = [None] * len(nums)
        min_value = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            min_value = min(min_value, nums[i])
            min_from_right[i] = min_value

        # max from left
        max_from_left = -1
        for i in range(len(nums)):
            max_from_left = max(max_from_left, nums[i])
            if max_from_left <= min_from_right[i+1]:
                return i + 1


# @lc code=end
