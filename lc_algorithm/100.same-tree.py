#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (52.20%)
# Likes:    2385
# Dislikes: 67
# Total Accepted:    601.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
#
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
#
# Example 1:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
#
# ⁠       [1,2,3],   [1,2,3]
#
# Output: true
#
#
# Example 2:
#
#
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
#
# ⁠       [1,2],     [1,null,2]
#
# Output: false
#
#
# Example 3:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
#
# ⁠       [1,2,1],   [1,1,2]
#
# Output: false
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        # if both nodes are node, we are the the leaf node of both
        # trees so they are considered same.
        if not p and not q:
            return True
        # if either p or q is none, trees are not same.
        if (not p and q) or (not q and p):
            return False

        # if values are not same, return False
        if p.val != q.val:
            return False

        # if any nodes in the left of the both trees are not same or
        # any nodes in the right of the both trees are not same,
        # trees are not same.
        return self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)


# @lc code=end
