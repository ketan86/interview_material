#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:


# Input: root = [5, 3, 6, 2, 4, null, 7], k = 9
# Output: true
# Example 2:


# Input: root = [5, 3, 6, 2, 4, null, 7], k = 28
# Output: false
# Example 3:

# Input: root = [2, 1, 3], k = 4
# Output: true
# Example 4:

# Input: root = [2, 1, 3], k = 1
# Output: false
# Example 5:

# Input: root = [2, 1, 3], k = 3
# Output: true


# Constraints:

# The number of nodes in the tree is in the range[1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        # create sorted in order list
        in_order_list = []
        self.in_order(root, in_order_list)

        i = 0
        j = len(in_order_list) - 1

        while i < j:
            node_sum = in_order_list[i] + in_order_list[j]
            if node_sum > k:
                j -= 1
            elif node_sum < k:
                i += 1
            else:
                return True
        return False

    def in_order(self, node, in_order_list):
        if not node:
            return
        self.in_order(node.left, in_order_list)
        in_order_list.append(node.val)
        self.in_order(node.right, in_order_list)

# @lc code=end
