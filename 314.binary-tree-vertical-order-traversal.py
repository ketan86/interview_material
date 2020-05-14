#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (43.93%)
# Likes:    896
# Dislikes: 161
# Total Accepted:    107.2K
# Total Submissions: 243.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the vertical order traversal of its nodes'
# values. (ie, from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left to
# right.
# 
# Examples 1:
# 
# 
# Input: [3,9,20,null,null,15,7]
# 
# ⁠  3
# ⁠ /\
# ⁠/  \
# ⁠9  20
# ⁠   /\
# ⁠  /  \
# ⁠ 15   7 
# 
# Output:
# 
# [
# ⁠ [9],
# ⁠ [3,15],
# ⁠ [20],
# ⁠ [7]
# ]
# 
# 
# Examples 2:
# 
# 
# Input: [3,9,8,4,0,1,7]
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7 
# 
# Output:
# 
# [
# ⁠ [4],
# ⁠ [9],
# ⁠ [3,0,1],
# ⁠ [8],
# ⁠ [7]
# ]
# 
# 
# Examples 3:
# 
# 
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left
# child is 5)
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7
# ⁠   /\
# ⁠  /  \
# ⁠  5   2
# 
# Output:
# 
# [
# ⁠ [4],
# ⁠ [9,5],
# ⁠ [3,0,1],
# ⁠ [8,2],
# ⁠ [7]
# ]
# 
#

# @lc code=start
# pylint: skip-file
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root):
        """
        This problem requires storing all nodes vertically in list so if we
        store all the nodes at each level in a map, it will have final
        results storing each vertical level with list of nodes.

        col/row    -1   0   +1   +2
            0           3
                     /       \
            1       9        20
                        /         \
            2           15        7

        
        using the above grid, we can start with storing the root node with
        column value as 0, then for each left and right node of the root,
        we can decrement of increment the column value. we are also storing
        the node in the map based on the column value.
        """
        if not root:
            return []
        # queue for dfs
        queue = deque()
        # map to store the list of node by column
        d = defaultdict(list)
        # append root node and mark the column as 0
        queue.append((root,0))
        # append the root node on column 0 key
        d[0].append(root.val)
        while queue:
            level = len(queue)
            for i in range(level):
                # pop the node and column value
                node, column = queue.popleft()
                if node.left:
                    # append left node to the list of nodes where column value
                    # is equal to root node column value - 1
                    d[column-1].append(node.left.val)
                    queue.append((node.left, column-1))
                if node.right:
                    # append right node to the list of nodes where column value
                    # is equal to root node column value + 1
                    d[column+1].append(node.right.val)
                    queue.append((node.right, column+1))

        # sort the dict by key and return the results.
        result = []
        for k, v in sorted(d.items()):
            result.append(v)

        return result
        

# t = TreeNode(3)
# t.left = TreeNode(9)
# t.right = TreeNode(20)
# t.right.left = TreeNode(15)
# t.right.right = TreeNode(7)
# print(Solution().verticalOrder(t))
# @lc code=end

