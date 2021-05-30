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
    """Runtime: 140 ms, faster than 27.43%"""

    def insertIntoBST(self, root, val):
        # if root node is none, return new tree node
        if not root:
            return TreeNode(val)
        node = root

        def dfs(node, val):
            # if node is none, return new node that will be set
            # either on left or right of it's parent
            if not node:
                return TreeNode(val)

            # value is less than the root node value, go left else right
            if val < node.val:
                # set returned node (either new or left/right of the curr node)
                node.left = dfs(node.left, val)
            else:
                node.right = dfs(node.right, val)

            # return current node to keep the tree intact
            return node

        dfs(node, val)

        return root
# @lc code=end
