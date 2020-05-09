#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (60.27%)
# Likes:    1339
# Dislikes: 1913
# Total Accepted:    141K
# Total Submissions: 224.7K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
#
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2.
#
#
#
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
#
#
# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
# ⁠   For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
# ⁠   For number 1 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
#
#
#
# Example 2:
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
# ⁠   For number 2 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
#
#
#
#
# Note:
#
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
#
#
#

# @lc code=start
# pylint: skip-file


class Solution:
    def nextGreaterElement(self, nums1, nums2):

        # store all nums1 to dict with value -1
        d = {}
        for num in nums1:
            d[num] = -1

        # stack to store elements until next greater element is found,
        # for ex, 1,3,2,4
        # 1 goes to stack, 3 is greater than 1 so pop 1 and if it is in dict,
        # current value is a next greater element. pop another element and
        # keep checking.
        # add 3 to the stack.
        # stack is not empty so add 2 to it. 2 is not greater than 3 so we
        # continue,
        # we get 4, 4 is greater than 2 so pop 2 and mark 4 is greatest for 2.
        # 4 is greater than 3 too, so pop and if it is dict, mark 4
        # a next greater element of 3.
        stack = []

        for num in nums2:
            # if stack is empty, add num
            if not stack:
                stack.append(num)
            else:
                # else pop all values until current number is less than the
                # top element of the stack.

                # all poped values will have current element the next greater
                # element.
                while stack:
                    if num > stack[-1]:
                        top = stack.pop()
                        # since we are only interested in nums in nums1,
                        # check if top element is part of the dict
                        if top in d:
                            d[top] = num
                    # if top element is <= current element, break
                    else:
                        break

                # add current element to stack
                stack.append(num)

        return list(d.values())


# print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
# print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
# @lc code=end
