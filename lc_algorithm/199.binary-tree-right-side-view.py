#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root):
        """Runtime: 32 ms, faster than 64.90%"""
        result = []
        if not root:
            return result

        # queue for bfs
        queue = deque()
        queue.append(root)

        while queue:
            levels = len(queue)
            for level in range(levels):
                node = queue.popleft()
                # if we at the last level, capture the element in the result
                if level == levels - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# @lc code=end
