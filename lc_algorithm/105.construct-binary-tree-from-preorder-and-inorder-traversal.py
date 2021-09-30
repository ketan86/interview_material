#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (46.89%)
# Likes:    3821
# Dislikes: 103
# Total Accepted:    389.3K
# Total Submissions: 788.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_index = 0
        self.in_index_map = {}

    def buildTree(self, preorder, inorder):
        """
        Runtime: 52 ms, faster than 95.99%

        recursively build the binary tree using the preorder and inorder
        lists.
        Inorder  -> [Left Root Right]
                    root can not be found using the only inorder since root
                    is in the middle of the list.
        Preorder -> [Root Left Right]
                    Since root is in the begining of the list, we can then
                    find the left and right nodes by checking the left and
                    right side of the inorder root node.

        For ex, [3, 9, 20, 15, 7] -> pre [root, left, right]
                [9, 3, 15, 20, 7] -> in  [left, root, right]

                              root-> 3 -> pre [9, 3, 15, 20, 7]
                                    find(in, 3)
                       left of 3 /             \ right of 3
                        9 -> pre [9]        20 -> pre [15,20,7]
                          find(in, 9)         find(in, 20)
                            / \        left of 20 /      \ right of 20
                           x   x        15 -> pre [] 7 -> pre []
                                            /    \       /    \
                                           x     x      x      x
                1. create a root node using the first index of the preorder list
                2. find the root node in the inorder list.
                3. left node of the root will be on the left list of inorder
                   root node. -> start to index - 1
                4. right node of the root will be on the right list of the inorder
                   root node. -> index += 1 to end

        """
        # populate the value to index map from the inorder list.
        for i in range(len(inorder)):
            self.in_index_map[inorder[i]] = i

        return self.build_efficient(preorder, in_start=0, in_end=len(preorder) - 1)

    def build_efficient(self, preorder, in_start, in_end):
        # if start is greater than end node, there is no left or right node.
        # return
        if in_start > in_end:
            return

        # create root node by selecting preorder item
        root = TreeNode(preorder[self.pre_index])

        # increment the pre index
        self.pre_index += 1

        # find the index of the root node value from the map. O(1)
        index = self.in_index_map[root.val]

        # build left and right nodes of the root node by searching left
        # and right list of the root node of the inorder list.
        root.left = self.build_efficient(preorder, in_start, index - 1)
        root.right = self.build_efficient(preorder, index + 1, in_end)

        return root

    # def build(self, preorder, inorder, in_start, in_end):
    #     # if start is greater than end node, there is no left or right node.
    #     # return None.
    #     if in_start > in_end:
    #         return None

    #     # create root node by selecting preorder item
    #     root = TreeNode(preorder[self.pre_index])

    #     # increment the pre index
    #     self.pre_index += 1

    #     # find the index of the root node in the inorder list. O(n)
    #     index = self.search_index(root, inorder, in_start, in_end)

    #     # build left and right nodes of the root node by searching left
    #     # and right list of the root node of the inorder list.
    #     root.left = self.build(
    #         preorder, inorder, in_start, index - 1)
    #     root.right = self.build(
    #         preorder, inorder, index + 1, in_end)

    #     return root

    # def search_index(self, node, inorder, start, end):
    #     # find the node value in the inorder list
    #     # linear search. O(n)
    #     for i in range(start, end + 1):
    #         if node.val == inorder[i]:
    #             return i
    #     return start

# print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
# @lc code=end
