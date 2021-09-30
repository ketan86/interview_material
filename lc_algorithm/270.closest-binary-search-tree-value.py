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

        for a balanced tree: 
        h = log(n)
        hence o(h) = o(log n)

        O(H) -> Height of the tree.

        """
        # maintain closest distance and closest node
        self.closest_distance = float('inf')
        self.closest_node = root.val

        def dfs(node):
            # if node is None, return
            if not node:
                return

            # find the min distance so far
            distance = min(self.closest_distance, abs(node.val - target))

            # if distance is not same as prev, update clostest node and distance
            if distance != self.closest_distance:
                self.closest_node = node.val
                self.closest_distance = distance

            # BST so go left if target is less than node else right
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)

        return self.closest_node
