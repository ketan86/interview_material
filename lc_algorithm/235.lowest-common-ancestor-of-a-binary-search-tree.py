#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (48.74%)
# Likes:    2307
# Dislikes: 111
# Total Accepted:    426.3K
# Total Submissions: 847.7K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
#
# Constraints:
#
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """Runtime: 80 ms, faster than 47.31%"""
        # NOTE: use BST property to decide if root is current root or it's
        # in left or right.

        # if not root, return None
        if not root:
            return

        # if both p and q are less than the current root val, root would
        # be in the left.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # if both p and q are greater than the current root val, root would
        # be in the right.
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # if p is on left and q on right, root is current root.
        else:
            return root

    def lowestCommonAncestorIterative(self, root, p, q):
        # use BST property to decide if root is current root or it's
        # in left or right.

        while root:
            # if both p and q are less than the current root val, root would
            # be in the left.
            if p.val < root.val and q.val < root.val:
                root = root.left
            # if both p and q are greater than the current root val, root would
            # be in the right.
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # if p is on left and q on right, root is current root.
            else:
                return root

    def lowestCommonAncestor(self, root, p, q):
        # if not root, return None
        if not root:
            return

        # if root's value is equal to p or q, return the root node
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if p and q found on the left and right of the current root, root
        # is current root.
        if left and right:
            return root
        # if p and q found in left of the root, root would move to left
        if left:
            return left
        # if p and q found on right of the root, root would move to right
        if right:
            return right

# @lc code=end
