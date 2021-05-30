#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (53.10%)
# Likes:    3375
# Dislikes: 84
# Total Accepted:    659.8K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
from collections import deque


class Solution:
    """Runtime: 36 ms, faster than 63.12%"""

    def levelOrder(self, root):
        result = []
        # if root node is None, return result
        if not root:
            return result

        # queue for bfs
        queue = deque()
        queue.append(root)

        # iterate over the queue by level
        while queue:
            # find the number of nodes and iterate over them
            # and store them in the level result.
            number_of_nodes = len(queue)
            level_result = []
            for _ in range(number_of_nodes):
                # pop the node and store the result
                node = queue.popleft()
                level_result.append(node.val)
                # if node has a left child, put it in the queue.
                if node.left:
                    queue.append(node.left)
                # if node has a right child, put it in the queue.
                if node.right:
                    queue.append(node.right)

            # save level results in the main result.
            result.append(level_result)

        return result

# @lc code=end
