#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            level_nodes = len(queue)
            prev_node = None
            for i in range(level_nodes):
                node = queue.popleft()
                # if not first node
                if i > 0:
                    prev_node.next = node

                prev_node = node
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root

# @lc code=end
