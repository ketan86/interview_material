#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        Runtime: 32 ms, faster than 87.16%

        Complete tree will have all levels filled except last with nodes
        filled from left to right.

        check when null node is found, all nodes are that node are null.
                     1
                2          3
             4     5     6    7
            8 9 10 11 12 13 n  n
          15
        """
        queue = deque()
        queue.append(root)
        # null flag for entire tree
        null_node = False
        while queue:
            node = queue.popleft()
            # when node is null, we found the first null node
            if not node:
                null_node = True
            else:
                # if prev node was null, it's not complete when node is found
                # after null node.
                if null_node:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True

# @lc code=end

