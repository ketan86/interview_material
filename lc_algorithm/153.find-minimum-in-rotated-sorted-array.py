#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.43%)
# Likes:    1658
# Dislikes: 214
# Total Accepted:    385.7K
# Total Submissions: 871.3K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#

# @lc code=start


class Solution:
    def findMin(self, nums):
        """
        Runtime: 40 ms, faster than 69.30% 
        """
        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:
            # to find mid between 2 to 6, we find the difference (6-2) = 4 so
            # if we add 4/2 to 2 = (2+2) = 4, we found the middle without
            # the overflow.
            mid = start_index + ((end_index - start_index) // 2)
            if nums[mid] > nums[len(nums) - 1]:
                start_index = mid + 1
            else:
                end_index = mid - 1

        return nums[end_index + 1]

# @lc code=end
