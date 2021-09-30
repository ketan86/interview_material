"""
285. Inorder Successor in BST
Medium

1650

72

Add to List

Share
Given the root of a binary search tree and a node p in it, return the in-order
successor of that node in the BST. If the given node has no in-order successor
in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return
value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer
is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
Accepted
208,452
Submissions
471,299

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        O(n) -> find inorder traversal and then choose the successor.
        O(log n) -> because it's BST we can find p in log(n) search.
            - [1,2,3,4,5,6]
                       ^
               - when p is in left, current node (5) can be a successor 
                    so store it.
               - when p is in right, we don't know who will become
                    successor.
        """

        # if p not found, we need to return None
        successor = None

        # traverse a tree
        while root:
            # if node is on right, do not update the successor
            if p.val >= root.val:
                root = root.right
            else:
                # if node is on left, save the successor
                successor = root
                root = root.left

        # return successor
        return successor
