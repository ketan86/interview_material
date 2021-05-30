# Given the root of a binary search tree and a target value, return the value in
# the BST that is closest to the target.


# Example 1:

#       4
#      /  \
#     2   5
#   /  \
#  1   3
#

# Input: root = [4, 2, 5, 1, 3], target = 3.714286
# Output: 4
# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range[1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root, target):
        """
        Runtime: 40 ms, faster than 64.37%

        """
        # maintain closest diff and closest node
        self.closest_diff = float('inf')
        self.closest_node = root.val

        def dfs(node):
            # if node is None, return
            if not node:
                return

            # find the min diff so far
            diff = min(self.closest_diff, abs(node.val - target))

            # if diff is not same as prev, update clostest node and diff
            if diff != self.closest_diff:
                self.closest_node = node.val
                self.closest_diff = diff

            # BST so go left if target is less than node else right
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)

        return self.closest_node
