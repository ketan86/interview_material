#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (41.59%)
# Likes:    1951
# Dislikes: 4197
# Total Accepted:    774.8K
# Total Submissions: 1.8M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Example 1:
#
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
#
# Example 2:
#
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.
#
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#

# @lc code=start
# pylint: skip-file


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # prev pointer
        i = 0
        # running pointer
        j = 1

        # use two pointers and if forward pointers find a number that is not
        # equal to current pointer value (unique), increment the ith index
        # and swap the number with j index.
        while j < len(nums):
            if nums[i] != nums[j]:
                # increment first because till ith index, elements
                # are unique already.
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1

        return i + 1


print(Solution().removeDuplicates([1, 1, 2]))
# @lc code=end
