#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (52.17%)
# Likes:    2028
# Dislikes: 190
# Total Accepted:    372.2K
# Total Submissions: 663.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        Height balanced binary search tree will have root node as middle
        element of the sorted array. once we find the root, left and right
        child can be found by doing the same operation on the left half
        of the sorted array and right half of the sorted array.
        """
        start = 0
        end = len(nums) - 1

        def create_bst(nums, start, end):
            if start > end:
                return

            # find the mid of the array and that become the root node.
            mid = int(start + ((end - start) / 2))

            # root node with mid value
            root = TreeNode(nums[mid])

            # now to find left, do recursive call in left half of the array.
            # this will become none, when start is greater than end.
            root.left = create_bst(nums, start, mid - 1)
            # now to find right, do recursive call in right half of the array.
            root.right = create_bst(nums, mid + 1, end)

            return root

        return create_bst(nums, start, end)


# print(Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# @lc code=end
