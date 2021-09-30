#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Runtime: 44 ms, faster than 73.99%"""
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            # find the depth of the subtree
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # choose the max depth of the left subtree and right subtree.
            self.diameter = max(self.diameter, left_depth + right_depth)

            # max depth by adding the current node
            return 1 + max(left_depth, right_depth)

        depth(root)

        return self.diameter

# @lc code=end

