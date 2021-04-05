#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (26.13%)
# Likes:    3365
# Dislikes: 476
# Total Accepted:    627.2K
# Total Submissions: 2.3M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# pylint:skip-file


class Solution:

    def isValidBST1(self, root):
        return self.traverse(root)

    def traverse(self, node, lower=float(-inf), upper=float(inf)):
        # if either left node is not None or right node is not None,
        # we are done travesing and did not find invalid node.
        # return True
        if node is None:
            return True
        # if current node value less than the lower or >= upper
        if node.val <= lower or node.val >= upper:
            return False

        # if while traversing left node, send the current node value as highest
        # you could expect (node.val <= upper). lower can be -inf. node can not be
        # less than -inf so (node.val <= lower) will never going to pass.
        if not self.traverse(node.left, lower, node.val):
            return False

        # if while traversing right node, send the current node value as lowest
        # you could expect (node.val >= lower).. higher can be +inf. node can be higher than
        # +inf so (node.val >= upper) will never going to pass.

        if not self.traverse(node.right, node.val, upper):
            return False

        # return True of all above conditions are met.
        return True

    prev = None

    def isValidBST(self, root):
        """
        # Runtime: 32 ms, faster than 99.44%

        In this approach, we do in-order traversal and during the traversal,
        if we find a node that is <= prev node, return False.
        """
        return self._is_bst(root)

    def _is_bst(self, node):
        # if node is None, return True
        if node is None:
            return True

        # left traversal
        if not self._is_bst(node.left):
            return False

        # if prev node is set and prev node value >= current node, return False
        if not self.prev:
            if self.prev.val >= node.val:
                return False

        # set the prev node to current node
        self.prev = node

        # right traversal
        if not self._is_bst(node.right):
            return False

        # if left and right is done and there is no invalid node, return True
        return True
# @lc code=end
