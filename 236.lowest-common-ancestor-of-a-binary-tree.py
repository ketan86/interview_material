#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (43.71%)
# Likes:    4293
# Dislikes: 181
# Total Accepted:    516.6K
# Total Submissions: 1.1M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
#
#
# Note:
#
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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
        """Runtime: 72 ms, faster than 65.75% """
        def dfs(root, p, q):
            # if root not is none, return None
            if not root:
                return

            # if node value is either left or right, return the root node.
            if root.val == p.val or root.val == q.val:
                return root

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            # if we find p and q in both left and right (does not matter
            # wether it's in right or left), current root is the LCA.
            if left and right:
                return root

            # if p and q are found only in left, root would move to left.
            if left:
                return left

            # if p and q are found only in right, root would move to right.
            if right:
                return right

        return dfs(root, p, q)

# @lc code=end
