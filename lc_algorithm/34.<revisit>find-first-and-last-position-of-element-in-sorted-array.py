#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]


print(Solution().searchRange(
    [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 9, 9], 9))
# @lc code=end
