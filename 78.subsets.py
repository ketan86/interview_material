#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.47%)
# Likes:    2226
# Dislikes: 54
# Total Accepted:    401.4K
# Total Submissions: 736.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start

class Solution:
    # def subsets(self, nums):
    #     s_time = time.time()
    #     result = []
    #     self.find(nums, [], 0, result)
    #     print('took', time.time() - s_time)

    # def find(self, nums, temp, index, result):
    #     if index == len(nums):
    #         result.append(temp)
    #         return temp

    #     self.find(nums, list(temp), index + 1, result)
    #     temp.append(nums[index])
    #     self.find(nums, list(temp), index + 1, result)

    #     return result

    def subsets(self, nums):
        """Runtime: 32 ms, faster than 82.45%"""
        result = [[]]
        # loop over the nums list
        for i in range(len(nums)):
            # copy the last index  of the result list.
            # NOTE: this can not be done in the range function as result
            # length would change at run time.
            j = len(result)
            # loop over prev results from 0 to last element and append
            # current element to each sublist to find next the permutation.
            for k in range(j):
                # create a new list from the result
                new_list = list(result[k])
                # append current element.
                new_list.append(nums[i])

                # NOTE: Above two steps have to be done outside since list
                # is updated in place.

                # push new list to result list as a next permutation.
                result.append(new_list)

        return result

    def subsetsRecursive(self, nums):
        """Runtime: 28 ms, faster than 94.36%"""
        # start with empty set
        result = [[]]
        self.find(nums, 0, result)
        return result

    def find(self, nums, index, result):
        # if index == length, return result list
        if index == len(nums):
            return

        # use temp result to find subset of new number with existing results.
        temp_result = []
        # iterate over the results subset
        for subset in result:
            # create a copy of the subset list
            new_subset = list(subset)
            # add current value to the subset
            new_subset.append(nums[index])
            # save it to temp result
            temp_result.append(new_subset)

        # extend results
        result.extend(temp_result)

        # recursive call for next index
        self.find(nums, index + 1, result)


print(Solution().subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                          13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

# @lc code=end
