#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (64.84%)
# Likes:    2778
# Dislikes: 81
# Total Accepted:    878.7K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
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
    def maxDepth2ndSimple(self, root):
        """Runtime: 40 ms, faster than 76.55% """

        # max depth of the binary tree is,
        # max(left sub tree height, right sub tree height)

        def dfs(node):
            # if node is none, return the max_depth
            if not node:
                return 0

            # find the max(left,right) + 1 (to add current node)
            return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)

    def maxDepth(self, root):
        # max depth of the binary tree is,
        # max(left sub tree height, right sub tree height)
        max_depth = 0

        def dfs(node, max_depth):
            # if node is none, return the max_depth
            if node is None:
                return max_depth

            # find the max(left,right) + 1 (to add current node)
            max_depth = max(
                dfs(node.left, max_depth),
                dfs(node.right, max_depth)
            ) + 1

            return max_depth

        return dfs(root, max_depth)


# @lc code=end
