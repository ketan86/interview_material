#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (33.59%)
# Likes:    4128
# Dislikes: 311
# Total Accepted:    398.3K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# Output: 42
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
class Solution:
    def maxPathSum(self, root):
        # initialize max_path_sum to neg infinite because node contains
        # negative values too.
        max_path_sum = float('-inf')

        def dfs(node):
            nonlocal max_path_sum
            # if node is node, return -inf
            if not node:
                return float('-inf')

            # find the max path sum of the left node and right node
            # if either left or right is negative, it will reduce
            # the path sum when added to node.val so reset to 0.
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # max path sum is the max of max path sum and node + left + right
            # we dont have to consider node, node+ left, node+ right because,
            # if left or right was negative, it would be set to 0 and hence,
            # all four conditions are satisfied.
            # 1. node.val                   <- both left and right max are -ve
            # 2. node.val + left_max        <- right max is -ve
            # 3. node.val + right_max       <- left max is -ve
            # 4. node.val + left_max + right_max  <- none are negative
            max_path_sum = max(
                max_path_sum,
                node.val + left_max + right_max
            )

            # current node can only add either left path or right path.
            # and also the max of both path so add max of left and right
            # to current node val.
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_path_sum


# @lc code=end
