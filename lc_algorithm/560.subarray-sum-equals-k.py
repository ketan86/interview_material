#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.77%)
# Likes:    4100
# Dislikes: 130
# Total Accepted:    279.8K
# Total Submissions: 639.6K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
#
# Constraints:
#
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
#
#
#

# @lc code=start
# pylint: skip-file
from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        """
        Hash map <running_sum:freq> to store the running sum at each index.
        if running_sum - k is found in map, the sum of the all elements
        from (map's running_sum -> index + 1) to current index is k:

        running_sum - k -> running_sum = k

        nums-> [0, 9, 1,  8,  6,  3], k=9
        sum -> [0, 9, 10, 18, 24, 27] <--- when running_sum == k, for (9) add that to count.

        d = {running_sum:freq}
                ^
                0-9 in d -> no ;d = {0 -> 1}
                   ^
                   9-9=0 in d -> yes, count += d[0] ; d {0 -> 1, 9 -> 1}
                      ^
                      10-9=1 in d -> no ; d  {0 -> 1, 9 -> 1, 10 -> 1}
                           ^
                           18-9=9 in d -> yes count +=d[9] ; d {0 -> 1, 9 -> 1, 10 -> 1, 18 -> 1}
                           ...

        """
        d = defaultdict(int)

        running_sum = 0
        count = 0

        # loop over the array and keep calculating the running sum
        for i in range(len(nums)):
            running_sum += nums[i]

            # if running sum == k, increment the count
            if running_sum == k:
                count += 1

            # if running_sum - k in dict, increment count by total instances
            # running_sum
            # for ex, [-2,-1,1,3,-3], k=0 -> running sum [-2,-3,-2,1,-2]
            # [-1,1], [-1,1,3,-3], [3,-3] = total 3 instances
            # count when index at 2, is 1
            # count when index at 4, is (1(prev)+2) = 3
            # [-2,-3,-2,1,-2] -> after sum was -3, it became -2 at index 2 for
            #                    subarray [-1,1]
            #                 -> after sum was -3, it became -2 at index 4 for
            #                    subarray [-1,1,3,-3]
            #                 -> after sum was 1, it became -2
            #                    subarray [3,-3]
            if (running_sum - k) in d:
                count += d[running_sum - k]
            # increment runing sum value by 1 to represent the total instances
            # where running_sum was 0.
            d[running_sum] += 1
            print(d)

        return count

    def subarraySumN2(self, nums, k):
        """
        O(n^2) solution.
        """
        count = 0
        if not nums:
            return count

        # use two pointers and calculate the running sum
        for i in range(len(nums)):
            running_sum = 0
            # start j from ith index
            for j in range(i, len(nums)):
                running_sum += nums[j]
                # at any give point, running sum is equal to k, count the
                # occurrence.
                if k == running_sum:
                    count += 1

        return count

    def onlyPositiveSubarraySum(
            self, nums, k):
        """
        O(n) solution. Since we have to find the sum of the contiguous
        elements, we can use sliding window pattern. when sum is greater
        than k, shrink to windows from start and if less than, expand from
        the end. this logic only works for all positive numbers.

        PROBLEM: Sliding window does not work for this problem because:
            Skipped part of the window may also contribute to a maxSize
            subarray. Move right does not make the sum bigger, move left
            does not make the sum smaller. because number can be
            *** positive or negative ***

            Silding window need a fixed constrain like k elements of the
            array instead of k sum where sum may not becomes greater or
            lesser. for ex, [-2,-1,1,1] k = 0
                             ^       ^ -> sum is still -1 which is less than
                             i       j    k. j has already reached end and
                                          even after moving i towards j, we
                                          will miss (-1,1) subarray.
        """

        # only for arrays with positive integers
        count = 0
        i = 0
        j = 0
        running_sum = 0
        # only check till j reaches end. since we are only keeping <= k
        # elements in the window, when j reaches end, i will be at position
        # where i..j sum will be less than k.
        while j < len(nums):
            # no need to check for a special case where i and j are same,
            # using j for adding sum takes care of that.
            running_sum += nums[j]
            # until sum is >= k and i is <= j, keep shirking window from
            # start.
            while running_sum >= k and i <= j:
                # at given point, running sum == k, found the instance.
                if running_sum == k:
                    count += 1
                # remove ith element from the running sum and increment i
                running_sum -= nums[i]
                i += 1
            # increment j
            j += 1
        return count


print(Solution().subarraySum([0, 9, 1, 8, 6, 3], 9))
# print(Solution().subarraySumN2([-2, -1, 1, 3, -3], 0))
# print(Solution().subarraySum([-2, -1, 1, 3, -3], 0))
# print(Solution().subarraySum([5, 4, 2, 1, 4, 5, 4, 4, 1], 9))
# @lc code=end
