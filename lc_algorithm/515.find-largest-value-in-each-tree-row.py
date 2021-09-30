#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode):
        result = []

        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level = len(queue)
            max_node = float('-inf')
            for _ in range(level):
                node = queue.popleft()
                max_node = max(max_node, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_node)

        return result
# @lc code=end
