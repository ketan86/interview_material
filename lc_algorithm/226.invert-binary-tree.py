#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (62.54%)
# Likes:    3692
# Dislikes: 61
# Total Accepted:    565.4K
# Total Submissions: 866.4K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
#
# Output:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
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
    def invertTree(self, root):
        """Runtime: 32 ms, faster than 60.48% """
        def dfs(node):
            # if node is none, return
            if not node:
                return
            # set right node to left and left node to right in recurssion
            node.left, node.right = dfs(node.right), dfs(node.left)
            # return the node.
            return node

        return dfs(root)

# @lc code=end
