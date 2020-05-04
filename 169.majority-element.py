#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (53.73%)
# Likes:    2732
# Dislikes: 210
# Total Accepted:    543.8K
# Total Submissions: 962.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start

# Bit manipulation : https://leetcode.com/problems/majority-element/discuss/51780/Moore-Voting-Sorting-and-Bit-Counting-solutions-in-C%2B%2B


class Solution:
    def majorityElement(self, nums):
        # since there is a guaranty that the majority element exists, we can
        # use hash map to store the freq of the element while iterating,
        # if any time freq of the number becomes greater than n/2, return
        # the element.
        freq_map = {}
        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1
                if freq_map[i] > len(nums) / 2:
                    return i

    def majorityElement(self, nums):
        # sort the array and return the mid element
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement(self, nums):
        # moore voting algorithm. the key here is, if you sum(majority
        # elements) - sum(no_majority elements) > 0, there is a majority
        # element.

        # make first element a majority element and set count to 1
        majority_element = nums[0]
        count = 1

        # iterate from 1 to n elements.
        for i in range(1, len(nums)):
            # if current element is not same as majority element and count
            # is 0, majority element can be the current element, else
            # reduce the count.
            if majority_element != nums[i]:
                if count == 0:
                    majority_element = nums[i]
                else:
                    count -= 1
            # else, majority element is same, increase the count
            else:
                count += 1
        # at last, we will have the majority element.
        return majority_element


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2, 1, 1]))
# @lc code=end
