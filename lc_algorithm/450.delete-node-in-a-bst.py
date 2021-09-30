#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
"""
450. Delete Node in a BST
Medium

3280

115

Add to List

Share
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?

 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105


"""

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        """Runtime: 76 ms, faster than 61.37%

        Time -> O(log n)
        Space -> O(h)
        """
        if not root:
            return root

        # if key is greater than roo, go right else left
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # if node is leaf node
            if not root.left and not root.right:
                root = None

            # if node has left child
            elif not root.left:
                root = root.right

            # if not has right child
            elif not root.right:
                root = root.left

            else:
                # go one step right and then all the way left
                curr = root.right
                while curr.left:
                    curr = curr.left

                # update current root value with smallest right value found
                root.val = curr.val
                # delete smallest value in right using delete node function.
                root.right = self.deleteNode(root.right, curr.val)
                
        return root
# @lc code=end
