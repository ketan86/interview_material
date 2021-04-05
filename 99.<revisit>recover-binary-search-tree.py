#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (35.43%)
# Likes:    1322
# Dislikes: 67
# Total Accepted:    153.3K
# Total Submissions: 400.7K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
#
# Input: [1,3,null,null,2]
#
# 1
# /
# 3
# \
# 2
#
# Output: [3,1,null,null,2]
#
# 3
# /
# 1
# \
# 2
#
#
# Example 2:
#
#
# Input: [3,1,4,null,null,2]
#
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
#
# Output: [2,1,4,null,null,3]
#
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
#
#
# Follow up:
#
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # class variables to store the first, second and prev nodes.
    # KEY:= first node = prev node when curr node val < prev node val
    # KEY:= second node = current node when curr node val < prev node val
    first = None
    second = None
    prev = None

    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        # during in order traversal, if we find a node where prev node val
        # is greater than current node, we find the first node that needs to
        # be swapped. later, when current node value is less than prev node,
        # we find the current node as second node that (value) needs be
        # swapped with first node value.
        def in_order(node):
            # if node is None, return
            if node is None:
                return
            # traverse left node
            in_order(node.left)
            # we are at the first node, and if prev node is None, go to next
            # node. if prev node value is not none, compare the current node.
            # if prev node value > current node value, and first node is not
            # found, set prev node to first node. and current node to second
            # node.

            # Here we are taking care of two cases.
            # 1. -> 1,5,3,4,2,6 (first node is 5 and second is 2)
            #    prev(5)^   ^curr(2)
            # 2. -> 2,1,3,4,5,6 (first node is 2 and second is 1)
            if self.prev is not None:
                if self.prev.val > node.val:
                    if self.first is None:
                        self.first = self.prev
                    # we are keep setting the current node to second even for
                    # case 1 to take care of the generic case (1 and 2)
                    self.second = node
            # set prev node to current node
            self.prev = node
            # traverse right node
            in_order(node.right)

        # in order traversal
        in_order(root)

        # swap values of first and second node.
        if self.first is not None and self.second is not None:
            self.first.val, self.second.val = self.second.val, self.first.val


# @lc code=end
