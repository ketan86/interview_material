#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (76.68%)
# Likes:    701
# Dislikes: 68
# Total Accepted:    94.2K
# Total Submissions: 118.8K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
#
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
#
# For example, 
#
#
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
#
#
# You can return this binary search tree:
#
#
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
#
#
# This tree is also valid:
#
#
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \
# ⁠   1   3
# ⁠        \
# ⁠         4
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
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        self.insert(root, val)
        return root

    def insert(self, node, val):
        if node is not None:
            if val < node.val:
                # go left
                if node.left is not None:
                    self.insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                # go right
                if node.right is not None:
                    self.insert(node.right, val)
                else:
                    node.right = TreeNode(val)

# @lc code=end
