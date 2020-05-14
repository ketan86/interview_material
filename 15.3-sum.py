# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

# pylint:skip-file


class Solution:
    def threeSum(self, nums):
        """
        Key of this problem is **sorting** and skipping **duplicate** elements.
        """
        results = []
        if not nums:
            return results
        nums.sort()
        n = len(nums) - 2
        # go till 3rd last element
        for i in range(n):
            # if we find the current element same as prev, skip it to eliminate
            # duplicates.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointers to find the diff
            m = i + 1
            n = len(nums) - 1
            # find the target sum in array from i+1, n
            target = 0 - nums[i]

            # only till m < n and NOT m <=n beacuse we need two elements
            while m < n:
                # sum of the two elements
                sum_ = nums[m] + nums[n]
                # if sum is less than target or m value is same as prev,
                # increment m
                if sum_ < target or (m > i + 1 and nums[m] == nums[m - 1]):
                    m += 1
                # if sum is greater than target or m value is same as prev,
                # decrement n
                elif sum_ > target or (
                        n < len(nums) - 1 and nums[n] == nums[n + 1]):
                    n -= 1
                # if sum is euqal to target, record the results and increament
                # m and decrement n.
                else:
                    results.append([nums[i], nums[m], nums[n]])
                    m += 1
                    n -= 1

        # return results.
        return results


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([-2, 0, 0, 2, 2]))
print(Solution().threeSum([0, 0, 0]))
