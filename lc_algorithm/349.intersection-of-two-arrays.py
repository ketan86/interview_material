#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (56.14%)
# Likes:    690
# Dislikes: 1111
# Total Accepted:    327.2K
# Total Submissions: 541.1K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
#
#
# Note:
#
#
# Each element in the result must be unique.
# The result can be in any order.
#
#
#
#
#

# @lc code=start
class Solution:
    def intersection(self, nums1, nums2):
        "Runtime: 36 ms, faster than 97.50%"
        # first n^2 solution would be to loop over both arrays and find the
        # common elements and save it to a list.
        # result = set()
        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             result.add(i)
        # return list(result)

        # we could improve the time complexity by adding adding one array to
        # set.
        nums1 = set(nums1)
        result = []
        for i in nums2:
            if i in nums1:
                result.append(i)
                nums1.remove(i)
        return result

# @lc code=end
