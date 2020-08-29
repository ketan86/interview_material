#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.04%)
# Likes:    2987
# Dislikes: 1058
# Total Accepted:    344.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#

# @lc code=start
# pylint: skip-file


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        STEPS:

        1. go from right to left and stop at the element where
        current element is less than the next element
        2. sort all element next to the right of the current element
        3. swap current element with first bigger element in the sorted
        array.
        """
        if len(nums) == 1:
            return nums

        # if length is 2, swap elements and return the numbers,
        # if numbers are
        if len(nums) == 2:
            self.swap(nums, 0, 1)
            return nums

        end = len(nums) - 2
        # move end till current element is >= the next element.
        while end >= 0 and nums[end] >= nums[end + 1]:
            end -= 1

        # reverse all the numbers starting from next of the current element.
        self.reverse(nums, end + 1, len(nums) - 1)

        # if we did not find the element where current element is less than
        # the next element, there is no greater permutation so
        # we could return the reversed list.
        if end == -1:
            return nums

        # traverse until current element is greater than next element
        # and next element is not crossing the array limit
        next_ = end + 1
        while next_ <= len(nums) - 1 and nums[end] >= nums[next_]:
            next_ += 1

        # swap the current element with next greater element.
        self.swap(nums, end, next_)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self, nums, start, end):
        nums[end], nums[start] = nums[start], nums[end]


# print(Solution().nextPermutation([5, 1, 1]))
# @lc code=end
