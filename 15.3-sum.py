# @lc app=leetcode id=23 lang=python3

# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]
# @lc code=start

# pylint:skip-file

# O(N^2) -> Time Complexity
class Solution:
    def threeSum(self, nums):
        """
        Key of this problem is **sorting** and skipping **duplicate** elements.
        """
        results = []
        if not nums:
            return results
        nums.sort()

        # go till 3rd last element
        for i in range(len(nums) - 2):
            # if i value is greater than 0, sum will never be 0.
            # for ex, [1,3,4,8..]
            if nums[i] > 0:
                break

            # if we find the current element same as prev, skip it to eliminate
            # duplicates.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointers to find the diff
            x = j = i + 1
            y = k = len(nums) - 1

            # only till j < k and NOT j <=k because we need two elements
            while j < k:
                # if prev value of the j or k is same, skip j or k.
                # NOTE: j > x and y < k (next condition) is to prevent
                # j from matching the i and k from going out of
                # bound in the first iteration.
                if j > x and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                if y > k and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                # sum of all the elements
                sum_ = nums[i] + nums[j] + nums[k]
                # if sum is 0, record the results and increment j and k
                if sum_ == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                # if sum is less than the target(0), increment j to reach
                # close to target. else decrement k
                elif sum_ < 0:
                    j += 1
                else:
                    k -= 1

        return results


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([-2, 0, 0, 2, 2]))
print(Solution().threeSum([0, 0, 0]))
# @lc code=end
