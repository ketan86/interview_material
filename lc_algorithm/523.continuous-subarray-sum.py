#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
"""
523. Continuous Subarray Sum
Medium

490

89

Add to List

Share
Given an integer array nums and an integer k, return true if nums has a
continuous subarray of size at least two whose elements sum up to a multiple
of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that
x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 


"""

# @lc code=start


class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        """
        Runtime: 876 ms, faster than 86.21%
        """

        # store remainder in set
        prefix_sum = set()
        # track current sum and prev_remainder
        curr_sum = prev_remainder = 0
        for num in nums:
            curr_sum += num
            curr_remainder = curr_sum % k
            print(curr_sum, curr_remainder, prefix_sum)
            if curr_remainder in prefix_sum:
                return True
            prefix_sum.add(prev_remainder)
            prev_remainder = curr_remainder
        return False


print(Solution().checkSubarraySum([23, 2, 4, 6, 7], k=6))
# @lc code=end
