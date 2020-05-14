#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (47.46%)
# Likes:    2407
# Dislikes: 297
# Total Accepted:    322.6K
# Total Submissions: 678.1K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#

# @lc code=start
# pylint: skip-file
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # store head and tail pointers
    head = None
    tail = None
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.

        We can flattern the binary tree on either side.
        """
        # if not root, return none
        if not root:
            return root
        
        # dfs traversal
        def dfs(node):
            if not node:
                return
            
            # before updating the right of the tail node, we have to
            # store the right in temp variable so we don't loose the
            # ref when tail.right is set to current node.

            # NOTE:: If we have to flattern the tree on left side, we
            # could store the left node.
            right = node.right

            # if tail node is none, it's a first node. set head and tail
            if not self.tail:
                self.head = node
            # else,
            # 1. set last tail node's right to current node
            # 2. set last tail node's left to cyrrent node 
            else:
                self.tail.right = node
                self.tail.left = None

            # move tail to last node
            self.tail = node

            # left and right traversal
            dfs(node.left)
            dfs(right)

        dfs(root)
        return self.head

# t = TreeNode(1)
# t.left = TreeNode(2)
# t.right = TreeNode(5)
# t.left.left = TreeNode(3)
# t.left.right = TreeNode(4)
# t.right.right = TreeNode(6)
# head = Solution().flatten(t)
# import pdb;pdb.set_trace()
# @lc code=end

