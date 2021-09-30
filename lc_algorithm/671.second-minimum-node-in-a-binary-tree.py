#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
# Easy
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally,
# the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in
# the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output - 1 instead.


# Example 1:


# Input: root = [2, 2, 5, null, null, 5, 7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# Example 2:


# Input: root = [2, 2, 2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.


# Constraints:

# The number of nodes in the tree is in the range[1, 25].
# 1 <= Node.val <= 231 - 1
# @lc code=start
# Definition for a binary tree node.


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # Time Complexity -> O(N)
        # Space Compexity -> O(N)
        queue = deque()
        queue.append(root)

        # define first and second min values
        min_values = [float('inf'), float('inf')]

        # iterate over the tree
        while queue:
            node = queue.popleft()
            # if node value is less than equal to first values, set first
            # value. else go and set second value
            if node.val <= min_values[0]:
                min_values[0] = node.val
            elif node.val <= min_values[1]:
                min_values[1] = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return min_values[1] if min_values[1] != float('inf') else -1


# @lc code=end
