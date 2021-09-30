#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """Runtime: 360 ms, faster than 54.14%
        
        - Inorder traversal gives sorted values.
        - Binary search to find the mid and divide the in_order nodes to
        left and right sub tree.

        Time -> O(n)
        Space -> O(n)
        """
        in_order_list = []
        def in_order(node):
            if node:
                in_order(node.left)
                in_order_list.append(node)
                in_order(node.right)
        
        def balance(left, right):
            if left <= right:
                mid = left + (right - left) // 2 
                node = TreeNode(in_order_list[mid].val)
                node.left = balance(left, right-1)
                node.right = balance(left+1, right)
                return node 

        in_order(root)
        return balance(0, len(in_order_list) - 1)
# @lc code=end

