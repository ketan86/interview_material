#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (36.55%)
# Likes:    1876
# Dislikes: 3779
# Total Accepted:    526.6K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# [1,2,2,3,5,6]
#
#
# pylint: skip-file
# @lc code=start
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        # Runtime: 36 ms, faster than 76.03%

        Do not return anything, modify nums1 in-place instead.

        Time Complexity : O(m+n)
        Space Complexity : O(1)
        """

        # NOTE: m could be set to 0 if m does not contain any values (except 0)
        # so a condition like if "m==0: return" will fail some testcase.
        # [0], m=0 & [1], n=1

        # nums1 pointer that moves inwards from m
        p1 = m - 1
        # nums2 pointer that moves inwards from n
        p2 = n - 1
        # nums3 pointer that moves inwards starting from the last index.
        p3 = len(nums1) - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1

        # if there are any elements left in nums2 OR there are no elements in
        # nums1, move it in nums1 if len(nums2) > len(nums1)
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1

        return nums1

# print(Solution().merge([0],0,  [1], 1))
# @lc code=end
