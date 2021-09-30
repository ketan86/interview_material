#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """Runtime: 36 ms, faster than 58.80%"""
        return self.are_mirror(root, root)

    def are_mirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t2 or not t2:
            return False

        return (
            t1.val == t2.val and
            self.are_mirror(t1.left, t2.right) and
            self.are_mirror(t1.right, t2.left)
        )


# @lc code=end
